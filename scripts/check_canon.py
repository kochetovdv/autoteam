#!/usr/bin/env python3
"""Read-only, standard-library checks for a complete English/Russian canon bundle.

Only declared bundle paths are read. Fingerprints and comparisons preserve exact
bytes (including line endings); timestamps and files outside the bundle do not
participate. This checks files and metadata, not the quality of their prose.
Metadata supports simple text scalars; Markdown supports common inline links,
including angle-bracket destinations and optional titles. These are not full
YAML/Markdown parsers, and link anchors are not checked.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
from urllib.parse import unquote, urlsplit


CONTENT_ROOTS = ("skills", "docs", "templates")
ENTRY_DOCUMENTS = ("README.md", "CHANGELOG.md")
SUPPORT_FILES = ("scripts/check_canon.py",)
LOCALES = {"en": ".", "ru": "ru"}
MANIFEST_KEYS = {"schema_version", "version", "canonical_language", "locales",
                 "content_roots", "entry_documents", "support_files"}
SEMVER = re.compile(
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?\Z", re.ASCII)
SKILL_NAME = re.compile(r"autoteam-[a-z0-9]+(?:-[a-z0-9]+)*\Z")
SKILL_REFERENCE = re.compile(r"(?<![A-Za-z0-9_-])autoteam-[a-z0-9]+(?:-[a-z0-9]+)*")
INLINE_LINK = re.compile(
    r"!?\[[^\]\n]*\]\(\s*("
    r"""<[^>\n]+>(?:[ \t]+(?:"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*'|\([^)\n]*\)))?"""
    r"|[^)\n]*?)\s*\)")
FINGERPRINT_METHOD = (
    "SHA256 of sorted UTF-8 relative paths and raw file bytes, each length-prefixed "
    "with 8 big-endian bytes; prefix autoteam-canon-bundle-v1\\0; "
    "exact bytes, no timestamps or newline normalization")


def ignored(name):
    return name in {".git", "__pycache__"} or name.lower().endswith((".pyc", ".pyo"))


def is_reparse(info):
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))


def manifest_errors(value):
    if not isinstance(value, dict):
        return ["canon.json must contain an object"]
    errors = []
    if set(value) != MANIFEST_KEYS:
        errors.append("canon.json has missing or unknown schema fields")
    if type(value.get("schema_version")) is not int or value["schema_version"] != 1:
        errors.append("canon.json schema_version must be 1")
    if not isinstance(value.get("version"), str) or not SEMVER.fullmatch(value["version"]):
        errors.append("canon.json version must be a semantic version")
    if value.get("canonical_language") != "en" or value.get("locales") != LOCALES:
        errors.append("canon.json must declare canonical English and locales en='.', ru='ru'")
    for field, required in (("content_roots", CONTENT_ROOTS),
                            ("entry_documents", ENTRY_DOCUMENTS),
                            ("support_files", SUPPORT_FILES)):
        actual = value.get(field)
        if not isinstance(actual, list) or any(not isinstance(p, str) for p in actual) \
                or sorted(actual) != sorted(required):
            errors.append("canon.json %s must declare exactly %s" % (field, list(required)))
    return errors


def fingerprint(files):
    digest = hashlib.sha256(b"autoteam-canon-bundle-v1\0")
    for relative, data in sorted(files.items()):
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def frontmatter(text):
    """Read simple plain, quoted, or indented block scalars without loading YAML."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, "missing opening frontmatter delimiter"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, "missing closing frontmatter delimiter"
    fields = {}
    for index, line in enumerate(lines[1:end], 1):
        match = re.match(r"^(name|description):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.groups()
        if key in fields:
            return {}, "duplicate frontmatter field: " + key
        if not value.startswith(("\"", "'")):
            value = re.split(r"(?:^|\s)#", value, maxsplit=1)[0].rstrip()
        if value in {"|", ">", "|-", ">-", "|+", ">+"}:
            continuation = []
            for next_line in lines[index + 1:end]:
                if next_line and not next_line[0].isspace():
                    break
                continuation.append(next_line.strip())
            value = " ".join(continuation).strip()
        elif value.startswith(("\"", "'")):
            quoted = re.fullmatch(
                r"""(?:"(?P<double>(?:\\.|[^"\\])*)"|'(?P<single>(?:''|[^'])*)')"""
                r"(?:[ \t]+#.*)?[ \t]*", value)
            if quoted is None:
                return {}, "frontmatter name and description must be simple text scalars"
            value = (quoted.group("double") if quoted.group("double") is not None
                     else quoted.group("single").replace("''", "'")).strip()
        elif re.search(r":(?:\s|$)", value) \
                or value.startswith(("[", "{", "!", "&", "*")) \
                or value in {"null", "Null", "NULL", "~", "true", "false"}:
            return {}, "frontmatter name and description must be simple text scalars"
        fields[key] = value
    if not fields.get("name") or not fields.get("description"):
        return fields, "frontmatter requires nonempty name and description"
    return fields, None


class Bundle:
    def __init__(self, root):
        self.root = Path(os.path.abspath(root))
        self.errors = []
        self.files = {}
        self.version = None
        self.skills = {"en": set(), "ru": set()}

    def error(self, relative, reason):
        self.errors.append("%s: %s" % (relative, reason))

    def safe_info(self, relative):
        """lstat every component before opening; never traverse a link/junction."""
        current = self.root
        parts = () if relative == "." else PurePosixPath(relative).parts
        try:
            for part in (None,) + parts:
                if part is not None:
                    current = current / part
                info = current.lstat()
                if is_reparse(info):
                    self.error(relative, "symlink or reparse point is forbidden")
                    return None
            current.resolve(strict=True).relative_to(self.root.resolve(strict=True))
            return info
        except (OSError, ValueError) as exc:
            self.error(relative, "missing, inaccessible, or outside bundle (%s)" % exc)
            return None

    def read_file(self, relative):
        info = self.safe_info(relative)
        if info is None:
            return
        if not stat.S_ISREG(info.st_mode):
            self.error(relative, "expected a regular file")
            return
        try:
            data = (self.root / relative).read_bytes()
        except OSError as exc:
            self.error(relative, "cannot read file (%s)" % exc)
            return
        self.files[relative] = data
        if not data.strip():
            self.error(relative, "empty file")

    def walk(self, relative):
        info = self.safe_info(relative)
        if info is None:
            return
        if not stat.S_ISDIR(info.st_mode):
            self.error(relative, "expected a directory")
            return
        before = len(self.files)
        try:
            entries = sorted((self.root / relative).iterdir(), key=lambda p: p.name)
        except OSError as exc:
            self.error(relative, "cannot list directory (%s)" % exc)
            return
        for entry in entries:
            if ignored(entry.name):
                continue
            child = relative + "/" + entry.name
            child_info = self.safe_info(child)
            if child_info is None:
                continue
            if stat.S_ISDIR(child_info.st_mode):
                self.walk(child)
            else:
                self.read_file(child)
        if len(self.files) == before:
            self.error(relative, "empty content directory")

    def inspect(self):
        self.read_file("canon.json")
        try:
            manifest = json.loads(self.files.get("canon.json", b"").decode("utf-8-sig"))
            self.errors.extend(manifest_errors(manifest))
            if isinstance(manifest, dict):
                self.version = manifest.get("version")
        except (ValueError, UnicodeError) as exc:
            self.error("canon.json", "invalid JSON (%s)" % exc)
        # Fixed schema paths, even if a candidate tries to omit/redefine them.
        for locale, prefix in LOCALES.items():
            base = "" if prefix == "." else prefix + "/"
            for relative in ENTRY_DOCUMENTS:
                self.read_file(base + relative)
            for relative in CONTENT_ROOTS:
                self.walk(base + relative)
            skill_base = base + "skills/"
            direct_names = {PurePosixPath(p[len(skill_base):]).parts[0]
                            for p in self.files if p.startswith(skill_base)
                            and "/" in p[len(skill_base):]}
            for name in sorted(direct_names):
                skill_file = skill_base + name + "/SKILL.md"
                if not SKILL_NAME.fullmatch(name):
                    self.error(skill_base + name, "invalid autoteam skill directory name")
                elif skill_file not in self.files:
                    self.error(skill_file, "missing skill entry")
                else:
                    self.skills[locale].add(name)
            if not self.skills[locale]:
                self.error(skill_base, "no populated skills")
        for relative in SUPPORT_FILES:
            self.read_file(relative)
        english = {p for p in self.files if p in ENTRY_DOCUMENTS
                   or p.split("/", 1)[0] in CONTENT_ROOTS}
        russian = {p[3:] for p in self.files if p.startswith("ru/")}
        for relative in sorted(english - russian):
            self.error("ru/" + relative, "missing locale counterpart")
        for relative in sorted(russian - english):
            self.error("ru/" + relative, "extra locale content without English counterpart")
        known_skills = self.skills["en"]
        for relative, data in sorted(self.files.items()):
            if not relative.lower().endswith(".md"):
                continue
            try:
                text = data.decode("utf-8-sig")
            except UnicodeError:
                self.error(relative, "Markdown must be UTF-8")
                continue
            if PurePosixPath(relative).name == "SKILL.md":
                fields, problem = frontmatter(text)
                if problem:
                    self.error(relative, problem)
                if fields.get("name") != PurePosixPath(relative).parent.name:
                    self.error(relative, "frontmatter name must match its skill directory")
            for name in sorted(set(SKILL_REFERENCE.findall(text)) - known_skills):
                self.error(relative, "unknown autoteam skill reference: " + name)
            self.check_links(relative, text)
        return self

    def in_scope(self, relative):
        fixed = {"canon.json", *ENTRY_DOCUMENTS, *SUPPORT_FILES,
                 *("ru/" + p for p in ENTRY_DOCUMENTS)}
        folders = {*CONTENT_ROOTS, *("ru/" + p for p in CONTENT_ROOTS)}
        return relative == "." or relative in fixed or relative in folders \
            or any(relative.startswith(p + "/") for p in folders) \
            or any(p.startswith(relative + "/") for p in fixed | folders)

    def check_links(self, relative, text):
        # Fenced and inline code examples are not rendered Markdown links.
        prose, fence = [], None
        for line in text.splitlines():
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if marker:
                char = marker.group(1)[0]
                fence = None if fence == char else char if fence is None else fence
            elif fence is None:
                prose.append(re.sub(r"`+[^`\n]*`+", "", line))
        for match in INLINE_LINK.finditer("\n".join(prose)):
            value = match.group(1).strip()
            angle = re.match(r"^<([^>\n]+)>", value)
            target = angle.group(1) if angle else value.split(maxsplit=1)[0] if value else ""
            if not target or target.startswith("#") or target.startswith("//"):
                continue
            if re.match(r"^[A-Za-z]:", target) or target.startswith(("/", "\\")):
                self.error(relative, "absolute local link is forbidden: " + target)
                continue
            try:
                parsed = urlsplit(target)
            except ValueError:
                self.error(relative, "invalid link: " + target)
                continue
            if parsed.scheme:
                if parsed.scheme.lower() == "file":
                    self.error(relative, "local file URL is forbidden: " + target)
                continue
            path = unquote(parsed.path).replace("\\", "/")
            if not path:
                continue
            candidate = Path(os.path.abspath(self.root / PurePosixPath(relative).parent / path))
            try:
                normalized = candidate.relative_to(self.root).as_posix()
            except ValueError:
                self.error(relative, "link escapes bundle: " + target)
                continue
            if not self.in_scope(normalized):
                self.error(relative, "link outside declared bundle paths: " + target)
            elif self.safe_info(normalized) is None:
                self.error(relative, "broken or unsafe relative link: " + target)

    def report(self):
        return {"root": str(self.root), "ok": not self.errors, "version": self.version,
                "counts": {"files": len(self.files),
                           "markdown_files": sum(p.lower().endswith(".md") for p in self.files),
                           "skills": {k: len(v) for k, v in self.skills.items()}},
                "fingerprint": fingerprint(self.files) if not self.errors else None,
                "fingerprint_method": FINGERPRINT_METHOD,
                "errors": sorted(set(self.errors))}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--compare", type=Path, metavar="FULL_BUNDLE_ROOT",
                        help="require an exact-byte match to another complete bundle")
    args = parser.parse_args(argv)
    bundle = Bundle(args.root).inspect()
    report = bundle.report()
    if args.compare is not None:
        reference = Bundle(args.compare).inspect()
        missing = sorted(reference.files.keys() - bundle.files.keys())
        extra = sorted(bundle.files.keys() - reference.files.keys())
        different = sorted(p for p in bundle.files.keys() & reference.files.keys()
                           if bundle.files[p] != reference.files[p])
        report["comparison"] = {
            "root": str(reference.root), "ok": not (reference.errors or missing or extra or different),
            "missing_files": missing, "extra_files": extra, "different_files": different,
            "reference_fingerprint": reference.report()["fingerprint"],
            "reference_errors": sorted(set(reference.errors))}
        report["ok"] = report["ok"] and report["comparison"]["ok"]
    print(json.dumps(report, ensure_ascii=True, indent=2, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

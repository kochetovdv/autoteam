"""Observable CLI acceptance tests; every inspected bundle lives in a temp dir."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "scripts" / "check_canon.py"


def write(root, relative, text):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def fixture(root):
    manifest = {
        "schema_version": 1, "version": "1.6.0", "canonical_language": "en",
        "locales": {"en": ".", "ru": "ru"},
        "content_roots": ["skills", "docs", "templates"],
        "entry_documents": ["README.md", "CHANGELOG.md"],
        "support_files": ["scripts/check_canon.py"],
    }
    write(root, "canon.json", json.dumps(manifest) + "\n")
    for prefix in ("", "ru/"):
        write(root, prefix + "README.md", "# Canon\n\n[Guide](docs/guide.md#start)\n")
        write(root, prefix + "CHANGELOG.md", "# Changes\n\nVersion 1.6.0.\n")
        write(root, prefix + "skills/autoteam-example/SKILL.md",
              "---\nname: autoteam-example\ndescription: A useful example.\n---\n\n# Example\n")
        write(root, prefix + "docs/guide.md",
              "# Guide\n\nUse `autoteam-example`. [Home](../README.md).\n")
        write(root, prefix + "templates/task.md", "# Task\n\nRecord the next action.\n")
    write(root, "scripts/check_canon.py", "# Bundle support checker\n")
    return root


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.stat().st_mtime_ns, p.read_bytes())
            for p in root.rglob("*") if p.is_file()}


class CanonCliTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="autoteam-canon-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = fixture(Path(self.temporary.name) / "candidate")

    def run_check(self, root=None, compare=None):
        command = [sys.executable, str(CHECKER), "--root", str(root or self.root)]
        if compare is not None:
            command += ["--compare", str(compare)]
        result = subprocess.run(command, capture_output=True, text=True,
                                encoding="utf-8", env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
                                timeout=20)
        self.assertIn(result.returncode, (0, 1), result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["ok"], result.returncode == 0)
        return report

    def reject(self, fragment, **kwargs):
        report = self.run_check(**kwargs)
        self.assertFalse(report["ok"])
        self.assertTrue(any(fragment in error for error in report["errors"]), report)
        return report

    def test_complete_bundle_reports_stable_fingerprint_and_does_not_write(self):
        before = snapshot(self.root)
        first = self.run_check()
        second = self.run_check()
        self.assertTrue(first["ok"], first)
        self.assertEqual(first["version"], "1.6.0")
        self.assertEqual(first["counts"], {"files": 12, "markdown_files": 10,
                                          "skills": {"en": 1, "ru": 1}})
        self.assertEqual(first["fingerprint"], second["fingerprint"])
        self.assertEqual(len(first["fingerprint"]), 64)
        # Independently reconstruct the documented byte framing.
        digest = hashlib.sha256(b"autoteam-canon-bundle-v1\0")
        for relative, (_, data) in sorted(before.items()):
            name = relative.encode("utf-8")
            digest.update(len(name).to_bytes(8, "big") + name)
            digest.update(len(data).to_bytes(8, "big") + data)
        self.assertEqual(first["fingerprint"], digest.hexdigest())
        self.assertEqual(before, snapshot(self.root))

    def test_a_single_locale_installation_is_incomplete(self):
        shutil.rmtree(self.root / "ru")
        self.reject("missing locale counterpart")

    def test_broken_relative_link_and_outside_bundle_link_fail(self):
        write(self.root, "docs/guide.md", "# Guide\n\n[Missing](gone.md).\n")
        self.reject("broken or unsafe relative link")
        write(self.root, "docs/guide.md", "# Guide\n\n[Outside](../../secret.txt).\n")
        self.reject("link escapes bundle")

    def test_external_links_anchors_and_code_examples_are_not_local_files(self):
        write(self.root, "docs/guide.md",
              '# Guide\n[Web](https://example.invalid/x). [Email](mailto:a@example.invalid).\n'
              '[Anchor](#start). `[Example](absent.md)`\n```md\n[Example](absent.md)\n```\n')
        self.assertTrue(self.run_check()["ok"])

    def test_angle_link_with_spaces_and_title_checks_the_destination(self):
        filenames = ("space file.md", "copy(1).md", "copy (2).md")
        links = ('[Space](<space file.md> "A title").\n'
                 '[Copy](<copy(1).md> "A title").\n'
                 '[Copy with space](<copy (2).md> "A (title)").\n')
        for prefix in ("", "ru/"):
            for filename in filenames:
                write(self.root, prefix + "docs/" + filename, "# Destination\n")
            write(self.root, prefix + "docs/guide.md", "# Guide\n\n" + links)
        report = self.run_check()
        self.assertTrue(report["ok"], report)
        for prefix in ("", "ru/"):
            for filename in filenames:
                (self.root / (prefix + "docs/" + filename)).unlink()
        report = self.run_check()
        self.assertFalse(report["ok"])
        for filename in filenames:
            self.assertTrue(any("broken or unsafe relative link: " + filename in error
                                for error in report["errors"]), report)

    def test_empty_content_and_empty_files_fail(self):
        (self.root / "docs/guide.md").unlink()
        self.reject("empty content directory")
        write(self.root, "docs/guide.md", " \n\t")
        self.reject("empty file")

    def test_missing_metadata_and_wrong_skill_name_fail(self):
        skill = "skills/autoteam-example/SKILL.md"
        write(self.root, skill, "# No metadata\n")
        self.reject("frontmatter")
        write(self.root, skill, "---\nname: autoteam-example\n---\n# Missing description\n")
        self.reject("nonempty name and description")
        write(self.root, skill,
              "---\nname: autoteam-example\ndescription: # only a comment\n---\n# Missing\n")
        self.reject("nonempty name and description")
        write(self.root, skill, "---\nname: autoteam-wrong\ndescription: Example.\n---\n# Wrong\n")
        self.reject("name must match")

    def test_unknown_skill_reference_fails(self):
        write(self.root, "docs/guide.md", "# Guide\n\nUse `autoteam-nonexistent`.\n")
        self.reject("unknown autoteam skill reference: autoteam-nonexistent")

    def test_quoted_metadata_accepts_comments_and_literal_hashes(self):
        descriptions = (
            '"# literal: description" # trailing comment',
            "'# literal: description' # trailing comment",
            "'It''s a # literal: description' # trailing comment",
            r'"A \"quote\" # literal: description" # trailing comment',
        )
        for description in descriptions:
            with self.subTest(description=description):
                write(self.root, "skills/autoteam-example/SKILL.md",
                      '---\nname: "autoteam-example" # role name\n'
                      "description: " + description + "\n---\n\n# Example\n")
                report = self.run_check()
                self.assertTrue(report["ok"], report)

    def test_plain_metadata_rejects_yaml_mapping_separators(self):
        write(self.root, "skills/autoteam-example/SKILL.md",
              "---\nname: autoteam-example\ndescription: example: description\n---\n# Example\n")
        self.reject("frontmatter name and description must be simple text scalars")
        write(self.root, "skills/autoteam-example/SKILL.md",
              "---\nname: autoteam-example\ndescription: See https://example.invalid/guide.\n"
              "---\n# Example\n")
        report = self.run_check()
        self.assertTrue(report["ok"], report)

    def test_links_do_not_access_undeclared_local_files(self):
        write(self.root, "private.txt", "Outside the bundle inputs.\n")
        write(self.root, "docs/guide.md", "# Guide\n\n[Private](../private.txt).\n")
        self.reject("outside declared bundle paths")
        write(self.root, "docs/guide.md", "# Guide\n\n[Drive](C:private.txt).\n")
        self.reject("absolute local link is forbidden")

    def test_manifest_cannot_hide_missing_content_or_metadata(self):
        path = self.root / "canon.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["content_roots"] = ["skills", "templates"]
        write(self.root, "canon.json", json.dumps(manifest))
        shutil.rmtree(self.root / "docs")
        self.reject("content_roots must declare exactly")
        manifest["content_roots"] = ["skills", "docs", "templates"]
        del manifest["support_files"]
        write(self.root, "canon.json", json.dumps(manifest))
        self.reject("missing or unknown schema fields")

    def test_invalid_semantic_version_fails(self):
        path = self.root / "canon.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["version"] = "1.06.0"
        write(self.root, "canon.json", json.dumps(manifest))
        self.reject("semantic version")

    def test_extra_translated_content_fails(self):
        write(self.root, "ru/docs/extra.md", "# Extra translated file\n")
        self.reject("extra locale content")

    def test_compare_detects_missing_changed_extra_and_support_bytes(self):
        reference = Path(self.temporary.name) / "reference"
        shutil.copytree(self.root, reference)
        self.assertTrue(self.run_check(compare=reference)["ok"])
        (self.root / "templates/task.md").unlink()
        write(self.root, "docs/guide.md", "# Changed guide\n")
        write(self.root, "scripts/check_canon.py", "# Changed support checker\n")
        for prefix in ("", "ru/"):
            write(self.root, prefix + "docs/extra.md", "# Extra\n")
        report = self.run_check(compare=reference)
        self.assertFalse(report["ok"])
        comparison = report["comparison"]
        self.assertIn("templates/task.md", comparison["missing_files"])
        self.assertIn("docs/guide.md", comparison["different_files"])
        self.assertIn("scripts/check_canon.py", comparison["different_files"])
        self.assertEqual(comparison["extra_files"], ["docs/extra.md", "ru/docs/extra.md"])

    def test_compare_requires_a_complete_reference(self):
        reference = fixture(Path(self.temporary.name) / "reference")
        (reference / "ru/CHANGELOG.md").unlink()
        report = self.run_check(compare=reference)
        self.assertFalse(report["ok"])
        self.assertTrue(report["comparison"]["reference_errors"])

    def test_fingerprint_preserves_line_endings_and_ignores_unrelated_files(self):
        original = self.run_check()["fingerprint"]
        write(self.root, "unrelated/private.txt", "Do not read outside the declared bundle.\n")
        write(self.root, "docs/__pycache__/ignored.pyc", "Ignored cache.\n")
        self.assertEqual(self.run_check()["fingerprint"], original)
        data = (self.root / "docs/guide.md").read_bytes()
        (self.root / "docs/guide.md").write_bytes(data.replace(b"\n", b"\r\n"))
        self.assertNotEqual(self.run_check()["fingerprint"], original)

    def test_symlink_content_is_rejected_when_supported(self):
        target = self.root / "docs/alias.md"
        try:
            target.symlink_to(self.root / "docs/guide.md")
        except (OSError, NotImplementedError) as exc:
            self.skipTest("Symlinks unavailable on this host: %s" % exc)
        self.reject("symlink or reparse point")


if __name__ == "__main__":
    unittest.main()

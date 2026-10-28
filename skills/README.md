# Skills and the full bundle

Each `autoteam-*/SKILL.md` owns the purpose, essential constraints, and route for a responsibility. Supporting documents are read progressively. A focused skill provides local guidance; where it requires shared documents, those are dependencies, not optional background. Missing dependencies must not be reported as full-method compliance.

The complete method is one versioned bundle: `canon.json`, root entry documents, `skills/`, `docs/`, `templates/`, the maintained `ru/` counterparts, and the validation script. Keep a verified immutable snapshot for the cycle. Register skills from that snapshot where supported. If an environment needs discovery copies, bind them to that same snapshot and resolve shared references there; copying only skill folders is not a complete installation.

The project profile records the canon root, version/fingerprint, selected language, and environment registration locations. Do not update global user skills, a shared canon checkout, or active cycle instructions incidentally. `scripts/check_canon.py --compare <bundle-root>` checks a full copied bundle against this source; it does not install anything or prove agent behavior.

Method changes belong here; project commands, domain meanings, local prohibitions, model IDs, and visual references stay in the profile/overlay. Use `autoteam-retro` to propose a general lesson from project evidence. An explicit canon-edit assignment authorizes implementing that proposal.

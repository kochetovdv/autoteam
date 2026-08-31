---
name: autoteam-release
description: Release and incidents — mechanism from the project (git-push, CI/CD, serverless, runbook), smoke, rollback, statuses. Use for deploy, release, incident, staging.
---

# Release and incidents

The release mechanism is a property of the product, not of the canon. First learn how **this** project ships (onboarding / runbook): git push → platform; merge → CI/CD; serverless; compose over SSH; manual runbook. Don't copy another product's hosts, SSH, and pipelines.

**Input.** An assignment to release / an incident / a ready change set; the project's deploy mechanism. **Output.** A release with smoke evidence, a runbook entry for an incident. **Forbidden.** Wipe, force-anything, heavy operations under load, commit-push "while at it", made-up scope, other products' hosts; destructive git operations in the developer's local tree (`reset --hard`, `clean`); releasing from feature branches — the cut ships from the integration branch. **Evidence.** Smoke command + output (or a URL check after a platform deploy). **Stop.** No "ship it / go ahead" — change set ready plus one question; don't hang. Declaring production is the human's call. **Next.** An incident with a data boundary → `autoteam-architecture-review` queue. Don't stop someone else's scope.

## Invariants (under any mechanism)

- Know what ships: the change set, migrations yes/no, what not to do.
- Smoke after the release: the main path is alive, evidence by command or request.
- Rollback known **before** the release: git revert, previous image, platform rollback.
- Secrets separated per environment; prod secrets not in release logs.
- Destructive actions (lossy migration, wipe, recompute) — backup and explicit sign-off.

## Statuses and sign-off

If the project keeps patch files: `draft` → `ready` (written by the implementer) → `published` (written by the releaser after smoke; a different subagent, not the code's author). In git flow the PR / release tag plays the patch's role — don't duplicate statuses, follow the project.

"Ship it / go ahead" in the assignment = allowed for this cycle. Environments — names as in the project; staging ≠ declaring production. Canon: `docs/delivery/release.md`, `incidents.md`, `ci-flags.md`.

## Incident

Symptom → evidence → mitigation → cause → the same check again → runbook entry. Template `templates/incident.md`. Don't refactor prod "while at it".

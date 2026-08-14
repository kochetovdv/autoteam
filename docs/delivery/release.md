# Release (universal)

Do not copy another product's SSH, IPs, and ports. The product has its own runbook (`deploy/README.md` or equivalent).

## Environments

Typically: local → staging (pre-production; may be named differently in the product) → production. Names as in the project. Secrets are not shared.

## Patch / release

One agreed cut: what went in, which services to rebuild, migrations yes/no, smoke, rollback, **do not do**.

Patch statuses (if you keep files): `draft` → `ready` → `published`. Implementation writes `ready`. Release is a different subagent. `published` only after smoke.

## Approval

"Release it / go ahead" in the assignment = allowed for this cycle. No such phrase — patch stays `ready` plus one question, don't stall. The "declared production" gate is not one the human closes with a patch.

Default prohibitions: wiping volumes, force-recomputing data and aggregates, heavy OPTIMIZE under load, commit-push "while we're at it", invented scope.

## Incident

Short cycle: symptom → evidence (log, status, query) → mitigation → cause → runbook entry. Do not fix production by blind refactoring. Skill: `autoteam-release`. Template: `templates/incident.md`.

# Resources and run lifecycle

Accounts, access, environments, data and human actions, plus resources created or borrowed by a run. Money: `autoteam-budget`. Secret values never enter this file, snapshots or archives; use vault pointers only. Reuse the existing project ledger. Method: `docs/process/resource-lifecycle.md` in the verified canon snapshot. The rows below are unfilled examples, not actual resources.

| ID | Type / resource identity | Status | Owner / access pointer | Expiry / limit | Dependent work |
|---|---|---|---|---|---|
| R-<id> | account / access / environment / data / human action | have / needed / requested (date) | | | |

For each run-owned or borrowed resource, include these fields in the same ledger or its work item; do not maintain duplicate registries:

```markdown
Run / work item / owner:
Exact identity (absolute tree path, process/session ID, container, volume, port, etc.):
Ownership: created / delegated / borrowed (owner and permission):
Purpose / authorized actions:
Status: planned | active | outcome-unknown | cleanup_pending | cleaned | retained | transferred
Lock owner token / heartbeat / liveness evidence, when relevant:
Preserve before cleanup → safe changes / evidence / needed ignored files / verified recovery pointer:
Cleanup or retention rule → action / owner / trigger or deadline:
Last reconciliation / actual outcome / error / next action:
```

- Capture exact IDs before dependent use. Unknown creation outcome requires reconciliation before retry. One writer per isolated physical tree; file assignment alone is insufficient. Ownership transfers within the authorized task are explicit coordinator actions; unrelated owner conflicts go to the human.
- Reconcile at finish **and** on failure/recovery. Preserve retrievable changes and necessary sanitized evidence before deleting. Only owned worktrees with recoverable snapshots may be archived; preserve needed ignored files separately. Exclude raw secrets from bulk operations.
- Cleanup validates owner and resolved target anew. No blind prune, shared-volume deletion or stale-age deletion. Lock age prompts liveness checks; unknown liveness blocks a second writer. Only verified absence permits conditional atomic lock recovery.
- Failed cleanup stays `cleanup_pending` in state and handoff with owner and next check. Retained resources have an explicit reason, owner and removal condition. Monitor actions use the same lifecycle.
- A registry mismatch stops only work relying on that entry until record or reality is corrected. A missing resource blocks its dependents. Human-only actions enter the human queue with a concrete consequence; shared limit allocation requires its authorized owner's decision. Check expiry at acceptance.
- An unavailable source/tool/export is an open perimeter limitation with owner, affected conclusions and recheck trigger. Recheck at relevant checkpoints and after restoration. Say “this scope was not searched”, never “absent”. Close by revising dependent conclusions; include unresolved limitations in the handoff. The agent cannot silently narrow the assignment.

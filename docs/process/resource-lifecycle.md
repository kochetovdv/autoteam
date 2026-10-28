# Resource ownership, recovery and cleanup

Resources include worktrees, draft trees, processes, ports, containers, volumes, temporary databases, artifacts and scheduled monitor actions, as well as durable accounts and access. Use the project's existing ledger or [resources template](../../templates/resources.md); a short local run may keep the few lifecycle fields in its work item. Do not create a separate bureaucracy for every command.

## Claim before use

Before creating or using a resource, establish the authorized scope and record the cycle/run, owner, exact identity, purpose, allowed actions and cleanup or retention rule. Allocate the identity before creation where possible; when a provider assigns it, capture the returned ID immediately before dependent use. A creation attempt that times out is `outcome-unknown`: reconcile that attempt's identity before retrying. Borrowed resources name their real owner and permission; access does not transfer ownership. A missing prerequisite blocks dependent work, not the whole cycle.

Physical filesystem writers need isolated worktrees or draft/output trees. One writer owns a tree at a time, including documentation-only changes; disjoint file lists in a common working tree do not create physical isolation. Parallel authors return artifacts or commits from their own trees to an assigned integrator. Within the authorized task, the coordinator may explicitly transfer ownership after the old writer stops and the new owner acknowledges the tree and pending changes. An unrelated or unfamiliar owner is a conflict for the human; never take it over silently. See [work-items.md](work-items.md) for assignment and [assurance.md](assurance.md) for review boundaries.

Record exact worktree paths, process/session IDs, container IDs, port bindings and volume/database identities. Before changing or deleting them, revalidate identity and owner; a reused PID or port is not the resource originally created. Resolve filesystem cleanup targets to absolute paths and verify they stay within the owned directory. An ownership label is useful evidence but does not authorize operating on someone else's resource.

## Locks and leases

Acquire an exclusive cycle/tree lock atomically before any writer starts. Include cycle/run, unique owner token, claimed scope, host/session identity, acquisition time and heartbeat/lease information. All launch and recovery paths obey the same lock protocol; a document saying “one writer” without enforcement does not prevent a double launch.

An old timestamp or expired lease triggers a liveness check, never automatic stale-lock deletion. Check the recorded owner/session and active work using available local or provider evidence. Only verified owner absence permits a coordinated atomic release/reacquire, conditional on the lock still holding the same owner token. If the owner is live, continue only through its coordinator. If ownership or liveness is unknown, mark the affected work blocked and resolve it with the human; do not start a second writer. The holder releases its own lock by matching its token. Heartbeat loss alone does not prove owner death; a resumed writer must revalidate its lease before writing again. A verified handoff records the new owner without an unguarded gap.

## Finish and recover

Every terminal path runs reconciliation: accepted completion, rejection, cancellation, timeout, tool failure or interrupted-session recovery. The coordinator or recovery owner compares the ledger with actual resources, checks for continuing work, preserves needed material, then releases only owned resources. On restart, first reconcile outstanding resources and locks from the prior run; do not create duplicates because state was interrupted. Absence is recorded as verified only within the inspected scope.

For unattended work, use the independent recovery trigger, owner and detection delay recorded under [work-item handoff](work-items.md); a dead coordinator cannot run its own cleanup, and a restart-only instruction does not ensure a restart. Cancellation/supersession stops new dispatch but does not prove a process or external effect stopped. Settle in-flight work and late completions against the invalidated assignment before releasing its resources; shared children/resources retain their other authorized owners. Preserve unsettled effects and `cleanup_pending` after the work item's non-delivery status becomes terminal.

Before cleanup, preserve changes and review evidence in an authorized recoverable location. Include needed ignored files explicitly, along with selected sanitized log excerpts and reproduction details; do not rely on a Git snapshot to capture ignored files. Check that preserved material is retrievable. Keep source pointers and conclusions rather than bulk logs. Raw secret values must not be read, copied or archived by bulk status, diff, snapshot, archive or cleanup operations: use explicit safe inputs and exclusions; preserve only vault pointers and restore instructions. If a safe recoverable snapshot cannot be made, leave the resource intact and record `cleanup_pending`.

Archive a worktree only if this run owns it and the archive mechanism creates a recoverable snapshot of its needed non-secret changes. Preserve required ignored files separately first. Verify the snapshot or archive result before removing the checkout. Never discard another owner's edits. Retention is explicit: what is retained, why, where, who owns it and when or under which condition it may be removed. No “temporary” name or old modification time substitutes for a retention decision.

Stop owned processes by their revalidated identities, remove only owned containers and disposable data, and release only owned ports and leases. Never use blind Docker prune, delete shared volumes, delete by stale age, or infer ownership from a naming prefix alone. Shared infrastructure is retained unless its authorized owner explicitly delegates the required change. Release credentials through the approved secret mechanism; do not put their values into the ledger.

## Failed cleanup stays visible

A failed or uncertain cleanup is `cleanup_pending`, with exact resource ID, error summary, owner, preserved-material pointer, next action and recheck trigger/date. Include it in the final handoff and current state; it is not “done” because the main artifact passed review. Retry only after ownership and liveness are revalidated. Record a confirmed cleaned, retained or transferred outcome so recovery does not repeat destructive work. If cleanup needs unavailable authority, queue that action and continue independent work.

Monitors, retries and unattended recovery follow the same rules: identify their run and targets before acting, bound their permission, preserve evidence and account for cleanup on failure. A monitor may not claim an unowned tree or delete a lock because nobody answered. See [monitoring.md](monitoring.md).

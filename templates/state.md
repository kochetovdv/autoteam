# Cycle state

Keep the current cycle summary in the product's `docs/process/state.md`. It links the durable records that let the next actor continue. [Work items](../docs/process/work-items.md) own P-* statuses, contributions, findings and acceptance history; [project knowledge](../docs/process/project-knowledge.md) defines the wider artifact map. State does not duplicate those sources.

The decision journal preserves decisions and amendments; immutable reviews preserve verdicts. State is a mutable navigation and scheduling summary, never a replacement for either. Logs and transcripts stay out: retain their material consequence and an artifact link.

## Method fields

| Field | Holds |
|---|---|
| `cycle` | ID, assignment/brief link, mode, start and pinned canon |
| `continuity` | new cycle, or explicit resume of the same interrupted cycle; checkpoint and revalidation record |
| `recovery` | shared recovery record or owner, verified independent wakeup/reconciliation route and maximum detection delay for unattended work; otherwise explicit manual-resume limitation |
| `phase` | current stage and next coordinating action |
| `packages` | links to authoritative existing P-* records, dependency/frontier view and observation revision/time |
| `decisions` | links to decisions in force and open decisions; text remains in the journal/request |
| `assumptions` | active ASSUMP links and revision triggers |
| `blockers` | links to blocked actions/P-records, blocker owner and next recheck; details remain at their source |
| `resources` | resource registry link and requests relevant now |
| `verdicts` | review/applicability record links needed for the next action |
| `awaiting_human` | all unresolved human decisions/actions, including interactive choices and hard stops; request ID/link, dependent P-items, continuation and recheck |
| `costs` | optional reported aggregate usage/time or budget link, including child runs, reviews/retries and cleanup; unavailable metrics stay unavailable |

The product overlay may add useful fields without replacing these meanings. A linked view may cache a status for readability only if tagged with its source revision/time; edit the P-record first and regenerate the view. A stale cache cannot authorize execution or acceptance.

## Updating and recovering

- Pass skill, assignment, state links and pinned artifacts to the next actor. Do not ask a human to copy chat history. Missing knowledge becomes a durable artifact in the appropriate record, not an ever-growing state dump.
- Apply explicit deltas and serialize writes to shared state. Parallel branches return their proposed changes and artifact links; the state maintainer merges them without silently dropping fields. Updating a summary does not itself accept a deliverable.
- New observations override a stale summary. Reconcile the affected records and references before scheduling dependent work; unaffected work continues. Checkpoint state with the linked work items, journal and recoverable source snapshot according to orchestration and resource lifecycle.
- A new assignment/cycle creates a new state. Preserve the closed cycle's final state and records; revalidate anything carried over. A state file found in a directory is not proof that the previous cycle is active.
- An explicitly resumed interrupted cycle keeps its ID and history. Reconstruct it from checkpoint, events, reviews and journal, verify current inputs, pending runs/ownership and resource locks, then record the resume and any stale acceptance. Do not create a new cycle merely because a chat or agent restarted, and do not silently resume an unrelated old assignment.
- Recovery does not depend on the failed coordinator waking itself: the linked mechanism reconciles durable assignments, completions and current ownership within its stated delay. Deduplicate late/replayed events and check their assignment generation and candidate before advancing; cancelled/superseded items stay terminal. Unsettled runs/effects and cleanup stay visible even after non-delivery leaves the delivery queue. See the handoff rules in [work items](../docs/process/work-items.md).

## Example

```text
cycle: C-001 | brief: <link> | mode: interactive | started: YYYY-MM-DD | canon: <pin>
continuity: resume C-001 from <checkpoint>; revalidated <record>; resumed <time>
recovery: <owner/record>; <verified independent trigger and maximum detection delay, or manual-resume limitation>
phase: delivery; next: review P-02 candidate <hash>
packages: P-01 <record link>; P-02 <record link>; observed at <revision/time>
decisions: <D-record links in force>; open <request link>
assumptions: <ASSUMP link> — revise when <trigger>
blockers: P-03 <record/blocker link> — owner <actor> — recheck <trigger/date>
resources: <registry link>; relevant request <R-id/link>
verdicts: P-02 <RV/applicability links>
awaiting_human: <request link> — interactive choice — affects P-03 — P-02 continues — recheck <date>
costs: <optional aggregate usage/budget link, or unavailable>
```

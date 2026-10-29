# Authoritative work item (P-*)

Use the existing P-record; do not create a second task registry. Keep only sections needed for the risk, inline or by link. [Work item rules](../docs/process/work-items.md) define status events, independent acceptance and review applicability.

```markdown
# P-<existing id> — <one outcome>
Cycle / brief: <links>
Route and risk: short | full | R&D — <reason>
Outcome and business/user impact:
Goal anchor: <original problem; primary evidence/authorized meaning; critical expected outcome>
In scope / out of scope:
Acceptance criteria: <observable success/failure; REQ/NFR links if present>

Inputs (immutable version/hash + location):
- brief / requirements / plan / contracts / relevant knowledge:
- source: <commit; for dirty inputs: base + recoverable patch/snapshot hash and location, relevant untracked inputs>
Reconciliation: <versions compared; criterion → requirement → plan/P-item coverage; conflicts/gaps resolved or blocking>
Reconnaissance, if needed: <observed behavior/entry points/tests; sources and unknowns>
Dependencies and shared/writable boundaries:

Executor: <stable actor_id; current run_id; role/model/family as metadata>
Review assignments: <independent actor/run, lens; model/family or selection constraint>
Review/refresh route: <familiar reviewer; fresh perspective needed when/why>
Meaning check, where consequential/disputed: <independent expected outcome derived from primary sources; actor/evidence; contradictions>
Checks and expected evidence: <criteria, environment, commands/procedures; exclusions with reasons>
Handoff: <assignment identity/generation; artifact locations; durable completion/return and replay route; next owner>
Unattended recovery, if used: <shared recovery record or owner; verified independent trigger/adapter and maximum detection delay; otherwise manual-resume limitation>

Status: <ready | in-work | on-review | blocked | done | cancelled | superseded; leave unset while an unprepared draft>
Next action and owner:
Blocker, if any: <prior status; cause; affected action; request/resource; owner; recheck trigger/date>

## Candidate and contributions
Candidate: <immutable version/hash + location>
Authors: <all actor_id/run_id contributions to this candidate; role/model/family; include reviewers who edited>
Evidence: <candidate/input versions; environment/tool versions; procedure/command; result/exit; criteria covered, limits; output links>

## Events (append only)
<time> | <actor_id/run_id> | <event and from → to status> | <reason/evidence link>

## Review history (append-only records or links)
<RV-id> | <candidate/input versions> | <reviewer actor/run/model/family> | <first verdict or re-review link>
Findings: <stable RV-id/F-id → author response → recheck/disposition record>
Repeated returns, if any: <progress against goal/evidence; stalled-work decision and bounded next probe under assurance>

## Applicability to the current candidate
<RV-id> | current | stale | <assessed candidate/input versions; assessment record>
Carry-forward, if any: <old/new hashes; change/dependency impact; criteria/findings/evidence still covered; limits; rationale; independent acceptor actor/run>

## Completion
<current independent acceptance; criterion coverage; blocking findings dispositions; delivered artifact/docs/handoff; authorized exceptions and follow-up owner>
For non-delivery instead: <cancel/supersede authority, reason/time, successor if any; invalidated assignments, child/dependent dispositions; unsettled runs/effects and cleanup owners; no delivered-value claim>
```

The current status/applicability sections are projections of recorded events and assessments. Preserve their history; a re-review does not overwrite an old verdict. Budget fields are optional and follow [model routing](../docs/process/model-routing.md).

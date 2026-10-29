# Task brief

Record the shared intent once; authoritative P-records link to it. A small change may keep this brief inside its P-record. Choose the detail by risk, not a document quota. [Orchestration](../docs/process/orchestration.md) defines communication and authorization; [work items](../docs/process/work-items.md) define execution and acceptance.

```markdown
Understood as / intended outcome:
Business or user impact:
Goal anchor: <starting observation + date/source → intended observable outcome; failure example; how progress is distinguished from patch activity>
Mode: interactive | solution (autonomous, decision journal)
Route: short | full | operational/docs | R&D | scope | product | growth — <risk/uncertainty reason>
Routing: L1/L2/L3 · task class · model/family metadata; actor/run assignments live in P-records
Canon: <immutable snapshot path, version, full content fingerprint, selected locale; source commit/tag when available, or link to that complete profile record>
Inputs: <source, requirements, plan, contracts and knowledge versions/hashes; dirty base + recoverable snapshot when relevant>
In scope:
Out of scope:
Acceptance criteria and expected evidence:
Reconnaissance needed / completed: <complex existing behavior; artifact link and unknowns>
Requirements ↔ plan ↔ P-items reconciliation: <revision/coverage link; inline for short work>
Risks, dependencies and shared boundaries:
Work items: <existing P-* record links, executor and independent review route>
Needed from the human: none | <decision/request/resource ids, consequence and dependent P-items>
Digest for the human: <open choices and actions; links to stored requests/resource registry>
Continues independently:
Next action and responsible actor:
Optional aggregate budget: <parent + children + reviews/retries + cleanup; policy link>
Critique bound: <from profile or default broad pass + targeted recheck; decision scope, evidence/stop condition; see assurance>
```

Do not wait for “go ahead” when the assignment already says “do X” and its meaning is clear. Store interactive choices as well as hard stops in cycle state; only their dependent work waits. A brief is not permission to exceed the assignment's boundaries.

# Verified project memory

Durable facts and lessons useful beyond the active cycle. Use the existing project knowledge store if one exists. Method: `docs/process/project-knowledge.md` in the verified canon snapshot. Everything below is an unfilled template, not established project knowledge.

```markdown
Entry ID / revision / recorded at (with timezone):
Status: proposed | verified | pending-recheck | superseded
Fact or lesson:
Scope / conditions of applicability:
Observed at / fact valid as of (with timezone; unknown if not established):
Observation vs inference (if a lesson):
Primary source(s) → location / revision or content fingerprint:
Verification → method / date / result / limits:
Accepted change / reviewer / acceptance reference:
Dependent entries / artifacts:
Recheck owner / event triggers / latest review date (or reason for event-only review):
Supersedes / superseded by:
```

- Authors propose small deltas; an acceptor reviews them with the accepted change. Only accepted evidence-backed entries are `verified`.
- `verified` is scoped to the observation and verification dates. Before current use, compare the entry with relevant current facts and record applicability in the dependent work item/decision. A recent recording date or unchanged source hash does not establish current validity.
- A guess, assumption, chat compression or another agent's summary is not a source fact. Follow its primary evidence; unresolved hypotheses stay outside verified memory.
- Source changes, contradictions or unsuitable extraction mark dependent entries `pending-recheck` until reviewed again. Preserve revision and supersession links.
- The agent derives recheck settings from risk and existing preferences. For volatile or consequential premises, use an owner, triggers and a latest review date; stable facts may justify event-only review. A due review or old date does not falsify the historical fact. Unknown current applicability stays explicit; recheck relevant premises rather than rereading all memory.
- Keep settings in the profile, intended behavior in the spec, choices in the journal and current tasks in state. Do not duplicate them here.
- No raw secrets, logs, tool transcripts or chat histories. Link only necessary sanitized evidence. A durable limitation includes the actual check, scope and recheck trigger; tool failure does not prove product absence.

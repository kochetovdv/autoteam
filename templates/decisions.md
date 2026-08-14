# Decision journal (autonomous mode)

Every decision that in interactive mode would have gone to the human is recorded as a row. The human reads the journal afterwards, not approves beforehand.

| ID | Date | Decision | Why this | Alternative | Reversibility | Decided by |
|----|------|---------|------------|--------------|-------------|-----------|
| D-001 | | | | | easy / costly / irreversible | agent role |

Rules:

- The irreversible and external money never enter the journal — those are a hard stop, not an agent's decision.
- "Reversibility: costly" — the decision is flagged for priority reading by the human.
- ASSUMP entries from spec/scope are not duplicated here — this is for choices ("took X, not Y"). Exception: ASSUMP entries that change the market, the audience, or money are duplicated here without fail.
- The journal is append-only: if a later artifact refined or overturned a decision, an amendment with a link is appended to the entry ("D-004a: refined in spec §5") — the entry is not rewritten. The check "the journal does not contradict the final artifacts" is an acceptance item.
- An amendment that changes an ASSUMP or a decision lists the dependent artifacts and spawns a task to revise them.

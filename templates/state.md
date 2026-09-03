# Cycle state

The cycle's current picture of the world, kept in `docs/process/state.md` of the product. What a wave needs in order to continue is here; everything else lives in the journal, the artifacts, and the checkpoints.

State is not history. The decision journal is append-only history for the retro; state is the mutable present for execution. Both are needed; neither replaces the other.

## Schema (method fields — always present)

| Field | Holds | Note |
|------|---------|-----------|
| `cycle` | id, assignment in one line, mode (interactive / solution), start | from the brief |
| `phase` | where the loop is now | product / positioning / scope / architecture / delivery / release / analytics |
| `packages` | package → status → owner | statuses: planned, in-work, on-review, `Blocked-by-resource`, done |
| `decisions` | D-ids of decisions in force | references, never the text — the text is in the journal |
| `assumptions` | ASSUMPs the current work rests on | with the revision trigger |
| `blockers` | what is stopping what, owner, date | includes open perimeter narrowings |
| `resources` | reference to the product's resource registry | plus what is awaited from the human |
| `verdicts` | last board verdicts and return count | acceptance input |
| `awaiting_human` | hard stops only | everything else is a decision |
| `costs` | time, tokens/calls if the environment reports them | retro input |

Product fields are added by the product's overlay (a stack pin, an environment, its own entities). The overlay extends the schema; it does not rewrite the method's fields.

## Rules

- **A wave is a step.** A subagent is launched from the skill plus the state plus the assignment of its wave — never from a transcript. Whatever must survive the wave goes into the state: what is not in the state is lost by design, not by oversight.
- **A patch, not a rewrite.** A wave returns a delta: which fields changed, what was added, what is explicitly removed. A delta that silently drops existing fields is invalid and comes back to its author. Removal is always explicit.
- **The author does not merge their own patch.** The orchestrator (or the acceptor) applies the delta — the author ≠ acceptor boundary extends to the state. An invalid patch is a return, not a fix in flight.
- **A fresh observation beats the state; the state never beats the observation.** Reality diverging from the state is a stop until the state is corrected — working on top of a state known to be stale is forbidden.
- **Noise does not enter.** Logs, telemetry, tool output are observations; only their consequence is committed to the state. A field nobody reads on the next wave does not belong in the schema.
- **A chat summary is not state.** Compressing history to fit the context is forbidden as a substitute for maintaining the state: a summary loses exactly the identifiers and dependencies the next wave needs.
- **One writer per wave.** Parallel branches return their own deltas; the merge is the orchestrator's, at the end of the wave, by the rules for a shared mutable boundary.
- **The state is checkpointed with everything else.** Restoring a cycle = the last checkpoint's state plus the journal.

## Template

```
cycle: C-001 | "<assignment in one line>" | mode: solution | started: YYYY-MM-DD
phase: delivery

packages:
  P-01 <name> — done — <role>
  P-02 <name> — in-work — <role>
  P-03 <name> — Blocked-by-resource R-002 — <role>

decisions: D-001..D-007 in force; D-004 amended by D-009
assumptions:
  A-01 <assumption> — revise when <trigger>

blockers:
  B-01 <what is blocked> — <cause> — owner — re-check YYYY-MM-DD

resources: docs/process/resources.md; awaiting from human: R-002 (account)
verdicts: board YYYY-MM-DD — ACCEPTED, N non-blocking, returns: N
awaiting_human: none
costs: 3 waves, ~N h; tokens: <if reported>
```

---
name: autoteam-retro
description: Method retrospective — what in the canon worked, what stalled the cycle, proposed edits without project details. Use after a completed cycle, an MVP, a process incident, "why did we stall".
---

# Canon retrospective

The autoteam canon is the baseline: while working on a product it is immutable. Improvements go only through this skill — as proposals the human approves. You do not edit the canon in a working cycle.

**Input.** Decision journal, the run's briefs and handoffs, stop points, facts of "a skill didn't work / wasn't found / contradicted another". **Output.** Retro report: what worked, what stalled, proposed canon edits (add / change / remove) justified by facts of the run. **Forbidden.** Editing the canon yourself; dragging project details into proposals (names, stack, domains, product paths) — an edit is phrased depersonalized, as method; proposing a new skill from a single case. **Evidence.** Every proposal links to a specific fact of the run (a decision from the journal, a stop, a discrepancy). **Stop.** None. Approving edits is the human's call. **Next.** Approved → canon edit as a separate task, then re-distribute the copies to projects.

## Procedure

1. Gather facts: where the cycle stalled and why; which decisions from the journal turned out wrong; which skills went unused or duplicated each other; where the agent acted "outside the canon" — and was right.
2. Separate: method defect (a rule got in the way) | method gap (there was no rule) | execution defect (the rule existed, the agent didn't follow it — not a reason to change the canon).
3. Depersonalize: from "project X got stuck choosing a DB" to "no rule for choosing storage on empty input". Test: the proposal reads without knowing the project.
4. Proposals: a minimal diff phrased "was → becomes → why"; for removal — a rule that was never needed in N cycles or was systematically violated with no harm.
5. Priority: first what stopped the cycle; then result quality; then style.

Cadence — by triggers, not after every run (a run with no findings is the norm for a well-tuned process): first run of a new task type; a stop or process incident; the human unhappy with the result; systematic zero returns at acceptance; ~5 runs without a retro — a light "pulse" (a quick stats check: returns, critic board remarks, cycle time — against degradation and stagnation).

Artifact: `docs/process/retro-YYYY-MM-DD.md` in the **product**; approved edits go into the canon as a separate task.

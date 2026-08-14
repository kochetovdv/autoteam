---
name: autoteam-research
description: A bounded experiment — hypothesis, baseline, metrics, ADOPT/REJECT/CONTINUE. Use for unknown feasibility, storage choice, load.
---

# Research

Reduce the unknown. A demo without a method is not evidence. Experiment code does not go to prod in this run.

**Input.** An unknown to narrow. **Output.** Protocol, raw logs, verdict `ADOPT` | `REJECT` | `CONTINUE_RESEARCH`, gaps before production. **Forbidden.** Moving the threshold after seeing the numbers without a new experiment; leaking the experiment into prod. **Evidence.** Baseline, threshold, timebox, environment versions. **Stop.** None. Don't stop independent tasks. Choosing the stack from the result — the human, if it's a platform change. **Next.** ADOPT into the product → `autoteam-architecture` + `autoteam-delivery`.

Protocol: which decision the result unlocks → falsifiable hypothesis → data resembling production, baseline, threshold, timebox → environment versions → raw logs → limitations → verdict → gaps before production.

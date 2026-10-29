---
name: autoteam-research
description: Run a bounded falsifiable experiment to resolve feasibility, quality, performance, or tool uncertainty. Use when an evidence-based decision needs a baseline and measured comparison.
---

# Research

Identify the decision to unlock, a falsifiable hypothesis, representative data/workload, baseline, success/failure thresholds, timebox, environment versions, and allowed side effects before the run. Reuse source derivations only while they answer this question with adequate coverage; [knowledge](../../docs/process/project-knowledge.md) governs freshness.

Control variables, retain reproducible commands and raw evidence without secrets, and report uncertainty, limitations, and threats to validity. Do not adjust the threshold after seeing the result without a new experiment. A demo or agreement among agents is not evidence of customer demand.

Stop when the decision threshold is reached, timebox/authorized allocation is exhausted, or unrepresentative inputs/confounders invalidate the method. Independent work continues. Return `ADOPT`, `REJECT`, or `CONTINUE_RESEARCH`, and separately list the work required for production. The experiment is not deployed as production implementation in this run.

Controlled data modifications use an isolated test copy with external effects disabled, following [QA](../../docs/delivery/qa.md). Record actual source, tool, and result versions and author/reviewer provenance. Adoption routes to architecture/delivery under the existing authority; a live-stack change follows [stack](../../docs/process/stack.md).

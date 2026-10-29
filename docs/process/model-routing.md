# Models and whole-task limits

The default objective is a verified outcome understood by the human. Token economy is secondary unless the user sets a limit. Automatically choose as many useful roles and reviewers as the task needs; every additional agent has a responsibility, output, and stopping condition.

Routing levels classify error cost: **L1** is bounded routine work with clear criteria; **L2** is ordinary delivery across known behavior; **L3** covers costly or hard-to-reverse decisions, architecture, security, money, data integrity, and concurrency. They are risk labels, not fixed model IDs or exemptions from independent acceptance.

## Dispatch by work, uncertainty, and error cost

- Use deterministic tools for search, copying, calculations, build/lint, and known resource operations when they suffice.
- Use an economical capable model for clear bounded implementation and routine synthesis.
- Use stronger reasoning for ambiguity, architecture, critical data/security/calculations, and costly decisions. A strong plan does not make every implementation simple.
- Select an independent critic capable of testing the relevant risks; price or a tier label is not evidence of competence. Prefer a different family where available. One family is allowed with fresh context, recorded `same-family`, and actual independent checks.
- Escalate a specific difficulty with evidence when risk rises, inputs conflict, or progress stalls. Once uncertainty is resolved, bounded work may return to a less costly executor.

The product profile maps these capabilities to available model IDs and adapters; the canon does not hardcode them or make unsupported claims about how models were trained. Record requested and actual model/family, actor/run, task class, evidence, and any fallback. An adapter that cannot dispatch the requested model reports that limitation; it does not claim a switch occurred.

Send concise pinned context and retrieved evidence, not every agent's transcript. Do not launch agents merely to appear parallel. Independent duplicate work is justified when it tests a material risk.

A model switch is not a new causal hypothesis or a reset of failed attempts. Transfer the original outcome, primary evidence, rejected approaches, stable findings and observed progress. If useful outputs keep arriving while the goal remains unmet, apply the bounded reassessment in [assurance](assurance.md) before dispatching another patch. Open-ended critique has its own finite round limit even when no token cap is requested; quality priority does not authorize an endless search.

## Optional assignment limit

A user may bound money, tokens, calls, elapsed time, or a combination. Without an explicit task cap, do not invent a token/agent ceiling; use the authorized resources and stop unproductive repetition. Existing account limits and authority for new external spending still apply.

The coordinator owns one shared ledger for the parent, all descendants, repeated runs, research, review, tool/infrastructure costs where measurable, preservation, and cleanup. Before parallel launches reserve allocations from the shared limit; reconcile actual usage and release unused allocations. Elapsed time and summed agent-time are distinct. Never sum incompatible provider units as exact money; unavailable measures remain unknown or labeled estimates.

Before any launch under a hard cap, include all in-flight parent/descendant reservations and a conservative upper bound for the next call/run, plus the remaining verification/preservation/cleanup reserve. Provider or adapter bounds and cancellation/timeout behavior must be verified; post-run reconciliation cannot prevent concurrent overspend. If no usable bound exists, do not launch budget-dependent work on an estimate.

If a requested hard limit cannot be measured or enforced by the adapter, disclose that limitation before budget-dependent launches and resolve an enforceable bound with the user. Estimates do not establish compliance with a hard cap; independent checks that consume none of the constrained resource may continue.

Reserve capacity for independent acceptance, checkpointing, and cleanup before implementation spends the available budget. Reaching the execution allocation stops new work while the reserve finishes preservation and reports partial status; it never converts incomplete work into `ACCEPTED`. Do not silently shrink agreed scope, skip criteria, raise the limit, or reset the ledger by changing agents. Explain outcome achieved, evidence, unfinished work, usage, and options for continuation.

Judge efficiency by the full cost of an accepted outcome, including human relaying, returns, and defects found after acceptance. User preference for quality does not permit unrelated paid services or production actions.

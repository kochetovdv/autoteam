---
name: autoteam-budget
description: Account for authorized spend, forecasts, category limits, and channel economics with sourced numbers. Use for cost questions, paid-service choices, and spending limits.
---

# Budget

Track infrastructure, models/APIs, paid services/fees, marketing/content, and one-off costs. Each line has a source, period, currency/unit, owning account/resource, and growth driver. Label forecasts and missing data; do not invent savings or prices.

New external spending or a higher account limit requires authority. Existing authorized usage may continue without a separately specified task-token cap; [model routing](../../docs/process/model-routing.md) owns optional whole-task limits and shared allocations. No limits for a proposed new purchase means prepare the decision without making the purchase.

Use the human's category ceilings and stop-lines, with forecast warnings before exhaustion. Propose thresholds where absent, explain them, and keep them in the project profile. A category limit stops new spend in that category without blocking independent work; do not silently exceed it.

## Channel decisions

Use comparable attribution, time window, and monetary units. Define `ROI = (attributed value - channel spend) / channel spend` for positive spend; lower is worse. State what "value" includes and how it was measured, with uncertainty. For zero spend, ROI is undefined: report absolute value/cost separately. Missing value is unknown, not zero. Do not divide monetary spend by unconverted time/risk scores and call it ROI.

Recommend changing a channel only against an agreed threshold, adequate evidence, and the observation window/repetition policy in the profile; a fixed number of periods is not proof. A cheaper cost-to-value ratio is a different metric whose lower values are better; do not mix its direction with ROI.

Artifact: the product's `docs/product/budget.md` or existing ledger. Link pricing to `autoteam-pricing`, measurements to `autoteam-analytics`, channels to `autoteam-growth`. Store amounts and public price references, not payment credentials or secret billing data.

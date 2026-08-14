---
name: autoteam-budget
description: Budget management — plan/actual spend, limits and stop-lines, infrastructure, models and APIs, services, marketing, channel ROI. Use on "how much are we spending", limits, choosing a paid service, judging a channel's payback.
---

# Budget

The team's money is a limited resource owned by the human. You keep the ledger, the forecast, and the stop-lines; spending new money is the human's decision.

**Input.** Spend sources (infrastructure, models/APIs, paid services, marketing), limits from the human, metrics (`autoteam-analytics`). **Output.** Plan/actual by category, forecast for the period, stop-lines, channel ROI, recommendations on what to cut or reinforce. **Forbidden.** Connecting a paid service or raising a limit without the human; hiding a spend category; "too small to count"; invented numbers instead of "no data". **Evidence.** Every number — an invoice, a price plan with a link, or a billing readout; a forecast is labeled as a forecast. **Stop.** A category's stop-line is reached — stop new spend in that category and ask the human; the rest of the work continues. No limits at all — request them once; until the answer, keep the ledger without spending. **Next.** Product economics → `autoteam-pricing`. Channel efficiency → `autoteam-growth` + `autoteam-analytics`.

## Categories (cover all)

1. Infrastructure: hosting, DB, storage, domains, traffic.
2. Models and APIs: tokens/calls by agent role — hungry loops get their own line.
3. Paid services: analytics, email, monitoring, payment provider (fees).
4. Marketing: paid channels, tools, content production.
5. One-offs: registrations, licenses, audits.

## Order

1. Spend map: category → line item → price plan → growth driver (users, events, tokens). Every paid plan is tied to an account from the resource registry (`templates/resources.md`) — a plan without an owning account is a ledger hole.
2. Limits and stop-lines from the human: a monthly ceiling per category; stop-line = 80% of the ceiling → warning, 100% → stop category spend.
3. Plan/actual every period: divergence >20% — a cause analysis, not silence.
4. Channel ROI: channel spend / value brought (from `autoteam-analytics`). A channel below threshold two periods in a row — recommend cutting.
5. Forecast: at current drivers — when we hit the ceiling; what grows faster than the benefit.

Artifact: `docs/product/budget.md` in the **product** (spend map, limits, plan/actual). Do not store payment credentials or billing secrets — only amounts and links to price plans.

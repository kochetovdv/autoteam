---
name: autoteam-pricing
description: Monetization — revenue model, plans, price, trial, payment flow, live unit economics. Use on "how do we charge money", plans, subscription, payments, payback.
---

# Monetization

"To revenue" = the product can take money and the economics adds up. The human approves the price; you prepare the decision.

**Input.** Positioning, ICP, cost base (infrastructure, models, fees), alternatives' prices. **Output.** Revenue model, plan grid, price with rationale, trial mechanics, payment flow plan, unit economics. **Forbidden.** Publishing prices without the human; "free for now" without a revision date; more than 3 plans at the start; hiding the cost base. **Evidence.** A competitor's price — link and date; the cost base — a calculation, not a feeling. **Stop.** The economics does not add up in any scenario — a monetization Blocker, verdict to the human. Payment provider choice — by market and jurisdiction, final call the human. **Next.** Payment code → `autoteam-delivery` (+ `autoteam-security`: money = audit). Pricing page → `autoteam-ui`. Revenue metrics → `autoteam-analytics`. Spend and limits → `autoteam-budget`.

## Order

1. Model: subscription / one-time / usage-based / commission / freemium. From the ICP and the nature of the value, not from fashion.
2. Value metric: what they pay for (seat, project, volume, outcome). The right one grows with the customer's benefit.
3. Grid: up to 3 plans, each for an ICP segment. What each includes and excludes — explicit.
4. Price: a range from value (what it saves or earns the customer) and from alternatives; the cost base is a floor, not the pricing logic.
5. Trial / free tier: lets them try the value, hits the paywall in an understandable place. Revision date.
6. Payment flow: provider by market, subscription cycle, failed payments, refunds, taxes — tasks with owners, not footnotes.
7. Live unit economics: `docs/product/unit-economics.md` of the canon. CAC, contribution, churn — from `autoteam-analytics`, not from the head. Recalculate on a price or channel change.

Artifact: `docs/product/pricing.md` in the **product**. The price is a hypothesis with a revision date, not a constant.

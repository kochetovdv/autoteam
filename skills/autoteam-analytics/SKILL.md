---
name: autoteam-analytics
description: Product analytics — north star, events, funnel, dashboard, honest reading of the numbers. Use on "what do we measure", metrics, conversion, A/B, "why aren't we growing".
---

# Analytics

Without measurement, growth is blind and experiment verdicts are opinions. You own what we measure, how events get into the code, and what the numbers mean.

**Input.** Product picture, funnel (`autoteam-growth`), business questions. **Output.** Metric tree (north star + 3–5 leading metrics), event plan, dashboard, honest conclusions. **Forbidden.** Vanity metrics as the goal (signups without activation); silently changing a metric's definition; conclusions from a "3 users" sample without a caveat; collecting personal data into events without a privacy map. **Evidence.** Every number — the query/event it came from. **Stop.** None. No data — file instrumentation as a task, do not invent a number. **Next.** Events into code → `autoteam-delivery`. Personal data in events → `autoteam-security`. Experiment → `autoteam-research` (threshold and verdict — before the numbers).

## Order

1. North star: one value metric (at the start — value usage, not revenue). Leading: activation, retention, conversion to money.
2. Funnel: stages from first touch to payment and repeat use. Each has a metric and an event.
3. Event plan: name, properties, when it fires, owner. The event schema is a contract: it changes explicitly, not silently.
4. The tool — from the stack and the product's decision (self-hosted / SaaS). Do not drag in a heavy platform "just in case".
5. Dashboard: north star, funnel, money. One screen, updates without manual assembly.
6. Reading: trend over a point; segments over the average; correlation ≠ causation. An anomaly — check the instrumentation first, theories second.

Artifact: `docs/product/metrics.md` in the **product** (metric tree and event plan).

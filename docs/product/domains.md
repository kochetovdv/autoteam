# Entering an unfamiliar domain

We do not breed 20 industry skills. One method; the cards are examples.

## The method (mandatory in a new domain)

1. Words that must not be confused (a glossary of 10–20 terms).
2. Who acts and what they fear (money, fines, downtime, reputation).
3. What the "record of truth" is (a deal, an order, a document, a ticket).
4. Which race conditions and roles are typical (two operators on one object, a tenant).
5. Regulation: the subjects' jurisdiction → `docs/compliance/privacy.md`; a regime is never assigned out of habit.
6. Three acceptance scenarios of the form "if this breaks, the product is dead".

Until items 1–3 exist, do not design the storage "like in the last project".

## Card: B2B SaaS

The truth is the organization and the role within it. Multi-tenant from the first feature. Estimation: rollout + support, not just screens. Unit economics are contract-based.

## Card: IoT / devices

The truth often lives in two places: "now" (an online API) and "history" (your own storage). Do not confuse device connectivity with device data. Race conditions on ingestion cursors. An empty dashboard ≠ "the database is busy" without a storage query. Device data and geolocation — privacy regime per the subjects' country.

## Card: retail / e-commerce

The truth is the order and the stock level — and there are two of them (storefront and warehouse): divergence = overselling. Race conditions on stock and promo codes. Load peaks (sales events) — in numbers before launch. Returns and partial cancellations are normal process, not an edge case. The economics are margin and basket, not just conversion.

## Card: marketing / SMM tools

The truth is the post and its metrics, and they live in someone else's APIs: rate limits, changes, and revocation of third-party contracts are the main risk. A queue of scheduled posts — idempotency is mandatory (a double post is a public incident). Access to other people's accounts — secrets and roles stricter than usual.

## Card: advertising / adtech

The truth is the impression/click event and the money attached to it. Counter mismatches with platforms are the norm — you need a reconciliation process, not panic. Fraud is background noise, not an exotic case. Attribution lags — do not close the day at midnight. Budgets are server-side stop-lines.

## Card: manufacturing / industrial

The truth is a physical process; the data about it lags and lies (sensors, manual entry). A stopped line costs more than any UI bug. Integration with legacy (SCADA, ERP, files) is the norm, not the exception. Releases go into maintenance windows. Safety includes the physical safety of people, not only data.

## Card: IT services / devtools

The truth is the contract and DX: the users are engineers, and the documentation and API are the product itself. Backward compatibility is sacred: a breaking change = Blocker. Self-serve to first success in minutes. On acceptance — a DX lens instead of art.

## Card: fintech

The truth is the ledger entry and the balance. Double-entry and idempotency are mandatory from the first line. Reconciliation with the provider is a daily process. KYC and regulation per jurisdiction — the map comes before the code. An audit trail for every action involving money.

## Card: logistics

The truth is cargo/an order in motion: a status model with time and place. The truth diverges from physical reality (a missed scan) — you need correction processes, not faith in the data. Route optimization is secondary to an honest status. Carrier integrations are fragile — timeouts and retries from day one.

## Card: content / landing page

The truth is the offer and a fact that can be quoted. SEO+GEO. No complex role model until there is an account area. Mobile = responsive web until an app is requested. The estimate must not hide "unique visuals" inside "one more screen".

## Card: internal tool

The truth is the process and the role inside the company. No SEO. Estimation = team hours and cost of error, not CAC. Permissions = departments and roles, not "customers on a plan".

## Card: B2C / self-serve

The truth is the user and their data. Funnel and churn. Personal data at scale. A mobile client — only if the product's channel is the phone.

## Card: platform / API

The truth is the contract and quotas. A breaking API change = Blocker. Estimation includes versioning and DX (how it is called), not just handlers.

## Card: R&D

The truth is the hypothesis and the threshold. Experiment code does not go to prod. R&D as separate packages. Skill: `autoteam-research`.

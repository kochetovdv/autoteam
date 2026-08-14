---
name: autoteam-docs
description: Documentation for business and for development, plus regular refresh — when it goes stale, who updates it. Use for kb, README, runbook, "docs are stale", after a behavior change.
---

# Product and code documentation

Not "write a README". Three layers: business, technical, process. Method canon: `docs/docs-practice/README.md`.

**Input.** A change in behavior/API/roles, or "docs are stale". **Output.** Updated layers in the **product** repository. **Forbidden.** Repo paths as a menu for business; made-up buttons; the only source of truth living in chat. **Evidence.** Button/API checked against the UI or the contract. **Stop.** None. No layer owner — queue it, don't stop someone else's code. **Next.** Behavior is changed by `autoteam-delivery` in the same cycle.

Business: screens and rules in plain language. Check buttons against the UI.

Technical: ADR, runbook, contract, how to run and roll back.

## Cadence

In the same change as the behavior/API/role/admin command/release.

Regular pass: active product — every 1–2 weeks; quiet — with the architecture review once a month.

Stale: a button that doesn't exist, code contradicting the doc, a dead link. Owner in the product README.

User-facing kb in the UI — bundled as the project does it (don't promise to serve files from `docs/` if the runtime doesn't put them there).

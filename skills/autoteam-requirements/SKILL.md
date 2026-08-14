---
name: autoteam-requirements
description: Shapes requirements from a statement of work or product picture — REQ/NFR, scenarios, facts vs assumptions. Use for specification and scope changes.
---

# Requirements

What and why. Don't pick the stack.

**Input.** Statement of work, product picture, or scope change. **Output.** Spec: facts/assumptions, in/out, REQ/NFR, scenarios, question batch. **Forbidden.** Rewriting the spec silently; "fast" without a number as a MUST; asking about REQs one at a time. **Evidence.** Every MUST has a scenario. **Stop.** Blocker only if a MUST cannot be formulated without the answer. Everything else — a question in the batch or R&D. **Next.** Design → `autoteam-architecture`. Scope → `autoteam-scope`. Code → `autoteam-delivery`.

Modes: `delivery` (gaps = questions) | `scope` (answers or ASSUMP). State the mode up front.

Order: problem and roles → facts/claims/assumptions/decisions kept separate → in/out → glossary → REQ/NFR (measurable or R&D) → given/when/then → data and permissions if people/money/personal data/devices are involved → question **batch** at the end, not one at a time.

Delivery: `Draft | Approved | Superseded`. Implementation is a plan, not the spec.

Domain input: method canon `docs/product/domains.md`.

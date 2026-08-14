---
name: autoteam-architecture
description: Designs the architecture — modular monolith, clean, hexagonal, DDD — ADRs, data, observability. Use for plans, ADRs, storage, a new service.
---

# Architecture

You own the design, not the requirements text. A new service/broker/store — a reason and an ADR.

**Input.** Spec or a boundary task. **Output.** Component picture, contracts, ADR if a new decision. **Forbidden.** Assigning a language/framework when the product has a live stack; multiplying services without a reason; a web client, mobile client, bots "while we're at it". **Evidence.** Load in numbers or ASSUMP; failure behavior described. **Stop.** No stack and the runtime can't be designed without one — a question to the human. Otherwise ASSUMP. **Next.** Code → `autoteam-delivery`. Scope → `autoteam-scope`. Review → `autoteam-architecture-review` (not you).

Method canon (if available): `docs/architecture/styles.md`, data `docs/delivery/data.md`, observability `docs/delivery/observability.md`, stack `docs/process/stack.md`.

## Default style

Modular monolith. Language and UI framework — from the product / an ADR. One store per load type. Clients are not part of the architecture until there is a requirement.

## Style

Monolith at the start. Clean — complex rules. Hexagonal — several entry points. DDD — different business languages and a context map. CQRS — only with evidence.

## Order

Components and data owners → contracts before code → failures (timeout, retry, idempotency) → load in numbers or ASSUMP → permissions and privacy map (regime per jurisdiction) → observability → release/rollback → ADR.

ADR template: `templates/adr.md` of the method canon.

Scope vs delivery: for scope planning — the simplest picture; don't guess the stack. Scope → `autoteam-scope`.

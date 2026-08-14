# Architecture styles

Default style: **modular monolith**. Language and UI framework — from the current product / ADR (`docs/process/stack.md`). No stack — pin it down with the human, do not assign a language. A new service, broker, or store — only with a measurable reason and an ADR.

## Which style when

| Style | When appropriate | Essence |
|-------|----------------|------|
| Modular monolith | almost always at the start | One process, hard package boundaries |
| Clean core (Clean) | complex rules, many adapters | Dependencies point inward only |
| Hexagonal (ports and adapters) | HTTP + queue + CLI + legacy | Core knows no framework |
| DDD | different business languages | Bounded contexts |
| CQRS / events | different read/write loads | Do not start without evidence |

Do not declare DDD without a context map. Do not declare microservices when the pain is in the modules of a single repo.

ADR template: `templates/adr.md`. Review: `docs/architecture/review.md`.

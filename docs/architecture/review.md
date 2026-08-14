# Architecture review

This is not a code review of one PR. Look at connections, data, failures, permissions.

Cadence and skill: `autoteam-architecture-review`. Report template: `templates/architecture-review.md`.

Active product: once a week or every ~8 tasks. Quiet: once a month. An incident involving data, a race condition, failures, or a lock — out of band.

While the review runs, independent tasks continue. Stop — only scope with a Blocker (service outage, data loss, permissions hole, state-corrupting race condition, incompatible contract).

Dimensions: boundaries; data owner; race conditions and idempotency; server-side roles; failures and observability; simplicity (KISS); debt with an owner and a date.

Verdict: `HEALTHY` | `WATCH` | `REMEDIATE`. REMEDIATE ≠ stopping all development.

---
name: autoteam-quality
description: Implementation quality — correctness and race conditions, failure resilience, performance, data integrity. Use for reviews, a flaky bug, money and statuses, timeouts, "it's slow".
---

# Quality

Works with `autoteam-delivery`. Don't inflate abstractions: KISS — the simplest thing that passes the criteria; DRY — shared essence, not matching lines; SOLID — one reason to change a module; YAGNI — no bus "for the future".

**Input.** Diff, flaky bug, queue/status/money, a speed complaint. **Output.** Findings or fixes with a reproducing test. **Forbidden.** Masking data corruption as "busy" without a log; swallowing errors; optimizing without measurement; duplicating security. **Evidence.** Reproduce or refute with a test; for performance — before/after measurement. **Stop.** A race condition or data loss involving money — Blocker for this task. **Next.** Roles/trust boundaries → `autoteam-security`. A workaround without a date → `autoteam-architecture-review` queue.

## Correctness and race conditions

A flaky bug ("sometimes it doesn't work") is almost always a race condition or timing: two implementers read-modify-write the same thing (cursor, balance, status, job owner). Reproduce or refute with a test. One record owner for the duration of the operation. Retrying a request is safe (idempotency). Integrity: a transaction where two writes must live together; an invariant is checked by code, not by hope.

## Resilience

Every external call: timeout, retry with backoff (idempotent ones only), behavior when the dependency is down. An error is handled, logged with context, shown honestly — don't swallow it and don't crash the whole process over one item. Partial failure means degradation, not a cascade. Inputs are validated at the boundary.

## Performance

Measure first, optimize second. Typical: N+1 queries, scans without an index, extra network round-trips, memory in a loop. The critical-path budget is a number from an NFR or an ASSUMP with a review trigger. Don't optimize the warm — optimize the measured hot.

Race-condition rules are in product language; stack details are in the product overlay.

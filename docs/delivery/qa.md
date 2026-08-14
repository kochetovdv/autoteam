# Quality checks (QA)

TDD — a failing check first, then code. This does not replace the pyramid.

| Kind | When mandatory | When N/A |
|-----|------------------|-----------|
| Unit | rules, calculations, in-memory race conditions | pure CSS layout |
| Integration | DB, queue, files | no I/O |
| Contract | an API/event between parts changes | internal refactor without schema changes |
| E2E | critical user path | copy edit |

Negative cases, permissions, idempotency — whenever money, personal data, roles, or request retries are involved.

Evidence: command + output. "The UI looks better" without a query is not sign-off for data.

States unreachable on real data may be checked via temporary data modification — with a note in the report: what was changed, how, original restored. Unmarked data modification in evidence is forbidden.

A finding of the "data loss or corruption" class: reading code is not enough — either reproduce it, or explicitly mark "mechanism confirmed, scale not measured" and queue a run for the human.

Delivery skill: `autoteam-delivery`. Race conditions: `autoteam-quality`.

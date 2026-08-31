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

Every check must distinguish "nothing happened" from "all good": a checking script asserts that it actually ran (the substitution took place, the line was found); a report carries an exit code next to every conclusion; the expected non-empty result is declared in advance — an empty answer is a failure, not a success.

An acceptance criterion is derived from how the change can break, not from what it should improve. The mandatory question before phrasing it: "what does this criterion look like if the change is broken?" — if that matches success, the criterion is unfit. Fit criteria distinguish states: "a spread of values exists", "the knob moves the result" — not "it got better".

States unreachable on real data may be checked via temporary data modification — with a note in the report: what was changed, how, original restored. Unmarked data modification in evidence is forbidden.

Judging logic correctness without checking the domain specification (if one exists) is judging the code's consistency with itself, not its correctness. Code diverging from the spec is a finding in both directions: the code may be wrong, or the spec may be stale; record both possibilities. Practice: a line-by-line "specification ↔ code" reconciliation registry (matches / diverges / not implemented) — after it, "that's how the code does it" stops being an argument.

Settings: "it is read" ≠ "it works". A setting is verified by the end-to-end path "changed it → saw a different result at an observable output, within a known time", including already-computed data (see derived data in data.md). A setting with no observable effect is dead — that is a finding.

A finding of the "data loss or corruption" class: reading code is not enough — either reproduce it, or explicitly mark "mechanism confirmed, scale not measured" and queue a run for the human.

A test is verified by mutation: break the behavior under test on a copy — the test must fail; a test that always passes is a defect nothing else catches, and the check costs minutes. Progress invariants (a cursor, a boundary, a window that must move) are tested by a sequence of steps requiring movement at each one — a single "within valid bounds" check lets "stuck" pass. A structural property not expressible in behavior (e.g., build splitting) may legitimately be checked by reading the source — with a recorded justification of why behavior cannot check it.

Delivery skill: `autoteam-delivery`. Race conditions: `autoteam-quality`.

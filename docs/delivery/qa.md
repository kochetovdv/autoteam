# Quality checks (QA)

TDD — a failing check first, then code. This does not replace the pyramid. Choose checks for the changed behavior and its risk; a small copy/CSS change does not require a full-system sweep. [Assurance](../process/assurance.md) maintains the broader coverage and deeper risk-based audits.

| Kind | When mandatory | When N/A |
|---|---|---|
| Unit | rules, calculations, in-memory race conditions | pure CSS layout |
| Integration | DB, queue, files | no I/O |
| Contract | an API/event between parts changes | internal refactor without schema changes |
| E2E | critical user path | copy edit |

Negative cases, permissions, idempotency — whenever money, personal data, roles, or request retries are involved. For stateful/background work include relevant offline/reconnect, timeout/hang, partial failure, restart, worker/lease ownership, and progress cases. Test the recovery as well as the failure when the requirement includes recovery.

Evidence: command + output + exit status, with revision, environment, data/workload, and time sufficient to reproduce it. "The UI looks better" without a query is not sign-off for data. Separate measured results, inference, and unknowns.

Every check must distinguish "nothing happened" from "all good": a checking script asserts that it actually ran (the substitution took place, the line was found); a report carries an exit code next to every conclusion; the expected non-empty result is declared in advance — an unexpected empty answer is a failure, not a success. A legitimately empty/zero result needs a declared expectation and evidence that the intended query/probe executed over the intended scope.

An acceptance criterion is derived from how the change can break, not from what it should improve. The mandatory question before phrasing it: "what does this criterion look like if the change is broken?" — if that matches success, the criterion is unfit. Fit criteria distinguish states: "a spread of values exists", "the knob moves the result" — not "it got better".

Challenge the criterion and evidence using the shared protocol: **claim → assumptions → counterexample → controlled probe → `CONFIRMED` / `REFUTED` / `INCONCLUSIVE`, with scope and follow-up**. Define the discriminating observation, expected result, bounds, and stop condition before the probe. Agreement between agents is not evidence of correctness or customer demand. Use the same protocol for a brief, finding, implementation, test, or business hypothesis, with evidence appropriate to the claim. Do not turn this into a heavy test for every source line.

## Safe test data and side effects

States unreachable in the available data may be checked through temporary modification **only in an isolated disposable/test copy with external side effects disabled**. Isolate credentials, workers, queues, outbound calls, notifications, payments, and other automatic consumers so the copy cannot act on production or third parties. A transaction rollback or restoring a row does not undo a message, payment, or worker action already triggered.

Mark the evidence: original source/snapshot, exactly what was changed and how, side-effect isolation, expected effect, output, and cleanup/restoration. Never present synthetic/modified data as an observation of production. Unmarked data modification in evidence is forbidden. Production-data QA requires a separately authorized procedure covering effects, access, recovery, and observation; a supposedly reversible row update is not sufficient authority.

## Specification and observable behavior

For consequential or disputed meaning, also perform the independent source-based check in [assurance](../process/assurance.md). Establish decisive expected observations without copying the author's interpretation. Consistency between a specification, its code and generated tests cannot expose an error shared by all three. Pin the original problem and compare actual outcome progress across returns; a model switch does not reset failed approaches.

Judging logic correctness without checking the domain specification (if one exists) is judging the code's consistency with itself, not its correctness. Code diverging from the spec is a finding in both directions: the code may be wrong, or the spec may be stale; record both possibilities. Practice: a line-by-line "specification ↔ code" reconciliation registry (matches / diverges / not implemented) — after it, "that's how the code does it" stops being an argument. This reconciliation is not a demand for a separate heavy test on each line.

Settings: "it is read" ≠ "it works". A setting is verified by the end-to-end path "changed it → saw a different result at an observable output, within a known time", including already-computed data (see derived data in [data.md](data.md)). A setting with no observable effect is dead — that is a finding.

A finding of the "data loss or corruption" class: reading code is not enough — either reproduce it safely, or explicitly mark "mechanism confirmed, scale not measured" and queue the required authorized run with an owner. A failed reproduction is scoped evidence, not proof that the mechanism cannot occur.

## Check the checks

A test is verified by mutation: break the behavior under test on an isolated copy — the test must fail. A test that always passes is a defect. Choose mutations at the behavioral boundary/invariant that matters, not mechanically at every source line; preserve the mutation and failing output as evidence, then restore the correct implementation.

Progress invariants (a cursor, a boundary, a window that must move) are tested by a sequence of steps requiring movement at each one — a single "within valid bounds" check lets "stuck" pass. For asynchronous work set an observable completion deadline and assert ownership/recovery where relevant; "worker is alive" alone does not prove progress. A structural property not expressible in behavior (e.g., build splitting) may legitimately be checked by reading the source — with a recorded justification of why behavior cannot check it.

Keep findings under stable IDs in the [work-item system](../process/work-items.md), deduplicate repeated observations, link fixes to independent verification, and reconcile accepted reusable lessons into [project knowledge](../process/project-knowledge.md). Green checks do not close untested dimensions or silently accept residual risk.

Delivery skill: `autoteam-delivery`. Race conditions: `autoteam-quality`. Broad audits: `autoteam-audit`.

# Delivery evidence and checks

Read [QA](../../docs/delivery/qa.md) for check design and [work items](../../docs/process/work-items.md) for evidence identity, status transitions and review history. The [delivery map](../../docs/delivery/README.md) routes specialized checks; language/framework craft and the set of clients belong to the product overlay. Stack selection is in [product stack](../../docs/process/stack.md).

Choose checks by the changed risk: unit for executable rules/calculations; integration for data stores, queues, files and other I/O; contract for a changed interface between parts; end-to-end for the affected critical path. Negative cases, rights and retry/idempotency checks apply when their failure can affect the outcome. Pure copy/layout/document changes may use proportionate inspection or rendering instead of artificial tests; record scope and limits.

A check must distinguish broken behavior from success and confirm that its intended target was exercised. Expected non-empty output is declared where relevant; empty output is not evidence of success by default. Compare implementation with the domain specification, not only with its own tests. If they diverge, record whether code or specification needs an authorized change; do not quietly redefine the requirement to fit the code.

Keep evidence reproducible: candidate and input versions/hashes, environment and relevant tool/dependency versions, command/procedure, output location, result/exit status, criterion coverage and what was not checked. Record any temporary data or configuration manipulation and restoration. Mark a confirmed mechanism whose real scale was not measured as such. Data conclusions need data evidence; a screenshot alone cannot establish them.

An existing test is never changed or weakened silently. The artifact must state what property it guarded, why that property is no longer valid, which alternative was rejected and what now protects the intended behavior. Without this explanation, acceptance rejects the change. The reviewer who repairs code or tests becomes a contributing author; another independent acceptor reviews that candidate.

After a fix, preserve the finding ID and record new evidence. The familiar independent reviewer rechecks the fix and its dependent surfaces; fresh review is added when the risk warrants it. New evidence does not erase old verdicts or automatically carry acceptance to a different candidate. Use the current/stale and justified carry-forward rules rather than treating a green rerun as acceptance.

---
name: autoteam-delivery
description: Deliver a feature, fix or bounded change through reconciled requirements, contract-first and test-first implementation, evidence and independent acceptance. Use for code delivery and implementation decomposition.
---

# Delivery

Combine SDD (agreed meaning), TDD (a meaningful failing check before the fix), contract-first (schema before a changed boundary) and DDD where business languages differ. Match the route and artifacts to risk; a minor change does not require a large specification.

**Input.** Brief, authoritative P-record, pinned requirements/plan/contracts and product stack. **Output.** Minimal candidate diff, versioned evidence and automatic handoff for independent acceptance. **Boundaries.** Do not change a contract or specification silently, accept your own contribution, or infer release permission from implementation permission. Common communication and autonomy rules are in [orchestration](../../docs/process/orchestration.md); execution events and review history are in [work items](../../docs/process/work-items.md).

## Prepare and implement

Preserve the original problem and its observable outcome. Consequential expected behavior needs an independent primary-source/observation check, not only tests derived from the specification. Follow [assurance](../../docs/process/assurance.md) for this check and the mandatory reassessment after two correction returns without outcome progress; retain that history across model switches.

- Reuse the existing `P-*` record, never a parallel task registry. Before coding, reconcile the current requirements, plan and work items: coverage, versions, conflicts, dependencies and acceptance criteria. For complex existing code, inspect affected behavior, entry points, contracts, tests and data flow before finalizing the specification. Unknown feasibility becomes a bounded R&D item.
- Pin inputs and the candidate to versions/hashes. A dirty tree needs its base plus a recoverable patch/snapshot, including relevant untracked files. Record stable author actor IDs and run IDs; role/model/family do not identify a participant. Claim `ready` work as `in-work` with its writable boundary and next action.
- For testable changed behavior, show a meaningful failing check, then the minimal implementation. Choose unit, integration, contract or critical-path checks by the ways it can fail; justify N/A. Keep scope atomic around one outcome. Maintain specification and user/operational documentation when behavior changes, in this cycle.
- Submit candidate, all contributing authors, evidence and limits. Evidence identifies environment/tool versions, commands or procedures, results/exit status and criterion coverage. A green test run or merged PR alone is not acceptance.

## Handoff and acceptance

Task completion triggers the assigned independent review through the orchestrator; pass artifact links and pinned context, not a copied transcript. Record `on-review` only when the handoff succeeds. A block records owner, dependent action and recheck while unrelated work continues.

The author cannot accept the candidate. An orchestrator or reviewer who edits the judged artifact joins its authors and requires another independent acceptor. Separate reviewers submit first verdicts without seeing peer verdicts. Keep immutable review records with reviewer actor/run/model/family, stable findings and exact candidate/input coverage. Normally route fixes back to the familiar independent reviewer; add a fresh perspective by risk. Use [model routing](../../docs/process/model-routing.md) for reviewer selection and optional aggregate budgets.

`CHANGES_REQUIRED` returns the P-item to `in-work` with the original finding IDs. A revised candidate makes affected acceptance stale; obtain re-review or a justified independent carry-forward after impact analysis. Mark `done` only when current independent acceptance, criteria, blocking finding dispositions and required handoff/documentation are complete. Do not turn retries into an unrecorded loop; resolve stalled disagreements under orchestration.

## Checks and related work

Read [reference.md](reference.md) when selecting evidence or handling an existing test change. Stack pin: [product stack](../../docs/process/stack.md). Craft map: [delivery docs](../../docs/delivery/README.md); language/framework rules belong to the product overlay.

Race conditions → `autoteam-quality`; secrets/roles → `autoteam-security`; screens → `autoteam-ui`; behavior/API documentation → `autoteam-docs`; release under the assignment's authority → `autoteam-release`.

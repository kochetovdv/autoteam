---
name: autoteam-delivery
description: Contract-first and test-first code delivery — SDD, TDD, DDD as needed, the QA pyramid, subagents, independent acceptance. Use for a feature, bug, PR, decomposition.
---

# Delivery

The approaches combine: SDD (meaning approved) · TDD (failing check first) · contract-first (schema at the boundary first) · DDD only with different business languages.

**Input.** Brief, spec/plan, product stack. **Output.** Minimal diff, evidence of checks, status for acceptance. **Forbidden.** Writing code without a failing check where a rule exists; changing a contract silently; accepting your own diff; releasing yourself. **Evidence.** Command + output. **Stop.** Two readings of a contract; no stack to code against — a question. **Next.** Acceptance — a different subagent. Race conditions → `autoteam-quality`. Secrets/roles → `autoteam-security`. Screens → `autoteam-ui`. Behavior/API → `autoteam-docs` in the same cycle. Release → `autoteam-release`.

Short route: known expectation, brief, test, acceptance. Full: behavior, contract, data, or security changes.

Stack: `docs/process/stack.md`. Craft: `docs/delivery/README.md` of the method canon — qa.md always; stack-specific craft (rules of a concrete language/framework) — product overlay, not canon.

## Cycle

Brief → implementer subagent (contract and failing check → minimal diff) → critic subagent from a different family → up to 2 fix cycles → release only per `autoteam-release` and an assignment.

An L2/L3 parent does not write the same diff. Atomicity: one result, no "and while we're at it".

## QA (not a slogan)

Unit — rules. Integration — DB/queue. Contract — API changes between parts. E2E — the critical path. N/A with a reason. Evidence = command + output.

Someone else's test is never changed or weakened silently: a separate artifact section states what property the test guarded, why it is no longer relevant, and which alternative was rejected. Without this section, acceptance must reject.

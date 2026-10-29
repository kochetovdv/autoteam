---
name: autoteam-requirements
description: Shape requirements from a statement of work, product intent or scope change into outcomes, boundaries, REQ/NFR, scenarios and acceptance criteria. Use for specification and behavior changes.
---

# Requirements

Define what and why; stack decisions belong to architecture and the product overlay. Separate facts, claims, assumptions and decisions. Preserve the source's meaning and references instead of quietly replacing an inconvenient requirement.

**Input.** Assignment, statement of work, product picture or scope change, plus relevant existing knowledge. **Output.** A versioned specification or inline brief appropriate to risk: outcome and business/user impact, in/out, measurable REQ/NFR, scenarios, acceptance criteria and a batch of unresolved questions. **Evidence.** Each MUST has a scenario and a criterion that distinguishes failure from success. “Fast” without a measure is a claim to resolve, not an invented MUST.

## Scope the route

State the mode: `delivery` (gaps become questions) or `scope` (answers or explicit ASSUMP). A short route can keep the specification and plan in the authoritative P-record for a bounded known change. Use a full route for consequential behavior, contracts, data, permissions or other uncertainty. Choose R&D when feasibility, quality or performance needs a bounded experiment; define the decision rule before promising the feature. No fixed document or subtask count applies.

For complex changes to an existing system, inspect relevant behavior, entry points, data flow, contracts, tests and constraints before writing a settled specification. Record observations, sources and unknowns; code describes current behavior but cannot alone prove intended behavior. Read-only analysis stores artifacts in the allowed output workspace and links them; it does not initialize, copy or commit the analyzed repository.

## Form and maintain the specification

Anchor the original problem and observable outcome. For consequential or disputed interpretation, obtain an independent derivation of decisive expected observations from primary material before the checker sees the author's derived expectations; reconcile it with the specification under [assurance](../../docs/process/assurance.md). A second agent copying the same summary is not a semantic check.

Work from problem and roles through boundaries, glossary and scenarios to measurable REQ/NFR and observable acceptance. Include data and permissions when people, money, personal data or devices are involved. Keep questions together; block only the work whose required input is missing, under [orchestration](../../docs/process/orchestration.md). Store interactive pending decisions as well as hard stops; continue independent work. In autonomous mode use explicit assumptions/decisions within the existing authority rather than silently inventing approval.

Before implementation, reconcile requirements, plan and existing `P-*` work items: exact revisions/hashes, criterion/REQ/NFR coverage, dependencies, gaps, contradictions and their resolution. Reuse the authoritative P-record; do not add a competing task registry. See [work items](../../docs/process/work-items.md) and [project knowledge](../../docs/process/project-knowledge.md). A lightweight change may record the reconciliation inline.

Use `Draft | Approved | Superseded` for specification maturity; approval follows the cycle's mode and authority. Implementation design belongs to the plan. Behavioral decisions amend the specification and dependent plans/P-records together, with version and rationale; never rewrite them silently. Reassess affected evidence and acceptance as current/stale after changes. A passing implementation test is not proof that the stated requirement was the right one.

Next: design → `autoteam-architecture`; scope → `autoteam-scope`; code → `autoteam-delivery`; changed behavior documentation → `autoteam-docs`. Domain input: [product domains](../../docs/product/domains.md).

# Assurance: audits and challenged claims

Assurance asks whether a conclusion is supported, what can still break, and where evidence is missing. It applies to a brief, design, code, test, calculation, business hypothesis, and an existing product. Confidence has a scope and a date; a green suite or agreement between agents is not proof of the whole product.

Use this document with [work items](work-items.md), [orchestration](orchestration.md), [project knowledge](project-knowledge.md), [resource lifecycle](resource-lifecycle.md), and [QA](../delivery/qa.md). The complete canon bundle includes these documents; the audit skill carries a short fallback for environments where the bundle is temporarily unavailable.

## Three different jobs

| Job | Result | Does not imply |
|---|---|---|
| Audit | A dated review of selected scope, coverage, findings, and evidence | Every dimension was tested exhaustively or all findings were fixed |
| Monitoring | Repeated observations against an explicit baseline and materiality rule; see [monitoring](monitoring.md) | Sources are always fresh or a scheduler is installed |
| Remediation | A work item that changes the product or process and is independently verified | The original finding was wrong because a fix now exists |

A monitor may request a focused audit or target check. An audit may recommend a monitor. Each links to the same authoritative finding/work item; it does not open another competing status ledger. Continue independent work; only scope exposed to a Blocker stops.

## Common challenge protocol

Use this sequence whenever a claim matters to a decision or is disputed:

1. **Claim.** State a falsifiable assertion, its scope, and the decision it supports. Separate an observation from an interpretation and a preference.
2. **Assumptions.** Name the required inputs, domain rules, permissions, timing, data quality, and environmental conditions. Record unknowns instead of silently treating them as true.
3. **Counterexample.** Seek the smallest plausible case that would make the claim false. Ask what the proposed criterion would report if the behavior were broken. A critique also needs a mechanism or a testable counterexample.
4. **Controlled probe.** Before running it, define the discriminating observation, expected result, bounds, and stop condition. Use a safe reproduction, source reconciliation, measured workload, or bounded customer experiment. Keep raw evidence and identify revisions, data, environment, and time. Controlled data modification follows QA isolation rules.
5. **Verdict.** Record `CONFIRMED`, `REFUTED`, or `INCONCLUSIVE`, limited to the tested scope and assumptions. Include evidence, remaining uncertainty, and the next action, owner, and review trigger/date. Confirmation is not a universal guarantee; lack of a reproduction is not refutation.

Choose a probe proportional to consequence and uncertainty. A short source check can resolve a copy edit; races, calculations, permissions, and irreversible actions need stronger discrimination. Do not create a heavy test for every source line. Inspect structural properties directly when behavior cannot establish them, and record why. For domain logic, reconcile specification and implementation in both directions; either can be stale.

The protocol challenges briefs, findings, review comments, tests, and acceptance evidence as well as implementation. A passing test is itself a claim: demonstrate that it detects a relevant break. A critic's confidence, seniority, number of agents, or majority vote does not settle a factual disagreement. Use evidence-driven convergence; record unresolved assumptions and choose another probe. If repeated attempts add no evidence, expose the cost and decision needed instead of retrying indefinitely.

Demand, usability, willingness to pay, retention, and economic outcomes require suitable evidence from actual or prospective customers, observed use, or a real bounded experiment. Agents can design and criticize a hypothesis; their simulated agreement cannot validate it. Label forecasts, interviews, observed behavior, and paid transactions separately, including sample limitations.

## Independent meaning and convergence

Before costly implementation, anchor the task in the original problem: observed starting state, intended user/business outcome, authoritative sources and dates, one observable success/failure distinction, and boundaries. Keep this inline for small work. Derive critical expected outcomes from these inputs, not solely from the proposed implementation. Passing an agreed specification can still faithfully implement a mistaken interpretation.

For consequential or disputed meaning, assign an independent semantic check as well as candidate acceptance. The checker must not own the interpretation being challenged. Before seeing the author's derived expectations or peer verdicts, inspect the relevant primary material and record their own expected observations for the decisive scenarios. Preserve relationships in diagrams/tables, exceptions, timing, units and permissions, not just extracted words. Then reconcile differences with the brief/specification and observable behavior. A copied expected result, a different model name, or tests derived from the same mistaken summary do not provide this independence. If primary material is unavailable or ambiguous, record that limitation; resolve a consequential ambiguity before dependent implementation, without silently rewriting the user's intent. Independent calculations or direct observations may supply the needed check when no document exists.

Track progress against the anchored outcome after each material return: what changed in observed behavior or decisive evidence, which failure remains, and whether the same assumption still drives the fix. Patch counts, closed comments, green tests and model switches are activity, not evidence of that progress. Preserve findings, rejected approaches and measurements across handoffs so a new model does not restart the same search.

Two consecutive correction returns without demonstrated progress toward the same outcome trigger a mandatory goal/approach reassessment, earlier for a recurring defect or a contradiction in the premise. Pause the affected patch chain; do not spawn another implementer with the same brief. Recheck the starting observation, source interpretation, causal hypothesis, adequacy of the acceptance check, and whether scope or environment changed. Choose one bounded discriminating investigation and record its question, expected evidence, owner and limit. The decision is to repair within a supported approach, change the approach/specification explicitly, reduce scope with applicable authority, or stop dependent work with an explained blocker. Unrelated work continues. A new cycle requires a recorded decision and a materially changed premise, approach or evidence; changing the model, task ID or wording does not reset the history or limit. No number of returns grants acceptance.

## Critique from other angles, with a limit

Ask: **Where could our understanding be wrong? Under which plausible conditions will this fail? What uncomfortable question could overturn this decision?** Select the relevant perspectives rather than reciting a universal questionnaire:

- User/business: the requested outcome versus a convenient proxy; who bears the effort, loss or side effect; whether a simpler alternative solves the problem.
- Meaning/evidence: missing relationships, shared assumptions, circular tests, dates and conditions; what observation would overturn the conclusion.
- Execution/time: cancellation, late results, lost acknowledgements, restart, offline operation, races, recovery and ownership.
- Product/process incentives: whether the rule optimizes reports, agent agreement or throughput at the expense of value, attention or total effort; when its cost exceeds the risk it reduces.

A useful objection names a plausible context, failure mechanism, consequence and discriminating check. Separate a confirmed defect, a testable hypothesis, an accepted tradeoff and a preference. Severity follows exposure and consequence; a wish for another feature or an imaginable catastrophe alone is not a delivery blocker. A new angle matters when it can change the decision, not merely increase the list of questions.

The coordinator sets a finite critique scope and stop condition from the task/profile; the user need not configure them. Unless a different bound is justified up front, use **one broad independent pass and one targeted recheck** of material findings, changed clauses and neighboring effects. These two rounds belong to the same decision across agents and models. Ordinary mandatory acceptance checks still apply; this default bounds open-ended challenge, not correctness obligations. Continue an additional critique round only by recording the new decision-relevant evidence/question, its finite allocation and why existing checks cannot settle it. Novel wording or a fresh critic alone is insufficient; repeated extensions without outcome progress trigger the reassessment above. Any user hard cap remains binding.

Stop the critique when the decision is supported within the declared scope or when the bound/available evidence is exhausted. No obligation to invent findings or prove universal perfection. Return the supported conclusion, material unresolved risks, untested areas and next decision. Exhaustion is not acceptance: a material contradiction remains unaccepted; nonblocking improvements and explicit authorized residual risks do not force an endless pass. A diagnosis or a bound extension also has an endpoint; if its question remains unresolved, report the blocker/options instead of opening another nominally new loop.

## Coverage map

At an audit, scan all applicable dimensions broadly, then spend depth where impact, uncertainty, change, or weak evidence makes it valuable. Applicability belongs to the project profile, not to a universal checklist. An omitted domain is `UNKNOWN` until assessed; `N/A` requires a reason and a trigger to reconsider.

| Dimension | Typical questions and discriminating evidence |
|---|---|
| Security and privacy | Trust boundaries, server-side permissions, tenant isolation, secrets, sessions, dependency exposure; negative permission probes and threat evidence |
| Reliability and state | Offline/reconnect, timeouts, hangs, stalled progress, partial failure, retries, races, idempotency, worker death/restart, ownership/lease loss; controlled failure and recovery sequences |
| Calculations and data | Domain formulas, units, rounding, boundaries, stale/derived data, migration and reconciliation; independent expected values and specification ↔ code reconciliation |
| Performance and capacity | Representative volume, concurrency, latency, memory, queues, saturation, cost; measured baseline and explicit budgets |
| Architecture | Ownership, contracts, dependencies, failure boundaries, maintainability, drift and temporary workarounds; system map and relevant decision records |
| Operations | Deploy/rollback/restore, observability, alert routing, runbooks, resources and missed background work; exercised procedures and operational evidence |
| Product hypotheses and UX | Who needs it, outcome, critical journeys, accessibility, friction, real use; customer evidence and observed task completion |
| Economics | Revenue assumptions, pricing, unit costs, limits, conversion and payback; sourced inputs, sensitivity and observed transactions where applicable |
| Process and documentation | Work-item truth, independent acceptance, knowledge freshness, obsolete instructions, skill/canon drift, repeated failures; sampled records and source reconciliation |

For each dimension/scope, record:

- applicability and reason; risk/impact and uncertainty;
- depth (`SCAN`, `TARGETED`, `DEEP`, or `NOT_CHECKED`) and what was actually examined;
- evidence links with revision/configuration, sample/workload, timestamps, limitations, and verdict;
- last check, next check or event trigger, owner, due status, and reason for any unknown/overdue entry.

Use an actual date/time with timezone for scheduled checks. If there is no defensible next date, use `UNKNOWN` with reason, owner, and an action to establish it. An event trigger has an owner and a backstop date so silence cannot defer review forever. `NOT_CHECKED`, stale evidence, inaccessible data, and `N/A` do not count as passed. A deep review of one flow does not cover its neighbors automatically. Expose overdue checks and newly unsupported claims in the coordinator's next prioritization.

## Cadence and depth

The coordinator proposes the coverage, triggers, and budget from the project profile, user preferences, failure cost, change rate, freshness of evidence, and available capacity. Reuse an agreed profile; do not ask the same setup questions each cycle. Record why the chosen cadence can catch meaningful drift in time.

The existing architecture cadence (active work: about a week or eight closed tasks; quiet product: about a month) is an opportunity to refresh the broader risk scan. It does not impose that frequency on every audit dimension or external news source. A small low-risk commit needs its relevant checks, not a full-system sweep. Accumulated changes, stale evidence, incidents, changed business assumptions, a new data store/trust boundary, or a material monitor signal can justify deeper or out-of-band work.

An audit has a bounded question, scope, evidence budget, and completion criterion. Start with the broad coverage map, explain the selected deeper probes and exclusions, then stop when the question is answered or the budget/available evidence is exhausted. An incomplete scan is reported as incomplete, with follow-up; it is not a clean bill of health.

## Findings to durable learning

1. **Identify and deduplicate.** Use a stable finding ID from the work-item system. Search existing findings first; attach repeated observations and link duplicates to the authoritative record. An `AUD-*` report is evidence, not a second finding-state owner.
2. **Characterize.** Record claim, affected scope/revision, impact, severity, uncertainty, reproduction/evidence, assumptions, and the condition that would refute it. Distinguish a confirmed mechanism from an unmeasured prevalence. A missing probe is a gap, not an invented pass or confirmed incident count.
3. **Prioritize.** The coordinator considers impact, likelihood/exposure, urgency, confidence, dependencies, and cost. Keep accepted risk explicit with owner, rationale, expiry/review trigger, and residual exposure. Do not silently close it as fixed.
4. **Route work.** Link a remediation/research/target-check work item with an owner and acceptance criterion. A report author does not quietly fix and accept their own conclusion in the same role. Emergency action follows the product's incident procedure and authority.
5. **Verify independently.** Another reviewer challenges the mechanism and the correction using the relevant before/after and negative cases. A failed reproduction can narrow or refute a finding only within the tested scope. Preserve history and reopen the same finding if the defect returns.
6. **Accept knowledge.** After the decision/verification is accepted, reconcile reusable facts, constraints, and lessons into [project knowledge](project-knowledge.md), with provenance, scope, confidence, date, and invalidation trigger. Draft impressions and unresolved hypotheses remain labeled. Update misleading documentation in the same change.

An audit can finish with open findings if they are visible and routed. A remediation item is complete only after its own acceptance. Neither a report nor a monitor bypasses human authority for money, external communication, release, or irreversible actions.

## Audit handoff

Use [the audit template](../../templates/audit.md). Return the question and scope, coverage/depth map, evidence and verdicts, stable finding links, work that can continue, bounded follow-ups, and proposed cadence changes. State what remains unknown and why. Preserve the report in the product's agreed location and link it from the authoritative work item.

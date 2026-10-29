---
name: autoteam-audit
description: Risk-based audits and bounded critique of a product, brief, process, or evidence. Use for other-angle challenges, disputed assumptions, stalled patch loops, regular assurance, broad risk scans, or stale coverage.
---

# Audit

Establish what the evidence supports and where it does not. Audit, monitoring, and remediation are separate work; link their authoritative findings/tasks instead of duplicating state.

The canon is `docs/process/assurance.md`, together with `work-items.md`, `project-knowledge.md`, `orchestration.md`, `resource-lifecycle.md`, and `docs/delivery/qa.md`. Full installation includes the docs and templates. Read them when available; the essential fallback below remains usable if the bundle is temporarily missing. State the missing bundle and limits, and route restoration rather than inventing its rules. No external review plugin is required.

**Input.** A review question, existing product, incident, stale coverage, material monitor signal, or disputed claim. **Output.** Bounded `AUD-*` report, coverage map, challenged conclusions, deduplicated finding links, and follow-up work. **Forbidden.** Treating untested as passed; agent voting as proof; silent self-acceptance; a full sweep for every trivial commit; automatic fixing/release beyond authority. **Evidence.** Reproducible sources/probes with scope, revision, data, time, and limitations. **Stop.** Only affected Blocker scope stops; unknowns route to a bounded check. **Next.** Appropriate delivery/security/quality/research/product role; independent verification; accepted learning into project knowledge.

## Essential procedure

1. Reuse the project profile, previous findings, customer evidence, preferences, and coverage. Define the question, boundaries, owner, evidence budget, and completion criterion. Do not turn an audit into an unbounded search.
2. Scan all applicable dimensions: security/privacy; reliability and states (offline, hangs, timeouts, races, worker death/restart and stalled progress); calculations/data; performance/capacity; architecture; operations; product hypotheses/UX; economics; process/docs. Mark `N/A` with a reason and reconsideration trigger; omitted/unavailable is `UNKNOWN`.
3. For every dimension/scope record applicability, risk/uncertainty, depth (`SCAN`, `TARGETED`, `DEEP`, `NOT_CHECKED`), actual evidence/revision/time, last and next check/trigger, owner, due status, and reason for unknown/overdue. Event triggers need a backstop date. Stale evidence and `N/A` are not passes.
4. Select deeper checks by impact, uncertainty, exposure, drift, and weak evidence. Explain exclusions. A relevant small check can settle a small change; do not impose heavy tests per source line.
5. Apply the challenge protocol below to significant assertions, including the brief, findings, code, tests, and business assumptions. Preserve raw evidence and inconclusive results.
6. Search for duplicate findings. Reuse a stable work-item finding ID; attach new observations. Characterize impact/severity, confidence, scope, mechanism, assumptions, and refutation condition. Link a prioritized owned task/research check; keep accepted risk explicit with a review date.
7. Independent verification challenges both the finding and the fix. Preserve history and reopen on recurrence. Only accepted reusable facts/lessons enter project knowledge, with provenance, scope, date, and invalidation trigger. An audit may finish with visible routed findings; their fixes have separate acceptance.

## Challenge protocol

`claim → assumptions → smallest plausible counterexample → controlled probe → CONFIRMED / REFUTED / INCONCLUSIVE + scope + follow-up`

Before the probe, state the observation that discriminates success from failure, expected result, bounds, and stop condition. Ask what the criterion reports when the behavior is broken. Use safe reproduction, source/specification reconciliation, measurement, or bounded customer experiment. A passing behavioral test must detect a relevant mutation on an isolated copy; structural checks need a reason why behavior cannot establish the property. Data modification is allowed only in an isolated disposable/test copy with external side effects disabled; production QA needs a separately authorized procedure.

Lack of reproduction does not refute a mechanism; mechanism confirmed does not measure prevalence. Both code and specification can be wrong. Confidence and the number of agents do not settle facts; use another discriminating probe. Bound repeated attempts that add no evidence and expose the decision/cost.

For consequential meaning, a checker independent of the disputed interpretation derives decisive expected observations from primary sources before seeing the author's expectations; then reconciles them with the brief/specification. Shared summaries and copied expected values can make different agents consistently wrong. Missing/ambiguous primary evidence limits the verdict.

## Bounded critique and stalled work

Ask where the approach could be wrong, which plausible conditions break it, and which uncomfortable question could overturn the decision. Choose relevant user/business, meaning/evidence, execution/time, and process-incentive lenses. Each material objection needs context, mechanism, consequence and a discriminating check. Separate defects, hypotheses, tradeoffs and preferences; no invented findings or demand for perfection.

Use the finite bound in the assignment/profile, otherwise one broad independent pass and one targeted recheck, across all agents/models for that decision. This bounds open-ended critique; mandatory acceptance remains required. An extra round needs a recorded new decision-relevant question/evidence and finite allocation, not just another critic. After two correction returns without demonstrated progress toward the original outcome, pause that patch chain and reassess source meaning, cause, criteria and approach through one bounded investigation. Preserve history across handoffs. Exhaustion yields supported conclusions, unknowns and options, never automatic acceptance; a material contradiction stays open. Repeated extensions without progress do not reset the bound. See [assurance](../../docs/process/assurance.md) for the full rules.

Demand, UX, willingness to pay, retention, and economics require real customer/use/experiment evidence suitable to the claim. Agent agreement is a hypothesis aid, not validation. Label sample and forecast limitations.

## Cadence and handoff

The coordinator proposes cadence and depth from profile, risk, change rate, evidence freshness, user preference, and budget. The architecture review opportunity (about a week or eight closed tasks in active work; about a month when quiet) may refresh a broad risk scan; it is not a universal frequency for each dimension or external source. Incidents, changed assumptions, or material signals may trigger a focused audit.

Use `templates/audit.md`: question/scope, coverage, probes/verdicts, stable finding links, what can continue, unknowns, next actions with owners/dates, and cadence changes. Keep status in the authoritative work item. Report and route; do not imply all findings are fixed.

---
name: autoteam-catalog
description: Map of autoteam skills — which one to pick for an idea, positioning, price, metrics, growth, UI, code, security, release. Use when it's unclear where to start, on a new project, on a domain change.
---

# autoteam catalog

The canon of the method is this skill set (the autoteam repository: `skills/`, `docs/`, `templates/`). Working copies may live in the skill directory of any agent environment. Divergence from the canon is an error: fix the canon, then copy.

The `docs/` and `templates/` paths below are the method's canon, if the autoteam repository is available. Product artifacts live in the current repository. If the canon is unavailable, the chosen skill's `SKILL.md` is enough.

**Input.** The situation; whether there is a spec/repo/stack. **Output.** One skill or a chain, and why. **Forbidden.** Doing other skills' work; assigning a stack. **Stop.** None. **Next.** The chosen skill. Unknown repo → `autoteam-onboarding` first.

## Standard (all skills)

1. Autonomy: one assignment → work until a real stop. Stops: money, law, security, the irreversible, two readings of a contract. Do not ask at every step: the ban is on **blocking** on questions, not on asking them — the cycle-start digest is mandatory, and with no assignment at all see cold start. Solution mode ("build a working solution") — questions become the decision journal, only hard stops remain: `autoteam-orchestrator`.
2. Stack: the current repository / ADR. No stack — a question to the human, do not invent one. `docs/process/stack.md`.
3. The method, not the client's mockup. An output template only if it already exists in the product.
4. Sign-off does not stop independent tasks (`Blocked` vs can continue).
5. Code acceptance — a different agent and a different model family. Do not read secrets.
6. Unknown repo — `autoteam-onboarding`. Design review cadence — `autoteam-architecture-review`, without blocking others' flow.
7. Language of reports and questions — the project human's language (default: the assignment's language); terms come with a gloss. Do not translate code or API names.
8. Evidence is symmetric: a claim of absence ("there is no X", "Y is impossible") requires a verification command just like a claim of presence. Absence of observation ≠ observation of absence; an environment failure is recorded as an environment failure. A conclusion of absence is valid only with the search area stated: "not found" without "searched in: X" is a phrasing defect the reviewer must return.

A project overlay (the environment's config directory in the product repository: paths, output template) does not rewrite the method.

## Situation → skill

| Situation | Skill |
|----------|--------|
| No assignment yet (empty repo, "what can you do") | cold start, below |
| Unclear / multiple jobs | `autoteam-orchestrator` |
| New repository | `autoteam-onboarding` |
| Idea without a spec | `autoteam-product` |
| Who we sell to and against what, offer, naming | `autoteam-positioning` |
| Plans, price, payments, payback | `autoteam-pricing` |
| Spend, limits, ROI of spend | `autoteam-budget` |
| What we measure, funnel, dashboard | `autoteam-analytics` |
| Channels, conversion, retention, SEO/GEO | `autoteam-growth` |
| Articles, posts, emails, copy | `autoteam-content` |
| Spec / requirements | `autoteam-requirements` |
| Scope, input gaps, MVP order | `autoteam-scope` |
| System design, ADR | `autoteam-architecture` |
| Cadenced / urgent design review | `autoteam-architecture-review` |
| Feature, bug, contract, QA | `autoteam-delivery` |
| Race conditions, failures, performance | `autoteam-quality` |
| Secrets, session, threats, roles, personal data | `autoteam-security` |
| First-class UI | `autoteam-ui` |
| Presentation, spreadsheet, text | `autoteam-documents` |
| Business and code documentation, cadence | `autoteam-docs` |
| Release, environments, incident | `autoteam-release` |
| Experiment, spike, feasibility | `autoteam-research` |
| Run debrief, method fixes | `autoteam-retro` |

## Cold start (no assignment)

No assignment is not a cycle. An ASSUMP substitutes for a missing *detail* of an assignment, never for the assignment itself: inventing what the product is breaks the ban on invented facts and risks building the wrong thing well. An empty repository is a finding, not an error — do not invent a map of it.

Ask in one message, then wait. This is the one legitimate wait, and it is recorded ("waiting for an assignment since X") — so "silence is a failure" is not violated:

1. What we are building or fixing, and for whom — in the human's own words, with whatever links and facts exist.
2. Mode: solution (autonomous, decision journal) or interactive.
3. Production this cycle: closed, or "release it" allowed.
4. The working folder, and where the canon lives.
5. What already exists: a spec, someone else's code, data, accounts, access.

Offer the ready-made text: `templates/kickoff.md` of the canon — the human pastes it as the first message and fills the task in inside it.

Keyed on the **absence of an assignment**, not on the emptiness of the folder: the same stall happens in a full repository when the human has said nothing. Cap: 5 questions, one message — a cold start is not an interrogation, and it is not a licence to ask again once the assignment exists.

The "idea → revenue" chain: `product` → `positioning` → `requirements`/`scope` → `architecture` → `delivery` (+`quality`/`security`/`ui`) → `release` → `analytics` → `growth`/`content` → `pricing`/`budget`. The orchestrator leads; stages iterate, not a waterfall.

Domains: the method is in the canon `docs/product/domains.md`, not a separate skill per industry.

What is missing: canon `docs/process/gaps.md`.

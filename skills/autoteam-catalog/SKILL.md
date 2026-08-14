---
name: autoteam-catalog
description: Map of autoteam skills — which one to pick for an idea, positioning, price, metrics, growth, UI, code, security, release. Use when it's unclear where to start, on a new project, on a domain change.
---

# autoteam catalog

The canon of the method is this skill set (the autoteam repository: `skills/`, `docs/`, `templates/`). Working copies may live in the skill directory of any agent environment. Divergence from the canon is an error: fix the canon, then copy.

The `docs/` and `templates/` paths below are the method's canon, if the autoteam repository is available. Product artifacts live in the current repository. If the canon is unavailable, the chosen skill's `SKILL.md` is enough.

**Input.** The situation; whether there is a spec/repo/stack. **Output.** One skill or a chain, and why. **Forbidden.** Doing other skills' work; assigning a stack. **Stop.** None. **Next.** The chosen skill. Unknown repo → `autoteam-onboarding` first.

## Standard (all skills)

1. Autonomy: one assignment → work until a real stop. Stops: money, law, security, the irreversible, two readings of a contract. Do not ask at every step. Solution mode ("build a working solution") — questions become the decision journal, only hard stops remain: `autoteam-orchestrator`.
2. Stack: the current repository / ADR. No stack — a question to the human, do not invent one. `docs/process/stack.md`.
3. The method, not the client's mockup. An output template only if it already exists in the product.
4. Sign-off does not stop independent tasks (`Blocked` vs can continue).
5. Code acceptance — a different agent and a different model family. Do not read secrets.
6. Unknown repo — `autoteam-onboarding`. Design review cadence — `autoteam-architecture-review`, without blocking others' flow.
7. Language of reports and questions — the project human's language (default: the assignment's language); terms come with a gloss. Do not translate code or API names.
8. Evidence is symmetric: a claim of absence ("there is no X", "Y is impossible") requires a verification command just like a claim of presence. Absence of observation ≠ observation of absence; an environment failure is recorded as an environment failure.

A project overlay (the environment's config directory in the product repository: paths, output template) does not rewrite the method.

## Situation → skill

| Situation | Skill |
|----------|--------|
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

The "idea → revenue" chain: `product` → `positioning` → `requirements`/`scope` → `architecture` → `delivery` (+`quality`/`security`/`ui`) → `release` → `analytics` → `growth`/`content` → `pricing`/`budget`. The orchestrator leads; stages iterate, not a waterfall.

Domains: the method is in the canon `docs/product/domains.md`, not a separate skill per industry.

What is missing: canon `docs/process/gaps.md`.

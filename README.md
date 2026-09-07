# autoteam

A skill library for an autonomous agent team: **how to think and how to build** from idea to revenue — work through and position the idea, design the product, build it, and take it to revenue. A baseline method: copied wholesale into any project and any agent environment (Claude, Cursor, your own runner), not tied to a customer, stack, or tool.

The canon is this repository: `skills/`, `docs/`, `templates/`. Change the canon here, then propagate the copies. Never leave two diverging versions.

English is the canonical language. Русская версия: [ru/](ru/README.md) — a maintained locale, updated in the same commit as the canon; when in doubt, English wins.

## Layers: method and product

| Layer | Question | Where |
|------|--------|-----|
| **Method (this repository)** | How to reason, design, write, review, release, grow | `skills/`, `docs/`, `templates/` |
| **Current product** | Stack, paths, overlay, output template if one exists | the repository where the work happens |

The product's output template (if any) defines *where to put* the result. It does not replace the method.

## How to plug in

1. Canon: folders `skills/autoteam-<name>/` (containing `SKILL.md`, and `reference.md` where needed).
2. Copy the folders you need into your agent environment's skills directory — wholesale, no edits. The copy is a cache: at cycle start in a product with the canon available, onboarding overwrites it with a fresh copy.
3. In a specific product you may add a thin overlay (paths, prohibitions, your own `docs/process/model-routing.md`, output template) in that repository's environment config directory. The overlay does not rewrite the method.

The language of reports and questions to the human is the project human's language (by default, the language of the assignment). Explain each technical term on first use. Do not translate code or API names.

## Stack

The stack comes from the current repository / ADR. No stack — pin it down with the human (in "solution mode" — pick the minimal sufficient one and record it in the journal). Details: `docs/process/stack.md`.

The client mix (web / responsive / PWA / cross-platform / native) is a per-project decision: never add a new platform silently; if there is a requirement — an explicit fork with its cost.

## Map: situation → skill

| Situation | Skill |
|----------|--------|
| No assignment yet: an empty folder, a fresh copy of the canon, "what can you do" | cold start: `autoteam-catalog` |
| Unclear where to start | `autoteam-catalog` |
| Multiple roles, autonomy, subagents | `autoteam-orchestrator` |
| New repository, "agent, find your bearings" | `autoteam-onboarding` |
| Business idea, no spec, demand validation | `autoteam-product` |
| Who we sell to and against what, offer, naming | `autoteam-positioning` |
| Plans, pricing, payments, payback | `autoteam-pricing` |
| Costs, limits, ROI of spend | `autoteam-budget` |
| What we measure, funnel, dashboard | `autoteam-analytics` |
| Channels, conversion, retention, SEO/GEO | `autoteam-growth` |
| Articles, posts, emails, copy | `autoteam-content` |
| There is a spec | `autoteam-requirements` |
| Scope, input gaps, MVP ordering | `autoteam-scope` |
| How to structure the system, ADR | `autoteam-architecture` |
| Regular or urgent review of the system's structure | `autoteam-architecture-review` |
| Feature, bug, tests, contract | `autoteam-delivery` |
| Race conditions, failures, performance | `autoteam-quality` |
| Secrets, sessions, threats, roles | `autoteam-security` |
| First-class UI: landing page, SaaS, admin panel | `autoteam-ui` |
| Presentation, spreadsheet, business writing | `autoteam-documents` |
| Product and code documentation, when to update | `autoteam-docs` |
| Release, environments, incident | `autoteam-release` |
| Hypothesis-driven experiment, spike | `autoteam-research` |
| Run debrief, method fixes | `autoteam-retro` |

The "idea → revenue" loop: `product` → `positioning` → `scope`/`requirements` → `architecture` → `delivery` → `release` → `analytics` → `growth`/`content`/`pricing`/`budget` → back to `product`. Not a waterfall: numbers and feedback change the picture.

Process details: `docs/process/`. Delivery craft: `docs/delivery/` (language-specific only if that language is already in the product).

## Autonomy and "solution mode"

The human gives one assignment. The orchestrator launches subagents in waves on its own. A critical approval does not freeze an independent stream.

The assignment "turn the idea into a working solution" enables "solution mode": the cycle runs non-stop, every question that would have gone to the human becomes an entry in the decision journal (`templates/decisions.md`), and the result is a complete working solution — not an MVP with gates and todos. There are three hard stops: external money; law and public commitments; irreversible destruction. Production — only on an explicit "release it". Details: `docs/process/orchestration.md`.

Unknown repository — `autoteam-onboarding` first. Do not read or copy secrets. Code acceptance — by a separate agent; a different model family if the environment provides one.

## Architecture review cadence

- Active development: once a week **or** every ~8 closed tasks (whichever comes first).
- Quiet product: once a month.
- Out of band: an incident involving data/a race condition/a boundary; a new store or service.

The review does **not** stop other tasks. Only work that runs into a Blocker stops. Template: `templates/architecture-review.md`. Skill: `autoteam-architecture-review`.

## What is not here

An honest list of holes: [`docs/process/gaps.md`](docs/process/gaps.md).

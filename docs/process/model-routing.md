# Model routing

Choose the model by **role and cost of error**, not by "the most expensive one". The method is not tied to a specific environment: substitute the models available in your runner (Claude, Cursor, your own orchestrator).

Specific model ids are not this repository's source of truth. A product may have its own `docs/process/model-routing.md` — read that one.

## Principles

1. Match role to risk: L1 routine, L2 ordinary delivery, L3 data / race conditions / security / architecture.
2. Take the minimally sufficient model.
3. Acceptance — a separate agent; a **different model family** if the environment offers several.
4. One family in the environment → an acceptor with fresh context and a critic's role (look for reasons to reject), a `same-family` note in the handoff; decisions with costly reversibility go to the human via the journal. Auto-`ACCEPTED` without a separate acceptor is always forbidden.
5. An expensive model is not assigned "just in case".
6. If two models were trained on each other, they are a weak acceptance pair for data and SQL; prefer clearly different families.

## Example: one family, tiers (substitute your environment's ids)

| Role | Tier |
|------|-----|
| Routine: copying, scans, formatting | light |
| UI/content/document implementers; orchestration | mid |
| L3: architecture, data, security, money | senior |
| Board critics | senior; always ≥ the implementer's tier |

Don't skimp on critics: a critic weaker than the implementer is acceptance theater. A light tier on routine is speed and money, not a quality compromise.

## Role → level (logic)

| Role | Level | Rationale |
|------|---------|--------|
| Analyst, planner, orchestrator | L2 | artifact synthesis |
| Architect, design review | L3 | boundaries and risk |
| UI/routine implementer | L1–L2 | fast edit cycle |
| Data/race-conditions implementer | L3 | strong reasoning |
| Acceptance | ≥ the implementer, separate agent | |
| R&D | long tool-loop | |
| Release | L2 | follows the patch, doesn't invent scope |
| Onboarding | L2 | maps the repo, doesn't rewrite the product |
| Content, documents | L1–L2 | facts from the input |

Routing record (in task/handoff):

```text
Routing level: L1 | L2 | L3
Model: <id from the project's environment>
Model family: <family>
Task class: feature | bugfix | data | concurrency | docs | R&D | ops | release | content
Data evidence required: yes | no
Reviewer: <separate agent; family or same-family>
Baseline deviation reason: none | …
```

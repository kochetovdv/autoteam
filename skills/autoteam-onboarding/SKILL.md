---
name: autoteam-onboarding
description: Agent onboarding into a new repository — map, stack, do not read secrets, overlay, first brief. Use on a fresh clone, on "get familiar", on the first chat in an unknown repo.
---

# Agent onboarding into a repository

Goal: in one pass understand **how to work here**, without rewriting the product.

**Input.** The root of the current repository. **Output.** A map: stack, overlay, contracts, how things are checked and released, holes, first safe step. **Forbidden.** Reading secret values; changing the stack; a "spring cleaning"; copying secrets into chat or another repository; recording an environment or product limitation without empirical verification — absence of observation is not observation of absence: a limitation is recorded together with the command that verified it; a tool failure is a property of the environment, not of the product. **Evidence.** Facts from files (lockfile, README, ADR), not guesses. **Stop.** None, except a secret in git — then a Blocker for that finding. **Next.** Assignment → `autoteam-orchestrator` or a role from the catalog.

## Order

1. Root: README, `docs/CURRENT.md` or equivalent, `docs/process/` if present.
2. Stack as-is (lockfile, manifest, compose, ADR). Record the fact. No stack — put "stack not set" in the map, do not assign a language. Rule: method canon `docs/process/stack.md`.
3. Agent environment overlay: config directories in the root (`.claude/`, `.cursor/`, `CLAUDE.md`, `AGENTS.md` and equivalents), the product's own `docs/process/model-routing.md`.
3a. A copy of the autoteam canon in the product is a cache: when the canon is available, refresh it wholesale at cycle start (overwrite, do not diff piecemeal), record it in the handoff. If the canon has a remote source (git remote) and the network is up — update the canon itself first (`git pull`), then copy. The canon version (tag/commit) the cycle started on goes into the brief; the canon is never updated mid-cycle. Canon unavailable — work from the copy. Working from a stale copy while the canon is available is an error.
3b. Which other agent environments work in this folder (config directories, fresh foreign edits) — into the map as a risk: two environments working the same folder at once is a perimeter incident, not background noise.
4. Secrets: know the path (`secrets/`, `.env.example`), do **not** output values, do not commit.
4a. Resource inventory: which accounts, accesses, environments, and data the product already has (from `.env.example`, deploy, runbook, docs — without reading values) → the product's `docs/process/resources.md` registry, template `templates/resources.md` of the canon.
5. Contracts: OpenAPI / AsyncAPI / SQL init / protobuf — what exists.
5a. Domain and algorithm specifications (docs, ADRs, documents referenced by code comments) — into the map as sources of truth. An explicit reference from code to a document is a mandatory edge: saw it — open it; didn't open it — that is a recorded perimeter narrowing, not silence.
6. How things are checked: test commands from the README.
7. How things are released: `deploy/`, the product's runbook. The method — `autoteam-release`, not another product's hosts.
8. Review cadence and documentation: is there `docs/architecture/reviews/`, kb.
8a. Product artifact conventions: before creating an artifact in the product's format, read neighboring instances of the same type (numbering, statuses, mandatory sections, entry point). A format derived from the README that diverges from the actual files is an artifact defect.
9. Return the map: what is the product's canon, what is a hole, what is the first safe step.

If the product has no short map for the next agents — write `docs/process/agent-onboarding.md` in **this** repository. Do not wait to be asked.

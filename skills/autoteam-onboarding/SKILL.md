---
name: autoteam-onboarding
description: Map an unfamiliar repository, reuse verified project knowledge, bind the cycle's canon snapshot and choose a safe first step. Use for a fresh clone, repository orientation, review or analysis setup.
---

# Onboard once, reuse verified knowledge

**Input.** Assignment, repository and allowed output location. **Output.** A compact evidence-backed map, relevant unknowns and first safe step; the cycle's method identity. **Forbidden.** Reading/copying secret values; changing the stack by observation; guessed facts; overwriting another owner's files or global user skills. **Evidence.** Primary files and observations with revision, scope and actual check. **Stop.** Only dependent work when authority, resource ownership, required evidence or method identity is unresolved. **Next.** Assignment → `autoteam-orchestrator` or the relevant catalog role.

Read the cycle snapshot's `docs/process/project-knowledge.md` and `resource-lifecycle.md`; use `work-items.md`, `assurance.md`, `monitoring.md` and `model-routing.md` as applicable. This skill alone is focused onboarding guidance, not a full method deployment.

## Establish the mode and method

Review, audit and analysis default to read-only treatment of the analyzed repository. Put reports and drafts only in the authorized output directory. Do not initialize Git, copy process docs into that repository, edit its state/locks, install skills or commit there. Acquire any run/output lock outside it. For implementation, use an owned isolated worktree/draft tree and one physical writer; follow existing project conventions. A per-file division in one tree is insufficient isolation.

Follow the root README's bundle and checker rules: select and validate a complete canon bundle, create and verify an immutable cycle-owned snapshot, record path, `canon.json` version, content fingerprint, locale and source revision when available. Read skills and method links only from it, or an exact verified copy bound to it. A missing required tree fails full deployment. A lone skill can be used only with its limited scope declared. Do not unconditionally pull a shared source, overwrite dirty canon files or replace global skills. Refreshes by other products never change this cycle's instructions. Reuse an existing verified snapshot for recovery of that cycle; a new cycle selects its own verified snapshot.

## One pass through existing knowledge

1. Read README, authorized instructions/config, project profile or equivalent, relevant verified memory and decisions in force. Inspect current work and ownership before launching writers. Previous-cycle state is history; do not treat it as a live task list. Empty repository or canon-only folder is a finding; with no assignment, use catalog cold start.
2. Reuse existing answers, artifact formats and naming by reading neighboring artifacts. Do not ask the same onboarding questionnaire each cycle. If an essential unknown prevents dependent work, ask one meaningful question; continue independent work. Mark other unknowns or assumptions explicitly.
3. Map the actual stack from manifests, lockfiles and ADRs; “stack not set” is valid. Distinguish authorized settings in the profile from observed implementation, desired behavior in the spec, choices in the journal, durable facts in memory and current work in state. Investigate conflicts; do not rewrite the spec to match the code.
4. Locate contracts, domain/algorithm specs and code-to-document references. Consult source-registry coverage and reuse suitable extraction. Open relevant unexamined material; new questions, poor extraction or contradictions allow targeted rereads even without a source change. Record inaccessible scope and dependent conclusions; tool failure does not prove product absence.
5. Map check commands with working directory and source revision; distinguish documented commands from checks actually executed. Map release authorization/runbook, review cadence and documentation entry points. Know secret/vault paths only; do not bulk read environment files, secret stores, logs or archives.
6. Map resources, budgets, connector permissions and retention from safe metadata. Before using a run resource record exact identity, owner, permission and cleanup plan. Reconcile outstanding prior-run resources and locks; old lock age requires a liveness check, not deletion. Unknown owners block conflicting work. Monitors obey the same lifecycle.
7. Return only the useful map: evidence references, scope limits, existing knowledge locations, snapshot identity, ownership, blockers and next step. Propose small profile/memory/source updates with the related change for acceptance; do not turn guesses or another summary into facts. Changed or contradicted sources mark dependent memory pending recheck.

In implementation mode, if the project lacks a reusable map, propose or write it in the authorized owned tree using the profile template and existing conventions. In read-only mode, keep that proposal in the output directory. Avoid copying the whole method or creating empty registries. Reconcile and clean up owned resources on success and failure; expose `cleanup_pending` with owner and next action.

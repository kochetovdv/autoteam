# Project knowledge and the cycle's method

Keep six different questions separate. Existing project files may serve these roles; the paths below are defaults, not a requirement to create six new registries.

| Layer | Question and authority | Default location |
|---|---|---|
| Method canon | How do we work? Versioned skills, process rules and templates; no product facts. | Verified cycle snapshot of `canon.json`, `skills/`, `docs/`, `templates/` |
| Project profile | What authorized settings apply here? Stack, commands, domain glossary, paths, conventions, budgets, connectors and resource pointers. Normative within the assignment and authority recorded for each setting. | `docs/process/project-profile.md` |
| Project memory | What durable facts and lessons have been verified? Evidence, revision and recheck triggers accompany every entry. | `docs/process/memory.md` |
| Specification | What behavior is required? Approved requirements, contracts and acceptance criteria. | The project's existing spec/contract locations |
| Decision journal | What was chosen, by whose authority, and what amended it? History with dependencies. | `docs/process/decisions.md` |
| Cycle state | What is happening now? Work item statuses, owners, blockers, next steps and references. | `docs/process/state.md` |

A source says what was observed or stated at a revision; a specification says what should happen; a decision records a choice. A passing observation does not approve behavior, and a decision does not make a factual claim true. When they conflict, record the conflicting references, impact, owner and investigation work item. Preserve the existing requirement until an authorized amendment changes it; never rewrite the spec automatically to fit the implementation. Stop only conclusions and actions that require the disputed input. Work item and acceptance rules: [work-items.md](work-items.md), [assurance.md](assurance.md).

## Start from what the project already knows

Onboarding reads the profile, relevant memory, source coverage, decisions in force and current work before asking the human. Reuse verified conventions and answers; do not repeat a questionnaire each cycle. A missing value stays unknown or becomes an explicit assumption with a resolution trigger. An agent's guess or another agent's summary is neither evidence nor authorization. Follow its cited source before promoting a claim. A user-approved setting needs a traceable authority reference; an observed command in a README needs a source revision and remains unverified as an executable check until actually run.

The profile separates authorized configuration from observed implementation. A profile amendment cites the assignment, accepted decision or human instruction that authorizes it. Memory does not override profile settings, policy or the spec. State holds the active task; durable knowledge belongs in memory only if it will help a future task after this cycle closes.

## Durable memory is reviewed evidence

An author proposes a small memory delta with the accepted change: fact or lesson, source location and revision/fingerprint, observation/as-of time, recording time, verification, scope, dependents and recheck trigger. Keep these times distinct: writing a note today does not make an older observation current. The acceptor checks it with the change; only accepted entries become verified memory. No author silently promotes their own conclusions. A lesson distinguishes the observed event from its inference and conditions of applicability. An unresolved inference stays a hypothesis outside verified facts.

`verified` means supported within the recorded scope and as-of time, not guaranteed to describe the present. Before relying on an entry for a current decision, compare its facts, observation and verification dates, conditions and source with the relevant current state. Record that applicability check with the dependent work item or decision, rather than creating another knowledge-status registry. Reuse still-applicable evidence; investigate a material difference or missing freshness evidence before treating the entry as a settled current premise. Recheck only the relevant premises, not all memory every cycle.

For a volatile or consequential premise, the agent supplies a recheck owner, event triggers and a latest review date appropriate to the rate of change and consequence; reuse existing project settings without a questionnaire. A stable fact may use event-based recheck with a recorded reason. A due date is a trigger to check applicability, not proof the historical fact became false. If current evidence is inaccessible, record the unknown and the affected decision; do not silently refresh the verification date.

When a source, contract, environment or relevant assumption changes, mark dependent entries `pending-recheck`; do the same when extraction is contradicted or no longer suitable. Investigate and accept a revised entry before using it as a settled premise. Keep supersession references so a later agent can explain why a fact changed. Do not bulk erase memory or treat age alone as falsification.

Memory contains no raw logs, secrets, transcripts, chat summaries, or duplicate active task lists. Preserve only the necessary sanitized evidence reference and consequence. Temporary failures belong in cycle state; a reproducible durable limitation may enter memory with its verification scope and recheck trigger. A tool failure establishes an access limitation, not the absence of a product feature.

## Sources are reusable, with question coverage

Use the existing source index or [sources template](../../templates/sources.md) for material that is expensive to reprocess or supports durable conclusions. Record identity, revision or content hash, scope, access limitations, processing tool/version and extraction settings, questions covered, derived artifacts and dependent entries/work items. Do not hash or extract raw secret stores. Link an existing revision instead of copying source content into several registries.

Reuse an extraction while its source revision, processing quality, time relevance and coverage suit the present question. An unchanged hash proves the same stored content, not that an external capability, price, rule or environment is still the same; compare the source's as-of time with current evidence when the decision needs current facts. An unchanged source does **not** forbid a targeted reread: a new question, poor OCR/parsing, omitted diagrams/tables or a contradiction can require reprocessing the relevant pages, ranges or sections. Record the reason and update coverage and dependents. If the source changed, assess the affected scope, mark dependents pending recheck and avoid a full reread when a reliable focused comparison suffices. An explicit code-to-spec reference is a required dependency: open the relevant material or record incomplete coverage and the blocked conclusions.

## Bind the method once per cycle

The root README defines full bundle deployment and `scripts/check_canon.py`. Validate the bundle before creating a cycle snapshot; an incomplete or inconsistent skills/docs/templates tree is a failed deployment, not a usable full method. Copy into a new cycle-owned location without replacing dirty files; verify the completed snapshot against the selected source bundle. Record its path, `canon.json` version, content fingerprint, locale and source revision when available. A tag or commit alone does not identify uncommitted content. Expose skills from this immutable snapshot or an exact verified copy explicitly bound to it. Follow method links inside that same snapshot throughout the cycle.

Do not run an unconditional `git pull` in a shared checkout, overwrite dirty canon sources or replace global user skills. Refreshes are explicit source-maintenance work in an owned checkout. Another product may refresh a shared source: it never switches an active cycle's instructions. A source becoming available or newer is not a reason to mutate an active snapshot. Recover from a verified matching snapshot; if its identity cannot be established, block method-dependent work until restored. A focused individual skill may be used alone with its scope declared; it cannot claim the full process when required process documents are missing.

Operational resources and physical write ownership: [resource-lifecycle.md](resource-lifecycle.md). Recurring actions: [monitoring.md](monitoring.md). Model selection: [model-routing.md](model-routing.md).

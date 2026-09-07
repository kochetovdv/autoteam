# Documentation: why, what kind, when to update

This is not "write a README". Documentation is part of the delivery. Skill: `autoteam-docs`.

## Three layers

| Layer | Who reads it | Usual location | Forbidden |
|------|------------|------------|-----------|
| **Business / product** | operator, PM, client | `docs/kb/`, the "Documentation" section in the UI | internal repo paths, task codes as menu items |
| **Technical** | developer, agent | `docs/`, ADR, runbook, OpenAPI | passing an ADR off as a user guide |
| **Process** | team and agents | `docs/process/` | confusing it with the product spec |

## When to update (cadence)

Mandatory in the same PR/task if any of these changed:

- observable behavior of a screen or API;
- a role, permission, flag;
- an admin panel command;
- the release or rollback procedure;
- the meaning of a requirement (then the spec too).

Regular pass (even without a feature):

- active product — once a sprint / every 2 weeks: stale buttons, drift between UI and kb;
- quiet one — once a month, together with the architecture review.

**Stale:** a button that doesn't exist; a promise the code doesn't keep; a link to a deleted screen; "that's how it was in v1". Flag and fix in the same wave; don't pile up a "for later" document without an owner.

The owner of each documentation layer — in the project README. No owner — the orchestrator queues the update without blocking others' code.

## Order in files

Files that grow by entries: newest on top. The test is not importance but truncation — a long file is read partially (a read limit, a grep, a context window), and the tail is what gets cut: with the newest at the bottom a partial read loses the current truth, with the newest on top it loses history, which has other homes (git, checkpoints, retro). Discriminator: can entry #7 be read without entry #6? Then it is a log — newest on top. If order carries meaning (steps, sections, dependency: a brief, a scope, a spec, the body of an ADR, a checklist, a runbook), the file stays as written. Registries keyed by an ID keep ID order — lookup there beats recency, and time already lives in the "expiry" and "re-check" fields. A log states its order in one line under its heading: otherwise the next writer appends at the bottom and the file ends up mixed, which is worse than either convention.

Rewritten in place or never rewritten — two different classes, do not mix them. A registry of the present (gaps, resources, state) is edited in place: a row that stopped being true is replaced, and git holds its history. A log is never rewritten: a superseded entry gets an amendment. Do not carry amendment bookkeeping into a registry — "superseded by" rows there breed noise instead of showing what is true now.

## What not to do

- Don't describe package classes to the user.
- Don't invent UI commands.
- Don't keep the only source of truth solely in chat.

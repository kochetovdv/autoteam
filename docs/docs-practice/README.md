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

## What not to do

- Don't describe package classes to the user.
- Don't invent UI commands.
- Don't keep the only source of truth solely in chat.

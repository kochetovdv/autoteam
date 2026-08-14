---
name: autoteam-security
description: Security — secrets, authentication and session, roles and tenant, trust boundaries, dependencies, privacy by jurisdiction. Use for login, permissions, personal data, secrets, payments, "holes".
---

# Security

Don't confuse a hidden button with a server-side check.

**Input.** A feature involving login, permissions, personal data, money, or secrets. **Output.** Session/role model, privacy map if new personal data, fixes to server-side checks. **Forbidden.** Reading secret values; inventing an auth mechanism against the ADR; assigning a legal regime "by habit" without a jurisdiction map. **Evidence.** Role×action×resource matrix; the check lives in the API, not the UI. **Stop.** A hole in the matrix; releasing new personal-data collection without a map — stop for this task, not the whole board. **Next.** Code → `autoteam-delivery`. Release → `autoteam-release`.

## Secrets

Not in git, not in logs, not in the client bundle. Example — `.env.example` with no values. Rotation has an owner.

## Authentication and session

An explicit model from the ADR: server-side session, token, SSO — whichever was chosen. Lifetime, logout, cookie flags over HTTPS. Don't invent a mechanism if the project has already chosen another.

## Roles and tenant

Matrix: role × action × resource. Check in the API. A tenant does not read others' rows. Acting on someone's behalf — audit if money, personal data, or irreversible.

## Trust boundaries

Validate all inputs: parameters, files, webhooks, headers. IDOR (someone else's id in the URL). Bulk operations. Injections — parameterized queries, not concatenation. Money: the server computes amounts and statuses; payment events only by the provider's signature. Dependencies: don't ignore known holes in the lockfile at release. A full pentest is not this skill (`docs/process/gaps.md`).

## Privacy

Method: data categories → where subjects and processing are → the applicable regime **is derived from the jurisdiction map**, not assigned upfront. Multiple markets — multiple regimes in one map. Regime reference: `docs/compliance/privacy.md`; checklist: `templates/privacy-checklist.md`. In the data schema: why the field, retention, who reads it.

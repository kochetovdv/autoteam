---
name: autoteam-architecture-review
description: Regular and trigger-based architecture review without stopping the independent flow. Use on cadence, after a burst of features, before a new store, on an incident.
---

# Architecture review

Not a PR code review. Don't fix code in this run. Not the same prompt that designed the system.

**Input.** Product repository, previous report if any. **Output.** Review file and verdict. **Forbidden.** Fixing code here; stopping the whole board over a REMEDIATE. **Evidence.** Code/ADR audit, comparison with the previous report. **Stop.** Only a Blocker within the boundary of affected tasks. **Next.** Fixes → `autoteam-delivery` / `autoteam-quality` / `autoteam-security` as separate tasks.

Cadence: active — a week or ~8 tasks; quiet — a month; data incident/race conditions — immediately.

Trigger: new context, service, store, broker, permission change, load growth.

Independent tasks continue. Stop — only a Blocker within their boundary.

Order: code and ADR audit → map of dependencies and data → measurements (boundaries, record owner, race conditions, roles on the server, failures/logs, KISS, dead and unreachable branches — traps for future changes, debt with a date) → comparison with the previous report → file.

Artifact: `docs/architecture/reviews/YYYY-MM-DD.md` in the **product**. Method canon template: `templates/architecture-review.md`.

Verdict: `HEALTHY` | `WATCH` | `REMEDIATE`. REMEDIATE does not stop the whole flow.

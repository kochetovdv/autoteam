# Incidents

1. Record the symptom and time (what the user sees, which request).
2. Evidence: API status, log with id, and for data — a query against the store. Not a UX excuse.
3. Mitigation (release rollback, flag, scaling) — with approval if destructive.
4. Cause. Reproduce with the same check.
5. Entry: what happened, how we saw it, how not to repeat it. Update the runbook.

Do not combine with "let's rewrite the module while we're at it". Do not stop independent tasks if the incident is in another boundary.

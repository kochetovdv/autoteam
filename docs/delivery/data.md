# Data

## Choosing a store

Do not pick Postgres, ClickHouse, cache, or search "by category". Look at: write consistency; insert pattern; which queries (point / scan / analytics); retention period; concurrency; cost of operation.

No numbers — an assumption plus a revisit trigger ("if >X events/day — redo"). Two stores — two owners of truth and an explicit desync rule.

## Migrations

Migrations: forward-only plus a documented rollback, or expand/contract; never edit a migration already applied in production. On release: compatibility with old code, backup **before** a destructive migration, who pushes the button.

## Backup

A delivery concern, not "ops later". Minimum: what we back up (a DB with personal data — yes), how often, how we verify restore, where the access secret lives. No restore verification — no backup.

## Derived data

Aggregates, scores, and caches are computed by rules (thresholds, formulas, boundaries) — a derived record carries the version of the rules that produced it. Version diverging from current = the record is stale: revision is a process (a recompute queue, a "stale" flag on read), not silence. A version field that is written but never read is not a mechanism — it is an imitation of one.

## Personal data

Categories and regime — `docs/compliance/privacy.md`. In the schema: why the field exists, retention, who reads it. Do not hoard "just in case".

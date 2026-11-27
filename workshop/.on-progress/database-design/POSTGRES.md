# PostgreSQL

How the rules in [SKILL.md](SKILL.md) land on PostgreSQL. Version-specific facts name their version; verify against the version in use.

## Types and ids

- Instants: `timestamptz` (stored as UTC). Money: `numeric` or integer minor units. Periods: `tstzrange` / `daterange`.
- Closed value sets: a check constraint or a lookup table evolves more easily than an `enum` type, whose values can't be removed.
- Integer ids: `bigint generated always as identity`.
- UUIDv7: native `uuidv7()` from PostgreSQL 18; earlier versions generate it in the application or an extension. `gen_random_uuid()` is v4 and scatters index writes.

## Constraints

- Conditional uniqueness is a partial unique index (`… WHERE status = 'active'`).
- No-overlap rules are exclusion constraints on GiST, with `btree_gist` for the equality columns (`room_id WITH =, during WITH &&`).
- Foreign keys are **not** indexed automatically.

## Indexes

- B-tree by default; `INCLUDE` columns make it covering.
- GIN: `jsonb` containment, arrays, `tsvector` full-text. `pg_trgm` (GIN or GiST): `LIKE`/`ILIKE` substring and fuzzy match.
- GiST: ranges, geometry, exclusion constraints. BRIN: huge append-only, time-ordered tables.

## Isolation and locking

- Default level is `READ COMMITTED`.
- `REPEATABLE READ` is snapshot isolation; a concurrent update of the same row fails with a serialization error (`40001`) instead of silently losing the update.
- `SERIALIZABLE` is SSI: retry the whole transaction on `40001`; retry deadlocks (`40P01`) too.
- Pessimistic locks: `SELECT … FOR UPDATE`. Job claiming: `FOR UPDATE SKIP LOCKED`.
- Advisory locks: the transaction-scoped `pg_advisory_xact_lock` survives transaction pooling; the session-scoped variant doesn't.

## Row-level security

- `ENABLE` and `FORCE ROW LEVEL SECURITY` on each tenant table, so owners are bound too.
- The application role is neither owner nor `BYPASSRLS`.
- Tenant context per transaction: `SET LOCAL app.tenant_id = …` or `set_config('app.tenant_id', $1, true)`; policies read `current_setting('app.tenant_id')`.

## Pooling (transaction mode)

- Session `SET` leaks across clients; use `SET LOCAL`.
- `LISTEN` needs a direct, session-mode connection.
- Named prepared statements depend on the pooler's support; with PgBouncer, that means 1.21+ with `max_prepared_statements` set.

## Migrations

- `SET lock_timeout` before DDL; retry on timeout.
- `CREATE INDEX CONCURRENTLY` runs outside a transaction block; a failed run leaves an `INVALID` index to drop and rebuild.
- `ADD CONSTRAINT … NOT VALID`, then `VALIDATE CONSTRAINT` under a lighter lock.
- `ADD COLUMN` with a constant default is metadata-only (PostgreSQL 11+); most column type changes rewrite the table.
- Partitioning is declarative; the partition key must be part of primary and unique keys; retention is `DETACH` / `DROP` of old partitions.
- `REFRESH MATERIALIZED VIEW CONCURRENTLY` needs a unique index on the view.
- Generated columns: `STORED`; PostgreSQL 18 adds virtual generated columns.

## Operations

- Per application role: `statement_timeout`, `idle_in_transaction_session_timeout`, `lock_timeout` (`ALTER ROLE … SET`).
- `pg_stat_statements` for top statements by total and mean time.
- Autovacuum health: dead tuples, table and index bloat, transaction-id age (wraparound). Long transactions and abandoned replication slots hold vacuum back.
- Point-in-time recovery: base backups plus continuous WAL archiving.

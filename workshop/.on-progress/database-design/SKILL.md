---
name: database-design
description: Relational data design rules and defaults: modeling, invariants, indexes, concurrency, tenancy, scaling, migrations. Use when designing, grilling or reviewing a schema or data model, or when writing or reviewing queries, migrations or data-access code.
---

# Database design

A pool of rules for relational data. It owns no process: consult the sections the current decision or code touches, and let the calling workflow (grilling, wayfinder, implementation, review) own the steps and the deliverable.

Project ADRs and the glossary win over these defaults. A deliberate deviation is a decision worth recording as an ADR.

Vendors, products and libraries already in the project are the given. Adding or replacing one is the user's decision: present the candidates as options, each with its trade-off, and recommend by requirement.

Beside this file:

- **Grilling or design review:** read [CHOICES.md](CHOICES.md) before the first question. Its defaults are the recommended answers for subtypes, polymorphic references, hierarchies, id type, history, deletion, derived data, isolation, locking, tenancy model and search; a recommendation drawn from it names its entry (`CHOICES: Id type`).
- **At session start, once the stack is known:** read [POSTGRES.md](POSTGRES.md) if the engine is PostgreSQL, [D1.md](D1.md) if the engine is Cloudflare D1.

Service-level concerns (API contract, idempotency keys, retries, caching) live in the `backend-design` skill.

## Stance

- **The database outlives the application.** Services, scripts, analysts and future rewrites all touch the data: model the domain truthfully and enforce invariants in the database.
- **Known access patterns shape the physical design; normalization keeps the unknown ones possible.** Denormalize for a measured hot path and pay its write complexity knowingly.
- **Name the trade-off.** Every significant decision states the alternative rejected and why.

## A model is ready when

Each question has a recorded answer, an explicit assumption, or "not applicable", in the spec or an ADR:

- What identifies each core entity in the business, not only technically?
- What is each entity's lifecycle: states, allowed transitions, and who triggers them?
- Which invariants must always hold, and which mechanism enforces each (see Integrity)?
- What must be remembered historically (price at order time, who changed what)?
- What must be forgotten (retention, erasure), and where does every copy live?
- Who is the single writer of each table?
- What is the access-pattern matrix (see Access patterns), and which pattern does each index and each denormalization serve?
- What is each foreign key's delete behaviour, and how does it fit the erasure path (see Integrity)?
- What is each table's expected size and growth?
- What are the RPO and RTO, and how is restore tested (see Lifecycle, protection and recovery)?

## Access patterns

- An **access-pattern matrix** comes before physical structures:

  | Pattern | Type | Frequency | Latency target | Filter / sort keys | Rows touched |
  |---|---|---|---|---|---|
  | A tenant's open invoices by due date | read | 200/s peak | p95 < 50 ms | tenant, status, due date | ≤ 50 per page |
  | Monthly revenue report | analytical | daily | minutes | tenant, month | millions |

- Estimate per table: rows per day × row width × retention, plus 1–3× for indexes; hot working set against memory; write rate on the busiest tables; read/write ratio.
- Separate transactional (OLTP) from analytical (OLAP) patterns early: analytical ones go to a replica, warehouse or columnar store.
- **No N+1:** a list fetches each relation's related rows with one batched query (`WHERE parent_id IN (…)`), so queries per request stay constant as the page grows.
- **No row explosion:** joining several one-to-many relations in one query multiplies rows (20 parents × 5 photos × 10 requests = 1,000 rows). Each one-to-many relation gets its own batched query, or is aggregated per parent in the database (e.g. JSON aggregation).
- List queries select only the columns the screen needs; wide text and blob columns stay out of lists.
- Child collections shown in lists are bounded: the first N rows, plus a count only when the UI shows it.

## Logical modeling

- Third normal form by default: each fact stored once; every non-key attribute depends on the key, the whole key, and nothing but the key.
- **Aggregates:** entities that change together (order + lines) form one transaction and consistency boundary. References across aggregates are ids and may be eventually consistent.
- Cardinality and optionality are decisions. 1:1 splits off optional, large or sensitive attributes; 1:N puts the reference on the child; M:N gets an association entity, which usually grows its own attributes and lifecycle (membership with role and joined date).
- State is explicit: one status attribute with a closed value set and defined transitions, plus check rules tying dependent attributes to it (status `paid` ⇔ `paid_at` present).
- Core data lives in typed columns. Genuinely variable, rarely queried attributes (settings, external payloads) go in a semi-structured document column; a document field that is regularly filtered, joined or constrained is promoted to a real column.

## Identity

- Surrogate keys identify rows; natural keys (email per tenant, SKU, invoice number per tenant) are unique constraints. Natural keys change; surrogates don't.
- Public identifiers may differ from internal keys (slugs, prefixed ids like `inv_…`); decide whether an id may leak volume or creation time.
- An unguessable id still passes an access check.
- Id type: CHOICES.md.

## Integrity

The closer to the data, the stronger the guarantee. Each invariant goes to the innermost layer that can express it:

1. **Type:** domain of values (exact decimals for money, zoned timestamps).
2. **Not-null:** presence.
3. **Check:** single-row rules (amount ≥ 0; end after start; status in set; exactly one of two references set).
4. **Unique / partial unique:** scoped or conditional uniqueness (invoice number per tenant; one active subscription per account).
5. **Foreign key:** existence of references, delete behaviour chosen per relationship: restrict by default, cascade only for true composition, set null for optional links.
6. **Exclusion:** no overlaps (room bookings with overlapping time ranges).
7. **Trigger or transaction logic:** multi-row and cross-table rules; or derive the value instead of checking it (header total from its lines).

Rules involving concurrency (uniqueness, no overlaps, limits) are enforced by a constraint, or, where no constraint can express them, by a serializable transaction or an explicit lock. A read-then-write check in application code races; application validation exists for friendly messages.

## Time and money

- Instants are timestamps with time zone, UTC semantics. Calendar concepts (birthdays, due dates) are dates. Where wall-clock meaning matters (recurring meetings), the IANA zone name is stored beside.
- Periods are half-open `[start, end)`; range types plus exclusion constraints model validity periods and bookings.
- Values needed as of a business event are copied onto it (an order line keeps the unit price at purchase).
- Money is an exact decimal or integer minor units plus an explicit currency, with rounding rules defined and placed. Floating point stays out.
- History pattern: CHOICES.md.

## Derived data

- Every derived structure (count, total, search index, read model, materialized view) names its source of truth, its freshness, and its rebuild procedure.
- Maintenance options: CHOICES.md.
- High-contention counters (likes, inventory) are hot rows: shard the counter, batch, or aggregate asynchronously.
- **Outbox** and **inbox** are tables in the same database as the business data. Outbox rows are written in the business transaction and published by polling or change data capture. Inbox rows (processed message ids) are inserted with the consumer's side effect; a unique violation means "already processed".

## Indexing

- Each index traces to an access-pattern row. Every index is a write tax (storage, write amplification, maintenance): write-heavy tables get few, precise indexes, and unused or redundant ones are dropped.
- Primary and unique constraints bring their own index; whether a foreign key does depends on the engine. Referencing columns used in joins, or scanned by parent deletes and updates, are indexed.
- Composite order: equality columns first, then the range or sort column, so one index serves "tenant + status, newest first, first 50".
- **Partial** indexes serve hot subsets (open orders, unprocessed jobs); **expression** indexes serve normalized lookups (lowercased email); **covering** indexes answer hot reads from the index alone.
- Specialized families: inverted (document containment, arrays, full-text), trigram (substring, fuzzy), spatial/range (geometry, ranges, exclusion), block-range (huge append-only, time-ordered tables).
- Tenant-scoped indexes lead with the tenant key.
- Pagination is **keyset**: an index on (sort key, unique id) and a seek past the last seen pair, constant cost per page. Offset only for small, shallow lists.
- Plans are verified on production-like volumes; small development datasets hide every problem.

## Concurrency

- Know the engine's default isolation level and the anomalies it allows; choosing a level: CHOICES.md.
- Atomic single statements ("decrement stock where stock ≥ quantity") close the read-modify-write gap wherever they can.
- Transactions are short: user interaction and network calls happen outside them. Long transactions hold locks and block maintenance.
- Rows are locked in a consistent order, against deadlocks.
- Retry on serialization failure and deadlock is designed in: the whole transaction re-runs, bounded, with backoff.
- Job tables are consumed with skip-locked row claiming, so workers never wait on each other.

## Multi-tenancy

- Tenancy model: CHOICES.md.
- With shared tables, the tenant key sits on every tenant-owned table and inside its unique constraints and foreign keys; composite references that include the tenant make cross-tenant links impossible by construction.
- Row-level security is defense in depth under application filtering: the application role cannot bypass policies, policies apply to table owners too, tenant context is set per transaction, predicates stay simple and indexable.
- Per-tenant export, deletion, and moving a large tenant to dedicated infrastructure have a planned path.

## Connections

- Connections are a scarce, fixed budget: the database serves hundreds well, not thousands. Many application instances or serverless functions reach it through a pooler.
- Under transaction pooling, context is per transaction: session variables, session-level locks, LISTEN/NOTIFY and session-scoped prepared statements don't carry across transactions. Set context inside each transaction.

## Scaling path

Climb in order; each rung is cheaper and less invasive than the next, and each climb names the measurement that triggered it.

1. Fix queries and indexes, starting with the top statements by total time.
2. Vertical scaling: memory for the hot set, faster storage, CPU.
3. Connection pooling.
4. Cache hot, rarely changing reads, with an invalidation story.
5. Read replicas for read-heavy and reporting load. Lag is accepted per read path; read-your-writes paths stay on the primary.
6. Partitioning by time (retention by dropping partitions) or by tenant/hash, on a key present in nearly every query. A data-management tool more than a speedup.
7. Archival and tiering of cold data.
8. Analytics offloaded via change data capture to a replica, columnar store or warehouse.
9. Sharding, usually by tenant. Cross-shard queries, transactions and rebalancing become yours.

## Lifecycle, protection and recovery

- Data is classified at design time (public / internal / confidential / regulated); PII columns are marked; collection is minimized.
- Each table has a retention rule: how long, then delete, anonymize or archive.
- Right to erasure covers every copy: derived data, logs, backups. Crypto-shredding (per-subject keys destroyed on erasure) serves immutable stores.
- The delete behaviour of every reference to a user or person (Integrity) is chosen together with the erasure path; for example set null for anonymized history.
- Soft delete: CHOICES.md.
- Roles: owner/migration, application (data manipulation only), read-only/analytics. Applications connect as neither superuser nor table owner.
- Highly sensitive fields get application-level encryption on top of transit and at-rest encryption.
- Backups: continuous archiving with point-in-time recovery, RPO/RTO defined, restores tested on a schedule. An untested backup is a hope.
- Access to sensitive data and administrative changes is audited.

## Operations

- Watch top statements by total and mean time, slow queries, lock waits, deadlocks, connection saturation, replication lag, and storage growth against forecast.
- Application roles run with statement and idle-in-transaction timeouts.
- Capacity is reviewed against the estimates on a schedule; alerts fire on trend breaks.

## Schema evolution

Old and new application versions run against the live database during every deploy.

- **Expand → migrate → contract:** add structures compatible with old code; backfill and dual-write; switch reads; remove the old structures in a later release. Renames and type changes are always multi-step.
- Every migration states its lock impact, runs with a lock timeout and retries, builds indexes without blocking writes, adds constraints unvalidated and validates them separately, and leaves full-table rewrites of large tables out.
- Backfills run in small, throttled, restartable, idempotent batches, and are monitored.
- Migrations are versioned, reviewed, forward-only in production, tested on production-like volumes (copies or database branches), and each carries a roll-forward plan.
- The schema is a data contract: analytics and change-data-capture consumers depend on it, so breaking changes get the same compatibility window as API breaks.

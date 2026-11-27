# Data design choices

Open modeling and physical choices, each with its options, a **default**, and the signal to deviate. A default is a recommended answer, not a verdict: the project's requirements and ADRs decide.

## Subtypes (payment is card, bank transfer, or wallet)

| Option | Pros | Cons |
|---|---|---|
| Single table + type discriminator + nullable subtype columns | Simple queries, one table | Many nulls; subtype rules need conditional checks |
| Base table + one table per subtype, shared key | Clean typing and constraints per subtype | Joins; "exactly one subtype row" needs enforcing |
| One table per concrete type | No nulls, independent evolution | Cross-type queries need unions; no single reference target |

**Default:** single table with per-type check constraints while subtypes share most attributes. **Deviate** to base + subtype tables once subtype-specific columns and rules dominate.

## Polymorphic references (a comment belongs to a post or a photo)

| Option | Trade-off |
|---|---|
| Separate optional foreign keys + an exactly-one-set check | Full referential integrity; one column per target |
| Shared supertype entity all targets reference | Integrity with one reference; an extra entity |
| Type + id pair | No referential integrity |

**Default:** separate optional foreign keys with the exactly-one check. **Deviate** to a supertype once targets are many or keep growing.

## Hierarchies

| Option | Fits |
|---|---|
| Adjacency list (parent reference) | Most trees; recursive queries for subtrees |
| Materialized path | Frequent subtree/ancestor queries on moderately stable trees |
| Closure table | Heavy ancestor/descendant querying |

**Default:** adjacency list.

## Tags and many-to-many classifications

**Default:** association table (integrity, indexing, own lifecycle). **Deviate** to an array or document column only when tags are owned by the row and never need their own lifecycle.

## Id type

| Option | Trade-off |
|---|---|
| Sequential integer | Compact, fast; enumerable, known only after insert |
| Time-ordered UUID (UUIDv7) | Globally unique, client-generatable (offline creation, idempotent inserts), index-friendly; larger, embeds creation time |
| Random UUID (v4) | Unique; scatters writes across indexes on large write-heavy tables |

**Default:** UUIDv7 for externally exposed entities, integers for internal high-volume tables.

## History

| Need | Pattern |
|---|---|
| Who changed what, when (compliance) | Append-only audit table written in the same transaction |
| Value as of a past date (prices, addresses) | Versioned rows with validity ranges (SCD type 2, temporal tables) |
| Values at the moment of a business event | Copy them onto the event row |
| Full reconstruction and replay | Event sourcing: events as source of truth, projections for reads |

**Default:** the cheapest pattern that meets the stated need. Event sourcing needs a concrete replay requirement to justify its cost.

## Deletion

| Option | Trade-off |
|---|---|
| Hard delete + audit/history | Simple queries and constraints; erasure is real |
| Explicit archived state | A business meaning ("archived project"), visible in the status model |
| Soft delete flag | Undo/restore; every query, unique rule and reference must account for deleted rows, and erasure still needs real deletion |

**Default:** hard delete plus audit/history. **Deviate** to an archived state when archiving means something to users; to soft delete only for a real undo requirement.

## Derived data maintenance

| Option | Freshness | Write cost | Risk |
|---|---|---|---|
| Compute at read time | Always fresh | None | Slow when large |
| Same transaction (trigger or application) | Fresh | Higher; hot-row contention | Drift if some writer bypasses the application path |
| Async projection (outbox/event → read model) | Seconds behind | Low on the write path | Needs rebuild procedure and lag monitoring |
| Periodically refreshed materialized view | Minutes to hours behind | Batch cost | Staleness must be acceptable |
| Generated column | Fresh | Per-row computation | Same-row derivations only |

**Default:** compute at read time until a hot path is measured; then the freshest option the write path can afford.

## Isolation level

| Level | Prevents | Still possible | Fits |
|---|---|---|---|
| Read committed | Dirty reads | Non-repeatable reads, lost updates in read-modify-write, write skew | Most simple operations |
| Repeatable read / snapshot | Non-repeatable reads (lost-update behaviour varies by engine) | Write skew across rows | Consistent reports, single-row read-modify-write |
| Serializable | All anomalies; behaves as if serial | Serialization failures to retry | Invariants spanning rows ("at least one doctor on call") |

**Default:** read committed, with constraints and atomic statements carrying the invariants. **Deviate** to serializable for multi-row invariants no constraint can express. Engine defaults and exact semantics differ; check the engine file.

## Concurrent writers

| Strategy | Fits |
|---|---|
| Atomic single-statement update | Any change expressible as one conditional statement |
| Optimistic (version checked on update) | User edits with think time; conflicts surfaced to the user |
| Pessimistic (lock rows before changing) | Short, highly contended critical sections |

**Default:** atomic statement first, optimistic for user-facing edits, pessimistic only for short contended sections.

## Tenancy model

| Model | Isolation | Operational cost | Fits |
|---|---|---|---|
| Shared tables + tenant key | Logical (app filter + RLS) | Lowest | Many small and medium tenants |
| Schema per tenant | Stronger logical | Migrations and connections × N | Tens to hundreds of tenants, per-tenant customization |
| Database per tenant | Physical | Highest; fleet management | Few large or regulated tenants, residency |
| Hybrid: pooled + dedicated tier | Mixed | Two paths to maintain | Enterprise tier needs isolation; long tail pooled |

**Default:** shared tables with a tenant key, enforced by composite references and row-level security. Schema-per-tenant runs every migration as a tracked fleet job.

## Search

**Default:** the database's built-in full-text search. **Deviate** to a dedicated search engine for relevance tuning, typo tolerance at scale, faceting across huge datasets, or multi-language analysis; it is then derived data, with a source of truth and a rebuild path.

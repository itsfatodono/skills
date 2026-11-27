# Design choices

Open backend design choices, each with its options, a **default**, and the signal to deviate. A default is a recommended answer, not a verdict: the project's requirements and ADRs decide.

## Estimates that drive choices

Orders of magnitude are enough; they decide caching, replicas, pooling and cost.

- **Request rate:** DAU × actions per user per day ÷ 86,400 = average req/s; × peak factor (typically 3–10×).
- **Read/write ratio** drives caching, replicas and indexes.
- **Payload size and egress:** egress is often a hidden cost.
- **Concurrency:** req/s × average latency ≈ in-flight requests, which instances and downstream connections scale with.
- **Non-functional targets to pin:** availability, latency percentiles, peak throughput and burst, durability (RPO/RTO), consistency per read path, data residency/compliance, cost budget. Write explicit non-goals.

Latency intuition (verify per platform): in-memory ≈ ns; same-region round trip ≈ sub-ms to a few ms; indexed DB lookup ≈ 1–10 ms; cross-continent ≈ 100–200 ms; cold start ≈ tens of ms (edge isolates) to seconds (heavy containers).

## Architecture style

| Option | Costs |
|---|---|
| Modular monolith: one deployable, strict module boundaries along domain lines | Needs discipline to keep modules decoupled |
| Services by bounded context | Network calls, distributed consistency, ops overhead, contract versioning |
| Event-driven: components react to published facts | Eventual consistency, harder debugging, event schema evolution |

**Default:** modular monolith. **Deviate** when a boundary has a concrete reason to separate: a different scaling profile, independent team ownership or release cadence, or isolation of a risky dependency. Separate services own separate data; a database shared between "independent" services is a monolith with network calls.

## Communication mode

| Mode | Fits | Watch |
|---|---|---|
| Synchronous request/response | Caller needs the result now | Latency chains, cascading failure; keep call depth shallow |
| Queue (point-to-point) | Slow work, burst smoothing, independent retry | At-least-once, poison messages, ordering, visibility timeouts |
| Pub/sub events | Several independent consumers of one fact | Eventual consistency, schema versioning, consumer lag |
| Durable workflow | Multi-step processes with waits, retries, compensation | Another platform component; workflow versioning |
| Outbound webhooks | Notifying external systems | Consumer downtime, no ordering guarantee |

**Default:** synchronous for reads and user-facing validation; queue for anything slow or retryable; a durable workflow once a process has waits or compensations.

## Saga coordination

**Default:** orchestration (a coordinator drives the steps; easy to monitor). **Deviate** to choreography for flows of about three steps or fewer, with no money involved, where loose coupling outweighs seeing the whole flow.

## API style

| Option | Fits | Costs |
|---|---|---|
| REST | Public/partner APIs, cacheability, many client types | More round trips for complex views |
| GraphQL | Many client types with very different data needs, fast-moving UIs | Query cost control, caching, per-field authorization |
| Typed RPC (end-to-end types) | Internal API, one same-language frontend in the same repo | Tight coupling; poor fit for third parties |

**Default:** typed RPC when the only consumer is your own same-language frontend in the repo; REST otherwise. **Deviate** to GraphQL only with the many-divergent-clients need.

## Session model

| Option | Trade-off |
|---|---|
| Server sessions (opaque id in httpOnly cookie) | Instant revocation; a session lookup per request |
| Short-lived signed tokens + rotating refresh tokens | Stateless verification; revocation waits for expiry |

**Default:** server sessions when you own the browser client (BFF). **Deviate** to short-lived tokens (minutes, with refresh rotation) for mobile, third-party or service clients, or when a per-request lookup is too costly.

## Authorization model

| Option | Fits |
|---|---|
| RBAC: roles → permissions | Coarse, stable permission sets |
| ABAC: policies over attributes | Rules on context (time, region, plan, data classification) |
| ReBAC: relationships (owner, member, shared-with) | Collaboration and sharing |

**Default:** RBAC plus ownership checks. **Deviate** to ReBAC when sharing or collaboration is core to the product; add ABAC rules where context really decides access.

## Cache placement and strategy

Placement, outermost first: CDN/edge (public, cacheable responses) → shared key-value cache → in-process (per instance) → the store's own buffer cache.

| Strategy | Trade-off |
|---|---|
| Cache-aside: app reads cache, loads DB on miss | Simple; stale until TTL or invalidation |
| Read-through: cache layer loads on miss | Centralized; needs a capable cache layer |
| Write-through: write cache and DB together | Fresher reads; slower writes |
| Write-behind: write cache, flush to DB later | Fast writes; loss on failure |

**Default:** HTTP caching for public data, cache-aside for the rest. Write-behind fits only data you can afford to lose (counters, analytics), never business records.

## Health checks (long-running servers)

- **Liveness:** the process works; independent of the database.
- **Readiness:** the instance can serve; checks only dependencies it cannot serve without, so one slow dependency doesn't pull every instance out of rotation.

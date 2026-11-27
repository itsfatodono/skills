# Serverless and edge

Rules that hold when code runs on serverless or edge functions, on top of [SKILL.md](SKILL.md).

## Instances

- Instances are stateless and ephemeral: anything that must survive a request lives in storage, a shared cache, or a durable object store.
- Breaker, bulkhead and rate-limit state can't live in instance memory: use a shared store, platform concurrency limits, or a queue in front of the dependency.
- Cold starts stay short: small dependency graph, lazy-load rare paths, light initialization.

## Concurrency hits dependencies

- Elastic scaling turns a traffic spike into many instances: concurrent instances ≈ req/s × latency (Little's law), and each may open its own connection to every downstream.
- Protect each downstream with a connection pooler or proxy, a concurrency cap, and a queue as a burst buffer.

## Placement

- Compute runs near the data: API handlers in the region of the system of record.
- Edge runs stateless work only: token checks, redirects, cache hits, personalization from edge-local data. An edge handler querying a single-region store turns every query into a long round trip.

## Persistent connections

- WebSocket and SSE connections outlive a function invocation: they terminate at a stateful component (managed pub/sub, a durable connection service) that functions publish to.

## Execution limits

- Requests have CPU and wall-time caps. Work beyond them goes to a queue, scheduled job, or durable workflow; reply 202 + a status resource.
- A request that would block on another in-flight request (e.g. a duplicate idempotency key) answers 409 at once.

## Deployment unit

| Option | Trade-off |
|---|---|
| One app per bounded context, internal routing | Shared middleware, fewer cold starts, simple deploys |
| Function per route | Isolated scaling and permissions; duplicated setup, more cold starts |

**Default:** one app per bounded context. **Deviate** for a route with a sharply different resource, permission or scaling profile.

## Health

The platform manages instance health; liveness and readiness endpoints (CHOICES.md) apply only to long-running components beside the functions.

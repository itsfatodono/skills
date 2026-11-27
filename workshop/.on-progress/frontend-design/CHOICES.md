# Frontend design choices

Open frontend choices, each with its options, a **default**, and the signal to deviate. A default is a recommended answer, not a verdict: the project's requirements and ADRs decide.

API style (REST, GraphQL, typed RPC) is a contract choice: see `backend-design`'s CHOICES.md.

## Rendering strategy (per route group, never per app)

| Strategy | Strengths | Costs | Fits |
|---|---|---|---|
| Static generation (build time) | Fastest TTFB/LCP, CDN-cacheable, cheap | Stale until rebuild; no per-user content | Marketing, docs, rarely changing content |
| Incremental / on-demand static | Static speed with periodic or event-driven refresh | Revalidation complexity; brief staleness | Catalogs, product pages, blogs |
| Server rendering per request | Fresh, personalized, indexable, less JS | Server cost and latency per request; TTFB tied to the slowest data | Personalized indexable pages, search results |
| Streaming server rendering | Shell early, slow sections stream in | Careful boundary placement; harder caching | Fast shell plus slow data |
| Server components / islands / partial hydration | JS only for interactive parts; data fetched near its source | Server/client boundary design; mental model | Content-heavy pages with pockets of interactivity |
| Client rendering (SPA) | Rich interactivity, simple hosting, smooth in-app navigation | Blank until JS loads; JS-heavy; weak SEO; fetch waterfalls | Authenticated apps, dashboards, editors |

**Default:** hybrid. Public, rarely changing routes static or incremental; personalized indexable routes server-rendered, streaming when some data is slow; authenticated app routes client-rendered or server-component based, per the framework in use.

**Edge rendering** pays off only when the data it needs is also at the edge (cache, KV); against a single-region database it adds latency.

## App structure

| Option | Fits | Cost |
|---|---|---|
| Single app, feature folders | One or a few teams, shared release | Discipline keeps boundaries |
| Modular monolith (enforced module boundaries, one deploy) | Several teams, shared UX, independent ownership | Boundary-enforcement tooling |
| Micro-frontends (independent deploys) | Many autonomous teams needing independent release cadence | Duplicate dependencies, consistency drift, integration testing, performance overhead |

**Default:** single app with feature folders; enforce module boundaries once several teams share it. Micro-frontends answer an organizational problem (deploy coupling across many teams), never a technical one.

## Backend-for-Frontend

**Default:** call the API directly. **Add a BFF** when screens aggregate data from many services, internal APIs or secrets must stay hidden, web and mobile need differently shaped payloads, or server-side auth with httpOnly cookies needs a home.

## Server-state library

| Option | Fits |
|---|---|
| The framework's data layer (route loaders, server components) | The framework already fetches per route or on the server |
| A dedicated server-state cache library | Client-rendered apps with rich cache needs: invalidation, optimistic updates, infinite lists |
| A GraphQL client with a normalized cache | GraphQL APIs |

**Default:** whatever the project already uses. For a new project: the framework's data layer when it has one, otherwise a dedicated server-state library. Either way, the server-state cache rules in SKILL.md hold.

## Cache shape

| Option | Fits |
|---|---|
| Query-shaped (one entry per request) | Most apps; simple |
| Normalized entity store (by type + id) | The same entity appears in many views and must update everywhere at once (chat, collaboration, social feeds) |

**Default:** query-shaped.

## Fetch timing

| Moment | Pros | Cons |
|---|---|---|
| On render (component asks) | Simple, colocated | Parent-then-child waterfalls, late start |
| On route transition (route declares its data) | Parallel, starts before render | Routes must know their data needs |
| Prefetch on intent (hover, viewport, likely next step) | Instant navigation | Wasted bandwidth when wrong |
| Server-side, with the HTML | Data near its source, no client round trip | Page latency tied to the slowest query unless streamed |

**Default:** route-level data declaration, plus prefetch on intent for the likely next step.

## Mutation pattern

| Pattern | UX | Complexity | Fits |
|---|---|---|---|
| Pessimistic (wait for the server) | Spinner, always correct | Low | Payments, irreversible or validation-heavy actions |
| Response-to-cache + invalidate | Correct, slight delay | Low | Most CRUD |
| Optimistic (apply now, roll back on error) | Instant | Medium: rollback, ordering, conflicts | Likes, toggles, reordering, sending a chat message |

**Default:** response-to-cache plus invalidation of affected queries. Pessimistic for irreversible actions; optimistic for small, reversible, high-frequency actions.

## Conflict policy for concurrent edits

| Policy | Fits |
|---|---|
| Last write wins | Low-value fields, single-editor data |
| Version check with a "someone else changed this" prompt (ETag/version) | Most shared records |
| Field-level merge | Forms where different users edit different fields |
| CRDT / OT | Real-time co-editing |

**Default:** version check with a prompt.

## Real-time transport

| Option | Direction | Fits | Costs |
|---|---|---|---|
| Polling | Client pull | Low frequency, staleness of tens of seconds tolerated | Wasted requests; latency = interval |
| Server-Sent Events | Server → client | Notifications, feeds, progress, AI token streams | One-way; writes go over normal requests |
| WebSocket | Bidirectional | Chat, presence, collaboration, games | Stateful connections; reconnection, scaling and auth are yours |
| Long polling | Pull emulating push | Environments that block the others | Connection churn |

**Default:** SSE for server-to-client updates; WebSocket when the client also streams (presence, co-editing); polling when the staleness budget allows it. On a serverless backend, either transport needs a stateful connection component: see `backend-design`'s SERVERLESS.md.

## Offline level

| Level | Means |
|---|---|
| 1. Graceful failure | Clear offline messages, nothing lost silently |
| 2. Cached read-only | Recently seen data readable offline |
| 3. Offline writes | Mutations queued and synced later (see Offline in SKILL.md) |

**Default:** level 1. **Deviate** to level 2 for read-on-the-go journeys, to level 3 only for an explicit offline-write requirement.

---
name: frontend-design
description: Frontend rules and design defaults for web apps. Use when designing, grilling or reviewing a frontend decision, or when writing or reviewing components, client state, or data-fetching code.
---

# Frontend design

A pool of rules. It owns no process: consult the sections the current decision or code touches, and let the calling workflow (grilling, wayfinder, implementation, review) own the steps and the deliverable.

Project ADRs and the glossary win over these defaults. A deliberate deviation is a decision worth recording as an ADR.

Vendors, products and libraries already in the project are the given. Adding or replacing one is the user's decision: present the candidates as options, each with its trade-off, and recommend by requirement.

Beside this file:

- **Grilling or design review:** read [CHOICES.md](CHOICES.md) before the first question. Its defaults are the recommended answers for rendering per route, app structure, BFF, server-state library, cache shape, fetch timing, mutation pattern, conflict policy, real-time transport and offline level; a recommendation drawn from it names its entry (`CHOICES: Fetch timing`).
- **At session start, once the stack is known:** read [REACT.md](REACT.md) if the UI runtime is React.
- **The client–server contract itself is being designed** (API style, errors, pagination, idempotency, versioning): invoke the `backend-design` skill.

## Stance

- **Every decision is a trade-off.** Name the options rejected and why. "It depends" is followed by *on what* and *which way*.
- **Requirements over fashion.** A rendering strategy, state library or micro-frontend split is justified by a requirement (SEO, latency budget, team topology, offline need).
- **Numbers over adjectives.** Targets are measurable and measured in the field.

## A frontend design is ready when

Each item has a recorded answer, an explicit assumption, or "not applicable", in the spec or an ADR:

- **Journeys:** the top 3 user journeys, the entities they touch, read- or write-heavy, collaboration level (single user, multi-user, live co-editing).
- **Loading:** Core Web Vitals targets at p75 per device class (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 as the baseline); first vs repeat visit; public vs logged-in.
- **Devices and network:** per-route budgets for compressed JS, request count, main-thread time on the weakest target device.
- **SEO and sharing:** which routes need server-rendered HTML or link previews.
- **Freshness:** maximum staleness per data type.
- **State:** each screen's state classified, with filters, sort and page in the URL (see State).
- **Server-state cache:** per query, its cache key, staleness window and invalidation triggers (see Server-state cache).
- **Screen states:** loading, empty and error designed for every screen where they are not obvious (see Network and resilience).
- **Real-time:** which changes by others must appear live, and how fast.
- **Offline:** which journeys work without network, read-only or with writes.
- **Data on screen:** maximum items rendered, document size, memory ceiling.
- **Accessibility:** WCAG 2.2 AA unless stated otherwise.
- **i18n:** locales at launch and later, RTL, currencies, time zones.
- **Security:** data that never reaches the client, and data never stored client-side; the Content Security Policy; scheme checks on user-supplied URLs (see Security).
- **Team:** how many teams touch the frontend, and whether they need independent deploys.
- **Out of scope:** written down; unstated scope is where designs go wrong.

## Architecture and boundaries

- **Layers**, dependencies pointing downward only:
  1. Routes / screens: composition, layout, route-level data requirements.
  2. Feature modules: a feature's UI and logic, owned by one team.
  3. Domain logic: business rules, formatting, validation; framework-free.
  4. Data access: server-state cache, API client, response validation.
  5. Platform: design system, routing, auth session, telemetry, feature flags.
- **Vertical slices:** organize by feature. A feature owns its screens, components, data hooks and tests behind a small public surface; cross-feature use goes through that surface or the platform layer.
- Business rules live in the domain layer, testable without rendering.
- **The data access layer alone knows URLs, transport and response shapes.** UI speaks in domain terms ("invoices for customer X").

## State

Classify every piece of state before placing it:

| Kind | Source of truth | Lives in |
|---|---|---|
| Server state (entities, lists) | Backend | Server-state cache keyed by query, or server-rendered |
| URL state (filters, sort, page, tab, search) | The URL | Route and query params |
| Form / draft state | The user, until submitted | Form-local, reconciled on submit |
| Ephemeral UI state (open, hover, step) | Component | The lowest component that needs it |
| Session / global client state (theme, session snapshot, flags) | Client | A small global store; tiny, rarely changing |
| Persistent client state (preferences, offline data) | Client storage | localStorage for tiny sync data, IndexedDB for large async data; schemas versioned and migrated |

- **One source of truth per datum.** The client holds a *cache* of server state, never a second copy in another store.
- **Derive, don't store:** totals, filtered lists and selected objects are computed from minimal state (store `selectedId`, derive the object).
- Shareable view state (filters, sort, pagination, selected tab) lives in the URL, so links, bookmarks and back/forward work.

## Server-state cache

- Every query defines: its **cache key** (what makes two requests the same), its staleness window, its invalidation triggers (mutation success, real-time event, focus, reconnect), and its garbage collection.
- Stale data stays on screen while revalidating.
- Paginated lists define what happens to cached pages when an item is inserted or deleted. Infinite lists cache an array of pages keyed by cursor.
- Cache shape (query-shaped vs normalized): CHOICES.md.

## Fetching

- **Independent requests start in parallel, as early as possible.** Request waterfalls are removed before any rendering micro-optimization.
- Fetch timing: CHOICES.md.
- Responses are validated at the data access boundary, so contract drift fails loudly in one place; validation failures are logged.
- Screens get screen-shaped data: one or a few requests per screen, no huge objects for a single field. Total counts are requested only when the UI shows them.
- The deployed client and server are out of sync during rollouts and in long-open tabs: the client reads tolerantly (unknown fields ignored, new enum values handled).

## Mutations

- The client writes the resource a mutation returns into the cache and invalidates the queries it affects (lists, counts).
- Mutation pattern (pessimistic, optimistic, refetch) and concurrent-edit conflict policy: CHOICES.md.
- Every optimistic update has a rollback and a defined ordering when several are in flight.
- Creates and payments the client may retry carry an idempotency key generated once per user intent.

## Network and resilience

- Every request has a timeout. Retries use exponential backoff with jitter, for idempotent or keyed requests only.
- **Error boundaries** at route and widget level, with retry affordances: one failing widget leaves the rest of the page working.
- Every async view has four designed states: **loading** (a skeleton matching the final layout), **empty**, **error** (actionable), **success**.
- Per dependency (search, recommendations, real-time), a degraded mode is decided: hide, fallback, or read-only.
- **Version skew:** a chunk-load failure after a new deploy prompts a reload.
- Risky features ship behind feature flags with a kill switch.

## Real-time

- Transport choice: CHOICES.md.
- Connections reconnect with backoff, then **resync**: fetch everything since the last cursor or sequence number.
- Pushed events are deduplicated by event id, ordered, and merged into the server-state cache.

## Offline

- Offline level: CHOICES.md.
- Offline writes need: a durable local store; an **outbox** of pending mutations with idempotency keys; a replay order; a conflict policy; UI states for "pending sync" and "sync failed"; storage quota and eviction handling.

## Components and design system

- Shared components are APIs: minimal inputs, composition over configuration flags, defined controlled/uncontrolled behaviour, accessibility built in.
- Layers: tokens (color, spacing, type, motion) → primitives (button, input, dialog) → composites → page patterns.

## Performance

- Per-route budgets (JS size, LCP, INP) are enforced in CI; real-user field data is the measure, lab scores the early warning.
- **Critical path:** what the first meaningful content needs is server-rendered or inlined; everything else is deferred.
- Code splitting at route boundaries first, then for heavy, rarely used features (editors, charts, maps, admin), coarse enough that navigation never becomes a request cascade.
- **INP is main-thread time:** heavy computation moves to a web worker or the server; long lists are virtualized; non-urgent updates are marked low priority.
- **Render scope:** fast-changing state stays local; global stores and contexts are split by update frequency.
- Media: responsive images with explicit dimensions, modern formats, lazy below the fold, the LCP image prioritized.
- Caching layers: content-hashed static assets with long immutable caching on the CDN; HTML short-lived or revalidated; public API data via HTTP caching; the in-memory server-state cache; a service worker for offline and repeat visits.
- Third-party scripts load late, run isolated, and sit inside the budget like first-party code.

## Security

- The client is untrusted: it holds no secrets, and every authorization decision is re-checked on the server. Hidden UI is not access control.
- **XSS** is the critical risk: framework escaping for all output; any rendered HTML sanitized; a Content Security Policy; user-supplied URLs scheme-checked (`https:`, `mailto:`) before use.
- Sessions ride httpOnly, Secure, SameSite cookies issued by the backend/BFF, with CSRF protection. A token that must live in JS is short-lived and held in memory.
- The client receives only fields the user may see; sensitive data stays out of browser storage; client caches and storage are cleared on logout.
- Dependencies are few and audited; third-party scripts are self-hosted or pinned with subresource integrity.

## Accessibility and i18n

Both are decided by the architecture, so they are built in from the first component.

- Semantic structure and keyboard operability live in the design-system primitives, so every feature inherits them.
- Focus is managed on route changes and in dialogs; async results are announced via live regions; the token palette meets WCAG AA contrast; reduced motion is respected.
- All strings are externalized from day one; dates, numbers, currencies and plurals use locale-aware formatting.
- Layouts tolerate text expansion and RTL (logical CSS properties).
- Times travel as UTC and display in the user's zone; per-language indexable pages carry the locale in the URL.

## Observability

- Real-user monitoring of Core Web Vitals per route and device class.
- Error tracking tagged with release version, route, and the correlation id shared with backend logs.
- Product analytics on key journey funnels, behind consent.

## Testing

- Domain logic: many cheap unit tests.
- Features: behaviour-level integration tests against a mocked network layer, querying elements by accessible role and name.
- Critical journeys: a few end-to-end tests against a real backend in a staging-like environment.
- Client and API share a schema or run contract tests.
- Design system: visual regression and automated accessibility checks in CI, plus periodic manual screen-reader passes.

## Evolution

- Feature flags: ship, roll out progressively, measure, then remove the flag.
- Migrations (state library, rendering mode, design system) go incrementally, strangler-style, route by route.
- Each architectural choice tracks its cost: bundle size, build time, onboarding complexity.

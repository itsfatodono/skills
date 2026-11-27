# React

How the rules in [SKILL.md](SKILL.md) land on React. Version-specific facts name their version; verify against the version in use.

## State and effects

- Derived values are computed during render; an effect that only syncs one piece of state from another is a derivation in disguise.
- Effects synchronize with systems outside React (subscriptions, timers, non-React widgets), and each one cleans up.
- List keys are stable ids, so reordering and inserts keep component state attached to the right item.
- Context consumers all re-render when the value changes: split contexts by update frequency and keep fast-changing values out of broad providers.

## Boundaries

- **Error boundaries** catch render-time errors in their subtree; event-handler and async errors are caught in code and surfaced as state.
- **Suspense boundaries** define loading states and streaming chunks: place them where a skeleton makes visual sense.
- `React.lazy` + Suspense splits routes and heavy features; a chunk-load failure lands in an error boundary that offers a reload.

## Server components

Where the framework renders server components:

- Components are server components unless marked; `"use client"` marks the client boundary.
- Props crossing the boundary are serializable.
- Client components stay leaf-ward, so interactive islands stay small.

## Responsiveness

- Non-urgent updates go through `startTransition` / `useTransition`; expensive derived views through `useDeferredValue`.
- With React Compiler enabled, memoization is automatic. Without it, `memo` / `useMemo` / `useCallback` go where profiling shows a cost.

## Forms with actions (React 19+)

Where forms are built on React actions:

- Actions with `useActionState` carry pending and error state for form submissions.
- `useOptimistic` holds the optimistic value until the action settles.

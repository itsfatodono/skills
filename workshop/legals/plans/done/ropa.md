# RoPA / KVKK processing inventory

| | |
|---|---|
| Id | `ropa` |
| Seed no. | 18 |
| Kind | document |
| Regions | root, with `eu`, `uk` blocks |
| Needed when | a region needs it |
| Status | **done** (built and reviewed) |
| Decisions | `PLAN.md` 28, 35, 36, 37 |

## Built

| File | Part | Samples | Saturated | Scanned |
|---|---|---|---|---|
| `skeletons/ropa.md` | root | 30 | true | 2026-10-26 |
| `regions/eu/ropa.md` | block | 15 | false | 2026-10-27 |
| `regions/uk/ropa.md` | block | 22 | true | 2026-10-27 |

Research: `research/ropa/`, `research/regions/<code>/ropa/`.

## Open tasks

None.

## Won't build

- `tr` block: No company or public university publishes a filled inventory (`research/regions/tr/ropa/README.md`). The RoPA is not triggered for `tr` until a block exists.

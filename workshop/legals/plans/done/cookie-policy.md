# Cookie Policy

| | |
|---|---|
| Id | `cookie-policy` |
| Seed no. | 6 |
| Kind | document |
| Regions | root; *Avoid* marks for `eu`, `tr`, `uk` |
| Needed when | non-essential cookies or trackers on the web |
| Status | **done** (built and reviewed) |
| Decisions | `PLAN.md` 44 |

## Built

| File | Part | Samples | Saturated | Scanned |
|---|---|---|---|---|
| `skeletons/cookie-policy.md` | root | 20 | true | 2026-10-27 |
| `regions/eu/cookie-policy.md` | block (*Avoid* marks only) | 20 | true | 2026-10-27 |
| `regions/tr/cookie-policy.md` | block (*Avoid* marks only) | 20 | true | 2026-10-27 |
| `regions/uk/cookie-policy.md` | block (*Avoid* marks only) | 20 | true | 2026-10-27 |

Research: `research/cookie-policy/`, `research/regions/<code>/cookie-policy/`.

## Open tasks

- [ ] `eu` block as its own region run. The current `eu` file only marks *Avoid* patterns.
- [ ] Then judge whether a `us` block adds anything beyond the privacy policy's `us` block.
- [ ] `uk` block: deferred by the owner (2026-10-27).
- [ ] `tr` block, `browser-controls`: waits for the wording of the KVKK cookie guide.
- [ ] Banner text: a separate item (a form or template), not built.

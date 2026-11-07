# terms-of-service: build record

Built 2026-10-26 (Phase 3, batch 1). Skeleton:
`plugins/fatodono-launchkit/skills/legals/skeletons/terms-of-service.md`.

## Files

- `candidates.md`: the pool of 30 and the reserve.
- `pool/`: raw rows from the `pool-collector` slices.
- `samples/sNN.md`: one extraction table per sample.
- `section-map.md`: each table row mapped to a section id (the basis of every count).
- `merge.md`: section ids and their meanings, merged list, folds, saturation log, document
  level, *Regional content*.
- `proposed-facts.md`: fact keys the skeleton names that `helpers/facts-schema.md` lacks.

## Run

- **Routes run:** R1 (US App Store charts) and R2 (App Store long-tail keywords), in six slices
  (`pool/r1-*`, `pool/r2-tail-*`), then R4 on each developer's site to find the terms URL. The R3
  (Play) slice planned by the first run never landed; it was not rerun because the pool already
  held 30 candidates (10 per size) from R1 and R2, and the build stopped with the pool, not with
  the routes.
- **Pool:** 30 candidates, 10 large, 10 mid, 10 small; no sector above 4 of 30. Group check (rule
  5) done at selection. 40 reserve candidates were never needed.
- **First batch:** s01–s15. s01, s02, s06 and s10 were extracted by the stopped run and kept; their
  old template-comparison notes were removed. The other eleven were extracted in this run. All 15
  valid.
- **Saturation:** s16–s30 judged in pool order (log in `merge.md`). New: s16, s17, s18, s19, s22,
  s26, s29, each only by a section written in a format (mostly a list) not yet recorded for it.
  No new section id appeared after s15.
- **Stop reason:** pool exhausted at s30 without 5 non-new samples in a row.
  `saturated: false`, `sample_count: 30`.

## Invalid

None. No candidate was unreachable or the wrong document.

## Templates

Rule 4 (one text, one sample): no two samples share a whole text, so no copies. Templates seen,
all kept as samples:

- s05 and s06 come from the same law-firm consumer-terms template family (same headings in the
  same order for most sections, several identical stock sentences), each with its own
  product-specific sections and dispute clauses.
- s09, s21 and s27 read as generator output (generic "Terms and Conditions" wording, a
  definitions list in s09, an unfilled venue placeholder in s27).

## Size thirds

10 large, 10 mid, 10 small. No shortfall.

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Anthropic PBC | https://www.anthropic.com/legal/consumer-terms | productivity | large | en | 2026-10-26 |
| s02 | Substack Inc. | https://substack.com/tos | news | mid | en | 2026-10-26 |
| s03 | Flighty LLC | https://flighty.com/legal/terms | travel | small | en | 2026-10-26 |
| s04 | Strava Inc. | https://www.strava.com/legal/terms | health-fitness | large | en | 2026-10-26 |
| s05 | Suno Inc. | https://suno.com/terms | music | mid | en | 2026-10-26 |
| s06 | Partiful Co. | https://partiful.com/terms | lifestyle | small | en | 2026-10-26 |
| s07 | Block, Inc. (Cash App) | https://cash.app/us/en/legal/tos | finance | large | en | 2026-10-26 |
| s08 | Speakeasy Labs, Inc. (Speak) | https://www.speak.com/terms | education | mid | en | 2026-10-26 |
| s09 | Sebastian Roehl (HabitKit) | https://habitkit.app/terms | productivity | small | en | 2026-10-26 |
| s10 | Snap Inc. | https://www.snap.com/terms?lang=en-US | photo-video | large | en | 2026-10-26 |
| s11 | Hallow, Inc. | https://hallow.com/terms-of-service | reference | mid | en | 2026-10-26 |
| s12 | Deglazed LLC | https://www.deglaze.app/terms | food-drink | small | en | 2026-10-26 |
| s13 | Walmart Inc. | https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0 | shopping | large | en | 2026-10-26 |
| s14 | Brave Software, Inc. | https://brave.com/terms-of-use/ | utilities | mid | en | 2026-10-26 |
| s15 | Matthew Steedman (Mochi Cards, LLC) | https://mochi.cards/terms | education | small | en | 2026-10-26 |
| s16 | Airbnb, Inc. | https://www.airbnb.com/help/article/2908 | travel | large | en | 2026-10-26 |
| s17 | Rocket Money, Inc. | https://www.rocketmoney.com/terms | finance | mid | en | 2026-10-26 |
| s18 | Just Imagine, Inc. (Rosebud) | https://help.rosebud.app/about-us/terms-of-service | health-fitness | small | en | 2026-10-26 |
| s19 | Reddit, Inc. | https://redditinc.com/policies/user-agreement | news | large | en | 2026-10-26 |
| s20 | 9280-0366 Quebec inc. (Transit) | https://transitapp.com/terms | navigation | mid | en | 2026-10-26 |
| s21 | Weekly LLC | https://weeklybudgeting.com/terms | finance | small | en | 2026-10-26 |
| s22 | Spotify USA Inc. | https://www.spotify.com/us/legal/end-user-agreement/ | music | large | en | 2026-10-26 |
| s23 | AllTrails, LLC | https://www.alltrails.com/terms | health-fitness | mid | en | 2026-10-26 |
| s24 | Arthur Chang (Priime) | https://prii.me/terms.html | photo-video | small | en | 2026-10-26 |
| s25 | Pinterest, Inc. | https://policy.pinterest.com/en/terms-of-service | lifestyle | large | en | 2026-10-26 |
| s26 | Hinge, Inc. | https://hinge.co/terms | lifestyle | mid | en | 2026-10-26 |
| s27 | Fable Group Inc. | https://fable.co/terms | books | small | en | 2026-10-26 |
| s28 | Coursera, Inc. | https://www.coursera.org/about/terms | education | large | en | 2026-10-26 |
| s29 | Kahoot! ASA | https://trust.kahoot.com/terms-and-conditions/ | education | mid | en | 2026-10-26 |
| s30 | Invoice Home Inc. | https://invoicehome.com/terms | business | small | en | 2026-10-26 |

Versions taken where a page holds several: s10, s16, s19 and s22 the version for US users (the
default en-US page); s19 also records the EEA/UK/CH deviations as extra rows; s08 the main text
(its France/Germany appendix is recorded as rows and as regional content); s28 only the Terms of
Use part of a five-document page.

## Folded subject items

Subscription terms, refunds and account deletion are separate catalog items, but the samples fold
them into the terms. They are recorded as the ToS's own sections, as the samples write them:
`subscriptions` (23/30), `refunds` (23/30), `account-closure` (18/30).

**Re-judged (2026-10-26):** under `PLAN.md` decision 27 (new section ids only) the run
saturated at s20; see `merge.md`.

## Lessons

- **Format novelty keeps a many-section document from saturating.** A terms of service has about
  35 section ids. After s15 no sample added a section id, but 7 of the 15 later samples were "new"
  only because one section was written as a list where only prose had been seen (or the reverse).
  The rule reset the counter every few samples, and the pool ran out with `saturated: false` even
  though the section list was stable from the first batch. The rule did what it says; it measures
  format variety more than section coverage for long contracts.
- **Format is recorded per row, so one bullet decides novelty.** A single bulleted sub-clause
  inside an otherwise prose section counts as the section being "written as a list". Judging
  format on the section's main body would be steadier, but `build.md` does not say which row
  stands for a section.
- **Granular extraction tables need a mapping step.** One row per heading or run-in sub-heading
  gave tables of 11 to 280 rows (s07, a financial app, had 280). Mapping every row to an id in a
  separate file (`section-map.md`) and counting with a script made the merge checkable; `build.md`
  says to map sections to ids but not where that mapping is kept.
- **Arbitration is regional practice, not a regional law.** The root rule ("what one law
  requires") does not cover arbitration clauses: no law requires them, but they are a US
  consumer-contract practice that would be wrong for most other companies. The skeleton keeps
  dispute resolution in the root and makes arbitration depend on a fact
  (`facts.company.dispute_forum`); the US mechanics (FAA, providers, mass filings) went to
  *Regional content*.
- **Shared subagent limit.** The five batch items share one limit of 20 concurrent subagents.
  Dispatching a batch at once failed for most calls, so extractors went out one or two at a time
  as slots freed; one extractor died on an API overload (529) and was re-dispatched once.

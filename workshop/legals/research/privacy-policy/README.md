# privacy-policy: build record

Built 2026-10-26 (Phase 2 pilot). Skeleton: `plugins/fatodono-founderkit/skills/legals/skeletons/privacy-policy.md`.

## Run

- **Routes run:** R1 (US charts, 18 genres), R2 (16 keywords), R3 (Play US, 5 categories), R4.
  Raw rows: `pool/` (185 rows from 7 `pool-collector` slices). Selection: `candidates.md`.
- **Re-judged 2026-10-27** under decisions 26 (templates and generated texts are valid samples)
  and 27 (only a new section id makes a sample new). s09 and s15, dropped by the first run as
  generated texts, are valid; neither is a copy of another sample. The run below is the
  re-judged one; details in `merge.md`.
- **First batch:** s01–s15 (5 large, 5 mid, 5 small, no replacements; decision 41).
- **Saturation:** s16–s20, none new. Stop after s20. s21–s32 came past the stop point and are
  kept.
- **Stop reason:** saturated after s20. `sample_count: 32`.
- **First run, for the record:** s09 and s15 replaced by s21 and s24; new s22, s23, s25; stop
  after s30 with 30 samples.
- **Merged section list:** `merge.md` (all 32 samples).

## Invalid

None. s09 (Wanderlog, a privacypolicygenerator.info text with company-written feature notices)
and s15 (Bear, an iubenda text served in an iframe; the `/full-legal` view was extracted) were
invalid under the old rule 4 and are valid samples under decision 26.

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Spotify | https://www.spotify.com/us/legal/privacy-policy/ | music | large | en | 2026-10-26 |
| s02 | Telegram FZ-LLC | https://telegram.org/privacy | social-networking | mid | en | 2026-10-26 |
| s03 | Flighty LLC | https://flighty.com/legal/privacy | travel | small | en | 2026-10-26 |
| s04 | Airbnb, Inc. | https://www.airbnb.com/help/article/3175 | travel | large | en | 2026-10-26 |
| s05 | Calm.com, Inc. | https://www.calm.com/privacy-policy | health-fitness | mid | en | 2026-10-26 |
| s06 | Partiful Co. | https://partiful.com/privacy | lifestyle | small | en | 2026-10-26 |
| s07 | Capital One Services, LLC | https://www.capitalone.com/privacy/online-privacy-policy/ | finance | large | en | 2026-10-26 |
| s08 | Proton AG | https://proton.me/legal/privacy | utilities | mid | en | 2026-10-26 |
| s09 | Travelchime Inc. (Wanderlog) | https://wanderlog.com/privacy | travel | small | en | 2026-10-26 |
| s10 | LinkedIn Corporation | https://www.linkedin.com/legal/privacy-policy | business | large | en | 2026-10-26 |
| s11 | You Need A Budget LLC (YNAB) | https://www.ynab.com/privacy-policy/ | finance | mid | en | 2026-10-26 |
| s12 | ReciMe Pty Ltd | https://recime.app/privacy-policy | food-drink | small | en | 2026-10-26 |
| s13 | Netflix, Inc. | https://help.netflix.com/legal/privacy | entertainment | large | en | 2026-10-26 |
| s14 | Substack Inc. | https://substack.com/privacy | news | mid | en | 2026-10-26 |
| s15 | Shiny Frog Ltd. (Bear) | https://www.iubenda.com/privacy-policy/7945401/full-legal | productivity | small | en | 2026-10-26 |
| s16 | Walmart | https://corporate.walmart.com/privacy-security/walmart-privacy-notice | shopping | large | en | 2026-10-26 |
| s17 | Feeld Ltd | https://feeld.co/about/privacy | lifestyle | mid | en | 2026-10-26 |
| s18 | Brainstash Inc | https://deepstash.com/privacy_policy | education | small | en | 2026-10-26 |
| s19 | REDDIT, INC. | https://web.archive.org/web/20261026065130/https://www.reddit.com/policies/privacy-policy | news | large | en | 2026-10-26 |
| s20 | Hallow, Inc. | https://hallow.com/privacy-policy | reference | mid | en | 2026-10-26 |
| s21 | Reviva Softworks Ltd | https://www.snorelab.com/snorelab-app-privacy-policy | medical | small | en | 2026-10-26 |
| s22 | Tinder LLC | https://policies.tinder.com/privacy/intl/en/ | lifestyle | large | en | 2026-10-26 |
| s23 | Monkimun Inc (Lingokids) | https://lingokids.com/privacy-policy | education | mid | en | 2026-10-26 |
| s24 | Signal Foundation | https://signal.org/legal/ | social-networking | small | en | 2026-10-26 |
| s25 | Dropbox, Inc. | https://www.dropbox.com/privacy | productivity | large | en | 2026-10-26 |
| s26 | Huckleberry Labs Inc. | https://huckleberrycare.com/privacy-policy | medical | mid | en | 2026-10-26 |
| s27 | Drawboard Pty Ltd | https://www.drawboard.com/privacy | productivity | small | en | 2026-10-26 |
| s28 | Snap, Inc. (Snapchat) | https://values.snap.com/privacy/privacy-policy?lang=en-US | photo-video | large | en | 2026-10-26 |
| s29 | Brave Software | https://brave.com/privacy/browser/ | utilities | mid | en | 2026-10-26 |
| s30 | Dovly, Inc. | https://www.dovly.com/privacy-policy/ | finance | small | en | 2026-10-26 |
| s31 | Epic Systems Corporation (MyChart) | https://www.epic.com/en-us/privacypolicies/ | medical | large | en | 2026-10-26 |
| s32 | Suno Inc. | https://suno.com/privacy | music | mid | en | 2026-10-26 |

## Format 2 (2026-10-26)

The skeleton was split per `region-format.md`: the root `skeletons/privacy-policy.md` is
region-neutral, and `legal-bases`, `us-states`, `eu-uk`, `dpf` and the regional patterns of
`controller`, `advertising`, `transfers` and `rights` moved to `regions/eu`, `regions/uk` and
`regions/us`. No sample was re-fetched. EU and US counts are the pilot's (now over 32 samples, with s09 and
s15); UK counts were
recounted from the extraction tables (rows that name the UK) and are lower bounds. `other-regions`
was dropped; its samples are listed in `merge.md` *Regional content* for future region runs.

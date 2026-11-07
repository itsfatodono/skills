---
doc_id: ropa
region: uk
built: 2026-10-27
routes_run: [R10, R11, R4]
raw_rows: pool/ and research/ropa/pool/r10-uk-public.md
---

UK pool for the RoPA's `uk` block. The global pool's UK samples come first (`build/build.md`
*Region run*: they count toward the batch) and keep their global ids, whose tables are in
`research/ropa/samples/`. New samples take ids from s41 and have UK-view tables in `samples/`.
Every row is `public-sector` (s09 is a charity, sector `education`): no UK company publishes
its record. Rows rotate size (large, mid, small) in pool order.

**Oxford ruling (2026-10-27, owner):** the five Oxford colleges (s02, s20, s41, s42, s46) are
one group (rule 5). s02 stays; s20, s41, s42 and s46 are dropped. The first batch below is
then 14 samples (3 mid), and the saturation order loses s42 and s46 (`merge.md`).

## First batch

16 samples: 5 large, 5 mid, 5 small and the ICO model. Four mid samples came from the global
pool; s41 is new.

| Id | Company | Body type | Size | Source |
|---|---|---|---|---|
| s01 | Herefordshire and Worcestershire Health and Care NHS Trust | nhs | large | global |
| s02 | Christ Church, Oxford | uk-college | mid | global |
| s03 | Little Smeaton Parish Council | parish-council | small | global |
| s07 | University of Manchester | uk-university | large | global |
| s05 | Leeds Arts University | uk-university | mid | global |
| s06 | Bexhill-on-Sea Town Council | town-council | small | global |
| s13 | London Borough of Haringey | uk-council | large | global |
| s14 | MLA College | uk-college | mid | global |
| s09 | Friends of the Angus | charity | small | global |
| s25 | University of Worcester | uk-university | large | global |
| s20 | Jesus College, Oxford (dropped: Oxford group) | uk-college | mid | global |
| s15 | Acton Burnell, Frodesley, Pitchford, Ruckley & Langley Parish Council | parish-council | small | global |
| s28 | Oldham Council | uk-council | large | global |
| s41 | Brasenose College, Oxford (dropped: Oxford group) | uk-college | mid | new (`pool/r10-uk-extra.md`) |
| s18 | Horsforth Town Council | town-council | small | global |
| s31 | ICO controller documentation template | standard-form | none | global |

## Saturation order

| Order | Id | Company | Body type | Size | Source |
|---|---|---|---|---|---|
| 1 | s43 | London Fire Brigade | uk-fire | large | new |
| 2 | s42 | St John's College, Oxford (dropped: Oxford group) | uk-college | mid | new |
| 3 | s21 | Badgeworth Parish Council | parish-council | small | global |
| 4 | s45 | Epping Forest District Council | uk-council | large | new |
| 5 | s46 | All Souls College, Oxford (dropped: Oxford group) | uk-college | mid | new |
| 6 | s27 | Peasenhall Parish Council | parish-council | small | global |
| 7 | s48 | NHS England (NHS Digital GDPR register) | nhs | large | new |
| 8 | s44 | Bracebridge Heath Parish Council | parish-council | small | new (global reserve) |
| 9 | s49 | Derbyshire County Council | uk-council | large | new (global reserve) |
| 10 | s47 | Ramsbury & Axford Parish Council | parish-council | small | new (global reserve) |
| 11 | — | Caister-on-Sea Parish Council | parish-council | small | global pool #30; fetched, not extracted |

## Not used

| Company | Reason |
|---|---|
| The Pensions Regulator | invalid in the global run (rule 6, a training deck) |
| University of Wales Trinity Saint David | 405, no Wayback capture |
| NHS Midlands and Lancashire CSU | rule 6: a services page about RoPAs, no record |
| Edge Hill, Eastleigh, Gloucestershire, Hackleton, Orton, Reedham, Alton | blocked in the global run; not retried, saturation came first |
| St Antony's College, Oxford | not fetched; saturation came first |

Groups: the Oxford colleges (s02, s20, s41, s42, s46) are one group by the owner's ruling;
the Friends of the Angus (s09) stays a separate sample.

# ropa, `uk` block: build record

Built 2026-10-27 as a region run (`build/build.md` *Region run*, `block`). Output:
`plugins/fatodono-founderkit/skills/legals/regions/uk/ropa.md`; new keys `facts.uk.ico_registration`,
`facts.uk.legitimate_interests`, `facts.uk.special_conditions`, `facts.uk.appropriate_policy`
in `regions/uk/facts.md`. Pool: `candidates.md`; raw rows: `pool/r10-uk-extra.md` plus the
global `research/ropa/pool/r10-uk-public.md`. Merge and saturation: `merge.md`.

## Run

- **Start:** the global RoPA pool's 17 UK samples (`research/ropa/merge.md` *Regional
  content*), re-read from their tables for UK-law content (cells marked `[law: ...]`). Their
  tables were made under `research/ropa/extract-notes.md`, which asked for exactly that mark,
  so no global sample was re-fetched.
- **Routes run:** R10 (UK universities, Oxford colleges, councils, fire service, NHS register,
  academy trusts), the global pool's reserve rows, R11 (the ICO model, already in the global
  pool; one per regulator). R4 for companies was not re-run: the global run's company searches
  found none, and the UK has no different route.
- **Collection and extraction:** by the item builder directly. This session had no subagent
  tool, so neither `pool-collector` nor `sample-extractor` ran; tables follow the same format and
  notes.
- **First batch:** 14 (5 large, 3 mid, 5 small, the ICO model), after the Oxford ruling below.
- **Saturation:** s43 new (`uk-law-enforcement`); s21, s45, s27, s48, s44 not new.
- **Stop reason:** saturated at s44. s49 and s47 were in the same batch and are kept
  (`sample_count: 22`). Caister was fetched and not extracted.
- **Size mix:** large 9, mid 3, small 9, standard form 1. Mid is short: the only other mid
  UK records found are Oxford colleges.
- **Oxford ruling (2026-10-27, owner):** the five Oxford colleges (s02, s20, s41, s42, s46)
  count as one sample under `build/sources.md` rule 5. s02, first in pool order, stays; s20,
  s41, s42 and s46 are dropped, their tables kept as records. s09 (a Regent's Park College
  charity) was not part of the ruling and stays. The first build had counted all five
  (26 samples, saturated at s27); prevalence and saturation were recounted (`merge.md`).
- **Shape:** reshaped to PLAN decision 37: the block is "UK:" columns added to the root grid
  and "UK:" lines in the controller block, not a separate section.

## Samples

Global ids keep their tables in `research/ropa/samples/` (URLs and fetch dates in
`research/ropa/README.md`).

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Herefordshire and Worcestershire Health and Care NHS Trust | global | public-sector | large | en | 2026-10-26 |
| s02 | Christ Church, Oxford | global | public-sector | mid | en | 2026-10-26 |
| s03 | Little Smeaton Parish Council | global | public-sector | small | en | 2026-10-26 |
| s05 | Leeds Arts University | global | public-sector | mid | en | 2026-10-26 |
| s06 | Bexhill-on-Sea Town Council | global | public-sector | small | en | 2026-10-26 |
| s07 | University of Manchester | global | public-sector | large | en | 2026-10-26 |
| s09 | Friends of the Angus | global | education | small | en | 2026-10-26 |
| s13 | London Borough of Haringey | global | public-sector | large | en | 2026-10-26 |
| s14 | MLA College | global | public-sector | mid | en | 2026-10-26 |
| s15 | Acton Burnell, Frodesley, Pitchford, Ruckley & Langley Parish Council | global | public-sector | small | en | 2026-10-26 |
| s18 | Horsforth Town Council | global | public-sector | small | en | 2026-10-26 |
| s20 | Jesus College, Oxford (dropped: Oxford group) | global | public-sector | mid | en | 2026-10-26 |
| s21 | Badgeworth Parish Council | global | public-sector | small | en | 2026-10-26 |
| s25 | University of Worcester | global | public-sector | large | en | 2026-10-26 |
| s27 | Peasenhall Parish Council | global | public-sector | small | en | 2026-10-26 |
| s28 | Oldham Council | global | public-sector | large | en | 2026-10-26 |
| s31 | ICO controller documentation template | global | standard-form | none | en | 2026-10-26 |
| s41 | Brasenose College, Oxford (dropped: Oxford group) | https://www.bnc.ox.ac.uk/policies/gdpr-ropa-employees-fellows-not-employed-senior-common-room-members-academic-visitors/ | public-sector | mid | en | 2026-10-27 |
| s42 | St John's College, Oxford (dropped: Oxford group) | https://www.sjc.ox.ac.uk/documents/2132/Archives-2023-ROPA.pdf | public-sector | mid | en | 2026-10-27 |
| s43 | London Fire Brigade | https://www.london-fire.gov.uk/media/stfbh4fo/ropa.pdf | public-sector | large | en | 2026-10-27 |
| s44 | Bracebridge Heath Parish Council | https://bracebridge-heath.parish.lincolnshire.gov.uk/downloads/file/98/data-map | public-sector | small | en | 2026-10-27 |
| s45 | Epping Forest District Council | https://www.eppingforestdc.gov.uk/app/uploads/2023/11/RoPA-Master-Copy-08-11-21.xlsx | public-sector | large | en | 2026-10-27 |
| s46 | All Souls College, Oxford (dropped: Oxford group) | https://www.asc.ox.ac.uk/sites/default/files/2026-06/ASC_ROPA_Current_Staff_and_Fellows.pdf | public-sector | mid | en | 2026-10-27 |
| s47 | Ramsbury & Axford Parish Council | https://ramsbury.org.uk/Media/5.Data%20Audit%20July%202026.pdf | public-sector | small | en | 2026-10-27 |
| s48 | NHS England (NHS Digital GDPR register) | http://web.archive.org/web/20250401081112/https://digital.nhs.uk/data-and-information/keeping-data-safe-and-benefitting-the-public/gdpr/gdpr-register | public-sector | large | en | 2026-10-27 |
| s49 | Derbyshire County Council | https://www.derbyshire.gov.uk/site-elements/documents/xlsx/working-for-us/information-audit-register-extract.xlsx | public-sector | large | en | 2026-10-27 |

## Invalid, copies and groups

- Dropped under rule 5 (Oxford colleges, one group): s20, s41, s42, s46; s02 represents the
  group. Their rows stay in the table above for the record.

- NHS Midlands and Lancashire CSU: rule 6, a page selling RoPA services, no record.
- UWTSD: unreachable (405), no Wayback capture.
- Copies (rule 4): none. s45 fills the ICO template (s31) with its own content; the Oxford
  colleges share a column set; Ramsbury and Caister share a parish template's opening, not
  their rows.

## Shortfalls

- **No companies.** As in the global run, every sized sample is a public body, college or
  charity. The block therefore counts how UK public bodies write UK content. The ids a startup
  needs most (`uk-representative`, `uk-transfers`, `uk-processor-record`) are rare here because
  public bodies are UK-established, keep data in the UK and rarely act as processors; their
  low prevalence says little about a startup's record, which is why each is gated by a fact,
  not by its tier.
- **Mid third is 3 samples** (s02, s05, s14): the other mid records found were Oxford
  colleges, one group.
- **No record names the IDTA, the UK Addendum or recognised legitimate interests.** The
  records predate or ignore them; the block notes them under *Commonly omitted*, not as
  patterns.

## Lessons

- Re-reading global tables worked because the global extract notes asked for a `[law: ...]`
  mark on every law-driven cell. A root item that expects region blocks should always carry
  that rule; without it, every UK sample would have needed a re-fetch.
- A region block's ids are much fewer than the root's (12 against 35), so saturation came after
  6 judged samples (also after the Oxford recount). For blocks, "5 non-new in a row" is cheap; the cost is in the pool.
- "Prevalence" mixes two things for a law-driven block: how often a field appears, and how
  often it applies to the body that wrote it. A representative field is kept and left empty by
  every UK body; that is 3/22 present but 0/22 filled. The block records both in its patterns;
  `skeleton-format.md` has no slot for "present but empty".
- Wayback's CDX index (`web.archive.org/cdx/search/cdx?url=<prefix>/*`) found archived pages of a
  register whose live site blocks fetching (s48), where `wayback/available` per URL found none.
- Groups need checking when a body type repeats in a pool: five Oxford colleges reached the
  first build as separate charities; the owner's ruling treats them as one group. A pool that
  rotates body type should cap any one university's colleges at one row before extraction.

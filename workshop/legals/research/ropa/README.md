# ropa: build record

Built 2026-10-26 (Phase 2 pilot of the alternative sources, `sources.md` *Few public samples*).
Skeleton: `plugins/fatodono-founderkit/skills/legals/skeletons/ropa.md`. Item 18 of the seed catalog, family
`internal-compliance`. New fact keys: `proposed-facts.md`. Item-specific extraction rules:
`extract-notes.md`.

## Run

- **Routes run:** R10 (EU institutions' Art. 31 registers; UK universities, colleges, councils,
  NHS, town and parish councils; Irish and Dutch bodies), R11 (regulator models: ICO, CNIL, JOIC, PDPC, AITI found in English; Belgium,
  Bavaria, Lithuania and Brazil only in other languages; Guernsey's link dead; none found for
  Ireland, Malta, Gibraltar, Isle of Man), plus R4 and R12 for companies (no company publishes
  its own record; `pool/r4-private.md` lists the searches). Raw rows: `pool/` (5 slices, 65
  rows). Selection: `candidates.md` (30 sized rows, 22 reserve rows, 5 standard forms).
- **Collection:** done by the item builder directly; the pool-collector dispatches hit the
  shared concurrent-subagent limit. Extraction mixed builder and `sample-extractor` work: the
  builder extracted s01–s11, s15, s18, s20, s24, s31, s32 and s34 itself for the same reason,
  then followed the coordinator's 3-at-a-time limit for the rest.
- **First batch:** s01–s15 (5 large, 5 mid, 5 small) and the 5 standard forms s31–s35, all
  valid.
- **Saturation:** batches s16–s21 and s22–s28, judged in pool order (`merge.md`). Invalid:
  s16, s19, s22. New: s18, s23. Not new: s24, s25, s26, s27, s28 (5 in a row).
- **Stop reason:** saturated after s28. `sample_count: 30`. s29, s30 and the reserve were not
  needed.
- **Size mix:** large 7, mid 9, small 9, standard forms 5 (one in six, under the one-in-four
  cap). Large is short because the three invalid samples were all large; the reserve held
  more large rows but saturation came first.
- **Merged section list:** `merge.md` (all 30 samples).

## Invalid

| Sample | Company | Rule | Reason |
|---|---|---|---|
| s16 | The Pensions Regulator | 6 | the FOI file is a staff training deck about RoPAs, not a record |
| s19 | University of Groningen | 3 | the English page wraps a Dutch-only register (PrivacyPerfect) |
| s22 | Court of Justice of the European Union | 3 | English register page, records in French |

## Templates

No two samples share the whole text, so rule 4 removed nothing. Shared layouts with their
own content, kept as samples: the ICO controller template filled in by s05 and s07 (the model
itself is s31); the Oxford colleges' column set in s02, s09 and s20 (s20's first row is word for
word s02's); the Art. 31 record form family across the eight EU bodies; a parish "data audit"
heading set noted in `pool/r10-uk-public.md` (Caister, Ramsbury; neither was extracted).

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Herefordshire and Worcestershire Health and Care NHS Trust | https://www.hacw.nhs.uk/download.cfm?doc=docm93jijm4n4153.pdf&ver=7504 | public-sector | large | en | 2026-10-26 |
| s02 | Christ Church, Oxford | https://chch.ox.ac.uk/sites/default/files/2025-03/230623-ROPA-student-data-for-publication_0.xlsx | public-sector | mid | en | 2026-10-26 |
| s03 | Little Smeaton Parish Council | https://littlesmeatonparishcouncil.gov.uk/assets/Policies-and-Procedures/LSPC-Record-of-Processing-Activities-under-GDPR.pdf | public-sector | small | en | 2026-10-26 |
| s04 | European Medicines Agency | https://www.ema.europa.eu/en/about-us/data-protection-privacy-ema/central-register-data-processing-records | public-sector | large | en | 2026-10-26 |
| s05 | Leeds Arts University | https://www.leeds-art.ac.uk/about-us/legal-and-governance-at-leeds-arts-university/record-of-processing-activities | public-sector | mid | en | 2026-10-26 |
| s06 | Bexhill-on-Sea Town Council | https://www.bexhilltowncouncil.gov.uk/wp-content/uploads/2026/05/Data-Audit-August-2025.pdf | public-sector | small | en | 2026-10-26 |
| s07 | University of Manchester | https://www.manchester.ac.uk/about/privacy-information/data-protection/processing-activities/ | public-sector | large | en | 2026-10-26 |
| s08 | EU Agency for Fundamental Rights | https://web.archive.org/web/20261011174431/https://fra.europa.eu/en/about-fra/data-protection/records-registry | public-sector | mid | en | 2026-10-26 |
| s09 | Friends of the Angus (Regent's Park College, Oxford) | https://www.rpc.ox.ac.uk/wp-content/uploads/2025/02/ROPA-Friends-of-the-Angus-2.pdf | education | small | en | 2026-10-26 |
| s10 | Wexford County Council | https://www.wexfordcoco.ie/sites/default/files/content/FOIs/FOI%2016%2025%20Combined.pdf | public-sector | large | en | 2026-10-26 |
| s11 | European Environment Agency | https://www.eea.europa.eu/en/about/working-practices/central-register-of-records-of-processing-activities/ | public-sector | mid | en | 2026-10-26 |
| s12 | Community Plant Variety Office | https://cpvo.europa.eu/sites/default/files/documents/cpvo_register_records_data_protection_2021-04_final.pdf | public-sector | small | en | 2026-10-26 |
| s13 | London Borough of Haringey | https://haringey.gov.uk/council-elections/data-finance/information-data-requests/data-protection-privacy/haringey-councils-record-processing-activities-ropa | public-sector | large | en | 2026-10-26 |
| s14 | MLA College | https://www.mla.ac.uk/app/uploads/secure/2026/01/11.01-ROPA-MLA-College-2026.pdf | public-sector | mid | en | 2026-10-26 |
| s15 | Acton Burnell, Frodesley, Pitchford, Ruckley & Langley Parish Council | https://www.actonburnell-pc.gov.uk/sites/default/files/data_processing_log_public_ro_2026.pdf | public-sector | small | en | 2026-10-26 |
| s17 | European Data Protection Board | https://www.edpb.europa.eu/edpb-centralised-register-of-records_en | public-sector | mid | en | 2026-10-26 |
| s18 | Horsforth Town Council | https://www.horsforthtowncouncil.gov.uk/_UserFiles/Files/Data%20Audit%202025.pdf | public-sector | small | en | 2026-10-26 |
| s20 | Jesus College, Oxford | https://www.jesus.ox.ac.uk/wp-content/uploads/2022/01/ROPA-Applicants-and-Prospective-Students-25-5-18-1.pdf | public-sector | mid | en | 2026-10-26 |
| s21 | Badgeworth Parish Council | https://badgeworthparishcouncil.gov.uk/wp-content/uploads/2024/12/Information-audit-retention-period-2018.pdf | public-sector | small | en | 2026-10-26 |
| s23 | European Labour Authority | https://www.ela.europa.eu/en/privacy-policy | public-sector | mid | en | 2026-10-26 |
| s24 | EU Institute for Security Studies | https://www.iss.europa.eu/data-protection-records-register | public-sector | small | en | 2026-10-26 |
| s25 | University of Worcester | https://informationassurance.wp.worc.ac.uk/wp-content/uploads/2021/10/Employee_record_of_processing_Master.pdf | public-sector | large | en | 2026-10-26 |
| s26 | European Union Agency for Cybersecurity (ENISA) | https://www.enisa.europa.eu/about-enisa/data-protection/enisa2019s-central-register-of-data-processing-activities | public-sector | mid | en | 2026-10-26 |
| s27 | Peasenhall Parish Council | https://peasenhallparishcouncil.gov.uk/assets/GDPR-Personal-Data-Audit-2023.pdf | public-sector | small | en | 2026-10-26 |
| s28 | Oldham Council | https://www.oldham.gov.uk/downloads/download/1390/ropa_records_of_processing_activities | public-sector | large | en | 2026-10-26 |
| s31 | Information Commissioner's Office (ICO), controller documentation template | https://ico.org.uk/media2/migrated/2172937/gdpr-documentation-controller-template.xlsx | standard-form | none | en | 2026-10-26 |
| s32 | CNIL, simplified record of processing (official English version) | https://www.cnil.fr/sites/default/files/2024-01/record-processing-activities.ods | standard-form | none | en | 2026-10-26 |
| s33 | Personal Data Protection Commission Singapore (PDPC), DPMP guide Annex C | https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/dpmp/guide-to-developing-a-data-protection-management-programme-(aug-2023).pdf | standard-form | none | en | 2026-10-26 |
| s34 | Jersey Office of the Information Commissioner (JOIC) | https://jerseyoic.org/media/guidance-downloads/template-record-of-processing-activity.docx | standard-form | none | en | 2026-10-26 |
| s35 | Authority for Info-communications Technology Industry of Brunei Darussalam (AITI) | https://pdp.aiti.gov.bn/media/jccpm0dx/aiti-pdp-essentials-infokit-jan-2026.pdf | standard-form | none | en | 2026-10-26 |

## Shortfalls

- **No companies.** Every sized sample is a public body or a charity. Companies keep the record
  internally (the law asks them to show it to the regulator on request, not to publish it), and
  the company searches in `pool/r4-private.md` found none. The sector cap ("no sector above a
  quarter") could not hold; the pool rotated body type instead (EU body, university or college,
  council, NHS, parish).
- **Size means little here.** "Small" is mostly parish councils (one clerk, 7–40 rows); "large"
  is councils, universities and EU agencies with hundreds of activities.
- **Large third short** (7 of 10): the three invalid samples were all large.
- **Published copies are often summaries.** 5 samples say they are the public part or a
  summary of a fuller internal record; their columns are fewer than a full record's.

## Lessons

**The main question: can the root be region-neutral? Yes, with one condition.**

- The fields are the same everywhere the record is required. Five regimes are in the samples
  (UK GDPR, EU GDPR in Ireland, the EU institutions' Reg. 2018/1725, Jersey, plus Singapore's
  and Brunei's regulator models), and the law-derived notes cover KVKK. Every one of them asks
  for the same core: activity, purpose, data subjects, data categories, recipients, transfers
  abroad, retention, security, controller contact. KVKK's processing inventory adds legal
  ground and maximum retention, both already root sections here. Even the two non-GDPR models,
  which call it a "data inventory map" and order it by life-cycle stage, hold the same facts.
  18 of the 21 root sections are core or common, and none needs a law's wording.
- What differs is vocabulary and a few add-on columns: the names of the legal grounds, the
  conditions for sensitive data (UK Schedule 1, KVKK Art. 6), transfer safeguards, the
  appropriate policy document, an ICO or VERBİS registration number, a separate processor
  record (GDPR Art. 30(2), none under KVKK), and the link to a retention and destruction policy
  (KVKK). Those are exactly what a `block` holds; `merge.md` *Regional content* lists them.
- The condition: the document only exists because a law requires it. The root cannot say when
  it is needed (that depends on the law: GDPR's 250-employee exemption with its exceptions,
  KVKK's VERBİS thresholds, no duty at all in most US states), and a root rule may not name a
  region. So the item's *trigger* must come from the regions: the catalog row should fire when
  any region in `facts.users.regions` has a `ropa` block (or a region fact like "record
  required"), not from a root question. Recommendation: keep `ropa` as a root item with
  region blocks, not a region item; build `eu`, `uk` and `tr` blocks next (`tr` from VERBİS
  summaries, per `regions/tr/region.md`). Making it a region item would mean near-copies of
  the same fields in every region.
- Writing the skeleton as "document level + per-activity fields" worked; the write branch will
  need to output a grid (one row per activity), not prose. `skeleton-format.md` assumes a
  prose document; a short note there on grid-shaped documents (the `activity` section as the
  row unit) would help the writer.

**Method problems found (rules not changed):**

- *Few public samples* expects ≥20 from R10/R11 and got 30, but the pool is all public sector,
  so the skeleton describes how public bodies publish their records. The regulator models
  (s31–s35) are the closest thing to what a startup would keep; the one-in-four cap kept them
  to a sixth of the samples. For internal documents a higher cap, or weighting the models,
  would fit the user better.
- Rule 3 failed twice on EU registers whose page is English but whose records are not (s19
  Dutch, s22 French). The pool collector should open one record, not just the register page.
- A sample made of many files (a register of one PDF per activity) has no rule in `build.md`.
  `extract-notes.md` fixed it: read the index plus three records (first, staff, core work). The
  same rule will be needed for DPIAs and policy sets.
- The format test (prose / list / table) is weak for a record: nearly every field is a grid
  column (`table`) or a form field (`list`), so after the first batch almost every format was
  already recorded, and the two "new" verdicts came from minor fields (an actions column, a
  storage field in a form). Saturation was quick, but it measures layout more than content.
  For grid documents, a new *field* is the real signal.
- An FOI-release route (R10) brought a training deck (s16). A file named "record of processing"
  is not always one; the collector should check that the file has rows or fields.
- Subagent limits: the shared 20-agent limit stopped every pool-collector dispatch, and a later
  overload capped extractors at three. About half the extraction was done by the builder in
  its own context; tables were checked against the same notes.

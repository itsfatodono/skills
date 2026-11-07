# ropa, `eu` block: build record

Built 2026-10-27 (region run `eu`, `part: block`); recounted the same day with the 8 EUDPR
registers (PLAN.md decisions 35 and 36). Block:
`plugins/fatodono-founderkit/skills/legals/regions/eu/ropa.md`. New fact key:
`facts.eu.processor_customers` in `regions/eu/facts.md`. Merged ids: `merge.md`. Selection:
`candidates.md`.

## Run

- **Routes run:** R10 Irish public bodies and universities, other EU bodies in English
  (`pool/r10-ie-public.md`, `pool/r10-ie-edu-mt-cy.md`, `pool/r10-r11-eu-other.md`, 2026-10-26);
  R11 regulator models across the EDPB's SME pages and 18 national authorities (same slices);
  a builder re-check of Irish universities, professional and sports bodies
  (`pool/r10-r11-builder.md`, 2026-10-27); the global pool's EU rows (`research/ropa/`). All
  routes in `regions/eu/region.md` have run: the pool is exhausted.
- **Collection and extraction:** done by the item builder directly. This session had no
  subagent tool, so no `pool-collector` or `sample-extractor` was dispatched. s01 and s02
  re-read the global tables (global s10 and s32) for EU content; s03–s07 were fetched and
  read in full (s06's model pages are images and were rendered to read them).
- **EUDPR recount:** s08–s15 are the 8 EU institutions' registers already extracted in the
  global pool (global s04 s08 s11 s12 s17 s23 s24 s26), re-read from their tables for the `eu`
  ids and tagged `law: EUDPR`. They count by meaning; no wording or article number is taken
  from them (decision 36).
- **First batch:** all 15 candidates, all valid. No saturation batch was possible.
- **Stop reason:** pool exhausted at exactly one first batch of 15. `saturated: false`.
  Informally, s06–s15 added no new id (10 in a row), and the EUDPR samples added none at all
  (`merge.md` *Saturation*).

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Wexford County Council (global s10) | https://www.wexfordcoco.ie/sites/default/files/content/FOIs/FOI%2016%2025%20Combined.pdf | public-sector | large | en | 2026-10-26 |
| s02 | CNIL, simplified record (global s32) | https://www.cnil.fr/sites/default/files/2024-01/record-processing-activities.ods | standard-form | none | en | 2026-10-26 |
| s03 | Maynooth University, high-level RoPA | https://www.maynoothuniversity.ie/sites/default/files/assets/document/MU%20ROPA%200926%20.docx | public-sector | large | en | 2026-10-27 |
| s04 | Data Protection Ombudsman (Finland), controller template | https://web.archive.org/web/2024id_/https://tietosuoja.fi/documents/6927448/8323207/Template+for+controllers+-+record+of+processing+activities.xlsx/696390cb-00ae-4780-884a-668d0f8dd655?t=1654165400828 | standard-form | none | en | 2026-10-27 |
| s05 | Commissioner for Personal Data Protection (Cyprus), template | https://web.archive.org/web/2024id_/https://www.dataprotection.gov.cy/dataprotection/dataprotection.nsf/ED1AAB60C3F3A93BC22582600037E15D/$file/Record%20of%20Activities%20Template%20ENG.xlsx | standard-form | none | en | 2026-10-27 |
| s06 | Data Protection Commission (Ireland), guidance layouts | https://www.dataprotection.ie/sites/default/files/uploads/2023-04/Records%20of%20Processing%20Activities%20(RoPA)%20under%20Article%2030%20GDPR.pdf | standard-form | none | en | 2026-10-27 |
| s07 | GAA, sample club record | https://www.gaa.ie/api/pdfs/image/upload/m0calrgs8dbwlllvob7p.pdf | standard-form | none | en | 2026-10-27 |
| s08 | European Medicines Agency (global s04), EUDPR | https://www.ema.europa.eu/en/about-us/data-protection-privacy-ema/central-register-data-processing-records | public-sector | large | en | 2026-10-26 |
| s09 | EU Agency for Fundamental Rights (global s08), EUDPR | https://web.archive.org/web/20261011174431/https://fra.europa.eu/en/about-fra/data-protection/records-registry | public-sector | mid | en | 2026-10-26 |
| s10 | European Environment Agency (global s11), EUDPR | https://www.eea.europa.eu/en/about/working-practices/central-register-of-records-of-processing-activities/ | public-sector | mid | en | 2026-10-26 |
| s11 | Community Plant Variety Office (global s12), EUDPR | https://cpvo.europa.eu/sites/default/files/documents/cpvo_register_records_data_protection_2021-04_final.pdf | public-sector | small | en | 2026-10-26 |
| s12 | European Data Protection Board (global s17), EUDPR | https://www.edpb.europa.eu/edpb-centralised-register-of-records_en | public-sector | mid | en | 2026-10-26 |
| s13 | European Labour Authority (global s23), EUDPR | https://www.ela.europa.eu/en/privacy-policy | public-sector | mid | en | 2026-10-26 |
| s14 | EU Institute for Security Studies (global s24), EUDPR | https://www.iss.europa.eu/data-protection-records-register | public-sector | small | en | 2026-10-26 |
| s15 | ENISA (global s26), EUDPR | https://www.enisa.europa.eu/about-enisa/data-protection/enisa2019s-central-register-of-data-processing-activities | public-sector | mid | en | 2026-10-26 |

By source type: 2 GDPR public-body records and 8 EUDPR registers (R10), 4 regulator models
(R11), 1 association model. No company record. No copies under rule 4. Sizes of the 10 full
samples: large 3, mid 5, small 2.

## Shortfalls

- **15 samples, only 2 of them GDPR records.** EU bodies under the GDPR rarely publish their
  record, and those that do mostly publish in their own language (rule 3 removed the Dutch,
  Spanish, Lithuanian, Croatian, Danish, German and Belgian ones). Ireland is the only
  English-language member state with full records online, and only through a university page
  and an FOI release.
- **Standard forms:** 5 of 15, inside the half cap once the EUDPR registers count. Before
  them they were 5 of 7; decision 35 now allows that for internal documents.
- **Public sector only.** Every real record is a public body; the EUDPR registers are EU
  agencies, which never need an Art. 27 representative or a processor record. That is why
  `eu-processor-record` fell to rare (4/15) and the representative field stays at 4/15:
  those counts come from the GDPR models alone.

## Owner decisions

1. Models above the half cap: decided, PLAN.md decision 35 (`build/sources.md` exception).
2. EUDPR registers: decided, decision 36; counted as s08–s15.
3. Placement: decided, decision 37 (region blocks as extra columns in tabular documents), to
   be applied with the `uk` block. Until then the block still tells the writer to write a
   table keyed by activity reference under the regional part.

## Lessons

- A university's data-protection page linked a current, filled record that the R10 slices
  missed: they searched for the phrase and the file, not the universities' data-protection
  menus. Region routes for records should walk each university's data-protection pages.
- A regulator's guidance note can hold its model as images (DPC). Extracting them needs a
  page render, not text extraction; a collector that reads only text will rate it "guidance".
- Regulator models that keep strictly to Art. 30's list (CNIL, Finland) leave out the legal
  basis, while the DPC calls it recommended. A block's prevalence on extras depends on which
  models are in the pool, a reason to keep models to their cap when real records exist.
- The run had no subagent tool. The method should say what a builder does then (do the
  steps itself and record it), as this README does.

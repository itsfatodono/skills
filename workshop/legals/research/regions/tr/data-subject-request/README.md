# data-subject-request, `tr` block: build record

Built 2026-10-27 (region run `tr`, `part: block` of the root item; PLAN.md item 13, decisions 45,
47, 49, 50). Block: `plugins/fatodono-founderkit/skills/legals/regions/tr/data-subject-request.md`. Root
skeleton and id list: `skeletons/data-subject-request.md`, `research/data-subject-request/merge.md`
(build `2f9af25`). Source row added to `regions/tr/region.md` *Documents*; no `catalog.md` row,
since the item is in the root catalog.

## Files

- `candidates.md`: 24 pool rows and 7 reserve rows from the shared KVKK pool's *Başvuru formu URL*
  column, with template families T1–T4, groups and first-screen drops.
- `../kvkk-pool/pool/`: the shared pool's raw rows (decision 45).
- `samples/sNN.md`: one extraction table per sample, s01–s15.
- `raw/`: stripped texts (git-ignored, never committed or shipped).
- `merge.md`: how `tr` content maps to the root ids, the one `tr` id, mapping notes, section map,
  merged list, shared wording, patterns, *Avoid* table with sources, document level, facts,
  qualification, saturation.

## Run

- **Routes run:** KAP, İSO 500 and Fortune Türkiye 500 → R4; R1 and R2 with `cc=tr` (the shared
  pool's `tr-large`, `tr-apps` and `tr-tail` slices). 40 rows with a form URL, 39 companies.
- **Pool:** 24 candidates (10 large, 8 mid, 6 small) and 7 large reserve. Mid ran 2 short and small
  4 short: most mid and small companies in the shared pool link no form. 6 dropped at the first
  screen (3 sign-up forms, 1 another company's form, 1 wrong company, 1 group rule). Decision 46's
  cut-off does not apply (KVKK Arts. 11 and 13 were not amended).
- **First batch:** s01–s15 = candidates 1–15, 5 per size. All valid; none replaced.
- **Saturation:** none. The owner closed the pool after the first batch (no more extraction or
  collection).
- **Stop reason:** `saturated: false`, `sample_count: 15`. The method stops only after 5 samples in
  a row add no id in saturation batches; no batch was run, so the rule could not be met. Inside the
  batch only s06 added an id (`tr-complaint`), but first-batch samples are not judged under the stop
  rule.

## Invalid

None. Borderline but valid (`merge.md` *First-batch qualification*): s04 a page plus its PDF; s08
an image-only PDF read by OCR, section C restored by hand; s09 an HTML page with the same text as
its .docx; s11 a form whose text names neither the company nor its address; s12 a page whose
business petition copies the user petition, read once.

## Templates and copies

Rule 4: no copies. On 6-word shingles the highest pair is s02/s03 at 0.37 (T2); every other pair
is under 0.25. Shared wording counts once in patterns (decision 39): B1 the T2 field and
declaration block (s01 s02 s03), B2 the ID-copy and disclaimer paragraph (s02 s04 s05 s07 s08 s10
s11), B3 the Art. 13(1) opening (s05 s07 s11 s13), B4 the 30-days-from-receipt line (s02 s05 s08 s11
s13), B5 the automated-decision objection (s09 s12 s13 s14), and the T3 reply tail (s05 s11, s07).
Families in the batch: T1 s07; T2 s02 s03; T3 s05 s11 (s13 opens alike); T4 none.

## Avoid

Checked against the Başvuru Tebliği (RG 10.03.2018, 30356), KVKK Arts. 4, 11, 13, 14, Board
decision 2019/296, the Board's announcement of 1 October 2026 on oral replies, and the sources
`tr-explicit-consent` used for consent. Four *Avoid* lines: paper-only channels (3/15), required
phone, fax or e-mail (3/15), a phone call as the answer (2/15), consent for the application's data
(3/15). No fee pattern is wrong. Patterns looked at and not marked are listed in `merge.md`.

## Size thirds

Valid samples: 5 large, 5 mid, 5 small.

## Samples

All fetched 2026-10-27, language `tr`.

| Sample | Company | URL | Sector | Size | Family |
|---|---|---|---|---|---|
| s01 | Flo Mağazacılık ve Pazarlama A.Ş. | https://floimages.mncdn.com/media/import/pdf/23-10/09/flo_ilgilikisi_basvuruformu_v4.pdf | shopping | large | (B1) |
| s02 | Eczacıbaşı Evital Sağlık Hizmetleri ve Tic. A.Ş. | https://img-evital.mncdn.com/evital/assets/files/Evital_Veri_Basvuru_Formu.pdf | health-fitness | mid | T2 |
| s03 | Fırsat Yapay Zeka Teknolojileri A.Ş. | https://firsat.com/ilgili-kisi-basvuru-formu | shopping | small | T2 |
| s04 | ING Bank A.Ş. | https://www.ing.com.tr/tr/ing/kisisel-verilerin-korunmasi/ilgili-kisi-basvuru-formu (+ https://www.ing.com.tr/F/Documents/pdf/Hakkimizda/Site_Basvuru_Formu_060722_.pdf) | finance | large | |
| s05 | Multinet Kurumsal Hizmetler A.Ş. | https://multinet.com.tr/sites/default/files/static/multinet-kvkk-basvuru-formu_1.pdf | finance | mid | T3 |
| s06 | Mahir Baran Aydoğan (6 Tekrar) | https://6tekrar.com/yasal/ilgili-kisi-basvuru-formu | health-fitness | small | |
| s07 | Shaya Kahve San. ve Tic. A.Ş. (Starbucks Türkiye) | https://media.sbuxtr.com/files/g7r5gvep/shaya-kahve-ilgili-kisi-basvuru-formu.pdf | food-drink | large | T1 |
| s08 | Honda Türkiye A.Ş. | https://honda.com.tr/assets/files/HondaBasvuruFormu2020.pdf | lifestyle | mid | |
| s09 | This Is A Company Teknoloji Gelişim ve Yatırım A.Ş. (Frink) | https://frink.com.tr/tr/kvkk-basvuru-formu | food-drink | small | |
| s10 | Mars Spor Kulübü ve Tesisleri İşletmeciliği A.Ş. (MACFit) | https://www.macfit.com/wp-content/uploads/2025/04/KVKK-Basvuru-Formu.pdf | health-fitness | large | |
| s11 | TürkKEP Kayıtlı Elektronik Posta Hizmetleri A.Ş. | https://turkkep.com.tr/wp-content/uploads/2020/12/FRM-058-Veri-Sahibi-Basvuru-Formu.pdf | productivity | mid | T3 |
| s12 | Ekin Hazal Altıparmak (Look Bubble Teknoloji) | https://lookbubble.com/kvkk-basvuru-formu/ | lifestyle | small | |
| s13 | Ets Ersoy Turistik Servisleri A.Ş. | https://images.etstur.com/files/images/site/images/politikalar/kvkk-basvuru-formu.pdf | travel | large | (T3 opening) |
| s14 | Gedik Yatırım Menkul Değerler A.Ş. | https://cdn.gedik.com/media/media/vxahm3i2/kvkk-verisahibibasvuruformu.pdf | finance | mid | |
| s15 | Ortakmarket Reklam Pazarlama ve Tic. Ltd. Şti. | https://ortakmarket.com/kvkk-basvuru-formu | business | small | |

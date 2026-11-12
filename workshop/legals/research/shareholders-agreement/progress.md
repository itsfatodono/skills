# shareholders-agreement: progress

Run started 2026-11-12. Pre-built run (no sector, no region). Builder: the main agent of the
shareholders-agreement run; workers: `pool-collector` (Sonnet, medium), `sample-extractor` (Opus,
high), at most 3 running at once.

## Done

- Read method files; checked routes by hand (EDGAR full-text search, exhibit fetch, NVCA with a
  browser User-Agent; UK Private Capital models behind a member login).
- `extract-notes.md`: scope, EDGAR recipe, row granularity, footnotes in Word models.
- Pool slices: `r8-founders` 2 rows, `r8-shareholders` 60, `r8-voting` 27, `r8-buysell` 27,
  `r9-models` 23 rows (12 projects).
- `candidates.md`: standard forms f1–f8 (s31–s38), pool c01–c30 (10/10/10), reserve, dropped list.
- Extracted: s01 invalid (starts at IPO), s02–s08 ok, s31 ok, s32 ok. s09, s10, s11 dispatched.
- `section-map.md` holds s02–s08, s31, s32; `merge.md` holds the draft section ids (39).
- 2026-11-12 ~14:20: usage limit stopped extractors s06, s07, s08 (raw text saved, no table);
  resumed after the reset.

- Extracted and mapped: s02–s16, s31–s33 (s01 invalid). Dispatched: s34, s35, s17.
- Counting script: `/tmp/fa-scripts/count.py` (outside the repo; reads `section-map.md` and
  the tables). If lost, rewrite: per id, count samples, median of first-row/rows, formats.

- First batch done (s02–s16 + s31–s35), mapped, merged list in `merge.md`. Saturation log
  started: s17 not new (1 in a row). Running: s18, s19, s20.

- Saturation: s17–s21 not new, **saturated at s21**. s22–s26 (one batch) kept past the stop
  point; s22, s23 mapped; s24, s25, s26 running.

- All extraction done: 29 valid samples (s02–s23, s25, s26, s31–s35); s01, s24 invalid.
- `merge.md` complete (folds, merged list, document level, regional content, copies).
- Facts: appended *Ownership keys* (7 keys) to `helpers/facts-schema.md`; reused sibling keys
  (entity_form, contract_law, signatory, founders, founder_prior_work, business_scope,
  staff_restrictions, staff_locations).

- Skeleton written (31 sections, valid per `formats/skeleton-format.md`); README.md written.
- Checks: `tools/check-facts` exit 0; `npm run check` and `claude plugin validate . --strict` pass.

## Next

Done. Owner review items are in `README.md` *For the owner's review*.

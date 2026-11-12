# ip-assignment: progress

Run started 2026-11-12. Pre-built run (no sector, no region). Method: `build/build.md` steps 1–7.

## Done
- Read method, formats, helpers, model build (terms-of-service).
- Tested R8: `efts.sec.gov/LATEST/search-index` works with `q`, `forms`, `startdt`, `enddt`, `sics`, `from`.
  Many hits are offer letters that only mention the agreement; collectors check each exhibit's title.
- R9 run: Cooley GO CIIAA (`cooleygo.com/documents/form-employee-confidential-information-inventions-assignment-agreement/`)
  is a ContractExpress generator at `docs.cooleygo.com` behind a Cloudflare bot wall (403); no Wayback
  capture of any output or docx. Recorded in `pool/r9-forms.md`.

- Collect: r8-founder (30 rows, all small, standalone founder/individual assignments), r8-tech (46 rows,
  mostly large/mid, most attached to offer letters: rule 6), r8-small-tail (10 rows), r8-other (50 rows, many industries; pharma and tech screened out).
  Collector note: `sics=` with a comma list and `forms=` with a comma list are unreliable; r8-tech
  queried one form at a time and filtered SIC on each hit.

- Select: `candidates.md` written (c01–c30, 10/10/10, 6 founder forms in small third, reserve by size).
  Title check done for all 30 (texts in /tmp/ipa-sel/txt, not kept). `extract-notes.md` written.

## Next
- Step 2 First batch DONE: s01–s15 all valid (c01–c15). No copies (max 6-gram containment 0.36, s07–s08).
- First-batch merge DONE: 26 ids in `merge.md`; row map in `section-map.md` (tool scripts in /tmp/ipa-tools; rebuild
  map.tsv from section-map.md with map_from_md.py if lost).

- Step 3 Saturation: batches of 5 in pool order (s16–s20 = c16–c20 ...). Dispatched: s16–s20. Judged: s16 not new, s17 not new, s18 NEW (closing), s19 not new, s20 not new (2 non-new in a row after s18), s21 not new (3), s22 not new (4), s23 not new (5) => SATURATED at s23. s24 s25 already dispatched: kept past the stop point. No further extraction. Judge one at a
  time in pool order, log in merge.md. Stop at 5 non-new in a row.

- Step 4 Merge DONE: merge.md has merged list (25), folds, section notes, document level, regional content, copies.
- Step 5 facts DONE (6 keys appended under Team keys). Step 6 skeleton DONE (24 sections, valid). Step 7 README DONE.
  check-facts exit 0. Run complete.

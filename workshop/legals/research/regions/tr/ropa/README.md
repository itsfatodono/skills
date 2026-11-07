# ropa, `tr` block: build record

Attempted 2026-10-26 (region run `tr`, `part: block`). **Won't build:** no public samples.
No `regions/tr/ropa.md` is written, so the RoPA is not triggered for `tr` users.

## Routes run

- **Companies, foundations, private schools and hospitals** (`pool/companies.md`): 18 web
  searches and a curl sweep of 44 company sites. None publishes a filled inventory or a VERBİS
  summary. Hits were retention and destruction policies (item 19), notices, law-firm or
  template-seller pages, and KVKK guides. Not run: `site:` variants, per-company searches, the
  "KVK Envanteri" / "Veri Envanteri" title variants.
- **Public universities** (`pool/edu.md`): about 45 university KVKK sites loaded, the first 80
  same-site links crawled on 28 of them, about 8 web searches. None publishes a filled
  inventory; Bingöl and Marmara keep theirs behind a login.
- **Public bodies and models** (`pool/public-and-models.md`): about 45 municipal, ministry,
  chamber and agency sites crawled. One clean filled model: KVKK Kurumu's guide with a 46-row
  sample inventory (xlsx), a `standard-form`. Borderline: Lüleburgaz Belediyesi's retention
  policy tables (no legal-ground or security columns), Türk Psikiyatri Derneği's Ek-D and
  TTB's guide (guides, not filled grids). One standard form cannot make a block.
- **VERBİS public query** (`verbis.kvkk.gov.tr/sicil-sorgula`): not run. It is
  captcha-gated, takes one controller name per query, and shows only the registration's
  category summary, not the inventory's layout.

## Reopening

A block could come from VERBİS summaries queried by hand (the creator solves the captcha), but
they cover the inventory's categories only. A block written from the law and KVKK's guides
alone would have `sample_count: 0`, outside the build method; decided against (2026-10-26).
`extract-notes.md` holds the extraction rules prepared for this run.

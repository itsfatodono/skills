# ropa, `eu` block: merged section list

Region run: the extractor read only content the EU GDPR (or, for s08–s15, the EUDPR) shapes (`build/build.md` *Region run*).
Formats as in `research/ropa/merge.md`. Root ids (activity, purpose, retention...) are not
recounted here; the root skeleton holds them.

## Section ids

Meanings fixed 2026-10-27, before counting. For an EUDPR sample (s08–s15) each id reads with
the EUDPR's matching article (Art. 31 for Art. 30, Art. 5 for Art. 6, Arts. 10–11 for Arts.
9–10, Chapter V for Chapter V).

| Id | Meaning | Includes |
|---|---|---|
| eu-gdpr-source | the record names the GDPR or Art. 30 as the reason it exists | title, intro line, help tab |
| eu-field-citations | field headings cite the GDPR article they implement | "[Article 30(1)(b)]", "provided for in Article 32" |
| eu-required-marks | the record marks which fields the law requires and which are conditional or extra | colour bands, "(if applicable)", Required / If relevant / If possible / Recommended |
| eu-controller | the Art. 30(1)(a) contact set beyond the controller: DPO (Art. 37) and Art. 27 representative | DPO block, representative block, "capacity" column |
| eu-legal-basis | the basis written as a GDPR Art. 6(1) point, and the law behind it (Art. 6(3)) | "6(1)(b) Contract", "Underlying law", "Legislation" |
| eu-special-categories | Art. 9 special categories and Art. 10 criminal data in the GDPR's terms, and the Art. 9(2) condition | fixed Art. 9/10 rows, condition column |
| eu-transfers | transfers to third countries or international organisations, in Chapter V terms: the EEA as boundary, the safeguard type, Art. 49 documentation | destination and safeguard columns, adequacy flags, no-transfer statement |
| eu-processor-record | the Art. 30(2) record kept when acting as processor, or a role column that makes room for it | separate processor template, controller/processor capacity, guidance on 30(2) |
| eu-processor-agreement | the Art. 28 contract with each processor, per row | "Reference to the processing agreement", "contracts are in place" |
| eu-dpia-consultation | DPIA (Art. 35) and prior consultation (Art. 36) per activity | |
| eu-main-auxiliary | whether the activity is main or auxiliary | |

## Counts

15 samples: s01–s07 under the GDPR, s08–s15 under the EUDPR (Reg. (EU) 2018/1725, tagged
`law: EUDPR`, decision 36). The EUDPR samples count by meaning; no wording comes from them.
No two samples share their whole text (rule 4).

| Id | Count | GDPR (s01–s07) | EUDPR (s08–s15) | Formats | Samples |
|---|---|---|---|---|---|
| eu-controller | 14/15 | 6/7 | 8/8 | list, table | s01 s02 s03 s04 s05 s06 s08 s09 s10 s11 s12 s13 s14 s15 |
| eu-transfers | 14/15 | 6/7 | 8/8 | list, prose, table | s01 s02 s03 s04 s05 s06 s08 s09 s10 s11 s12 s13 s14 s15 |
| eu-gdpr-source | 13/15 | 6/7 | 7/8 | prose, table | s01 s02 s03 s04 s06 s07 s08 s09 s11 s12 s13 s14 s15 |
| eu-legal-basis | 10/15 | 3/7 | 7/8 | embedded, list, table | s01 s05 s06 s08 s09 s11 s12 s13 s14 s15 |
| eu-special-categories | 8/15 | 4/7 | 4/8 | embedded, list, table | s01 s02 s03 s06 s08 s09 s11 s13 |
| eu-required-marks | 7/15 | 3/7 | 4/8 | list, table | s01 s04 s06 s08 s10 s11 s14 |
| eu-field-citations | 6/15 | 2/7 | 4/8 | list, table | s01 s04 s09 s11 s12 s13 |
| eu-processor-agreement | 5/15 | 2/7 | 3/8 | list, table | s04 s07 s09 s13 s15 |
| eu-processor-record | 4/15 | 4/7 | 0/8 | prose, table, pointer | s01 s04 s05 s06 |
| eu-dpia-consultation | 1/15 | 1/7 | 0/8 | table | s05 |
| eu-main-auxiliary | 1/15 | 1/7 | 0/8 | table | s05 |

`eu-information` is dropped as an id (2026-10-27, after the EUDPR samples): how people are
informed is the root's `notice` id, which every EUDPR register carries; s05's column 12 maps
there.

Splits inside the ids:

- eu-controller: DPO 13/15 (all but s05 s07); one shared DPO mailbox or form, the same in every
  record, 9/13 (s01 and the 8 EUDPR); representative field 4/15, all GDPR models (s02 s04 s05
  s06), filled in none; "capacity" column 1/15 (s05).
- eu-legal-basis: its own field 6/10 (s01 s05 s06 s11 s12 s13); inside the purpose 4/10 (s08
  s09 s14 s15). The law behind the basis named 9/10 (all but s05). GDPR wording: point plus
  short name (s06), point quoted in full (s01). Left out by s02 s04 (models that keep to
  Art. 30's list) and s03 s07 s10; typed "Recommended" by s06.
- eu-special-categories: condition named 3/8 (s01 s06 s13); criminal-offence data apart 4/8
  (s02 s03 s09 s13); the categories as a fixed list or checklist 3/8 (s02 s09 s13); flagged
  inside the data field 2/8 (s08 s11).
- eu-transfers: separate destination and safeguard columns 4/14 (s01 s02 s04 s06); one field
  asking where to and with which safeguard 7/14 (s05 s08 s10 s11 s12 s14 s15); yes/no plus a
  checklist of transfer grounds 2/14 (s09 s13); a paragraph for the whole record 1/14 (s03).
  No-transfer statement 8/14 (s01 s04 s06 s10 s11 s12 s14 s15). Safeguards from a fixed
  vocabulary 4/14 (s02 s03 s09 s13). International organisations named 10/14 (s01 s04 s05 s06
  s08 s09 s10 s11 s13 s14). Art. 49(1) documentation 2/14 (s04 s06). Expired mechanism warned
  against 1/14 (s06).
- eu-processor-record: separate template 1/4 (s04); role column 2/4 (s01 s05); guidance 1/4
  (s06). None of the EUDPR registers publishes a processor record.

## Saturation

The pool holds 15 samples, exactly a first batch; there are no further candidates for a
saturation batch, so `saturated: false` (`build/build.md` step 3). Informal check only: in pool
order, the last sample with a new id is s05 (eu-dpia-consultation, eu-main-auxiliary); s06–s15
added none, 10 in a row. The 8 EUDPR samples added no id at all.

## From ids to the block

- Sections: `eu-controller`, `eu-legal-basis`, `eu-special-categories`, `eu-transfers`,
  `eu-processor-record`, in the root's field order.
- Document level: `eu-field-citations`, `eu-required-marks`. `eu-gdpr-source` became the
  `eu-law` section (a header line) when the block was reshaped into columns (decision 37,
  2026-10-27), to match the `uk` block's `uk-law`.
- `eu-processor-agreement` is the root `processors` section's contract pattern; no block
  section.
- *Commonly omitted*: `eu-dpia-consultation`, `eu-main-auxiliary` (1/15 each).
- `eu-processor-record` falls to rare (4/15) once the EUDPR registers count; it stays, since
  `facts.company.acts_as_processor` decides it.
- Joint controllers appear in s01 s02 s03 s04 s06 and every EUDPR register but are a root section
  (`joint-controllers`); the block does not repeat them.

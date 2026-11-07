# ropa, `uk` block: merged section list

Only content that applies under UK law counts (`build/build.md` *Region run*). The region-neutral
fields (purpose, data categories, retention...) are the root skeleton's and are not recounted.
Global samples are read from their tables in `research/ropa/samples/` (cells marked
`[law: ...]`, per `research/ropa/extract-notes.md`); new samples from `samples/`.

## Section ids

Meanings fixed before judging the saturation batch (2026-10-27), seeded from
`research/ropa/merge.md` *Regional content*.

| Id | Meaning | Includes |
|---|---|---|
| uk-law | the record names the UK law it is kept under or the regulator it is shown to | "UK GDPR Art. 30", "Data Protection Act 2018", "GDPR" in a title or band, "shown to the ICO on request" |
| uk-ico-registration | the controller's ICO registration (data protection fee) number | |
| uk-representative | the UK representative (Art. 27) field | empty or "n/a" fields count: the field is kept |
| uk-legal-basis | the UK GDPR Art. 6 basis per activity | article points, the article's words, short names; statutes or contracts behind a basis |
| uk-legitimate-interests | the legitimate interest named, or its assessment (LIA) linked or appended | "details relating to lawful basis" columns |
| uk-special-conditions | the Art. 9(2) condition or DPA 2018 Schedule 1 condition for special-category or criminal-offence data | Art. 10 / Sch. 1 Parts 2–3 for criminal data |
| uk-appropriate-policy | the appropriate policy document (Sch. 1 Part 4), or the "retained and erased per the policy document?" check | "special category assurance statement" |
| uk-transfers | transfers out of the UK in UK GDPR terms | third countries, Art. 49 safeguards, adequacy, "outside the UK/EEA" flags |
| uk-rights | which UK GDPR rights apply to the activity | |
| uk-processor-record | a separate record of processing done as a processor (Art. 30(2)) | |
| uk-public-authority | the body's status under the Freedom of Information Act 2000, or FOI handling | |
| uk-law-enforcement | processing under DPA 2018 Part 3 (law enforcement) and its Schedule 8 conditions | added at s43 |

Counted as root content, not here: consent mechanics (UK GDPR Art. 7 cited by s13 and s49),
DPIA rules (Art. 35, s01), automated decisions (Art. 22), security (Art. 32), Art. 30(1) letters
in column headings (a layout, recorded under *Document level*).

## Oxford colleges count once (2026-10-27)

Owner's ruling: the five Oxford colleges (s02, s20, s41, s42, s46) are one group under
`build/sources.md` rule 5. The first in pool order, s02, stays; s20, s41, s42 and s46 are
dropped and their tables kept as records only. s09 (Friends of the Angus, a Regent's Park
College charity) was not part of the ruling and stays. The first build's counts (26 samples,
saturated at s27) are replaced by those below.

## First batch

s01, s02, s03, s05, s06, s07, s09, s13, s14, s15, s18, s25, s28, s31 (14: 5 large, 3 mid,
5 small, 1 standard form). Mid is short: s20 and s41 left with the group ruling and no other
mid UK record was in the pool (St Antony's, the next lead, is another Oxford college).

| Id | Count | Samples |
|---|---|---|
| uk-legal-basis | 13/14 | s01 s02 s03 s05 s06 s07 s09 s13 s14 s15 s18 s25 s31 |
| uk-law | 11/14 | s01 s02 s03 s05 s06 s07 s13 s14 s15 s28 s31 |
| uk-special-conditions | 8/14 | s01 s02 s05 s07 s09 s13 s25 s31 |
| uk-legitimate-interests | 5/14 | s02 s09 s13 s25 s31 |
| uk-transfers | 6/14 | s05 s07 s13 s25 s28 s31 |
| uk-ico-registration | 4/14 | s05 s07 s13 s14 |
| uk-appropriate-policy | 4/14 | s05 s07 s13 s31 |
| uk-representative | 3/14 | s05 s07 s31 |
| uk-public-authority | 3/14 | s05 s07 s25 |
| uk-rights | 2/14 | s06 s31 |
| uk-processor-record | 1/14 | s31 |

## Saturation

Re-judged in pool order without s42 and s46. Batches as extracted: s43, s21, s45, then s27,
s48, s44, s49, s47.

| Sample | Verdict | Why |
|---|---|---|
| s43 | **new** | `uk-law-enforcement`: an activity run under DPA 2018 Part 3 with Schedule 8 conditions |
| s21 | not new | 1: title in Art. 30 vocabulary only |
| s45 | not new | 2: the ICO template filled; every id already listed |
| s27 | not new | 3: lawful-basis column |
| s48 | not new | 4: Art. 6 with statute, "transferred outside the UK?", rights |
| s44 | not new | 5 non-new in a row after s43: **saturated** |
| s49 | kept | past the stop point, same batch: "GDPR Information Audit", Art. 6 points, consent check |
| s47 | kept | same batch: lawful-basis column; FOI note |
| s42, s46 | dropped | Oxford group (rule 5) |

Stop: saturated at s44 (20th sample). With the kept samples, `sample_count: 22`: large 9,
mid 3, small 9, standard form 1. No id was lost by the ruling: every id the dropped colleges
had is also in a kept sample.

## All samples

| Id | Count | Samples |
|---|---|---|
| uk-legal-basis | 20/22 | s01 s02 s03 s05 s06 s07 s09 s13 s14 s15 s18 s25 s27 s31 s43 s44 s45 s47 s48 s49 |
| uk-law | 16/22 | s01 s02 s03 s05 s06 s07 s13 s14 s15 s21 s28 s31 s43 s45 s48 s49 |
| uk-special-conditions | 10/22 | s01 s02 s05 s07 s09 s13 s25 s31 s43 s45 |
| uk-transfers | 8/22 | s05 s07 s13 s25 s28 s31 s45 s48 |
| uk-legitimate-interests | 6/22 | s02 s09 s13 s25 s31 s45 |
| uk-appropriate-policy | 5/22 | s05 s07 s13 s31 s45 |
| uk-ico-registration | 5/22 | s05 s07 s13 s14 s43 |
| uk-rights | 4/22 | s06 s31 s45 s48 |
| uk-public-authority | 4/22 | s05 s07 s25 s47 |
| uk-representative | 3/22 | s05 s07 s31 |
| uk-processor-record | 1/22 | s31 |
| uk-law-enforcement | 1/22 | s43 |

Patterns behind the block's counts:

- uk-legal-basis: short names only 9/20 (s03 s06 s14 s15 s18 s27 s44 s47 s48); the article's
  words 4/20 (s02 s09 s13 s25); article point plus short name or words 7/20 (s05 s07 s31 s43
  s45 s49, and s01 mixes Art. 6 and Art. 9 labels without points). Statute or contract behind
  the basis: 6/20 (s02 s13 s25 s43 s48 s49).
- uk-law: UK GDPR and DPA 2018 together 6/16 (s01 s05 s06 s07 s14 s31); "GDPR" alone 7/16
  (s02 s03 s15 s21 s28 s48 s49); shown to the ICO or "supervisory authority" on request 3/16
  (s13 s14 s28); bands named for the law 2/16 (s31 s45).
- uk-special-conditions: Schedule 1 part and paragraph cited 6/10 (s05 s07 s13 s31 s43 s45);
  condition in words with the Act named 2/10 (s02 s09); Art. 9 conditions only, no Schedule 1,
  2/10 (s01 s25); separate criminal-data column 3/10 (s02 s09 s13); a sentence naming the duty
  and why consent is not used 2/10 (s02 s09); a lookup sheet of conditions 1/10 (s13).
- uk-legitimate-interests: one or two sentences naming the interest 3/6 (s02 s09 s25); an LIA
  link column 2/6 (s31, s45: "Yes" or empty); LIAs appended below the grid 1/6 (s13).
- uk-transfers: a third-countries column and a safeguards column 4/8 (s05 s07 s31 s45), empty
  or N/A on nearly every row; a yes/no flag 3/8 (s13 s25 s48); generic EEA wording 1/8 (s28).
  Filled rows name the country and the provider's certification (s45, Privacy Shield) or
  adequacy (s25). None names the IDTA or the UK Addendum.
- uk-appropriate-policy: the ICO template's three columns 4/5 (s05 s07 s31 s45); a yes/no
  "Special Category Assurance Statement" column 1/5 (s13).
- uk-representative: a header-grid field, empty or "n/a" in every filled sample (all are
  UK-established).
- uk-ico-registration: with a pointer to the ICO register 1/5 (s14).

## Document level

- The UK content sits in the same grid as the root fields: extra columns in grids, extra lines
  in forms. No sample gives it a part of its own (22/22). The block is written as "UK:"
  columns and header lines (PLAN decision 37).
- Column sets: the ICO template 4/22 (s05 s07 s31 s45); the Oxford colleges' set 2/22 (s02,
  and s09, which uses it).
- Article points cited in headings or cells: 9/22 (s05 s07 s13 s25 s28 s31 s43 s45 s49).

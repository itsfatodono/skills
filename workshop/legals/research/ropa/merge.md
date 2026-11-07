# ropa: merged section list

Formats: `prose`, `list`, `table`; layout marks `embedded` (inside another field) and
`pointer` (points to another document). For a RoPA, `table` is a column in a grid where each
row is an activity, `list` a labelled field in a per-record form, `prose` running text
(`extract-notes.md`). Ids marked *(regional)* exist because of one law; they count for the
saturation judgement but stay out of the root skeleton (*Regional content*).

## Section ids

Meanings fixed before judging the saturation batches (2026-10-26). Change only with a note
below.

| Id | Meaning | Includes |
|---|---|---|
| intro | opening statement: what the record is, the duty to keep it, its scope | title with a sentence of context; a bare title line does not count |
| controller | identity and contact of the controller, its DPO and any representative | header grids, contact blocks, DPO lines in each record |
| index | list of the records or activities in the set | register pages, processing list tabs, list of per-unit files |
| record-meta | reference number, version, creation and update dates, author, approval, review cycle | audit columns, version-control tables, "reviewed monthly" statements |
| owner | the unit or person accountable for the activity | business function, department, information asset owner, data owner, "service responsible" |
| activity | the name of the activity or record type the row or record describes | data asset, function, record set, processing operation name |
| purpose | why the data is processed, and how the processing runs | sub-purposes, description of the processing operation, nature of processing |
| legal-basis | the ground the law gives for the processing | statute or contract behind it, legitimate interest named, how consent is obtained |
| data-subjects | categories of people the data is about | |
| data-categories | categories or items of personal data | |
| sensitive-data | whether special-category or criminal-offence data is involved, which, and the condition relied on | flags, type lists, condition columns |
| source | where the data comes from and how it is collected | collection channel, time and manner of collection |
| recipients | who receives the data, inside and outside the organisation | sharing agreements pointed to |
| processors | service providers processing for the controller, and their contracts | "who is actually conducting the processing", link to contract, DPA in place |
| joint-controllers | joint controllers and their contact | |
| transfers | transfers out of the country or region, destinations and safeguards | "country where data is processed" |
| retention | how long data is kept, and what happens after | disposal, anonymisation, pointer to a retention schedule, deletion checks |
| security | technical and organisational security measures | "data controls" instructions |
| storage | systems, locations and media holding the data | |
| rights | which rights apply and how people exercise them | |
| notice | the privacy notice covering the activity, or how people are informed | |
| dpia | whether an impact assessment is needed, its status or link | |
| role | whether the organisation acts as controller, joint controller or processor for the row | |
| screening | whether the activity involves personal data at all | |
| automated-decisions | automated decision-making or profiling | |
| notes | free notes or comments per row | |
| consent-records | where consents are recorded | |
| risk | risk level or a risk register tied to the record | |
| operations | the processing operations performed (collect, store, transmit, erase) | |
| actions | open compliance actions and companion documents prepared | |
| declaration | the controller's attestation that the record is accurate | |
| breaches | breach history per activity | |
| appropriate-policy *(regional)* | appropriate policy document / "special category assurance statement" and the retention-per-policy check | `uk`: DPA 2018 Sch. 1 Part 4 |
| public-authority *(regional)* | statement that the body is a public authority under freedom of information law | `uk`: FOIA 2000 |
| lia *(regional)* | legitimate interests assessment | `eu`, `uk`: GDPR Art. 6(1)(f) |

## First batch

s01–s15 and s31–s35 (20 samples: 5 large, 5 mid, 5 small, 5 standard forms). No two samples
share the whole text (rule 4). s05 and s07 share the ICO template's columns (s31) and a similar
web-page layout; s02 and s09 share the Oxford colleges' column set; their contents differ.

| Id | Count | Formats | Samples |
|---|---|---|---|
| activity | 20/20 | embedded, list, prose, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 s35 |
| data-categories | 20/20 | embedded, list, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 s35 |
| retention | 20/20 | embedded, list, pointer, prose, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 s35 |
| purpose | 19/20 | embedded, list, prose, table | s01 s02 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 s35 |
| data-subjects | 19/20 | embedded, list, table | s01 s02 s03 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 s35 |
| recipients | 17/20 | embedded, list, pointer, table | s01 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 s35 |
| legal-basis | 17/20 | embedded, list, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s12 s13 s14 s15 s31 s34 s35 |
| record-meta | 16/20 | list, prose, table | s01 s02 s03 s04 s06 s08 s09 s10 s11 s12 s13 s14 s15 s32 s33 s34 |
| controller | 16/20 | embedded, list, table | s01 s03 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 s31 s32 s34 |
| intro | 15/20 | list, prose | s01 s03 s04 s05 s06 s07 s08 s11 s12 s13 s14 s32 s33 s34 s35 |
| security | 14/20 | embedded, list, prose, table | s01 s04 s06 s08 s10 s11 s12 s13 s14 s15 s31 s32 s33 s34 |
| sensitive-data | 14/20 | embedded, list, table | s01 s02 s03 s04 s05 s07 s08 s09 s10 s12 s13 s14 s31 s32 |
| owner | 13/20 | embedded, list, table | s01 s02 s05 s07 s08 s10 s11 s12 s13 s14 s31 s33 s35 |
| transfers | 13/20 | list, prose, table | s04 s05 s07 s08 s10 s11 s12 s13 s15 s31 s32 s33 s34 |
| processors | 10/20 | embedded, list, table | s04 s05 s06 s07 s08 s11 s12 s13 s31 s34 |
| source | 9/20 | embedded, list, table | s02 s06 s09 s10 s13 s15 s31 s33 s35 |
| storage | 9/20 | embedded, prose, table | s06 s08 s10 s12 s13 s14 s31 s33 s34 |
| joint-controllers | 8/20 | embedded, list, table | s04 s05 s07 s10 s11 s31 s32 s34 |
| index | 6/20 | list, table | s04 s08 s11 s12 s13 s32 |
| rights | 6/20 | list, pointer, table | s04 s06 s08 s11 s12 s31 |
| notice | 5/20 | embedded, list, pointer | s04 s08 s11 s12 s13 |
| appropriate-policy (regional) | 4/20 | table | s05 s07 s13 s31 |
| dpia | 3/20 | embedded, prose, table | s01 s31 s34 |
| public-authority (regional) | 2/20 | prose | s05 s07 |
| role | 2/20 | table | s10 s34 |
| screening | 2/20 | table | s10 s13 |
| automated-decisions | 2/20 | table | s13 s31 |
| notes | 2/20 | table | s13 s34 |
| lia (regional) | 2/20 | prose, table | s13 s31 |
| consent-records | 2/20 | prose, table | s31 s33 |
| risk | 2/20 | embedded, prose | s33 s34 |
| operations | 1/20 | table | s03 |
| actions | 1/20 | list | s06 |
| declaration | 1/20 | prose | s12 |
| breaches | 1/20 | table | s31 |

## Saturation

Batches of 5 in pool order from s16. A sample is new when it has an id not above, or writes a
known id in a format (prose, list, table) not yet recorded for it.

| Sample | Verdict | Why |
|---|---|---|
| s16 | invalid | rule 6: an 8-slide staff training deck about RoPAs, not a record |
| s17 | not new | every id in a recorded format (EU Art. 31 form as a numbered grid: table) |
| s18 | **new** | `actions` written as a table column ("Action Needed"); only `list` was recorded |
| s19 | invalid | rule 3: the register behind the English wrapper page is Dutch only |
| s20 | not new | same column set as s02 and s09; 1 non-new after s18 |
| s21 | not new | 2 |
| s22 | invalid | rule 3: the register page is English, the records are French |
| s23 | **new** | `storage` and `automated-decisions` written as labelled form fields (`list`), not recorded; further-purpose and modes-of-processing fields read as `purpose` and `automated-decisions` |
| s24 | not new | 1 non-new after s23 |
| s25 | not new | 2 |
| s26 | not new | 3 |
| s27 | not new | 4 |
| s28 | not new | 5 non-new in a row after s23: **saturated** |

Stop: saturated after s28. s29 and s30 were not extracted. Size thirds of the 25 sized samples:
large 7 (s16, s19 and s22, all large, were invalid), mid 9, small 9;
standard forms 5 of 30 (one in six).

## All samples

s01–s15, s17, s18, s20, s21, s23–s28, s31–s35 (30). Formats per id over all samples.

| Id | Count | Formats | Samples |
|---|---|---|---|
| activity | 30/30 | embedded, list, prose, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s17 s18 s20 s21 s23 s24 s25 s26 s27 s28 s31 s32 s33 s34 s35 |
| data-categories | 30/30 | embedded, list, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s17 s18 s20 s21 s23 s24 s25 s26 s27 s28 s31 s32 s33 s34 s35 |
| retention | 30/30 | embedded, list, pointer, prose, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s17 s18 s20 s21 s23 s24 s25 s26 s27 s28 s31 s32 s33 s34 s35 |
| purpose | 29/30 | embedded, list, prose, table | s01 s02 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s17 s18 s20 s21 s23 s24 s25 s26 s27 s28 s31 s32 s33 s34 s35 |
| data-subjects | 29/30 | embedded, list, table | s01 s02 s03 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 s17 s18 s20 s21 s23 s24 s25 s26 s27 s28 s31 s32 s33 s34 s35 |
| recipients | 26/30 | embedded, list, pointer, table | s01 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 s17 s18 s21 s23 s24 s25 s26 s27 s28 s31 s32 s33 s34 s35 |
| controller | 26/30 | embedded, list, prose, table | s01 s03 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 s17 s18 s20 s21 s23 s24 s25 s26 s27 s28 s31 s32 s34 |
| legal-basis | 25/30 | embedded, list, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s12 s13 s14 s15 s17 s18 s20 s23 s24 s25 s26 s27 s31 s34 s35 |
| record-meta | 24/30 | list, prose, table | s01 s02 s03 s04 s06 s08 s09 s10 s11 s12 s13 s14 s15 s17 s18 s20 s23 s24 s26 s27 s28 s32 s33 s34 |
| intro | 21/30 | list, prose | s01 s03 s04 s05 s06 s07 s08 s11 s12 s13 s14 s17 s23 s24 s25 s26 s28 s32 s33 s34 s35 |
| security | 21/30 | embedded, list, prose, table | s01 s04 s06 s08 s10 s11 s12 s13 s14 s15 s17 s18 s23 s24 s26 s27 s28 s31 s32 s33 s34 |
| sensitive-data | 19/30 | embedded, list, table | s01 s02 s03 s04 s05 s07 s08 s09 s10 s12 s13 s14 s18 s20 s23 s25 s28 s31 s32 |
| transfers | 19/30 | list, prose, table | s04 s05 s07 s08 s10 s11 s12 s13 s15 s17 s23 s24 s25 s26 s28 s31 s32 s33 s34 |
| owner | 17/30 | embedded, list, table | s01 s02 s05 s07 s08 s10 s11 s12 s13 s14 s18 s23 s24 s26 s31 s33 s35 |
| processors | 15/30 | embedded, list, table | s04 s05 s06 s07 s08 s11 s12 s13 s17 s21 s23 s24 s26 s31 s34 |
| source | 12/30 | embedded, list, table | s02 s06 s09 s10 s13 s15 s20 s25 s27 s31 s33 s35 |
| joint-controllers | 12/30 | embedded, list, table | s04 s05 s07 s10 s11 s17 s23 s24 s26 s31 s32 s34 |
| storage | 12/30 | embedded, list, prose, table | s06 s08 s10 s12 s13 s14 s18 s21 s23 s31 s33 s34 |
| index | 11/30 | list, pointer, table | s04 s08 s11 s12 s13 s17 s23 s24 s26 s28 s32 |
| rights | 9/30 | list, pointer, table | s04 s06 s08 s11 s12 s17 s23 s24 s31 |
| notice | 8/30 | embedded, list, pointer | s04 s08 s11 s12 s13 s23 s24 s26 |
| appropriate-policy (regional) | 4/30 | table | s05 s07 s13 s31 |
| dpia | 3/30 | embedded, prose, table | s01 s31 s34 |
| automated-decisions | 3/30 | list, table | s13 s23 s31 |
| public-authority (regional) | 2/30 | prose | s05 s07 |
| actions | 2/30 | list, table | s06 s18 |
| role | 2/30 | table | s10 s34 |
| screening | 2/30 | table | s10 s13 |
| notes | 2/30 | table | s13 s34 |
| lia (regional) | 2/30 | prose, table | s13 s31 |
| consent-records | 2/30 | prose, table | s31 s33 |
| risk | 2/30 | embedded, prose | s33 s34 |
| operations | 1/30 | table | s03 |
| declaration | 1/30 | prose | s12 |
| breaches | 1/30 | table | s31 |

## From ids to the skeleton

- Root sections, in median field order: `intro`, `controller`, `record-meta`, then per
  activity `activity`, `owner`, `purpose`, `legal-basis`, `data-subjects`, `data-categories`,
  `sensitive-data`, `source`, `recipients`, `processors`, `joint-controllers`, `transfers`,
  `retention`, `security`, `storage`, `dpia`, `automated-decisions`, `processor-activities`.
- `role` is renamed `processor-activities` in the skeleton (its *Applies when* is the company
  acting for customers); same samples.
- Folded, per `skeleton-format.md` (rare drafting ids no fact decides): `index` (11/30) into
  the document *Shape*; `rights` and `notice` (11/30 together) into `activity`; `notes`,
  `risk`, `actions` and `declaration` into `record-meta`; `consent-records` into
  `legal-basis`; `operations` and further-purpose fields into `purpose`.
- Left to *Commonly omitted*: `screening` (2/30), `breaches` (1/30).
- Regional ids (`appropriate-policy`, `public-authority`, `lia`) and every `[law: ...]` pattern
  stay out of the root; see below.

## Document level

- Shape: grid with one row per activity 19/30 (s01 s02 s03 s05 s06 s07 s09 s10 s13 s14 s15
  s18 s20 s21 s25 s27 s31 s33 s34); one form per activity 11/30 (s04 s08 s11 s12 s17 s23 s24
  s26 s28 s32 s35).
- Row unit: processing activity 17/30 (s04 s05 s07 s08 s10 s11 s12 s13 s14 s17 s23 s24 s26
  s28 s32 s34 s35); record type 7/30 (s03 s06 s15 s18 s21 s25 s27); data category within a
  purpose 4/30 (s02 s09 s20 s31); department 2/30 (s01 s33).
- Grouping: department, function or area 8/30 (s04 s05 s07 s11 s13 s23 s31 s33); data-subject
  group 3/30 (s02 s18 s20); theme 1/30 (s25).
- Web summary page with lists plus the full grid: 3/30 (s05 s07 s14).
- Status: says it is the public part or a summary of a fuller internal record 5/30 (s01 s04
  s08 s14 s23); FOI release of internal records 1/30 (s10); blank models 5/30 (s31–s35); no
  sign of a fuller version 19/30. See README *Lessons*.
- Register: formal third person in the EU forms (s04 s08 s11 s12 s17 s23 s24 s26); data-subject
  voice in s02 s09 s20; first person in s28.
- Shared layouts (not copies under rule 4): the ICO controller template filled in by s05 and
  s07 (model s31); the Oxford colleges' column set in s02, s09 and s20 (s20's first row is word
  for word s02's); the EU Art. 31 form family in the eight EU bodies.

## Regional content

Content one law requires, left out of the root skeleton. Region runs start from these samples.
Every sample comes from a law that requires the record; the table says which law shaped which
part.

| Region | Content | Samples |
|---|---|---|
| uk | Legal basis cited as UK GDPR Art. 6(1) points, by letter or in the article's own words, or as their short names | s01 s02 s03 s05 s06 s07 s09 s13 s14 s15 s18 s20 s25 s27 s31 s34 |
| uk | Special-category and criminal-offence conditions as DPA 2018 Schedule 1 part and paragraph, often from a drop-down; Art. 9(2) points beside them | s02 s05 s07 s09 s13 s20 s25 s31 |
| uk | Appropriate policy document ("special category assurance statement") and the "retained and erased per the policy document?" check, both under the ICO template's DPA 2018 band | s05 s07 s13 s31 |
| uk | Legitimate interests explained per row, or a legitimate interests assessment (LIA) linked or appended | s02 s09 s13 s20 s31 |
| uk | ICO registration number (data protection fee) in the controller block | s05 s07 s13 s14 |
| uk | Statement that the body is a public authority under FOIA 2000 | s05 s07 |
| uk | The ICO controller template's column set, with a separate processor template (Art. 30(2)) | s05 s07 s31 |
| eu, uk | Art. 30(1)(a)–(g) cited per column; representative (Art. 27) in the header grid; Art. 30(2) processor record | s05 s07 s10 s31 s32 |
| eu, uk | Transfer safeguards in the GDPR's vocabulary: adequacy decision, SCCs, BCRs, codes, certification, Art. 49 derogations; drop-down country list flagged adequate / not adequate | s04 s07 s08 s12 s23 s24 s26 s32 |
| eu | Irish statutes behind each basis (Art. 6(3)); Law Enforcement Purposes under the Irish DPA 2018 Part 5 | s10 |
| eu (institutions) | Reg. (EU) 2018/1725 Art. 31 register: a public register duty (Art. 31(5)), a numbered 12–18 item form per operation, Art. 5 bases, Art. 10/11 sensitive data, Chapter V transfers, "see the privacy statement" field. Public-sector only; no app maker is under this regulation, so no block is needed. | s04 s08 s11 s12 s17 s23 s24 s26 |
| je | Data Protection (Jersey) Law 2018 Art. 14(3); formal record mandatory only for larger or higher-risk processing | s34 |
| sg | Singapore PDPA: the record is a "data inventory map" organised by life-cycle stage (collection, use, disclosure in Singapore, storage, transfer outside Singapore, disposal); no legal-basis column; consent kept in a separate consent register | s33 |
| bn | Brunei PDPO: data inventory map by four life-cycle steps; "consent" as the basis; anonymisation after retention | s35 |
| tr | KVKK "kişisel veri işleme envanteri" and VERBİS. Not sampled in this run (`global` takes English texts; `regions/tr/region.md` names the VERBİS public query as the route). From the law (Veri Sorumluları Sicili Hakkında Yönetmelik, definition of the inventory; KVKK Art. 16): the inventory ties each business process to its purposes and legal ground (KVKK Arts. 5–6), data category, recipient group and data-subject group, with the maximum retention period, data planned for transfer abroad, and security measures. Differences from the root: rows are usually built around data categories per process; the maximum retention period is mandatory and links to the Saklama ve İmha Politikası (item 19); the inventory feeds the VERBİS registration (item 25), whose fields are the same categories; there is no processor record. | none |
| br | LGPD Art. 37 requires a record without listing fields; ANPD publishes a RoPA model for small processing agents (Portuguese, left out under rule 3) | none |

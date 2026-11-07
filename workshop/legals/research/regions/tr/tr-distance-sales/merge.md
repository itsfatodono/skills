# tr-distance-sales: merged section list

## First batch (written before saturation)

Samples: s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 (5 large, 5 mid, 5 small).

Formats, as in `build.md` step 3: prose (paragraphs, including numbered clauses written as
sentences), list (bullet or lettered enumeration of items), table (order table or label/value
block). Layout marks, which never make a sample new: pointer (content deferred to another page
or document), embedded (folded into another section), template (the sample has the section,
but its text is a template block per candidate rule 4).

These format definitions were tightened before any saturation sample was judged: the first
draft of this list used a wider set (fields, reference, numbered sub-clauses as list), which
would have made layout differences count as new. While judging the first saturation batch,
six first-batch samples were found coded inconsistently (a buyer defined in a sentence, or a
price described in prose, recorded as table or pointer only); they were corrected to include
prose before the verdicts below were final.

A section whose text is a template block still counts toward presence: the company chose to
include it. Its patterns are taken only from samples where the text is the company's own.

| Id | Title | Count | Formats | Samples |
|---|---|---|---|---|
| parties | Parties | 15/15 | prose, table | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| subject | Subject and legal basis | 15/15 | prose, template | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| delivery | Delivery | 15/15 | embedded, list, prose, template | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| withdrawal | Right of withdrawal | 15/15 | list, pointer, prose, template | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| exceptions | Withdrawal exceptions | 15/15 | embedded, list, pointer, prose | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| disputes | Disputes and governing law | 15/15 | prose | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| formation | Formation and entry into force | 15/15 | embedded, prose, template | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 s30 |
| goods-price | Goods, price and order details | 14/15 | pointer, prose, table | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s18 s24 |
| performance | Seller's performance, impossibility and force majeure | 14/15 | embedded, prose, template | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s24 s30 |
| pre-info-ack | Acknowledgement of pre-contract information | 13/15 | embedded, prose, template | s01 s02 s03 s04 s05 s07 s08 s10 s11 s12 s13 s14 s30 |
| card-misuse | Unauthorised card use and chargebacks | 10/15 | prose, template | s01 s02 s04 s05 s07 s08 s11 s12 s13 s24 |
| payment | Payment | 10/15 | embedded, list, prose, table | s02 s04 s05 s07 s10 s12 s13 s14 s18 s30 |
| order-limits | Consumer-only scope and order limits | 8/15 | embedded, prose | s02 s04 s05 s08 s10 s11 s12 s13 |
| default | Default | 8/15 | list, prose, template | s04 s05 s08 s11 s12 s14 s24 s30 |
| inspection | Inspection on delivery and damaged goods | 7/15 | embedded, prose, template | s01 s04 s05 s08 s10 s12 s24 |
| personal-data | Personal data | 7/15 | embedded, list, pointer, prose | s02 s03 s07 s12 s13 s18 s24 |
| signature | Signature block | 6/15 | table | s01 s02 s04 s05 s11 s12 |
| complaints | Complaints channel | 6/15 | embedded, prose, table | s01 s07 s08 s10 s12 s13 |
| use-terms | Use of the site and the purchased service | 6/15 | list, prose | s03 s07 s13 s18 s24 s30 |
| evidence | Evidence and records | 5/15 | prose | s04 s05 s08 s12 s24 |
| notices | Notices | 4/15 | embedded, prose | s01 s08 s12 s24 |
| definitions | Definitions | 4/15 | embedded, list, template | s07 s08 s10 s11 |
| withdrawal-form | Model withdrawal form | 2/15 | table | s01 s05 |
| misc-rare | Other rare blocks (cash on delivery, in-store exchange, unsolicited goods, unilateral amendment) | 2/15 | prose | s02 s10 |
| subscription | Recurring orders and subscriptions | 2/15 | embedded, prose | s24 s30 |
| loyalty | Loyalty points on returns | 1/15 | prose | s07 |

## Saturation

Batches in pool order (unused valid candidates only; invalid ones skipped and replaced by the
next in order). A sample is new when it has a section id not yet in the list, or a known id in
prose, list or table where that format is not yet recorded.

| Sample | Size | Verdict | Non-new streak |
|---|---|---|---|
| s16 | large | NEW: pre-info-ack as list | 0 |
| s17 | mid | not new | 1 |
| s19 | large | NEW: section marketplace | 0 |
| s20 | mid | NEW: goods-price as list | 0 |
| s22 | large | not new | 1 |
| s23 | mid | NEW: performance as list; card-misuse as list; inspection as list | 0 |
| s25 | large | not new | 1 |
| s26 | mid | not new | 2 |
| s28 | large | not new | 3 |
| s29 | mid | not new | 4 |
| s32 | mid | not new | 5 |

Skipped in pool order as invalid: s31 (rule 5), s33 (rule 4), s35 (rule 4). Stop: 5 non-new
in a row after s32 (s25, s26, s28, s29, s32), `saturated: true`.

Past the stop point and kept: s34 (large), s36 (small), s42 (small). s36 and s42 had been
extracted early as replacements for the small third; s34 was in flight when the run stopped.
None of the three is new against the list (checked: not new).

## Re-judge under decisions 26 and 27 (2026-10-27)

The verdicts above are the first run's; this section replaces them. Templates are valid
samples (decision 26), so the eight candidates dropped under the old rule 4 were judged again
(tables for s35 and s39 added now), and only a new section id makes a sample new (decision 27).

**Copies** (`build/sources.md` rule 4, same whole text): s27, s33 and s35 are the s15 text: the
same 14 articles and headings in the same order, Genel Hükümler 9.1–9.16, the same quotes; only
the seller's name and address differ (s27 adds a toy example to the exceptions and nothing
else). They count once, as s15. Not copies: s21 is the same template cut down to 8 articles (no
definitions, site-use clauses, default or entry-into-force article), so its section set differs
and it stays a sample; s06 (a WooCommerce shop template), s09 (a generator text) and s39 (a
pre-2014 shop template) match no other sample. s31 stays out under rule 5.

**First batch:** s01–s15 in pool order, 5 large, 5 mid, 5 small, with no replacements. Its
merged list has every id of the list above except `marketplace` (s19 only) and `subscription`
(s24 and s30 only). None of s06, s09, s15 brings an id outside the list; their content maps to
existing ids (s09's software-licence and IP clause to `use-terms`, s06 and s39's minimum-age and
price-error clauses to `order-limits`, s39's warranty-repair clause to `inspection`).

**Saturation**, batches of 5 in pool order, copies and invalid candidates skipped:

| Sample | Size | Verdict | Non-new streak |
|---|---|---|---|
| s16 | large | not new (first run: new by format only) | 1 |
| s17 | mid | not new | 2 |
| s18 | small | not new | 3 |
| s19 | large | NEW: `marketplace` | 0 |
| s20 | mid | not new (first run: new by format only) | 1 |
| s21 | small | not new | 2 |
| s22 | large | not new | 3 |
| s23 | mid | not new (first run: new by format only) | 4 |
| s24 | small | NEW: `subscription` | 0 |
| s25 | large | not new | 1 |
| s26 | mid | not new | 2 |
| s27 | small | copy of s15, skipped | – |
| s28 | large | not new | 3 |
| s29 | mid | not new | 4 |
| s30 | small | not new | 5 |

Stop: 5 non-new in a row after s30 (s25, s26, s28, s29, s30), `saturated: true`. Past the stop
point and kept: s32, s34, s36, s39, s42 (none new). Skipped: s31 (rule 5), s33 and s35 (copies of
s15). `sample_count: 34`.

**Patterns** (decisions 38 and 39): every sample counts for prevalence; in patterns each
template's wording counts once, and s21 (the s15 template cut down) adds none. The template
blocks in the 11 earlier samples were re-read on 2026-10-27 against each other and against s15
and s39 (6-word shingles per sentence, pages re-fetched):

| Template | Carried by | Counted once through |
|---|---|---|
| the common contract (Forbes TR / Law Insider TR; the IdeaSoft default is a close variant) | blocks in s01 s11 s19 s22 s24 s25 s28 s29 s32 s34 s42 | s15 |
| the pre-2014 shop template ("imzalı nüshası", "nakliyeyi engelleyen hava muhalefeti") | blocks in s01 s24; s25's 5.x general provisions | s39 |
| the alomaliye.com contract | blocks in s29; s34's own-coded text | s34 |
| a delivery, inspection and evidence set | blocks in s29; s22's own-coded text | s22 |
| the KVKK, IP and linked-sites block (Law Insider TR 9HSOCBT1vEp) | blocks in s19 (12, 11.3, 13.6, 19) and s22 (Madde 6) | s19, added now |

Changes: s19's block now counts once (personal-data full clause, commercial messages, marketing
consent in the contract; `use-terms` presence and website-terms; bank instalment campaigns;
loss of value on withdrawal; formation by electronic approval, copy in the account, article
count). s25's pre-2014 template sentences no longer count, as s39 carries that wording (third-
party recipient, intact delivery, force-majeure choice and events, card misuse). s21's pattern
counts are removed. Statutory wording (the regulation's exception list) is not template wording
and counts in every sample.

## Merged list (all 34 samples)

| Id | Title | Count | Formats | Samples |
|---|---|---|---|---|
| parties | Parties | 34/34 | pointer, prose, table | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 s42 |
| subject | Subject and legal basis | 34/34 | prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 s42 |
| withdrawal | Right of withdrawal | 34/34 | list, pointer, prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 s42 |
| exceptions | Withdrawal exceptions | 34/34 | embedded, list, pointer, prose | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 s42 |
| disputes | Disputes and governing law | 34/34 | embedded, prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 s42 |
| delivery | Delivery | 33/34 | embedded, list, prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s39 s42 |
| formation | Formation and entry into force | 32/34 | embedded, prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s18 s19 s20 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 s42 |
| goods-price | Goods, price and order details | 32/34 | list, pointer, prose, table, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s28 s32 s34 s36 s39 s42 |
| performance | Seller's performance, impossibility and force majeure | 31/34 | embedded, list, prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s20 s21 s22 s23 s24 s25 s26 s28 s29 s30 s32 s34 s36 s39 |
| pre-info-ack | Acknowledgement of pre-contract information | 30/34 | embedded, list, prose, template | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 s16 s17 s19 s20 s21 s22 s23 s25 s26 s29 s30 s32 s34 s36 s39 |
| card-misuse | Unauthorised card use and chargebacks | 22/34 | list, prose, template | s01 s02 s04 s05 s07 s08 s11 s12 s13 s15 s16 s17 s20 s21 s22 s23 s24 s25 s26 s29 s39 s42 |
| payment | Payment | 20/34 | embedded, list, prose, table | s02 s04 s05 s06 s07 s10 s12 s13 s14 s17 s18 s19 s20 s22 s23 s28 s30 s32 s34 s42 |
| inspection | Inspection on delivery and damaged goods | 19/34 | embedded, list, prose, template | s01 s04 s05 s06 s08 s10 s12 s15 s16 s17 s20 s22 s23 s24 s25 s26 s29 s34 s39 |
| personal-data | Personal data | 18/34 | embedded, list, pointer, prose, template | s02 s03 s06 s07 s12 s13 s15 s16 s17 s18 s19 s22 s23 s24 s26 s28 s29 s36 |
| use-terms | Use of the site and the purchased service | 18/34 | list, prose, template | s03 s07 s09 s13 s15 s16 s17 s18 s19 s22 s23 s24 s25 s26 s28 s30 s34 s36 |
| signature | Signature block | 16/34 | table | s01 s02 s04 s05 s06 s11 s12 s15 s20 s21 s23 s28 s29 s32 s36 s39 |
| default | Default | 15/34 | list, prose, template | s04 s05 s08 s11 s12 s14 s15 s16 s19 s22 s23 s24 s25 s30 s36 |
| order-limits | Consumer-only scope and order limits | 15/34 | embedded, prose | s02 s04 s05 s06 s08 s10 s11 s12 s13 s17 s19 s22 s25 s34 s39 |
| evidence | Evidence and records | 10/34 | embedded, prose | s04 s05 s08 s12 s16 s22 s24 s25 s26 s42 |
| definitions | Definitions | 10/34 | embedded, list, template | s06 s07 s08 s10 s11 s15 s19 s23 s25 s28 |
| complaints | Complaints channel | 9/34 | embedded, prose, table | s01 s07 s08 s10 s12 s13 s16 s22 s34 |
| notices | Notices | 5/34 | embedded, prose, template | s01 s08 s12 s24 s34 |
| misc-rare | Other rare blocks (cash on delivery, in-store exchange, unsolicited goods, unilateral amendment) | 4/34 | prose | s02 s10 s19 s34 |
| loyalty | Loyalty points on returns | 4/34 | prose | s07 s16 s26 s28 |
| withdrawal-form | Model withdrawal form | 3/34 | table | s01 s05 s28 |
| subscription | Recurring orders and subscriptions | 2/34 | embedded, prose | s24 s30 |
| marketplace | Marketplace role | 1/34 | prose, table | s19 |

### Folded into other skeleton sections

Ids kept here for the record but written into other skeleton sections:

- `complaints` (9/34) → *parties* (complaint channel) patterns.
- `evidence` (10/34) → *disputes*; samples put it right before or inside the disputes article.
- `notices` (5/34) → *parties* (address for service) and *formation* (e-mail/SMS as notice
  channel).
- `definitions` (10/34) → *Document*, recurring elements.
- `misc-rare` (4/34: cash on delivery 1, in-store exchange 1, unsolicited goods and digital
  codes 1, unilateral amendment clause 3 across s10, s24, s34) → *Document*, commonly omitted.

`definitions`, `complaints`, `evidence` and `notices` have no fact that could make a rare
section's *Applies when* true, so a separate rare section would never be written.

### Median position (0 = first, 1 = last; first 29 samples, not recomputed)

```
parties          median 0.06  n=29
definitions      median 0.06  n=8
subject          median 0.07  n=29
goods_price      median 0.18  n=28
marketplace      median 0.20  n=1
pre_info_ack     median 0.29  n=25
delivery         median 0.38  n=28
payment          median 0.38  n=19
performance      median 0.48  n=26
inspection       median 0.51  n=16
order_limits     median 0.53  n=13
misc_rare        median 0.53  n=8
complaints       median 0.54  n=8
subscription     median 0.56  n=2
card_misuse      median 0.57  n=19
use_terms        median 0.62  n=15
withdrawal       median 0.64  n=29
personal_data    median 0.68  n=16
exceptions       median 0.70  n=29
default          median 0.79  n=14
evidence         median 0.85  n=10
disputes         median 0.88  n=29
formation        median 0.91  n=27
notices          median 0.91  n=4
signature        median 1.00  n=12
withdrawal_form  median 1.00  n=3
```

`loyalty` (inside misc in this table before the split) sits after the exceptions in all four
samples, so the skeleton places it there.

## Document level

- Words: median 1,588 (s29 and s06), range 393 (s18) – 4,480 (s07). Under 600 words: s03 s14
  s18 s30 s32 s36 s42.
- Article style: "MADDE n" 26/34; plain numbered headings 8/34 (s10 s11 s15 s18 s19 s21 s23
  s30).
- Shares the page with the Ön Bilgilendirme Formu: s11 s24 s36; s13 calls itself the form in
  one article.
- Per-order template (blanks or tokens): 23/34; general text with no order fields: 11/34 (s03
  s09 s18 s20 s24 s25 s29 s30 s32 s36 s42).
- Whole text is a template: s06 s09 s15 s21 s39 (5/34). Template blocks inside an otherwise
  own text: s01 s11 s19 s22 s24 s25 s28 s29 s32 s34 s42 (11/34). Paraphrased from the common
  template without copied sentences: s02 s23.
- Outdated references (repealed Law 4077 or regulation, former ministry names, 2014 limits):
  s01 s05 s06 s13 s15 s17 s21 s22 s29 s34 s39.
- Drafting leftovers published: s03 (unfilled brackets), s09 (generator warning, unfilled
  bracket), s10 (lawyer's review notes), s12 (editor comment), s28 (unfilled carrier bracket).
- Seller entity differs from the brand or candidate row (group company): s02 s04 s14 s24 s26.
- Withdrawal period above 14 days: s16 and s34 (30 days); s31 (Boyner group, invalid) too.

## Regional content

None: this is a `whole` skeleton for a region-only item. Every section is Turkish-law
specific by design; no root skeleton is affected.

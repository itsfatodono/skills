# tr-pre-contract-info: merged section list

## First batch (written before saturation)

Samples: s01–s15 in pool order (5 large: s01 s04 s07 s10 s13; 5 mid: s02 s05 s08 s11 s14; 5
small: s03 s06 s09 s12 s15), no replacements. Goods: physical 12, digital or service 3 (s02
s03 s09). Form: stand-alone page 13, block inside the contract page 2 (s08, T3; s10, a page
titled "Satış Sözleşmesi" whose text calls itself the form and has no contract after it).

Formats, as in `build.md` step 3: prose, list, table, and the layout marks pointer and
embedded. A sample is new only when it has a section whose content fits no id below (decision
27); a known id written in another format or place is a pattern.

### Section ids

Ids reused from `research/regions/tr/tr-distance-sales/merge.md` keep that file's name and, as
far as the form allows, its meaning; the note says where this list draws the line differently.

| Id | Meaning (one line) | Overlap with tr-distance-sales |
|---|---|---|
| parties | Who the seller is and how to reach it (trade name, address, phone, e-mail, MERSIS, KEP), plus buyer, recipient and invoice fields when present | same id |
| subject | What the form is for and the law it is issued under (Law 6502, the Distance Contracts Regulation) | same id |
| definitions | Defined terms used in the form | same id |
| marketplace | The seller's role relative to a platform or brand: intermediary service provider block, authorised-reseller statement | same id, widened to the reseller case (s13) |
| goods-price | Main characteristics of the goods or service and the total price with taxes: order table, order fields, or a pointer to the product page or order screen | same id; price validity is split out below |
| price-validity | How long the listed prices, offers and pre-contract information stay valid | new; tr-distance-sales folds it into `goods-price` |
| payment | Payment methods, instalments, transfer deadlines, bank details, invoicing, collection by the platform | same id |
| payment-duty | Warning that confirming the order creates a duty to pay the price, shipping and taxes | new |
| delivery | Delivery or performance: place, recipient, carrier, dispatch time, legal maximum, delivery cost, digital activation | same id |
| performance | What happens when the seller cannot perform on time: impossibility, substitute goods, force majeure, buyer's cancellation and refund | same id |
| inspection | Checking the parcel on delivery and reporting damaged, wrong or missing items | same id |
| card-misuse | Unauthorised card use, chargebacks and unpaid card payments after delivery (note 1) | same id |
| order-limits | Who and what the seller will not sell to or may cancel: consumer-only scope, business-buyer rules, fraud or resale cancellation, bulk caps, price errors, territorial scope | same id |
| withdrawal | Right of withdrawal: period and start, how to notify, return of goods, refund, costs | same id |
| exceptions | Goods and services with no withdrawal right, including a statement that the right does not exist for what is sold | same id |
| withdrawal-form | The model withdrawal form, appended | same id |
| digital-content | What the buyer needs to use the product: usage instructions, functionality and technical requirements of digital content or software, technical protection measures, where its data lives | new (Regulation art. 5/1 ı and i items) |
| after-sales | Warranty, guarantee and after-sales support | new; tr-distance-sales maps a warranty-repair clause to `inspection` |
| subscription | Contract duration, recurring supply and renewal, including a statement that the sale is one-off | same id, widened to "duration" (s07 states there is no term) |
| complaints | Channel for complaints and requests to the seller | same id |
| disputes | Consumer arbitration committees, consumer courts, monetary limits, mediation, venue | same id |
| personal-data | How buyer personal data is processed, or a pointer to the privacy notice | same id |
| use-terms | Use of the site and of the purchased content: site disclaimers, third-party links, IP in content, download bans | same id |
| loyalty | Loyalty points, gift vouchers and campaign benefits on withdrawal or cancellation | same id |
| pre-info-ack | Buyer confirms having read and been informed of the pre-contract information | same id |
| formation | How the form relates to the contract: accepted electronically before the contract step, becomes part of the contract, when the contract forms | same id |
| copy | How the buyer receives and can later reach a copy of the form and contract, and how long the seller keeps it | new; tr-distance-sales folds "copy in the account" into `formation` |
| misc-rare | Rare one-off blocks: correcting order-entry errors (s01, s12), chamber membership and code of conduct (s01), list of related documents (s03) | same id name, different contents |

Not used from tr-distance-sales: `default`, `evidence`, `notices` (no sample has them) and
`signature` (see *Drafting boilerplate*).

Note 1 (2026-10-27, while judging s17; wording made explicit, scope unchanged): `card-misuse`
also covers what follows when the buyer's card payment or instalment is not paid over: the
dispute is between buyer and bank, and the buyer answers for the seller's loss from late
payment. The first batch already mapped this here (s01 row 11, default interest on card
instalments; s04 row 9 and s07 row 12, unpaid instalments). So s17's "TEMERRÜT HÜKÜMLERİ"
article maps to `card-misuse` (buyer side) and `performance` (seller side) and does not revive
tr-distance-sales `default`. Likewise s20's notice-address clause maps to `parties` (how to
reach the seller), as the tr-distance-sales skeleton folds `notices` into *parties*.

### Drafting boilerplate (decision 44; `build.md` step 3)

The form is a notice: it informs before the contract, and its own text says the binding terms
are in the distance sales contract it becomes part of. So text that gives the buyer no fact is
noted here and is never an id or a reason to call a sample new:

- Signature and date blocks (SATICI / ALICI / TARİH fields, consumer name and date fields):
  s07 (inside 12), s12 (closing block), s13 (after 9), s14 (closing block), s15 (closing). The
  acknowledgement sentence next to them is `pre-info-ack`; only the fields are boilerplate.
- "Made for commercial purposes" line: s08, s15 (T3 and T1 carry it; it contradicts the
  consumer framing).
- Template note "this form is a standard template" (s03), update or validity date lines (s02,
  s03, s12, s14), a general reservation of statutory rights (s10, inside `complaints`).

Accepted 2026-10-27 (chief of staff): signature and date blocks stay at document level under
decision 44, so this skeleton has no `signature` id; and s01's built-in blanket consent to data
use and commercial messages stays flagged as wrong (see *personal-data* under *Patterns*), never
a default.

No sample has a binding-language, severability or entire-agreement clause. The contract-style
clauses some forms carry (card misuse, seller cancellation, site disclaimers, IP) give the buyer
facts, so they stay as ids here; whether the skeleton keeps them is a write-step question.

### Section map per sample

Row numbers are the extraction tables'. Rows marked *doc* are document level.

| Sample | Map |
|---|---|
| s01 | 1 definitions; 2 parties, complaints (embedded: complaint line and e-mail fields); 3 subject, delivery (pre-order shipping); 4 payment, goods-price, misc-rare (order errors), order-limits (no service abroad); 5–6 withdrawal; 7 exceptions, withdrawal (shipping deduction); 8 personal-data (pointer), misc-rare (ITO code of conduct), copy; 9 parties; 10 goods-price, delivery; 11 delivery, payment, card-misuse, performance; 12 personal-data, use-terms; 13 performance (refund), disputes, pre-info-ack, formation; 14 payment-duty, goods-price, payment, withdrawal (repeat of 2–4); 15 exceptions (repeat); 16 withdrawal-form |
| s02 | 0 subject, formation; 1 parties; 2 goods-price; 3 goods-price, payment; 4 delivery (digital); 5 withdrawal, exceptions; 6 complaints, disputes; 7 copy; 8 price-validity, formation |
| s03 | 1 subject; 2 *doc* (template note); 3 pre-info-ack, payment-duty, formation; 4 parties; 5 goods-price, digital-content; 6 subscription; 7 goods-price, payment, delivery (cost), price-validity; 8 delivery, inspection, after-sales, digital-content (prerequisites); 9 goods-price (seats), after-sales, order-limits (used hardware for business buyers only); 10–11 digital-content (data location, backup, telemetry); 12 withdrawal, exceptions, order-limits (no right for business buyers); 13 complaints, disputes, subscription (renewal requests); 14 misc-rare (related documents); 15 pre-info-ack |
| s04 | 1 subject, copy; 2 definitions; 3 parties; 4 marketplace; 5 goods-price, price-validity, delivery, payment, marketplace (platform collects); 6 payment, goods-price; 7 withdrawal; 8 exceptions; 9 payment (invoices), delivery, inspection, card-misuse, performance; 10 disputes; 11 goods-price (pointer); 12 goods-price; 13 payment |
| s05 | 1–2 parties; 3 subject; 4 goods-price, payment; 5 delivery, performance; 6 delivery; 7 payment; 8 price-validity, order-limits (price errors); 9 withdrawal; 10 exceptions; 11 formation; 12 disputes; 13 order-limits (fraud); 14 order-limits (consumer-only), pre-info-ack |
| s06 | 1 subject; 2 formation (deemed acceptance); 3 parties, payment (bank details); 4 goods-price; 5 delivery; 6 payment; 7 delivery; 8 complaints; 9 exceptions, withdrawal; 10–11 withdrawal; 12 disputes; 13 pre-info-ack, formation, copy |
| s07 | 1 subject, copy; 2 definitions; 3 parties; 4 goods-price, price-validity; 5 payment, delivery, goods-price, withdrawal (return carrier); 6 complaints; 7–9 withdrawal; 10 exceptions; 11 delivery, performance, inspection; 12 card-misuse, payment; 13 performance; 14 loyalty; 15 order-limits; 16 digital-content (usage instructions); 17 price-validity (repeat); 18 subscription (one-off, no term); 19 disputes; 20 personal-data; 21 pre-info-ack, formation, *doc* (signature fields); 22 personal-data; 23 withdrawal-form |
| s08 | 1–2 parties; 3 goods-price, price-validity; 4 pre-info-ack; 5 delivery; 6 performance; 7 payment, card-misuse; 8 performance; 9 disputes; 10 *doc* (commercial purpose) |
| s09 | 1 subject, formation, pre-info-ack; 2 parties; 3 goods-price, payment, use-terms (download ban), digital-content; 4 payment; 5 delivery (access link); 6 withdrawal, exceptions; 7 use-terms; 8 personal-data; 9–10 digital-content; 11 performance; 12 complaints, disputes, pre-info-ack, copy; 13 order-limits (consumer-only); 14 pre-info-ack |
| s10 | 1–2 parties; 3 subject; 4 goods-price, delivery (cost); 5 price-validity; 6 pre-info-ack; 7 use-terms, personal-data; 8 delivery, inspection, performance; 9 card-misuse, performance, order-limits; 10 payment (instalment ban); 11 withdrawal; 12 exceptions; 13 complaints; 14 disputes; 15 formation |
| s11 | 1 parties; 2 goods-price; 3 goods-price, payment, delivery (charge); 4 delivery; 5 goods-price, performance (substitution); 6 exceptions (no withdrawal for perishables); 7 inspection; 8 performance; 9 personal-data (pointer); 10 disputes; 11 pre-info-ack |
| s12 | 1 definitions; 2 parties; 3 subject; 4 goods-price, payment, misc-rare (order errors); 5 order-limits (price errors); 6 delivery; 7–9 withdrawal; 10 exceptions; 11 goods-price (order fields); 12 personal-data (pointer); 13 complaints, disputes; 14 pre-info-ack, copy, formation; 15 *doc* (signature, update date) |
| s13 | 0 marketplace (authorised reseller), subject; 1 parties, complaints (embedded); 2 goods-price, payment, delivery; 3 payment; 4 delivery, performance, inspection, payment, after-sales (technical support), complaints; 5 withdrawal, exceptions, order-limits (non-consumers); 6 personal-data; 7 disputes; 8 formation, pre-info-ack, *doc* (date and signature lines); 9 withdrawal-form |
| s14 | 0 subject; 1 parties; 2 goods-price, price-validity; 3 payment; 4 delivery; 5 withdrawal, after-sales (freshness guarantee); 6 exceptions; 7 disputes; 8 pre-info-ack, *doc* (seller line, validity date) |
| s15 | 1 subject, payment-duty; 2–3 parties; 4 goods-price, price-validity, payment; 5 pre-info-ack, delivery, performance, card-misuse, payment; 6 payment (invoice); 7 withdrawal; 8 exceptions, disputes; 9 *doc* (commercial purpose, signature) |

### Merged list

Count is presence in the 15 samples. Formats count samples per format (a sample can write an id
in more than one). Median position: 0 = first section, 1 = last, first occurrence, *doc* rows
left out.

| Id | Count | Median pos. | Formats | Samples |
|---|---|---|---|---|
| parties | 15/15 | 0.09 | list 15, prose 1 | all |
| payment | 15/15 | 0.23 | prose 11, list 8, table 3 | all |
| goods-price | 15/15 | 0.23 | list 10, prose 8, table 4, pointer 1 | all |
| delivery | 15/15 | 0.33 | prose 13, list 5, table 2 | all |
| disputes | 15/15 | 0.85 | prose 13, list 2 | all |
| exceptions | 14/15 | 0.65 | list 9, prose 5 | all but s08 |
| subject | 13/15 | 0.00 | prose 13 | all but s08 s11 |
| withdrawal | 13/15 | 0.62 | prose 12, list 3 | all but s08 s11 |
| pre-info-ack | 13/15 | 0.89 | prose 11, list 3 | all but s02 s04 |
| performance | 10/15 | 0.54 | prose 10, list 1 | s01 s04 s05 s07 s08 s09 s10 s11 s13 s15 |
| formation | 10/15 | 0.78 | prose 9, list 1 | s01 s02 s03 s05 s06 s07 s09 s10 s12 s13 |
| price-validity | 9/15 | 0.33 | prose 7, table 3 | s02 s03 s04 s05 s07 s08 s10 s14 s15 |
| complaints | 9/15 | 0.75 | prose 7, list 3 | s01 s02 s03 s06 s07 s09 s10 s12 s13 |
| order-limits | 8/15 | 0.55 | prose 8, list 1 | s01 s03 s05 s07 s09 s10 s12 s13 |
| personal-data | 7/15 | 0.67 | prose 5, pointer 3 | s01 s07 s09 s10 s11 s12 s13 |
| copy | 7/15 | 0.85 | prose 7 | s01 s02 s04 s06 s07 s09 s12 |
| inspection | 6/15 | 0.48 | prose 4, list 2 | s03 s04 s07 s10 s11 s13 |
| card-misuse | 6/15 | 0.62 | prose 6 | s01 s04 s07 s08 s10 s15 |
| definitions | 4/15 | 0.02 | list 4 | s01 s04 s07 s12 |
| payment-duty | 3/15 | 0.08 | prose 3 | s01 s03 s15 |
| digital-content | 3/15 | 0.23 | prose 3, list 2 | s03 s07 s09 |
| misc-rare | 3/15 | 0.23 | prose 2, list 1 | s01 s03 s12 |
| use-terms | 3/15 | 0.43 | prose 3, list 1 | s01 s09 s10 |
| after-sales | 3/15 | 0.46 | prose 3, list 1 | s03 s13 s14 |
| withdrawal-form | 3/15 | 1.00 | list 3 | s01 s07 s13 |
| marketplace | 2/15 | 0.12 | list 1, prose 1, table 1 | s04 s13 |
| subscription | 2/15 | 0.54 | prose 2, list 1 | s03 s07 |
| loyalty | 1/15 | 0.59 | prose 1 | s07 |

28 ids: 9 at 13/15 or more; 9 at 6/15–10/15; 7 at 3/15–4/15 (definitions 27%, the other six
exactly at the 20% line); 3 under 20% (marketplace, subscription, loyalty), which go to
*Commonly omitted* if the count holds. Final classes wait for saturation.

### Patterns (first batch; template wording counted once, see *Copies*)

- **parties.** Seller block filled in 12/15; left blank or as tokens for the checkout 3 (s01
  s04 s15). MERSIS given 9 (s01 s02 s04 s06 s07 s08 s09 s12 s13), KEP 4 (s02 s04 s08 s13).
  Buyer fields present 8 (s01 s03 s04 s05 s09 s10 s13 s15); s08 defines the buyer in one
  sentence as the registered member; s02 s06 s11 s14 have no buyer block. Separate notice or
  return addresses: s10 (per product line), s12 (notice and showroom).
- **goods-price.** Order table or order fields 10 (s01 s03 s04 s05 s06 s07 s09 s12 s13 s15);
  only a pointer to the product page or order screen 5 (s02 with a price placeholder, s08 s10
  s11 s14; s10's pointer is circular, to the form itself). Product-specific characteristics
  written out: s03 (software modules and limits), s11 (perishable, representative images).
- **price-validity.** One shared sentence (prices valid until changed, time-limited prices
  until their end) in 6 samples, counted once; own wording: s02 (information valid until the
  order), s03 (validity of offers), s14. s05 adds price-error handling (mapped to order-limits).
- **payment.** Methods listed 15/15. Bank account or IBAN in the form: s06 s09. Instalment or
  bank-campaign disclaimers: s04 s13; a category instalment ban: s10. Invoice handling: s02
  s04 s13 s15.
- **delivery.** The 30-day legal maximum stated 12/15; the three without it are digital or
  service sales (s02 s09) or give only a shop-wide window (s06). Shop-wide dispatch figures
  instead of per-order: s06 s07 s14.
- **withdrawal.** Start-date rules for split, multi-part and regular deliveries: s01 s04 s07 s10
  s12 s13; s06 gives 14 days from delivery (last item) only. Return cost: on the seller s10 s15, on the buyer with exceptions s14,
  contradictory s05. Stricter-than-law return conditions (unopened, original box, invoice
  original): s05 s06 s07 s13. Duplicated in full inside the same form: s01. Voluntary goodwill
  refunds beyond the law: s03 (24 hours), s09 (partial).
- **exceptions.** The regulation's full list copied 8 (s01 s04 s05 s07 s10 s12 s13 s15; the
  list is statutory wording and counts in every sample); a subset fitting the goods 6 (s02 s03
  s06 s09 s11 s14). Own additions to the list: s05 (old-style category list), s10 (custom-made
  goods), s01 and s14 (examples in brackets).
- **pre-info-ack.** In the closing part 8 (s01 s05 s06 s07 s11 s12 s13 s14); inside the
  general provisions 3 (s08 s10 s15); at the top 2 (s03 s09, both repeat it at the end). Statute-citing closing sentence (Law 6502
  art. 48/2, regulation arts. 5–7): s05 s09, one wording.
- **formation.** "The contract step follows only after the form is accepted" sentence: s05 s07
  s13 (one wording); "the form becomes part of the contract": s01 s02 s09 s12; deemed acceptance
  of the contract by site users: s06.
- **disputes.** Thresholds by reference to the ministry's yearly figures 10; the current figure
  in TL: s12 s13; dated figures under old law: s08 s15; no threshold: s11. Mediation before
  court: s03 s12 s13. Separate venue for business buyers: s03 s06; a named city court: s14.
- **complaints.** Its own section 3 (s06 s07 s10); a clause in the disputes article 4 (s02 s03
  s09 s12); a clause in the delivery article (s13, which also lists a complaint e-mail in the
  seller block); only fields in the seller block (s01).
- **personal-data.** Pointer to a separate notice 3 (s07 art. 11, s11, s12); short inline
  notice 4 (s01 s09 s10 s13; s07 adds an annex). s12 says accepting the form is not marketing
  consent; s01 drafts a deemed blanket consent to data use and messages inside the form (the
  pattern decision 47 calls wrong for item 12; flag it, never a default).
- **order-limits.** Consumer-only scope clause: s05 s09 (one wording), s03 s13 (own). Fraud or
  resale cancellation: s05 s07 s10. Price errors: s05 s10 s12 (s12 limits the seller explicitly).
- **copy.** Kept in the buyer's account or on the site: s02 s04 s06 s07; e-mailed: s01 s02;
  seller retention period stated: s01 s09; durable medium after the order: s12.
- **digital-content, after-sales, subscription.** All three come mostly from the digital or
  service samples (s03 s09) plus s07's statutory-item articles (usage, duration). They track
  *Goods*, which suggests an *Applies when* on product type rather than a size or sector effect.

### Copies (`build/sources.md` rule 4; decisions 26, 38, 39)

Raw texts s01–s15 compared pairwise on 6-word shingles (2026-10-27). **No copies in the first
batch.** The highest overlap is s04/s07 (35% of s04, 21% of s07); every pair above 10% was
read span by span, and the shared text is the template blocks below plus statutory wording.
Section sets differ in every pair, so all 15 stay samples and none is a cut-down template
(decision 38 does not apply).

Shared texts named in `candidates.md`:

| Template | In the first batch | Note |
|---|---|---|
| T1 | s15 (whole text) | Only carrier in the batch; Shaya, OPPO and Hidromas (reserve) share its opening. |
| T2 | s01 (source text) | s19 Tekzen (saturation) shares the opening; not judged here. |
| T3 | s08 (block) | Only carrier in the batch. |
| T4, T5 | none | Reserve rows only. |

Template blocks that cross these texts (decision 39: each counts once in patterns; every
carrier still counts for presence):

| Block | Marker wording (paraphrased) | Carried by | Counted once through |
|---|---|---|---|
| older shop general provisions | force majeure as "weather blocking transport"; bank-refund delay disclaimer; ministry limits "set each December" | s08 (3.1–3.9, dispute), s10 (6.1, 6.7–6.16, 10), s15 (5.x, part of 7) | s08 |
| common contract provisions | statutory definitions; delivery to a third person; inspection report with the carrier; payment before delivery and 3-day chargeback return; 3-day substitute notice; "value announced by the ministry" | s04 (2, 5, 9, 10), s07 (2, 4, 5, 11–13, 19), fragments in s01 (7.x) | s04 |
| price-validity sentence | prices valid until changed; time-limited prices until the end date | s04 s05 s07 s08 s10 s15 | s04 |
| subject sentence | Law 6502 and the regulation cited by gazette date and number | s05 s10 | s05 |
| consumer-only and art. 48/2 closing | protective clauses apply only to consumers; buyer confirms under 6502 art. 48/2 | s05 (14), s09 (13–14) | s05 |
| formation sentence | contract step only after electronic acceptance | s05 s07 s13 | s05 |

The first two blocks look like the `tr-distance-sales` templates it calls "the pre-2014 shop
template" (marker "nakliyeyi engelleyen hava muhalefeti") and "the common contract"; that run
kept no `raw/` texts, so the match is by its recorded markers, not a text comparison.
Statutory wording (the exception list, the start-date cases, the model withdrawal form, the
14-day sentence) is not template wording and counts in every sample.

## Document level

- Words: median 1,734 (s12), range 270 (s11) – 4,200 (s01). Under 500 words: s02 s11 s14.
  s08's 739 is the block only; its page runs to about 2,200 with the contract.
- Article style: "MADDE n" 6 (s01 s03 s06 s08 s10 s12); plain numbered headings 9.
- Per-order template (blank fields or checkout tokens) 12; general text with no order fields 3
  (s08 s11 s14). Token styles left visible: `{_…_}` (s06 s15), `%…%` and a loop tag (s05),
  `{{ … }}` and a `{% for %}` loop (s04), square brackets (s02 s03), `Xxxx` (s09).
- Update or effective date: s02 s03 s12; none in 12.
- Model withdrawal form appended: s01 s07 s13.
- Contract-style general provisions inside the form (card misuse, seller cancellation, site
  disclaimers): s01 s04 s07 s08 s10 s15, mostly through the two template blocks above.
- Outdated references (repealed Law 4077 limits, former ministry names, 2014 limits): s05 s08
  s10 s15.
- Drafting errors published: s01 (withdrawal articles duplicated with drift), s07 (duplicate
  article numbers, a heading copied over other content), s08 and s10 ("SATICI" where the buyer
  is meant), s13 (no section 6), s15 (garbled numbering, calls itself a contract).
- Seller entity differs from the candidate row: s02 (Fernus Eğitim Teknolojileri A.Ş.), s13
  (authorised reseller GPN, not ASUS), s14 (a sole trader).
- Marketplace form repeated per seller with one order summary: s04.

## Regional content

None: this is a `whole` skeleton for a region-only item. Every section is Turkish-law specific
by design; no root skeleton is affected.

## Saturation

Batches of 5 in pool order. A sample is new only when it has a section whose content fits no id
above (decision 27); copies (rule 4) are skipped and do not count.

| Sample | Size | Verdict | Non-new streak |
|---|---|---|---|
| s16 | large | not new | 1 |
| s17 | mid | not new (note 1) | 2 |
| s18 | small | not new | 3 |
| s19 | large | not new; not a copy | 4 |
| s20 | mid | not new | 5 |

Stop: 5 non-new in a row after s20 (s16–s20), `saturated: true`. No id added. `sample_count:
20`.

**Copies.** Raw texts s16–s20 compared on 6-word shingles against s01–s20. s19 (Tekzen)
shares 45% of its text with s01 (Karaca, T2): the definitions, purpose line, general
provisions, withdrawal and notice articles and the delivery clauses follow T2. It is not the
same whole text: it drops s01's repeated withdrawal block, rewrites the exceptions as a subset
with its own product examples, replaces s01's blanket consent with a short data clause pointing
to the privacy notice, and adds a payment-duty article. It stays a sample and is not a cut-down
template under decision 38, since it adds its own text; its T2 wording counts once in patterns,
through s01 (decision 39), and its own parts count. No other saturation sample shares more than
15% with any sample (s16: 15% with s07; s17: 12% with s07; s18 and s20: under 10%).

**Section maps** (rows as in the extraction tables):

| Sample | Map |
|---|---|
| s16 | 1 subject; 2 parties; 3 goods-price, payment, delivery (click-and-collect, uncollected orders cancelled); 4 withdrawal, inspection; 5 exceptions; 6 complaints, disputes; 7 withdrawal-form; 8 complaints (pointer to contact form) |
| s17 | 0 *doc* (title); 1–2 parties; 3 subject; 4 goods-price; 5 payment; 6 delivery; 7 inspection; 8 pre-info-ack, payment-duty, performance, card-misuse, disputes (applicable law); 9 withdrawal; 10 exceptions; 11 performance, withdrawal (refund); 12 card-misuse, performance (note 1); 13 copy (3-year record keeping); 14 disputes; 15 formation, pre-info-ack; 16 *doc* (signature block); 17 withdrawal-form |
| s18 | 1 subject; 2 parties; 3 goods-price; 4 goods-price, payment; 5 delivery (digital); 6 exceptions; 7 subscription; 8 complaints, disputes; 9 *doc* (dates) |
| s19 | 1 definitions; 2 subject, delivery (pre-order); 3 payment, payment-duty, goods-price, misc-rare (order errors), delivery; 4 withdrawal; 5 withdrawal; 6 exceptions; 7 parties; 8 goods-price, delivery, performance, inspection; 9 personal-data (pointer), use-terms; 10 complaints, disputes, pre-info-ack; 11 payment-duty; 12 withdrawal-form; 13 formation (deemed acceptance), *doc* (signature labels) |
| s20 | 1 parties; 2 subject, pre-info-ack; 3 goods-price, payment; 4 delivery, payment (fees); 5 delivery, inspection, card-misuse, payment, performance, complaints, after-sales (warranty repairs), order-limits (abroad, minors), digital-content (devices for e-books), use-terms (copy ban), parties (notice addresses, note 1); 6 withdrawal; 7 exceptions; 8 withdrawal, inspection, after-sales (printing defects); 9 disputes; 10 formation, pre-info-ack, disputes (6502 as fallback law) |

What they add as patterns (counted in the final merge): s16 and s17 copy the regulation's
newer exceptions (phones, tablets, computers, vehicles, installed goods), absent from every
first-batch list; s16 handles click-and-collect next to home delivery; s17 calls the seller an
"intermediary service provider" without a marketplace role; s18 is the shortest form so far
(178 words), with no withdrawal right, no acknowledgement and no buyer fields; s20 gives the
seller's own shorter window for wrong-order returns beside the statutory right, and offers an
online withdrawal form.

## Merged list (all 20 samples, step 4)

Count, median position (first occurrence, *doc* rows left out) and skeleton handling. Tiers per
`skeleton-format.md`: core ≥16/20, common 8–15, rare <8.

| Id | Count | Median pos. | Skeleton |
|---|---|---|---|
| parties | 20/20 | 0.10 | core |
| goods-price | 20/20 | 0.23 | core |
| payment | 20/20 | 0.25 | core |
| delivery | 20/20 | 0.33 | core |
| disputes | 20/20 | 0.85 | core |
| exceptions | 19/20 | 0.62 | core |
| subject | 18/20 | 0.00 | core |
| withdrawal | 17/20 | 0.56 | core |
| pre-info-ack | 16/20 | 0.78 | core |
| performance | 13/20 | 0.50 | common |
| complaints | 13/20 | 0.75 | common |
| formation | 13/20 | 0.89 | common |
| inspection | 10/20 | 0.46 | common |
| price-validity | 9/20 | 0.33 | common |
| order-limits | 9/20 | 0.54 | common |
| card-misuse | 8/20 | 0.57 | common; placed before *withdrawal* (0.56) so withdrawal and exceptions stay together |
| personal-data | 8/20 | 0.67 | common, with *Avoid* (s01) |
| copy | 8/20 | 0.82 | common |
| withdrawal-form | 6/20 | 1.00 | rare |
| definitions | 5/20 | 0.00 | folded into *Document* (recurring elements); no fact decides it |
| payment-duty | 5/20 | 0.17 | folded into *goods-price* and *pre-info-ack* as a pattern; no fact decides it |
| use-terms | 5/20 | 0.44 | rare |
| misc-rare | 4/20 | 0.22 | folded: order-entry errors into *goods-price*, the rest into *Document*, commonly omitted |
| digital-content | 4/20 | 0.34 | rare |
| after-sales | 4/20 | 0.45 | rare (new key `facts.tr.after_sales`) |
| subscription | 3/20 | 0.77 | rare |
| marketplace | 2/20 | 0.12 | rare |
| loyalty | 1/20 | 0.59 | rare; placed after *exceptions*, as in tr-distance-sales |

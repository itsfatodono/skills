# tr-explicit-consent: merged section list

First batch: s01–s15 (5 large, 5 mid, 5 small; candidates 1–15 in pool order), written before any
saturation batch (`build/build.md` step 3). All 15 are valid; none was replaced. Region run `tr`,
kind `whole`: every section is KVKK content, so there is no *Regional content* split (step 4's
root/region rule does not apply). Each meaning below is fixed from here: change one only with a
dated note under *Changes*. One sample row can map to more than one id when it gives more than one
kind of fact (most consent texts are one long sentence, so s15 row 2 gives `controller`,
`notice-link`, `data-categories`, `purposes`, `recipients` and `consent-statement`). This is a
notice-like text, so drafting boilerplate that gives the reader no fact is not an id (PLAN.md
decision 44); see *Not sections*.

**A saturation sample is compared against the 19 ids in *Section ids*.**

## Section ids

| Id | Meaning | First-batch samples |
|---|---|---|
| intro | Opening request in the company's voice: the law consent is asked under, why consent is the basis (no adequacy decision, servers abroad), and the request itself. A title alone is document level. | s01 s05 s10 s12 |
| controller | The controller named as the party consent is given to, with any identity or contact details (trade name, brands, address, tax number, phone, e-mail). | all 15 |
| notice-link | The link to the separate Aydınlatma Metni: an acknowledgment that it was given and read (named, linked or summarised), or a statement that this text is separate from it (Tebliğ Art. 5(1)(f)). | s01 s02 s03 s04 s05 s06 s08 s09 s11 s12 s13 s14 s15 |
| purposes | The purposes the consent covers, listed or by reference to the notice. | all 15 |
| data-categories | The personal data the consent covers, by category or field, including whether special-category data is covered. | all 15 |
| recipients | Recipients inside Turkey the consent lets data go to, by name or category, and their purpose; transfers the person is told of that do not rest on the consent. | s01 s02 s03 s04 s06 s07 s08 s09 s11 s13 s14 s15 |
| transfer-abroad | Transfer abroad on consent (Art. 9): foreign recipients, countries, why data goes abroad, the data sent, the recipient's use limits. | s01 s02 s03 s04 s05 s06 s07 s09 s11 s12 s13 s14 |
| commercial-messages | Permission to send commercial electronic messages (Law 6563) given inside the text: channels, message types, İYS. Processing for sending messages, without permission wording, is `purposes`. | s06 s09 s10 |
| scope-limits | What the consent does not cover: excluded uses, purposes that need their own consent, permissions taken elsewhere (ETK approval, cookie banner), data held as processor. | s03 s09 s15 |
| voluntariness | Whether each consent is optional or required, and what refusing costs: nothing, an alternative channel, a feature, or no account. | s03 s05 s09 s15 |
| guardian | Consent given by a parent, guardian or legal representative for a minor or a person under guardianship. | s06 s08 |
| user-duties | What the person warrants or must do: that third parties' data they share was shared lawfully and with those persons informed. | s06 |
| retention | How long data under the consent is kept, where it is stored, and when it is deleted. | s03 |
| security | The controller's data-security undertaking. | s07 |
| withdrawal | That consent can be withdrawn, the channel, and the effect (forward only, a feature or the account stops). | s02 s03 s05 s09 s12 s13 s15 |
| rights | The Art. 11 rights referred to, reserved or where to use them, other than withdrawal (incl. the right to compensation). | s02 s07 s11 s15 |
| consent-records | How a given or refused consent is logged and proved (date, text version, source), and the copy the person can read before consenting. | s03 s09 |
| changes | How the text is updated and when it takes effect. | s12 |
| consent-statement | The affirmative declaration and how it is given: the consent wording the person adopts, a checkbox, an approve / do-not-approve choice per item, a signature block. | all 15 |

Not sections (document level, step 4): titles (every sample's row 1, s02's help-centre date and
channel labels); version and date lines (s03 row 1, s09 row 0); s04's page footer (uncontrolled
copy note) and s15's print button. Drafting boilerplate (decision 44), folded into the row it sits
in: defined short names ("Şirket", "Kanun", "Biz"); restated Art. 4 processing principles (s01 row
3's first two bullets); s01 row 6, which says processing follows the Art. 5 and 6 conditions;
strings of processing verbs (s04 A, s06 item 1: record, store, classify, keep); free-will formulas
("özgür irademle", "hiçbir etki altında kalmadan", "bilerek ve isteyerek"), counted as a pattern of
`consent-statement`.

**Outside the document** (`sources.md` rule 6): s06's site-wide KVKK notice and legal-warning
pop-ups; s08's signup drawer is kept as one `consent-statement` row (it shows how this text is
accepted) but its contract, notice and marketing boxes are other texts; s01's separate *Müşteri
Yurtdışı Açık Rıza Metni* and page footer modals.

## Mapping notes

- s01: row 2 to `intro` and `controller`; row 3 to `recipients`, `transfer-abroad` (one recipient
  list "yurtiçinde veya yurt dışında") and `purposes` (transfer purposes by business line); row 5
  ends with the non-consent bases (contract, legal obligation, legal claims, legitimate interest)
  listed as purposes: `purposes`, and an *Avoid*; row 7 repeats `controller` as a block; row 8 to
  `notice-link` and `consent-statement`.
- s02: row 2 names the controller inside the notice acknowledgment (`controller`, `notice-link`);
  row 4's commercial-message purpose has no permission wording, so `purposes`, not
  `commercial-messages`; row 6 (company note) to `withdrawal` and `rights`.
- s03: row 2 to `notice-link` (separate from the notice), `consent-statement` (unticked box) and
  `consent-records` (copy readable first); row 4 to `scope-limits` and `retention` (inputs
  discarded); row 5 (Gemini) to `transfer-abroad`, `retention` and `voluntariness`; rows 7 and 8
  (check-in, dietitian) are separate consents described here, to `recipients`, `retention`,
  `withdrawal` and `consent-records` (server-side record).
- s04: the acknowledgment (row 2) names the controller and restates the notice topics; A to
  `purposes` (by reference), `data-categories` (generic) and `consent-statement`; B to
  `recipients`; C to `transfer-abroad`; the signature block to `consent-statement`.
- s05: row 2 to `controller` and `intro` (Art. 9, no adequacy list as the reason); row 3 to
  `notice-link`, `purposes` and `transfer-abroad`; rows 4, 5 and 8 to `voluntariness` (no pressure,
  no detriment, call-centre alternative, complaint e-mail); row 5 also `consent-statement` and
  `withdrawal`; row 7 to `transfer-abroad` and `consent-statement`.
- s06: rows 2–3 (blanket advance consent) to `notice-link`, `controller` and `consent-statement`;
  row 4 to `data-categories`; row 5 ("I know" ministry transfers, not consent) to `recipients` and
  `purposes`; items 2, 3 and 7 to `transfer-abroad` (2 regular, 3 and 7 per case); item 6 to
  `commercial-messages`; row 13 (family disclosure) to `recipients`; row 14 to `user-duties`; row
  15 to `consent-statement` and `guardian` (parent of a child patient signs).
- s07: row 2 to `controller`, `data-categories` (all data obtained, no categories), `purposes`,
  `recipients`, `transfer-abroad` and `consent-statement`; row 3 to `security` and `rights`
  (compensation). Its "İlgili bilgilendirme kapsamında" only implies a notice: no `notice-link`.
- s08: row 2 to `controller`, `notice-link`, `purposes`, `data-categories`, `recipients` (domestic
  only) and `consent-statement`; row 3 to `guardian`; row 4 (signup checkbox) to
  `consent-statement`.
- s09: row 1 to `notice-link`, `voluntariness` and `scope-limits` (web analytics via the cookie
  banner); row 2 names the brand (`controller`) and is `consent-statement`; item 1 to `purposes`,
  `data-categories` and `recipients` (Gemini named; abroad is item 3); item 3 to
  `transfer-abroad`, `voluntariness` and `withdrawal` (account closes); item 4 to
  `commercial-messages`; row 8 to `consent-records`.
- s10: row 2 to `intro` (ETK law) and `controller`; row 3 names data only inside purposes
  (`data-categories`); row 4 to `commercial-messages` and `consent-statement`.
- s11: row 3's "Art. 11 rights reserved" to `rights`; rows 3–4 are one sentence.
- s12: row 6 to `changes` (takes effect on approval; unilateral update right).
- s13: the lead-in "consent can be withdrawn" (row 2) to `withdrawal`; rows 4–5 are written as
  notice ("işlendiğini", "aktarıldığını bildiğimi"), mapped by content.
- s14: row 3's ETK calls and e-mails are a processing purpose, not a permission: `purposes`.
- s15: row 3 to `voluntariness`, `withdrawal` and `rights`; row 4 to `scope-limits`.
- s16: rows 1–2 are titles (document level); the WhatsApp notice above them on the same page is
  another text (rule 6). Row 3 to `controller` (with address) and `notice-link`; row 4 to
  `data-categories` and `purposes` (both by reference to the notice, storage added),
  `transfer-abroad` (WhatsApp LLC, Art. 9) and `consent-statement`. Its closing "informed,
  understood, learned my rights" formula is drafting, not `rights`. No domestic recipient.
- s17: rows 1–2 are titles; row 3 is one sentence: `controller`, `notice-link`, `purposes`,
  `data-categories` ("current or future-updated" data, none listed) and `consent-statement`. The
  KVKK citation inside the sentence is not an `intro` (as in s11–s15).
- s18: row 1 title and salutation (document level); row 2 to `intro` (why consent is asked) and
  `voluntariness` (the relationship does not depend on it); row 3 to `controller` (address,
  chamber registry number), `withdrawal` (the right only) and `transfer-abroad` (contracted cloud
  providers abroad); row 4 (data processed under Art. 5–6 without consent, consent only for the
  rest) to `scope-limits`; row 5 to `data-categories`; row 6 to `notice-link` and
  `consent-statement` (RIZAM VARDIR / YOKTUR block); row 7's date is document level. **No
  purpose anywhere:** no `purposes` row.
- s19: row 1 title ("Aydınlatma ve Rıza Metni"); row 2 (one sentence) to `controller`,
  `purposes`, `data-categories`, `recipients`, `transfer-abroad` (domestic and foreign in one
  clause), `retention`, `withdrawal` (reject step in each message; required communications
  continue) and `commercial-messages` (6563, channels); row 3 to `consent-statement`. The 6563
  citation inside the sentence is not an `intro`. No `notice-link`: the text calls itself the
  notice too.
- s20: row 1 title; row 2 to `controller`, `notice-link` and `data-categories` (by reference);
  row 3 to `purposes`; row 4 to `recipients` (group companies, partners, suppliers; abroad not
  mentioned); row 5 to `consent-statement` (one "onay veriyorum" for both bullets); row 6 footer
  block to `controller`; its version code is document level.

## Section map

First-row order of ids per sample (the basis of every count and median below).

```
s01 intro controller recipients transfer-abroad purposes data-categories notice-link consent-statement
s02 controller notice-link data-categories purposes recipients transfer-abroad consent-statement withdrawal rights
s03 notice-link consent-statement consent-records controller data-categories purposes scope-limits retention transfer-abroad voluntariness recipients withdrawal
s04 controller notice-link purposes data-categories consent-statement recipients transfer-abroad
s05 controller intro notice-link purposes transfer-abroad voluntariness consent-statement withdrawal data-categories
s06 notice-link controller consent-statement data-categories recipients purposes transfer-abroad commercial-messages user-duties guardian
s07 controller data-categories purposes recipients transfer-abroad consent-statement security rights
s08 controller notice-link purposes data-categories recipients consent-statement guardian
s09 notice-link voluntariness scope-limits controller consent-statement purposes data-categories recipients transfer-abroad withdrawal commercial-messages consent-records
s10 intro controller purposes data-categories commercial-messages consent-statement
s11 controller notice-link purposes data-categories rights recipients transfer-abroad consent-statement
s12 intro controller notice-link purposes data-categories transfer-abroad consent-statement withdrawal changes
s13 withdrawal controller notice-link data-categories purposes recipients transfer-abroad consent-statement
s14 controller notice-link purposes data-categories recipients transfer-abroad consent-statement
s15 controller notice-link data-categories purposes recipients consent-statement voluntariness withdrawal rights scope-limits
s16 controller notice-link data-categories purposes transfer-abroad consent-statement
s17 controller notice-link purposes data-categories consent-statement
s18 intro voluntariness controller withdrawal transfer-abroad scope-limits data-categories notice-link consent-statement
s19 controller purposes data-categories recipients transfer-abroad retention withdrawal commercial-messages consent-statement
s20 controller notice-link data-categories purposes recipients consent-statement
```

## Merged list (s01–s20)

Median position is the first row's rank divided by the sample's id count less one (0 = first,
1 = last). Tiers per `formats/skeleton-format.md` (core ≥80% = 16+/20, common 40–79% = 8–15, rare
<40% = 7 or fewer). *Commonly omitted* = fewer than 20% (≤3/20). Median ids per sample: 8. The
*s01–s15* column is the first-batch count.

| Id | Count | s01–s15 | Tier | Median pos. | Note |
|---|---|---|---|---|---|
| intro | 5/20 | 4/15 | rare | 0.00 | folded into `controller` in the skeleton (drafting no fact decides) |
| controller | 20/20 | 15/15 | core | 0.00 | 15/20 name it only in passing |
| notice-link | 17/20 | 13/15 | core | 0.17 | Tebliğ Art. 5(1)(f); carries an *Avoid* (s19) |
| purposes | 19/20 | 15/15 | core | 0.38 | carries two *Avoid*; s18 gives no purpose at all |
| data-categories | 20/20 | 15/15 | core | 0.46 | |
| scope-limits | 4/20 | 3/15 | rare | 0.59 | |
| consent-records | 2/20 | 2/15 | rare | 0.59 | commonly omitted |
| voluntariness | 5/20 | 4/15 | rare | 0.62 | carries an *Avoid* |
| retention | 2/20 | 1/15 | rare | 0.63 | commonly omitted |
| recipients | 14/20 | 12/15 | common | 0.65 | was core; s16 s17 s18 name no domestic recipient |
| transfer-abroad | 15/20 | 12/15 | common | 0.67 | was core; every one of the 15 rests a regular transfer on consent: *Avoid* |
| withdrawal | 9/20 | 7/15 | common | 0.82 | 11/20 silent |
| commercial-messages | 4/20 | 3/15 | rare | 0.84 | item 51's subject |
| security | 1/20 | 1/15 | rare | 0.86 | commonly omitted |
| user-duties | 1/20 | 1/15 | rare | 0.89 | commonly omitted |
| consent-statement | 20/20 | 15/15 | core | 0.92 | |
| rights | 4/20 | 4/15 | rare | 0.94 | folded into `withdrawal` in the skeleton |
| guardian | 2/20 | 2/15 | rare | 1.00 | commonly omitted |
| changes | 1/20 | 1/15 | rare | 1.00 | commonly omitted |

By count: 5 core, 3 common, 11 rare (19 ids). Since the first batch, `recipients` (12/15 →
14/20) and `transfer-abroad` (12/15 → 15/20) moved from core to common; `consent-statement`'s
median moved later (0.75 → 0.92) because the short saturation texts end on it. The core is still
who, what data, what for, the notice link and the declaration. `transfer-abroad`'s count still
shows practice the law now rejects, not a default (see *Avoid*); its tier does not change what
the skeleton does, since its *Applies when* limits it to occasional transfers.

## Patterns (s01–s15)

- **controller:** 15/15 name it; 13/15 only in passing (title, opening or acknowledgment
  sentence). 2/15 give an address or block (s01 with tax number, phone, fax, e-mail; s13 address);
  4/15 give only an e-mail, for withdrawal or complaints (s03 s05 s09 s15). s09 names the brand,
  never the legal person; s03 names the sole trader; s13 groups five brands as one controller.
- **notice-link:** 13/15. 10/15 a first-person "I read / was informed by the [named] notice" (s01
  s02 s04 s06 s08 s11 s12 s13 s14 s15); s05 in company voice ("the notice we gave you before");
  s03 and s09 say this text is separate from the notice. 3/15 restate the Art. 10 topics as
  received (s04 s11 s14; s04 includes the risks of occasional transfer abroad and a handed-over
  copy). s07 only implies a notice, s10 has none.
- **purposes:** 7/15 inline in one sentence (s05 s07 s11 s12 s13 s14 s15), 5/15 a bulleted or
  numbered list (s01 s02 s03 s08 s10), 3/15 one purpose per consent item (s04 s06 s09); s04 gives
  them only by reference to the notice. By scope: 6/15 mix service and marketing (s01 s02 s04 s07
  s09 s12), 4/15 marketing only (s10 s13 s14 s15), 4/15 health or special-category data (s03 s06
  s08 s11), 1/15 a single transfer (s05). s01 says "not limited to" for both data and purposes.
- **data-categories:** 11/15 name categories or fields (s01 s02 s03 s05 s06 s08 s09 s11 s12 s14
  s15), 2/15 only inside purposes (s10 s13), 2/15 only generically ("kişisel verilerim", "personal
  and special-category data": s04 s07). 6/15 cover special-category data (s02 biometric, s03 s04
  s06 s08 s11 health).
- **recipients:** 12/15, by category in 10; s03 (a dietitian the user picks) and s09 (Google
  Gemini) name one. s06 adds a separate consent for named family members with blank fields, and
  states legally required transfers as "I know", not as consent.
- **transfer-abroad:** 12/15. 9/12 put it in the same consent as processing or domestic sharing
  (s01 s02 s05 s07 s11 s12 s13 s14, s03 in the same checkbox); 3/12 give it its own choice (s04 C,
  s06 items 2, 3, 7, s09 item 3). 3/12 name the foreign recipient (s03 Google LLC, s05 Zendesk Inc.,
  s12 Elektraweb), 9/12 give categories only (group companies, correspondent banks, suppliers,
  "social media and search engine companies"). 2/12 name countries (s05 US; s09 Germany, EU, US).
  3/12 cite Art. 9 (s02 s05 s09); 3/12 say why data goes abroad (s05 no adequacy decision and the
  vendor abroad, s09 and s12 servers abroad). **0/12 state the possible risks** that Art. 9(6)(a)
  requires the person to be told (s04 says its notice did). Only s06 items 3 and 7 (second opinion,
  consultation or test abroad, per case) describe occasional transfers.
- **consent-statement:** 15/15. 14/15 first-person declarations the person adopts ("açık rıza
  veriyorum", "muvafakat ederim"); s05 defines what ticking the box means. Mechanism shown: 4/15
  a checkbox (s03 unticked, s05 before "Gönder", s08 a separate unticked box at signup, s09 one ☐
  per item), 2/15 a paper approve / do-not-approve choice with a signature block (s04 s06), 9/15
  none on the page. Granularity: 4/15 a choice per item (s03 s04 s06 s09), 11/15 one acceptance
  for everything. 8/15 add a free-will formula (s01 s09 s10 s11 s12 s14 s15, s05 in company voice);
  2/15 the triple "kabul, beyan ve taahhüt" (s06 s13).
- **withdrawal:** 7/15; 8/15 silent (s01 s04 s06 s07 s08 s10 s11 s14). Channel: 4/15 name one (s03
  in-app settings and e-mail, s09 e-mail and İYS or message link, s15 e-mail, s02 the website); s12
  points to the notice's channels, s05 "electronic channels", s13 states the right only. Effect:
  2/15 forward only (s03 s09); s09 says withdrawing item 3 closes the account; s03 says withdrawal
  does not need account deletion.
- **voluntariness:** 4/15. 3/15 say refusing costs nothing or only the feature (s03 s05 s15); s05
  offers the call centre as the alternative and an e-mail to report pressure; s09 labels each item
  optional or required.
- **commercial-messages:** 3/15 (s06 item 6, joined with appointment reminders; s09 item 4 with its
  own box and İYS; s10 in the same sentence as the marketing consent). s15 says the ETK approval
  is taken separately; s02 and s14 process data for e-messages with no permission wording.
- **rights:** 4/15; s07 reserves the right to compensation, s11 reserves the Art. 11 rights, s15
  says they were explained, s02 points to the website.

### Avoid candidates (decisions 47, 50)

Patterns the guidance calls wrong; never a Default, whatever the count. Every id and pattern above
was checked against: the Board's page "Açık Rıza Alırken Dikkat Edilecek Hususlar"
(https://www.kvkk.gov.tr/Icerik/2037/Acik-Riza-Alirken-Dikkat-Edilecek-Hususlar, published
2018-01-30, read 2026-10-27); the Board decision summary "Hizmetin Açık Rıza Şartına Bağlanması"
(https://www.kvkk.gov.tr/Icerik/5412/Acik-Rizanin-Hizmet-Sartina-Baglanmasi); KVKK Art. 9 as
amended by Law 7499 (in force 2024-06-01) and Art. 6(3) as amended; the Aydınlatma Tebliğ Art. 5(1).

| Id | Pattern | Count | Guidance |
|---|---|---|---|
| transfer-abroad | Regular transfer abroad on explicit consent (group companies, suppliers, hosting, SaaS vendors) | 12/15 → **15/20** with s16 (WhatsApp LLC for a support line), s18 (contracted cloud providers) and s19 (suppliers, ad networks "yurt içinde ve dışında") (s01 s02 s03 s04 s05 s06 s07 s09 s11 s12 s13 s14 s16 s18 s19: every sample with the id; s06's items 3 and 7 are per-case and fine, its item 2 is regular) | KVKK Art. 9(6)(a) as amended by Law 7499: consent only "arızi olmak kaydıyla", where no adequacy decision and no Art. 9(4) safeguard (standard contract, BCR, undertaking) can be used, and only after the person is told the possible risks. s05 still argues from the pre-7499 text ("no adequate countries announced"). s03 frames its Gemini transfer as consent renewed on each use; the transfer is still a standing processor flow. |
| purposes | Consent asked for processing that has another Art. 5/6 basis | 5/15 → **6/20** with s19 (information on purchases and contractual and legal matters, which contract and legal obligation cover) (s01 account, invoicing, delivery and the contract, legal-obligation and legitimate-interest bases themselves; s02 KYC, identity and biometric checks, financial transactions and contract performance; s06 diagnosis, treatment, appointments and insurer billing of health data, which Art. 6(3)(e) covers, item 4 even says the transfer is "zorunlu"; s07 risk management and reporting at a bank; s12 reservations, guest support and sales support) | Decision "Hizmetin Açık Rıza Şartına Bağlanması" (Icerik/5412): where another condition exists, asking consent misleads the person and is an abuse of right, contrary to Art. 4. Tebliğ Art. 5(1)(j): no misleading information. Borderline, not counted: s08 (health data for audit, ethics and archiving, where no Art. 6(3) condition clearly fits), s11 (insurer's health data for claims; Art. 6(3)(e) "finansmanı" may cover it), s13 (CRM and customer satisfaction inside a marketing list). |
| purposes | Blanket consent: no specific purpose or processing | 3/15 → **4/20** with s18 (no purpose anywhere; consent to processing and transfer of seven data categories "in the frame of this text") (s01 data and purposes "sınırlı olmamak üzere"; s04 consents to all processing, domestic and foreign transfer of all personal and special-category data "within the notice", naming none; s06 rows 2–3, an advance permission ("peşinen izin") to every processing of "her türlü" personal and health data, before the itemised choices) | Icerik/2037: consent not limited to a specific subject and to the processing concerned is a "battaniye rıza" and legally invalid ("her türlü … veri işleme faaliyeti"). Borderline, not counted: s07 (all data obtained for the bank's products, one consent for nine purposes and every recipient group); s17 (named marketing purposes, but "current or future-updated" data with none listed); s19 (all personal data in the customer's contract, and third parties the recipients choose). |
| voluntariness | Consent made a condition of the service | 1/15 → **1/20** (s09 items 2 and 3: "uygulama için gereklidir", no account without them, withdrawal closes the account) | Icerik/5412: making the service conditional on consent vitiates the consent. Icerik/2037: consent must be "özgür iradeyle açıklanan". Not determinable: s08's signup button starts disabled, but the HTML does not show whether its consent box is required; s02 takes consent in the signup and KYC flow; s16 says nothing of refusal, and the WhatsApp line is the channel itself. |
| notice-link | Consent bundled with the notice: one text, one acceptance | **1/20** (s19, titled "Aydınlatma ve Rıza Metni": controller, purposes, recipients and opt-out folded into the consent sentence, no separate notice referred to) | Aydınlatma Yükümlülüğü Tebliğ Art. 5(1)(f): where processing rests on explicit consent, informing and taking consent are done separately. Borderline, not counted: s16 (notice and consent on one page, but each under its own label and title, the consent naming the notice). |
| consent-statement | One acceptance for several purposes | **13/20** (s01 s02 s07 s08 s10 s11 s12 s13 s14 s15 s17 s19 s20: more than one purpose, or processing plus sharing or transfer abroad, under one acceptance). Not counted: the 4 with a choice per item (s03 s04 s06 s09); s05 (one purpose, one transfer); s16 (one transfer for the support line's purposes; borderline); s18 (no purpose; counted as blanket) | The Board's guide "Açık Rıza" (KVKK Yayınları No: 98, June 2025, p. 10, https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/e3c6aa10-9de4-46f8-9b51-71bcf07c09b5.pdf, read 2026-10-27): "her amaç için ayrı bir açık rıza alınması gerekir", and a secondary operation such as a transfer abroad needs its own consent. |

Looked for, not found or not an *Avoid*:
- **Consent bundled with the notice** (Tebliğ Art. 5(1)(f)): found in the saturation batch (s19), now an *Avoid* row above. In s01–s15: 0/15 is one text with one acceptance
  for both. Every sample points to a separate notice except s07 (implied) and s10. Borderline, not
  counted: s01 and s13 restate notice content inside the consent ("bildiririz", "işlendiğini …
  bildiğimi"), and s06 shows its notice as a pop-up on the same page.
- **Consent bundled with the contract:** 0/15. s08's signup puts contract acceptance and the
  notice acknowledgment in one box, but this consent has its own unticked box; that box is the
  notice's matter, not this text's.
- **No way to withdraw:** 0/20 deny withdrawal. 8/15 are silent on it (11/20 with s16 s17 s20). Icerik/2037 states the
  right and its forward effect but does not require the text to state it, so silence is a pattern,
  not an *Avoid* (owner may decide otherwise). s09's account closure on withdrawing item 3 is
  counted under conditioning.
- **Transfer risks not stated:** 0/12 state them in the consent text (0/15 with s16 s18 s19); Art. 9(6)(a) needs them told,
  but the notice may do it (s04 says its notice did). Not judgeable from the consent text alone:
  a pattern, and a point the skeleton should cover.
- **ETK permission inside a KVKK consent** (s06 s09 s10, and s19, where the whole text is an ETK
  muvafakatname with KVKK processing and transfer folded in): none of the four sources calls it wrong;
  a pattern for item 51.

## Patterns: saturation batch (s16–s20)

The first-batch patterns above stand; these are the changes over s01–s20, the counts the skeleton
uses. s13 and s17 share one marketing-purposes string (*Copies*); it counts once where noted.

- **controller:** 15/20 only in passing; 5/20 give an address or block (s01 s13, s16 address, s18
  address and chamber registry number, s20 a letterhead footer with registry, MERSIS, KEP, phone).
  `intro` 5/20 (s18 adds why consent is asked).
- **notice-link:** 17/20. First-person acknowledgment of a named notice 14/20 (adds s16 s17 s18
  s20; s17 and s20 take the data scope from it); s05 company voice; s03 s09 separate. Bundled with
  the notice 1/20 (s19, *Avoid*); s07 implied, s10 none.
- **purposes:** 19/20 (s18 none). Inline in one sentence 10/20 (adds s16 s17 s19), a list 6/20
  (adds s20), one per item 3/20; by reference to the notice only 2/20 (s04 s16). Scope: marketing
  only 6/20 (adds s17 s20; s13 and s17 share one string), service and marketing 7/20 (adds s19),
  health 4/20, a single transfer 2/20 (s05, s16).
- **data-categories:** 20/20. Categories or fields 13/20 (adds s18 a seven-category list, s19
  contact fields), only inside purposes 2/20, generic or by reference to the notice 5/20 (adds s16
  s17 s20). Special-category 6/20.
- **recipients:** 14/20, by category in 12 (adds s19 s20); s20's group companies and partners with
  no word on where they are.
- **transfer-abroad:** 15/20. Same consent as processing 11/20 (adds s18 s19); a choice or text of
  its own 4/20 (adds s16, a consent only for transfer to WhatsApp LLC). Named recipient 4/20 (adds
  s16), categories 11/20; countries 2/20; Art. 9 cited 4/20 (adds s16); reason given 3/20. Risks
  0/15. Occasional transfers: still only s06 items 3 and 7.
- **consent-statement:** 20/20; first person 19/20. Mechanism: checkbox 4/20, a paper choice with
  name and date or signature 3/20 (adds s18 RIZAM VARDIR / YOKTUR), none on the page 13/20.
  Granularity: per item 4/20, one acceptance 16/20 (s20 joins two bullets under one verb). Free-will
  formula 10/20 (adds s18 s19).
- **withdrawal:** 9/20 (adds s18 the right only, s19 the reject step in each message and changing
  preferences); 11/20 silent. Channel named 5/20; forward effect 2/20; s19 says legally required
  communications continue.
- **voluntariness:** 5/20; refusing costs nothing 4/20 (adds s18: the legal relationship does not
  depend on consent).
- **scope-limits:** 4/20 (adds s18: some data is processed under Art. 5–6 without consent; consent
  covers only the rest).
- **commercial-messages:** 4/20 (adds s19: SMS, auto-dialled calls, social media, ad networks,
  e-mail). **retention:** 2/20 (adds s19: a period within the legal maximum).

## Document level (s01–s20)

Over s01–s20 (the first-batch notes below stay for the record):
- **Words:** median about 280 (range 100–1,260). Large about 275, mid about 205, small about 425.
- **Carrier:** 16/20 web pages, 3/20 PDFs (s04 a signable form; s19 a Word export; s20 on
  letterhead), s06 a paper form on an HTML page.
- **Title:** subject named 8/20 (adds s16 WhatsApp transfer abroad); audience 4/20 (adds s18
  users); s19 calls itself "Aydınlatma ve Rıza Metni".
- **Structure:** unheaded paragraphs 12/20 (adds s16 s17 s19), items or bullets 5/20 (adds s20),
  unheaded paragraphs with a bulleted data list 2/20 (s05 s18), s03 headed sections.
- **Recurring elements:** a date or version 5/20 (adds s18 "Son Güncelleme", s20 a version code);
  address, e-mail or phone 9/20 (adds s16 s18 s20); a signature or name-and-date block 3/20 (adds
  s18); leftovers or broken clauses 5/20 (adds s16 an editor's "[BY1]" mark in the notice above
  the consent, s19 contact details "stated below" that are absent).

## Document level (s01–s15)

- **Words:** median about 280 (range 150–1,260). Large about 275, mid about 300, small about 450:
  as in the notice, small companies write the longest texts (s06 1,260, s03 1,060), and banks the
  shortest (s07 164, s10 152).
- **Carrier:** 13/15 web pages; s04 a signable PDF form, s06 a paper patient form published as an
  HTML page. s08's page also holds the signup drawer.
- **Title:** 15/15 "Açık Rıza Metni / Beyanı / Onay Formu". 7/15 name the subject (s03 health
  data, s05 live-support transfer abroad, s08 special-category data, s10 commercial communication
  and marketing, s13 marketing data, s14 contact, s15 marketing); 3/15 the audience
  (s02 customers, s04 product or service customers, s06 patients and relatives).
- **Structure:** 9/15 one to three unheaded paragraphs, usually one long sentence ending in the
  consent verb (s01 s02 s07 s10 s11 s12 s13 s14 s15); 4/15 numbered or lettered consent items (s04
  s06 s08 s09); s03 nine headed sections; s05 unheaded paragraphs with a bulleted data list.
- **Register:** formal legal Turkish in 13/15; 14/15 in the data subject's first person, often after
  a company-voice opening (s01 s05 s12); s03 and s09 plain, short sentences.
- **Recurring elements:** a date 3/15 (s02 help-centre date, s03 and s09 with a version; s03's
  version id still ends in "draft.8" beside "in force"), none 12/15; an address, e-mail or phone in
  6/15 (s01 s03 s05 s09 s13 s15); a signature block 2/15 (s04 s06). Typos or
  broken clauses 3/15 (s06 unfinished sentence, s13 "İLİŞKİN İLİŞKİN" and "akaktarılmasına", s12
  calls itself a "KVKK Politika").
- **Not sections:** see the note under *Section ids*.

## Facts preview

Facts each id needs (step 5 comes later; no facts file is edited here). Existing keys first, from
`helpers/facts-schema.md` and `regions/tr/facts.md`. The consent rows of `facts.tr.legal_bases` (5/1 and
6/3-a) decide which purposes this text covers; the `occasional` rows of `facts.tr.transfer_tools`
decide whether `transfer-abroad` applies at all.

| Id | Facts | Keys |
|---|---|---|
| intro | whom the text addresses; which product, channel or feature | `facts.data.subject_categories`, `facts.product.services_in_scope`, `facts.product.name` |
| controller | legal name, brand, address, contacts, registry ids | `facts.company.legal_name`, `facts.product.name`, `facts.company.address`, `facts.company.contact_email`, `facts.company.phone`, `facts.tr.seller_registry` |
| notice-link | the notice's title and URL | `facts.tr.kvkk_notice_url`, `facts.company.published_policies` |
| purposes | purposes resting on consent | `facts.data.purposes` filtered by `facts.tr.legal_bases` (5/1, 6/3-a); `facts.product.features`, `facts.product.ai_features` |
| data-categories | data per consented purpose; special-category data | `facts.data.collected`, `facts.data.sensitive` |
| recipients | domestic recipients of consented data | `facts.processors.list`, `facts.data.other_recipients`, `facts.company.group_companies` |
| transfer-abroad | recipient, country, data and reason per occasional transfer; the risks (derived from the country and the missing tool) | `facts.tr.transfer_tools` (rows with tool `occasional` only), `facts.data.storage_locations` |
| commercial-messages | channels and whether marketing messages are sent | `facts.marketing.email`, `facts.marketing.sms`, `facts.marketing.push` (İYS left to item 51/52, as in `tr-kvkk-notice`) |
| scope-limits | permissions taken elsewhere; processor-held data | `facts.company.published_policies`, `facts.data.cookie_controls`, `facts.company.acts_as_processor` |
| voluntariness | per consent: what refusing turns off, the alternative | **`facts.tr.consent_capture`** |
| guardian | minors served; who consents for them | `facts.product.min_age`, `facts.product.child_directed` |
| user-duties | none (drafting) | — |
| retention | periods for consented data | `facts.data.retention` |
| security | measures | `facts.data.security_measures` |
| withdrawal | where and how consent is withdrawn; effect | `facts.users.rights_channels`, `facts.data.cookie_controls`, **`facts.tr.consent_capture`** |
| rights | where rights are used | `facts.users.rights_channels` |
| consent-records | logging of consent and refusal | **`facts.tr.consent_capture`** |
| changes | how changes are announced | `facts.company.change_notice` |
| consent-statement | where and how each consent is taken; one choice per item | **`facts.tr.consent_capture`** |

Proposed key (1): `facts.tr.consent_capture`: for each consent the company asks, where it is
taken (signup, first use of a feature, a web form, settings, paper, a call), whether it has its
own unticked box, what refusing or withdrawing turns off and the alternative offered, the in-product
withdrawal path, and whether consent and refusal are logged with date, text version and source.
Nothing fits now: `facts.tr.acceptance_mechanism` is the contract's acceptance, and
`facts.data.cookie_controls` and `facts.data.telemetry_controls` cover only cookies and telemetry.
Proposed shared key: `facts.data.consent_capture` (the same fact under GDPR consent).

## Copies (rule 4)

None in s01–s15. Compared on the `raw/` texts with 6-word shingles (share of the smaller text's
shingles): the highest pair is s08/s12 at 0.04 (the standard phrase "kişisel verilerin işlenmesine
… açık rıza veriyorum" and statutory wording), then s04/s11 at 0.04; every other pair is under
0.03. The partial overlaps in `candidates.md` (TürkKEP/Tuzcular, Tekzen/E-Ticaret360, Gedik/
Emlaksitem, the two clinics) each have one member outside the first batch; check them when that
member is judged.

Saturation batch (s16–s20, same method): no copies. One partial overlap the pool did not list:
s13 (İpekyol) and s17 (Lufian) share 0.33 of s17's shingles, one fashion-retail marketing-purposes
string (offers, campaigns, contests, segmentation, profiling, ads on third-party media, customer
experience). Their tables differ (s13 adds an address, withdrawal, domestic and foreign
recipients; s17 has none of them), so both are samples and the string counts once in patterns.
Every other pair with s16–s20 is under 0.04. The listed overlaps' other members (Tuzcular,
E-Ticaret360, Emlaksitem, the clinics) were not extracted.

## First-batch qualification

All 15 valid. Borderline ones:

| Sample | Verdict | Why |
|---|---|---|
| s04 Emaa Sigorta (large) | valid | the general form from a hub of six PDF forms (rule 6); purposes and recipients only by reference to the notice. |
| s06 Hande Arda (small) | valid | a paper patient form on a web page; the notice pop-ups are outside the document; one category list lost its labels in the source, not in the extraction. |
| s07 Ziraat Bankası (large) | valid; **a short text, not a thin extraction** | 3 rows because the page holds a title and two paragraphs. Re-fetched 2026-10-27: the page body is the same 164 words as `raw/s07.txt`, with only site chrome and links to the bank's other privacy texts around it. No checkbox or form is on the page. |
| s10 Tekzen (large, `etk`) | valid | mostly an ETK permission, but it also asks KVKK consent for marketing processing; its ETK paragraph is shared with E-Ticaret360 (pool row 60). |
| s15 Cari Plus (small) | valid | 153 words, matching the raw text; short, not thin. |

Other short samples are short on the page too: s10 (152 words), s11 (177), s12 (200), s14 (206);
each extraction's word count matches its raw text.

## Saturation

A sample is new only when it has a section whose content fits no id in *Section ids*; how it
writes a known id never makes it new (`build/build.md` step 3). Stop at 5 non-new in a row. Copies
(rule 4) are not judged. Drafting boilerplate never makes a sample new (decision 44).

Batch 1 in pool order: s16–s20 (candidates 16–20: large, mid, small, large, mid; tags
`transfer-consent`, none, `transfer-consent`, `etk, transfer-consent`, none). All valid: each is
the company's customer or user consent text in Turkish, and each company is its own group (rule
5, checked over the 63 in `candidates.md`). s16 is the consent part of a page that also holds the
WhatsApp notice, and s18 the user tab of a two-tab page (rule 6). s17 names an operating company
(NE-SAÇ Tekstil) that differs from the candidate row; it is still the brand's own text. s19 is the
second and last `etk` pick allowed in rows 1–27. No copies (*Copies*).

| Sample | Verdict | Why |
|---|---|---|
| s16 Penti (large) | not new | consent only for a regular transfer abroad (WhatsApp LLC) on a support line: `controller` with address, `notice-link`, `data-categories` and `purposes` by reference, `transfer-abroad` (*Avoid*), `consent-statement`. 1 non-new |
| s17 Lufian (mid) | not new | one sentence: `controller`, `notice-link`, marketing `purposes` (string shared with s13), `data-categories` by reference, `consent-statement`. 2 |
| s18 Look Bubble (small) | not new | the richest of the batch (7 rows, 9 ids), all known: `intro`, `voluntariness`, `withdrawal`, `scope-limits` (consent only for data no Art. 5–6 condition covers), a data list, cloud providers abroad (`transfer-abroad`, *Avoid*); no purpose at all (blanket *Avoid*). 3 |
| s19 Bauhaus (large, `etk`) | not new | one sentence folding notice, ETK permission, processing and foreign transfer together: `commercial-messages`, `retention`, `withdrawal`, `recipients`, `transfer-abroad`; three *Avoid* (bundled with the notice, other-basis purposes, regular transfer). 4 |
| s20 T.O.M. Bank (mid) | not new | `controller` (text and footer), `notice-link`, `data-categories` by reference, marketing `purposes`, `recipients`, one `consent-statement` for two bullets. 5 |

**Stop (step-3 rule):** 5 non-new in a row (s16–s20): `saturated: true` at s20 with 20 samples
(7 large, 7 mid, 6 small). No id was added after the first batch: 19 ids throughout.

**Reservation.** The batch is thin: three of the five are under 140 words (s16 131, s17 101, s20
139) and hit 5–6 ids against a median of 8, so they are weak tests for a new id. The rare tail is
recurring, not growing: no id is new, and `intro`, `scope-limits`, `voluntariness`, `retention`,
`withdrawal` and `commercial-messages` each gained a sample. The first batch was thin the same way
(short single-sentence texts are this document's typical shape: 12/20 are one to three unheaded
paragraphs), so this is the population, not a skew of the batch. I see no reason for an extra
batch; the chief of staff may order one (s21–s25: pool rows 21 small, 22 large, 23 mid, 24 small,
25 mid).

## Changes

- 2026-10-27 (saturation batch 1, s16–s20): no id added and no meaning changed. Counts moved to
  s01–s20: `recipients` core → common (14/20), `transfer-abroad` core → common (15/20; the earlier
  merge's *Applies when* and Default for it stand). *Avoid* counts: regular transfer on consent
  12/15 → 15/20 (s16 s18 s19), other-basis purposes 5/15 → 6/20 (s19), blanket consent 3/15 →
  4/20 (s18), conditioning 1/20. New *Avoid* row: consent bundled with the notice 1/20 (s19,
  Tebliğ Art. 5(1)(f)), moved from *Looked for, not found*.
- 2026-10-27 (step 4): `intro` (5/20) is folded into `controller` and `rights` (4/20) into
  `withdrawal` as patterns in the skeleton (drafting no fact decides; `skeleton-format.md`
  rare-section rule). Both stay ids here. The skeleton has 17 sections: 5 core, 3 common, 9 rare.
- 2026-10-27 (chief of staff's decisions): (1) `transfer-abroad` is common by count (15/20); its
  fixed *Applies when* (occasional transfers only) and Default (s06 per case) stay. (2) No extra
  batch: saturated at s20, `sample_count: 20`. (3) Both writer choices kept, each with a sourced
  reason in the skeleton, verified against the source text on 2026-10-27:
  - one unticked choice per consent (`consent-statement`): the Board's guide "Açık Rıza" (KVKK
    Yayınları No: 98, June 2025, p. 10: "her amaç için ayrı bir açık rıza alınması gerekir", and
    separately for a secondary operation such as a transfer abroad;
    https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/e3c6aa10-9de4-46f8-9b51-71bcf07c09b5.pdf)
    and "Doğru Bilinen Yanlışlar -II-" (No: 66, March 2026, question 8, opt-in only, citing
    decision 2020/173;
    https://kvkk.gov.tr/SharedFolderServer/CMSFiles/d077b665-66b6-4615-975a-249f93e084ba.pdf).
    Directly supported.
  - `withdrawal` *Applies when: always*: Icerik/2037 (withdrawal at any time, forward effect),
    "Doğru Bilinen Yanlışlar -II-" questions 6–7 (forward effect; withdrawing as easy as
    consenting) and "Açık Rıza" p. 11 (the person must know the consequences of consenting). No
    source says in terms that the text must state the right; the skeleton says so. Supported by
    inference, not by an express rule.
- 2026-10-27 (chief of staff's decision, decisions 47/50): one acceptance for several purposes
  becomes an *Avoid* on `consent-statement`, 13/20 (only texts covering more than one purpose
  with a single acceptance; s05, s16 and s18 excluded, see the *Avoid* table). The writer
  instruction (one unticked choice per consent) stays. `withdrawal` *Applies when: always* stays
  with its inference stated.

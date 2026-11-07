# data-subject-request (`tr` block): merged section list

First batch: s01–s15 = candidates 1–15 in pool order (5 large, 5 mid, 5 small), all valid, none
replaced (`candidates.md`). By owner decision (2026-10-27) there is no further extraction or
collection, so no saturation batch was run and the block is `saturated: false` (see *Saturation*).
Region run per `build/build.md` *Region run*, part `block` of the root item (PLAN.md decisions 45,
49, 50). Each sample is mapped against the root's 27 ids (`research/data-subject-request/merge.md`
*Section ids*, root build `2f9af25`). A `tr` section that fits a root id is a regional addition to
that id; content that fits none gets a `tr-` id. One sample row can map to more than one id.

The Turkish document is the "İlgili Kişi / Veri Sahibi Başvuru Formu": a form the person fills in
and sends to the controller under KVKK Arts. 11 and 13 and the Veri Sorumlusuna Başvuru Usul ve
Esasları Hakkında Tebliğ (RG 10.03.2018, 30356; "Başvuru Tebliği" below). 14/15 are printable
(10 PDFs, 4 HTML pages to print); only s12 has an online submit.

## Section ids

All root ids keep their root meaning. The `tr` run adds one id.

| Id | Meaning | Samples |
|---|---|---|
| *(root ids)* | as in `research/data-subject-request/merge.md` | see *Section map* |
| tr-complaint | The right to complain to the KVK Board when the controller refuses the request, answers inadequately or does not answer in time, with or without the KVKK Art. 14 time limits. Not root `appeal`, which is an appeal to the company itself. | s06 s15 |

Meanings fixed for this run (how `tr` content is read against root ids, no root meaning changed):

- `alt-channels` holds the Başvuru Tebliği Art. 5(1) channels (in person, notary, post, KEP,
  e-mail from a registered address, e-signed or mobile-signed e-mail, an application tool). In a
  printable form these are the only ways to send it, but they are still "ways to send the
  request", the root meaning.
- `steps` holds "fill in, sign and send" lines and the envelope or subject-line marking.
- `handler` holds the controller's legal identity on the form (letterhead, addressee line,
  footer with address and MERSİS).
- `identity-fields` holds the Art. 5(2) fields and the signature and date block; `request-details`
  the "Talep Konusu" free text and attachments (Art. 5(2)(d), 5(3)).
- `request-types` holds a list or tick-list of the Art. 11 rights, whether shown as information
  above the fields or as choices. A form with only a free-text box has no `request-types` row
  (root s10 kept a rights list; none of the 5 free-text-only `tr` forms has one).
- `timeline` holds the 30-day deadline; `fees-refusal` the fee rule, refusal with reasons and the
  refund.
- `response-method` holds the reply-channel field; `confirmation` the office-use receipt box.
- `data-use` holds purpose lines, the notice for the form's own data and consent or "izin" lines
  for processing the application data.

Not sections: page footers with page numbers and form codes, classification labels ("Gizli-KV",
"Confidential - Internal", "Hizmete Özel": s05 s07 s11), version and date lines (s03 s05 s06 s11
s12 s15; document level), s09's download link (§12), s12's submit button (§15), s12's tabs (§2,
read as `requester-type`). No drafting boilerplate of the kind decision 44 names.

## Mapping notes

- s01: §1 to `handler`; §2 to `intro` and `request-types` (all nine rights as information, the
  notification rights merged into the correction and erasure items); §3 to `alt-channels` and
  `timeline`; §4 and §6 to `identity-fields`, §4's purpose line also to `data-use`; §5 to
  `requester-type`; §7 (no special-category data) and §8 to `request-details`; §9 to `attestation`
  and `fees-refusal`; §10 to `response-method`; §11 to `identity-fields` (signature); §12–§15 to
  `data-use` (a full Art. 10 notice for request data); §16 repeats `request-types` and gives
  `timeline` and `fees-refusal` again.
- s02 (T2): §1 to `handler`; §2 to `intro`, `alt-channels` and `steps` (envelope text per
  channel); §3 to `identity-fields` and `data-use`; §4 to `requester-type`; §5 to
  `request-details` and `timeline`; §6 to `response-method`; §7 to `attestation` and
  `fees-refusal`; §8 to `identity-fields`; §9 to `intro` (purpose of the form) and `verification`
  (ID copies, disclaimer). No rights list.
- s03 (T2): as s02 without a deadline: §1 `handler`; §2 `intro`, `alt-channels`, `steps`; §3
  `identity-fields`, `data-use`; §4 `requester-type`; §5 `request-details`; §6
  `response-method`, `attestation`, `fees-refusal`; §7 `identity-fields`. No rights list, no
  30-day line.
- s04: page §1 to `intro` and `request-types` (nine rights, information only); §2 and §7 to
  `alt-channels`, §2's ID check in person also to `verification`; §3 to `timeline` and
  `fees-refusal` (refusal reasons in writing or electronically); §4 to `identity-fields`; §5 to
  `requester-type`; §6 to `request-details`; §8 to `intro` and `verification`; §9 to
  `verification` and `confirmation` (delivery problems); §10 to `identity-fields`; §11 (office-use
  receipt) to `confirmation`; §12 to `handler`. No reply-channel field.
- s05 (T3): §0 to `handler`; §1 to `intro`; §2 to `request-types` (four rights paraphrased); §3
  and §4 to `alt-channels`; §5 to `steps`; §6 to `identity-fields` and `requester-type`; §7 to
  `requester-type`; §8 to `request-details`; §9 to `response-method` and `representative`
  (collection by proxy with a notarised power of attorney); §10 to `intro` and `timeline`; §11 to
  `verification` and `fees-refusal`; §12 to `identity-fields`.
- s06: §1 to `handler` and `contact`; §2 to `alt-channels`; §3 to `identity-fields` (ID number
  asked only on written applications); §4 to `requester-type`; §5 to `request-types` and
  `request-details`; §6 to `response-method`; §7 to `attestation` and `verification`; §8 to
  `timeline`, `fees-refusal` and **`tr-complaint`**.
- s07 (T1): §2 to `intro`, `handler`, `timeline` and `fees-refusal`; §3 and §5 to `alt-channels`,
  §3's reserved ID check to `verification`; §4 to `steps`; §6 to `intro`, `verification` and
  `fees-refusal` (refusal with reasons); §7 to `identity-fields`; §8 to `requester-type`; §9 to
  `handler`; §10 to `request-types` (eight boxes covering all nine rights); §11 and §12 to
  `request-details`; §13 to `response-method` and `representative`; §14 to `identity-fields`; §15
  to `representative`.
- s08 (OCR, section C restored by hand): §1 and §10 to `handler`; §2 and §8 to `identity-fields`
  (§8 lists the Art. 5(2) contents and says an application without them is invalid); §3 to
  `requester-type`; §4 to `request-details`; §5 to `response-method`; §6 to `intro` and
  `verification`; §7 to `alt-channels` and `steps`; §9 to `timeline`, `fees-refusal` and
  `response-method`. No signature block.
- s09: §1 to `intro` and `handler`; §2 to `alt-channels` and `steps`; §3 to `timeline` and
  `fees-refusal`; §4 to `eligibility` (only the data subject may apply) and `representative`
  (power of attorney); §5 to `identity-fields` and `requester-type`; §6 to `request-types`; §7 and
  §8 to `request-details`; §9 to `response-method`; §10 to `attestation` and `data-use` ("izin"
  to process the application data); §11 to `identity-fields`.
- s10: §1 to `intro`, `alt-channels` and `verification` (ID card in person); §2 and §7 to
  `identity-fields`; §3 to `request-details`; §4 to `requester-type`; §5 to `response-method`; §6
  to `attestation` and `verification`. The controller is never named: no `handler` row.
- s11 (T3): §1 to `intro`; §2 and §3 to `alt-channels`, §3 also to `steps` and `verification`; §4
  to `timeline`; §5 to `identity-fields`; §6 to `requester-type`; §7 to `request-details`; §8 to
  `response-method` and `representative`; §9 to `verification` and `fees-refusal`; §10 to
  `identity-fields`. The text gives no legal name and no address (the address column is blank in
  every row, only the logo names the company): no `handler` row, and its `alt-channels` row is
  counted with that gap.
- s12: §1 and §4 to `intro`; §2, §5, §16 and §17 to `requester-type` (user or business tab; the
  business petition copies the user petition, user wording included, and is read once); §3 to
  `handler`; §6 to `request-types` (five fixed requests, Art. 11/1 (a), (b), (c), (ç), (g); it
  leaves out (d), (e), (f) and (ğ)); §7 and §13 to `response-method`; §8, §9 and §11 to
  `identity-fields`; §12 to `request-details`; §14 to `privacy-link` and `data-use` (notice
  acknowledgement and consent in one required box); §18 to `timeline`; §19 to `attestation`; §20
  to `verification`; §21 to `fees-refusal`. No channel is named; the web form is itself the
  Tebliğ's "application" route, but the page does not say so, so no `alt-channels` row.
- s13: §2 to `intro` and `alt-channels`; §3 to `alt-channels` and `steps`; §4 to `timeline`; §5 to
  `identity-fields` and `requester-type`; §6 to `request-types` and `request-details`; §7 to
  `attestation`, `data-use` ("izin") and `response-method`; §8 to `identity-fields`; §9 to
  `representative` (no one may apply for a spouse, relative or child) and `verification`. "ETS"
  is never defined and no trade name appears: no `handler` row.
- s14: §1 to `intro`, `handler` and `privacy-link`; §2 to `alt-channels`, `steps` and
  `verification`; §3 to `identity-fields`; §4 to `requester-type`; §5 to `request-types` and
  `request-details`; §6 to `timeline` and `response-method`; §7 to `verification` and
  `fees-refusal`; §8 to `attestation` (assessment request only) and `identity-fields`.
- s15: §1 to `intro`; §2 to `handler` and `contact`; §3 to `alt-channels` and `steps`; §4 to
  `timeline` and `fees-refusal`; §5 to **`tr-complaint`**; §6 to `identity-fields` and `data-use`;
  §7 to `requester-type`; §8 to `request-types`; §9 to `other-routes` and `request-effects`; §10
  to `request-details`; §11 to `response-method`; §12 to `representative`; §13 to `attestation`
  and `verification`; §14 to `data-use` (Art. 10 notice paragraph); §15 (office-use box) to
  `confirmation`.

## Section map

First-row order of ids per sample (basis of every count and median below).

```
s01 handler intro request-types alt-channels timeline identity-fields data-use requester-type request-details attestation fees-refusal response-method
s02 handler intro alt-channels steps identity-fields data-use requester-type request-details timeline response-method attestation fees-refusal verification
s03 handler intro alt-channels steps identity-fields data-use requester-type request-details response-method attestation fees-refusal
s04 intro request-types alt-channels verification timeline fees-refusal identity-fields requester-type request-details confirmation handler
s05 handler intro request-types alt-channels steps identity-fields requester-type request-details response-method representative timeline verification fees-refusal
s06 handler contact alt-channels identity-fields requester-type request-types request-details response-method attestation verification timeline fees-refusal tr-complaint
s07 intro handler timeline fees-refusal alt-channels verification steps identity-fields requester-type request-types request-details response-method representative
s08 handler identity-fields requester-type request-details response-method intro verification alt-channels steps timeline fees-refusal
s09 intro handler alt-channels steps timeline fees-refusal eligibility representative identity-fields requester-type request-types request-details response-method attestation data-use
s10 intro alt-channels verification identity-fields request-details requester-type response-method attestation
s11 intro alt-channels steps verification timeline identity-fields requester-type request-details response-method representative fees-refusal
s12 intro requester-type handler request-types response-method identity-fields request-details privacy-link data-use timeline attestation verification fees-refusal
s13 intro alt-channels steps timeline identity-fields requester-type request-types request-details attestation data-use response-method representative verification
s14 intro handler privacy-link alt-channels steps verification identity-fields requester-type request-types request-details timeline response-method fees-refusal attestation
s15 intro handler contact alt-channels steps timeline fees-refusal tr-complaint identity-fields data-use requester-type request-types other-routes request-effects request-details response-method representative attestation verification confirmation
```

## Merged list (s01–s15)

Median position as in the root merge (rank / (ids − 1)). Tiers over 15: core ≥12, common 6–11,
rare ≤5. *Commonly omitted* = ≤2/15. *Block* names the `tr` section that carries the id's
Turkish content; "root" means the root section already covers what the samples do and the block
adds nothing.

| Id | Count | Tier | Median | Block |
|---|---|---|---|---|
| intro | 14/15 | core | 0.00 | root (Art. 11/13 citation folded into `tr-rights`) |
| handler | 12/15 | core | 0.03 | root (controller's address and KEP in `tr-channels`) |
| contact | 2/15 | rare | 0.09 | root |
| alt-channels | 14/15 | core | 0.18 | **tr-channels** |
| steps | 10/15 | common | 0.28 | **tr-channels** (envelope marking, sign and send) |
| privacy-link | 2/15 | rare | 0.37 | root |
| timeline | 13/15 | core | 0.40 | **tr-timeline** |
| identity-fields | 15/15 | core | 0.42 | **tr-application-content** |
| eligibility | 1/15 | rare | 0.43 | root |
| request-types | 10/15 | common | 0.46 | **tr-rights** |
| requester-type | 15/15 | core | 0.54 | root |
| data-use | 7/15 | common | 0.55 | **tr-request-notice** (Art. 10 notice; consent lines go to its *Avoid*) |
| other-routes | 1/15 | rare | 0.63 | root |
| verification | 12/15 | core | 0.68 | root |
| tr-complaint | 2/15 | rare | 0.68 | **tr-complaint** |
| request-effects | 1/15 | rare | 0.68 | root |
| request-details | 15/15 | core | 0.69 | **tr-application-content** (Art. 5(2)(d), 5(3)) |
| response-method | 14/15 | core | 0.80 | **tr-reply** |
| attestation | 10/15 | common | 0.86 | root |
| representative | 6/15 | common | 0.87 | root |
| fees-refusal | 13/15 | core | 0.92 | **tr-timeline** |
| confirmation | 2/15 | rare | 0.95 | root (office-use box noted in `tr-reply`) |
| residence, status, appeal, opt-out-signals, sale-status, non-discrimination | 0/15 | — | — | — |

Block sections, by the median of the id that leads them: `tr-channels` (0.18), `tr-timeline`
(0.40; union with `fees-refusal` 14/15), `tr-application-content` (0.42; 15/15), `tr-rights`
(0.46; 10/15), `tr-complaint` (0.68; 2/15), `tr-reply` (0.80; 14/15), `tr-request-notice`
(3/15; it sits at the end in s01 and s15 and after the fields in s12, about 0.90).
`tr-request-notice` counts the samples that give or link a notice for the form's data (s01 s12
s15), not every purpose line; the purpose lines and "izin" lines stay root `data-use`.

The root sections take the rest as written. Turkish counts for the writer's information:
`requester-type` 15/15 (customer, employee or former employee, job applicant, business partner or
supplier staff, visitor, other, often with years or a date), `verification` 12/15 (7 of them the
shared ID-copy paragraph, counted once), `attestation` 10/15, `representative` 6/15.

## Shared wording (rule 4, decision 39)

Raw texts compared on 6-word shingles (containment over the smaller text) and 8-word strings
present in 3 or more samples. **No copies**: the highest pair is s02/s03 at 0.37 (T2); every
other pair is under 0.25. Every sample counts for prevalence. Shared blocks add to patterns once:

| Block | Samples | Wording |
|---|---|---|
| B1 (T2 core) | s01 s02 s03 | identity purpose line, field grid, relationship boxes, reply options, first-person declaration with the fee acknowledgement; s01's opening differs, so candidates.md did not tag it T2 |
| B2 (ID-copy paragraph) | s02 s04 s05 s07 s08 s10 s11 | purpose of the form; the right to ask for ID card or driving licence copies "to avoid unlawful disclosure"; no liability for wrong or unauthorised applications |
| B3 (T1/T3 opening) | s05 s07 s11 s13 | Art. 13(1): applications in writing or by the Board's methods |
| B4 (deadline line) | s02 s05 s08 s11 s13 | 30 days "from the date the request reaches us", reply in writing or electronically |
| B5 (objection wording) | s09 s12 s13 s14 | first-person objection to a result from solely automated analysis |
| T3 tail | s05 s11 (s07) | reply by e-mail "faster"; collection in person by proxy only with a notarised power of attorney |

Families: T1 has one member in the batch (s07; Midas Kripto, row 20, and Penti, row 30, are not
extracted); T2 has s02 and s03 (Pluxee 17, Opet 21, Vestel 26, Koton 28 not extracted); T3 has s05
and s11 (s13 opens alike, then its own words; Pamukkale 23 not extracted); T4 (Macrocenter 29,
IKEA 27) has no member in the batch. The
extraction notes hold: s12's business petition is read once; s11 lacks a name and address; s08's
section C was restored by hand and is read as extracted.

## Patterns (s01–s15)

Counts are samples; "(Bn once)" marks where a shared block's wording is one pattern.

- **tr-channels** (14/15; s12 none): in person 13/14, notary 9/14, post 8/14 (registered post
  in s05 s08 s09 s11 s13); KEP 9/14 (s01 s02 s03 s04 s05 s07 s08 s11 s14); e-mail from the address
  on file 8/14 (s01 s02 s03 s05 s06 s07 s08 s15); e-mail with secure electronic or mobile
  signature 7/14 (s01 s02 s03 s04 s06 s08 s15; s04 accepts e-mail only that way); an application
  tool 0/14. Paper only 3/14 (s09 hand or registered post; s10 in person or notary; s13
  registered mail, "using this form"): see *Avoid*. 2/14 add "other methods the law allows" (s04
  s07). A per-channel table or grid with address and envelope text 5/14 (s02 s03 s05 s11 s13; T2
  and T3 once each); the subject line "Kişisel Verilerin Korunması Kanunu Kapsamında Bilgi Talebi"
  7/14. 4/14 say to fill in and sign (or print) before sending (s08 s09 s14 s15). 5/14 ask for ID
  when applying in person (s04 s07 s10 s11 s14). s11 leaves every address blank; s10 says "the
  nearest club".
- **tr-timeline** (14/15; s10 none): 30 days in 13/15 (not s03, s10); 4/13 add "as soon as
  possible" (s01 s07 s13, s04 "according to the nature of the request"); 5/13 count from receipt
  (B4 once). Free of charge said in 6/15 (s01 s06 s07 s12 s14 s15). Fee: 10/15 point to the Board's
  tariff without amounts (s01 s02 s03 s04 s05 s06 s07 s11 s12 s14); 2/15 give the Tebliğ amounts
  (s08 s15: free up to 10 pages, 1 TL per page above, the cost of the medium); s09 will ask for
  approval if the request costs more than expected. 3/15 make the applicant acknowledge a possible
  fee in the declaration (B1 once). Refusal with reasons 2/15 (s04 s07); refund when the
  controller is at fault 1/15 (s15). Every fee statement matches KVKK Art. 13(2) and Tebliğ Arts.
  6(5) and 7; none asks for a fee up front.
- **tr-application-content** (15/15): T.C. kimlik no. 15/15 (s06 only for written applications);
  nationality and passport or ID number for foreigners 9/15 (s01 s02 s03 s04 s06 s07 s08 s11
  s15); an address 15/15, most in the Tebliğ's words ("tebligata esas yerleşim yeri veya iş yeri
  adresi"); fax 4/15 (s01 s02 s04 s07). Signature block 14/15 (not s08), with a date in 13/15.
  3/15 cite the Tebliğ on the fields (s01 footnote, s11 footnote, s08 lists Art. 5(2) and says an
  application without it is invalid); s15 says why the ID number and address are asked. Request
  subject as free text 15/15; 6/15 ask for supporting documents (s01 s02 s03 s07 s09 s13; s13 for
  evidence of damage), s09 says not to send originals; s01 warns not to send special-category
  data. Required phone, fax or e-mail: 3/15, see *Avoid*.
- **tr-rights** (10/15): all nine Art. 11 rights 7/10 (s01 s04 s06 s07 s13 s14 s15; s01 and s07
  merge the notification right into correction and erasure, s14 splits it in two); s09 leaves out
  (f) and (ğ); s12 offers (a), (b), (c), (ç) and (g) only; s05 paraphrases four. A tick-list 6/10
  (s06 s07 s09 s13 s14 s15); information above the fields only 3/10 (s01 s04 s05); a fixed
  petition asserting every listed right at once 1/10 (s12). First-person options 7/10 ("…öğrenmek
  istiyorum"); article letters on each option 3/10 (s12 s13 s15). Prompts for detail after
  correction or damage 3/10 (s06 s07 s13). Rows beyond the statute: consent withdrawal (s06 s15),
  an electronic copy split from (b) (s15). 5/15 take free text only (s02 s03 s08 s10 s11). The
  automated-decision objection reads alike in s09 s12 s13 s14 (B5 once).
- **tr-complaint** (2/15): s06 one sentence naming the three triggers (refused, inadequate, late);
  s15 the triggers and the 30/60-day windows of Art. 14(1).
- **tr-reply** (14/15; s04 none): post or letter 12/14; e-mail 13/14; fax 2/14 (B1 once);
  collection in person 4/14 (s05 s07 s11 s15; T3 tail once, with a notarised power of attorney
  for proxies); KEP 1/14 (s15); "in writing or electronically" without a pick 1/14 (s08). E-mail
  nudged as faster 3/14 (T3 tail once). s07 answers by the channel used to apply when none is
  ticked. s15 sends electronic copies through an expiring link or an encrypted file with the
  password sent separately. Oral reply by phone 2/14 (s09 s10): see *Avoid*. Office-use receipt
  box (root `confirmation`) 2/15 (s04 s15).
- **tr-request-notice** (3/15): s01 a separate, titled Aydınlatma Metni for the request process on
  its own page (controller; purposes by legal condition: legal obligation, legitimate interest;
  recipients; collection method; rights; kept for the general limitation period as evidence); s15
  one paragraph (purposes, Art. 5(2)(ç) and (e), recipients, server abroad with a pointer to the
  main notice, retention); s12 a required box linking the notice, bundled with consent (see
  *Avoid*). Root `data-use` also has the T2 purpose line (B1 once) and the "izin" lines of s09
  and s13.

## Avoid (decisions 47, 50)

Each source was read on 2026-10-27; the citations were checked against the text.

| Block section | Pattern | Samples | Source |
|---|---|---|---|
| tr-channels | Naming only paper routes (in person, notary, registered post) as the way to apply | **3/15** (s09 hand or registered post; s10 in person or notary; s13 registered mail only, on this form) | Board decision 2019/296 (01.10.2019, summary at kvkk.gov.tr/Icerik/6557): telling people they may apply only through a notary or by e-signature "Kanun’da ya da Tebliğ’de öngörülmeyen maddi bir külfet" imposes and is incompatible with the lawfulness and good-faith rule of Başvuru Tebliği Art. 6(1); Art. 5(1) lets the person choose written application, KEP, secure e-signature, mobile signature, a registered e-mail address or an application tool. |
| tr-application-content | Making phone, mobile, fax or e-mail required, or saying the Tebliğ requires them | **3/15** (s01 asterisks every field, fax included, and names the Tebliğ as the source; s12's web form requires mobile and e-mail; s13 asks for every field, mobile and e-mail included) | Başvuru Tebliği Art. 5(2)(ç): e-mail, phone and fax only "Varsa" (if any); KVKK Art. 4(2)(ç): data limited and proportionate to the purpose. |
| tr-reply | Offering an oral reply (a phone call) as the answer | **2/15** (s09, s10) | KVKK Art. 13(3) and Başvuru Tebliği Art. 6(3): the answer is given "yazılı olarak veya elektronik ortamda"; the Board's public announcement of 1 October 2026 (kvkk.gov.tr/Icerik/9024) says phone, face-to-face or other oral replies are not the answer those articles require. |
| tr-request-notice | Asking consent ("rıza", "izin") to process the data given in the application, or bundling it with the notice | **3/15** (s12 one required box "Aydınlatma Metni'ni okudum ve … rıza gösteriyorum"; s09 and s13 "izin" in the declaration) | Answering is a legal duty (KVKK Art. 13), so the processing rests on Art. 5(2)(ç), as s15 says. Board decision summary "Hizmetin Açık Rıza Şartına Bağlanması" (kvkk.gov.tr/Icerik/5412): asking consent where another condition exists misleads the person and is an abuse of right (Art. 4). For s12 also Aydınlatma Yükümlülüğü Tebliğ Art. 5(1)(f): informing and taking consent are done separately. Same sources as `tr-explicit-consent`. |

Looked at, not marked (no authority text found that calls them wrong; for the chief of staff):

- Fees: none. Every fee line matches KVKK Art. 13(2) and Tebliğ Arts. 6(5), 7.
- Reserving the right to ask for ID card or driving-licence copies (7/15, B2 once). The Tebliğ
  names no identity document; 2019/296 concerns channels, not documents. Kept as a root
  `verification` pattern.
- "Written applications must use this form" (s13) or "fill in this form completely and sign it"
  (s14). The Tebliğ sets the content, not a form, and `tr-kvkk-notice` s06 says a form is not
  required; no Board text found. Kept as a pattern.
- "No one may apply for a spouse, relative or child" (s13). Parents act for minors as legal
  representatives under the Civil Code, but no KVKK text on representatives was found. Kept as a
  root `representative` pattern.
- The ID number asked only on written applications (s06): Tebliğ Art. 5(2)(b) lists it for every
  application, but asking less does not burden the person. Pattern only.
- s12 leaving out four rights: KVKK Art. 11 gives all nine, but no text bars a short list. The
  block says to list all nine.

## Document level (s01–s15)

- **Words:** median 547 (189–1,040). Large 672 (s01 s04 s07 s10 s13), mid 543 (s02 s05 s08 s11
  s14), small 497 (s03 s06 s09 s12 s15).
- **Carrier:** 10/15 PDF (s01 s02 s04 with an HTML page s05 s07 s08 s10 s11 s13 s14), 4/15 an
  HTML page to print (s03 s06 s09 with a .docx, s15), 1/15 HTML with an online form (s12). 14/15
  have no submit button.
- **Title:** "İlgili Kişi Başvuru Formu" (s01 s03 s04 s06 s07), "Veri Sahibi Başvuru Formu" (s02
  s11 s15), "KVKK Başvuru Formu" (s12) or "Başvuru Formu" (s10), a title naming Law 6698 (s05 s09
  s13 s14); s08 only the company name.
- **Structure:** numbered or lettered parts 11/15 (s09's .docx too); explanatory text first and
  fields after in most; s08 and s04's PDF put the explanation after the fields.
- **Register:** formal legal Turkish 13/15 ("Şirketimiz", "siz"), s06 informal "sen", s15 plain;
  10/15 switch to the applicant's first person in options and the declaration ("istiyorum",
  "beyan ve taahhüt ederim").
- **Recurring elements:** KVKK article numbers 13/15 (not s10, s14); the Tebliğ named 7/15 (s01
  s02 s03 s07 s08 s11 s15); a date or version
  6/15; classification labels 3/15; tick boxes and blank lines throughout.
- **Commonly omitted:** an application tool as a channel (0/15 named; s12's form unnamed as
  such); that applications are made in Turkish (Tebliğ Art. 4(2); 0/15); the complaint to the
  Board (13/15 omit); refusal with reasons (13/15 omit); the refund when the controller is at
  fault (14/15 omit).

## Facts (step 5)

No new key (decision 29). The block reuses:

| Section | Keys |
|---|---|
| tr-channels | `facts.users.rights_channels`, `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.tr.seller_registry` (its `kep_address` and `mersis_no`) |
| tr-timeline | `facts.users.request_handling` (`response_days`) |
| tr-application-content | `facts.users.request_handling` (`identifiers`), `facts.product.has_accounts` |
| tr-rights | `facts.users.rights_channels`, `facts.data.automated_decisions` |
| tr-complaint | none (statutory) |
| tr-reply | `facts.users.request_handling` (`reply_channels`) |
| tr-request-notice | `facts.tr.kvkk_notice_url`, `facts.tr.legal_bases`, `facts.tr.transfer_tools`, `facts.data.retention` |

Considered and not added: a key for the channels accepted (the Tebliğ list) — `rights_channels`
holds routes, and the KEP address is in `facts.tr.seller_registry`; a fee key — the Tebliğ fixes
the tariff, and no sample charges more.

## First-batch qualification

All 15 valid, each the controller's own Art. 11/13 form. Borderline:

| Sample | Verdict | Why |
|---|---|---|
| s04 ING | valid | HTML page plus its PDF form, one sample (rule 6). |
| s08 Honda | valid | image-only PDF read by OCR; section C restored by hand and checked against the page image. |
| s09 Frink | valid | HTML page with the same text as the linked .docx; the .docx's attachment table counted. |
| s11 TürkKEP | valid | the text never names the company or its address; counted as written. |
| s12 Look Bubble | valid | user and business tabs; the business petition copies the user one and is read once. |

## Saturation

Not run. The method needs a first batch of 15, then batches of 5 until 5 samples in a row add no
id (`build/build.md` step 3). The owner closed the pool after the first batch (2026-10-27), so no
sample after s15 was judged and the stop rule could not be met: `saturated: false`,
`sample_count: 15`. Within the batch, the only id outside the root list (`tr-complaint`) came from
s06; s07–s15 added none, which is 9 in a row, but samples inside the first batch are not judged
under the stop rule. Pool rows 16–24 and reserve rows 25–31 are not extracted.

## Changes

- 2026-10-27: list written from s01–s15. One id added (`tr-complaint`). No root meaning changed.

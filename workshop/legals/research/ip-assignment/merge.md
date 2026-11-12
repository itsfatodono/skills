# ip-assignment: merged section list

Row-level mapping: `section-map.md`. Formats per `build.md` step 3: `prose`, `list`, `table`, plus
the layout marks `pointer` and `embedded`.

## Section ids

Fixed after mapping the first batch (s01–s15), before judging s16 onward. An id is one kind of fact
the agreement gives the signer, not a heading. A change made later is noted under *Folds*.

| Id | Meaning |
|---|---|
| parties | Parties, recitals, purpose, effective date and consideration (employment, shares, access to confidential information, a nominal sum); who counts as "the Company" (affiliates, successors); which periods of service the agreement covers (earlier contractor work, backdating). |
| confidentiality | What counts as confidential information and what does not; the duty not to use or disclose it and for how long; information third parties entrusted to the company; approval before publishing; no reverse engineering; reporting misuse; following security rules. |
| protected-disclosures | What the confidentiality duty does not stop: reports to authorities, disclosures a law or court compels, protected talk about working conditions, immunity for disclosing a trade secret to officials or in a sealed filing. |
| prior-obligations | The signer's promises about earlier duties: no conflicting agreement, no bringing or using a former employer's or anyone else's confidential information. |
| assignment | What IP the company gets and how: the definitions of invention and IP rights, the test (made during the relationship, related to the business, using company resources), present words of assignment, works made for hire, a period after leaving that the assignment still reaches, assignment onward to a customer or government at the company's direction, no licence to the signer, interim licences; in a founder form, the identified technology and its schedule. |
| excluded-inventions | Inventions made during the relationship that the signer keeps (own time, own equipment, unrelated to the business), the notice that states this limit, and how the signer claims an invention falls under it. |
| prior-inventions | Inventions the signer made before the relationship and keeps: the list or schedule, the excuse for not describing one under another confidentiality duty, and the licence the company gets when one is built into its work. |
| invention-disclosure | The duty to tell the company promptly about inventions, during the relationship and for a time after it. |
| records | The duty to keep records of inventions and hand them over. |
| assistance | The duty to help the company obtain, register, perfect and enforce its rights, during and after the relationship; the power of attorney that backs it; a quitclaim of infringement claims against the company; perfecting a founder assignment that missed something. |
| moral-rights | Waiver of moral rights and of other rights that cannot be assigned, with a fallback licence or covenant not to sue. |
| compensation | What the signer gets for the IP itself, apart from the job: shares, a price, royalties, or a statement that nothing more is owed. Named `invention-compensation` until the merge (see *Folds*). |
| open-source | Rules on putting open-source or other third-party code into company work. |
| warranties | The signer's warranties about the IP assigned (sole owner, no encumbrance, no infringement, authority to sign) and the indemnity for a breach of them. |
| conflicting-activities | Duty of loyalty and limits on outside work or conflicting interests during the relationship. |
| non-solicitation | After the relationship: no soliciting or hiring staff; no soliciting or interfering with customers, suppliers or partners. |
| non-compete | A ban on competing after the relationship ends. |
| non-disparagement | A ban on disparaging the company. |
| name-likeness | Consent to the company using the signer's name, image or likeness. |
| return-of-property | Company property and information on leaving: return, deletion from personal devices, inspection, no expectation of privacy on company systems, the exit certificate. |
| notify-new-employer | Telling later employers about the agreement: the company's right to notify them, the signer's duty to show it. |
| no-employment-promise | The agreement is not an employment contract; employment stays at will or on its own terms. |
| enforcement | Remedies for breach (injunction without bond, fees, fixed sums); acknowledgements that the covenants are reasonable; court narrowing; extending a covenant by the time it was breached. |
| arbitration | Arbitration of disputes; class, collective and jury waivers. |
| governing-law | Governing law and courts. |
| closing | Added at s18. A deferred transfer's mechanics: conditions to be met before the assignment closes, exclusivity until then, closing deliveries, either side's right to walk away, and what happens to the IP and information if the deal fails. |
| general | Closing clauses: entire agreement, amendment, waiver, severability, successors and assignment of the agreement, survival, notices, counterparts and e-signatures, export, interpretation, advice of counsel and voluntary signing, effect of a change of role, third-party beneficiaries, relationship of the parties. |

Marks that are not sections (`section-map.md`): `host`, `signature`, `heading`, `regional`.

Drafting rows folded at mapping: definitions blocks go to the id they serve (invention and IP
definitions to `assignment`, confidential-information definitions to `confidentiality`); a general
"further assurances" closing clause goes to `general`, the IP-specific duty to `assistance`.

## First batch (s01–s15)

Three founder forms (s03, s09, s15) and twelve employee forms. Median position is the first row of
the id divided by the sample's row count (host, signature and heading rows left out).

| Id | Count | Median pos. | Formats | Samples |
|---|---|---|---|---|
| parties | 15/15 | 0.00 | list, prose | s01–s15 |
| confidentiality | 13/15 | 0.05 | list, prose | s01 s02 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 |
| prior-obligations | 11/15 | 0.14 | prose | s01 s02 s04 s05 s06 s07 s08 s11 s12 s13 s14 |
| assignment | 15/15 | 0.16 | list, prose | s01–s15 |
| prior-inventions | 13/15 | 0.19 | list, prose, table | s01 s02 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 |
| protected-disclosures | 9/15 | 0.20 | prose | s01 s02 s04 s06 s07 s10 s12 s13 s14 |
| compensation | 3/15 | 0.29 | prose | s06 s09 s12 |
| invention-disclosure | 11/15 | 0.29 | prose | s01 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 |
| moral-rights | 9/15 | 0.29 | prose | s01 s04 s06 s07 s08 s10 s11 s13 s15 |
| assistance | 14/15 | 0.36 | prose | s01 s02 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 |
| warranties | 5/15 | 0.36 | prose | s02 s03 s09 s12 s15 |
| records | 8/15 | 0.38 | prose | s04 s05 s07 s08 s11 s12 s13 s14 |
| excluded-inventions | 11/15 | 0.39 | list, prose | s02 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 |
| open-source | 4/15 | 0.46 | prose | s04 s07 s08 s11 |
| conflicting-activities | 9/15 | 0.50 | list, pointer, prose | s01 s04 s06 s07 s08 s10 s11 s13 s14 |
| non-compete | 5/15 | 0.50 | prose | s01 s02 s04 s10 s12 |
| return-of-property | 12/15 | 0.52 | prose | s01 s02 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 |
| non-solicitation | 11/15 | 0.53 | prose | s01 s02 s04 s06 s07 s08 s10 s11 s12 s13 s14 |
| name-likeness | 2/15 | 0.59 | pointer, prose | s01 s14 |
| non-disparagement | 2/15 | 0.63 | prose | s06 s14 |
| arbitration | 2/15 | 0.66 | prose | s07 s12 |
| notify-new-employer | 11/15 | 0.67 | prose | s01 s02 s05 s06 s07 s08 s10 s11 s12 s13 s14 |
| enforcement | 13/15 | 0.69 | prose | s01 s02 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 |
| general | 15/15 | 0.69 | list, prose | s01–s15 |
| governing-law | 15/15 | 0.72 | prose | s01–s15 |
| no-employment-promise | 10/15 | 0.77 | prose | s01 s04 s06 s07 s08 s10 s11 s12 s13 s14 |

The founder forms use a subset of the employee ids (`parties`, `assignment`, `assistance`,
`governing-law`, `general`; s15 also `confidentiality`, `prior-inventions`, `moral-rights`,
`enforcement`; s09 `compensation`) plus `warranties`, which 3/3 founder forms carry and
2/12 employee forms (s02, s12). No id is founder-only.

## Saturation log

Judged in pool order from s16. New = a section id not in the list above (`PLAN.md` decision 27).

| Sample | Result | Why |
|---|---|---|
| s16 | not new | all rows fit known ids; conflict-of-interest policy and audit rows fold into `conflicting-activities` and `return-of-property` |
| s17 | not new | all rows fit known ids |
| s18 | new | `closing`: conditions to closing, deliveries, walk-away rights and failed-deal terms of an asset-purchase-shaped founder sale; its price, royalties and escrow fit `compensation`, its mutual indemnities `warranties` |
| s19 | not new | all rows fit known ids (unnumbered paragraphs; assignment terms sit in its Exhibit A) |
| s20 | not new | all rows fit known ids; ownership of online accounts made for the company folds into `return-of-property` (company property handed over) |
| s21 | not new | all rows fit known ids; the consultant's warranties that work does not infringe and carries no malicious code fold into `warranties` |
| s22 | not new | all rows fit known ids; the severance agreement's clauses that point to the assignment are host rows |
| s23 | not new | all rows fit known ids; not a copy of s21 (6-gram containment 0.10). Fifth non-new sample in a row (s19–s23): **saturated at s23** |
| s24 | not new (past the stop point) | founder form; all rows fit known ids |
| s25 | not new (past the stop point) | all rows fit known ids; its Colorado attestation addendum is regional |

No new id after s18. s19–s23 are five non-new samples in a row: `saturated: true` at s23. s24 and
s25 were dispatched before s23 was judged and are kept as samples past the stop point. The pool's
c26–c30 were never extracted. `sample_count: 25`.

## Folds (made at merge, after judging)

None changes a judgement: each id involved was in the list when its samples were judged.

- `invention-compensation` renamed `compensation`, and its meaning widened from pay for inventions
  to what the signer gets for the IP. Founder forms state their consideration (shares, a price, a
  nominal sum) as their own clause, which is the same kind of fact. s03, s15 and s24's
  consideration clauses were remapped to it. Count 11/25.
- A founder form's general "further assurances" closing clause goes to `general` (s24 row 14), its
  duty to complete the transfer to `assistance` (s24 row 6), as in the employee forms.
- Ownership of domains and social accounts made for the company (s20) folded into
  `return-of-property`; a security-policy row (s06, s25) into `confidentiality`; conflict-of-interest
  policies (s14, s16) into `conflicting-activities`.

## Merged list (all 25)

Median position as in the first batch.

| Id | Count | Tier | Median pos. | Formats | Samples |
|---|---|---|---|---|---|
| parties | 25/25 | core | 0.00 | list, prose | s01–s25 |
| confidentiality | 22/25 | core | 0.06 | list, prose | all but s03 s09 s24 |
| protected-disclosures | 13/25 | common | 0.14 | prose | s01 s02 s04 s06 s07 s10 s12 s13 s14 s16 s17 s20 s25 |
| prior-obligations | 19/25 | common | 0.14 | prose | s01 s02 s04 s05 s06 s07 s08 s11 s12 s13 s14 s16 s17 s19 s20 s21 s22 s23 s25 |
| assignment | 25/25 | core | 0.16 | list, prose, table | s01–s25 |
| prior-inventions | 21/25 | core | 0.23 | list, prose, table | all but s03 s09 s18 s24 |
| invention-disclosure | 17/25 | common | 0.29 | prose | s01 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s17 s19 s20 s22 s23 s25 |
| compensation | 11/25 | common | 0.31 | embedded, list, prose | s03 s06 s09 s12 s15 s18 s20 s21 s23 s24 s25 |
| moral-rights | 16/25 | common | 0.35 | list, prose | s01 s04 s06 s07 s08 s10 s11 s13 s15 s16 s17 s18 s20 s21 s23 s25 |
| assistance | 24/25 | core | 0.38 | prose | all but s03 |
| warranties | 8/25 | rare | 0.40 | list, prose | s02 s03 s09 s12 s15 s18 s21 s24 |
| records | 13/25 | common | 0.42 | prose | s04 s05 s07 s08 s11 s12 s13 s14 s16 s20 s21 s22 s25 |
| open-source | 5/25 | rare | 0.47 | prose | s04 s07 s08 s11 s21 |
| excluded-inventions | 16/25 | common | 0.48 | list, prose | s02 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s16 s17 s19 s20 s23 |
| conflicting-activities | 16/25 | common | 0.49 | list, pointer, prose | s01 s04 s06 s07 s08 s10 s11 s13 s14 s16 s17 s19 s20 s22 s23 s25 |
| return-of-property | 20/25 | core | 0.52 | prose | all but s03 s09 s15 s18 s24 |
| non-solicitation | 18/25 | common | 0.54 | prose | s01 s02 s04 s06 s07 s08 s10 s11 s12 s13 s14 s16 s17 s19 s21 s22 s23 s25 |
| non-compete | 10/25 | common | 0.56 | prose | s01 s02 s04 s10 s12 s18 s21 s22 s23 s25 |
| non-disparagement | 5/25 | rare | 0.64 | prose | s06 s14 s17 s19 s25 |
| notify-new-employer | 17/25 | common | 0.67 | prose | s01 s02 s05 s06 s07 s08 s10 s11 s12 s13 s14 s16 s17 s20 s22 s23 s25 |
| enforcement | 20/25 | core | 0.70 | prose | all but s03 s09 s16 s19 s24 |
| general | 25/25 | core | 0.70 | list, prose | s01–s25 |
| governing-law | 24/25 | core | 0.74 | prose | all but s19 (its host carries it) |
| no-employment-promise | 16/25 (root 13/25) | common | 0.79 | prose | s01 s04 s06 s07 s08 s10 s11 s12 s13 s14 s17 s19 s20 s22 s23 s25 |
| name-likeness | 4/25 | under 20% | 0.59 | pointer, prose | s01 s14 s17 s20 |
| arbitration | 3/25 | under 20% | 0.69 | prose | s07 s12 s20 |
| closing | 1/25 | under 20% | 0.35 | list, prose | s18 |

Under 20%, so *Commonly omitted* and no section: `name-likeness`, `arbitration` (two more samples
send disputes to a separate arbitration agreement beside the assignment: s13, s16, s17's host),
`closing`.

**Founder forms (s03 s09 s15 s18 s24).** Each carries `parties`, `assignment`, `governing-law` and
`general`; 5/5 `compensation`; 5/5 `warranties` (3/5 as a full list, 2/5 knowledge-qualified or
short); 4/5 `assistance`; 2/5 `moral-rights`, `confidentiality`, `enforcement`; 1/5
`prior-inventions`, `non-compete`, `closing`. None carries `invention-disclosure`, `records`,
`return-of-property`, `notify-new-employer`, `no-employment-promise` or `non-solicitation`: those
belong to an ongoing relationship. Every founder form is its own short instrument; none sits inside
an employee agreement. One employee form (s20, the CEO and co-founder's copy) reaches back to work
done for "predecessors or founders".

## Section-level notes for the skeleton

Counts out of the samples that have the section unless stated.

- **Assignment test.** Present words ("hereby assign") about 20/25; "and agree to assign" for future
  inventions 6/25; one founder form only agrees to assign at closing (s18) and one confirms an
  earlier assignment (s09). Test by time alone (anything made during the relationship) about 8/20
  employee forms; tied to the business, the work or company resources about 12/20. A period after
  leaving that the assignment or the disclosure duty still reaches: 8/25 (s02 s05 s06 s07 s10 s19
  s20 s25), counted in months or years. Copyright works treated as owned from creation, the assignment
  as fallback: 13/25. Onward assignment to a customer or government the company names: 11/25.
  Held in trust until assigned: 5/25.
- **Prior inventions.** A schedule to fill: 18/21 (16 filed, 2 cited but not filed); "no list means
  none" 16/21; a licence to the company when one is built into its work 21/21, nearly always
  non-exclusive, royalty-free,
  perpetual, irrevocable, worldwide and sublicensable; notice before building one in 3/21; a second
  table for inventions the signer cannot describe because of another duty 2/21 (s04 s20). Schedule
  layouts: tick boxes (none / see below / extra sheets) 11/18; columns for title, date and
  identifying number 9/18.
- **Excluded inventions.** 13/16 follow one statute's wording (own time, own equipment, no company
  information, unrelated to the business or the work); 9/16 attach or quote a statutory notice.
  3/16 state the carve-out with no law behind it (s02 tied to permitted outside activities, s23,
  s04's state version).
- **Confidentiality.** During and after the relationship with no end date 18/22; a fixed fallback
  period only where a court needs one 2/22 (s04 s10); exclusions (public, already known,
  independently made) about 13/22; third parties' information held by the company 16/22; prior
  approval to publish or lecture 7/22; duty to report misuse 2/22; reverse engineering banned 3/22; mutual only in the founder sale
  (s18).
- **Covenants.** Staff non-solicit 17/18 of `non-solicitation`; customer, supplier or partner
  non-solicit or non-interference 12/18; both run for a fixed number of months or years after
  leaving (12 or 24 months typical in the filled copies). 5/18 limit the post-employment
  non-solicit to use of confidential information. Non-compete 10/25, all with a fixed period and an
  area (worldwide 3/10, a state or radius 3/10, a defined business elsewhere).
- **Assistance.** Duty to sign and help during and after the relationship 24/24, usually at the
  company's expense (about 15/24); power of attorney if the signer's signature cannot be had 21/24;
  quitclaim of infringement claims against the company 5/24.
- **Enforcement.** Injunction without bond, breach called irreparable 19/20; reasonableness
  acknowledgement 9/20; court narrowing 9/20; fee shifting about 6/20; fixed sums for breach 1/20 (s10).
- **General.** Entire agreement 22/25, severability 21/25, amendment 22/25, successors and
  assignment of the agreement 22/25, waiver 18/25, survival 16/25, counterparts or e-signature
  16/25, change of role does not end it 13/25, notices 11/25, advice of counsel or voluntary
  signing 9/25, export 5/25.

## Document level

- **Length:** median about 4,000 words (range 1,255 s24 to 15,390 s10). Founder forms median about
  1,600 (1,255–13,587, the top an asset-purchase form); employee forms median about 4,000.
- **Host:** 12/25 stand alone; 13/25 are attached to another agreement: an offer letter 8 (s05 s07
  s13 s14 s16 s17 s20 s22), an employment agreement 3 (s06 s19 s23), a separation letter 1 (s08), a
  consulting agreement 1 (s21). Every host makes signing a condition of the job or engagement.
- **Signer:** employee 19/25 (most are executives' signed copies of the standard form), consultant
  1/25, founder 5/25. Unsigned forms: 3/25 (s10 s12 s25); the rest executed copies.
- **Register:** first person from the signer ("I agree", "I hereby assign") with the company in the
  third person 16/25; third person throughout ("Employee", "Assignor") 9/25, including all five
  founder forms; plain-English rewrite 1/25 (s13). Formal US drafting with long "including without
  limitation" lists in most; capitals for at-will, advice-of-counsel or governing-law clauses in
  about 14/25.
- **Recurring elements:** numbered sections 23/25; signature blocks 25/25 (the company countersigning in most); a
  prior-inventions schedule 16/25 filed (2 more cited but not filed); a statutory notice as an exhibit
  9/25; an exit certificate form 3/25 (s12 s14, s11 cited but not filed); an effective date tied to
  the first day of service or earlier 9/25; definitions set inline, a definitions block or clause in about 9/25.
- **Commonly omitted:** a table of contents (25/25 have none); a summary; any statement of how
  long the company keeps the signer's personal data; a duty on the company (beyond the founder
  forms' payment and s10's access promise).

## Regional content

Content one law requires, left out of the root skeleton. Region runs start from these samples.

| Region | Content | Samples |
|---|---|---|
| us | Defend Trade Secrets Act whistleblower-immunity notice (18 U.S.C. § 1833(b)), as a clause or exhibit | s01 s02 s04 s06 s07 s08 s10 s12 s13 s14 s17 s19 s20 s25 |
| us | California Labor Code §§ 2870–2872: own-time invention exclusion and the written notice of it; sister statutes in Delaware, Illinois, Kansas, Minnesota, Nevada, New Jersey, New York, North Carolina, Utah, Washington (s10 quotes 11) | s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s16 s17 s19 s20 |
| us | Works made for hire under the Copyright Act (17 U.S.C. § 101) | s01 s04 s05 s06 s10 s17 s20 s21 s22 s23 s25 |
| us | Carve-outs for SEC whistleblowing (Rule 21F-17), NLRA Section 7 talk about pay and conditions, and agency charges (EEOC, OSHA, NLRB) | s04 s06 s07 s08 s10 s16 s19 s20 s25 |
| us | State limits on restrictive covenants: California Business and Professions Code § 16600 (no post-employment non-compete; staff non-solicit only through confidential information), Labor Code § 925 (California law and forum), Government Code § 12964.5 (unlawful-acts carve-out); Colorado, D.C., Illinois, Louisiana, Maryland, Massachusetts, Minnesota, Nebraska, North Dakota, Oklahoma, Oregon, Texas, Virginia, Washington, Wisconsin addenda (pay thresholds, notice periods, bans) | s08 s10 s11 s12 s13 s14 s16 s17 s25 |
| us | At-will employment statement | s01 s04 s07 s08 s10 s12 s13 s14 s17 s19 s20 s22 s23 s25 |
| us | Arbitration under the Federal Arbitration Act, class waiver, California PAGA | s07 s12 s20 |
| us | Tax-free contribution of founder IP for shares (Internal Revenue Code § 351) | s15 |
| il | Israeli Patents Law 1967 § 134 waiver of service-invention royalties and the fallback "special compensation"; Copyright Law 2007 § 45 moral rights | s21 s23 |
| ca | Quebec civil-law sale of IP: Civil Code penal clause, suretyship, French-language clause, sales-tax registration, Canadian moral-rights waiver (Copyright Act s. 14.1) | s18 |
| au | New South Wales deed of assignment (no law-specific clause found) | s09 |

**Root counts after removing regional content** (step 4: left out wherever the sample put it).
A sample counts toward a root section when its content gives that section's fact without resting
on one law; the statute's own text, notice or rule goes to the region.

- `no-employment-promise`: root 13/25. s13, s20 and s22 state only at-will status (us row above),
  so they do not count; the other 13 also say the agreement promises no employment for any period.
- `protected-disclosures`: stays 13/25. The trade-secret immunity notice and the sealed-filing
  immunity are the us block's; its fact that the signer may report a suspected breach of law to
  officials or a lawyer stays in the root (12/13, all but s16). Agency carve-outs 6/13 (s04 s07
  s10 s13 s20 s25), talk about pay, conditions or unlawful acts 8/13 (s04 s06 s07 s10 s13 s16 s20
  s25), compelled disclosure 5/13 (s06 s10 s12 s17 s25).
- `excluded-inventions`: stays 16/25; the carve-out is a contract term lawful anywhere. The
  statutory notice (attached or quoted 9/16, pointed to 4/16) is the us block's.
- `assignment`: works made for hire leave the root's patterns (us row above).
- `compensation`: stays 11/25; s21 and s23 also say the pay covers the IP. Their waiver of the
  statutory employee-inventor compensation is the il block's.

No sample comes from the UK, the EU or Turkey. Their employee-invention rules (UK Patents Act 1977
ss. 39–43; German ArbnErfG compensation; Turkish Industrial Property Law no. 6769 arts. 113 ff.)
are for a region run to source from the law and regional samples.

## Copies (rule 4)

No two samples share their whole text. Highest 6-word-shingle containment between `raw/` texts:
s07–s08 0.36, s01–s17 0.27, s05–s22 0.25 (form families with their own edits). s21 and s23 share a
title (an Israeli form) but only 0.10 of their text.

# *Avoid* sweep (2026-10-27)

A read-through of every skeleton (`skeletons/*.md`) and region block (`regions/*/*.md`) built
before PLAN.md decision 50, for patterns that could move to an *Avoid* field. Nothing here has been
edited. Counts come from the skeletons as they stand; they were not checked against the
`merge.md` files. Guidance names are leads to verify before any move. Where a citation is marked
*(verify)*, the exact article or paragraph has not been checked.

Done in the same pass: `regions/tr/tr-distance-sales.md` › `personal-data`, 4/18 (s07 s16 s19 s23)
marketing consent inside the contract.

## Open question before moving any root candidate

Under *Regions* in `formats/skeleton-format.md`, root skeletons may not have a pattern that names
a specific law. Every root candidate below breaks a regulator's guidance (EDPB, ICO, CNIL, FTC, CMA)
that applies in some regions and not others. There are two options: (a) let *Avoid* in a root
skeleton cite guidance in general terms and treat that as an exception to *Regions*, or (b) put
the *Avoid* in the region block (`eu`, `uk`, `us`) and keep the root pattern as it is. The format
does not settle this. Decide it before moving 1–16.

## Strong candidates

The guidance names the pattern directly.

| # | File › section | Pattern and count | Guidance it breaks |
|---|---|---|---|
| 1 | `skeletons/cookie-policy.md` › `intro` | 2/20 treat visiting or continuing to use the service as agreeing to cookies | EDPB Guidelines 05/2020 on consent (continuing to browse or scroll is not consent); CNIL cookie guidelines and recommendation (2020); ICO guidance on storage and access technologies; CJEU C-673/17 *Planet49* |
| 2 | `skeletons/cookie-policy.md` › `browser-controls` | 2/19 make browser settings the only control on offer | ICO cookie guidance and CNIL 2020 guidelines (browser settings alone do not give valid consent for non-essential cookies) |
| 3 | `skeletons/privacy-policy.md` › `intro-scope` | 6/32 treat use of the product as consent to the policy | EDPB Guidelines 05/2020 on consent (consent bundled with acceptance of terms, or inferred from use, is not freely given or unambiguous); GDPR Art. 7(2) |
| 4 | `skeletons/terms-of-service.md` › `privacy` | about 12/23 treat use of the product as agreement to the privacy policy | Same as 3 |
| 5 | `skeletons/privacy-policy.md` › `sensitive` | 5/9 tie it to consent given by choosing to provide the data | EDPB Guidelines 05/2020, explicit consent (needs an express statement; providing data is not enough); GDPR Art. 9(2)(a) |
| 6 | `skeletons/eula.md` › `telemetry` | 4/12 frame telemetry as the user's consent | EDPB Guidelines 05/2020 (consent buried in a licence is not separate or freely given; telemetry needed for licensing rests on another basis) |
| 7 | `skeletons/privacy-policy.md` › `changes` | 13/32 treat continued use as acceptance (1 reserving change with little or no notice) | FTC, "AI (and other) companies: quietly changing your terms of service could be unfair or deceptive" (Feb 2024) and *Gateway Learning* (2004): material, retroactive privacy changes need affirmative express consent |
| 8 | `skeletons/cookie-policy.md` › `changes` | 2/11 treat continued use after a change as acceptance | Same as 7; for cookies also 1 (a change cannot switch on tracking without a new choice) |
| 9 | `skeletons/terms-of-service.md` › `terms-changes` | 6/27 make changes effective on posting and put the duty to check on the user (beyond this, about 24/27 treat continued use as acceptance) | CMA unfair contract terms guidance (CMA37) on variation clauses; Consumer Rights Act 2015 Sch. 2 Pt. 1 paras 11–13; Directive 93/13/EEC Annex 1(j)–(k). The 24/27 is core, but *Avoid* applies whatever the prevalence, so decide whether it goes too or only the narrower 6/27 |
| 10 | `skeletons/eula.md` › `terms-changes` | about 7/16 change the agreement at will with continued use as acceptance; 2/7 without notice | Same as 9 |
| 11 | `skeletons/terms-of-service.md` › `communications` | 8/12 take text-message consent from the user giving a number | FCC TCPA rules, 47 CFR 64.1200(a)(2): marketing texts need prior express written consent. This applies only when the texts are marketing (*verify* the split in the samples) |
| 12 | `regions/eu/privacy-policy.md` › `eu-legal-bases` | 2/24 (generator texts) list the bases without saying which purpose uses which | Article 29 WP / EDPB Guidelines on transparency (WP260 rev.01), annex on Art. 13(1)(c): each purpose must be tied to its legal basis |

## Weaker candidates

These conflict with guidance only in some readings, or the guidance is general.

| # | File › section | Pattern and count | Guidance it may break |
|---|---|---|---|
| 13 | `skeletons/terms-of-service.md` › `fees-payment` | about 6/27 treat continued use as acceptance of a price change | ROSCA (15 U.S.C. 8403), express informed consent to recurring charges; CMA37 on price-variation terms; Directive 93/13 Annex 1(l) |
| 14 | `skeletons/subscription-terms.md` › `changes` | 6/26 treat continued use after a price or terms change as acceptance | Same as 13; California Automatic Renewal Law on material changes *(verify)* |
| 15 | `skeletons/eula.md` › `software-changes`; `skeletons/terms-of-service.md` › `service-changes` | about 7/13 and about 12/21 change or stop the product at any time without notice or liability | Directive (EU) 2019/770 Art. 19 (modifying digital content or services needs notice, and a right to terminate on a negative impact); CMA37 |
| 16 | `skeletons/privacy-policy.md` › `deidentified` | 6/12 say de-identified data may be used or disclosed without restriction | CCPA §1798.140(m) (de-identified data needs a public commitment not to re-identify, plus contractual controls); FTC 2012 privacy report, three-part test |
| 17 | `regions/tr/tr-distance-sales.md` › `inspection` | 8/19 deem an accepted parcel undamaged; 5/19 disclaim liability for damage once accepted | Law 6502 Arts. 8–12 (defective goods rights, two-year period, no duty to notify at handover); Haksız Şartlar Yönetmeliği on terms that limit the consumer's legal rights *(verify)* |
| 18 | `regions/tr/tr-pre-contract-info.md` › `inspection` | 4/10 deem an accepted parcel undamaged; 1/10 deems silence acceptance after a few hours | Same as 17 |
| 19 | `regions/tr/tr-distance-sales.md` › `withdrawal` | 15/34 list return conditions (original box, accessories, resaleable); 2/34 read as a returns policy (seller approval, unopened box); 1/34 keeps the pre-2014 20-day take-back rule | Mesafeli Sözleşmeler Yönetmeliği Arts. 9–14 (withdrawal without giving reasons; liability only for loss of value beyond inspection, Art. 14). The 15/34 is a split; probably only "unopened" / "original box as a condition" goes to *Avoid* *(verify per sample)* |
| 20 | `regions/tr/tr-pre-contract-info.md` › `withdrawal` | 4/17 add return conditions stricter than the law (unopened, original box, original invoice) | Same as 19 |
| 21 | `regions/tr/tr-distance-sales.md` › `exceptions` | 1/34 declares special-day and campaign goods non-returnable (some of the 14/34 house rules may also go beyond the list) | Mesafeli Sözleşmeler Yönetmeliği Art. 15: closed list of exceptions |
| 22 | `regions/tr/tr-pre-contract-info.md` › `exceptions` | 1/4 states the digital exclusion without the consent condition; 2/19 add their own categories (custom-made goods; an older software, media and cosmetics list) | Art. 15 closed list; Art. 15(1)(ğ)–(h): the digital and service exceptions need the consumer's prior approval |
| 23 | `regions/tr/tr-distance-sales.md` › `withdrawal` (digital and service sellers) | 4/7 never state the 14-day right and rely on the exception alone | Yönetmelik Art. 15(1)(ğ)–(h) (the exception needs the consumer's approval to start performance) and Art. 5 (pre-contract information on the right, or that there is none) |
| 24 | `regions/tr/tr-distance-sales.md` › `delivery` | 1/33 (old template) says delivery may take up to 3 months | Law 6502 Art. 48 and Yönetmelik Art. 16: 30-day maximum |
| 25 | `regions/tr/tr-distance-sales.md` › `performance` | 1/31 allows an equal-quality substitute without a consent step | Yönetmelik on performance and substitution *(verify article)*; the other 10/31 ask for consent |
| 26 | `regions/tr/tr-distance-sales.md` › `disputes` | 1/34 makes the seller's domicile the only forum; 1/34 names only a city's courts (for consumer buyers) | Law 6502 Art. 73(5): the consumer may sue where they live or where the transaction took place *(verify paragraph)* |
| 27 | `regions/tr/tr-pre-contract-info.md` › `disputes` | 1/20 names one city's courts for all disputes | Same as 26 |
| 28 | `regions/tr/tr-distance-sales.md` › `disputes` | 10/34 make the seller's books and electronic records conclusive evidence (7 citing HMK Art. 193) | Haksız Şartlar Yönetmeliği, annex list of terms that restrict the consumer's evidence *(verify item)*. Courts have treated such clauses in consumer contracts as unfair |

## Considered and left out

- `skeletons/terms-of-service.md` › `intro`, 29/29 make use the act of acceptance: it is weak
  under US browsewrap case law, but no regulator's guidance calls it wrong.
- `skeletons/subscription-terms.md` › `auto-renewal`, 1/29 says no reminder is sent: whether
  that is wrong depends on the region (California ARL, for example). It goes to a `us` block if
  anywhere.
- `skeletons/subscription-terms.md` › `payment`, 5/30 deemed acceptance of a charge after a
  reporting deadline: this may conflict with card-network and FCBA dispute windows. Too
  indirect.
- `skeletons/subscription-terms.md` › `refunds`, `skeletons/terms-of-service.md` › `refunds`
  and `skeletons/eula.md` › `refunds`, no-refund rules without a legal carve-out: the root
  already carries the carve-out pattern, and the statutory rights belong in region blocks.
- `skeletons/terms-of-service.md` › `liability`, no carve-out for death or injury: this is an
  absence, not a pattern.
- `regions/eu/ropa.md` › `eu-transfers`, naming Privacy Shield: already written as a DPC
  warning, with no sample count.
- `regions/tr/tr-pre-contract-info.md` › `disputes`, 2/20 give dated limits under old law: this
  is out of date, not something the guidance calls wrong.

**Total: 28 candidates (12 strong, 16 weaker).**

## Classification under the owner's rule (2026-11-04)

The owner's rule: a pattern that breaks a law, or that the authority enforcing the law calls
invalid, is *Avoid* and is never written, even if the user asks. A pattern in a grey area (lawful
but against the consumer, or only open to challenge as an unfair term) stays a normal pattern: the
writer follows the usual majority rule, and the user may ask for it. *Avoid* goes in the block of each region where the
law applies, not in the root (option (b) above), so a pattern lawful in one region stays open
there.

Citations checked on 2026-11-04 against the official texts: Law 6502 Arts. 5, 8–12, 48(3), 73(5);
Mesafeli Sözleşmeler Yönetmeliği Arts. 13(2), 15(1), 16(1), 16(4), 17. Corrections to the tables
above: the value-loss rule is Art. 13(2), not Art. 14; Art. 15(1)(ğ) (instant digital content
and services) carries no consent condition, only (h) (services started before the period ends)
does; the Yönetmelik has no provision on substitution.

### Avoid

| # | Pattern | Regions | Source |
|---|---|---|---|
| 1 | Visiting or continuing to use = agreeing to cookies | eu, uk, tr | ePrivacy Art. 5(3) and GDPR Art. 4(11); CJEU C-673/17 *Planet49*; EDPB 05/2020; PECR reg. 6; KVKK Çerez Rehberi (2022) |
| 2 | Browser settings as the only control, for cookies that need consent | eu, uk; tr *(verify the guide's wording)* | ICO and CNIL cookie guidance |
| 3 | Use of the product = consent to the privacy policy | eu, uk, tr | GDPR Arts. 4(11), 7(2); EDPB 05/2020; KVKK Aydınlatma Tebliği Art. 5(1)(f) |
| 4 | Same, in the terms of service | eu, uk, tr | Same as 3 |
| 5 | Providing sensitive data = consent to its processing | eu, uk, tr | GDPR Art. 9(2)(a), EDPB 05/2020 on explicit consent; KVKK Art. 6 |
| 6 | Installing or using = consent to telemetry | eu, uk, tr | EDPB 05/2020 (consent inside a licence); ePrivacy Art. 5(3); KVKK Board, "Hizmetin Açık Rıza Şartına Bağlanması" |
| 7 (narrow) | A material change applied to data already collected, with continued use as the only consent | us; eu, uk when the change adds a consent-based purpose | FTC, *Gateway Learning* (2004) and Feb 2024 guidance; GDPR Art. 6(1)(a) |
| 8 | Continued use after a change = consent to new cookies | eu, uk, tr | Same as 1 |
| 11 (narrow) | Giving a phone number = consent to marketing texts | us, tr | 47 CFR 64.1200(a)(2) (prior express written consent); Law 6563 Art. 6 and Ticari İletişim Yönetmeliği (prior onay) |
| 12 | Listing legal bases without tying each to its purpose | eu | GDPR Art. 13(1)(c); WP260 rev.01 |
| 15 (narrow) | Changing a digital product without notice, for consumers | eu | Directive 2019/770 Arts. 19, 22 |
| 16 | De-identified data "without restriction", with no commitment not to re-identify | us | Cal. Civ. Code §1798.140(m) |
| 17, 18 | Accepting the parcel = undamaged; no liability for damage after acceptance; silence for a few hours = acceptance | tr | Law 6502 Arts. 8–12 (no duty to notify, two-year period); Yönetmelik Art. 17 (seller bears loss and damage until delivery) |
| 19, 20 (part) | Withdrawal conditional on unopened packaging, the original box or resaleable condition (except goods under Art. 15(1)(ç) and (e)) | tr | Yönetmelik Arts. 9, 13(2), 15(1) |
| 21 | Campaign or special-day goods, or any other category outside Art. 15, excluded from withdrawal | tr | Yönetmelik Art. 15(1), closed list |
| 22 (part) | Art. 15 categories listed without their condition (software, media and consumables without "packaging opened") | tr | Yönetmelik Art. 15(1)(e) |
| 24 | Delivery period longer than 30 days | tr | Law 6502 Art. 48(3); Yönetmelik Art. 16(1) |
| 26, 27 | A single forum for consumer disputes (the seller's domicile or a named city) | tr | Law 6502 Art. 73(5); HMK Art. 18(2) |
| new | Monetary limits for the arbitration committee taken from a past year (`tr-pre-contract-info` › `disputes`, 2/20: s08 s15; `tr-distance-sales` › `disputes`, the common template's 2014 figures) | tr | Wrong information, the same kind as 24. Was listed under *Considered and left out* |

### Grey (stay patterns)

| # | Pattern | Why grey |
|---|---|---|
| 7 (rest) | Continued use = acceptance of a changed privacy policy | Unlawful only in the narrow case above |
| 9, 10 | Terms or agreement changed at will, with continued use as acceptance (both the 24/27 and the 6/27) | CRA 2015 Sch. 2, Directive 93/13 Annex and the Haksız Şartlar Yönetmeliği list are indicative: a court decides |
| 11 (rest) | Giving a number = consent to informational texts; marketing in eu and uk | Prior express consent is enough for informational texts; soft opt-in (PECR reg. 22(3), ePrivacy Art. 13(2)) |
| 13, 14 | Continued use = acceptance of a price change | Indicative unfair-term lists; ROSCA covers consent to the renewal, not each price change *(California ARL: verify)* |
| 15 (rest) | Change or stop the product without notice, in uk, us, tr and for business users | No rule like Art. 19 there |
| 19, 20 (rest) | Asking for accessories and the invoice with the return | Practical instruction, not a condition on the right |
| 19 (rest) | The seller taking the goods back within 20 days (1/34, pre-2014 wording) | Art. 13(1) lets the seller offer to collect the goods; no period binds that offer |
| 23 | Digital or service sellers relying on the exception without stating the 14-day right | Art. 5 asks for when the right is lost; the consent step is there |
| 25 | An equal substitute without the buyer's consent | No rule in the current Yönetmelik; the buyer keeps the Law 6502 rights |
| 28 | The seller's records as conclusive evidence | HMK Art. 193 allows evidence agreements; only those that remove proof altogether are void (193(2)) |

### Dropped

- 22 (part), the digital exception stated without a consent condition: Art. 15(1)(ğ) needs none.
  A service seller still needs the consent under (h); `facts.tr.immediate_performance_consent`
  covers that.
- 22 (part), custom-made goods: already Art. 15(1)(b).

### Blocks needed

*Avoid* entries for root sections need a block in every region where they apply. Blocks that
exist: `privacy-policy` (eu, uk, us). New blocks holding only *Avoid*: `cookie-policy` (eu, uk,
tr), `privacy-policy` (tr), `terms-of-service` (eu, uk, us, tr), `eula` (eu, uk, tr): 11 files.

### Applied (2026-11-04, PLAN decision 53)

All *Avoid* rows above are now in the skeletons: the 11 blocks; *Avoid on root sections* in the
eu, uk and us privacy blocks; an *Avoid* field in `eu-legal-bases` and in the Turkish sales
documents' `inspection`, `withdrawal`, `exceptions`, `delivery` and `disputes`. The `inspection`
quotes of both Turkish documents showed an *Avoid* pattern and were replaced (s10, s07).
Open: row 2 for `tr` (the KVKK cookie guide's wording on browser settings is unchecked).

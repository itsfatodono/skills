---
doc_id: privacy-policy
title: Privacy Policy, European Union part
kind: document
family: privacy-notices
region: eu
part: block
sample_languages: [en]
sample_count: 32
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** What the GDPR adds to the privacy policy for users in the EU/EEA.
- **Shape:** 23/32 carry EU content. Placement: 10/23 a separate regional part (near the end in
  9); 10/23 woven into the main sections; 3/23 a pointer to a separate regional notice. 20/23
  cover the UK in the same text; none gives the EU a part of its own. 2/23 are generator texts
  written around the GDPR alone.
- **Register:** more formal than the rest of the policy; GDPR terms ("controller", "personal
  data", "processing") appear here even when the main text avoids them.
- **Recurring elements:** Art. 27 representative address blocks (14/23); links to the list of
  supervisory authorities (8/23).
- **Commonly omitted:** DPIA mentions; a data protection officer for small companies.

Counts come from the 32 global privacy-policy samples (`research/privacy-policy/`).

## Sections

### eu-controller: Controller and representative

- **Covers:** the controller for EU users, its EU establishment or Art. 27 representative, and
  the DPO if one is appointed.
- **Prevalence:** 14/32 (44%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.eu.representative`, `facts.company.dpo_contact`
- **Patterns:**
  - 14/23 name an Art. 27 representative, with address and email or web form; most in the
    contact section, as an address block.
  - 6/32 name a separate EU entity as controller, introduced by "If you live in the EEA...".
  - 8/32 route requests to a DPO.
- **Quote:** "As Telegram is located outside the EEA, we have designated a third party ... as our representative pursuant to Article 27 of the GDPR." (s02)
- **Commonly omitted:** the reason the representative was appointed.

### eu-legal-bases: Legal bases

- **Covers:** the GDPR legal basis for each kind of processing.
- **Prevalence:** 24/32 (75%), common
- **Applies when:** always
- **Facts:** `facts.data.purposes`
- **Patterns:**
  - Placement splits: 10/24 inline with each purpose; 8/24 a separate section listing the bases
    with examples; 6/24 only in a regional part or a linked page. Under the regional part, write
    the separate list.
  - Bases used: contract, legitimate interests, consent, legal obligation (all four in 18/24).
  - 2/24 (generator texts) list the bases without saying which purpose uses which.
  - 6/24 spell out each legitimate interest ("It is in our legitimate interest to...").
  - 4/24 put bases in a table (category or purpose, basis).
- **Avoid:** listing the bases without saying which purpose uses which: 2/24 (generator texts).
  GDPR Art. 13(1)(c) asks for the purposes "as well as the legal basis for the processing", and
  the Article 29 WP transparency guidelines (WP260 rev.01, annex) read it as a link from each
  purpose to its basis.
- **Quote:** "We are required by law to tell you what the legal basis for each use is, so we've done that too." (s21)
- **Commonly omitted:** article numbers (cited by 3/24); the balancing test itself.

### eu-rights: GDPR rights and complaints

- **Covers:** the rights the GDPR adds (object, restrict, portability, withdraw consent) and the
  right to complain to a supervisory authority.
- **Prevalence:** 17/32 (53%), common
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`
- **Patterns:**
  - 17/32 include the complaint right; 8/32 link the list of supervisory authorities; 3/32 name
    the lead authority.
  - 1/32 asks users to contact the company first while affirming the direct right to complain.
- **Quote:** "We encourage you to contact us first ... so we can address your concerns directly." (s11)
- **Commonly omitted:** the one-month response deadline (given by 5/32 overall).

### eu-transfers: Transfers out of the EEA

- **Covers:** the legal mechanism for each transfer out of the EEA, and how to get a copy.
- **Prevalence:** 12/32 (38%), rare
- **Applies when:** `facts.data.storage_locations` has a country outside the EEA
- **Facts:** `facts.eu.transfer_mechanisms`, `facts.data.storage_locations`
- **Patterns:**
  - 12/32 name the mechanism: standard contractual clauses most often, then adequacy decisions.
  - 5/32 offer a copy of the safeguards on request.
- **Quote:** "When we transfer personal data to a third country, we use appropriate mechanisms." (s22)
- **Commonly omitted:** the list of destination countries per processor.

### eu-dpf: EU-U.S. Data Privacy Framework

- **Covers:** EU-U.S. DPF certification, with the statements the framework requires.
- **Prevalence:** 3/32 (9%), rare
- **Applies when:** `facts.eu.dpf == true`
- **Facts:** `facts.eu.dpf`, `facts.company.legal_name`
- **Patterns:**
  - 3/3 near-statutory wording in the framework's order: certification, precedence of the
    Principles, FTC oversight, onward-transfer liability, independent dispute body, binding
    arbitration.
- **Quote:** "Our adherence to the DPFs specified above is subject to the investigatory and enforcement powers of the U.S. Federal Trade Commission." (s14)
- **Commonly omitted:** nothing; the framework fixes the content.

### eu-children: Age of digital consent

- **Covers:** the higher minimum age that applies to EU users without parental consent.
- **Prevalence:** 3/32 (9%), rare
- **Applies when:** `facts.eu.consent_age > facts.product.min_age`
- **Facts:** `facts.eu.consent_age`, `facts.product.min_age`
- **Patterns:**
  - 3/3 one clause in the children paragraph ("under 13, or 16 in the EEA").
- **Quote:** "If we learn we have collected or received personal data from a child under 13 (or 16 in the EEA or UK), we will delete that information." (s11)
- **Commonly omitted:** the per-country ages (13–16).

## Avoid on root sections

### intro-scope

- **Avoid:** treating use of the product as consent to the policy: 6/32. GDPR Arts. 4(11) and
  7(2) and the EDPB Guidelines 05/2020 on consent: consent is never inferred from use or bundled
  with acceptance of other terms, so the sentence claims a legal basis that does not exist.

### sensitive

- **Avoid:** tying sensitive data to consent given by choosing to provide it: 5/9. GDPR Art.
  9(2)(a) needs explicit consent, which the EDPB Guidelines 05/2020 (section 4) describe as an
  express statement; providing the data is not one.

### changes

- **Avoid:** treating continued use as consent to a change that adds a purpose resting on
  consent: part of the 13/32 that treat continued use as acceptance. GDPR Arts. 6(1)(a) and 7 and
  the EDPB Guidelines 05/2020: consent to the new purpose is asked for on its own. Continued use
  as acceptance of other changes stays a pattern.

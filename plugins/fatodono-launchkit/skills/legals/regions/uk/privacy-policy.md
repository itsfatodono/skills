---
doc_id: privacy-policy
title: Privacy Policy, United Kingdom part
kind: document
family: privacy-notices
region: uk
part: block
sample_languages: [en]
sample_count: 32
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** What the UK GDPR adds to the privacy policy for users in the United Kingdom.
- **Shape:** 20/32 name the UK in their regional content, and all 20 write it in one text with
  the EEA ("EEA and UK", "Designated Countries"); none gives the UK a part of its own. This block
  is the UK half of that text, so a document with both regions repeats some content; the
  repetition is the cost of keeping each region removable.
- **Register:** as the EU part: formal, with UK GDPR terms.
- **Recurring elements:** a UK representative address block next to the EU one (10/32); the
  ICO named as the authority (3/32).
- **Commonly omitted:** UK-only differences from the EU rules.

Counts come from the 32 global privacy-policy samples (`research/privacy-policy/`). A sample
counts only when the row for that content names the UK, so every count here is a lower bound;
samples that wrote "Europe" and meant the UK too are not counted.

## Sections

### uk-controller: Controller and representative

- **Covers:** the controller for UK users and its UK representative.
- **Prevalence:** 10/32 (31%), rare
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.uk.representative`, `facts.company.dpo_contact`
- **Patterns:**
  - 10/32 name a UK representative, as an address block beside the EU one, with its own email
    or web form.
  - 7/32 name the controller for UK users explicitly, often the same entity as for the EEA.
- **Commonly omitted:** the legal basis for the representative (UK GDPR Art. 27).

### uk-legal-bases: Legal bases

- **Covers:** the UK GDPR legal basis for each kind of processing.
- **Prevalence:** 6/32 (19%), rare
- **Applies when:** always
- **Facts:** `facts.data.purposes`
- **Patterns:**
  - 6/32 scope their legal-bases list to "EEA/UK" or "UK/EU law"; the bases and layout are those
    of the EU part (contract, legitimate interests, consent, legal obligation).
  - 1/32 lays bases out per data category in an annex (category, source, purpose, lawful basis).
- **Quote:** "Withdrawing your consent will not affect the lawfulness of any processing we conducted prior to your withdrawal." (s11)
- **Commonly omitted:** article numbers.

### uk-rights: Rights and complaints to the ICO

- **Covers:** UK GDPR rights and the right to complain to the Information Commissioner's Office.
- **Prevalence:** 8/32 (25%), rare
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`
- **Patterns:**
  - 8/32 extend the complaint right to UK users; 3/32 name the ICO, 1/32 with its full contact
    block.
- **Quote:** "We encourage you to contact us first ... so we can address your concerns directly." (s11)
- **Commonly omitted:** the ICO's contact details (given by 1/32).

### uk-transfers: Transfers out of the UK

- **Covers:** the legal mechanism for transfers out of the UK.
- **Prevalence:** 9/32 (28%), rare
- **Applies when:** `facts.data.storage_locations` has a country outside the UK
- **Facts:** `facts.uk.transfer_mechanisms`, `facts.data.storage_locations`
- **Patterns:**
  - 9/32 cover UK transfers in the same sentence as EEA transfers.
  - 2/32 name the UK Addendum or the IDTA; the rest rely on "standard contractual clauses" or
    "appropriate safeguards".
- **Commonly omitted:** the UK adequacy regulations by name.

### uk-dpf: UK Extension to the Data Privacy Framework

- **Covers:** certification under the UK Extension to the EU-U.S. DPF.
- **Prevalence:** 2/32 (6%), rare
- **Applies when:** `facts.uk.dpf == true`
- **Facts:** `facts.uk.dpf`, `facts.company.legal_name`
- **Patterns:**
  - 2/2 name the UK Extension in the same certification statement as the EU-U.S. framework.
- **Commonly omitted:** nothing; the framework fixes the content.

## Avoid on root sections

### intro-scope

- **Avoid:** treating use of the product as consent to the policy: 6/32. UK GDPR Arts. 4(11)
  and 7(2) and the ICO's guidance on consent: consent is never inferred from use or bundled with
  acceptance of other terms, so the sentence claims a legal basis that does not exist.

### sensitive

- **Avoid:** tying sensitive data to consent given by choosing to provide it: 5/9. UK GDPR Art.
  9(2)(a) needs explicit consent, which the ICO's guidance on consent describes as an express
  statement; providing the data is not one.

### changes

- **Avoid:** treating continued use as consent to a change that adds a purpose resting on
  consent: part of the 13/32 that treat continued use as acceptance. UK GDPR Arts. 6(1)(a) and 7
  and the ICO's guidance on consent: consent to the new purpose is asked for on its own.
  Continued use as acceptance of other changes stays a pattern.

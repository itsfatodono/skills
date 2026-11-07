---
doc_id: data-subject-request
title: Data Subject Request Form, European Union part
kind: document
family: privacy-notices
region: eu
part: block
sample_languages: [en]
sample_count: 20
saturated: false                # the root pool was closed after one saturation batch (see the root skeleton)
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** What the GDPR adds to the request form for a company whose users include people in
  the EU/EEA: the further rights the form offers, the time limits and fees, and the data
  protection officer as a route.
- **Shape:** 8/20 forms carry EU content. None gives it a part of its own: 6/8 put the extra
  rights straight into the request menu, and the rest add a sentence to a notice or a fallback.
  4/8 offer these rights to every country, with no law named. No sample names the GDPR on the
  page except one explainer.
- **Register:** the root form's plain register; rights named with the regulation's own words
  ("restrict", "object", "portability", "withdraw consent"), often beside a plain synonym
  ("rectification/correction").
- **Recurring elements:** a "contact the data protection officer" option or fallback (2/8).
- **Commonly omitted:** the one-month deadline as a number (0/8 EU samples give it); the right
  to complain to a supervisory authority (0/8); the data protection officer's contact on the form
  (6/8 give none).

Counts come from the 20 global request-form samples (`research/data-subject-request/`, *Regional
content*). The root pool was closed after one saturation batch, so this block is also
`saturated: false`.

## Sections

### eu-request-types: Further rights in the request menu

- **Covers:** the GDPR rights the request menu adds to access, correction and deletion:
  restriction, portability, objection (including to direct marketing and profiling), review of a
  decision made by automated means, withdrawal of consent, and erasure from places other than the
  account.
- **Prevalence:** 7/20 (35%), rare
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.data.automated_decisions`, `facts.product.ai_features`
- **Patterns:**
  - Restriction, portability and objection as menu options: 5/7 (s05 s09 s13 s14 s15); 1/7 lists
    them as free-text choices under the menu for European residents only (s12).
  - Withdraw consent as an option: 3/7, 1 of them for sensitive data only, saying processing
    stops for the purpose consented to (s12 s13 s14).
  - 1/7 folds direct marketing, profiling and automated decisions into one objection line with a
    plain definition (s15).
  - 1/7 offers a request to remove personal data from an AI model's answers, asking for the
    prompts that produced it and saying it is weighed against freedom of expression (s04).
  - 4/7 offer these rights to everyone, not only EU residents.
- **Quote:** "Data portability right: request a copy of your personal data in a commonly used and machine-readable format so you can transfer it to another organisation." (s15)
- **Commonly omitted:** what restriction does in practice; that portability covers only data the
  person provided, processed by consent or contract.

### eu-time-fees: Time limits, fees and refusals

- **Covers:** answering without undue delay and within one month, extending by up to two more
  months with notice, answering free of charge, and refusing manifestly unfounded or excessive
  requests with reasons.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 1/1 a short paragraph under the submit button: reply without undue delay within the legal
    deadline, notice if extended, free of charge, unfounded or excessive requests may be refused,
    reasons given; the deadline is tied to "governing law" with no number (s09).
- **Quote:** "The processing of this request is free of charge." (s09)
- **Commonly omitted:** the one-month figure; the right to complain to a supervisory authority
  or seek a judicial remedy when a request is refused (GDPR Art. 12(4)).

### eu-dpo: The data protection officer

- **Covers:** the data protection officer as a recipient of requests, a menu option, or the
  fallback when the form fails.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.company.dpo_contact` names a data protection officer
- **Facts:** `facts.company.dpo_contact`
- **Patterns:**
  - 1/2 says the form also reaches the DPO and offers "contact the DPO" as a request type (s15).
  - 1/2 gives the DPO's email in the confirmation and error messages, for people who cannot use
    the inbox or whose request fails (s01).
- **Quote:** —
- **Commonly omitted:** the DPO's postal address.

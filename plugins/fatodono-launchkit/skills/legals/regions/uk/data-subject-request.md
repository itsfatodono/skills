---
doc_id: data-subject-request
title: Data Subject Request Form, United Kingdom part
kind: document
family: privacy-notices
region: uk
part: block
sample_languages: [en]
sample_count: 20
saturated: false                # the root pool was closed after one saturation batch (see the root skeleton)
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** What the UK GDPR and the Data Protection Act 2018 add to the request form for a
  company whose users include people in the United Kingdom: the subject access request with its
  deadline, the further rights in the menu, a way to complain, and withholding other people's
  data.
- **Shape:** 4/20 forms carry UK content. 2/4 are access-only "subject access request" forms
  from UK companies (s07 s17); 2/4 add the UK rights to a general menu (s11 s12, the second shared
  with the EEA). None gives the UK a part of its own.
- **Register:** plain help-page tone; the formal name "Subject Access Request (SAR)" given beside
  the plain one; the ICO named as the source of guidance.
- **Recurring elements:** a link to the ICO's guidance on the right of access (1/4); a separate
  postal SAR form (1/4).
- **Commonly omitted:** the right to complain to the ICO (0/4); two changes made by the Data
  (Use and Access) Act 2025 that no sample mentions yet: the "reasonable and proportionate
  search" limit on access answers (in force since 19 June 2025) and the duty to give people a
  way to complain to the company (DPA 2018 s. 164A, in force since 19 June 2026), which only
  1/4 meets, through a "complaint" option (see `uk-complaints`).

Counts come from the 20 global request-form samples (`research/data-subject-request/`, *Regional
content*). A UK row counts only when it names the UK or comes from a UK company's form. The root
pool was closed after one saturation batch, so this block is also `saturated: false`.

## Sections

### uk-sar: Subject access request and deadline

- **Covers:** the access request named as a subject access request, the one-calendar-month
  deadline, when it starts (on receipt, or on receipt of verification documents), extension with
  notice, and how the answer is sent.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 2/2 name the request plainly first, then give the formal name and acronym.
  - 2/2 state one calendar month; 1/2 restates it after submitting and says the clock starts once
    verification documents arrive; 1/2 says the period may be extended and asks for a date range
    to speed the search.
  - 1/2 links the ICO's guidance; 1/2 names the UK GDPR and the Data Protection Act together.
  - 2/2 reply by email.
- **Quote:** "Once we've received your request – or any further verification documents, if needed – we'll send you a copy of the data you're entitled to within 1 calendar month." (s07)
- **Commonly omitted:** that the extension is up to two further months and only for complex or
  numerous requests.

### uk-request-types: Further rights in the request menu

- **Covers:** the UK GDPR rights the request menu adds to access, correction and deletion:
  restriction, portability, objection and review of automated decisions.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.data.automated_decisions`
- **Patterns:**
  - 1/2 lists restriction, portability, objection and automated-decision review as buttons with
    no descriptions (s11).
  - 1/2 offers one menu to the EEA, Switzerland and the UK together, with restriction,
    portability and objection as free-text choices (s12).
- **Quote:** —
- **Commonly omitted:** what each right does.

### uk-third-parties: Other people's data

- **Covers:** that data about other people (others on a shared account) is withheld from an
  access answer unless their authorisation is enclosed.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** `facts.product.account_roles` lists shared, family or multi-user accounts
- **Facts:** `facts.product.account_roles`
- **Patterns:**
  - 1/1 asks for the names of others on the account and says their data will be withheld unless
    their written authorisation and ID are enclosed (s17).
- **Quote:** "Note: as part of our response, we will not disclose information relating to anyone authorised on the account (other than yourself) unless we have their authorisation to do so." (s17)
- **Commonly omitted:** that the company may still disclose others' data when it is reasonable to
  do so without consent.

### uk-complaints: Complaints to the company

- **Covers:** a way to make a data protection complaint to the company through the form, which
  DPA 2018 s. 164A has required of every controller since 19 June 2026.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`
- **Patterns:**
  - 1/1 a "complaint" request type in a UK company's menu, with a free-text box and no
    description (s11). Two non-UK forms offer the same option (s13 s15; root `request-types`).
  - No sample says how complaints are acknowledged (the duty asks for an acknowledgement within
    30 days) or names the ICO as the next step.
- **Quote:** —
- **Commonly omitted:** the acknowledgement time; the ICO as the next step.

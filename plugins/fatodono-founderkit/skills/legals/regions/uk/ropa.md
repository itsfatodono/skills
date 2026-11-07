---
doc_id: ropa
title: Record of Processing Activities, United Kingdom part
kind: document
family: internal-compliance
region: uk
part: block
sample_languages: [en]
sample_count: 22
saturated: true
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** What the UK GDPR (Art. 30) and the Data Protection Act 2018 add to the record of
  processing for a company whose users include people in the United Kingdom. The root skeleton
  holds the fields every record has; this block adds the UK legal grounds, conditions and
  registrations.
- **Shape:** The record is a table, so this block is extra columns, not a section (PLAN
  decision 37). Each per-activity section below is one column added to the root grid after the
  root's columns, its heading starting with "UK:" (*Column*). The three record-level sections
  (`uk-law`, `uk-ico-registration`, `uk-representative`) are lines added to the root's
  controller block, each starting with "UK:" (*Header line*). Removing the region deletes
  those columns and lines and nothing else. No sample gives the UK content a part of its own
  either: 22/22 put it in the record's own columns or fields. The ICO's documentation template
  is the most copied column set (4/22).
- **Register:** Labels and article points in grids ("Article 6(1)(b) contract", "Sch.1, Pt.1,
  1 - Employment"); forms write the article's own words.
- **Recurring elements:**
  - Article points cited in column headings or cells: 9/22.
  - "GDPR" written where the UK GDPR is meant, with no UK law named: 7/22.
  - "N/A" kept in UK columns that do not apply to a row (transfers, conditions,
    representative), as in the root record.
- **Commonly omitted:** the UK Addendum and the IDTA by name (0/22); the exemption for
  organisations under 250 staff, which no sample mentions; the recognised legitimate interests
  basis (Art. 6(1)(ea), in force since 5 February 2026), which no sample uses yet;
  freedom-of-information status (4/22) and law-enforcement processing under DPA 2018 Part 3
  (1/22), both found only at public bodies.

Counts come from 22 UK records: 17 from the global RoPA pool (`research/ropa/`) and 5 found in
this run (`research/regions/uk/ropa/`). The Oxford colleges count once (s02). All are public
bodies, colleges or a charity, plus the ICO's template; no UK company publishes its record.

## Sections

### uk-law: Law and regulator

- **Covers:** the UK law the record is kept under and the regulator it is shown to on request.
- **Header line:** "UK: kept under UK GDPR Art. 30 and the Data Protection Act 2018; shown to
  the ICO on request."
- **Prevalence:** 16/22 (73%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`
- **Patterns:**
  - The law named in the title or the opening line: 16/16. "UK GDPR" and "Data Protection Act
    2018" together in 6/16; "GDPR" alone in 7/16.
  - 3/16 say the record is shown to the ICO on request.
  - The ICO template groups columns under bands named for the law ("Article 30 Record of
    Processing Activities", "Data Protection Act 2018 - Special Category or Criminal Conviction
    and Offence data"): 2/16.
- **Quote:** "As such, the College is legally required to maintain a Record of Processing
  Activities (ROPA) in accordance with Article 30 of the UK GDPR." (s14)
- **Commonly omitted:** why the record is needed despite the small-organisation exemption.

### uk-ico-registration: ICO registration

- **Covers:** the controller's registration number with the Information Commissioner (paid
  with the data protection fee).
- **Header line:** "UK: ICO registration number"
- **Prevalence:** 5/22 (23%), rare
- **Applies when:** `facts.registrations.privacy_regulator` has a `uk` entry with status
  `registered`
- **Facts:** `facts.registrations.privacy_regulator`
- **Patterns:**
  - One line in the controller block ("ICO registration number: Z..."): 5/5; 1/5 adds a pointer
    to the ICO's public register.
- **Quote:** —
- **Commonly omitted:** the fee tier; the renewal date.

### uk-representative: UK representative

- **Covers:** the representative a company without a UK establishment appoints under UK GDPR
  Art. 27.
- **Header line:** "UK: Representative" (name, address, email, telephone)
- **Prevalence:** 3/22 (14%), rare
- **Applies when:** `facts.company.country` is not `GB`
- **Facts:** `facts.uk.representative`
- **Patterns:**
  - A field in the header grid beside the controller and DPO: name, address, email,
    telephone: 3/3. Every sample that has it is UK-established and wrote "n/a" or left it
    empty, so no filled field was seen.
- **Quote:** —
- **Commonly omitted:** the representative's mandate or contract date.

### uk-legal-basis: Lawful basis

- **Covers:** the UK GDPR Art. 6 basis for each activity, and the law or contract behind it.
- **Column:** "UK: Lawful basis (UK GDPR Art. 6)"
- **Prevalence:** 20/22 (91%), core
- **Applies when:** always
- **Facts:** `facts.data.purposes`
- **Patterns:**
  - Short names only ("Contract", "Legal obligation", "Public task", "Consent", "Legitimate
    interests"): 9/20. The article's own words: 4/20. Article point plus short name ("Article
    6(1)(e) Public Task"): 7/20.
  - Several bases per row are common.
  - The statute or contract behind a legal obligation or task named beside it: 6/20.
  - 4/22 add a column listing the rights that apply per activity, which follow from the basis
    (portability only for contract and consent; objection for legitimate interests).
- **Quote:** "Processing is necessary for performance of our contract with you." (s02)
- **Commonly omitted:** why one basis was chosen over another; the recognised legitimate
  interests basis.

### uk-legitimate-interests: Legitimate interests

- **Covers:** for an activity based on legitimate interests, the interest itself and the
  assessment that weighs it against people's rights.
- **Column:** "UK: Legitimate interest and assessment"
- **Prevalence:** 6/22 (27%), rare
- **Applies when:** `facts.data.purposes` has a purpose with legal basis legitimate interests
- **Facts:** `facts.uk.legitimate_interests`, `facts.data.purposes`
- **Patterns:**
  - A "details relating to lawful basis" column with one or two sentences naming the interest:
    3/6.
  - A "link to record of legitimate interests assessment" column: 2/6, left empty or "Yes" in
    the filled sample.
  - 1/6 appends a short assessment per activity below the grid: expectations,
    proportionality, impact.
- **Quote:** "We, and you, have a legitimate interest in maintaining contact information in
  order to facilitate communication between us." (s09)
- **Commonly omitted:** the balancing test itself.

### uk-special-conditions: Conditions for sensitive data

- **Covers:** for special-category or criminal-offence data, the UK GDPR Art. 9(2) condition and
  the Data Protection Act 2018 Schedule 1 condition relied on.
- **Column:** "UK: Art. 9 condition / DPA 2018 Schedule 1 condition"
- **Prevalence:** 10/22 (45%), common
- **Applies when:** `facts.data.sensitive` is not empty
- **Facts:** `facts.uk.special_conditions`, `facts.data.sensitive`
- **Patterns:**
  - Schedule 1 cited by part and paragraph ("Sch.1, Pt.1, 1 - Employment"): 6/10. The
    condition in words with the Act named ("Substantial public interest under the UK Data
    Protection Act 2018"): 2/10. Art. 9 conditions only: 2/10.
  - A separate column for criminal-offence data: 3/10; "N/A" on every row but vetting.
  - 2/10 add a sentence naming the duty behind the condition (equality law) and why consent is
    not used.
  - 1/10 fills the column from a lookup sheet of Schedule 1 conditions.
- **Quote:** "In both cases, the processing must be carried out without consent so as not to
  prejudice those purposes." (s02)
- **Commonly omitted:** the Art. 9 point beside the Schedule 1 condition, when only one is given.

### uk-appropriate-policy: Appropriate policy document

- **Covers:** whether an appropriate policy document covers the activity, as DPA 2018 Schedule
  1 Part 4 requires for most Schedule 1 conditions, and whether data is kept and erased as it
  says.
- **Column:** "UK: Appropriate policy document / kept and erased as it says?"
- **Prevalence:** 5/22 (23%), rare
- **Applies when:** `facts.uk.special_conditions` names a Schedule 1 condition
- **Facts:** `facts.uk.appropriate_policy`, `facts.uk.special_conditions`
- **Patterns:**
  - The ICO template's three columns: a link to the retention and erasure policy, "retained and
    erased in accordance with the policy document?" (Yes / No), and the reason for not
    adhering: 4/5. Filled rows mostly repeat one policy link and "Yes".
  - A yes/no "Special Category Assurance Statement" column: 1/5.
- **Quote:** —
- **Commonly omitted:** the policy's review date.

### uk-transfers: Transfers out of the UK

- **Covers:** whether the activity's data leaves the UK, to which countries, and the UK GDPR
  safeguard for it.
- **Column:** "UK: Transfers out of the UK (country, safeguard)"
- **Prevalence:** 8/22 (36%), rare
- **Applies when:** `facts.data.storage_locations` has a country outside the UK
- **Facts:** `facts.uk.transfer_mechanisms`, `facts.uk.dpf`, `facts.data.storage_locations`,
  `facts.processors.list`
- **Patterns:**
  - Two columns, "names of third countries or international organisations" and "safeguards
    for exceptional transfers": 4/8. A yes/no "transferred outside the UK?" flag: 3/8. Generic
    "outside the EEA" text: 1/8.
  - "N/A" or "No" on nearly every row; filled rows name the country and the provider, then the
    safeguard in a phrase (adequacy, a provider's certification).
- **Quote:** —
- **Commonly omitted:** the IDTA or the UK Addendum by name; the UK's adequacy regulations.

### uk-processor-record: Record as a processor

- **Covers:** the separate record UK GDPR Art. 30(2) asks of a company that processes data on
  behalf of business customers.
- **Column:** "UK: Controller we act for" on the root's `processor-activities` rows, plus the
  root's transfer and security columns for those rows
- **Prevalence:** 1/22 (5%), rare
- **Applies when:** `facts.company.acts_as_processor == true`
- **Facts:** `facts.company.acts_as_processor`, `facts.company.processor_customers`,
  `facts.processors.list`
- **Patterns:**
  - The ICO offers it as a separate template beside the controller one: the customers
    (controllers) it acts for with their contacts, the categories of processing, transfers and
    security measures. Its fields mirror the root's `processor-activities` rows.
- **Quote:** —
- **Commonly omitted:** individual customers' names (categories of customer are given instead).

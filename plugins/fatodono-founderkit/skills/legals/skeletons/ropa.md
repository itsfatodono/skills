---
doc_id: ropa
title: Record of Processing Activities
kind: document
family: internal-compliance
sample_languages: [en]
sample_count: 30
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** An internal register that lists each activity in which the company handles
  personal data: why, whose data, which data, who receives it, where it goes, how long it is
  kept and how it is protected. It is kept up to date and shown to a regulator on request.
- **Shape:**
  - 19/30 are one grid with one row per activity (a spreadsheet, or a table in a PDF or Word
    file); 11/30 give each activity its own form of labelled fields. 11/30 put an index of all
    activities in front.
  - The row is a processing activity in 17/30, a record type or data asset ("Payroll
    records") in 7/30, a data category within one purpose in 4/30, and a whole department in
    2/30.
  - 12/30 group the rows: by department, function or business area (8), by data-subject group
    (3), by theme (1).
  - 3/30 add a short web page that summarises the record as lists (data subjects, data
    categories, purposes, recipients) and links the full grid.
  - Length follows the number of activities: 7–40 rows for a small organisation (400–2,500
    words); large registers run to hundreds of activities.
- **Register:** Grids hold short labels, fixed vocabularies and fragments, not sentences.
  Forms are written in formal third person ("the Agency"), in paragraphs (8/30). 3/30 address
  the data subject ("We obtain this data from you") because the record doubles as the source
  for the privacy notice; 1/30 is in the first person. 5/30 phrase column headings as questions
  ("With whom do we share this data?").
- **Recurring elements:**
  - The law or article behind a field cited in its heading: 11/30.
  - A review date, version or "next review" line: 24/30 (as `record-meta`).
  - "N/A" or "Not applicable" filling fields that do not apply, kept rather than deleted:
    most samples.
  - A fixed vocabulary for data categories repeated down the rows in most grids; drop-down
    lists behind it in 2/30.
  - Pointers to companion documents: a retention schedule (8/30), privacy notices (8/30).
- **Commonly omitted:** impact-assessment status (27/30), automated decisions (27/30), data
  source (18/30), systems and storage locations (18/30), joint controllers (18/30), named
  processors (15/30), a list of data subjects' rights (21/30), an introduction for smaller
  bodies' grids (9/30), field-level data lists (categories are the norm).

## Sections

Region-neutral. What one law requires (the legal grounds' names, conditions for sensitive data,
transfer safeguards, registration numbers, a separate processor record, a national registry) is
in the region's block, `regions/<code>/ropa.md`, written as extra columns and controller-block
lines (`formats/region-format.md`, tabular documents).

The record has two parts. The first three sections describe the record as a whole; the rest
are the fields of each activity, written once per activity, as grid columns or as a form.

### intro: About this record

- **Covers:** what the record is, why the company keeps it, and what it covers.
- **Prevalence:** 21/30 (70%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.product.services_in_scope`
- **Patterns:**
  - 1–3 sentences: the duty to keep a record, that it lists the processing activities, and
    that it is kept up to date and shown to the regulator on request.
  - 7/30 list the fields the record holds right after the duty sentence.
  - 6/30 say who maintains the record and who is accountable for each part.
  - 5/30 say whether the published copy is the full record or a summary of it.
- **Quote:** "Its purpose is to provide a detailed log of all personal data processing
  activities carried out by an organisation." (s03)
- **Commonly omitted:** any explanation of terms; the scope of what is not covered.

### controller: Controller and contacts

- **Covers:** who is responsible for the data, its contact details, and the data protection
  officer or privacy contact.
- **Prevalence:** 26/30 (87%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.company.country`,
  `facts.company.contact_email`, `facts.company.dpo_contact`, `facts.company.group_companies`
- **Patterns:**
  - 8/30 put one contact block above the grid or on the page that links it: name, address,
    email and phone for the controller, the DPO, and (4/30) a representative.
  - 9/30 repeat the controller and DPO in every activity's form.
  - 7/30 name the controller only in the title.
  - The DPO or privacy contact is a shared mailbox or a contact form, not a personal address
    (most forms); "Not applicable" when none is appointed (s28).
  - Forms name the internal unit or role that owns the activity next to the controller
    ("Internally: Head of ...").
- **Quote:** —
- **Commonly omitted:** a phone number; a personal name for the DPO.

### record-meta: Version and review

- **Covers:** when the record was made and last reviewed, by whom, when it is next reviewed,
  and open follow-up actions.
- **Prevalence:** 24/30 (80%), core
- **Applies when:** always
- **Facts:** `facts.company.privacy_owner`
- **Patterns:**
  - A "last updated", "completed" or "approved" date: 18/30; a version number: 5/30; a
    next-review date or interval: 5/30.
  - 4/30 number the grid's rows; 9/30 give each activity's form a record code.
  - 5/30 end with a sign-off: who completed it, who approved it (a committee or board), and
    when.
  - 3/30 keep edit history columns (created by, modified by, dates).
  - 4/30 record open actions or notes per row (an "Action needed" column, a notes column,
    risk level), or a closing to-do list.
  - 1/30 ends each record with the owner's declaration that it is accurate.
- **Quote:** "This document is reviewed monthly by the Trust Information Governance team and
  will be updated following review on a regular basis." (s01)
- **Commonly omitted:** a changelog; what triggers a review besides the calendar.

### activity: Activity

- **Covers:** the name of each processing activity; the unit every other field describes.
- **Prevalence:** 30/30 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.purposes`, `facts.product.features`, `facts.product.ai_features`,
  `facts.data.tracking`, `facts.marketing.email`, `facts.company.internal_activities`,
  `facts.company.collects_applicant_data`
- **Patterns:**
  - A 1–6 word name ("Payroll", "Customer support", "Newsletter"); forms add a code and a
    longer title.
  - The list covers the organisation's own operations (staff, recruitment, suppliers and
    invoices, correspondence, events) as well as its core service; staff and HR activities
    appear in nearly every sample.
  - 11/30 point from each activity to the privacy notice that covers it and say how people
    exercise their rights there, or list which rights apply.
  - 4/30 split one activity into several rows, one per data category.
- **Quote:** —
- **Commonly omitted:** the systems that carry the activity, in the name itself.

### owner: Owner

- **Covers:** the team, function or person accountable for the activity.
- **Prevalence:** 17/30 (57%), common
- **Applies when:** always
- **Facts:** `facts.company.privacy_owner`, `facts.company.internal_activities`
- **Patterns:**
  - A department or business function column (Finance, HR, Marketing): 9/17.
  - A named owner or role per row ("Information Asset Owner", "Data Owner", "Who is
    responsible for keeping it?"): 4/17.
  - Forms put the owning unit inside the controller field: 6/17.
- **Quote:** —
- **Commonly omitted:** a deputy; contact details per owner.

### purpose: Purpose

- **Covers:** why the data is processed in this activity, and how the processing runs.
- **Prevalence:** 29/30 (97%), core
- **Applies when:** always
- **Facts:** `facts.data.purposes`, `facts.product.features`
- **Patterns:**
  - A 2–6 word label: 11/29; one to three sentences: 8/29; paragraphs that walk through the
    process step by step (forms): 8/29; folded into the activity name: 2/29.
  - 4/30 split a main purpose into sub-purposes; 1/30 adds further uses such as archiving,
    research or statistics.
  - Forms state what the record does not cover and point to the record that does.
  - 1/30 lists the operations performed (collect, record, store, transmit, erase).
- **Quote:** "So that we can administer and provide your course." (s02)
- **Commonly omitted:** the systems and vendors involved (left to `processors` and
  `storage`).

### legal-basis: Legal ground

- **Covers:** the ground the applicable law gives for the activity, and what supports it.
- **Prevalence:** 25/30 (83%), core
- **Applies when:** always
- **Facts:** `facts.data.purposes`, `facts.data.sensitive`
- **Patterns:**
  - A separate field or column: 20/25; folded into the purpose field: 5/25.
  - One or two short labels per activity (contract, legal obligation, consent, legitimate
    interests, public task): 11/25; the ground written out in the law's own words: 9/25.
  - 9/25 name the statute, contract or mandate behind the ground.
  - 5/25 explain a legitimate interest in a sentence.
  - Where consent is the ground, 4/30 say how it is obtained or where consents are recorded.
  - Regional additions name the grounds and their articles.
- **Quote:** —
- **Commonly omitted:** why the ground was chosen over another.

### data-subjects: Data subjects

- **Covers:** whose data the activity handles.
- **Prevalence:** 29/30 (97%), core
- **Applies when:** always
- **Facts:** `facts.data.subject_categories`, `facts.product.child_directed`
- **Patterns:**
  - 1–4 group labels per activity (customers, users, employees, job applicants, suppliers,
    members of the public), from a short fixed list in most grids.
  - 3/30 use the subject group as the grid's grouping instead of a column.
  - Forms split subjects into internal and external, or separate administrative from
    operational subjects.
- **Quote:** —
- **Commonly omitted:** counts of people; children as a separate group unless the service
  targets them.

### data-categories: Personal data

- **Covers:** which personal data the activity uses.
- **Prevalence:** 30/30 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.collected`
- **Patterns:**
  - Categories, not fields, in most grids ("contact details", "financial details",
    "employment record"), often from a fixed vocabulary repeated across rows.
  - Forms and small grids list example fields in brackets or as bullets (name, address,
    bank account, IP address).
  - 2/30 give a retention period per data category inside this field.
  - 2/30 mark which fields are optional and which are required.
- **Quote:** "Uses patient and staff personal, health and employment data." (s01)
- **Commonly omitted:** volumes; data that is not personal.

### sensitive-data: Sensitive data

- **Covers:** whether the activity involves sensitive data (health, biometrics, beliefs,
  ethnicity, sex life, criminal records and the like), which, and what allows it.
- **Prevalence:** 19/30 (63%), common
- **Applies when:** `facts.data.sensitive` is not empty
- **Facts:** `facts.data.sensitive`, `facts.product.child_directed`
- **Patterns:**
  - A yes/no flag with the types in brackets: 3/19.
  - The types listed inside the personal-data field: 6/19.
  - A separate column or field for the condition that allows it, with a short explanation:
    10/19; criminal-record data gets its own column in 5/19.
  - Regional additions name the conditions.
- **Quote:** —
- **Commonly omitted:** sensitive data that is only incidental (in free-text messages).

### source: Source

- **Covers:** where the data comes from and how it is collected.
- **Prevalence:** 12/30 (40%), common
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.data.third_party_sources`
- **Patterns:**
  - Fixed phrases repeated across rows: "from you", "we generate it", "from <named body>",
    "from third parties".
  - 3/12 add the channel or moment of collection (form, email, on application).
- **Quote:** "We obtain this data from the University of Oxford." (s02)
- **Commonly omitted:** the specific third parties.

### recipients: Recipients

- **Covers:** who receives the data, inside and outside the company.
- **Prevalence:** 26/30 (87%), core
- **Applies when:** always
- **Facts:** `facts.processors.list`, `facts.data.other_recipients`,
  `facts.company.group_companies`, `facts.product.public_content`,
  `facts.product.integrations`
- **Patterns:**
  - Kinds of recipient ("payroll provider", "tax authority", "auditors", "police where
    required"), several per row; forms add internal roles on a need-to-know basis.
  - Many grids name bodies (tax office, regulators, banks) and some name vendors.
  - 3/30 give the purpose of each disclosure beside the recipient.
  - Forms close with a stock line on auditors, courts and oversight bodies that may receive
    data in specific cases.
  - 1/30 asks whether a data-sharing agreement exists for routine sharing.
- **Quote:** "The processors listed in section 6 may have access to the personal data for the
  purpose of fulfilling their tasks." (s04)
- **Commonly omitted:** each recipient's country (left to `transfers`).

### processors: Service providers

- **Covers:** the providers that process data for the company in this activity, and the
  contract that binds them.
- **Prevalence:** 15/30 (50%), common
- **Applies when:** `facts.processors.list` is not empty
- **Facts:** `facts.processors.list`
- **Patterns:**
  - Named providers with what they do (helpdesk, e-recruitment, hosting), sometimes their
    address or country.
  - 3/15 have a "link to the contract with the processor" column (left empty in the
    published copies).
  - 1/15 keeps a separate providers table with a "data processing agreement in place?"
    column and notes on providers that act as independent controllers.
- **Quote:** —
- **Commonly omitted:** sub-processors; contract dates.

### joint-controllers: Joint controllers

- **Covers:** organisations that decide the purposes of the activity together with the
  company.
- **Prevalence:** 12/30 (40%), common
- **Applies when:** `facts.company.joint_controllers` is not empty
- **Facts:** `facts.company.joint_controllers`
- **Patterns:**
  - A field or column kept in every row, "Not applicable" in nearly all of them; filled rows
    give the partner's name, address and mailbox, and who answers people's requests.
- **Quote:** —
- **Commonly omitted:** how responsibilities are split between the controllers.

### transfers: Transfers abroad

- **Covers:** whether data leaves the country or region, to where, and under what safeguard.
- **Prevalence:** 19/30 (63%), common
- **Applies when:** always
- **Facts:** `facts.data.storage_locations`, `facts.processors.list`, `facts.company.country`
- **Patterns:**
  - "No transfers" on most rows; a yes/no column plus a destinations-and-safeguards column in
    grids, one field in forms.
  - Filled rows name the country and the provider, then the safeguard in one phrase.
  - 1/30 has only a "country where data is processed" column.
  - Regional additions name the safeguards.
- **Quote:** —
- **Commonly omitted:** onward transfers by providers' sub-processors.

### retention: Retention

- **Covers:** how long the data is kept, and what happens to it after.
- **Prevalence:** 30/30 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.retention`, `facts.data.deletion_lag`
- **Patterns:**
  - A period with its trigger per activity ("6 years after employment ends", "12 months after
    the end of the application cycle"): 25/30.
  - Only a pointer to a retention schedule: 5/30.
  - Periods split by outcome or group (successful vs unsuccessful applicants) are common in
    HR rows.
  - 5/30 say what happens after: destroy, archive or anonymise, and how.
  - 1/30 asks whether data is actually deleted on time ("To be developed" in some rows).
- **Quote:** "Data are kept for two years after the notification of the outcome of the
  application (deadline for lodging possible complaints)." (s24)
- **Commonly omitted:** backups; the reason for each period.

### security: Security measures

- **Covers:** the technical and organisational measures that protect the data.
- **Prevalence:** 21/30 (70%), common
- **Applies when:** always
- **Facts:** `facts.data.security_measures`
- **Patterns:**
  - Short generic phrases per row (access controls, encryption, password protection, locked
    cabinet); forms open with a boilerplate sentence, then one or two activity-specific
    measures.
  - 1/30 lists the measures once for the whole organisation instead of per activity.
  - 2/30 write the measures as instructions to staff ("Not to be shared", "Clerk to retain in
    a secure place").
- **Quote:** "The Agency has put appropriate technical and organisational measures (security
  policies and procedures) in place to protect personal data from accidental or unlawful
  destruction, loss, alteration, unauthorised disclosure or access." (s04)
- **Commonly omitted:** named standards or certifications; incident handling.

### storage: Systems and storage

- **Covers:** the systems, services and media where the data is held.
- **Prevalence:** 12/30 (40%), common
- **Applies when:** always
- **Facts:** `facts.data.storage_locations`, `facts.processors.list`
- **Patterns:**
  - Named systems or providers (HR system, CRM, shared drive, cloud service) and paper files.
  - Forms use tick boxes for paper, network drive, database, cloud, provider's premises.
- **Quote:** —
- **Commonly omitted:** hosting regions (left to `transfers`).

### dpia: Impact assessment

- **Covers:** whether the activity needs a privacy impact assessment, and its status.
- **Prevalence:** 3/30 (10%), rare
- **Applies when:** `facts.data.dpia_done` has an entry with status `planned` or `done`
- **Facts:** `facts.data.dpia_done`
- **Patterns:**
  - A yes/no column, a status (completed, in progress) and a link; or a note in the notes
    column ("DPIA completed 2024").
  - 1/30 states the rule on the record's front page: new projects need an assessment before
    anything is bought.
- **Quote:** —
- **Commonly omitted:** the assessment's findings.

### automated-decisions: Automated decisions

- **Covers:** whether the activity makes decisions about people by automated means alone,
  including profiling.
- **Prevalence:** 3/30 (10%), rare
- **Applies when:** `facts.data.automated_decisions == true`
- **Facts:** `facts.data.automated_decisions`, `facts.product.ai_features`
- **Patterns:**
  - A yes/no field, "No" on nearly every row, with a details field for the rows that say yes.
- **Quote:** —
- **Commonly omitted:** the logic involved.

### processor-activities: Processing for customers

- **Covers:** activities the company performs on behalf of business customers who decide the
  purposes.
- **Prevalence:** 2/30 (7%), rare
- **Applies when:** `facts.company.acts_as_processor == true`
- **Facts:** `facts.company.acts_as_processor`, `facts.processors.list`
- **Patterns:**
  - A role column (controller, joint controller, processor) per row: 2/30. One regulator
    model also offers a separate template for this record.
  - Rows for customer work name the customer category, the service and the sub-processors.
- **Quote:** —
- **Commonly omitted:** individual customers' names.

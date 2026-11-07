---
doc_id: ropa
title: Record of Processing Activities, European Union part
kind: document
family: internal-compliance
region: eu
part: block
sample_languages: [en]
sample_count: 15
saturated: false
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** What the GDPR (Art. 30) adds to the record for a company whose users include
  people in the EU/EEA: its contact set, the legal-basis and transfer vocabulary, and the
  separate record a processor keeps.
- **Shape:**
  - The record is a table, so this block is extra columns, not a section (PLAN decision 37).
    Each per-activity section below is one column added to the root grid after the root's
    columns, its heading starting with "EU:" (*Column*). The record-level sections (`eu-law`,
    `eu-controller`) are lines added to the root's controller block, each starting with "EU:"
    (*Header line*). Removing the region deletes those columns and lines and nothing else. No
    sample gives the EU content a part of its own either: 15/15 put it in the record's own
    columns or fields.
  - 10 of the 15 are real records: 2 under the GDPR (an Irish council, an Irish university)
    and 8 EU institutions' registers under the EUDPR, Reg. (EU) 2018/1725, whose record mirrors
    the GDPR's (tagged EUDPR in the research). 5 are models from regulators and one
    association (CNIL, Finland, Cyprus, Ireland's DPC, the GAA). The EUDPR registers count
    toward prevalence; wording and article numbers come only from the GDPR samples.
- **Register:** the GDPR's own terms: "controller", "processor", "third country",
  "international organisation", "special categories of personal data", "technical and
  organisational measures".
- **Recurring elements:**
  - Fields marked as required or conditional ("(if applicable)", "(if designated)",
    asterisks, or bands of mandatory and optional columns): 7/15. The DPC asks for this so
    a reader sees which fields Art. 30 prescribes and which are extras.
  - Article cited in field headings ("Purposes of processing [Article 30(1)(b)]"): 6/15.
  - "N/A" kept in fields that do not apply (representative, joint controller, transfers):
    every model and most registers.
  - The DPC model notes that the exemption for firms under 250 staff (Art. 30(5)) does not
    cover processing that is not occasional, such as payroll, so a company with staff keeps
    a record (s06).
- **Commonly omitted:** DPIA and prior-consultation columns (1/15), a main-or-auxiliary flag
  (1/15), the Art. 30(5) exemption reasoning in the record itself.

Counts come from 15 samples (`research/regions/eu/ropa/`). The pool ran out at one first
batch, so no saturation batch could run (`saturated: false`); the last 10 samples in pool
order added no new section.

## Sections

### eu-law: Law and regulator

- **Covers:** the EU law the record is kept under and that it is shown to the supervisory
  authority on request.
- **Header line:** "EU: kept under GDPR Art. 30; shown to the supervisory authority on
  request."
- **Prevalence:** 13/15 (87%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`
- **Patterns:**
  - The law named in the title, the opening line or the help text: 13/13 (the GDPR in 6, the
    EUDPR's Art. 31 in 7).
  - 2/13 cite the article in the title ("under GDPR Article 30").
- **Quote:** "The following is a log of processing activities undertaken by the St Mary's GAA
  Club, as defined under the General Data Protection Regulation" (s07)
- **Commonly omitted:** why the record is needed despite the exemption for firms under 250
  staff.

### eu-controller: DPO and EU representative

- **Covers:** the parts of Art. 30(1)(a)'s contact set beyond the controller: the data
  protection officer, and the Art. 27 representative for a company with no EU establishment.
- **Header line:** "EU: Representative (GDPR Art. 27)" (name, address, email, telephone), or
  "N/A"; the DPO is the root's controller-block line.
- **Prevalence:** 14/15 (93%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`,
  `facts.company.contact_email`, `facts.company.dpo_contact`, `facts.eu.representative`
- **Patterns:**
  - A DPO block: 13/15; a representative block: 4/15, all of them regulator models, which
    set it beside the controller and DPO (name, address, email, phone) and keep it when
    empty ("N/A", "If relevant").
  - None of the samples fills the representative; all are EU bodies or blank models.
  - The DPO is one shared mailbox or contact form, the same in every record: 9/13. The DPC
    wants role mailboxes over personal ones, and an external DPO's firm named.
  - 1/15 uses one "capacity" column (controller, processor, representative) with the
    name and contact beside it; every other sample keeps these in the header.
- **Quote:** "Personal emails are not recommended due to personnel changes." (s06)
- **Commonly omitted:** the representative field (11/15, since EU bodies need none); the DPO's
  personal name.

### eu-legal-basis: Legal basis under the GDPR

- **Covers:** the Art. 6(1) basis for each activity in the GDPR's terms, and the law behind
  it where the basis is a legal obligation.
- **Column:** "EU: Lawful basis (GDPR Art. 6)"
- **Prevalence:** 10/15 (67%), common
- **Applies when:** always
- **Facts:** `facts.data.purposes`, `facts.company.internal_activities`,
  `facts.company.country`
- **Patterns:**
  - A field of its own: 6/10; inside the purpose field: 4/10.
  - Among the GDPR samples: the article point plus a short name, one or two per activity
    ("6(1)(b) Contract", "6(1)(f) Legitimate interests") in the DPC model; the point quoted
    in full in the council record. Write the point plus short name.
  - 9/10 name the law behind the basis (an employment or tax act, a founding regulation),
    2 of them in a column of their own. Name it only when the user gives it.
  - The two models that keep to Art. 30's list (CNIL, Finland) leave the basis out; the DPC
    types it "recommended", not required.
- **Quote:** "Article 6(1)(c) Legal Obligation" (s06)
- **Commonly omitted:** the legitimate-interests balancing; why one basis was chosen over
  another.

### eu-special-categories: Special categories and criminal data

- **Covers:** whether the activity uses data in the Art. 9 special categories or Art. 10
  criminal-offence data, and the Art. 9(2) condition relied on.
- **Column:** "EU: Art. 9 / Art. 10 data and condition"
- **Prevalence:** 8/15 (53%), common
- **Applies when:** `facts.data.sensitive` is not empty
- **Facts:** `facts.data.sensitive`
- **Patterns:**
  - 3/8 name the condition relied on: a column beside the basis, a checklist of the allowing
    grounds, or added in the basis cell ("Article 9(2)(b)").
  - 4/8 name criminal-offence data apart from the special categories.
  - 3/8 list the categories as fixed rows or a checklist (one with a retention per
    category); 2/8 only flag them inside the data field.
  - Uses the Art. 9 list's wording (health, racial or ethnic origin, trade union membership,
    biometric data) rather than "sensitive".
- **Quote:** "Legal basis for processing special category data [Article 9]" (s01)
- **Commonly omitted:** the member-state law behind an Art. 9(2)(b), (g) or (j) condition.

### eu-transfers: Transfers to third countries

- **Covers:** for each activity, whether data goes to a country outside the EEA or to an
  international organisation, which one, and the Chapter V safeguard.
- **Column:** "EU: Transfers out of the EEA (country or organisation, safeguard)"; "No
  transfers outside the EEA" on rows without one
- **Prevalence:** 14/15 (93%), core
- **Applies when:** always
- **Facts:** `facts.data.storage_locations`, `facts.processors.list`,
  `facts.eu.transfer_mechanisms`, `facts.eu.dpf`
- **Patterns:**
  - One field asking where to and with which safeguard: 7/14; destination and safeguard in
    separate columns: 4/14; yes/no plus a checklist of transfer grounds: 2/14; a paragraph
    for the whole record: 1/14.
  - Rows without a transfer say so ("No transfers outside the European Economic Area") rather
    than leave the cell empty: 8/14. Finland's heading asks for that statement.
  - The safeguard is one term from a short list: adequacy decision, standard contractual
    clauses, binding corporate rules, code of conduct, certification, an Art. 49 derogation
    (a fixed list in 4/14). Name the EU-U.S. Data Privacy Framework only when `facts.eu.dpf` is true.
  - 2/14 ask for the documentation of suitable safeguards for an Art. 49(1)
    second-subparagraph transfer; 10/14 name international organisations beside third
    countries.
  - The DPC warns against naming an expired mechanism (Privacy Shield).
- **Quote:** "Depending on the circumstances, these safeguards may include an adequacy
  decision, Standard Contractual Clauses, or another lawful transfer mechanism." (s03)
- **Commonly omitted:** onward transfers by a provider's sub-processors; a link to the
  signed clauses (1/14, CNIL).

### eu-processor-record: Record as processor

- **Covers:** the separate Art. 30(2) record for processing done on behalf of business
  customers: each customer controller, the categories of processing done for it, transfers,
  and security measures.
- **Column:** "EU: Controller we act for" on the root's `processor-activities` rows, plus the
  root's transfer and security columns for those rows
- **Prevalence:** 4/15 (27%), rare
- **Applies when:** `facts.company.acts_as_processor == true`
- **Facts:** `facts.company.acts_as_processor`, `facts.company.processor_customers`,
  `facts.processors.list`, `facts.company.dpo_contact`, `facts.eu.representative`,
  `facts.eu.transfer_mechanisms`, `facts.data.security_measures`
- **Patterns:**
  - All 4 are GDPR samples; no EU institution's register publishes a processor record.
  - 1/4 offers a separate processor template beside the controller one; 2/4 add a role column
    (controller, joint controller, processor) to the controller grid; the DPC lists the four
    processor fields in its guidance.
  - Organised by customer first, then the categories of processing for each; in the grid,
    one row per customer or customer category.
  - Customers are named with contact details, or by customer category with a pointer to the
    customer list when they are many.
- **Quote:** "It is recommended that processors start with each controller they are
  processing data for, and then the breakdown of the different categories of personal data
  they are processing for each controller." (s06)
- **Commonly omitted:** purposes, data subjects and retention (Art. 30(2) does not ask for
  them; the customer decides).

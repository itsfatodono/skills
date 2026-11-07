# ropa: proposed fact keys

Merged into `helpers/facts-schema.md` on 2026-10-26; see the key map below.

Keys the `ropa` skeleton names that `helpers/facts-schema.md` lacks. Each is in the format of a
`helpers/facts-schema.md` entry, under its intended shared name. Checked against `helpers/facts-schema.md`,
`regions/*/facts.md` and the other items' `proposed-facts.md` on 2026-10-26: no existing key
has the same meaning. Transfer safeguards stay in the regions' own keys
(`facts.eu.transfer_mechanisms`, `facts.uk.transfer_mechanisms`).

### facts.company.internal_activities
- **Means:** processing the company does for running itself rather than for the product:
  staff and payroll, recruitment, contractors, suppliers and bookkeeping, customer support,
  sales contacts, events.
- **Type:** list of (activity, data subjects, data, tool or provider)
- **Look:** existing legal docs (privacy policy, job pages); careers pages and application
  forms in the website code; support desk, CRM and accounting SDKs or integrations (Zendesk,
  Intercom, HubSpot, Xero, Stripe Billing). Payroll and HR are not in code.
- **Ask:** "Besides the product, which of these do you handle: staff and payroll, job
  applicants, contractors, suppliers and invoices, customer support, sales leads? For each,
  which tool do you use?" Recommend the activities the scan found plus "suppliers and
  invoices", which every company has; ask about staff only when the company has employees.

### facts.data.subject_categories
- **Means:** the groups of people whose personal data the company processes.
- **Type:** list of enum [users, customers, website-visitors, newsletter-subscribers,
  children, employees, job-applicants, contractors, supplier-contacts, business-contacts,
  other]
- **Look:** account and profile models (users), payment and billing code (customers),
  analytics on the website (visitors), newsletter forms, careers pages, team or B2B features.
- **Ask:** "Whose personal data do you hold? The scan found: <list>." Recommend the scanned
  list plus supplier contacts.

### facts.data.other_recipients
- **Means:** parties other than the company's processors that receive personal data:
  independent controllers (payment networks, app stores, banks, accountants, auditors),
  public authorities (tax office, regulators), partners, and other users or the public where
  the product shows data to them.
- **Type:** list of (recipient, role [independent-controller, public-authority, partner,
  other-users, public], data, purpose)
- **Look:** payment and app-store integrations, tax and invoicing integrations, partner API
  clients, sharing and publishing features.
- **Ask:** "Apart from your service providers, who receives personal data from you (app
  stores, payment networks, accountants, tax office, partners)?" Recommend the scanned list
  plus the tax authority for invoicing data.

### facts.company.joint_controllers
- **Means:** other organisations that decide together with the company why and how some
  personal data is processed (a co-branded service, a research partner, a parent company that
  sets the purposes).
- **Type:** list of (name, contact, activity)
- **Look:** existing legal docs; partner agreements. Not in code.
- **Ask:** "Do you decide jointly with another organisation why and how any personal data is
  used (a co-branded service, a shared programme)? Name each." Recommend "none".

### facts.company.acts_as_processor
- **Means:** whether the company processes personal data on behalf of business customers,
  who decide the purposes (a B2B SaaS holding its customers' end users' data).
- **Type:** bool
- **Look:** team, workspace or organisation features where a customer's admin controls other
  people's accounts; a customer DPA among existing legal docs; business plans in pricing.
- **Ask:** "Do business customers use the product to handle their own people's data (their
  staff, their clients), with you acting on their instructions?" Recommend "yes" when
  workspace or admin features exist.

### facts.company.privacy_owner
- **Means:** the person or role who keeps the record of processing up to date, and how often
  it is reviewed.
- **Type:** record (role, name, review interval)
- **Look:** existing legal docs; CODEOWNERS or security contacts. Not otherwise in code.
- **Ask:** "Who keeps this record up to date, and how often will it be reviewed?" Recommend
  the founder or DPO, reviewed every 12 months and whenever a new feature or provider handles
  personal data.

### facts.data.dpia_done
- **Means:** impact assessments done or planned, per activity.
- **Type:** list of (activity, status [not-needed, planned, done], date or link)
- **Look:** existing legal docs (`legal/` DPIA files). Not in code.
- **Ask:** "Have you assessed the privacy risk of any activity (a DPIA)? Which, and when?"
  Recommend "not needed" except for activities on sensitive data, children's data, or
  large-scale tracking, for which recommend "planned".

## Key map

| Proposed | Final | Note |
| --- | --- | --- |
| `facts.company.internal_activities` | `facts.company.internal_activities` |  |
| `facts.data.subject_categories` | `facts.data.subject_categories` |  |
| `facts.data.other_recipients` | `facts.data.other_recipients` |  |
| `facts.company.joint_controllers` | `facts.company.joint_controllers` |  |
| `facts.company.acts_as_processor` | `facts.company.acts_as_processor` |  |
| `facts.company.privacy_owner` | `facts.company.privacy_owner` |  |
| `facts.data.dpia_done` | `facts.data.dpia_done` |  |

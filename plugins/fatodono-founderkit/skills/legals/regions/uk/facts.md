# UK fact keys

Keys only the `uk` region uses, in the format of `helpers/facts-schema.md`.

### facts.uk.representative
- **Means:** the UK GDPR Art. 27 representative, for a company with no UK establishment.
- **Type:** record (name, address, email or web form)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Have you appointed a UK representative? If so, give its name and contact." Recommend "none" when `facts.company.country` is GB.

### facts.uk.transfer_mechanisms
- **Means:** the legal tools used for transfers out of the UK.
- **Type:** list of enum [adequacy, idta, uk-addendum, dpf, consent, other]
- **Look:** processors' DPAs; not in code.
- **Ask:** "Which legal tools cover transfers of UK users' data out of the UK?" Recommend the UK Addendum to the SCCs, which processors' DPAs normally include.

### facts.uk.dpf
- **Means:** whether the company is certified under the UK Extension to the EU-U.S. Data Privacy Framework.
- **Type:** bool
- **Look:** existing legal docs; dataprivacyframework.gov list. Not in code.
- **Ask:** "Is the company certified under the UK Extension to the Data Privacy Framework?" Recommend "no" unless the user confirms a listing.

### facts.uk.legitimate_interests
- **Means:** for each purpose based on legitimate interests, the interest in one sentence and the assessment (LIA) that weighs it against people's rights.
- **Type:** list of (purpose, interest, assessment link or date)
- **Look:** purposes in `facts.data.purposes` whose basis is legitimate interests; existing legal docs. Not otherwise in code.
- **Ask:** "For <purpose>, what is the interest you rely on, and have you written down why it does not override users' rights?" Recommend one sentence per purpose (fraud prevention, security, product analytics), and an assessment for any purpose users would not expect.
- **Proposed shared key:** `facts.data.legitimate_interests` (the EU GDPR asks the same).

### facts.uk.special_conditions
- **Means:** for each kind of special-category or criminal-offence data, the UK GDPR Art. 9(2) condition and, where one is needed, the Data Protection Act 2018 Schedule 1 condition relied on.
- **Type:** list of (category, purpose, Art. 9 condition, Schedule 1 condition or none)
- **Look:** `facts.data.sensitive`; not otherwise in code.
- **Ask:** "For <sensitive data>, which condition allows it?" Recommend explicit consent (Art. 9(2)(a), no Schedule 1 condition) for user features such as health data, and the employment condition (Art. 9(2)(b), Schedule 1 Part 1 paragraph 1) for staff data.

### facts.uk.appropriate_policy
- **Means:** the appropriate policy document that DPA 2018 Schedule 1 Part 4 requires when a Schedule 1 condition is relied on: whether it exists, where, and when it was last reviewed.
- **Type:** record (exists bool, link, review date)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Do you have an appropriate policy document for the sensitive data you rely on a Schedule 1 condition for?" Recommend writing one when `facts.uk.special_conditions` names a Schedule 1 condition; none is needed for explicit consent alone.

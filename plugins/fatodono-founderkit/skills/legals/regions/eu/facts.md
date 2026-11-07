# EU fact keys

Keys only the `eu` region uses, in the format of `helpers/facts-schema.md`.

### facts.eu.representative
- **Means:** the GDPR Art. 27 representative in the EU, for a company with no EU establishment.
- **Type:** record (name, address, email or web form)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Have you appointed an EU representative under GDPR Art. 27? If so, give its name and contact." Recommend "none" when `facts.company.country` is in the EU.

### facts.eu.transfer_mechanisms
- **Means:** the legal tools used for transfers out of the EEA.
- **Type:** list of enum [adequacy, scc, dpf, consent, other]
- **Look:** processors' DPAs; not in code.
- **Ask:** "Which legal tools cover transfers of EU users' data out of the EEA?" Recommend SCCs, which processors' DPAs normally include.

### facts.eu.dpf
- **Means:** whether the company is certified under the EU-U.S. Data Privacy Framework.
- **Type:** bool
- **Look:** existing legal docs; dataprivacyframework.gov list. Not in code.
- **Ask:** "Is the company certified under the EU-U.S. Data Privacy Framework?" Recommend "no" unless the user confirms a listing.

### facts.eu.consent_age
- **Means:** the age below which EU users need parental consent for the service (GDPR Art. 8).
- **Type:** number (13–16)
- **Look:** age gates in code. Not otherwise in code.
- **Ask:** "Below which age do EU users need a parent's consent?" Recommend 16, the highest member-state age, unless parental consent is collected.

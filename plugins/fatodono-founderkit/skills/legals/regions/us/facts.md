# US fact keys

Keys only the `us` region uses, in the format of `helpers/facts-schema.md`.

### facts.us.sells_or_shares
- **Means:** whether personal data is "sold" or "shared" as US state laws define it, which
  includes giving identifiers to ad partners for cross-context advertising.
- **Type:** bool
- **Look:** ad and attribution SDKs that share identifiers, ad pixels, data-broker integrations.
- **Ask:** "Do you give users' data to ad partners for targeted advertising, or sell it?" Recommend "yes" when an ad or attribution SDK is present.

### facts.us.appeal_process
- **Means:** how a consumer appeals when the company declines a privacy request, as most US state
  privacy laws require: where the appeal is sent, how long the company takes to decide, and
  whether a denied appeal points to the state attorney general.
- **Type:** record (channel: string, decision_days: number or none, attorney_general_link: bool)
- **Look:** the US section of the existing privacy policy; an "appeal" request type in the
  privacy-request form or portal; the privacy email. Not in code otherwise.
- **Ask:** "If you turn down a privacy request from a US user, how can they appeal, and how
  quickly do you decide?" Recommend the privacy email (or an "Appeal" option in the request
  form), a decision within 45 days, and a link to the attorney general's complaint page if the
  appeal is denied.

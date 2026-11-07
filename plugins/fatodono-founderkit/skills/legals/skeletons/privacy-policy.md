---
doc_id: privacy-policy
title: Privacy Policy
kind: document
family: privacy-notices
sample_languages: [en]
sample_count: 32
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** Tells users what personal data the product collects, why, who receives it, how
  long it is kept, and what control they have over it.
- **Shape:**
  - 32/32 one long web page; median 5,250 words (range 550–9,000).
  - 15/32 number their sections; 5/32 phrase every heading as a reader's question ("What
    information do we collect?").
  - 10/32 open with a table of contents; 7/32 with a key-points summary of 4–6 one-line
    promises; 4/32 open each section with a one-line summary before the full text.
  - 12/32 use at least one table (data inventory, purposes per category, processors, retention).
  - 8/32 push regional or detailed content to linked companion pages (regional notices,
    cookie policy, FAQ); 5/32 append annexes or product supplements at the end.
  - 2/32 are generator texts (privacypolicygenerator.info, iubenda) with the company's own
    parts added; 1 of them is served in an iframe from the generator's host.
- **Register:** 31/32 "we/you"; 1/32 (a generator text) third person ("the Owner", "the
  User"). 23/32 plain, medium-length sentences; 6/32 formal legal drafting throughout; 3/32 a
  deliberate brand voice with jokes. The register rises in the regional
  sections in most samples. Heavy "may" hedging is common.
- **Recurring elements:**
  - "Last updated" or "Effective" date: 31/32 (25 at the top, 6 at the bottom).
  - Defined terms in the opening ("Services", "we", "you"): 22/32.
  - "We do not sell your personal information" stated at least once: 15/32, often repeated.
  - One privacy email repeated as the channel in several sections: 15/32.
  - Settings paths or links to help pages for each control: 15/32.
  - Cross-references by section title: 13/32.
  - Link to the previous version: 6/32; a changelog of the last revision: 4/32.
- **Commonly omitted:** processor names (23/32 give categories only); field-level data lists;
  concrete retention periods for every category (19/32 give none); named security standards
  (27/32); a definitions block (26/32); privacy request statistics (31/32); job applicants
  (29/32).

## Sections

Region-neutral. What one law requires is in the region's block, `regions/<code>/privacy-policy.md`,
written under the document's regional part (`formats/region-format.md`).

### intro-scope: About this policy

- **Covers:** who the policy is from, which apps, sites and services it covers, and what it
  leaves to other documents.
- **Prevalence:** 32/32 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.product.services_in_scope`
- **Patterns:**
  - 22/32 define "Services" (or a brand term) and "we/you" in the first paragraph.
  - 10/32 open with a values or mission line before any fact.
  - 8/32 name what the policy does not cover: other group brands, third-party sites,
    processing done as a processor for business customers.
  - 7/32 say the policy is part of, or read with, the Terms of Service.
  - 6/32 treat use of the product as consent to the policy.
- **Quote:** "This Privacy Policy does not cover the practices of companies we don't own or control or people we don't manage." (s20)
- **Commonly omitted:** a list of the policy's own sections in prose; a legal framework
  statement naming the governing law (3/32).

### controller: Who we are

- **Covers:** the legal entity responsible for the data, and its address.
- **Prevalence:** 28/32 (88%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.country`, `facts.company.address`, `facts.company.group_companies`
- **Patterns:**
  - Placement splits: 11/28 name the entity in the opening paragraph; 10/28 in the contact or a
    regional part; 7/28 give it its own section.
  - 6/28 name a different entity for some regions; that entity belongs to the regional part.
  - 4/28 add the company registration number.
- **Quote:** "If you are outside of the Designated Countries, LinkedIn Corporation will be the controller of (or business responsible for) your personal data." (s10)
- **Commonly omitted:** the word "controller" outside the regional part; the reason for each
  entity's role.

### data-collected: Data we collect

- **Covers:** the categories of personal data collected, with examples, and what triggers each.
- **Prevalence:** 32/32 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.product.has_accounts`, `facts.product.features`
- **Patterns:**
  - Grouping splits: 13/32 by labelled category (account, usage, device, payment); 11/32 by
    source (you give us / collected automatically / from others); 6/32 by product feature;
    2/32 by collection moment (sign-up, use, optional).
  - 24/32 name categories with "such as" examples; 5/32 give field-level lists.
  - 5/32 put the inventory in a table (category, examples, purpose, recipients).
  - 10/32 say which data is optional and what happens if it is not given.
  - 6/32 open with a data-minimisation statement before the list.
- **Quote:** "Not all categories of personal information will be collected or received about every individual." (s16)
- **Commonly omitted:** SDK names; field-level lists for usage and device data; data kept only
  on the device, unless the product is privacy-led.

### data-sources: Data from other sources

- **Covers:** data about users received from third parties: sign-in providers, partners, app
  stores, other users, public sources.
- **Prevalence:** 19/32 (59%), common
- **Applies when:** `facts.data.third_party_sources != []`
- **Facts:** `facts.data.third_party_sources`
- **Patterns:**
  - 14/19 give source types, not company names; 5/19 name the social sign-in providers and the
    exact fields received.
  - 9/19 make it a subsection of *Data we collect*; 10/19 a section of its own.
  - 5/19 cover contact uploads by other users, often with a hashing explanation.
- **Quote:** "We'll ask your permission before we collect your information from certain third parties." (s01)
- **Commonly omitted:** how long third-party data is kept; which purposes each source feeds.

### sensitive: Sensitive data

- **Covers:** special-category or sensitive data (health, biometric, precise location, sexual
  life), why it is processed and the consent behind it.
- **Prevalence:** 9/32 (28%), rare
- **Applies when:** `facts.data.sensitive != []`
- **Facts:** `facts.data.sensitive`
- **Patterns:**
  - 6/9 flag sensitive items inline in the data list ("This is considered health data");
    3/9 give a section of their own.
  - 5/9 tie it to consent given by choosing to provide the data, with removal at any time.
  - 3/9 give a fixed deletion period for biometric data.
- **Quote:** "If you provide us with sensitive information, we will consider that you have consented to us collecting it." (s12)
- **Commonly omitted:** a definition of "sensitive" under each law.

### purposes: How we use data

- **Covers:** the purposes for which data is used.
- **Prevalence:** 31/32 (97%), core
- **Applies when:** always
- **Facts:** `facts.data.purposes`, `facts.product.ai_features`
- **Patterns:**
  - 18/31 a verb-led bullet list ("To provide...", "To improve..."), often grouped under
    themed headings.
  - 9/31 map each purpose to the data categories it uses (as a closing list, a table, or
    per-service blocks).
  - 4/31 fold purposes into each data category or feature instead of a separate section.
  - 10/31 name model training or AI features as a purpose.
- **Quote:** "We use your personal information to provide, maintain, improve, and promote the Netflix service, and to communicate with you." (s13)
- **Commonly omitted:** purposes per individual field; a promise not to add purposes without
  notice (2/31).

### automated-ai: Automated decisions and AI

- **Covers:** profiling, automated decisions with significant effects, and AI features and
  model training on user data.
- **Prevalence:** 15/32 (47%), common
- **Applies when:** `facts.product.ai_features != []` or `facts.data.automated_decisions == true`
- **Facts:** `facts.product.ai_features`, `facts.data.automated_decisions`
- **Patterns:**
  - 7/15 state that no decisions with legal or similar effects are made automatically.
  - 9/15 disclose AI or model training on user data; 5/15 give a no-training promise for
    user content or chat inputs.
  - 5/15 per AI feature: where processing runs, what is sent, which provider.
  - 2/15 mention human review of automated moderation.
- **Quote:** "None of them uses your content to train content-producing artificial intelligence." (s27)
- **Commonly omitted:** the right to contest an automated decision; model provider names.

### deidentified: De-identified and aggregated data

- **Covers:** creation and use of data that no longer identifies anyone.
- **Prevalence:** 12/32 (38%), rare
- **Applies when:** `facts.data.deidentified_use == true`
- **Facts:** `facts.data.deidentified_use`
- **Patterns:**
  - 8/12 one or two sentences inside *How we use*, *Who we share with* or a feature notice.
  - 6/12 say such data may be used or disclosed without restriction.
  - 3/12 give a publication example (trend reports).
- **Quote:** "We may disclose aggregated information about our users, and information that does not identify any individual, without restriction." (s03)
- **Commonly omitted:** the de-identification method.

### disclosure: Who we share data with

- **Covers:** recipients of personal data and why each receives it, including legal requests
  and business transfers.
- **Prevalence:** 29/32 (91%), core
- **Applies when:** always
- **Facts:** `facts.processors.list`, `facts.company.group_companies`, `facts.data.sells`
- **Patterns:**
  - 26/29 list recipients by category (service providers, affiliates, other users, partners,
    authorities, acquirers) with a bold label and a reason.
  - 22/29 name no vendor; 7/29 name processors (3 in a table: purpose, provider, data,
    location).
  - 26/29 cover legal requests; 8/29 add a notice-and-challenge practice or transparency report.
  - 22/29 cover mergers and acquisitions; 4/29 promise notice before the transfer.
  - 14/29 open or close with "we do not sell".
  - 5/29 give group-company sharing its own subsection.
- **Quote:** "We do not sell your data to advertisers." (s06)
- **Commonly omitted:** the data categories each recipient gets (given by 6/29); processor
  locations.

### public-visibility: What others can see

- **Covers:** what other users, collaborators or the public can see of a user's profile and
  content, and the risk of onward sharing.
- **Prevalence:** 14/32 (44%), common
- **Applies when:** `facts.product.public_content != none`
- **Facts:** `facts.product.public_content`
- **Patterns:**
  - 8/14 a subsection of *Who we share with*; 5/14 a section of its own; 1/14 inside the data
    list, next to the profile fields.
  - 9/14 end with a warning that shared content can be saved or reused by others.
  - 6/14 list profile fields by visibility (always public / optional / never shown).
- **Quote:** "Everything you post in public will be accessible to everyone." (s02)
- **Commonly omitted:** search-engine indexing.

### cookies: Cookies and tracking

- **Covers:** cookies, pixels, SDKs and similar technologies, their purposes, and how to control
  them.
- **Prevalence:** 24/32 (75%), common
- **Applies when:** `facts.data.tracking != []`
- **Facts:** `facts.data.tracking`
- **Patterns:**
  - 16/24 a section inside the policy; 4/24 a pointer to a separate cookie policy; 3/24 a full
    cookie policy embedded as an annex or section; 1/24 one catch-all sentence in the data
    list.
  - 10/24 define cookies in lay terms (session vs persistent).
  - 9/24 group by purpose (necessary, analytics, advertising, functionality).
  - 8/24 name one or more analytics or ad providers with an opt-out link.
  - 13/24 end with browser-settings instructions and the consequence of blocking.
- **Quote:** "We do not use cookies for profiling or advertising." (s02)
- **Commonly omitted:** a per-cookie list (3/24); cookie lifetimes.

### advertising: Advertising, sale and sharing

- **Covers:** targeted advertising, whether data is sold, and the opt-outs.
- **Prevalence:** 22/32 (69%), common
- **Applies when:** always
- **Facts:** `facts.data.targeted_ads`, `facts.data.sells`
- **Patterns:**
  - 14/22 run targeted ads and explain the mechanism (partner pixels, hashed email or phone
    matching).
  - 8/22 state there is no targeted advertising or no sale at all.
  - 9/22 list opt-out routes: in-app setting, a privacy-choices link, industry opt-out tools,
    device settings.
  - 5/22 add a no-targeting statement for minors.
- **Quote:** "We offer you choices regarding personalized ads, but you cannot opt-out of seeing non-personalized ads." (s10)
- **Commonly omitted:** the list of ad partners; how long ad data is kept.

### signals: Do Not Track and opt-out signals

- **Covers:** whether the site responds to Do Not Track and Global Privacy Control.
- **Prevalence:** 15/32 (47%), common
- **Applies when:** `facts.data.tracking != []`
- **Facts:** `facts.data.honors_dnt`, `facts.data.honors_gpc`
- **Patterns:**
  - 11/15 say they do not respond to DNT; 8/15 say they honour GPC.
  - 10/15 put it inside the advertising, cookies or rights section; 5/15 give it its own
    short section.
  - 3/15 add that the opt-out applies per browser or device only.
- **Quote:** "We do not currently respond to DNT browser signals; however, we honor opt-out preference signals, such as Global Privacy Control, as described above." (s06)
- **Commonly omitted:** how long the signal is honoured.

### third-party-services: Third-party links and integrations

- **Covers:** linked sites, connected apps and embedded content run by others, and that their
  own policies apply.
- **Prevalence:** 19/32 (59%), common
- **Applies when:** always
- **Facts:** `facts.product.integrations`
- **Patterns:**
  - 14/19 a short no-responsibility disclaimer of two or three sentences.
  - 6/19 describe connected integrations: what data moves and how to revoke access.
  - 3/19 cover embedded content (video, images) that may collect data.
- **Quote:** "Third-party services have their own privacy policies, and you may be giving them permission to use your data in ways we would not." (s10)
- **Commonly omitted:** which integrations exist (most stay generic).

### feature-notices: Feature-specific notices

- **Covers:** short notices for features whose data flow the general sections do not explain:
  sync, backup, contact matching, recordings, payments, age checks, session replay, chat.
- **Prevalence:** 17/32 (53%), common
- **Applies when:** `facts.product.features != []`
- **Facts:** `facts.product.features`, `facts.processors.list`
- **Patterns:**
  - 10/17 one labelled subsection per feature inside *Data we collect* or *How we use*; 4/17
    organise the whole policy by feature; 3/17 append product supplements or annexes.
  - Each notice typically states: what is collected, where it is processed, who else is
    involved, retention, and how to turn it off.
  - 5/17 cover in-app payments: the processor holds card data, the company keeps only a token
    or the last four digits.
  - 6/17 lead with what the company cannot see (encryption, on-device processing).
- **Quote:** "Your credit card information never reaches Telegram's servers." (s02)
- **Commonly omitted:** features that only process data on the device.

### platform-disclosures: Platform-required disclosures

- **Covers:** statements a platform requires in the policy: the Google API Services User Data
  Policy (Limited Use), Google Play health-app disclosures.
- **Prevalence:** 3/32 (9%), rare
- **Applies when:** `facts.product.platform_disclosures != []`
- **Facts:** `facts.product.platform_disclosures`, `facts.product.integrations`
- **Patterns:**
  - 2/3 one sentence naming the Google API Services User Data Policy and its Limited Use
    requirements, 1 of them inside a Gmail feature notice; 1/3 a headed section framed as
    required by Google Play, pointing back to the feature sections.
  - 1 more sample (s27) describes a Google Drive integration without the Limited Use sentence.
- **Quote:** "Google has determined our mobile apps are subject to their Health Apps requirements." (s31)
- **Commonly omitted:** the scopes requested.

### transfers: International transfers

- **Covers:** where data is stored and processed, and the safeguards for cross-border transfers.
- **Prevalence:** 24/32 (75%), common
- **Applies when:** always
- **Facts:** `facts.data.storage_locations`
- **Patterns:**
  - 18/24 name the home country of processing; 1/24 points to the place given for each
    service instead.
  - 12/24 name a legal transfer mechanism, 8/24 say only "appropriate safeguards"; which
    mechanism applies belongs to the regional part.
  - 4/24 warn that other countries' laws may protect less.
- **Quote:** "When we transfer personal data to a third country, we use appropriate mechanisms." (s22)
- **Commonly omitted:** the list of destination countries per processor.

### retention: How long we keep data

- **Covers:** how long data is kept, by category or by rule, and what happens after account
  deletion.
- **Prevalence:** 28/32 (88%), core
- **Applies when:** always
- **Facts:** `facts.data.retention`, `facts.data.deletion_lag`
- **Patterns:**
  - 15/28 give criteria only ("as long as necessary", with factors: relationship, legal
    obligations, disputes); 13/28 add concrete periods for at least some categories.
  - 8/28 give a fixed number of days from account deletion to full deletion, often with backup
    lag.
  - 5/28 give a per-category list or table of periods.
  - 5/28 merge retention into the security section.
- **Quote:** "If you delete your account, we'll initiate deletion of this information after 30 days." (s25)
- **Commonly omitted:** backup retention (stated by 5/28); log retention.

### security: How we protect data

- **Covers:** the safeguards for personal data and the limits of security.
- **Prevalence:** 25/32 (78%), common
- **Applies when:** always
- **Facts:** `facts.data.security_measures`
- **Patterns:**
  - 20/25 generic measures (administrative, technical, physical) plus a no-guarantee
    disclaimer.
  - 5/25 name concrete controls (encryption at rest and in transit, MFA by default, access
    controls, testing).
  - 6/25 add the user's share of the duty (passwords, shared devices).
  - 2/25 commit to breach notification.
- **Quote:** "However, be aware that no system is ever completely secure." (s01)
- **Commonly omitted:** standards and certifications; incident history.

### rights: Your rights and choices

- **Covers:** the rights users have over their data, how to exercise them, verification, and
  the right to complain.
- **Prevalence:** 31/32 (97%), core
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`
- **Patterns:**
  - Framing splits: 11/31 lead with in-app self-service (settings paths), then email as
    fallback; 6/31 a jurisdiction-hedged list ("depending on where you live"); 4/31 grant the
    same rights to all users regardless of location; 2/31 only point to regional notices; 2/31
    give only the GDPR list, with no rights for anyone else.
  - 20/31 one bullet per right with a one-line plain explanation.
  - 17/31 include the right to complain to a data protection authority.
  - 5/31 give a response deadline (30 days or one month).
  - Verification, agents, appeals and non-discrimination belong to the regional part.
  - 12/31 describe account deletion here, with what remains after it.
- **Commonly omitted:** fees (2/31); the exact verification data asked for.

### marketing: Marketing messages

- **Covers:** marketing email, SMS and push, and how to opt out; service messages that continue.
- **Prevalence:** 21/32 (66%), common
- **Applies when:** `facts.marketing.email == true` or `facts.marketing.push == service-and-marketing`
- **Facts:** `facts.marketing.email`, `facts.marketing.push`
- **Patterns:**
  - 13/21 inside the rights or choices section; 8/21 a section of its own.
  - 14/21 name the opt-out routes (unsubscribe link, account preferences, device settings).
  - 10/21 say transactional and service messages continue after opting out.
  - 3/21 cover push notifications separately.
- **Quote:** "Please be aware that you cannot opt out of receiving service messages from us, including security and legal notices." (s10)
- **Commonly omitted:** processing time for an opt-out (2/21).

### children: Children

- **Covers:** the minimum age, that children's data is not knowingly collected, and what happens
  when it is found.
- **Prevalence:** 19/32 (59%), common
- **Applies when:** always
- **Facts:** `facts.product.min_age`, `facts.product.child_directed`, `facts.company.contact_email`
- **Patterns:**
  - 16/19 one short paragraph; 3/19 (child-directed products) a full section with parental
    consent, parent rights and a retention schedule.
  - Age splits: 9/19 under 13 (with a higher age for some regions in 3); 8/19 under 18; 2/19 per country.
  - 10/19 promise deletion on discovery; 7/19 give a contact for reports.
- **Quote:** "If we learn that we have collected Personal Information from a child, we will promptly take steps to delete that information." (s03)
- **Commonly omitted:** how age is checked (3/19).

### job-applicants: Job applicants

- **Covers:** data from job applications made through the website and its use.
- **Prevalence:** 3/32 (9%), rare
- **Applies when:** `facts.company.collects_applicant_data == true`
- **Facts:** `facts.company.collects_applicant_data`
- **Patterns:**
  - 3/3 one short paragraph: categories (CV, references, diversity data), recruitment purposes,
    keeping data for future roles.
- **Quote:** "This data is limited to what we need to assess your application." (s27)
- **Commonly omitted:** retention for rejected applicants.

### changes: Changes to this policy

- **Covers:** how the policy changes and how users are told.
- **Prevalence:** 32/32 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - 21/32 promise notice of material changes (email, in-app, banner); the rest only update the
    date, 1 reserving the right to change with little or no notice.
  - 13/32 treat continued use as acceptance; 4/32 add that the only alternative is to stop
    using or close the account.
  - 5/32 say changes take effect on posting; 3/32 give an advance-notice period.
- **Quote:** "We will notify you before material changes take effect so that you have time to review the changes." (s22)
- **Commonly omitted:** what counts as "material".

### contact: Contact us

- **Covers:** how to reach the company about privacy, including the DPO and representatives.
- **Prevalence:** 32/32 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.address`, `facts.company.dpo_contact`
- **Patterns:**
  - 26/32 give an email; 17/32 a postal address; 2/32 only a link to a form.
  - 14/32 list regional representatives here, as address blocks.
  - 8/32 route to a DPO.
  - 5/32 group contacts by region or entity.
- **Quote:** "If you have any questions about our practices or this Policy, please contact us at [email]." (s03)
- **Commonly omitted:** a phone number (4/32); response times.

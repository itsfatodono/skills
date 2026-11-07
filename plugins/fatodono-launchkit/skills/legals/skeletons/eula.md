---
doc_id: eula
title: End User License Agreement
kind: document
family: terms
sample_languages: [en]
sample_count: 22
saturated: true
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** The licence for software the user installs: what the user may do with their copy,
  what they may not do, what the company promises about the software, and how the licence ends.
- **Shape:**
  - 18/22 one web page; 2/22 a plain-text file shipped with the installer; 1/22 a PDF; 1/22 a web
    copy that says the binding text is the one shown at install. Median about 4,900 words (range
    390–14,000): large companies about 7,100, mid about 4,300, small about 1,800.
  - 16/22 number their sections; 1/22 opens with a table of contents.
  - 5/22 stack a base agreement with modules, product addenda or product-specific pages that win
    on conflict.
  - 7/22 cover several products in one agreement; 9/22 vary clauses or the contracting entity by
    where the user lives or bought the licence.
- **Register:** formal licence drafting. About 14/22 name the company in the third person
  ("Licensor", the brand, "the Company") and about 8/22 write mostly "we/you". 13/22 set the
  warranty and liability clauses in all caps. 2/22 open with a plain-language preface or welcome.
- **Recurring elements:**
  - A dated "last updated" or version line: 11/22; a version tag without a date: 2/22.
  - "Licensed, not sold": 15/22.
  - A definitions block: 6/22; the rest define terms inline in quotes.
  - A caps "read carefully before installing" banner above the text: 7/22.
  - A closing contact section: 10/22.
  - Third-party licence texts or a component list on the same page: 2/22.
- **Commonly omitted:** a contact section (12/22); a dated version line (9/22); a definitions block
  (16/22); a table of contents (21/22); an indemnity (9/22) and a dispute clause (10/22) in the
  shorter texts.

## Sections

Region-neutral. What one law requires is in the region's block, `regions/<code>/eula.md`, written
under the document's regional part (`formats/region-format.md`).

### intro: About this agreement

- **Covers:** who licenses the software, which products and versions it covers, that the software
  is licensed and not sold, and how the user accepts the agreement.
- **Prevalence:** 22/22 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.product.name`, `facts.product.services_in_scope`, `facts.product.eula_acceptance`, `facts.company.group_companies`
- **Patterns:**
  - 15/22 say the software is licensed, not sold, here or in the grant.
  - About 17/22 make downloading, installing or using the software the act of acceptance; 7/22
    name a button ("I agree", "Accept"); 3/22 tie acceptance to a checkout checkbox or the pay
    button; 2/22 have no acceptance clause (one is formed by an order).
  - 11/22 tell a user who disagrees not to install, to stop using, or to delete the software.
  - 7/22 give the licensor's registered name with its address or registration number.
  - 6/22 name a different contracting entity by region or brand.
  - About 7/22 define what "the Software" includes (documentation, updates, media, online services).
  - 7/22 cover several products; 6/22 give a definitions block.
  - 7/22 put a caps banner above the text; 2/22 open with a plain-language preface explaining why
    there is an EULA.
- **Quote:** "The SOFTWARE PRODUCT is licensed, not sold." (s03)
- **Commonly omitted:** a description of what the software does (about 18/22).

### incorporated-terms: Other terms that apply

- **Covers:** other documents that form part of the agreement (main service terms, order
  documents, product addenda, external use-rights pages) and which wins on conflict.
- **Prevalence:** 13/22 (59%), common
- **Applies when:** `facts.company.published_policies != []`
- **Facts:** `facts.company.published_policies`, `facts.product.services_in_scope`
- **Patterns:**
  - 6/13 let product addenda, product-specific pages or location terms win over the base text.
  - 6/13 let a separate signed agreement, licence certificate or order document win over the EULA.
  - 3/13 send the use of the online service to the main terms of service or bring the privacy
    policy in by name; 1/13 says the EULA is separate from the purchase contract.
  - 2/13 cover reseller purchases (the reseller's terms do not bind the licensor).
- **Quote:** "If there is any conflict between the General Terms and the Specific Terms, the Specific Terms will govern with respect to those Software." (s19)
- **Commonly omitted:** an order of precedence among the incorporated documents themselves.

### eligibility: Who may accept

- **Covers:** minimum age or legal capacity, and authority to accept for an organisation.
- **Prevalence:** 12/22 (55%), common
- **Applies when:** always
- **Facts:** `facts.product.min_age`, `facts.product.business_use`
- **Patterns:**
  - 9/12 have the person accepting for a company warrant their authority; "you" then means the
    company.
  - 5/12 set a minimum age or the age of majority; 1/12 sets ages by country in a table.
  - 3/12 sell some licences to businesses only.
  - Usually one or two sentences inside the opening.
- **Quote:** "If you are accepting this EULA on behalf of an entity, you represent and warrant that you have the authority to bind that entity to these terms." (s19)
- **Commonly omitted:** parental consent (1/12).

### licence-grant: Your licence

- **Covers:** what the user may do with the software: the kind of licence, permitted purpose,
  devices, users or seats, installs and backup copies, and the conditions on the grant.
- **Prevalence:** 22/22 (100%), core
- **Applies when:** always
- **Facts:** `facts.product.licence_terms`, `facts.product.services_in_scope`, `facts.sales.plans`
- **Patterns:**
  - About 19/22 grant a limited, non-exclusive, non-transferable licence; 7/22 add "revocable".
  - 9/22 count devices or installs (often one device at a time); 5/22 use the app-store wording
    "devices you own or control"; 4/22 count users or named seats; the rest set no unit.
  - 7/22 limit use to personal, non-commercial purposes; 5/22 to the licensee's internal business.
  - 8/22 make the grant conditional on payment; 8/22 allow a backup copy.
  - 6/22 set out several editions or plans with their own scope (personal, business, site,
    floating seats).
  - 4/22 write the permissions as a list.
- **Quote:** "Licenses are per user and valid for use on all supported operating systems." (s03)
- **Commonly omitted:** an end date other than termination for perpetual licences.

### account: Your account

- **Covers:** whether an account is needed, accurate details, credential security, responsibility
  for activity on the account, and account roles.
- **Prevalence:** 8/22 (36%), rare
- **Applies when:** `facts.product.has_accounts == true`
- **Facts:** `facts.product.has_accounts`, `facts.product.business_use`, `facts.product.account_roles`
- **Patterns:**
  - 4/8 need an account to activate or fully use the software.
  - 3/8 make the user responsible for credentials and activity and ask them to report misuse.
  - 2/8 ban transferring the account; 2/8 cover admin or owner roles for business accounts.
- **Quote:** "The transfer or assignment of the User Account without the express consent of Ableton is prohibited." (s05)
- **Commonly omitted:** how to close the account (left to the terms of service or a deletion page).

### special-licences: Trial, free and other licence types

- **Covers:** licence types with their own limits (trial or evaluation, free, educational, OEM,
  not-for-resale, migration) and what changes when they convert or expire.
- **Prevalence:** 13/22 (59%), common
- **Applies when:** `facts.product.licence_terms` lists more than one model, or a `trial`, `free`, `educational` or `oem` model
- **Facts:** `facts.product.licence_terms`, `facts.sales.free_trial`, `facts.product.software_warranty`
- **Patterns:**
  - 12/13 cover a trial or evaluation; 4/12 give a default length when none is stated and require
    buying or deleting at the end.
  - 6/13 cover free versions; 4/13 educational or academic licences (who qualifies, no commercial
    use); 4/13 OEM, not-for-resale, migration or cover-disc copies.
  - 6/13 give free and trial versions an as-is warranty and a lower or fixed liability cap.
  - 3/13 say trial and free licences cannot be transferred.
  - One subsection per type, after the main grant.
- **Quote:** "If you continue to use this Software after the Trial Period, you are required to purchase a license." (s18)
- **Commonly omitted:** what happens to the user's work when a trial ends.

### app-stores: App stores

- **Covers:** distribution through app stores: the store is not a party, the store's usage rules,
  store-billed purchases and refunds, and the clauses the stores require.
- **Prevalence:** 7/22 (32%), rare
- **Applies when:** `facts.sales.purchase_channels` includes `app-store` or `google-play`, or `facts.product.services_in_scope` includes kind `ios` or `android`
- **Facts:** `facts.sales.purchase_channels`, `facts.product.services_in_scope`, `facts.company.contact_email`
- **Patterns:**
  - 5/7 restate the Apple-required terms: the agreement is with the company, not Apple; licence
    limited by the store's usage rules; Apple owes no support; Apple's only warranty duty is
    refunding the price; the company handles product and IP claims; Apple is a third-party
    beneficiary. 2/5 apply the same to Google Play.
  - 3/5 spread these terms across the warranty, support and IP sections instead of one block.
  - 3/7 send refunds for store purchases to the store.
- **Quote:** "Apple, and Apple`s subsidiaries, are third party beneficiaries of this Agreement." (s06)
- **Commonly omitted:** the store's own refund window.

### company-ip: Ownership

- **Covers:** the licensor's ownership of the software and its content, reserved rights,
  trademarks and proprietary notices.
- **Prevalence:** 21/22 (95%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`
- **Patterns:**
  - 21/21 state the licensor and its suppliers own the software and every copy.
  - About 12/21 reserve every right not expressly granted.
  - 5/21 say the user gets no licence to the company's trademarks; 4/21 call the code a trade
    secret; 4/21 name the copyright laws that protect it.
  - 2/21 separate owning the media from owning the software.
  - Usually one or two sentences.
- **Quote:** "Except for those rights expressly granted in this EULA, no other rights are granted, whether express or implied." (s01)
- **Commonly omitted:** patents (2/21 name them).

### beta-features: Beta features

- **Covers:** beta, pre-release or optional untested features and their risks.
- **Prevalence:** 4/22 (18%), rare
- **Applies when:** `facts.product.beta_features == true`
- **Facts:** `facts.product.beta_features`
- **Patterns:**
  - 4/4 give them as is, with no duty to keep or release them.
  - 2/4 add no support and no liability; 1/4 warns they may have serious issues and advises a
    backup.
- **Quote:** "Optional Items are not fully tested by Malwarebytes and may include significant issues." (s28)
- **Commonly omitted:** how beta features are labelled.

### activation: Activation and licence checks

- **Covers:** licence keys, activation, online licence checks or disabling technology, and what
  happens when activation fails or a licence lapses.
- **Prevalence:** 7/22 (32%), rare
- **Applies when:** `facts.product.activation != none`
- **Facts:** `facts.product.activation`, `facts.product.has_accounts`, `facts.data.collected`
- **Patterns:**
  - 3/7 say the software stops or loses features when it is not activated or the licence ends.
  - 2/7 let the company block a key for breach or non-payment; 2/7 list the data a licence check
    sends; 1/7 locks activation to a region or language.
  - 2/7 ban circumventing the check, repeated in the restrictions.
- **Quote:** "The Software may contain an automatic disabling mechanism that prevents its use after a certain period of time." (s13)
- **Commonly omitted:** how many reactivations are allowed after hardware changes (1/7).

### fees-payment: Price and payment

- **Covers:** buying the licence: price, payment, taxes, price changes, resellers, licence
  conditional on payment, non-payment.
- **Prevalence:** 12/22 (55%), common
- **Applies when:** `facts.sales.purchase_channels != []`
- **Facts:** `facts.sales.purchase_channels`, `facts.sales.plans`, `facts.sales.payment_provider`, `facts.sales.taxes`, `facts.company.change_notice`
- **Patterns:**
  - 4/12 put taxes on the user; 4/12 cover reseller purchases; 4/12 suspend use or support for
    non-payment.
  - 3/12 set invoice due dates and late interest (business licences); 3/12 promise notice of price
    changes.
  - 2/12 state prices or the upgrade price in the text; 1/12 warns that store prices may differ.
  - 1/12 covers card updates and payment retries.
- **Quote:** "You consent for us to charge your payment type using the updated details." (s04)
- **Commonly omitted:** the currency; the payment provider's name.

### restrictions: What you may not do

- **Covers:** what the user may not do with the software: copy, modify, reverse engineer,
  redistribute, rent, host for others, remove notices, circumvent protections, prohibited end uses.
- **Prevalence:** 22/22 (100%), core
- **Applies when:** always
- **Facts:** `facts.product.licence_terms`, `facts.product.activation`
- **Patterns:**
  - 19/22 ban reverse engineering; 11/22 except what the law allows; 1/22 permits it except to
    make derivative works or circumvent protections.
  - About 10/22 ban removing proprietary notices; 7/22 hosting, service-bureau or SaaS use for
    others; 5/22 circumventing licence keys or protections.
  - 3/22 ban high-risk uses (aviation, life support, weapons); 3/22 benchmarking or competing
    products; 3/22 using the software or its output to train AI models.
  - 2/22 expressly allow building plug-ins through the public APIs.
  - 7/22 write a list after "You may not:"; the rest one run of verbs in prose.
- **Quote:** "You may not rent, lease, or lend the license key or the SOFTWARE PRODUCT." (s03)
- **Commonly omitted:** the consequence of each breach (most refer to termination).

### system-requirements: System requirements

- **Covers:** devices, operating systems, internet access and data charges the user needs.
- **Prevalence:** 6/22 (27%), rare
- **Applies when:** `facts.product.system_requirements != none`
- **Facts:** `facts.product.system_requirements`
- **Patterns:**
  - 6/6 put a compatible device and OS on the user; 3/6 add internet access and data charges.
  - 2/6 promise no compatibility with every device or third-party software; 2/6 may change the
    requirements.
  - 3/6 point to a product page instead of listing versions.
- **Quote:** "You are responsible for ensuring your device meets the technical specifications required to use the Application." (s09)
- **Commonly omitted:** actual version numbers.

### feedback: Feedback

- **Covers:** suggestions users send and the licensor's right to use them.
- **Prevalence:** 11/22 (50%), common
- **Applies when:** always
- **Facts:** none
- **Patterns:**
  - About 10/11 let the licensor use feedback freely, without payment or credit.
  - 5/11 take ownership or a perpetual licence.
  - 5/11 fold it into another section (ownership, confidentiality, user content, data).
- **Quote:** "Please keep in mind that we'll use it without restriction or payment." (s04)
- **Commonly omitted:** a confidentiality statement for feedback.

### updates: Updates and upgrades

- **Covers:** what updates include and how they arrive, whether they are free or paid, the effect
  on the prior licence, and support for old versions.
- **Prevalence:** 18/22 (82%), core
- **Applies when:** always
- **Facts:** `facts.product.update_policy`, `facts.product.licence_terms`
- **Patterns:**
  - About 6/18 owe no updates at all; updates that come fall under the agreement.
  - 6/18 split free updates (a period or a major version) from paid upgrades.
  - 4/18 install updates automatically, 2/4 with an opt-out; 4/18 make some updates mandatory or
    put the cost of not updating on the user.
  - 5/18 end support for old versions; 2/18 end the prior licence on upgrade.
  - 1/18 promises never to install updates silently.
- **Quote:** "You may opt out of these automatic downloads by changing the corresponding preferences in Your settings." (s05)
- **Commonly omitted:** how long old versions keep working.

### acceptable-use: Rules of use

- **Covers:** conduct and content rules for using the software: unlawful use, banned content,
  monitoring other people lawfully.
- **Prevalence:** 10/22 (45%), common
- **Applies when:** always
- **Facts:** `facts.product.public_content`, `facts.product.features`, `facts.company.published_policies`
- **Patterns:**
  - About 6/10 say only that use must be lawful and respect others' rights.
  - 3/10 list banned content; 2/10 point to a separate acceptable use policy.
  - 2/10 require legal authority before tracking or monitoring children, staff or devices.
  - 1/10 lets the company suspend the licence for prohibited use, without a refund.
- **Quote:** "If the product you purchase includes tracking features, you must have the legitimate right and authority before using them to track and monitor children or other third parties." (s04)
- **Commonly omitted:** the steps the company takes on a breach.

### transfer: Transferring the licence

- **Covers:** whether the licence can be resold, given away or moved to another person, and the
  conditions.
- **Prevalence:** 13/22 (59%), common
- **Applies when:** always
- **Facts:** `facts.product.licence_terms`
- **Patterns:**
  - 8/13 ban transfer, or allow it only with written consent.
  - 4/13 allow transfer of the whole licence on conditions: the seller removes every copy, the
    buyer accepts the agreement, sometimes registers it.
  - 1/13 lets a named-user seat move only when the original user leaves.
  - 2/13 exclude trial, free or not-for-resale licences.
  - 5/13 write it as one sentence inside the restrictions.
- **Quote:** "You may, however, transfer the license to use the Ableton Product as a whole to another person or entity." (s05)
- **Commonly omitted:** what the buyer must do to register.

### support: Support

- **Covers:** whether maintenance or support is owed, by whom, through which channels, and for
  which versions.
- **Prevalence:** 16/22 (73%), common
- **Applies when:** always
- **Facts:** `facts.product.support`, `facts.company.contact_email`
- **Patterns:**
  - 7/16 owe no support, or give it at their discretion.
  - 9/16 describe the support given: channels (email, forum, help site), included versus paid
    support, an error-fixing effort for business licences.
  - 3/16 limit support to supported versions; 3/16 offer paid support.
  - 3/16 say the company, not the app store, owes any support the law requires.
- **Quote:** "At Cockos discretion, Cockos may provide limited support through email or discussion forums at http://www.reaper.fm." (s18)
- **Commonly omitted:** response times.

### software-changes: Changes to the software

- **Covers:** the licensor's right to change, suspend, remove features from or discontinue the
  software or a connected service.
- **Prevalence:** 13/22 (59%), common
- **Applies when:** always
- **Facts:** `facts.company.change_notice`, `facts.sales.partial_refunds`
- **Patterns:**
  - About 7/13 reserve the right to change or stop the software at any time, without notice or
    liability.
  - 4/13 cover discontinued products: perpetual licensees keep the current version without
    support; prepaid subscribers are moved or may not renew.
  - 1/13 allows changes only for good cause; 1/13 promises not to remove features on purpose.
  - About 5/13 sit under the updates or terms-changes heading.
- **Quote:** "Limited Maintenance Mode means that the Licensor will no longer release new enhancements (upgrades and updates) of the Software." (s23)
- **Commonly omitted:** a refund when a paid feature is removed (1/13).

### refunds: Refunds

- **Covers:** when money comes back: money-back guarantee, no-refund rule, pro-rata refunds,
  refunds through the store.
- **Prevalence:** 12/22 (55%), common
- **Applies when:** `facts.sales.purchase_channels != []`
- **Facts:** `facts.sales.refund_rule`, `facts.sales.partial_refunds`, `facts.sales.purchase_channels`
- **Patterns:**
  - 4/12 refuse refunds once paid; 1/12 ties that to a free trial the user could test first.
  - 2/12 give a money-back window; 1/12 points to a separate refund policy.
  - 4/12 refund pro rata when the company ends the licence or a paid add-on, or when the user
    leaves over a change to the terms.
  - 2/12 send store purchases to the store.
  - 2/12 make a refund the remedy for a defect or an IP claim.
  - About 8/12 put it inside the acceptance, warranty, termination or payment section; 2/12 give
    it a heading.
- **Quote:** "Once you pay the license fee, your payment is final and may not be reimbursed." (s18)
- **Commonly omitted:** how to ask for a refund.

### online-services: Online services

- **Covers:** online services delivered with the software (cloud, sync, storage, SaaS editions):
  scope, the licence to process the user's data to run them, security effort, availability.
- **Prevalence:** 5/22 (23%), rare
- **Applies when:** `facts.product.features` includes a feature processed on the company's servers (sync, backup, cloud editing)
- **Facts:** `facts.product.features`, `facts.data.security_measures`, `facts.processors.list`
- **Patterns:**
  - 3/5 promise commercially reasonable availability, subject to maintenance downtime; 1/5
    promises no availability for free users.
  - 2/5 extend the EULA to the online services and list them.
  - 1/5 takes a licence to user data only as needed to run the service; 1/5 promises security
    effort without a guarantee.
- **Quote:** "To the extent you elect to use the Software Services, you grant the Omni Group a non-exclusive, revocable license to use Customer Data as necessary to provide the Software Services to you." (s11)
- **Commonly omitted:** a service level or uptime figure.

### subscriptions: Subscriptions and renewal

- **Covers:** subscription licences: term, automatic renewal, how and when to cancel, and what
  happens at expiry.
- **Prevalence:** 11/22 (50%), common
- **Applies when:** `facts.sales.subscription != none`
- **Facts:** `facts.sales.subscription`, `facts.sales.plans`, `facts.sales.purchase_channels`
- **Patterns:**
  - 9/11 renew automatically for the same term until cancelled; 2/11 at the then-current price.
  - 6/11 say how to cancel (account page, notice before the end of the term, a deadline).
  - 3/11 bar ending a subscription mid-term.
  - 3/11 stop features or downgrade to a free version at expiry; 2/11 let a perpetual licence
    convert to or from a subscription.
- **Quote:** "After the expiration of your Subscription, features of the Software will stop running." (s11)
- **Commonly omitted:** a renewal reminder (1/11).

### terms-changes: Changes to this agreement

- **Covers:** how the agreement changes, notice, and when changes bind the user.
- **Prevalence:** 16/22 (73%), common
- **Applies when:** always
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - About 7/16 change the agreement at will, with continued use as acceptance; 2/7 without notice.
  - 5/16 give notice and a window to object or leave, keeping the old terms or refunding the user.
  - 4/16 apply changes from the next version or renewal the user installs or accepts.
  - 3/16 allow changes only by written agreement of both parties.
  - 1/16 keeps old terms for disputes that arose earlier.
- **Quote:** "If you renew your subscription, you accept the most recent version of these terms." (s04)
- **Commonly omitted:** a summary of what changed.

### privacy: Privacy

- **Covers:** where the privacy policy is, and any other statement on personal data in the
  agreement.
- **Prevalence:** 17/22 (77%), common
- **Applies when:** always
- **Facts:** `facts.company.published_policies`, `facts.company.acts_as_processor`, `facts.data.storage_locations`
- **Patterns:**
  - About 13/17 point to the privacy policy in one or two sentences.
  - 3/17 bring the policy into the agreement by reference.
  - 3/17 summarise the data collected and its purposes before the pointer.
  - 2/17 point business customers to a data processing addendum; 1/17 says data may be processed
    abroad.
- **Quote:** "Our handling of personal information we collect through the LinkedIn Services or the Software is governed by the LinkedIn Privacy Policy." (s01)
- **Commonly omitted:** the policy's content.

### third-party-services: Third-party services

- **Covers:** outside services, content and links reached through the software.
- **Prevalence:** 12/22 (55%), common
- **Applies when:** always
- **Facts:** `facts.product.integrations`
- **Patterns:**
  - About 11/12 say the third party's terms apply, use is at the user's risk, and the licensor is
    not liable.
  - 2/12 name kinds (social networks, cloud storage, telephone dial-in); 2/12 cover third-party
    technology the software works with.
  - 1/12 adds that information from those services is for information only.
- **Quote:** "You agree to use the External Services at your sole risk." (s06)
- **Commonly omitted:** names of the services.

### third-party-components: Open-source and third-party components

- **Covers:** open-source and third-party code inside the software: their own licences apply, where
  the notices are, and no warranty for them.
- **Prevalence:** 10/22 (45%), common
- **Applies when:** `facts.product.third_party_components != none`
- **Facts:** `facts.product.third_party_components`
- **Patterns:**
  - About 7/10 say the components' own licences apply and win where they grant more.
  - 7/10 point to the notices (a web page, a repository, the about box or readme files); 2/10 list
    the components or paste the licence texts on the same page.
  - 3/10 offer source code for copyleft components; 3/10 disclaim warranty for them.
  - 1/10 adds codec patent notices.
- **Quote:** "Rights and obligations under any applicable Open Source license remain unaffected by this EULA." (s05)
- **Commonly omitted:** a component list in the agreement itself (8/10).

### telemetry: Data the software sends

- **Covers:** device, usage and diagnostic data the software itself sends to the licensor: kinds,
  purposes, aggregation, consent and opt-out.
- **Prevalence:** 12/22 (55%), common
- **Applies when:** `facts.data.collected` includes a category with source `automatic`
- **Facts:** `facts.data.collected`, `facts.data.purposes`, `facts.data.telemetry_controls`, `facts.data.deidentified_use`
- **Patterns:**
  - About 10/12 name the kinds in categories (device, version, usage, crash and licence data).
  - 7/12 give purposes: support, product improvement, licence compliance, threat detection.
  - 4/12 say the data is anonymous or aggregated; 4/12 frame it as the user's consent.
  - 2/12 say how to turn it off; 1/12 promises no tracking without the user's authorisation.
  - 2/12 share some of it with third parties.
- **Quote:** "We will not track or collect any information about you, your data, or your use of the software except as you specifically authorize." (s27)
- **Commonly omitted:** retention periods (left to the privacy policy).

### warranty: Warranty and disclaimer

- **Covers:** what the licensor promises about the software and what it disclaims.
- **Prevalence:** 21/22 (95%), core
- **Applies when:** always
- **Facts:** `facts.product.software_warranty`, `facts.product.risk_domains`, `facts.sales.refund_rule`
- **Patterns:**
  - About 19/21 provide the software as is and name the implied warranties disclaimed.
  - 7/21 first give a limited warranty: the software works as documented, or the media is sound,
    for a set number of days; 4/7 name the remedy (fix, replace or refund).
  - About 13/21 set the disclaimer in all caps; about 6/21 add that some jurisdictions do not allow
    it; about 4/21 keep non-waivable consumer rights.
  - 3/21 exclude trial or free versions from any warranty; 2/21 say the company, not the app store,
    bears any warranty that cannot be disclaimed.
  - Product-specific lines: no promise to catch every threat, not a healthcare provider, back up
    your data (about 4/21).
  - 1/21 puts a money-back guarantee here.
- **Quote:** "We do not warrant that the software or your ability to use it will be uninterrupted or error-free." (s27)
- **Commonly omitted:** how to make a warranty claim.

### termination: Term and termination

- **Covers:** how long the licence lasts, termination by the licensor and by the user, automatic
  termination on breach, the duty to stop use and delete, and survival.
- **Prevalence:** 21/22 (95%), core
- **Applies when:** always
- **Facts:** `facts.product.licence_terms`, `facts.sales.subscription`
- **Patterns:**
  - About 13/21 end the licence automatically on any breach.
  - About 12/21 require the user to stop using and delete every copy; 2/21 ask for a written
    certificate of deletion.
  - 8/21 let the user end it by deleting or destroying the software.
  - 4/21 give a cure period before termination for breach; 4/21 refuse refunds on termination.
  - About 6/21 list surviving clauses; 4/21 set the licence term by model (perpetual, subscription,
    trial).
  - About 4/21 are two sentences with no effects clause.
- **Quote:** "You may terminate this EULA at any time by giving us written notice." (s27)
- **Commonly omitted:** time to export work before access ends.

### user-content: Your content

- **Covers:** content the user creates with or uploads to the software: ownership, licence back to
  the licensor, the user's warranties and responsibility.
- **Prevalence:** 7/22 (32%), rare
- **Applies when:** `facts.product.public_content != none` or `facts.product.features` stores user files on the company's servers
- **Facts:** `facts.product.public_content`, `facts.product.features`, `facts.product.ai_features`
- **Patterns:**
  - 5/7 say the user owns the content and is responsible for it; 3/7 back it with an indemnity.
  - 3/7 take a broad licence to the content; 1/7 extends it to training AI models.
  - 2/7 say the licensor does not monitor content; 2/7 list banned content.
- **Quote:** "You retain all rights and ownership in your User Content and Dolby does not claim any ownership rights in your User Content." (s10)
- **Commonly omitted:** an end date for the licence after deletion.

### communications: Messages from us

- **Covers:** messages from the licensor (in-product messages, email, push, texts) and electronic
  notices.
- **Prevalence:** 6/22 (27%), rare
- **Applies when:** `facts.marketing.sms != none` or `facts.marketing.email == true` or `facts.marketing.push != none`
- **Facts:** `facts.marketing.sms`, `facts.marketing.email`, `facts.marketing.push`
- **Patterns:**
  - 2/6 show in-product messages or ads, one as a condition of the free version.
  - 2/6 cover text messages and calls; 1/6 marketing email and push opt-out.
  - 2/6 accept electronic notices as meeting any "in writing" requirement.
- **Quote:** "You may opt-out of receiving such communications by following the unsubscribe options provided in such messages or by through the settings in your Device." (s10)
- **Commonly omitted:** message frequency.

### indemnity: Indemnity

- **Covers:** the user's duty to cover the licensor's losses from claims the user causes.
- **Prevalence:** 13/22 (59%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.group_companies`
- **Patterns:**
  - 13/13 cover claims from the user's use, breach of the agreement or law, or third-party rights.
  - About 6/13 are one sentence with no defence mechanics; 3/13 let the licensor control the
    defence.
  - 2/13 extend it to the user's staff and anyone given access; 1/13 limits it to export breaches.
  - 1/13 is mutual (business licence).
- **Quote:** "You agree to indemnify, defend and hold harmless Ableton and its affiliates and licensors." (s05)
- **Commonly omitted:** a cap on the user's indemnity.

### liability: Limitation of liability

- **Covers:** the damages the licensor excludes and the cap on its liability.
- **Prevalence:** 22/22 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.liability_cap`
- **Patterns:**
  - About 21/22 exclude indirect, consequential and special damages, lost profits and lost data.
  - Cap: the fees paid (6/22); the fees paid in a recent period, usually 12 months (6/22); the
    greater of fees paid or a small fixed sum (5/22); a fixed sum only (1/22); fees for the current
    term or a fixed sum for free users (1/22); a refund or fix as the only remedy (1/22); no cap
    (2/22).
  - About 13/22 in all caps; about 9/22 add that some jurisdictions do not allow the limits.
  - About 4/22 carve out liability that cannot be excluded (death or injury from negligence,
    intent, gross negligence).
  - 3/22 set a lower or fixed cap for trial, free or evaluation licences; 3/22 tell users to back
    up their data.
- **Quote:** "In any case, Cockos entire liability under the provisions of this EULA or the applicable law shall be limited to the amount paid by you for the Software." (s18)
- **Commonly omitted:** different caps for consumers and business users.

### audit: Usage reporting and audit

- **Covers:** the licensee's duty to report usage and the licensor's right to audit and charge for
  over-use.
- **Prevalence:** 4/22 (18%), rare
- **Applies when:** `facts.product.licence_terms.usage_reporting == true`
- **Facts:** `facts.product.licence_terms`, `facts.product.business_use`
- **Patterns:**
  - 4/4 apply to organisations only.
  - 4/4 allow an audit with notice, remote or on site; 3/4 bill over-use at list price.
  - 2/4 shift the audit cost to the licensee above an under-licensing threshold (5% or 10%).
  - 2/4 require self-declarations or usage reports on request.
- **Quote:** "TeamViewer may require Customer, at any time, to provide a self-declaration regarding its actual scope of use and/or usage pattern." (s22)
- **Commonly omitted:** how often audits may happen (1/4 says).

### export-sanctions: Export controls

- **Covers:** export controls, sanctioned countries and parties, and the user's duty to follow
  local law.
- **Prevalence:** 15/22 (68%), common
- **Applies when:** always
- **Facts:** `facts.company.country`
- **Patterns:**
  - 15/15 require compliance with export laws, usually naming the company's home country's rules.
  - About 10/15 have the user represent they are not in an embargoed country or on a sanctions
    list.
  - 3/15 ban weapons end uses; 2/15 put compliance with local law on users abroad; 1/15 treats
    remote access as an export.
  - About 6/15 are one or two sentences.
- **Quote:** "You agree to comply with all applicable export and import laws." (s05)
- **Commonly omitted:** the list of excluded countries.

### ip-claims: Infringement claims against the software

- **Covers:** who handles a third-party claim that the software infringes IP: defence, indemnity
  toward the user, remedies.
- **Prevalence:** 9/22 (41%), common
- **Applies when:** always
- **Facts:** `facts.sales.purchase_channels`, `facts.product.services_in_scope`
- **Patterns:**
  - 4/9 let the licensor get the right to continue, modify or replace the software, or take it back
    and refund; 2/4 list exclusions (modified, combined, free or open-source parts).
  - 3/9 refuse any indemnity but say the company, not the app store, handles such claims.
  - 2/9 require the user to notify the licensor of a claim at once.
- **Quote:** "Licensor shall not be obligated to indemnify or defend you with respect to any third party claim arising out or relating to the Licensed Application." (s06)
- **Commonly omitted:** a cap on the licensor's IP indemnity.

### dispute-resolution: Resolving disputes

- **Covers:** how disputes are raised and decided: informal resolution, the forum, waivers, time
  limits and injunctions.
- **Prevalence:** 12/22 (55%), common
- **Applies when:** always
- **Facts:** `facts.company.dispute_forum`, `facts.company.contact_email`, `facts.company.address`
- **Patterns:**
  - When `facts.company.dispute_forum == arbitration` (8/12): binding arbitration with a named
    body; 6/8 individual only, with a class-action waiver, an up-front caps notice and often an
    opt-out window (3/8); 1/8 three arbitrators for business disputes.
  - 4/12 require an informal step first; 4/12 set a time limit for claims (often one year).
  - 2/12 keep the licensor's right to court injunctions; 2/12 award attorneys' fees to the winner.
  - 1/12 waives class actions without arbitration.
- **Quote:** "Most disputes can be resolved informally by contacting Customer Service." (s04)
- **Commonly omitted:** mediation.

### bundled-content: Content included with the software

- **Covers:** rules for using content shipped with the software (samples, loops, templates,
  effects, fonts, stock media) in the user's own work.
- **Prevalence:** 4/22 (18%), rare
- **Applies when:** `facts.product.bundled_content != none`
- **Facts:** `facts.product.bundled_content`
- **Patterns:**
  - 4/4 allow use in the user's own work and ban redistributing the content on its own or in a
    competing library.
  - 2/4 limit commercial use (none, or only with an on-screen credit); 1/4 prints the copyright
    line to use.
  - 1/4 lets the licensor withdraw an asset when a third party claims it.
- **Quote:** "You may not use the effects built in Filmora in any way that allows others to download, extract, or redistribute the effects as a standalone file…" (s07)
- **Commonly omitted:** whether the content licence survives the end of the software licence (1/4).

### data-after-end: Your data when the licence ends

- **Covers:** what happens to the user's stored data or account when the agreement ends, and the
  user's backup duty.
- **Prevalence:** 4/22 (18%), rare
- **Applies when:** `facts.product.features` stores user data on the company's servers
- **Facts:** `facts.data.deletion_lag`, `facts.data.kept_after_deletion`, `facts.sales.subscription`
- **Patterns:**
  - 4/4 let the licensor delete stored data after the end; 1/4 without notice.
  - 2/4 put backup or export before the end on the user; 1/4 keeps backups for a period.
  - Usually a sentence in the termination section.
- **Quote:** "You're responsible for storing and backing-up your content before termination." (s04)
- **Commonly omitted:** an export window.

### feature-terms: Feature-specific terms

- **Covers:** rules for one feature or business line of the product that the general sections do
  not handle.
- **Prevalence:** 4/22 (18%), rare
- **Applies when:** `facts.product.features != []`
- **Facts:** `facts.product.features`, `facts.product.integrations`
- **Patterns:**
  - One short paragraph per feature, after the general sections or in an addendum.
  - Kinds seen: monitoring and protection features (1/4), a text-message service (1/4), an in-app
    support channel (1/4), self-hosted server components (1/4).
  - Each says what the feature does and does not do, then disclaims results.
- **Quote:** "This is a notice only service." (s04)
- **Commonly omitted:** features that only process data, which go to the privacy policy.

### general: General terms

- **Covers:** standard closing clauses: entire agreement, severability, waiver, assignment, force
  majeure, notices, language, survival, publicity.
- **Prevalence:** 19/22 (86%), core
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.address`
- **Patterns:**
  - Clauses: entire agreement (about 16/19), severability (about 15/19), waiver (about 12/19),
    assignment with the user barred and the licensor free (about 9/19), force majeure (5/19),
    English prevails over translations (4/19), notices (4/19), publicity or customer-logo rights
    (4/19), purchase-order terms rejected (3/19), confidentiality (2/19).
  - About 14/19 bundle them under one heading; about 5/19 give each its own heading.
- **Quote:** "This EULA constitutes the entire agreement between you and LinkedIn regarding the Software." (s01)
- **Commonly omitted:** third-party beneficiaries outside the app-store clause (1/19).

### ai-features: AI features

- **Covers:** AI features in the software: inputs and outputs, ownership of output, accuracy and
  not-advice disclaimers, AI-specific bans, use of content to train models.
- **Prevalence:** 5/22 (23%), rare
- **Applies when:** `facts.product.ai_features != []`
- **Facts:** `facts.product.ai_features`, `facts.processors.list`
- **Patterns:**
  - 4/5 warn that output may be wrong or is not professional advice; 1/5 adds crisis lines.
  - 2/5 send the AI feature to a third-party provider's terms.
  - 2/5 say output may not be unique; 1/5 gives the user the output.
  - 1/5 requires human review of AI actions; 1/5 bans removing watermarks or training on outputs.
  - 2/5 put AI terms in an addendum.
- **Quote:** "Due to the nature of generative AI, Output may not be unique across users, and the Services may generate the same or similar output for us or a third party." (s07)
- **Commonly omitted:** model provider names.

### governing-law: Governing law and courts

- **Covers:** which law governs the agreement and which courts hear disputes.
- **Prevalence:** 21/22 (95%), core
- **Applies when:** always
- **Facts:** `facts.company.governing_law`, `facts.company.country`
- **Patterns:**
  - About 15/21 name the law of the licensor's home state or country and exclusive courts.
  - 9/21 vary the law and courts by where the user lives or bought, often in a table.
  - About 11/21 exclude the UN Convention on Contracts for the International Sale of Goods.
  - About 6/21 let consumers keep the mandatory protection of their home law.
  - 2/21 name the law only, with no forum.
- **Quote:** "Any dispute between Sketch and You shall exclusively be submitted to the competent court in The Hague, the Netherlands." (s02)
- **Commonly omitted:** the reason for the chosen law.

### contact: Contact

- **Covers:** how to reach the licensor about the agreement or the software.
- **Prevalence:** 10/22 (45%), common
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.address`, `facts.company.phone`
- **Patterns:**
  - 8/10 close the document; 1/10 sits in a preface; 1/10 inside the general clauses.
  - About 7/10 give an email; 3/10 a postal address block; 1/10 tells users how to mark legal
    notices.
- **Quote:** "If you have any questions about this Agreement, please contact us at hello@cleanshot.com." (s24)
- **Commonly omitted:** a phone number (1/10).

---
doc_id: terms-of-service
title: Terms of Service
kind: document
family: terms
sample_languages: [en]
sample_count: 30
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** The contract between the company and each user: who may use the product, on what
  terms, what each side owns and owes, how payment and termination work, and how disputes are
  settled.
- **Shape:**
  - 30/30 one long web page; median about 6,500 words (range 166–51,850). Small companies run
    short (median about 2,700), mid and large companies long (about 8,000–11,000).
  - 16/30 number their sections; 6/30 open with a table of contents.
  - 4/30 add a plain-language summary to each section; 2/30 open with a summary of the latest
    changes.
  - 6/30 put several versions or regional appendices on one page, chosen by where the user lives.
  - Boilerplate clauses sit under one closing "General" or "Miscellaneous" heading in about 18/27.
- **Register:** 28/30 "we/you", often mixed with the brand name in the third person. About 15/30
  formal contract drafting with long sentences; 8/30 plain or conversational; 4/30 generic
  generator wording. 24/30 set the warranty,
  liability and dispute clauses in all caps.
- **Recurring elements:**
  - "Last updated" or "Effective" date: 27/30 (a change log instead: 1/30); link to the previous
    version: 3/30.
  - Defined terms set inline in quotes ("Services", "Content", "you"): 27/30; a definitions
    block: 3/30.
  - A notice at the top that disputes go to individual arbitration: 16/30.
  - Links to companion policies (privacy, acceptable use, community guidelines, refunds): most
    samples, several times.
  - A closing contact section: 17/30.
- **Commonly omitted:** a table of contents (24/30); a user-side account-deletion procedure
  (12/30 have none); a definitions block (27/30); per-section summaries (26/30).

## Sections

Region-neutral. What one law requires is in the region's block,
`regions/<code>/terms-of-service.md`, written under the document's regional part
(`formats/region-format.md`).

### intro: About these terms

- **Covers:** who offers the product, which apps, sites and services the terms cover, that they
  form a binding contract, and how the user accepts them.
- **Prevalence:** 29/30 (97%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.product.services_in_scope`, `facts.company.group_companies`
- **Patterns:**
  - About 25/29 name the legal entity and define "Services" (or a brand term) and "we/you" in
    the first paragraph.
  - 29/29 make use of the product the act of acceptance; 3/29 add clicking "I agree" or "I
    accept".
  - About 10/29 add that a user who disagrees must not use the product.
  - 10/29 describe what the product does, as a sentence or a short section; 3/10 add that the
    company is only an intermediary or aggregator for others' offers or data.
  - 7/29 name a different contracting entity depending on where the user lives (one as a table).
  - 6/29 open with a welcome or mission line; 4/29 set the acceptance paragraph in all caps.
  - 3/29 give a definitions list instead of inline definitions.
- **Quote:** "By accessing our Services, you agree to these Terms." (s01)
- **Commonly omitted:** company registration details; a description of the product (19/29).

### incorporated-terms: Other terms that apply

- **Covers:** the other documents that form part of the terms, and which wins on conflict.
- **Prevalence:** 18/30 (60%), common
- **Applies when:** `facts.company.published_policies != []`
- **Facts:** `facts.company.published_policies`
- **Patterns:**
  - 9/18 list the incorporated policies by name and link, inside the opening.
  - 3/18 give a bullet list with a one-line gloss of what each policy covers.
  - 5/18 say product-specific or supplemental terms apply when the user uses that product, and
    win on conflict.
  - 1/18 lets an organisation's own contract override the terms for its members.
- **Quote:** "If those additional terms apply (for example, because you use the applicable Services), then they will become part of these Terms, meaning that you must comply with them." (s10)
- **Commonly omitted:** an order of precedence among the companion policies themselves.

### eligibility: Who may use the product

- **Covers:** minimum age, parental consent, legal capacity, acting for an organisation, and
  other conditions of use.
- **Prevalence:** 26/30 (87%), core
- **Applies when:** always
- **Facts:** `facts.product.min_age`, `facts.product.child_directed`, `facts.product.business_use`
- **Patterns:**
  - About 22/26 state a fixed minimum age; 7/26 raise it to a higher local age where one
    applies; 2/26 defer to the local age of majority only.
  - 12/26 let younger users in with a parent's or guardian's consent, sometimes making the parent
    responsible for the minor's acts.
  - 9/26 cover accepting on behalf of a company: the person warrants authority and "you" then
    means the company.
  - 6/26 write the conditions as a bullet list of what the user represents.
  - 5/26 add that the user is not on a sanctions list; 4/26 limit use to residents of the
    company's home country.
  - 4/26 add that children's data is deleted once the company learns of it.
- **Quote:** "No one under 13 is allowed to use or access the Services." (s19)
- **Commonly omitted:** how age is checked (1/26 says the company may verify it).

### account: Your account

- **Covers:** registration, accurate information, credential security, responsibility for
  activity on the account, and account types.
- **Prevalence:** 23/30 (77%), common
- **Applies when:** `facts.product.has_accounts == true`
- **Facts:** `facts.product.has_accounts`, `facts.product.business_use`, `facts.product.integrations`
- **Patterns:**
  - About 19/23 make the user responsible for credentials and for everything done on the
    account; about 18/23 require accurate, current information.
  - About 14/23 ask the user to report unauthorised use at once.
  - 7/23 ban sharing or transferring the account.
  - 7/23 cover organisation, team, managed or brand accounts, including an admin's power over
    members' accounts.
  - 4/23 allow sign-in through a third-party account and say that provider's terms apply.
  - 5/23 say the company cannot guarantee security, some adding advice (strong password,
    two-factor).
  - 4/23 let the company reclaim or change usernames; 3/23 cover identity checks.
- **Quote:** "You are responsible for any activity that occurs in your account." (s10)
- **Commonly omitted:** what happens to the account after the user's death (1/30, in the
  closing clauses).

### privacy: Privacy

- **Covers:** where the privacy policy is and how it relates to the terms.
- **Prevalence:** 23/30 (77%), common
- **Applies when:** always
- **Facts:** `facts.company.published_policies`, `facts.data.storage_locations`
- **Patterns:**
  - 23/23 point to the privacy policy by link, most in one or two sentences.
  - About 12/23 treat use of the product as agreement to the policy.
  - 3/23 add that data is processed in the company's home country.
  - 2/23 add a short statement on data security.
- **Quote:** "Your privacy matters to us." (s10)
- **Commonly omitted:** any summary of the policy's content.

### licence: Your licence to use the product

- **Covers:** the licence the company grants the user to use the service and install the app,
  with its limits.
- **Prevalence:** 25/30 (83%), core
- **Applies when:** always
- **Facts:** `facts.product.services_in_scope`
- **Patterns:**
  - About 22/25 grant a limited, revocable, non-exclusive, non-transferable licence.
  - About 12/25 limit it to personal, non-commercial use.
  - About 8/25 say the app is licensed, not sold, often per device the user owns.
  - About 9/25 have the user consent to automatic updates.
  - 7/25 list software restrictions (copy, modify, reverse engineer) inside the licence.
  - 5/25 say open-source components keep their own licences, which win for those parts.
  - 5/25 reserve every right not expressly granted.
- **Quote:** none
- **Commonly omitted:** a licence end date other than termination.

### acceptable-use: Rules of use

- **Covers:** what users may not do with the product or post on it.
- **Prevalence:** 28/30 (93%), core
- **Applies when:** always
- **Facts:** `facts.product.public_content`, `facts.company.published_policies`
- **Patterns:**
  - About 16/28 give a bullet list of prohibited uses; the rest one long sentence of
    semicolon-separated items.
  - About 7/28 point to a separate acceptable use policy or community guidelines as part of the
    terms.
  - About 15/28 ban scraping, bots and automated access; about 12/28 reverse engineering.
  - 8/28 ban commercial use without permission; 4/28 ban competitors or building a competing
    product; 4/28 ban using content to train AI models.
  - 5/28 add a separate list of prohibited content.
  - 3/28 add rules tied to the product (excessive use, behaviour at real-world places, profile
    photos).
  - 2/28 say only that use must be lawful.
- **Quote:** "You may not access or use, or help another person to access or use, our Services in the following ways:" (s01)
- **Commonly omitted:** the consequence of each breach (most refer to the termination section).

### user-content: Your content

- **Covers:** who owns what users upload or create, the licence the user grants the company (and
  other users), and the user's promises about it.
- **Prevalence:** 23/30 (77%), common
- **Applies when:** always
- **Facts:** `facts.product.public_content`, `facts.product.ai_features`, `facts.data.targeted_ads`
- **Patterns:**
  - About 17/23 say the user keeps ownership.
  - About 19/23 take a broad worldwide, royalty-free, sublicensable licence; about 14/23 make it
    perpetual and irrevocable.
  - 2/23 take a narrow licence only to store and run the service; 4/23 scale the licence by who
    can see the content (private, shared, public).
  - About 16/23 have the user warrant they hold the rights and consents; 7/23 as a bullet list.
  - 8/23 extend the licence to the user's name and likeness in promotion; 4/23 license the
    content to other users; 4/23 waive moral rights where law allows.
  - 4/23 say content may be used to train AI models.
  - 5/23 warn that shared content may become public.
- **Quote:** "First and foremost, you own what you create." (s02)
- **Commonly omitted:** an end date for the licence after deletion.

### content-moderation: Content moderation

- **Covers:** the company's right to review and remove content, responsibility for others'
  content, reporting, and appeals.
- **Prevalence:** 20/30 (67%), common
- **Applies when:** `facts.product.public_content != none`
- **Facts:** `facts.product.public_content`, `facts.company.contact_email`
- **Patterns:**
  - About 14/20 reserve a right, not a duty, to monitor and remove content; 5/20 for any or no
    reason, without notice.
  - 8/20 say each poster alone is responsible for their content.
  - 8/20 describe how to report content; 6/20 how to appeal a decision.
  - 7/20 allow preserving and disclosing content to meet legal process, enforce the terms or
    protect safety.
  - 3/20 describe the mix of automated tools and human review.
- **Quote:** "However, we do not review all content on our Services." (s10)
- **Commonly omitted:** response times for reports and appeals.

### ai-features: AI features

- **Covers:** AI inputs and outputs, their accuracy, who owns outputs, and limits on AI use.
- **Prevalence:** 13/30 (43%), common
- **Applies when:** `facts.product.ai_features != []`
- **Facts:** `facts.product.ai_features`, `facts.processors.list`
- **Patterns:**
  - About 11/13 warn that output may be wrong and that the user must check it.
  - 6/13 define inputs and outputs and fold them into the content licence.
  - 4/13 give the user the company's rights in outputs; 2/13 warn that outputs may not be
    unique.
  - 3/13 list prohibited AI uses; 2/13 ban training other models on outputs or passing output
    off as human-made.
  - 3/13 cover AI agents acting for the user, requiring the user to confirm actions.
  - 3/13 name the use of third-party AI vendors; 1/13 gives an opt-out from model training.
- **Quote:** "AI technologies have known and unknown risks and limitations and may make mistakes; you understand and agree that you use AI Features at your own risk." (s04)
- **Commonly omitted:** model provider names; where processing runs.

### feedback: Feedback

- **Covers:** suggestions users send and the company's right to use them.
- **Prevalence:** 18/30 (60%), common
- **Applies when:** always
- **Facts:** none
- **Patterns:**
  - About 17/18 let the company use feedback freely, without payment or credit.
  - About 9/18 say feedback is not confidential.
  - 5/18 take a perpetual licence or ownership of feedback.
  - 4/18 tell users not to send ideas they do not want to give away.
  - 8/18 fold it into the content or IP section.
- **Quote:** none
- **Commonly omitted:** a way to withdraw feedback.

### company-ip: Our intellectual property

- **Covers:** the company's ownership of the product, its brand, and data derived from use.
- **Prevalence:** 24/30 (80%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`
- **Patterns:**
  - 24/24 state the company and its licensors own the product and its content.
  - About 12/24 require written permission to use the company's marks; third-party marks belong
    to their owners.
  - About 10/24 reserve every right not granted and deny any implied licence.
  - About 8/24 list forbidden uses of the company's content (copy, frame, scrape, resell).
  - 3/24 claim rights in usage data derived from use; 2/24 set rules for linking to the site.
- **Quote:** "You understand that we own Substack." (s02)
- **Commonly omitted:** patents (2/24).

### copyright-complaints: Copyright complaints

- **Covers:** how rights holders report infringing content, how users respond, and what happens
  to repeat infringers.
- **Prevalence:** 22/30 (73%), common
- **Applies when:** `facts.product.public_content != none`
- **Facts:** `facts.company.contact_email`, `facts.company.address`, `facts.company.published_policies`
- **Patterns:**
  - About 11/22 list the required contents of a notice as bullets.
  - 7/22 point to a separate copyright policy instead.
  - About 13/22 terminate repeat infringers; 9/22 give a counter-notice procedure with a
    restoration window.
  - About 10/22 give a contact block for notices (name or role, postal address, email).
  - 5/22 extend the procedure to trademarks; 5/22 warn about liability for false notices; 3/22
    say notices are forwarded to the poster.
- **Quote:** "Snap respects the rights of others." (s10)
- **Commonly omitted:** response times.

### communications: Messages from us

- **Covers:** texts, calls, push notifications and emails the company sends, consent to them,
  opt-out and carrier charges.
- **Prevalence:** 12/30 (40%), common
- **Applies when:** `facts.marketing.sms != none` or `facts.marketing.email == true` or `facts.marketing.push != none`
- **Facts:** `facts.marketing.sms`, `facts.marketing.email`, `facts.marketing.push`
- **Patterns:**
  - 8/12 cover text messages: consent by giving a number, opt-out by replying STOP, help by
    replying HELP.
  - About 7/12 say carrier charges apply; 4/12 add device-compatibility limits.
  - 4/12 accept electronic notices as satisfying any "in writing" requirement.
  - 3/12 cover marketing-email opt-out; 3/12 push notifications.
- **Quote:** "Message frequency varies." (s06)
- **Commonly omitted:** how often messages are sent, beyond "varies".

### fees-payment: Fees and payment

- **Covers:** prices, billing, payment methods and processors, taxes, price changes and failed
  payments.
- **Prevalence:** 27/30 (90%), core
- **Applies when:** `facts.sales.purchase_channels != []`
- **Facts:** `facts.sales.purchase_channels`, `facts.sales.payment_provider`, `facts.company.change_notice`
- **Patterns:**
  - About 16/27 promise notice before a price change, taking effect from the next billing
    period; about 6/27 treat continued use as acceptance, about 5/27 let the user cancel first.
  - About 11/27 say a third-party processor handles payment under its own terms and the company
    does not store card data.
  - About 10/27 have the user authorise recurring charges; about 10/27 put taxes on the user;
    about 8/27 require billing details to be kept current.
  - 8/27 cover failed payments (access cut, amounts still owed).
  - 5/27 point to a pricing page instead of stating prices; 2/27 send all payment terms to a
    separate document.
  - 3/27 allow the card issuer to update card details; 2/27 ask users to contact support before
    a chargeback.
- **Quote:** "Notwithstanding any amounts owed to Partiful for the Premium Features, Partiful does not process payment card transactions." (s06)
- **Commonly omitted:** actual prices (most point to the store or a pricing page); the currency
  (2/27 state it).

### subscriptions: Subscriptions, renewal and cancellation

- **Covers:** plans, automatic renewal, how and when to cancel, free trials and plan changes.
- **Prevalence:** 23/30 (77%), common
- **Applies when:** `facts.sales.subscription != none`
- **Facts:** `facts.sales.subscription`, `facts.sales.free_trial`, `facts.sales.plans`, `facts.sales.purchase_channels`
- **Patterns:**
  - About 19/23 renew automatically for the same period until cancelled; 5/23 at the then-current
    price.
  - About 16/23 say how to cancel, often separately for app-store and web purchases; 4/23 give the
    menu path step by step.
  - About 12/23 keep access to the end of the paid period after cancelling; 5/23 give a deadline
    before renewal (hours or days).
  - 13/23 cover free trials; about 10/13 convert to paid automatically unless cancelled.
  - 3/23 warn that deleting the app or account does not cancel the subscription.
  - 4/23 set the renewal terms in all caps; 3/23 define a lifetime plan as lasting only while the
    product exists.
  - 4/23 cover upgrades and downgrades; 3/23 point to separate subscription terms.
- **Quote:** "Deleting the Mobile App does not cancel your Subscription." (s06)
- **Commonly omitted:** a reminder before a trial converts (1/13 promises one).

### refunds: Refunds

- **Covers:** whether and when payments are refunded.
- **Prevalence:** 23/30 (77%), common
- **Applies when:** `facts.sales.purchase_channels != []`
- **Facts:** `facts.sales.refund_rule`, `facts.sales.partial_refunds`, `facts.sales.purchase_channels`
- **Patterns:**
  - About 16/23 make payments non-refundable except where the law requires.
  - 6/23 allow refunds case by case at the company's discretion.
  - 7/23 send app-store purchases to the store's refund process.
  - 6/23 refuse refunds for partly used periods; 2/23 refund prepaid fees pro rata if the product
    is discontinued.
  - 3/23 point to a separate refund policy; 2/23 put the no-refund rule in all caps.
  - 9/23 give it only a sentence or two inside the payment, subscription or termination section;
    about 9/23 give refunds a heading of their own.
- **Quote:** "All fees are non-refundable unless legally required or explicitly stated by Deglaze." (s12)
- **Commonly omitted:** how to request a refund (4/23 say how).

### promotions: Promotions, referrals and gift cards

- **Covers:** referral rewards, promo codes, gift cards and contests.
- **Prevalence:** 10/30 (33%), rare
- **Applies when:** `facts.sales.promotions != []` or `facts.sales.gifts != none`
- **Facts:** `facts.sales.promotions`, `facts.sales.gifts`
- **Patterns:**
  - 5/10 cover referral rewards: who qualifies, one reward per referral, clawback for abuse.
  - 4/10 cover promo codes or offers (no stacking, no cash value, new users only); 4/10 gift
    cards or gifted plans.
  - 2/10 say a promotion's own rules win on conflict; 2/10 put contests users run themselves on
    the user.
- **Quote:** "You agree that if you use our service to administer your promotion, you do so at your own risk." (s27)
- **Commonly omitted:** reward amounts.

### app-stores: App stores

- **Covers:** the terms the app stores require, and the stores' role in billing and refunds.
- **Prevalence:** 19/30 (63%), common
- **Applies when:** `facts.product.services_in_scope` includes kind `ios` or `android`
- **Facts:** `facts.product.services_in_scope`, `facts.sales.purchase_channels`, `facts.company.contact_email`
- **Patterns:**
  - 13/19 restate the Apple-required clauses (the agreement is with the company, not Apple; Apple
    gives no support; Apple's only warranty duty is refunding the price; Apple is a third-party
    beneficiary); 5/13 as bullets.
  - 3/19 add matching clauses for Google Play.
  - 8/19 say purchases through a store follow the store's billing and refund terms.
  - 2/19 ask consent to share usage data with the store when it decides a refund.
- **Quote:** "If you purchase access to our Services through a distributor (e.g. an app store) ( "App Distributor" ), then you will make payment to the App Distributor, and the App Distributor's terms in relation to payment methods, billing, and refunds will apply instead." (s01)
- **Commonly omitted:** a link to the store's own terms.

### feature-terms: Feature-specific terms

- **Covers:** rules for one feature or business line of the product that the general sections do
  not handle.
- **Prevalence:** 19/30 (63%), common
- **Applies when:** `facts.product.features != []`
- **Facts:** `facts.product.features`, `facts.product.integrations`
- **Patterns:**
  - One section per feature, usually after the payment sections; financial and marketplace
    products run to dozens of sections.
  - Kinds seen: orders and delivery (2/19), financial products (2/19), creator, host or
    marketplace roles (3/19), virtual items (2/19), community features such as clubs, moderators
    and reviews (4/19), bank or data aggregation (2/19), location sharing (2/19), licences for
    the company's public data (1/19).
  - Each repeats the general pattern: what the feature is, who may use it, its limits, and that
    the company is not liable for third parties involved.
- **Quote:** "When you agree to a third-party Creator's terms, you understand that any such agreement is directly between you and the issuing Creator, and that Substack is not a party to any such terms." (s02)
- **Commonly omitted:** features that only process data (sync, backup), which go to the privacy
  policy instead.

### beta-features: Beta features

- **Covers:** preview or early-access features and their risks.
- **Prevalence:** 7/30 (23%), rare
- **Applies when:** `facts.product.beta_features == true`
- **Facts:** `facts.product.beta_features`
- **Patterns:**
  - 6/7 provide them as is, at the user's own risk; 3/7 in all caps.
  - 4/7 let the company withdraw them at any time; 2/7 offer no support.
  - 1/7 asks users to keep beta software confidential.
- **Quote:** none
- **Commonly omitted:** how beta features are labelled (1/7).

### third-party-services: Third-party services and links

- **Covers:** links, integrations, products and ads from third parties.
- **Prevalence:** 24/30 (80%), core
- **Applies when:** always
- **Facts:** `facts.product.integrations`, `facts.data.targeted_ads`
- **Patterns:**
  - About 20/24 disclaim control, endorsement and liability for third-party sites and services.
  - About 10/24 say the third party's own terms and privacy policy govern.
  - 6/24 cover integrations the user connects; 6/24 say ads may appear, including next to the
    user's content.
  - 5/24 say purchases from third parties are between the user and them; 3/24 have the user
    release the company.
- **Quote:** "All sales and transactions are conducted directly between you and the Third-Party Services." (s06)
- **Commonly omitted:** names of integrated services (5/24 name some).

### user-interactions: Dealings between users

- **Covers:** the user's responsibility for dealings and disputes with other users.
- **Prevalence:** 8/30 (27%), rare
- **Applies when:** `facts.product.public_content != none`
- **Facts:** `facts.product.public_content`
- **Patterns:**
  - 6/8 make dealings between users solely their own affair; 4/8 let the company step in but
    not be obliged to.
  - 3/8 say the company does not verify users' identities.
  - 5/8 have the user release the company from claims arising from such disputes, 2/8 waiving a
    statute that protects unknown claims.
- **Quote:** none
- **Commonly omitted:** a dispute channel between users.

### export-sanctions: Export controls and use from other countries

- **Covers:** export and sanctions restrictions, and the user's duty to follow local law when
  using the product from another country.
- **Prevalence:** 16/30 (53%), common
- **Applies when:** always
- **Facts:** `facts.company.country`
- **Patterns:**
  - 10/16 have the user represent that they are not on a sanctions list or in an embargoed
    country, usually naming the company's home country's lists.
  - 8/16 say the product is run from the company's home country and users elsewhere are
    responsible for their local law.
  - 1/16 bans using a VPN to get around the restrictions.
- **Quote:** none
- **Commonly omitted:** which countries are excluded.

### service-changes: Changes to the product

- **Covers:** the company's right to change, suspend or discontinue the product or features, and
  downtime.
- **Prevalence:** 21/30 (70%), common
- **Applies when:** always
- **Facts:** none
- **Patterns:**
  - About 20/21 reserve the right to change or stop any part at any time; about 12/21 without
    notice or liability.
  - 5/21 promise reasonable efforts to give notice of material adverse changes.
  - 3/21 cover maintenance downtime; 2/21 let the company add mandatory features or updates.
  - About 8/21 fold it into the terms-changes or termination section.
- **Quote:** "Our Services are novel and will change." (s01)
- **Commonly omitted:** data export or refunds when a feature ends (2/21 refund prepaid fees).

### terms-changes: Changes to these terms

- **Covers:** how the terms change, how users are told, and when changes bind them.
- **Prevalence:** 27/30 (90%), core
- **Applies when:** always
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - About 24/27 treat continued use after the change as acceptance.
  - About 16/27 promise notice of material changes by email or in the product; 7/27 a fixed number
    of days in advance.
  - 6/27 make changes effective on posting and put the duty to check on the user.
  - About 10/27 say a user who disagrees must stop using the product or close the account; 4/27
    give an explicit right to terminate over a change.
  - 3/27 keep the old terms for disputes that arose earlier; 3/27 let the company alone decide
    what is material; 3/27 give example reasons for changes.
- **Quote:** "If you don't agree with the new Terms, you are free to reject them; unfortunately, that means you will no longer be able to use Substack." (s02)
- **Commonly omitted:** a summary of what changed (1/27).

### termination: Suspension and termination

- **Covers:** when the company may suspend or end a user's access, how the user may end the
  terms, and what follows.
- **Prevalence:** 29/30 (97%), core
- **Applies when:** always
- **Facts:** `facts.product.has_accounts`, `facts.data.deletion_lag`
- **Patterns:**
  - About 18/29 let the company terminate for any reason at its sole discretion; nearly all for
    breach; about 14/29 without notice.
  - 5/29 promise notice and a way to appeal, at least where safety allows.
  - About 15/29 list the clauses that survive termination.
  - 7/29 delete the user's content or data on termination; 7/29 may close long-inactive
    accounts.
  - 6/29 refuse refunds on termination; 2/29 bar the user from opening a new account.
  - 2/29 describe a ladder of measures (warning, limits, suspension, ban).
- **Quote:** "Mochi reserves the right to terminate your account without cause." (s15)
- **Commonly omitted:** time for the user to retrieve content before closure (1/29).

### account-closure: Closing your account

- **Covers:** how the user closes or deletes the account and what happens to the content.
- **Prevalence:** 18/30 (60%), common
- **Applies when:** `facts.product.has_accounts == true`
- **Facts:** `facts.users.rights_channels`, `facts.data.deletion_lag`, `facts.sales.subscription`
- **Patterns:**
  - 15/18 sit as a sentence or two inside the termination section.
  - 8/18 point to a settings path in the product; 5/18 to an email request; 4/18 say the user may
    simply stop using the product.
  - 3/18 warn that deleting the app does not close the account or cancel a store subscription.
  - 4/18 say some content or backups remain after deletion; 2/18 cover recovery after a mistaken
    deletion; 1/18 gives a deletion time.
- **Quote:** "You may terminate these Terms at any time and for any reason by deleting your Account and discontinuing use of all Services." (s19)
- **Commonly omitted:** how long deletion takes (17/18).

### disclaimers: Disclaimers

- **Covers:** the warranties the company disclaims, and product-specific disclaimers.
- **Prevalence:** 30/30 (100%), core
- **Applies when:** always
- **Facts:** `facts.product.risk_domains`, `facts.product.ai_features`
- **Patterns:**
  - About 27/30 provide the product "as is" and "as available"; about 22/30 name the implied
    warranties disclaimed (merchantability, fitness, non-infringement).
  - About 19/30 set it in all caps; 7/30 deliberately in sentence case.
  - About 14/30 list what is not promised (uninterrupted, error-free, secure, accurate).
  - About 12/30 add that some jurisdictions do not allow these exclusions.
  - 8/30 add disclaimers for the product's domain: not medical, financial or professional advice;
    physical risk of activities; no guaranteed matches; connectivity.
  - 6/30 disclaim other users' and third parties' conduct; 4/30 disclaim lost data and tell users
    to keep their own backups.
- **Quote:** "Substack is provided to you on an "as-is" basis." (s02)
- **Commonly omitted:** any positive warranty (1/30 promises performance and uptime).

### liability: Limitation of liability

- **Covers:** the damages the company excludes and the cap on its liability.
- **Prevalence:** 29/30 (97%), core
- **Applies when:** always
- **Facts:** `facts.company.liability_cap`
- **Patterns:**
  - About 28/29 exclude indirect, consequential and special damages and lost profits or data;
    5/29 exclude direct damages too.
  - About 14/29 cap liability at the greater of fees paid in a recent period (often 12 months) or
    a fixed sum; 4/29 a fixed sum only; 3/29 fees paid only; 4/29 set no cap.
  - About 20/29 in all caps; 6/29 in sentence case.
  - About 12/29 add that some jurisdictions do not allow the limits; 5/29 carve out liability that
    cannot be excluded (death or injury from negligence, fraud, gross negligence).
  - 5/29 make stopping use the user's sole remedy; 4/29 call the limits an essential basis of the
    bargain.
- **Quote:** none
- **Commonly omitted:** different caps for paying and free users (2/29).

### indemnity: Indemnity

- **Covers:** the user's duty to cover the company's losses from claims the user causes.
- **Prevalence:** 28/30 (93%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`
- **Patterns:**
  - 28/28 cover third-party claims from the user's use, breach of the terms, content or breach of
    law; about 20/28 list the triggers.
  - About 14/28 define a protected group (affiliates, officers, employees).
  - 12/28 let the company take over the defence; 4/28 forbid settling without the company's
    consent.
  - About 9/28 are one sentence with no defence mechanics.
  - 6/28 limit it "to the extent permitted by law"; 3/28 extend it to others using the user's
    account.
- **Quote:** "In summary: If you cause us some damage, you will compensate us." (s10)
- **Commonly omitted:** a cap on the user's indemnity.

### dispute-resolution: Resolving disputes

- **Covers:** how disputes are raised and decided: informal resolution, the forum, waivers, and
  time limits.
- **Prevalence:** 24/30 (80%), core
- **Applies when:** always
- **Facts:** `facts.company.dispute_forum`, `facts.company.contact_email`, `facts.company.address`
- **Patterns:**
  - 19/24 require a notice of dispute and an informal resolution period first, usually with a
    waiting period in days.
  - When `facts.company.dispute_forum == arbitration` (19/24): binding individual arbitration with
    a class-action waiver; about 18/24 also waive a jury; about 14/24 keep small-claims court;
    about 10/24 keep court for intellectual-property claims and injunctions; about 17/24 name the
    provider and its rules; about 14/24 allocate fees.
  - Arbitration samples add: an all-caps notice at the top of the terms (16/24); an opt-out
    window after sign-up (8/24); a right to reject later changes to the clause (5/24);
    procedures for mass filings (11/24).
  - When the forum is the courts (5/24): one paragraph on informal resolution, a jury waiver or
    the company's right to court injunctions.
  - 9/24 set a time limit to bring claims (often one year).
- **Quote:** "We want to address any disputes without needing arbitration." (s10)
- **Commonly omitted:** mediation.

### governing-law: Governing law and courts

- **Covers:** which law governs the terms and which courts hear disputes.
- **Prevalence:** 28/30 (93%), core
- **Applies when:** always
- **Facts:** `facts.company.governing_law`, `facts.company.country`
- **Patterns:**
  - About 25/28 name the law of the company's home state or country, excluding its conflict-of-law
    rules.
  - About 18/28 name exclusive courts in one city or district; 4/28 name the law only.
  - 6/28 let consumers keep their home country's mandatory law and courts.
  - 6/28 exclude the UN Convention on Contracts for the International Sale of Goods.
  - Usually one or two sentences; 5/28 embedded in the closing boilerplate.
- **Quote:** none
- **Commonly omitted:** the reason for the chosen law.

### general: General terms

- **Covers:** standard closing clauses: entire agreement, severability, waiver, assignment,
  relationship, notices, force majeure, interpretation and language.
- **Prevalence:** 27/30 (90%), core
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.address`
- **Patterns:**
  - About 18/27 bundle the clauses under one heading, one or two sentences each; about 9/27 give
    each its own heading.
  - Clauses: severability and waiver (about 25/27), entire agreement (about 24/27), assignment
    with the company free to assign and the user needing consent (about 22/27), no partnership or
    agency (about 10/27), notices (about 9/27), force majeure (about 8/27), third-party
    beneficiaries (about 8/27), headings and "including" (about 8/27).
  - 6/27 say the English version prevails over translations; 4/27 admit a printed copy as
    evidence.
- **Quote:** "Under applicable law, you may have certain rights that can't be limited by a contract." (s22)
- **Commonly omitted:** a confidentiality clause (1/27).

### contact: Contact us

- **Covers:** how to reach the company about the terms.
- **Prevalence:** 20/30 (67%), common
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.address`, `facts.company.phone`
- **Patterns:**
  - 18/20 close the document; 2/20 give it only in the opening.
  - About 14/20 give an email; about 10/20 a postal address; 3/20 only a link to a support page
    or form; 3/20 a phone number.
  - 4/20 set it as a field block (entity, address, email, phone).
- **Quote:** "If you have any questions about these Terms please email us." (s16)
- **Commonly omitted:** response times; a named person.

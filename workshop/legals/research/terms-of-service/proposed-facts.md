# terms-of-service: proposed fact keys

Merged into `helpers/facts-schema.md` on 2026-10-26; see the key map below.

Keys the `terms-of-service` skeleton names that `helpers/facts-schema.md` lacks, in its entry format,
under their intended shared names. Three reuse names the `tr` region already proposes
(`regions/tr/facts.md` *Proposed shared key*): `facts.company.phone`, `facts.sales.subscription`,
`facts.sales.payment_provider`. The maintainer moves them into `helpers/facts-schema.md`.

## Company

### facts.company.phone
- **Means:** a phone line users can call about the service, if the company offers one.
- **Type:** string or none
- **Look:** website footer, contact page, support settings, store metadata (App Store support
  phone, Play *About the developer*).
- **Ask:** "Is there a phone number users can call? If so, which?" Recommend none unless a
  support line is published.

### facts.company.published_policies
- **Means:** the company's other public legal documents that the terms point to or make part of
  themselves (privacy policy, acceptable use policy, community guidelines, refund policy,
  subscription terms, copyright policy), with their URLs.
- **Type:** list of (title, url, incorporated: bool)
- **Look:** existing legal docs, footer and settings links in the app and website, the documents
  the current write run produces.
- **Ask:** "Which other policies should the terms link to, and which should be part of the
  terms?" Recommend every document this run writes plus those already published, with the
  privacy policy linked but not incorporated.

### facts.company.governing_law
- **Means:** the law that governs the terms and the courts where disputes go when they go to
  court.
- **Type:** record (law: country or state, courts: city or district)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Which law should govern the terms, and which city's courts should hear disputes?"
  Recommend the law and courts of the company's registered seat (`facts.company.country`,
  `facts.company.address`).

### facts.company.dispute_forum
- **Means:** how disputes with users are resolved: in court, or by binding individual
  arbitration; and whether an informal step comes first.
- **Type:** record (forum: enum [courts, arbitration], informal_first: bool, provider)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Should disputes go to court, or to binding individual arbitration? Do you want users
  to contact you first to try to settle?" Recommend courts with an informal step first;
  arbitration only on the advice of a lawyer in a country where consumer arbitration is
  enforceable.

### facts.company.liability_cap
- **Means:** the cap on the company's total liability to a user, if any.
- **Type:** record (basis: enum [greater-of, fees-paid, fixed, none], months, amount, currency)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Should the terms cap your liability? A common choice is the greater of what the user
  paid in the last 12 months or a small fixed amount." Recommend `greater-of`, 12 months, 100 in
  the company's currency.

## Product

### facts.product.business_use
- **Means:** whether organisations use the product as such: team or organisation accounts,
  accounts made on behalf of a company, brand accounts, admins who control members' accounts.
- **Type:** record (org_accounts: bool, admin_control: bool, separate_business_terms_url) or none
- **Look:** team, workspace, organisation or admin models; domain-based account linking; seat
  billing; business plans in pricing code.
- **Ask:** "Can companies or schools use the product as an organisation, with admins over their
  members' accounts?" Recommend what the code shows; none for a single-user app.

### facts.product.beta_features
- **Means:** whether the product offers beta, preview or early-access features to users.
- **Type:** bool
- **Look:** feature flags exposed to users, "beta" or "labs" labels, TestFlight or Play testing
  tracks offered publicly.
- **Ask:** "Do users get beta or preview features?" Recommend what the code shows.

### facts.product.risk_domains
- **Means:** areas where users might rely on the product's information or features in ways that
  risk their health, money, safety or legal position, which call for a specific disclaimer.
- **Type:** list of enum [health, fitness, mental-health, finance, tax, legal, navigation, outdoor-safety, other]
- **Look:** app category, health or finance SDKs (HealthKit, Health Connect, Plaid), workout,
  diagnosis, budgeting or route features, store age-rating and category answers.
- **Ask:** "Could users rely on the app for health, financial, legal or safety decisions?"
  Recommend the domains the category and code suggest; none for a general productivity tool.

## Sales

### facts.sales.channels
- **Means:** where users buy paid features: the App Store, Google Play, the company's own web
  checkout, or elsewhere. Empty when nothing is sold.
- **Type:** list of enum [app-store, google-play, web, other]
- **Look:** in-app purchase and subscription SDKs (StoreKit, Play Billing, RevenueCat), web
  checkout code (Stripe, Paddle, Lemon Squeezy), store product configuration.
- **Ask:** "Where can users pay: in the App Store, Google Play, on your website?" Recommend what
  the code shows.

### facts.sales.subscription
- **Means:** subscription plans: billing periods, automatic renewal, free trials, lifetime
  plans, and how the user cancels on each channel.
- **Type:** record (periods, auto_renews: bool, trial_days, lifetime: bool, cancel_path per channel) or none
- **Look:** subscription SDKs and plans (RevenueCat, App Store / Play subscriptions, Stripe
  Billing), trial configuration, "manage subscription" screens.
- **Ask:** "Do you sell subscriptions? Which periods, is there a free trial, and how does the
  user cancel?" Recommend what the code shows.
- **Note:** same name and meaning as the `tr` proposal `facts.tr.subscription`, with trial and
  lifetime fields added.

### facts.sales.payment_provider
- **Means:** the payment institution that processes payments outside the app stores, and
  whether the company stores card data itself.
- **Type:** record (name, stores_card_data: bool) or none
- **Look:** payment SDKs and API clients; card-vault or tokenisation code.
- **Ask:** "Which payment provider processes web payments, and do you store card numbers
  yourselves?" Recommend "does not store card data" when only a provider's hosted form or token
  is used.

### facts.sales.refund_policy
- **Means:** the company's own refund rule for purchases it sells directly (app-store purchases
  follow the store's rules).
- **Type:** record (rule: enum [none-except-law, case-by-case, money-back-window], window_days, prorated_on_discontinuation: bool)
- **Look:** existing refund page or help article; refund handling in payment code
  (Stripe refunds, RevenueCat refund handling).
- **Ask:** "Do you refund purchases? Never unless the law requires, case by case, or within a
  money-back window?" Recommend `none-except-law` with case-by-case exceptions, which most
  samples state.

### facts.sales.promotions
- **Means:** promotional programmes the product runs: referral rewards, promo codes, gift cards
  or gifted plans, contests run by the company or by users.
- **Type:** list of enum [referral, promo-codes, gift-cards, contests, user-contests]
- **Look:** referral, coupon, offer-code and gift models; RevenueCat or store offer codes;
  invite-link rewards.
- **Ask:** "Do you run referral rewards, promo codes, gift subscriptions or contests?" Recommend
  what the code shows.

## Marketing

### facts.marketing.sms
- **Means:** whether the company sends text messages to users (verification codes, service
  alerts, marketing).
- **Type:** enum [none, verification-only, service, service-and-marketing]
- **Look:** SMS providers (Twilio, Vonage, MessageBird, Firebase phone auth), phone-number
  fields, SMS templates.
- **Ask:** "Do you send text messages, and are any of them promotional?" Recommend what the code
  shows.

## Key map

| Proposed | Final | Note |
| --- | --- | --- |
| `facts.company.phone` | `facts.company.phone` |  |
| `facts.company.published_policies` | `facts.company.published_policies` |  |
| `facts.company.governing_law` | `facts.company.governing_law` |  |
| `facts.company.dispute_forum` | `facts.company.dispute_forum` |  |
| `facts.company.liability_cap` | `facts.company.liability_cap` |  |
| `facts.product.business_use` | `facts.product.business_use` |  |
| `facts.product.beta_features` | `facts.product.beta_features` |  |
| `facts.product.risk_domains` | `facts.product.risk_domains` |  |
| `facts.sales.channels` | `facts.sales.purchase_channels` |  |
| `facts.sales.subscription` | `facts.sales.subscription` | `trial_days` moved to `facts.sales.free_trial`, `lifetime` to `facts.sales.plans` |
| `facts.sales.payment_provider` | `facts.sales.payment_provider` |  |
| `facts.sales.refund_policy` | `facts.sales.refund_rule` | `prorated_on_discontinuation` moved to `facts.sales.partial_refunds` |
| `facts.sales.promotions` | `facts.sales.promotions` | `gift-cards` moved to `facts.sales.gifts` |
| `facts.marketing.sms` | `facts.marketing.sms` |  |

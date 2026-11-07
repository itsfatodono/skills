# refund-policy: proposed fact keys

Merged into `helpers/facts-schema.md` on 2026-10-26; see the key map below.

Keys the `refund-policy` skeleton names that are not in `helpers/facts-schema.md`, in its format, under
their intended shared names. Four reuse the `tr` region's *Proposed shared key* names
(`regions/tr/facts.md`) with the same meaning; their text is adapted from there, with the
change noted. The rest are new. The maintainer moves them into `helpers/facts-schema.md`.

## Reused from `regions/tr/facts.md` (proposed shared names)

### facts.sales.offer_type
- **Means:** what the company sells: physical goods, digital content (files, codes, software
  access, in-app content, subscriptions to content), services, or a mix.
- **Type:** enum [physical, digital-content, service, mixed]
- **Look:** product models and checkout code (shipping address required or not), cart line
  types, download or licence delivery code, in-app purchase and subscription products.
- **Ask:** "Do you sell physical goods, digital content, services, or a mix?" Recommend what
  the checkout code shows.
- **Origin:** `facts.tr.offer_type`, same meaning.

### facts.sales.subscription
- **Means:** recurring plans: billing periods, automatic renewal, renewal notice, how the buyer
  cancels, and free trials.
- **Type:** record (periods, auto_renews: bool, renewal_notice: bool, cancel_path, trial) or none
- **Look:** subscription SDKs and plans (RevenueCat, StoreKit, Play Billing, Stripe Billing,
  Paddle), "cancel subscription" screens, trial configuration.
- **Ask:** "Do you sell subscriptions? If so, how often is the buyer charged, does it renew
  automatically, is there a free trial, and how does the buyer cancel?" Recommend what the
  code shows.
- **Origin:** `facts.tr.subscription`; `trial` added, which the refund samples need.

### facts.sales.return_address
- **Means:** the address returned goods are sent to, when it differs from the seller's address.
- **Type:** string or none
- **Look:** return-label integrations, warehouse settings, existing returns page.
- **Ask:** "Where should buyers send returns, if not to your company address?" Recommend "same
  as the company address".
- **Origin:** `facts.tr.return_address`, same meaning.

## New keys

### facts.sales.purchase_channels
- **Means:** every place a buyer can pay for the product, and who decides and pays the refund
  for purchases made there.
- **Type:** list of (channel: enum [app-store, google-play, other-app-store, website,
  merchant-of-record, reseller, retail-store, own-store], name, refunds_by: enum [store,
  company, reseller], store_window)
- **Look:** in-app purchase SDKs (StoreKit, Play Billing, RevenueCat store configuration),
  web checkout (Stripe, Paddle, Lemon Squeezy, FastSpring: the last three are merchants of
  record), licence-key or gift-card resale code, platform folders (`ios/`, `android/`,
  `macos/`, `web/`).
- **Ask:** "Where can buyers pay: the App Store, Google Play, your website, resellers? For each,
  who handles refunds?" Recommend "store" for app-store purchases and "company" for website
  purchases; a merchant of record refunds under its own policy.

### facts.sales.refund_rule
- **Means:** the general refund rule: the stance, the window, what it covers and its
  conditions.
- **Type:** record (stance: enum [money-back-window, case-by-case, no-refunds-except-law],
  window_days, window_start: enum [purchase, delivery, first-payment], covers: list of enum
  [first-purchase, renewals, one-time-purchases, add-ons], conditions: list of string,
  discretionary: bool, law_prevails: bool)
- **Look:** existing refund or terms pages; refund endpoints and their time checks (Stripe
  `refunds.create` guarded by a purchase-date check, admin refund tools); usage counters that
  gate a refund.
- **Ask:** "Do you give refunds? If so, within how many days of purchase, for the first
  purchase only or for renewals too, and on what conditions?" Recommend what an existing refund page says; with none, a 14- or 30-day
  window on the first purchase (the most common windows in the samples) and a line that
  mandatory consumer law prevails.

### facts.sales.refund_exclusions
- **Means:** purchases and cases that are never refunded, including refusals for abuse,
  repeat requests, chargebacks or account termination.
- **Type:** list of (item or case, reason)
- **Look:** consumable in-app products and credits, gift-card or code products, lifetime
  plans, chargeback webhooks (`charge.dispute.created`) that lock accounts, refund-count
  checks.
- **Ask:** "Are any purchases or cases never refunded (credits, gift cards, renewals, used
  items, after a chargeback, after a ban)?" Recommend the consumables and gift cards found in
  the product list, plus "no refund after a chargeback is opened" when disputes are handled.

### facts.sales.refund_request
- **Means:** how a buyer asks for a refund: channel, steps, what to include, and whether the
  decision is automatic or manual.
- **Type:** record (channel: enum [email, support-ticket, chat, account-button, cancel-flow,
  returns-portal, contact-form, help-site, mail-in], contact, steps, required_info: list,
  decision: enum [manual, automatic])
- **Look:** support email in store metadata and `mailto:` links, in-app support or chat SDKs
  (Intercom, Zendesk, Crisp), refund buttons or cancel flows in account screens.
- **Ask:** "How do buyers ask you for a refund, and what should they include?" Recommend
  the support email with the account email and order or receipt number.

### facts.sales.refund_processing
- **Means:** how an approved refund is paid and what follows it.
- **Type:** record (method: enum [original-payment-method, store-credit, wallet],
  typical_days, fees_deducted: bool, access_after_refund: enum [ends, kept-to-period-end],
  data_kept: bool)
- **Look:** payment provider refund calls, entitlement revocation on refund webhooks
  (`charge.refunded`, RevenueCat `CANCELLATION` with refund reason), store-credit code.
- **Ask:** "When you refund, where does the money go, how long does it take, and does access
  end at once?" Recommend "original payment method, 5–10 business days, access ends".

### facts.sales.partial_refunds
- **Means:** whether partial or pro-rated refunds are given for unused time or on plan changes.
- **Type:** enum [none, prorated, discretionary]
- **Look:** proration settings in the billing provider (Stripe `proration_behavior`), plan
  change and downgrade code.
- **Ask:** "Do you refund the unused part of a period, or on downgrades?" Recommend "none",
  which is what the samples that address it most often state.

### facts.sales.return_rules
- **Means:** rules for returning physical goods.
- **Type:** record (window_days, window_start: enum [delivery, purchase], condition,
  return_shipping_payer: enum [seller, buyer, seller-if-at-fault], label_provided: bool,
  in_store_returns: bool, exchanges: bool, damaged_items_route, order_cancellation: bool)
- **Look:** return-label and returns-portal integrations (Loop, Narvar, Shopify returns),
  shipping settings, store-location data.
- **Ask:** "For physical goods: how many days to return, in what condition, who pays return
  shipping, and how are damaged or wrong items handled?" Recommend 30 days from delivery,
  unused in original packaging, and a free replacement or refund for damaged or wrong items.

### facts.sales.gifting
- **Means:** whether buyers can purchase items as gifts for someone else.
- **Type:** bool
- **Look:** gift options at checkout, gift-purchase or gift-code products, gift-message fields.
- **Ask:** "Can buyers buy your product as a gift for someone else?" Recommend what the
  checkout shows.

## Key map

| Proposed | Final | Note |
| --- | --- | --- |
| `facts.sales.offer_type` | `facts.sales.offer_type` |  |
| `facts.sales.subscription` | `facts.sales.subscription` | `trial` moved to `facts.sales.free_trial` |
| `facts.sales.return_address` | `facts.sales.return_address` |  |
| `facts.sales.purchase_channels` | `facts.sales.purchase_channels` |  |
| `facts.sales.refund_rule` | `facts.sales.refund_rule` |  |
| `facts.sales.refund_exclusions` | `facts.sales.refund_exclusions` |  |
| `facts.sales.refund_request` | `facts.sales.refund_request` |  |
| `facts.sales.refund_processing` | `facts.sales.refund_processing` |  |
| `facts.sales.partial_refunds` | `facts.sales.partial_refunds` | now a record; adds `on_discontinuation` |
| `facts.sales.return_rules` | `facts.sales.return_rules` |  |
| `facts.sales.gifting` | `facts.sales.gifts` |  |

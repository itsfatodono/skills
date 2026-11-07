# subscription-terms: proposed fact keys

Merged into `helpers/facts-schema.md` on 2026-10-26; see the key map below.

Keys `skeletons/subscription-terms.md` names that `helpers/facts-schema.md` does not define yet, in its
entry format, under their intended shared names. Added 2026-10-26. `facts.sales.subscription`,
`facts.sales.payment_methods` and `facts.sales.payment_provider` are the shared names the `tr`
pilot proposed (`regions/tr/facts.md`); their meaning here matches it, and
`facts.sales.subscription` adds fields.

Keys reused from `helpers/facts-schema.md`: `facts.company.legal_name`, `facts.company.contact_email`,
`facts.product.name`, `facts.product.services_in_scope`, `facts.product.has_accounts`,
`facts.product.min_age`, `facts.data.retention`.

### facts.sales.subscription_terms_placement
- **Means:** where the subscription terms are published: their own page, or a section of the terms of service.
- **Type:** enum [separate-page, tos-section]
- **Look:** existing legal docs (a `subscription`, `terms-of-sale` or `paid-terms` page, or a subscription heading inside the ToS); links in the paywall and settings screens.
- **Ask:** "Should the subscription terms be their own page, or a section of your terms of service?" Recommend `tos-section` when one product sells one or two plans; `separate-page` when there are several products, plan types or purchase channels.

### facts.sales.subscription
- **Means:** the recurring plans: billing periods, whether they renew automatically, whether a reminder goes out before renewal, how the buyer cancels on each channel, the cancellation deadline, and what happens after cancelling.
- **Type:** record (periods: list, auto_renews: bool, renewal_notice: bool, cancel_path: list of (channel, path), cancel_deadline, after_cancel: enum [access-to-period-end, immediate-end], data_after_end) or none
- **Look:** subscription SDKs and product configs (RevenueCat offerings, StoreKit product ids, Play Billing base plans, Stripe Billing prices); renewal-reminder emails or jobs; "manage subscription" and cancel screens; downgrade-to-free code.
- **Ask:** "Which billing periods do you sell, do they renew automatically, and how does a buyer cancel on each platform?" Recommend what the product configs show; "access to the end of the paid period" after cancelling, and the stores' own cancel paths for store purchases.
- **Proposed shared key:** same name as `facts.tr.subscription`'s proposal; this definition adds `cancel_deadline`, `after_cancel` and `data_after_end`.

### facts.sales.plans
- **Means:** the paid plans and what each adds over the free tier, including lifetime plans, add-ons, credits or quotas, and where the price is shown.
- **Type:** list of (name, period [week, month, year, lifetime, other], includes, price_shown_at)
- **Look:** paywall screens and their strings, entitlement checks in code, RevenueCat entitlements and offerings, store product metadata, the pricing page.
- **Ask:** "Which paid plans do you offer, and what does each unlock?" Recommend the plans and entitlements found; price shown "in the app and the store before purchase".

### facts.sales.billing_channels
- **Means:** who bills the buyer: Apple, Google, the company directly (web checkout), another platform, a partner bundle, or an employer or organisation that pays for access.
- **Type:** list of enum [app-store, google-play, web-direct, other-platform, partner-bundle, organisation]
- **Look:** StoreKit and Play Billing code, RevenueCat platforms, Stripe/Paddle/Lemon Squeezy checkout, promo or partner entitlement grants, team or organisation billing.
- **Ask:** "Where can people pay for a subscription: App Store, Google Play, your website, or elsewhere?" Recommend every channel the code integrates.

### facts.sales.payment_methods
- **Means:** the payment methods offered at checkout.
- **Type:** list of enum [card, card-instalments, bank-transfer, cash-on-delivery, wallet, gift-card, other]
- **Look:** payment SDK and checkout configuration (Stripe, Apple Pay, Google Pay, PayPal, iyzico), card-updater settings.
- **Ask:** "Which payment methods can buyers use on your own checkout?" Recommend the methods configured; for store-only products, "handled by the store".
- **Proposed shared key:** same as `facts.tr.payment_methods`.

### facts.sales.payment_provider
- **Means:** the payment institution that processes payments the company takes directly, and whether the company stores card data itself.
- **Type:** record (name, stores_card_data: bool, three_d_secure: bool)
- **Look:** payment SDKs and API clients; card-vault or tokenisation code.
- **Ask:** "Which payment provider processes your direct payments, and do you store card numbers yourselves?" Recommend "does not store card data" when only a provider's hosted form or token is used.
- **Proposed shared key:** same as `facts.tr.payment_provider`.

### facts.sales.taxes
- **Means:** whether shown prices include tax, and who collects it.
- **Type:** enum [included, added-at-checkout, collected-by-store, mixed]
- **Look:** store pricing (stores show tax-inclusive prices in most countries and remit tax); Stripe Tax or tax settings on the web checkout; price strings with "+ tax".
- **Ask:** "Do your prices include tax?" Recommend `collected-by-store` for store-only products and `mixed` when web checkout adds tax.

### facts.sales.failed_payment
- **Means:** what happens when a renewal charge fails: retries, grace period, and the effect on access.
- **Type:** record (retries: bool, grace_days: number, effect: enum [suspend, downgrade-to-free, cancel], backup_method: bool)
- **Look:** billing-retry and grace-period settings (App Store billing grace period, Play grace period and account hold, Stripe Smart Retries and dunning), entitlement handling for `BILLING_ISSUE` events.
- **Ask:** "If a renewal payment fails, do you retry, and does the user keep access for a while?" Recommend the store and provider settings found; otherwise "access ends until payment succeeds".

### facts.sales.free_trial
- **Means:** the free trial: length, whether a payment method is needed, whether it converts to paid automatically, who is eligible, and any reminder before it ends.
- **Type:** record (length, payment_method_required: bool, converts_automatically: bool, eligibility, reminder: bool) or none
- **Look:** introductory-offer configuration (StoreKit free trial, Play free-trial phase, Stripe `trial_period_days`), trial-ending notifications.
- **Ask:** "Do you offer a free trial? How long, and does it turn into a paid plan automatically?" Recommend what the product configs show; eligibility "new subscribers only, once".

### facts.sales.promotions
- **Means:** discounts beyond the trial: introductory prices, promo codes, referral credits, win-back offers, with eligibility and what the price becomes afterwards.
- **Type:** list of (kind [intro-price, discount, promo-code, referral, win-back], eligibility, price_after) or none
- **Look:** StoreKit promotional and offer codes, Play offers, Stripe coupons and promotion codes, referral features.
- **Ask:** "Do you run discounts, promo codes or referral offers?" Recommend what the configs show.

### facts.sales.change_notice
- **Means:** how subscribers are told before a price, plan or terms change takes effect, and from when it applies.
- **Type:** record (days: number, channels: list of enum [email, in-app, store, posting], applies_from: enum [next-renewal, immediately])
- **Look:** existing legal docs; store price-increase consent flows (Apple and Google ask existing subscribers to accept increases); email or in-app announcement mechanisms.
- **Ask:** "How far in advance will you tell subscribers about a price change, and how?" Recommend 30 days by email and in-app, effective from the next renewal.

### facts.sales.refund_policy
- **Means:** the company's refund rule for subscription fees: none, a window after first purchase, pro-rata, or case by case; and where store buyers ask for refunds.
- **Type:** record (default: enum [none, window, pro-rata, discretionary], window_days: number, exceptions: list, store_route: bool)
- **Look:** existing legal docs, refund handling in the support tooling or payment provider (Stripe refunds), store refund notifications.
- **Ask:** "Do you refund subscription fees, and when?" Recommend "no refunds for partial periods, except where the law requires; store purchases are refunded by the store".

### facts.sales.one_time_purchases
- **Means:** non-recurring purchases sold under the same terms: consumables, virtual currency, credits, rentals, lifetime unlocks.
- **Type:** list of (name, kind [consumable, credits, rental, lifetime, other], refundable: bool, expiry) or none
- **Look:** non-consumable and consumable product ids in StoreKit, Play in-app products, RevenueCat non-subscription products, credit balances in code.
- **Ask:** "Do you sell anything that is not a subscription (credits, lifetime access, items)?" Recommend what the product configs show.

### facts.sales.plan_changes
- **Means:** how upgrades, downgrades and switches between plans work: timing and proration.
- **Type:** record (upgrade: enum [immediate-prorated, next-renewal], downgrade: enum [period-end, immediate]) or none
- **Look:** subscription groups and upgrade levels (StoreKit), Play replacement modes, Stripe proration settings.
- **Ask:** "Can subscribers switch plans? When does an upgrade or downgrade take effect?" Recommend the store defaults: upgrades immediately with proration, downgrades at the end of the period.

### facts.sales.shared_plans
- **Means:** family, household, team or group plans: how many members, who pays, who can cancel.
- **Type:** record (kind [family, household, team, group], max_members: number, payer_controls_cancel: bool) or none
- **Look:** Family Sharing flag on store products, team or seat models, invite flows.
- **Ask:** "Can one subscription cover several people? Who pays and who can cancel?" Recommend what the code shows.

### facts.sales.gifts
- **Means:** gift subscriptions, gift cards or redemption codes: whether they turn into renewing subscriptions, refunds, expiry.
- **Type:** record (kind [gift-subscription, gift-card, redemption-code], converts_to_renewal: bool, refundable: bool, expiry) or none
- **Look:** offer or redemption code flows, gift purchase pages, voucher models.
- **Ask:** "Do you sell gift subscriptions or redemption codes?" Recommend what the code shows.

### facts.sales.paid_feature_limits
- **Means:** limits that apply to the paid features themselves: devices, simultaneous streams, household-only use, countries, usage quotas, storage periods.
- **Type:** list of (limit, value) or none
- **Look:** device-count or concurrency checks, quota counters, region locks, storage-retention settings tied to entitlements.
- **Ask:** "Do paid features have limits (devices, usage quotas, countries)?" Recommend the limits found in code.

### facts.sales.pause
- **Means:** whether subscribers can pause instead of cancelling, for how long and how often.
- **Type:** record (max_length, per_period_limit) or none
- **Look:** Play subscription pause setting, pause flows in the account settings, Stripe `pause_collection`.
- **Ask:** "Can subscribers pause their subscription?" Recommend what the store and provider settings show.

## Key map

| Proposed | Final | Note |
| --- | --- | --- |
| `facts.sales.subscription_terms_placement` | `facts.sales.subscription_terms_placement` |  |
| `facts.sales.subscription` | `facts.sales.subscription` |  |
| `facts.sales.plans` | `facts.sales.plans` |  |
| `facts.sales.billing_channels` | `facts.sales.purchase_channels` |  |
| `facts.sales.payment_methods` | `facts.sales.payment_methods` |  |
| `facts.sales.payment_provider` | `facts.sales.payment_provider` |  |
| `facts.sales.taxes` | `facts.sales.taxes` |  |
| `facts.sales.failed_payment` | `facts.sales.failed_payment` |  |
| `facts.sales.free_trial` | `facts.sales.free_trial` |  |
| `facts.sales.promotions` | `facts.sales.promotions` |  |
| `facts.sales.change_notice` | `facts.company.change_notice` | one entry per kind of change (`documents`, `prices`) |
| `facts.sales.refund_policy` | `facts.sales.refund_rule` | `pro-rata` moved to `facts.sales.partial_refunds`; `store_route` to `refunds_by` in `facts.sales.purchase_channels` |
| `facts.sales.one_time_purchases` | `facts.sales.one_time_purchases` |  |
| `facts.sales.plan_changes` | `facts.sales.plan_changes` |  |
| `facts.sales.shared_plans` | `facts.sales.shared_plans` |  |
| `facts.sales.gifts` | `facts.sales.gifts` |  |
| `facts.sales.paid_feature_limits` | `facts.sales.paid_feature_limits` |  |
| `facts.sales.pause` | `facts.sales.pause` |  |

---
doc_id: subscription-terms
title: Subscription Terms
kind: document
family: commerce
sample_languages: [en]
sample_count: 30
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** Tells subscribers how paid plans are billed and renewed, how trials and offers
  convert, how prices change, and how to cancel and get refunds, on every channel they can buy
  through.
- **Shape:**
  - Placement splits: 19/30 publish the terms as a part of the terms of service, 11/30 as a
    separate page. `facts.sales.subscription_terms_placement` decides it. Separate pages are
    more common at large companies (6/10) than at mid (2/10) or small ones (3/10).
  - As a ToS part: 13/19 sit in the first third of the ToS, right after accounts or
    registration; 8/19 spread the topics over several non-adjacent sections. Write one
    contiguous part.
  - As a separate page: 7/11 say they supplement, or are incorporated into, the terms of
    service; 3/11 say they win on conflict.
  - Length: median about 1,200 words (185–23,000); ToS parts median 1,050, separate pages
    median 2,100.
  - 2/30 open with a key-points box (auto-renewal, how to cancel, no refunds); 1/30 is itself a
    plain-language summary that defers to the ToS; 2/30 have a table of contents; 3/30 are
    written mostly as bullet lists.
  - Purchase channels: 19/30 cover both store and direct billing, 5/30 store billing only,
    6/30 direct billing only. Most sections split their rules by channel.
- **Register:** 30/30 address the reader as "you". 13/30 plain consumer style with short
  sentences; 17/30 formal contract style with defined terms in quotes ("Subscription
  Period", "Payment Method"). 11/30 put at least one key rule (no refunds, trial conversion) in
  capitals.
- **Recurring elements:**
  - "Last updated" or "Effective" date: 9/11 separate pages (ToS parts carry the ToS date).
  - Apple and Google named by brand: 20/30.
  - A help-article link for cancelling: 10/30.
  - A support email offered as a cancellation or refund channel: 7/30.
  - A fixed cut-off before renewal ("at least 24 hours before the end of the period"),
    repeated in renewal, trial and cancellation text: 10/30.
- **Commonly omitted:** actual prices (prices are "shown at purchase"); a renewal reminder
  before charging (28/30 promise none); a fixed notice period for price changes (20/26 give
  none); named payment processors (26/30); plan upgrade and downgrade rules (24/30).

## Sections

Region-neutral. What one law requires (statutory withdrawal or cooling-off rights, state or
country cancellation rules) is in the region's block, `regions/<code>/subscription-terms.md`,
written under the document's regional part (`formats/region-format.md`).

### scope: Scope and relation to other terms

- **Covers:** which products, plans and purchase types the terms cover, who provides them, how
  they relate to the terms of service, who may buy, and where to ask questions.
- **Prevalence:** 14/30 (47%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.product.services_in_scope`, `facts.sales.subscription_terms_placement`, `facts.product.min_age`, `facts.company.contact_email`
- **Patterns:**
  - 10/14 are separate pages; a ToS part usually starts straight with the rules.
  - 7/14 say the terms supplement or are incorporated into the ToS, which governs disputes
    and liability; 3/14 add that these terms win on conflict.
  - 4/14 treat buying or using the paid tier as acceptance.
  - 3/14 set a minimum age to buy (the age of majority) and 3/14 name the providing entity.
  - Separate pages only: 4/30 end with general clauses (electronic notices, severability,
    entire agreement, precedence of translations), and 4/30 end with a support contact.
- **Quote:** "To the extent there is a conflict between these Cam Plus Terms and the Standard Terms, these Cam Plus Terms will govern such conflict." (s11)
- **Commonly omitted:** a definitions block (scope uses inline defined terms); governing law
  (left to the ToS).

### plans: Plans and what they include

- **Covers:** the paid plans and billing periods, what they add over the free tier, and where
  the price is shown.
- **Prevalence:** 21/30 (70%), common
- **Applies when:** always
- **Facts:** `facts.sales.plans`, `facts.sales.subscription`
- **Patterns:**
  - 7/21 open with the free/paid split: some features need a paid subscription.
  - Plans are rarely listed: 6/21 send the reader to the app, store or pricing page for plans
    and prices; 4/21 list what the plan includes.
  - 4/21 cover a lifetime plan, defined as the life of the product, not of the buyer.
  - 4/21 cover add-ons, perks, credits or quotas that come with a plan, and that unused
    allowances do not roll over.
  - 3/21 cover special plan types (per device, student or education, pre-paid
    non-renewing).
- **Quote:** "We provide access to certain features in our Products on a paid basis (each, a “Paid Offering”)." (s29)
- **Commonly omitted:** prices in the text; a feature comparison table.

### service-terms: Paid-feature terms of use

- **Covers:** rules that apply to the paid features themselves: personal use, device or stream
  limits, household-only sharing, countries, quotas, what the paid tier stores.
- **Prevalence:** 5/30 (17%), rare
- **Applies when:** `facts.sales.paid_feature_limits != none`
- **Facts:** `facts.sales.paid_feature_limits`
- **Patterns:**
  - 4/5 grant a personal, non-commercial licence for the subscription's duration.
  - 3/5 state device, simultaneous-stream or household limits; 2/5 restrict use to the
    country of sign-up.
  - 2/5 say which ads the paid tier removes and which it does not.
- **Quote:** "The Products and any content accessed through the Products are for your personal, non-commercial use only and may not be shared with anyone outside of your household." (s10)
- **Commonly omitted:** general licence and conduct rules, which stay in the ToS.

### payment: Payment and billing

- **Covers:** accepted payment methods, the authorisation to charge them, when charges happen,
  keeping payment details current, and how billing errors and chargebacks are handled.
- **Prevalence:** 26/30 (87%), core
- **Applies when:** always
- **Facts:** `facts.sales.purchase_channels`, `facts.sales.payment_methods`, `facts.sales.payment_provider`
- **Patterns:**
  - Nearly all state an authorisation to charge the payment method on file for the first
    period and each renewal.
  - 8/26 list method types (cards, wallets, PayPal, bank transfer); 4/26 name the payment
    processor; 4/26 fix the currency.
  - 7/26 let the company update card details from the card network or processor
    (card-updater), and 5/26 say where the user updates them (account page, or the store
    account for store buyers).
  - 4/26 explain pre-authorisation holds at sign-up.
  - Store-only products say the store takes payment and the company never sees payment data.
  - 5/30 add billing disputes: a deadline to report a wrong charge (60 days in two), deemed
    acceptance after it, and a duty to raise issues before a chargeback.
- **Quote:** "You authorize us to store your payment method(s) and to automatically charge your payment method(s) every month until you cancel." (s19)
- **Commonly omitted:** set-off and retention clauses; the invoice due date (only business
  plans paid by invoice).

### auto-renewal: Automatic renewal

- **Covers:** that the subscription renews until cancelled, the renewal period and price, and
  the cut-off for cancelling before a renewal charge.
- **Prevalence:** 29/30 (97%), core
- **Applies when:** `facts.sales.subscription.auto_renews == true`
- **Facts:** `facts.sales.subscription`
- **Patterns:**
  - Opens with one plain rule: the subscription renews automatically until cancelled.
  - Renewal price: 7/29 at the then-current price, 4/29 at the same price and plan; the rest
    do not say.
  - 8/29 list the billing periods (weekly, monthly, yearly).
  - 10/29 give a fixed cut-off in hours before the period ends; the rest say "before the
    renewal date".
  - 4/29 reproduce the app-store disclosure checklist (charged at confirmation, renews unless
    turned off at least 24 hours before, charged within 24 hours before renewal, managed in
    account settings).
  - Reminders: 2/29 promise one before renewal (annual plans); 1/29 says plainly that no
    reminder is sent.
- **Quote:** "Any paid subscriptions will renew automatically unless you cancel." (s03)
- **Commonly omitted:** the renewal reminder; what happens to promotional prices at renewal
  (covered under `promotions`).

### taxes: Taxes

- **Covers:** whether prices include tax, the user's duty to pay it, and tax collected by the
  store.
- **Prevalence:** 19/30 (63%), common
- **Applies when:** always
- **Facts:** `facts.sales.taxes`, `facts.sales.purchase_channels`
- **Patterns:**
  - 6/19 give taxes their own heading; the rest fold "plus applicable taxes" into the fee or
    renewal clause.
  - 8/19 say fees exclude tax and the user pays it; 2/19 say the store collects it.
  - 3/19 add that bank, card or currency-conversion fees are the user's.
- **Quote:** "Subscription fees are exclusive of all applicable taxes, levies, or duties imposed by taxing authorities." (s05)
- **Commonly omitted:** tax rates; tax changes mid-term.

### failed-payments: Failed and late payments

- **Covers:** what happens when a charge fails: retries, backup methods, suspension or
  downgrade, liability for unpaid amounts.
- **Prevalence:** 18/30 (60%), common
- **Applies when:** always
- **Facts:** `facts.sales.failed_payment`
- **Patterns:**
  - 10/18 let the company suspend or end access when payment fails.
  - 4/18 keep the user liable for uncollected amounts; 4/18 add collection costs.
  - 3/18 charge a backup payment method on file; 3/18 describe retries and restored access
    once payment succeeds.
  - Store-only products send failed payments to the store.
- **Quote:** "If your payment method fails or your account is past due, we may suspend or terminate your access to the Services." (s05)
- **Commonly omitted:** a grace period length; late-payment interest (1/30).

### free-trial: Free trials

- **Covers:** who gets a trial, whether a payment method is needed, conversion to a paid plan,
  and how to cancel before it converts.
- **Prevalence:** 22/30 (73%), common
- **Applies when:** `facts.sales.free_trial != none`
- **Facts:** `facts.sales.free_trial`, `facts.sales.subscription`
- **Patterns:**
  - 18/22 state automatic conversion to a paid plan unless cancelled before the trial ends;
    1/22 has an opt-in trial that ends without charging.
  - 11/22 require a payment method to start the trial, often with "you will not be charged
    during the trial".
  - 8/22 limit trials to new subscribers, once per person or payment method.
  - 7/22 leave the trial length to the sign-up screen or offer.
  - 4/22 give a cut-off before the trial ends; 2/22 explain a pre-authorisation hold.
  - 11/22 offer the trial at the company's discretion and reserve the right to change it.
- **Quote:** "To avoid any charges, you must cancel your subscription before the end of the free period granted and notified to you while subscribing." (s28)
- **Commonly omitted:** a reminder before the trial ends (1/22).

### third-party-billing: Purchases through app stores and other third parties

- **Covers:** purchases billed by Apple, Google, another platform, a partner bundle or an
  organisation: whose terms apply and who handles billing, cancellation and refunds.
- **Prevalence:** 25/30 (83%), core
- **Applies when:** `facts.sales.purchase_channels` contains a channel other than `web-direct`
- **Facts:** `facts.sales.purchase_channels`
- **Patterns:**
  - Placement splits: about half give the store rules their own section; the rest fold a
    store sentence into cancellation and refunds.
  - Store buyers cancel and request refunds through the store; the company's text points to
    the store's settings or help pages.
  - 9/25 say the store's terms govern the purchase; 6/25 say the company cannot start, cancel
    or refund store subscriptions.
  - 6/25 define one term for the stores ("App Store", "External Service").
  - 6/25 cover access through a partner bundle, reseller or employer, under that party's
    terms.
  - 2/25 say what account data goes to the store when a user asks it for a refund.
  - 3/25 name Apple only.
- **Quote:** "Copilot does not have the ability to manage your subscription on your behalf, including initiating, canceling, or refunding your subscriptions." (s18)
- **Commonly omitted:** a warning about duplicate charges when switching from store to direct
  billing (1/30).

### changes: Changes to prices, plans and these terms

- **Covers:** the right to change prices, plans, included features or these terms, the notice
  given, and the user's remedy.
- **Prevalence:** 26/30 (87%), core
- **Applies when:** always
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - Most pair a reservation to change prices with a promise of notice and a chance to cancel
    before the new price applies.
  - Notice period: 6/26 fix one (30 days or one month in four); the rest say "advance" or
    "reasonable" notice, or none.
  - 8/26 apply a new price only from the next renewal; 6/26 name the notice channel (email,
    in-app).
  - 6/26 treat continued use after the change as acceptance.
  - 5/26 also cover changes to the terms themselves (separate pages).
  - 11/30 reserve the right to add, change or remove paid features or content; 3/30 add that
    purchases do not depend on future features.
- **Quote:** "We will notify you at least one month before any price changes or changes to your subscription plan will become effective." (s04)
- **Commonly omitted:** price protection when prices fall (3/30 deny it explicitly).

### promotions: Promotional and introductory offers

- **Covers:** discounts, introductory prices, promo and referral codes: eligibility, extra
  offer terms, and the price after the offer ends.
- **Prevalence:** 13/30 (43%), common
- **Applies when:** `facts.sales.promotions != none`
- **Facts:** `facts.sales.promotions`
- **Patterns:**
  - 7/13 limit offers to new customers, one per person, not combinable.
  - 6/13 say the price steps up to the full rate after the offer period.
  - 5/13 defer conditions to the offer screen ("Offer Terms"); 5/13 reserve the right to
    change or withdraw offers.
  - 1/13 lists promo-code conditions as an (a)–(g) list.
- **Quote:** "Unless stated otherwise in the Offer Terms, Promotional Offers are only for new customers who have not previously subscribed to Calm Premium or enrolled in a Promotional Offer." (s08)
- **Commonly omitted:** referral programme rules (1/30).

### one-time-purchases: One-time and consumable purchases

- **Covers:** non-recurring purchases sold under the same terms: virtual items, credits,
  rentals, passes. Lifetime plans are in `plans`.
- **Prevalence:** 7/30 (23%), rare
- **Applies when:** `facts.sales.one_time_purchases != none`
- **Facts:** `facts.sales.one_time_purchases`
- **Patterns:**
  - 4/7 make them final and non-refundable.
  - 3/7 call them a licence with no cash value, lost when the account ends.
  - 2/7 give credits an expiry date.
- **Quote:** "A One-time Purchase does not renew and is not charged again." (s24)
- **Commonly omitted:** transfer between accounts (always barred when mentioned).

### plan-changes: Upgrades, downgrades and plan switches

- **Covers:** switching plans: when the change takes effect and how prepaid fees are
  credited.
- **Prevalence:** 6/30 (20%), rare
- **Applies when:** `facts.sales.plan_changes != none`
- **Facts:** `facts.sales.plan_changes`
- **Patterns:**
  - Upgrades take effect at once with the difference charged pro rata; downgrades at the end
    of the period (3/6).
  - 2/6 credit unused prepaid fees toward the new plan, at the company's discretion.
- **Quote:** "If during the Access Period of your Current Product you elect to downgrade to a different Subscription Product (\"Downgrade Product\"), you will retain access to the Current Product for the remainder of the Access Period." (s22)
- **Commonly omitted:** store-specific upgrade rules.

### cancellation: Cancellation

- **Covers:** how and where to cancel on each channel, the deadline, when cancellation takes
  effect, what happens to the account and data afterwards, and when the company may end a
  subscription.
- **Prevalence:** 30/30 (100%), core
- **Applies when:** always
- **Facts:** `facts.sales.subscription`, `facts.sales.purchase_channels`, `facts.product.has_accounts`, `facts.data.retention`
- **Patterns:**
  - 24/30 keep access until the end of the paid period; the cancellation stops future
    charges only.
  - 13/30 give the cancel route per channel (account settings for direct buyers, store
    settings for store buyers); 7/30 spell out the click path; 10/30 link a help article.
  - 7/30 warn that deleting the app or the account does not cancel the subscription.
  - 7/30 say what happens afterwards: back to the free tier, data kept or deleted.
  - 10/30 add the company's right to suspend or end a subscription for breach or by
    discontinuing it; 4/30 refund the unused part in that case.
  - 2/30 charge an early-termination fee on annual plans billed monthly.
- **Quote:** "Deleting your Telegram account or removing the Telegram application from your device does not cancel your subscription." (s02)
- **Commonly omitted:** cancellation by phone or post; pausing (see `pause`).

### refunds: Refunds

- **Covers:** the refund rule for subscription fees, partial periods, discretionary refunds,
  and where store buyers ask for refunds.
- **Prevalence:** 27/30 (90%), core
- **Applies when:** always
- **Facts:** `facts.sales.refund_rule`, `facts.sales.partial_refunds`, `facts.sales.purchase_channels`
- **Patterns:**
  - 22/27 state no refunds and no credits for partial periods; 10/27 carve out what the law
    requires, without naming it.
  - 12/27 send store buyers to the store's refund process.
  - 5/27 allow discretionary refunds or credits that set no precedent.
  - 4/27 offer a full refund within a short window after the first purchase.
  - Placement splits: about half fold refunds into the cancellation section.
- **Quote:** "Payments are nonrefundable and there are no refunds or credits for partially used subscription periods." (s04)
- **Commonly omitted:** refund timing and method (2/30 say refunds go back to the original
  payment method).

### shared-plans: Family and shared plans

- **Covers:** plans that cover several people: members, who pays, who controls and cancels.
- **Prevalence:** 8/30 (27%), rare
- **Applies when:** `facts.sales.shared_plans != none`
- **Facts:** `facts.sales.shared_plans`
- **Patterns:**
  - 4/8 make the paying holder responsible for members and the only one who can cancel.
  - Members lose access when the holder cancels; some plans require one household.
  - 2/8 cover team seats added mid-term with prorated charges.
- **Quote:** "Sub-Account Holders are not eligible to manage or cancel Family Subscriptions." (s13)
- **Commonly omitted:** the maximum number of members (given in 2/8).

### gifts: Gift subscriptions and gift cards

- **Covers:** buying and redeeming gift subscriptions, gift cards and codes, and what happens
  when they end.
- **Prevalence:** 6/30 (20%), rare
- **Applies when:** `facts.sales.gifts != none`
- **Facts:** `facts.sales.gifts`
- **Patterns:**
  - 3/6 turn a redeemed gift into a renewing subscription once a payment method is added.
  - 3/6 bar cash-out and refunds after redemption or the gift start date.
- **Quote:** "No refunds are available after the gift start date." (s25)
- **Commonly omitted:** gift card validity periods (1/6).

### pause: Pausing a subscription

- **Covers:** pausing instead of cancelling: how long, how often, access during the pause, and
  reactivation.
- **Prevalence:** 1/30 (3%), rare
- **Applies when:** `facts.sales.pause != none`
- **Facts:** `facts.sales.pause`
- **Patterns:**
  - The one sample walks through the pause in order: maximum length, once per billing cycle,
    no paid access while paused, automatic reactivation at the renewal price, cancelling while
    paused.
- **Quote:** "Your subscription will be reactivated automatically after the specified pause duration at the price at which it would have renewed prior to the pause, and you authorize your form of payment to be charged for your subscription on a recurring basis upon reactivation." (s25)
- **Commonly omitted:** everything else; the section is rare.

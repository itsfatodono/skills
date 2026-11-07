---
doc_id: refund-policy
title: Refund Policy
kind: document
family: commerce
sample_languages: [en]
sample_count: 25
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** Tells buyers whether and when they get their money back, how to ask, and who
  handles the refund when they paid through someone else (an app store, a reseller).
- **Shape:**
  - Short: median 500 words (range 41–2,559); 9/25 are under 250 words.
  - 12/25 a standalone page (one of them a hub linking separate policies per sales channel);
    11/25 a help-center article; 2/25 a part of a combined page (terms, or billing and refund).
  - 9/25 organise the whole page by purchase channel (app store, other store, website) rather
    than by topic.
  - 5/25 phrase the title or headings as the buyer's question ("Do you offer refunds?");
    5/25 number their sections; 2/25 use a table (refund windows per plan or per country).
  - 3/25 also carry billing terms (billing cycles, trials, price changes); that content
    belongs in the subscription terms, not here.
- **Register:** 22/25 "we/you"; 3/25 name the company in the third person. 19/25 plain
  support or brand voice with short sentences, some with exclamation marks or emoji (2/25);
  5/25 formal contract drafting with defined terms and numbered clauses; 1/25 terse
  troubleshooting steps. Hedging ("may",
  "generally", "at our discretion") is common in both.
- **Recurring elements:**
  - A visible "last updated" or effective date: 9/25.
  - A pointer to the terms of service or another governing document: 9/25.
  - Links to the app stores' own refund pages: 8/25.
  - A "changes to this policy" clause: 2/25.
- **Commonly omitted:** a visible date (16/25); a postal address (23/25); named laws (2/25
  cite one); chargebacks (21/25); refund timing and method (11/25 give neither); a changes
  clause (23/25); exact refund amounts or pro-rating rules (20/25).

## Sections

### scope: What this policy covers

- **Covers:** which products, purchases and buyers the policy applies to, and that the rules
  differ by plan or purchase channel.
- **Prevalence:** 16/25 (64%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.product.services_in_scope`,
  `facts.sales.offer_type`
- **Patterns:**
  - Opens the page: one or two sentences, no heading.
  - 7/16 say the rules or the route differ by plan, region or where the buyer paid, often as
    a lead-in to channel blocks.
  - 4/16 open with a satisfaction promise ("we want you to be happy") before any rule.
  - 4/16 list the products or plans covered; 3/16 say business buyers or plans are covered.
  - 2/16 (resellers and merchants of record) name who actually sells and refunds.
- **Quote:** "Refund eligibility depends on how you subscribed to the Fax App." (s20)
- **Commonly omitted:** customer types (consumers vs businesses); an effective date in the
  opening.

### eligibility: When you can get a refund

- **Covers:** the general rule: whether refunds are given, the window in days, what the window
  covers (first purchase, renewals, one-time purchases) and any conditions.
- **Prevalence:** 23/25 (92%), core
- **Applies when:** always
- **Facts:** `facts.sales.refund_rule`, `facts.sales.offer_type`, `facts.sales.subscription`
- **Patterns:**
  - 19/23 grant a window, most often 14 or 30 days (range: hours to 60 days), sometimes one
    per plan or billing period. It runs from purchase (digital) or from delivery (physical
    goods).
  - 4/23 state a blanket no-refund rule with exceptions only where the law or another
    agreement requires.
  - 4/23 limit the refund to the first purchase; renewals are not refunded.
  - 4/23 add a usage condition (not used, played under a set time, no core feature used).
  - 5/23 give separate rules per product type (subscriptions, one-time purchases, add-ons,
    pre-orders).
  - 4/23 frame it as a "no questions asked" money-back guarantee in one sentence.
  - 8/25 add a line that mandatory consumer law prevails over the policy, without naming the
    law in the root text.
  - 4/23 allow discretionary refunds outside the rule, case by case ("we may still look at
    it").
  - 1/23 gives the windows as a table per plan and billing period.
- **Quote:** "If you purchased Tower and changed your mind, let us know within 30 days and we'll be happy to refund you." (s21)
- **Commonly omitted:** the reason for the window; partial refunds within the window;
  whether a trial counts toward the window.

### physical-returns: Returning physical goods

- **Covers:** return window from delivery, item condition and packaging, who pays return
  shipping, return labels, in-store returns, exchanges, and damaged, faulty or wrong items.
- **Prevalence:** 4/25 (16%), rare
- **Applies when:** `facts.sales.offer_type` is `physical` or `mixed`
- **Facts:** `facts.sales.return_rules`, `facts.sales.return_address`
- **Patterns:**
  - 3/4 require the item unused, complete and in its original packaging.
  - 4/4 send damaged, faulty or wrong items to a separate route (warranty claim, customer
    service), before or instead of a refund.
  - 2/4 say who pays return shipping (flat fee by product type; no refund of shipping unless
    the seller was at fault).
  - 2/4 allow returns in their own stores; 2/4 offer exchanges.
  - 1/4 refuses returns outright for perishable goods and promises to "make it right" instead.
  - 1/4 refuses order cancellation because orders ship immediately.
- **Quote:** "You have 14 calendar days to return an item from the date you received it." (s04)
- **Commonly omitted:** restocking fees; return address when it is the main address.

### purchase-channels: Purchases through app stores and other sellers

- **Covers:** who decides and pays the refund depending on where the buyer paid: the app
  stores, other stores, resellers, retailers, partners, payment processors, or the company.
- **Prevalence:** 18/25 (72%), common
- **Applies when:** `facts.sales.purchase_channels` includes any channel the company does not
  refund itself
- **Facts:** `facts.sales.purchase_channels`
- **Patterns:**
  - 13/18 send App Store buyers to Apple: 5/13 give the steps, the rest link to Apple's page
    or only say Apple decides.
  - Google Play splits: 7/18 send the buyer to Google, 3/18 handle Google Play refunds
    themselves on request.
  - 7/18 cover resellers, retailers, partners or gift cards bought elsewhere: the seller's
    own policy applies and the company cannot refund.
  - One labelled block per channel (store name as the heading), with the same two-sentence
    template repeated.
  - 7/18 quote the store's usual window (often presented as a fact about the store, not a
    promise).
  - 2/18 explain which payment processor appears on the buyer's statement for website
    purchases.
  - 1/18 says it may share purchase-activity data with the store to help it decide refunds.
- **Quote:** "Subscriptions purchased through the Android app are processed and billed by Google Play." (s26)
- **Commonly omitted:** links to every store's refund page; what happens when the store
  refuses (2/18 say the company will not refund instead).

### cancellation: Cancelling a subscription

- **Covers:** how cancelling relates to a refund: access until the end of the period,
  cancelling is not a refund, a refund ends the subscription, trials, pro-rating and plan
  changes.
- **Prevalence:** 12/25 (48%), common
- **Applies when:** `facts.sales.subscription` is not none
- **Facts:** `facts.sales.subscription`, `facts.sales.free_trial`, `facts.sales.partial_refunds`, `facts.sales.plan_changes`
- **Patterns:**
  - 6/12 say access continues to the end of the paid period after cancelling.
  - 3/12 state that cancelling stops renewal but does not refund by itself.
  - 2/12 warn that a refund cancels the subscription and ends access at once.
  - 3/12 say uninstalling or deleting the app does not cancel.
  - 3/12 cover free trials (cancel before the trial ends; trial cancellation ends access at
    once).
  - Pro-rating: 2/12 refuse partial or pro-rated refunds; 1/12 pro-rates under rules that
    vary by country; 2/12 cover refunds on plan upgrades and downgrades.
  - 1/12 only links to a separate cancellation article.
- **Quote:** "Canceling your subscription will stop future billing but will not automatically issue a refund." (s22)
- **Commonly omitted:** the cancellation steps themselves (left to the store or a help
  article); renewal reminders.

### request: How to request a refund

- **Covers:** the channel and steps to ask for a refund or start a return, what to include,
  and how the decision is made.
- **Prevalence:** 21/25 (84%), core
- **Applies when:** always
- **Facts:** `facts.sales.refund_request`, `facts.company.contact_email`
- **Patterns:**
  - Channel: 11/21 email, a support ticket or chat; 5/21 a button or flow in the account,
    order page or returns portal (often inside the cancel flow); 3/21 a help site or contact
    form; 1/21 mail-in; 1/21 names no channel ("let us know").
  - 9/21 list what to include (account email or username, order or receipt number, reason);
    5/21 ask for the reason, sometimes framed as feedback rather than a condition.
  - Numbered steps with button names, often with screenshots, in help-center versions.
  - 2/21 say eligibility is decided automatically, 1/21 with a route to human review.
  - 7/25 end with a short contact block (support email, in-app chat).
  - 3/21 suggest contacting support first to fix the problem before refunding.
- **Quote:** "Please include a clear explanation why you are unhappy so we can see if there is anything we can do to improve." (s27)
- **Commonly omitted:** a response deadline; a postal address; identity checks (3/21 mention them).

### processing: How the refund is paid

- **Covers:** refund method, time until the money arrives, deductions, and what happens to
  access, licences or data after a refund.
- **Prevalence:** 14/25 (56%), common
- **Applies when:** always
- **Facts:** `facts.sales.refund_processing`
- **Patterns:**
  - 8/14 refund to the original payment method; 3/14 name a fallback (store credit or
    wallet, gift card for gift returns).
  - 11/14 give a time: a range of business days (5–10 most often), or "within N days of
    approval", often with "depending on your bank".
  - 4/14 say access ends after the refund; 1/14 adds a duty to delete licensed software;
    1/14 says progress or data is kept.
  - 1/14 deducts transaction fees from the refund.
- **Quote:** "All refunds are processed to the original payment method and can take up to 5-7 days to reflect depending on your financial institution." (s08)
- **Commonly omitted:** currency or exchange-rate differences; partial refunds of taxes.

### exclusions: When no refund is given

- **Covers:** purchases and cases never refunded: consumables and credits, gift cards,
  renewals, used or opened items, price drops, items bought elsewhere; refusal for abuse,
  repeat requests, chargebacks or account termination.
- **Prevalence:** 17/25 (68%), common
- **Applies when:** always
- **Facts:** `facts.sales.refund_exclusions`, `facts.sales.refund_rule`
- **Patterns:**
  - A bulleted list of excluded items or cases (10/17), often after a "we can't refund:"
    lead-in; 1/17 follows each case with a worked "Example:".
  - Typical items: in-app credits and consumables (5), gift cards and codes (4), used or
    opened goods (3), renewals (3), digital items once delivered (3), price drops and coupons
    (1).
  - 8/25 limit repeat refunds (once per account or product) or refuse when refunds are abused;
    2/8 list the grounds (terms violations, heavy use, prior chargebacks).
  - 4/25 address chargebacks: ask the buyer to contact the company first, or refuse a refund
    once a dispute is opened.
  - 2/25 refuse refunds when the account is terminated for breaking the terms.
- **Quote:** "If it appears to us that you are abusing refunds, we may stop offering them to you." (s23)
- **Commonly omitted:** why each exclusion exists; how the exclusion is shown at purchase
  (1/17 marks non-refundable items on the store page).

### gifts: Gift purchases

- **Covers:** returns and refunds of items bought as gifts: who may ask, what the recipient
  needs, and where the money goes.
- **Prevalence:** 3/25 (12%), rare
- **Applies when:** `facts.sales.gifts != none`
- **Facts:** `facts.sales.gifts`, `facts.sales.refund_processing`
- **Patterns:**
  - 2/3 refund the recipient in store credit or a gift card, not cash; 1/3 returns the money
    to the original purchaser.
  - 2/3 ask for the order or serial number, or the giver's name or email.
- **Quote:** "Funds used to purchase the gift will be returned to the original purchaser." (s23)
- **Commonly omitted:** gift returns for subscriptions.

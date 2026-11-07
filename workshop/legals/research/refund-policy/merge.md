# refund-policy: merged section list

## Section ids (fixed before saturation)

Meaning of each id. A row of a sample maps to every id whose content it clearly carries; the
id that the row mainly serves takes the row's format, the others take `embedded`. Formats:
`prose`, `list`, `table`; layout marks `pointer`, `embedded`.

| Id | Meaning |
|---|---|
| scope | What the policy covers: products, purchases, customer types (consumers, business plans), seller identity when it sells for others; an opening promise counts here |
| eligibility | The general rule: whether and when a refund is given (money-back window, "all sales final", conditions such as no use, refund grounds) |
| purchase-channels | Who handles the refund by where the buyer paid: app stores, partners, resellers, retailers, payment processors, direct purchases |
| request | How to ask for a refund or start a return: channel, steps, what to include |
| exclusions | Purchases or cases that are never refunded (consumables, credits, gift cards, used items, price drops) |
| processing | After approval: refund method, time to arrive, delays |
| cancellation | Cancelling a subscription and its effect: access until period end, refund ends the subscription, trial cancellation |
| partial-refunds | Pro-rating, partial refunds, refunds on plan changes or renewals |
| statutory-rights | Region-neutral line that mandatory consumer law prevails over the policy (the region-specific rights go to *Regional content*) |
| faulty-items | Defective, damaged, wrong or problem orders; warranty route |
| returns | Physical returns: item condition, packaging, return shipping and labels |
| exchanges | Swapping an item instead of a refund |
| gifts | Returns and refunds for gift recipients |
| order-cancellation | Cancelling an order before it ships |
| abuse-limits | Limits on repeat refunds; refusal for abuse or fraud |
| termination | No refund when the company suspends or terminates the account |
| after-refund | What happens to access, licences, data after a refund |
| goodwill | Discretionary refunds beyond the rule, case by case |
| chargebacks | Chargebacks and payment disputes |
| terms-link | Pointer to the terms or another governing document; the policy forms part of the terms |
| changes | Changes to the policy |
| contact | Contact or help block |
| payment-plans | Instalment plans |
| service-issues | Refunds or credits for outages and disrupted service |
| billing | Billing terms carried inside the refund page: billing cycles, auto-renewal, trials, payment methods, price and tax changes, invoices (added at s18) |
| store-data-sharing | Sharing purchase or usage data with an app store so it can decide a refund (added at s20) |
| misc | Single-sample blocks (linked third-party service contracts) |

Document-level layouts (never make a sample new): organised by purchase channel; FAQ
questions as headings; jump list or table of contents; troubleshooting template; country
subsections; effective date line.

## First batch (15 samples)

s01 s02 s03 s04 s06 s07 s08 s10 s11 s12 s13 s14 s15 s16 s17 (5 large, 5 mid, 5 small).
s05 (Strava) and s09 (Wanderlog) were invalid under rule 6.

| Id | Count | Formats | Samples |
|---|---|---|---|
| eligibility | 14/15 | prose, list, table, embedded | s01 s02 s03 s04 s06 s07 s08 s10 s11 s13 s14 s15 s16 s17 |
| request | 11/15 | prose, list, embedded | s02 s04 s06 s07 s08 s11 s12 s14 s15 s16 s17 |
| purchase-channels | 10/15 | prose, list, embedded | s01 s02 s03 s04 s06 s11 s12 s13 s14 s15 |
| scope | 9/15 | prose, list | s02 s04 s07 s08 s11 s12 s13 s14 s16 |
| exclusions | 7/15 | prose, list, embedded | s01 s04 s07 s08 s11 s13 s16 |
| processing | 7/15 | prose, list, embedded | s02 s04 s06 s08 s11 s14 s16 |
| cancellation | 5/15 | prose, embedded | s01 s11 s13 s14 s16 |
| terms-link | 5/15 | pointer, embedded | s01 s04 s10 s11 s16 |
| contact | 4/15 | prose, list, pointer | s03 s12 s13 s14 |
| faulty-items | 4/15 | prose, list | s04 s08 s16 s17 |
| statutory-rights | 3/15 | prose, embedded | s11 s13 s16 |
| partial-refunds | 3/15 | prose, table, embedded | s02 s11 s13 |
| abuse-limits | 3/15 | embedded | s02 s13 s16 |
| after-refund | 3/15 | embedded | s11 s14 s16 |
| termination | 2/15 | prose | s02 s10 |
| returns | 2/15 | prose, list | s04 s08 |
| gifts | 2/15 | prose | s04 s08 |
| goodwill | 2/15 | prose | s14 s16 |
| exchanges | 1/15 | prose | s04 |
| order-cancellation | 1/15 | prose | s08 |
| chargebacks | 1/15 | prose | s16 |
| changes | 1/15 | prose | s16 |
| payment-plans | 1/15 | prose | s06 |
| service-issues | 1/15 | embedded | s01 |
| misc | 1/15 | prose | s04 |

## Saturation

Judged in pool order. New = a section id not yet in the list, or a section written as prose,
list or table where that format is not yet recorded for the id.

| Sample | New? | Why |
|---|---|---|
| s18 | new | `billing` (billing cycles, trial period, payment methods, price changes); `cancellation` as a list |
| s19 | not new (1) | eligibility prose, exclusions list, returns prose, request prose+list, processing prose, purchase-channels/faulty-items pointer; hub page with three linked sub-policies (judgement: the hub and its sub-pages are one policy) |
| s20 | new | `store-data-sharing` (consumption information sent to Apple); `changes` as a list. Combined page (billing part not extracted); newer `/billing-refund-policy/` taken per rule 2 |
| s21 | not new (1) | eligibility prose, request embedded, trial nudge under `billing` prose |
| s22 | new | `abuse-limits` as its own prose paragraph (refund-denial grounds); also eligibility, cancellation, statutory-rights, partial-refunds (upgrades), exclusions, purchase-channels, billing in prose. Combined page `/about/terms` (five documents), refund part only |
| s23 | not new (1) | eligibility, goodwill, statutory-rights, processing, scope, exclusions, cancellation, gifts, purchase-channels, abuse-limits, request: all prose; hardware and EU withdrawal as pointers |
| s24 | not new (2) | scope, purchase-channels (merchant of record), eligibility, statutory-rights, processing, chargebacks prose; request list; eligibility review factors as list |
| s25 | not new (3) | eligibility prose, request list (incl. automated decision with human review, as in s13), purchase-channels list, processing list+prose, ineligibility reasons as exclusions list, cancellation pointer, statutory-rights and terms-link embedded |
| s26 | not new (4) | purchase-channels prose+list, request list+prose, cancellation and terms-link embedded |

Stop: s23–s27 are 5 non-new samples in a row, so `saturated: true` with 25 valid samples. Pool
candidates 28–30 (Squarespace, Sketch, Mo Meditation) were not extracted. Copies (rule 4): none;
no two tables share their headings, order and quotes.

## All samples (25)

Counts per section id; position is the median relative position (0 = first, 1 = last).

| Id | Count | Position | Formats | Samples |
|---|---|---|---|---|
| eligibility | 23/25 | 0.22 | embedded, list, prose, table | s01 s02 s03 s04 s06 s07 s08 s10 s11 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s27 |
| request | 21/25 | 0.55 | embedded, list, prose | s02 s04 s06 s07 s08 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s23 s24 s25 s26 s27 |
| purchase-channels | 18/25 | 0.42 | embedded, list, pointer, prose | s01 s02 s03 s04 s06 s11 s12 s13 s14 s15 s18 s19 s20 s22 s23 s24 s25 s26 |
| scope | 16/25 | 0.00 | list, prose | s02 s04 s07 s08 s11 s12 s13 s14 s16 s18 s20 s22 s23 s24 s26 s27 |
| exclusions | 14/25 | 0.73 | embedded, list, prose | s01 s04 s07 s08 s11 s13 s16 s18 s19 s20 s22 s23 s25 s27 |
| processing | 14/25 | 0.65 | embedded, list, prose | s02 s04 s06 s08 s11 s14 s16 s18 s19 s20 s22 s23 s24 s25 |
| cancellation | 11/25 | 0.44 | embedded, list, pointer, prose | s01 s11 s13 s14 s16 s18 s20 s22 s23 s25 s26 |
| terms-link | 9/25 | 0.73 | embedded, pointer | s01 s04 s10 s11 s16 s18 s23 s25 s26 |
| abuse-limits | 8/25 | 0.33 | embedded, prose | s02 s13 s16 s18 s20 s22 s23 s25 |
| statutory-rights | 8/25 | 0.24 | embedded, prose | s11 s13 s16 s20 s22 s23 s24 s25 |
| contact | 7/25 | 1.00 | embedded, list, pointer, prose | s03 s12 s13 s14 s18 s20 s27 |
| partial-refunds | 5/25 | 0.67 | embedded, prose, table | s02 s11 s13 s18 s22 |
| faulty-items | 5/25 | 0.50 | embedded, list, pointer, prose | s04 s08 s16 s17 s19 |
| after-refund | 4/25 | 0.44 | embedded | s11 s14 s16 s18 |
| chargebacks | 4/25 | 0.88 | embedded, prose | s16 s20 s24 s27 |
| returns | 3/25 | 0.29 | list, prose | s04 s08 s19 |
| gifts | 3/25 | 0.91 | prose | s04 s08 s23 |
| goodwill | 3/25 | 0.18 | prose | s14 s16 s23 |
| billing | 3/25 | 0.22 | list, prose | s18 s21 s22 |
| termination | 2/25 | 1.00 | prose | s02 s10 |
| exchanges | 2/25 | 0.65 | embedded, prose | s04 s19 |
| changes | 2/25 | 0.92 | list, prose | s16 s20 |
| service-issues | 1/25 | 1.00 | embedded | s01 |
| misc | 1/25 | 0.45 | prose | s04 |
| payment-plans | 1/25 | 1.00 | prose | s06 |
| order-cancellation | 1/25 | 1.00 | prose | s08 |
| store-data-sharing | 1/25 | 0.67 | prose | s20 |

## Skeleton mapping

Rare ids with no deciding fact were folded into the section they serve (`skeleton-format.md`
*Applies when*); the skeleton's counts are the union of the merged ids.

| Skeleton section | Ids | Count |
|---|---|---|
| scope | scope | 16/25 |
| eligibility | eligibility; patterns from statutory-rights (8), goodwill (3) | 23/25 |
| physical-returns | returns, exchanges, faulty-items (physical sellers s04 s08 s17 s19), order-cancellation | 4/25 |
| purchase-channels | purchase-channels; store-data-sharing as a pattern | 18/25 |
| cancellation | cancellation, partial-refunds | 12/25 |
| request | request; contact (7) as a pattern | 21/25 |
| processing | processing, after-refund | 14/25 |
| exclusions | exclusions, abuse-limits, chargebacks, termination | 17/25 |
| gifts | gifts | 3/25 |
| Document level | terms-link (9), changes (2), billing (3, belongs to subscription terms), effective date | — |
| Commonly omitted | service-issues, payment-plans, misc, faulty digital products (s16) | — |

## Document level

- Words: median 500, range 41–2,559; 9/25 under 250.
- Page type: 12 standalone (s19 a hub with three sub-policies), 11 help-center articles, 2
  combined (s20 billing and refund, s22 five documents on one terms page).
- Organised by purchase channel: s02 s03 s12 s14 s15 s18 s19 s20 s26.
- Question headings: s02 s15 s21 s25 s26. Numbered sections: s16 s18 s20 s22 s24. Tables: s11 s13.
- Visible date: s02 s14 s16 s18 s20 s22 s23 s24 s26.
- Third person: s07 s10 s19. Formal drafting: s10 s16 s18 s20 s22.

## Regional content

Content one law or region requires, left out of the root skeleton. Region runs start here.

| Region | Content | Samples |
|---|---|---|
| eu | 14-day withdrawal right for digital content and services; loss of the right once supply starts with express consent; withdrawal button | s02 s11 s16 s18 s20 s22 s23 |
| eu | strong customer authentication for web payments | s18 |
| de | cancellation without signing in | s13 |
| uk | 14-day withdrawal named with the EU; UK annual-renewal cancellation period | s02 s16 s20 s22 |
| tr | 14-day window named for Turkey | s02 s16 |
| us | state cooling-off (3 days) for named states; pro-rated refund on death, partial on disability | s20 |
| us | territory export steps for high-value returns (Puerto Rico) | s04 |
| kr, br | 7-day cancellation right | s02 s16 |
| cn | China: 7-day right; country-specific rules by pointer | s07 s16 |
| ca | 7-day cancellation; French version acknowledgement (Quebec) | s16 |
| sg, il | 5-day (Singapore) and 14-day (Israel) rights | s16 |
| several | pro-rated refunds available per country, as tables (Canada, Denmark, France, Israel, Korea, Türkiye, others) | s13 |

s24 and s25 mention mandatory law without naming a region; that line stays in the root
(`eligibility` pattern).

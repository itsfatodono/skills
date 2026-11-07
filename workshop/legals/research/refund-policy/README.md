# refund-policy: build record

Built 2026-10-26 (Phase 3 batch 1). Skeleton: `plugins/fatodono-launchkit/skills/legals/skeletons/refund-policy.md`.
New fact keys: `proposed-facts.md`. Merge, saturation log and regional content: `merge.md`.

## Run

- **Routes run:** R1 (US `topgrossingapplications`, 17 genres in two slices), R2 (12 keywords,
  US), R3 (Play US, 9 categories), R4 (web software, consumer and B2B SaaS, e-commerce). Raw
  rows: `pool/` (137 rows, 8 slices). Selection: `candidates.md` (30 candidates, 10 per size,
  no sector above 4).
- **First batch:** s01–s04, s06–s08, s10–s17 (15 valid, 5 per size). s05 (Strava) and s09
  (Wanderlog) were invalid and replaced by s16 (Paddle) and s17 (Graza), the next unused
  candidates of the same size.
- **Saturation:** batch s18–s22, then s23–s27. New: s18, s20, s22. Not new: s19, s21, then
  s23, s24, s25, s26, s27 (5 in a row).
- **Stop reason:** saturated after s27. `sample_count: 25`. Pool candidates 28–30 were not
  needed.

## Invalid

| Sample | Company | Rule | Reason |
|---|---|---|---|
| s05 | Strava, Inc. | 6 | terms of service; refunds only as two single sentences inside "Fees and Payment", no distinct refund part |
| s09 | Wanderlog (Travelchime Inc.) | 6 | the refund URL serves the whole terms of use; the "Refunds" clause is one sentence |

## Copies (rule 4)

None. No two extraction tables share headings, order and quotes.

## Templates

- s08 (Fellow) and s17 (Graza) are Shopify `/policies/refund-policy` pages: the platform's
  policy page and title, with each shop's own text. They count as normal samples.
- s16 (Paddle) and s24 (Serpentype, sold through Paddle) are related: Serpentype's own short
  policy names Paddle as merchant of record; the texts differ.
- No generated-policy text (Termly, iubenda and similar) was found among the samples.

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Spotify AB | https://support.spotify.com/us/article/refund-policy/ | music | large | en | 2026-10-26 |
| s02 | Perplexity AI Inc. | https://intercom.help/perplexity-ai/en/articles/10354288-refunds | productivity | mid | en | 2026-10-26 |
| s03 | Evolly.app Pte. Ltd. | https://evolly.app/refund-policy-test/ | utilities | small | en | 2026-10-26 |
| s04 | Apple Inc. | https://www.apple.com/shop/help/returns_refund | e-commerce | large | en | 2026-10-26 |
| s06 | Libros Media Limited (Rocket Languages) | https://www.rocketlanguages.com/refund-policy | education | small | en | 2026-10-26 |
| s07 | JetBrains | https://sales.jetbrains.com/hc/en-gb/articles/38317486190610-Refunds-How-to-request-a-refund-for-a-JetBrains-purchase | developer-tools | large | en | 2026-10-26 |
| s08 | Fellow | https://fellowproducts.com/policies/refund-policy | e-commerce | mid | en | 2026-10-26 |
| s10 | Payward, Inc. (Kraken) | https://www.kraken.com/legal/refund-policy | finance | large | en | 2026-10-26 |
| s11 | Setapp (MacPaw) | https://setapp.com/refund-policy | utilities | mid | en | 2026-10-26 |
| s12 | Pixelcut Inc. | https://www.pixelcut.ai/docs/user-guide/plans-credits/refunds | graphics-design | small | en | 2026-10-26 |
| s13 | Microsoft | https://support.microsoft.com/en-us/accounts-billing/subscriptions/microsoft-subscription-refund-policy | productivity | large | en | 2026-10-26 |
| s14 | Tonara / JoyTunes (Simply) | https://piano-help.hellosimply.com/en/articles/2639396-request-a-refund-for-simply-piano | education | mid | en | 2026-10-26 |
| s15 | Hevy Studios | https://www.hevyapp.com/help/refund-ios-andriod/ | health-fitness | small | en | 2026-10-26 |
| s16 | Paddle | https://www.paddle.com/legal/refund-policy | b2b-saas | mid | en | 2026-10-26 |
| s17 | Graza | https://graza.co/policies/refund-policy (text via https://checkout.shopify.com/55000039638/policies/refund-policy) | e-commerce | small | en | 2026-10-26 |
| s18 | Lightricks Ltd. | https://static.lightricks.com/legal/refund-policy.html | photo-video | large | en | 2026-10-26 |
| s19 | Nintendo of America | https://www.nintendo.com/us/refund-return-policy/ (with its three sub-pages) | games | large | en | 2026-10-26 |
| s20 | Municorn Limited | https://comfax.com/billing-refund-policy/ | business | mid | en | 2026-10-26 |
| s21 | fournova Software GmbH (Tower) | https://www.git-tower.com/help/guides/account/faq/refunds | developer-tools | small | en | 2026-10-26 |
| s22 | Coursera Inc. | https://www.coursera.org/about/terms#refund-and-cancellation-policy | education | large | en | 2026-10-26 |
| s23 | Valve Corporation (Steam) | https://store.steampowered.com/steam_refunds/ | games | mid | en | 2026-10-26 |
| s24 | Serpentype | https://www.serpentype.com/refund | e-commerce | small | en | 2026-10-26 |
| s25 | Nordvpn S.A. | https://support.nordvpn.com/hc/en-us/articles/19476991311121 | utilities | large | en | 2026-10-26 |
| s26 | Ultimate Guitar USA LLC | https://help.ultimate-guitar.com/en/articles/6741748-how-to-request-a-refund-for-an-ultimate-guitar-subscription | music | mid | en | 2026-10-26 |
| s27 | Ibericode (MC4WP) | https://www.mc4wp.com/refund-policy/ | developer-tools | small | en | 2026-10-26 |

Size mix: 9 large, 8 mid, 8 small. Two replacements kept the first batch at 5 per size; the
saturation batches followed pool order, which is why the sizes are not even.

## Size shortfalls

None. Each size third had 10 candidates. Small sellers with their own refund page were easy to
find on the web (R4) and through R2. App-store developers rarely publish one: the R1 consumer
slice found 20 among about 360 top-grossing apps.

## Judgement calls

- s19 (Nintendo): the candidate URL is a hub of three one-sentence links. The three linked
  policies (digital, online store, retail stores) were extracted with it as one sample: one
  company, one refund policy split by sales channel.
- s20 (Municorn): the candidate `/refund/` page is an older version; the site's footer links
  `/billing-refund-policy/`, which was taken per rule 2. It is a combined billing-and-refund
  page; only the refund part was extracted.
- s22 (Coursera): the `/about/terms/refund` URL renders nothing; the refund part of
  `/about/terms` (five documents on one page) was extracted per rule 6.
- s17 (Graza): the shop's domain blocks fetching and Wayback has no capture; the text came from
  the same store's Shopify policy endpoint, a host the shop's pages use (rule 1).
- s16 (Paddle) sells other companies' software as merchant of record. Its policy is buyer-facing
  and its own text, so it counts; it is the source of most of the country content in `merge.md`.
- Section folding: rare ids with no deciding fact were folded into the section they serve
  (`merge.md` *Skeleton mapping*). `statutory-rights` (8/25) became an `eligibility` pattern,
  so the root carries only "mandatory law prevails"; country rules went to *Regional content*.
- Billing content (cycles, trials, price changes) found in 3 samples was left out of the
  skeleton as belonging to the subscription terms; the document level says so.

## Lessons

- **Rule 6 needs a size floor.** Collectors marked ToS pages `(combined)` whenever they had a
  "Refunds" heading. Two of the four combined candidates (Strava, Wanderlog) had a
  one-sentence refund clause and failed at extraction. Rule 6 says "a distinct part" but not
  how big; a pool collector should open the part and check it says more than one sentence.
- **R1 is a weak route for refund pages.** The `topgrossing` hint in *Documents* row A yields
  few hits: most app developers leave refunds to the stores and publish nothing. R4 at web
  sellers (SaaS, software, e-commerce) and R2's small developers gave most of the pool.
- **JS-rendered help centers.** Zendesk's Help Center API JSON, Intercom's server HTML and
  Apple's `<noscript>` block gave full text where curl got a shell; Wayback was not needed.
  This belongs in the extractor's fetch step.
- **Hub pages.** Some companies split the policy across linked sub-pages (Nintendo). No rule
  says whether linked sub-pages are part of the sample; it was treated like a combined page in
  reverse.
- **Collectors' URLs go stale.** Two candidates (Municorn, Coursera) pointed to an old or empty
  page; the extractor found the live one through the site's own links. Rule 2 worked as
  written.
- **Retries on API overload.** After a 529 stop, re-dispatching a "missing" collector raced the
  original, which was still running: both wrote `pool/r2-tail.md`, and the later write replaced
  the earlier one (two reserve rows were lost; no selected candidate was affected). A retry
  should write to a new slice file, or first confirm that the original agent has stopped.

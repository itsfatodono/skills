# subscription-terms: build record

Built 2026-10-26 (Phase 3, batch 1, global run, English). Skeleton:
`plugins/fatodono-launchkit/skills/legals/skeletons/subscription-terms.md`. New fact keys:
`proposed-facts.md`. Merged section list, judging and regional content: `merge.md`.
Selection: `candidates.md`.

## Run

- **Routes run:** R1 (US `topgrossingapplications` feeds, 22 genres in 4 slices), R2 (22
  keywords in 2 slices), R3 (Play US, 8 categories; the category pages showed no grossing
  list, so the top-chart list was used), R4 (each candidate's own site, to locate the terms).
  Raw rows: `pool/` (119 rows, 7 `pool-collector` slices). The four R1 slices came from the
  stopped earlier run and were kept; the R2 and R3 slices were added in this run.
- **Pool:** 30 candidates, 10 large, 10 mid, 10 small; no sector above 3. Group check at
  selection (rule 5): Match Group (Tinder kept, Hinge dropped), Google (YouTube kept, YouTube
  Music dropped), Sirius XM (Pandora kept, SiriusXM dropped), Disney and Microsoft (none
  selected).
- **First batch:** s01–s15, 5 per size, all valid. s17 and s18 were extracted early as spares
  and judged in pool order.
- **Saturation:** batches s16–s20, s21–s25, s26–s30. New: s17, s20, s25, s28, s30. The longest
  run of non-new samples was 4 (s21–s24).
- **Stop reason:** pool exhausted after s30; `saturated: false`. `sample_count: 30`. Only one
  sample after the first batch added a new section (s25, `pause`); the other four new samples
  were new by format (a section written as a list for the first time).
- **Placement (rule 6):** 19/30 subscription parts inside the ToS, 11/30 separate pages; see
  `merge.md` *Document level*.

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Tinder LLC | https://policies.tinder.com/terms/intl/en/ | lifestyle | large | en | 2026-10-26 |
| s02 | Telegram FZ-LLC | https://telegram.org/tos#terms-of-service-for-telegram-premium | social-networking | mid | en | 2026-10-26 |
| s03 | Reviva Softworks Ltd (SnoreLab) | https://www.snorelab.com/terms-of-use | medical | small | en | 2026-10-26 |
| s04 | Netflix, Inc. | https://web.archive.org/web/20261014020742/https://help.netflix.com/legal/termsofuse | entertainment | large | en | 2026-10-26 |
| s05 | You Need A Budget LLC | https://www.ynab.com/terms/ | finance | mid | en | 2026-10-26 |
| s06 | Happy Moose Apps Inc. (Bitsboard) | https://www.bitsboard.com/subscription-terms | education | small | en | 2026-10-26 |
| s07 | Dropbox, Inc. | https://www.dropbox.com/terms | productivity | large | en | 2026-10-26 |
| s08 | Calm.com, Inc. | https://web.archive.org/web/20251226204828/https://www.calm.com/terms | health-fitness | mid | en | 2026-10-26 |
| s09 | Flighty LLC | https://flighty.com/legal/terms | travel | small | en | 2026-10-26 |
| s10 | NFL Enterprises LLC | https://www.nfl.com/legal/subscriptions_terms | sports | large | en | 2026-10-26 |
| s11 | Wyze Labs, Inc. | https://services.wyze.com/terms/camplus | lifestyle | mid | en | 2026-10-26 |
| s12 | KptnCook GmbH | https://www.kptncook.com/terms | food-drink | small | en | 2026-10-26 |
| s13 | The New York Times Company | https://help.nytimes.com/policies/115014893968-terms-of-sale | news | large | en | 2026-10-26 |
| s14 | Ultimate Guitar USA LLC | https://www.ultimate-guitar.com/about/tos.htm | music | mid | en | 2026-10-26 |
| s15 | GM UniverseApps Limited (Cleaner Guru) | https://cleanerguru.universeapps.limited/hub/legal/subscription-terms | utilities | small | en | 2026-10-26 |
| s16 | Strava, Inc. | https://www.strava.com/legal/terms | health-fitness | large | en | 2026-10-26 |
| s17 | ClassDojo, Inc. | https://www.classdojo.com/premium-features-terms/ | education | mid | en | 2026-10-26 |
| s18 | Copilot Money, Inc. | https://www.copilot.money/terms-of-service | finance | small | en | 2026-10-26 |
| s19 | Adobe Inc. | https://www.adobe.com/legal/subscription-terms.html (via https://web.archive.org/web/20261015184728/ and Adobe's AEM origin fragment) | business | large | en | 2026-10-26 |
| s20 | Perplexity AI, Inc. | https://www.perplexity.ai/hub/legal/terms-of-service | productivity | mid | en | 2026-10-26 |
| s21 | Unstatic Ltd Co (Habitify) | https://habitify.me/terms-of-use | health-fitness | small | en | 2026-10-26 |
| s22 | Pandora Media, LLC | https://www.pandora.com/legal/subscription | music | large | en | 2026-10-26 |
| s23 | onXmaps, Inc. | https://www.onxmaps.com/tou | navigation | mid | en | 2026-10-26 |
| s24 | Digital Workroom Ltd (Noted) | https://www.notedapp.io/terms-of-use/ | productivity | small | en | 2026-10-26 |
| s25 | Ancestry.com Operations Inc. | https://web.archive.org/web/20261016214245/https://www.ancestry.com/c/legal/renewal-cancellation-terms | reference | large | en | 2026-10-26 |
| s26 | Photoroom SAS | https://www.photoroom.com/legal/terms-and-conditions | photo-video | mid | en | 2026-10-26 |
| s27 | Book Vitals Inc. (Bible Chat) | https://thebiblechat.com/terms-and-conditions/ | reference | small | en | 2026-10-26 |
| s28 | Google LLC (YouTube) | https://www.youtube.com/t/terms_paidservice?hl=en&gl=US | photo-video | large | en | 2026-10-26 |
| s29 | Huckleberry Labs Inc. | https://huckleberrycare.com/terms-of-use | medical | mid | en | 2026-10-26 |
| s30 | Bimi Boo Kids Learning Games for Toddlers FZ LLC | https://bimiboo.net/subscription-terms/ | education | small | en | 2026-10-26 |

## Templates

No two samples share a whole text, so no sample was counted as a copy (rule 4). Texts built
from templates or model wording stay valid samples: s24 (an online-generator terms template
with added store sentences), s06 (the app-store auto-renewal disclosure checklist pasted in
twice), s21 (a generic terms template plus statutory model withdrawal wording), s12 (statutory
model withdrawal instructions and form inside the company's own text).

## Size shortfalls

None: 10 large, 10 mid, 10 small. The large and mid thirds came from the R1 grossing charts;
most of the small third came from R2.

## Judgement calls

- **s11 Wyze:** the candidate URL was a 75-word store "Cancellation policy" stub whose first
  line points to the Cam Plus Supplemental Terms. The stub was replaced by that page, Wyze's
  actual subscription terms, before judging.
- **s25 Ancestry:** the ToS section on renewals is a one-sentence pointer to a separate
  "Renewal and Cancellation Terms" page; that page was extracted (its subscription block only).
- **s04 Netflix, s08 Calm:** the live pages serve a version by the fetcher's location (or
  block fetching); the latest Wayback capture of the default US English version was used.
- **s19 Adobe:** the early-termination charge is read as a `cancellation` pattern, not a new
  section; prepaid and redemption cards as `gifts`; credit packs as `one-time-purchases`.
- **Folded rare sections:** `service-changes` into `changes`, `company-termination` into
  `cancellation`, `billing-disputes` into `payment`, `legal-boilerplate` and `contact` into
  `scope`. They are drafting sections that no fact decides. `pause` (1/30) is kept as a rare
  section because a fact decides it.
- **Regional content** (statutory withdrawal, state and country rules) is out of the root and
  listed in `merge.md` *Regional content*; no region blocks were built.

**Re-judged (2026-10-26):** under `PLAN.md` decision 27 (new section ids only) the run
saturated at s20; see `merge.md`.

## Lessons

- **Format novelty kept the counter from reaching 5.** After the first batch, four of the
  five new samples (s17, s20, s28, s30) were new only because a page laid out mostly as
  bullets wrote a known section as a list. The section list stopped growing at s25. Build
  step 3 already treats whole-document layouts (a summary before each section) as
  document-level. An all-bullets page is the same kind of layout and could be recorded once at
  document level.
- **Rule 6 with pointer pages.** Two candidates' listed "subscription" pages were pointers: a
  one-sentence ToS section (s25) and a store stub (s11). Rule 6 does not say whether to follow
  the pointer. Following it to the company's own subscription document worked. Taking the
  pointer page would have made both invalid, or a 75-word sample.
- **Scattered ToS parts.** 8/19 ToS samples spread subscription topics over non-adjacent
  sections (trial in one place, payment in another, cancellation in a third). Pool rows name
  one heading. Extractors needed an explicit instruction to collect every paid-plan section and
  leave out general ones.
- **Placement marks at pool time.** Having collectors mark each row `(separate)` or
  `(ToS § "<heading>")` made the placement split countable at selection, and kept the pool
  mixed (9 separate, 21 ToS).
- **Parallel dispatch under load.** The first dispatch of 20 extractors hit API overload (HTTP
  529) and 9 died; the rest of the build ran at most 3 at a time. Early dispatch of spares
  helps only when capacity allows.
- **Word counts mislead on matrix pages.** s19 repeats the same paragraphs once per plan (about
  23,000 words, 9,000 unique), which skews length statistics; the skeleton reports the median.

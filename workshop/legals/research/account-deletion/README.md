# account-deletion: build record

Built 2026-10-26 (batch 1). Skeleton: `plugins/fatodono-launchkit/skills/legals/skeletons/account-deletion.md`.
Proposed fact keys: `proposed-facts.md`.

## Run

- **Routes run:** R1 (App Store US charts: Social Networking, Lifestyle, Health & Fitness, Photo
  & Video, Productivity, Finance, Education, Music, Entertainment), R2 (App Store US long tail,
  8 keywords), R3 (Play US: Shopping, Travel & Local, Food & Drink, Communication, Business,
  Parenting, Maps & Navigation, Auto & Vehicles; News & Magazines and Medical from category
  leaders, because their chart pages returned no list), R4 (company help centers and deletion
  pages, for every row). Raw rows: `pool/` (94 rows, 5 slices). Selection: `candidates.md`.
- **Resumed run:** three slices (`r1-social-health`, `r1-work-media`, `r2-tail-a`) were on disk
  from the stopped run and untouched by the old rule 4, so they were kept. No samples,
  candidates or merge existed. `r3-play-a` and `r3-play-b` were added. A planned second
  long-tail slice was not run: the small third already had 27 rows.
- **First batch:** s01–s15, all valid; no replacements.
- **Saturation:** s16–s20, then s21–s25. New: s20 (section `inactivity`; `partial-deletion` as a
  list). Not new: s16–s19, then s21–s25 (5 in a row).
- **Stop reason:** saturated after s25. `sample_count: 25`.
- **Merged section list and judgements:** `merge.md`.

## Sizes

9 large, 8 mid, 8 small. No shortfall: the pool held 10 per size.

## Templates and copies

No two samples share the same text (rule 4). Several small companies publish a dedicated
`/delete-account` page of the shape Google Play asks for (s06, s12, s15, s18, s21, s24), but
each is written differently. Fiverr publishes one article under three help-center ids; it was
extracted once (s22).

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Spotify AB | https://support.spotify.com/us/article/how-can-i-close-my-spotify-account/ | music | large | en | 2026-10-26 |
| s02 | Calm.com, Inc. | https://support.calm.com/api/v2/help_center/en-us/articles/115003990133.json | health-fitness | mid | en | 2026-10-26 |
| s03 | Partiful | https://help.partiful.com/en-us/articles/15525651-how-can-i-delete-my-account | lifestyle | small | en | 2026-10-26 |
| s04 | Strava | https://support.strava.com/en-us/articles/15401906-how-do-i-delete-my-strava-account | health-fitness | large | en | 2026-10-26 |
| s05 | Medisafe | https://help-center.medisafe.com/en/articles/8095731-i-would-like-to-delete-my-account | medical | mid | en | 2026-10-26 |
| s06 | Bill Tracker Pro, Inc. | https://billtrackerpro.com/account-deletion | finance | small | en | 2026-10-26 |
| s07 | Duolingo, Inc. | https://www.duolingo.com/help/9/delete-my-account-and-data | education | large | en | 2026-10-26 |
| s08 | Qustodio | https://www.qustodio.com/en/help-close-account/ | utilities | mid | en | 2026-10-26 |
| s09 | Galaxy Edge Ltd | https://recipenotes.app/help/delete-account | food-drink | small | en | 2026-10-26 |
| s10 | Pinterest | https://help.pinterest.com/en/article/deactivate-or-close-your-account | lifestyle | large | en | 2026-10-26 |
| s11 | Monarch Money | https://help.monarch.com/api/v2/help_center/en-us/articles/4412388754708.json | finance | mid | en | 2026-10-26 |
| s12 | Styrkelabbet AB | https://www.strengthlog.com/delete-strengthlog-account/ | health-fitness | small | en | 2026-10-26 |
| s13 | OpenAI | https://help.openai.com/en/articles/6378407-deleting-your-chatgpt-account | productivity | large | en | 2026-10-26 |
| s14 | Transit App | https://help.transitapp.com/article/201-manage-your-transit-account | navigation | mid | en | 2026-10-26 |
| s15 | Flashcards World SL | https://flashcards.world/delete_account | education | small | en | 2026-10-26 |
| s16 | Vinted UAB | https://www.vinted.com/help/88 | shopping | large | en | 2026-10-26 |
| s17 | Polarsteps | https://support.polarsteps.com/api/v2/help_center/en-us/articles/24267572129554.json | travel | mid | en | 2026-10-26 |
| s18 | jinal alagiya (PlanWiz) | https://planwiz.app/delete-account/ | productivity | small | en | 2026-10-26 |
| s19 | Snap Inc. | https://help.snapchat.com/hc/en-us/articles/7012328360596-How-do-I-deactivate-or-delete-my-Snapchat-account | photo-video | large | en | 2026-10-26 |
| s20 | Telegram | https://telegram.org/faq#q-how-do-i-delete-my-account | social-networking | mid | en | 2026-10-26 |
| s21 | With Bytes LLC | https://www.critiqueai.app/help/delete-account | lifestyle | small | en | 2026-10-26 |
| s22 | Fiverr International Ltd. | https://help.fiverr.com/api/v2/help_center/en-us/articles/36988729058961.json | business | large | en | 2026-10-26 |
| s23 | Feedly | https://docs.feedly.com/article/211-how-can-i-delete-my-feedly-account | news | mid | en | 2026-10-26 |
| s24 | New Chapter Technology LLC | https://langx.io/data-deletion | education | small | en | 2026-10-26 |
| s25 | Life360, Inc. | https://support.life360.com/api/v2/help_center/en-us/articles/23053748967319.json | social-networking | large | en | 2026-10-26 |

URL notes: `api/v2/help_center` URLs are the public Zendesk article API for a help-center page
that blocks fetchers (s02, s11, s17, s22, s25). s03: the pool URL was a one-sentence stub; its
only link led to the real article, which was extracted. s22: the pool URL (`fiverr.com/delete`)
is a bot wall whose captures are not a deletion page; Fiverr's own help-center deletion article
was extracted. s13 was read through a reader proxy of the live page (403 to scripts, Wayback
offline). s07 was read from the JSON endpoint the JS-only page loads.

## Lessons

- **Play hides the deletion URL.** The Data safety page shows only "You can request that data
  be deleted" (confirmed on `com.strava`), as `sources.md` *Forms* says. R3 yields app names
  only; every deletion URL still comes from R4, which took most of the collectors' time
  (26 of 43 apps skipped in one slice for lack of a findable page).
- **Zendesk JSON API.** Many help centers return 403 to scripts. `https://<host>/api/v2/help_center/<locale>/articles/<id>.json`
  served the live article for 5 samples where Wayback would otherwise have been needed.
  `sources.md` rule 2 does not mention it.
- **Collector URLs can be wrong.** A stub page (s03) and a dead redirect (s22) reached
  extractors. The brief let extractors follow to the company's real article; `sources.md` has no
  rule for that.
- **Help-center chrome.** Extractors differed on whether "Still need help?" boxes and related-
  article lists are sections. `build.md` does not say; this build excluded them at merge.
- **Section-id width decides saturation.** For short pages, the 15 ids fixed after the first
  batch were broad (one id each for steps, request route, timeline), so later samples rarely
  added a section. Narrower ids (one per platform route, one per verification step) would have
  run longer. `build.md` gives no guidance on id width.
- **Capacity.** The 20-agent limit is shared by the five parallel item builds, and the API
  returned overload errors (529). Many dispatches were refused or died; the run went to at most
  3 agents at once with retries. Early dispatch of spares was not possible.

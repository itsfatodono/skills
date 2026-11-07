---
doc_id: refund-policy
built: 2026-10-26
routes_run: [R1, R2, R3, R4]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (137 rows, 8 slices: `r1-grossing-prod`, `r1-grossing-life`,
`r2-tail`, `r3-play`, `r4-software`, `r4-saas`, `r4-ecommerce`). Size is an estimate per
`sources.md`. Rotated by size and sector; no sector above 4 of 30. Group check (rule 5) done at
selection: LinkedIn left out (Microsoft group), Audible left out (Amazon), Busuu left out (Chegg),
Dropbox and Coursera appear in two slices and are taken once. Unused raw rows are the reserve if
the pool runs out. Marks: `(combined)` ToS with a refund part (rule 6), `(help)` help-center
article, `(store-pointer)` a refund page that mostly routes store buyers to Apple or Google.

| # | Company | App (store id) | URL | Sector | Size | Language | Route |
|---|---|---|---|---|---|---|---|
| 1 | Spotify AB | Spotify: Music and Podcasts (com.spotify.music) | https://support.spotify.com/us/article/refund-policy/ (help) | music | large | en | R3 |
| 2 | Perplexity AI Inc. | Perplexity: AI Agent & Search (1668000334) | https://intercom.help/perplexity-ai/en/articles/10354288-refunds (help) | productivity | mid | en | R1 |
| 3 | Evolly.app Pte. Ltd. | TV Remote - Universal Control (1539090879) | https://evolly.app/refund-policy-test/ | utilities | small | en | R1 |
| 4 | Apple | — | https://www.apple.com/shop/help/returns_refund | e-commerce | large | en | R4 |
| 5 | Strava, Inc. | — | https://www.strava.com/legal/terms (combined) | health-fitness | mid | en | R4 |
| 6 | Libros Media Limited | Rocket Languages (597293943) | https://www.rocketlanguages.com/refund-policy | education | small | en | R2 |
| 7 | JetBrains | — | https://sales.jetbrains.com/hc/en-gb/articles/38317486190610-Refunds-How-to-request-a-refund-for-a-JetBrains-purchase (help) | developer-tools | large | en | R4 |
| 8 | Fellow | — | https://fellowproducts.com/policies/refund-policy | e-commerce | mid | en | R4 |
| 9 | Vacation and Travel Planner App LLC | Wanderlog - Travel Planner (1476732439) | https://wanderlog.com/terms/refund-policy (combined) | travel | small | en | R1 |
| 10 | Payward, Inc. (Kraken) | Kraken: Buy Crypto & Stocks (1481947260) | https://www.kraken.com/legal/refund-policy | finance | large | en | R1 |
| 11 | Setapp (MacPaw) | — | https://setapp.com/refund-policy | utilities | mid | en | R4 |
| 12 | Pixelcut Inc. | Pixelcut: AI Photo & Video (1534785237) | https://www.pixelcut.ai/docs/user-guide/plans-credits/refunds (help) | graphics-design | small | en | R1 |
| 13 | Microsoft | — | https://support.microsoft.com/en-us/accounts-billing/subscriptions/microsoft-subscription-refund-policy (help) | productivity | large | en | R4 |
| 14 | Tonara / JoyTunes (Simply) | Simply Piano (com.joytunes.simplypiano) | https://piano-help.hellosimply.com/articles/2639396-request-a-refund (help) | education | mid | en | R3 |
| 15 | Hevy Studios | Hevy - Gym Log Workout Tracker (com.hevy) | https://www.hevyapp.com/help/refund-ios-andriod/ (store-pointer) | health-fitness | small | en | R3 |
| 16 | Lightricks Ltd. | Facetune: Photo & Video Editor (1149994032) | https://static.lightricks.com/legal/refund-policy.html | photo-video | large | en | R1 |
| 17 | Paddle | — | https://www.paddle.com/legal/refund-policy | b2b-saas | mid | en | R4 |
| 18 | Graza | — | https://graza.co/policies/refund-policy | e-commerce | small | en | R4 |
| 19 | Nintendo | — | https://www.nintendo.com/us/refund-return-policy/ | games | large | en | R4 |
| 20 | Municorn Limited | FAX from iPhone: Send Doc App (978931264) | https://comfax.com/refund/ | business | mid | en | R1 |
| 21 | Tower (fournova) | — | https://www.git-tower.com/help/guides/account/faq/refunds (help) | developer-tools | small | en | R4 |
| 22 | Coursera Inc. | Coursera: Grow your career (org.coursera.android) | https://www.coursera.org/about/terms/refund | education | large | en | R3 |
| 23 | Valve (Steam) | — | https://store.steampowered.com/steam_refunds/ | games | mid | en | R4 |
| 24 | Serpentype | — | https://www.serpentype.com/refund | e-commerce | small | en | R4 |
| 25 | Nordvpn S.A. | NordVPN: VPN Fast & Secure (905953485) | https://support.nordvpn.com/hc/en-us/articles/19476991311121 (help) | utilities | large | en | R1 |
| 26 | Ultimate Guitar USA LLC | Ultimate Guitar: Chords & Tabs (com.ultimateguitar.tabs) | https://help.ultimate-guitar.com/en/articles/6741748-how-to-request-a-refund-for-an-ultimate-guitar-subscription (help) | music | mid | en | R3 |
| 27 | MC4WP (Ibericode) | — | https://mc4wp.com/refund-policy | developer-tools | small | en | R4 |
| 28 | Squarespace | — | https://www.squarespace.com/terms-of-service (combined) | business | large | en | R4 |
| 29 | Sketch | — | https://www.sketch.com/support/general/refunds/ (help) | graphics-design | mid | en | R4 |
| 30 | Mo Meditation Inc. | Mo Meditation, Sleep, Recovery (1570156834) | https://momeditation.app/refund-policy | health-fitness | small | en | R2 |

## Reserve order (same size, used in this order when a candidate is invalid)

- large: Anthropic PBC (support.claude.com refund article), Bose, Envato, 1Password, Wix, Aura, Anker eufy, Discord, Shopify (combined)
- mid: Owlet, WeTransfer, Speechify, Teachable, WP Rocket, Kiddopia, PlantIn (Vortemol), Proton (combined), Our Place, TextNow
- small: Novel Effect, Intuitibits, Workouts+ (Anuj Seth), Sparkful, Settlemate, Mozart (NineG), Bullet Journal (Lightcage), Burner, Handscraft, Apimac

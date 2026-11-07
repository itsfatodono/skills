# refund-policy pool: r1-grossing-life

Route R1, App Store US (`us`), feed `topgrossingapplications` (limit=100 per genre), genres 6013 Health & Fitness, 6017 Education, 6012 Lifestyle, 6016 Entertainment, 6011 Music, 6005 Social Networking, 6015 Finance, 6018 Books, 6020 Medical, 6023 Food & Drink, 6003 Travel, 6001 Weather, walked interleaved by rank (the first 360 distinct apps, about the top 30 of each genre, were examined). sellerName, sellerUrl, primary genre and userRatingCount come from the lookup API (`country=us`). Refund documents were located via R4: for each developer domain I probed common paths (`/refund-policy`, `/refunds`, `/legal/refund-policy`, `/policies/refund-policy`, `/terms/refund-policy`, `/returns` and similar, on the sellerUrl host, www and bare domain) and kept pages that load and are about refunds, then scanned homepages of the rest for refund links and web-searched a few large apps (Duolingo, Tinder, MyFitnessPal, Peacock, Life360 had no fetchable refund page). Most apps have none and were skipped; `(blocked)` marks Cloudflare/JS-only pages that returned a bot wall or empty shell to curl. Genre is the App Store primary genre (Book = Books). Some companies are device makers whose app is a companion (Wyze, Eko, Nanit, Owlet, eufy, Hume); their refund page covers hardware as well.

| Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
|---|---|---|---|---|---|---|
| Audible, Inc. | Audible: Audiobooks & Podcasts | 379693831 | Book | 5616696 (App Store US) | https://www.audible.com/legal/refund-policy (blocked) | http://www.audible.com |
| Wyze Labs, Inc. | The Official Wyze App | 1288415553 | Lifestyle | 461613 (App Store US) | https://www.wyze.com/policies/refund-policy (blocked) | https://www.wyze.com |
| Eko Health, Inc. | Eko: Digital Stethoscope + ECG | 1026457544 | Medical | 11145 (App Store US) | https://www.ekohealth.com/policies/refund-policy (blocked) | http://shop.ekohealth.com |
| Nara Organics, Inc. | Nara Baby & Pregnancy Tracker | 1444639029 | Medical | 24486 (App Store US) | https://nara.com/policies/refund-policy (blocked) | https://narababy.com/pages/nara-baby-tracker |
| UdiSense Inc. | Nanit | 1137885597 | Lifestyle | 38348 (App Store US) | https://www.nanit.com/policies/refund-policy (blocked) | https://www.nanit.com |
| FitTrack Inc | Hume Health | 1477782599 | Health & Fitness | 75288 (App Store US) | https://humehealth.com/policies/refund-policy | https://humehealth.com |
| AURA GET INC | Aura: Security & Protection | 1547735089 | Finance | 110868 (App Store US) | https://www.aura.com/legal/refund-policy | https://www.aura.com |
| Owlet Baby Care, Inc. | Owlet Dream | 1590590105 | Lifestyle | 43104 (App Store US) | https://owletcare.com/policies/refund-policy | https://owletcare.com |
| Payward, Inc. | Kraken: Buy Crypto & Stocks | 1481947260 | Finance | 35970 (App Store US) | https://www.kraken.com/legal/refund-policy | https://kraken.com |
| EVOY LTD | Whipp: Meal Planner & Recipes | 6778126199 | Food & Drink | 449 (App Store US) | https://www.whipp.app/refund (store-pointer) | https://whipp.app |
| Settlemate Inc | Settlemate: Claim Savings | 6737785495 | Finance | 76062 (App Store US) | https://www.settlemate.io/refund-policy | https://www.settlemate.io |
| Vacation and Travel Planner App LLC | Wanderlog - Travel Planner | 1476732439 | Travel | 36113 (App Store US) | https://wanderlog.com/terms/refund-policy (combined) | https://wanderlog.com |
| Novel Effect Inc | Novel Effect: Read Aloud Books | 1057374139 | Book | 9855 (App Store US) | https://noveleffect.com/refund_returns/ | https://noveleffect.com |
| SimplyWise, Inc. | SimplyWise: Receipts, Expenses | 1538521095 | Finance | 38208 (App Store US) | https://www.simplywise.com/terms (combined) | https://www.simplywise.com |
| Power Mobile Life LLC | Anker eufy | 1424956516 | Lifestyle | 71598 (App Store US) | https://www.eufy.com/policies/refund-policy | https://www.eufylife.com |
| TradingView, Inc. | TradingView: Track All Markets | 1205990992 | Finance | 421034 (App Store US) | https://www.tradingview.com/support/solutions/43000485430-i-ve-paid-for-a-subscription-and-would-like-to-get-a-refund/ (help) | https://www.tradingview.com/about |
| Vortemol Limited | PlantIn: Plant Identifier・Care | 1527399597 | Education | 230263 (App Store US) | https://legal.myplantin.com/vortemol/money-back-policy.html | https://myplantin.com |
| WINK TECH LIMITED | Duet Dating App: Chat & Meet | 1673723000 | Lifestyle | 106513 (App Store US) | https://duetapp.net/refund | https://duetapp.net |
| Kiddopia, Inc. | Kiddopia: Kids Learning Games | 1223397201 | Education | 162172 (App Store US) | https://kiddopia.com/refund-and-cancellation-policy | https://kiddopia.com |
| NINEG UYGULAMA GELISTIRME VE PAZARLAMA ANONIM SIRKETI | AI Song Generator: Mozart | 6502656704 | Music | 31861 (App Store US) | https://mozartai.app/refund-policy | https://mozartai.app |

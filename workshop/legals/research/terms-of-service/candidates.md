---
doc_id: terms-of-service
built: 2026-10-26
routes_run: [R1, R2, R4]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (6 slices; the planned `r3-play` slice never landed and
was not needed, see `README.md`). Size is an estimate per `sources.md`. Group check (rule 5) done at
selection: one brand per owner (Meta, Google, Amazon, Microsoft/LinkedIn, Match Group,
ByteDance, X Corp, Uber, NYT each at most once across pool and reserve; Hinge taken, so
Tinder is out). No sector above 7 of 30.

| # | Company | App (store id) | URL | Sector | Size | Language | Route |
|---|---|---|---|---|---|---|---|
| 1 | Anthropic PBC | Claude by Anthropic (6473753684) | https://www.anthropic.com/legal/consumer-terms | productivity | large | en | R1 |
| 2 | Substack Inc. | Substack (1581650857) | https://substack.com/tos | news | mid | en | R1 |
| 3 | Flighty LLC | Flighty – Live Flight Tracker (1358823008) | https://flighty.com/legal/terms | travel | small | en | R1 |
| 4 | Strava Inc. | Strava: Run, Bike, Walk (426826309) | https://www.strava.com/legal/terms | health-fitness | large | en | R1 |
| 5 | Suno Inc. | Suno - AI Songs, Music, Lyrics (6480136315) | https://suno.com/terms | music | mid | en | R1 |
| 6 | Partiful Co. | Partiful: Party Invite Maker (1662982304) | https://partiful.com/terms | lifestyle | small | en | R1 |
| 7 | Block, Inc. | Cash App (711923939) | https://cash.app/us/en/legal/tos | finance | large | en | R1 |
| 8 | Speak (Speakeasy Labs) | Speak: Language Learning (1286609883) | https://www.speak.com/terms | education | mid | en | R1 |
| 9 | Sebastian Roehl | Habit Tracker - HabitKit (6443918070) | https://habitkit.app/terms | productivity | small | en | R2 |
| 10 | Snap Inc. | Snapchat (447188370) | https://www.snap.com/terms?lang=en-US | photo-video | large | en | R1 |
| 11 | Hallow, Inc. | Hallow: Prayer & Meditation (1405323394) | https://hallow.com/terms-of-service | reference | mid | en | R1 |
| 12 | Deglazed LLC | Deglaze: Recipe Manager (6443578246) | https://www.deglaze.app/terms | food-drink | small | en | R2 |
| 13 | Walmart Inc. | Walmart: Shopping & Savings (338137227) | https://www.walmart.com/help/article/walmart-com-terms-of-use/3b75080af40340d6bbd596f116fae5a0 | shopping | large | en | R1 |
| 14 | Brave Software | Brave Browser & Search Engine (1052879175) | https://brave.com/terms-of-use/ | utilities | mid | en | R1 |
| 15 | Matthew Steedman | Mochi - Flashcards and notes (1507775056) | https://mochi.cards/terms | education | small | en | R2 |
| 16 | Airbnb, Inc. | Airbnb (401626263) | https://www.airbnb.com/help/article/2908 | travel | large | en | R1 |
| 17 | Rocket Money | Rocket Money - Bills & Budgets (1130616675) | https://www.rocketmoney.com/terms | finance | mid | en | R1 |
| 18 | Just Imagine, inc. | Rosebud: AI Journal & Diary (6451135127) | https://help.rosebud.app/about-us/terms-of-service | health-fitness | small | en | R2 |
| 19 | Reddit, Inc. | Reddit (1064216828) | https://redditinc.com/policies/user-agreement | news | large | en | R1 |
| 20 | 9280-0366 Quebec inc. (Transit) | Transit: Subway & Bus Times (498151501) | https://transitapp.com/terms | navigation | mid | en | R1 |
| 21 | Weekly LLC | Weekly: Budget Planner & Bills (1460038809) | https://weeklybudgeting.com/terms | finance | small | en | R2 |
| 22 | Spotify | Spotify: Music and Podcasts (324684580) | https://www.spotify.com/us/legal/end-user-agreement/ | music | large | en | R1 |
| 23 | AllTrails, Inc. | AllTrails: Hike, Bike & Run (405075943) | https://www.alltrails.com/terms | health-fitness | mid | en | R1 |
| 24 | Arthur Chang (Priime) | Priime: Photo & Video Editor (934587545) | https://prii.me/terms.html | photo-video | small | en | R2 |
| 25 | Pinterest, Inc. | Pinterest (429047995) | https://policy.pinterest.com/en/terms-of-service | lifestyle | large | en | R1 |
| 26 | Hinge, Inc. | Hinge Dating App (595287172) | https://hinge.co/terms | lifestyle | mid | en | R1 |
| 27 | Fable Group Inc. | Fable: Track & Discuss Books (1488170618) | https://fable.co/terms | books | small | en | R1 |
| 28 | Coursera, Inc. | Coursera: Grow your career (736535961) | https://www.coursera.org/about/terms | education | large | en | R1 |
| 29 | Kahoot! ASA | Kahoot! Play & Create Quizzes (1131203560) | https://trust.kahoot.com/terms-and-conditions/ | education | mid | en | R1 |
| 30 | Invoice Home Inc. | Invoice Maker by Invoice Home (1435778692) | https://invoicehome.com/terms | business | small | en | R2 |

Sectors: education 4; health-fitness, lifestyle, finance 3; productivity, news, travel, music,
photo-video 2; reference, food-drink, shopping, utilities, navigation, books, business 1.

## Reserve

Used in this order, same size only, when the pool runs out of a size. Sector rotates.

| # | Company | App (store id) | URL | Sector | Size | Route |
|---|---|---|---|---|---|---|
| L1 | LinkedIn Corporation | LinkedIn (288429040) | https://www.linkedin.com/legal/user-agreement | business | large | R1 |
| L2 | Netflix, Inc. | Netflix Game Controller (6447582581) | https://help.netflix.com/legal/termsofuse | entertainment | large | R1 |
| L3 | Flo Health UK Limited | Flo Cycle & Period Tracker (1038369065) | https://flo.health/terms-of-service | health-fitness | large | R1 |
| L4 | Lyft, Inc. | Lyft (529379082) | https://www.lyft.com/terms | travel | large | R1 |
| L5 | Vinted Limited | Vinted (632064380) | https://www.vinted.com/terms_and_conditions | shopping | large | R1 |
| L6 | Lightricks Ltd. | Facetune (1149994032) | https://static.lightricks.com/legal/terms-of-use.pdf | photo-video | large | R1 |
| L7 | Cricut, Inc. | Cricut Design Space (749471884) | https://cricut.com/en-us/legal#terms-of-use | graphics-design | large | R1 |
| L8 | Wikimedia Foundation | Wikipedia (324715238) | https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use | reference | large | R1 |
| L9 | Okta, Inc. | Okta Verify (490179405) | https://www.okta.com/legal/terms-of-service/ | business | large | R1 |
| L10 | TradingView, Inc. | TradingView (1205990992) | https://www.tradingview.com/policies/ | finance | large | R1 |
| M1 | DuckDuckGo, Inc. | DuckDuckGo (663592361) | https://duckduckgo.com/terms | utilities | mid | R1 |
| M2 | SpotHero, Inc. | SpotHero (499097243) | https://spothero.com/legal/terms-of-use | navigation | mid | R1 |
| M3 | MyFitnessPal, Inc. | MyFitnessPal (341232718) | https://www.myfitnesspal.com/terms-of-service | health-fitness | mid | R1 |
| M4 | MileIQ Inc. | MileIQ (578830929) | https://www.mileiq.com/terms | finance | mid | R1 |
| M5 | Midwest Tape LLC (hoopla) | Hoopla (580643740) | https://www.hoopladigital.com/terms | books | mid | R1 |
| M6 | Trucker Path Inc. | Trucker Path (782746890) | https://truckerpath.com/terms-of-service | navigation | mid | R1 |
| M7 | Guideposts (Abide) | Abide (726031617) | https://abide.com/terms/ | reference | mid | R1 |
| M8 | Proton AG | Proton VPN (1437005085) | https://proton.me/legal/terms | utilities | mid | R1 |
| M9 | onXmaps, Inc. | onX Hunt (672902340) | https://www.onxmaps.com/tou | navigation | mid | R1 |
| M10 | New Leaf Publishing (ReelShort) | ReelShort (1636235979) | https://www.reelshort.com/web-terms.html | entertainment | mid | R1 |
| S1 | Thoughts ACC, Inc. | Untold - Voice Journal (6451427834) | https://web.untoldapp.com/terms | health-fitness | small | R2 |
| S2 | Rishi Mody | Neuecast (6446780219) | https://neuecast.app/terms | news | small | R2 |
| S3 | Will Bishop | Pestle: Recipe Manager (1574776971) | https://pestlechef.app/terms | food-drink | small | R2 |
| S4 | Maximilian Munker | Onrise (1547137474) | https://onrise.me/terms-conditions.html | productivity | small | R2 |
| S5 | Ori App Studio GmbH | TravelSpend (1434284824) | https://travel-spend.com/terms/ | travel | small | R2 |
| S6 | Lightpage, Inc. | Lightpage (6502964348) | https://lightpage.com/terms/ | health-fitness | small | R2 |
| S7 | Michal Dobrzanski | Planter (1564440923) | https://plantermobile.com/terms-and-conditions/ | lifestyle | small | R2 |
| S8 | Krzysztof Nowak | Diarly (1387167765) | https://diarly.app/terms-and-conditions | health-fitness | small | R2 |
| S9 | Have a nice day e.U. | ScanMe (1480368456) | https://appscanme.com/terms.html | business | small | R2 |
| S10 | Spine Revolution UAB | Wordletic (6760678675) | https://wordletic.com/en/terms-and-conditions | education | small | R2 |
| S11 | Serandi systems LTD | PenToPrint (1308003011) | https://www.pen-to-print.com/terms/ | productivity | small | R2 |
| S12 | Wergames OU | Amber: Photo Editor (6563149597) | https://amberfilmapp.com/terms-conditions | photo-video | small | R2 |
| S13 | Hammer Media LLC | Dollarwise (6739215932) | https://dollarwise.com/terms-of-use | finance | small | R2 |
| S14 | Star Focus, Inc. | EveryDoggy (1488080064) | https://everydoggy.com/terms/ | lifestyle | small | R2 |
| S15 | Matthew/Going Merry LLC | Plain Flashcards (971833934) | https://goingmerry.xyz/terms-conditions | education | small | R2 |
| S16 | Mo Meditation Inc. | Mo Meditation (1570156834) | https://momeditation.app/terms-of-use | health-fitness | small | R2 |
| S17 | Culi, Inc. | Zest (1595938390) | https://zestapp.co/terms | food-drink | small | R2 |
| S18 | Devenyi Gabor | Gymaholic (648518560) | https://www.gymaholic.app/termsofuse.html | health-fitness | small | R2 |
| S19 | Anastasia Naumkina | Pencora (6790469095) | https://pencora.app/terms/ | education | small | R2 |
| S20 | Amarok Technologies Inc. | Dog Assistant (1479477230) | https://www.dogassistant.io/terms-and-conditions | lifestyle | small | R2 |

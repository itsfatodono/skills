# refund-policy pool: r2-tail

Route R2 (App Store long tail), US storefront (`us`), `https://itunes.apple.com/search?term=<kw>&entity=software&country=us&limit=200` for the keywords pdf editor, habit tracker, language learning, workout planner, budget planner, photo editor, meditation, ai assistant, planner, scanner, markdown, journal. Only apps under 5,000 ratings were kept (about 1,590 distinct sellers); the search API does not expose in-app purchases, so price/IAP was not filtered and most rows are free apps with subscriptions. Documents were located via R4: a scripted probe of `/refund`, `/refunds`, `/refund-policy`, `/legal/refund-policy`, `/policies/refund-policy` and similar on each seller URL, plus a homepage-link scan for hrefs containing refund/money-back; each URL was fetched and checked to be a refund-subject page. Sellers with no refund page were skipped (the large majority). Ratings column: `userRatingCount (App Store US)`; Genre is the App Store primary genre.

| Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
|---|---|---|---|---|---|---|
| Libros Media Limited | Rocket Languages | 597293943 | Education | 2559 (App Store US) | https://www.rocketlanguages.com/refund-policy | https://www.rocketlanguages.com |
| HyperLingua LLC | HyperLingua: Learn Languages | 6773765162 | Education | 122 (App Store US) | http://hyperlingua.app/refunds/ | https://hyperlingua.app |
| Alexey Nenastyev | Language Reactor - PlayLingo | 6743090216 | Education | 812 (App Store US) | https://playlingo.app/refund-policy | https://playlingo.app |
| Anuj Seth | Workouts+ HIIT Interval Timer | 585542275 | Health & Fitness | 2110 (App Store US) | https://parabolicriver.com/help/refunds/ | https://parabolicriver.com/workoutsplus |
| SPARKFUL INC. | Fortune City: Expense Tracker | 1172713884 | Finance | 4983 (App Store US) | https://sparkful.app/legal/refund-policy | https://sparkful.app/fortune-city |
| Greigh Studios LLC | FiHaven: Budget Planner | 6781084347 | Finance | 0 (App Store US) | https://fihaven.app/refunds | https://fihaven.app/ |
| Mo Meditation Inc. | Mo Meditation, Sleep, Recovery | 1570156834 | Health & Fitness | 2692 (App Store US) | https://momeditation.app/refund-policy | https://momeditation.app |
| sip and om LLC | Sip and Om Meditation | 1216664612 | Health & Fitness | 382 (App Store US) | https://www.sipandom.com/policies/refund-policy (blocked) | https://www.sipandom.com/ |
| Atif Qayyum Toor | Burrak AI Assistant | 6794853944 | Productivity | 0 (App Store US) | https://burrakai.com/refund-policy | https://burrakai.com |
| Burlac Mihail | Metis: Markdown Notes | 6785268461 | Productivity | 0 (App Store US) | https://www.empiricapps.com/refund | https://www.empiricapps.com/metis |
| Bravely Studios LLC | Markd.ly - Markdown Editor | 6768107092 | Productivity | 0 (App Store US) | https://bravely.dev/refund | https://bravely.dev/markdly |
| Crocopliers OU | MDViewer — Quick Markdown | 6809376439 | Developer Tools | 0 (App Store US) | https://getmd.ma/refund | https://getmd.ma |
| Evgeniya Vorontsova | 2 MD: Markdown File Converter | 6801185846 | Developer Tools | 0 (App Store US) | https://chat-downloader.com/refund/ | https://chat-downloader.com/markdownconverter-site/ |
| Trade Like A Pro SRL | SuperTrader: Trading Journal | 1601101836 | Finance | 1205 (App Store US) | https://supertrader.me/refund | https://www.supertrader.me |
| FOXIT SOFTWARE INCORPORATED | Foxit PDF Editor | 507040546 | Productivity | 4761 (App Store US) | https://www.foxit.com/support/refund-policy/ | https://www.foxit.com/pdf-editor/ |
| Ivan Marzan | PDF Scanner, Editor, Converter | 1619135136 | Business | 2445 (App Store US) | https://scannerapp.xyz/refund | https://scannerapp.xyz |
| Gototop LTD | Habio - Daily Habit Tracker | 1517360968 | Health & Fitness | 3931 (App Store US) | https://terms.habio.app/applabel/money-back-policy | https://habio.app/ |
| Coachify.AI Inc. | Coachify AI: Workout Planner | 6449539939 | Health & Fitness | 2011 (App Store US) | https://coachify.ai/money-back | https://coachify.ai |
| AI Workout Planner Apps LTD | Fitny - Stretching & Fitness | 6474268576 | Health & Fitness | 2484 (App Store US) | https://fitny.app/refund-policy | https://fitny.app |
| Hotbot Limited | HotBot: AI Chat & Assistant | 6737478660 | Productivity | 0 (App Store US) | https://www.hotbot.com/terms#refund (combined) | https://www.hotbot.com |
| Anders Borum | Git client - Working Copy | 896694807 | Developer Tools | 3788 (App Store US) | https://workingcopy.app/refund.html (store-pointer) | https://workingcopy.app/ |
| Teleprompter LLC | Markdown゜ | 1494902837 | Productivity | 501 (App Store US) | https://www.teleprompter.com/refund-policy | http://matekovacs.com |

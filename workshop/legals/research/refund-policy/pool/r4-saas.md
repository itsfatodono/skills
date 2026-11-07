# refund-policy pool: r4-saas

Route R4 (company site), global run, English. Large and mid-size companies that sell software subscriptions or digital services on the web (productivity and collaboration, creative and AI tools, games and platform stores, learning, wellness, password/privacy, cloud, e-commerce plans). Companies were taken from my own knowledge, then each refund page was found by guessing the company's help-center or legal paths and by web search (`<company> refund policy`), and every Document URL was fetched with `curl -sL -A "Mozilla/5.0"` and checked for the refund text. Companies already in r1-grossing-prod and r4-software were skipped. `(combined)` marks a Terms of Service page with a distinct refund section; `(help)` a help-center article; `(blocked)` a page that returned 403 or a bot wall to curl (URL taken from search results); `(store-pointer)` a refund page that mostly sends app-store buyers to Apple or Google. No app column data: App `—`, Store id `—`. Ratings `—`. Rejected after checking (no refund page found or 404): Zoom, Slack, Figma, Duolingo, Babbel, Peloton, Spotify, Tinder, Bumble, Hinge, Semrush, Ahrefs, Hostinger, Kinsta, WP Engine, malware/VPN vendors that blocked or timed out.

| Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
|---|---|---|---|---|---|---|
| Microsoft | — | — | productivity | — | https://support.microsoft.com/en-us/accounts-billing/subscriptions/microsoft-subscription-refund-policy (help) | https://www.microsoft.com |
| Notion | — | — | productivity | — | https://www.notion.com/help/refunds (help) | https://www.notion.com |
| Dropbox | — | — | productivity | — | https://help.dropbox.com/plans/refund (help) | https://www.dropbox.com |
| Adobe | — | — | graphics-design | — | https://helpx.adobe.com/account/individual/terms-policies-and-regulations/adobe-subscription-terms-refund-policies-california.html (help) (blocked) | https://www.adobe.com |
| Valve (Steam) | — | — | games | — | https://store.steampowered.com/steam_refunds/ | https://store.steampowered.com |
| Epic Games | — | — | games | — | https://www.epicgames.com/help/en-US/epic-accounts-c74/receipts-and-purchases-c75/what-is-epics-refund-policy-a3085 (help) (blocked) | https://www.epicgames.com |
| Nintendo | — | — | games | — | https://www.nintendo.com/us/refund-return-policy/ | https://www.nintendo.com |
| Sony (PlayStation) | — | — | games | — | https://www.playstation.com/en-us/legal/terms-of-service/ (combined) | https://www.playstation.com |
| Setapp (MacPaw) | — | — | productivity | — | https://setapp.com/refund-policy | https://setapp.com |
| LinkedIn | — | — | social-networking | — | https://www.linkedin.com/help/linkedin/answer/a1337140 (help) | https://www.linkedin.com |
| Paddle | — | — | b2b-saas | — | https://www.paddle.com/legal/refund-policy | https://www.paddle.com |
| Midjourney | — | — | graphics-design | — | https://docs.midjourney.com/hc/en-us/sections/27646307671309-Cancellations-Refunds (help) (blocked) | https://www.midjourney.com |
| Skillshare | — | — | education | — | https://help.skillshare.com/hc/articles/204536798 (help) (blocked) | https://www.skillshare.com |
| Headspace | — | — | health-fitness | — | https://help.headspace.com/hc/en-us/articles/115013837848-I-purchased-my-subscription-via-the-Apple-App-Store-and-I-want-a-refund-What-can-I-do (help) (store-pointer) (blocked) | https://www.headspace.com |
| Coursera | — | — | education | — | https://www.coursera.org/about/terms (combined) | https://www.coursera.org |
| ElevenLabs | — | — | productivity | — | https://elevenlabs.io/terms-of-use (combined) | https://elevenlabs.io |
| Shopify | — | — | e-commerce | — | https://www.shopify.com/legal/terms (combined) | https://www.shopify.com |
| Proton | — | — | utilities | — | https://proton.me/legal/terms (combined) | https://proton.me |
| Squarespace | — | — | website-builder | — | https://www.squarespace.com/terms-of-service (combined) | https://www.squarespace.com |
| ClickUp | — | — | productivity | — | https://clickup.com/terms (combined) | https://clickup.com |
| Strava | — | — | health-fitness | — | https://www.strava.com/legal/terms (combined) | https://www.strava.com |
| Cloudflare | — | — | b2b-saas | — | https://www.cloudflare.com/terms/ (combined) | https://www.cloudflare.com |

# dsar-tail: small-company long tail (R2 us and gb, R4, web search)

Collected 2026-10-27. Method:
- **R2.** About 95 keyword searches (`itunes.apple.com/search`, `entity=software`, `limit=200`, storefronts us and gb) kept sellers with 200–30,000 ratings: 5,540 distinct sellers, 4,900 with a seller URL.
- **R4, scripted.** For each seller site: homepage links matching dsar / data-request / privacy-rights / privacy-choices / ccpa, then the homepage's privacy-policy page and the links inside it that look like a request link. A page is kept when it loads (200), has a form (`<form>`/`<input>`), mentions access or delete and request or rights, and is under 20K characters of text. Hosts that fail rule 1 were dropped (DataRep, Termly, TrustArc, OneTrust, TrueVault, EDPO, Rakuten, Intercom's own form on a customer's row). Then every hit was fetched and read.
- **Web search.** 5 queries for small companies' own forms; 3 usable hits (Glyyd, Luzid, Adspark).
- **Yield is low.** About 1 seller in 400 publishes a readable request form; most small apps give an email address in the policy. Rows below are what survived. Size is not judged here.
- Skipped developers already in `dsar-us.md` / `dsar-eu-uk.md`: Take-Two group (Gram Games, Zynga, Popcore, Rollic), Dave, Crunch.

| Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
|---|---|---|---|---|---|---|
| You Need A Budget LLC | YNAB | 1010865877 | Finance | 61988 ratings (us) | https://www.ynab.com/privacy-policy/data-subject-rights-request | https://www.ynab.com |
| Astrocenter.com (Astrology.com) | Astrology Plus | 327586041 | Lifestyle | 6551 ratings | https://www.astrology.com/us/privacy-request.aspx | https://www.astrology.com |
| Jam City, Inc. | Genies & Gems: Puzzle & Quests | 1032443533 | Games | 18045 ratings | https://support.jamcity.com/privacyrequest/ | https://www.jamcity.com |
| Grow Care, Inc. | Grow Therapy | 6744416231 | Health & Fitness | 10923 ratings | https://growtherapy.jotform.com/240836997526068 | https://growtherapy.com |
| CBC Restaurant Corp | Corner Bakery Cafe | 783177433 | Food & Drink | 2351 ratings | https://cornerbakerycafe.com/my-privacy-choices/ | https://cornerbakerycafe.com |
| Hatch Baby Inc. | Hatch Sleep | 1158048301 | Health & Fitness | 364 ratings (gb) | https://www.hatch.co/subject-rights-requests (blocked) | https://www.hatch.co |
| Waking Up Course, LLC | Waking Up: Meditation & Wisdom | 1307736395 | Health & Fitness | 7215 ratings | https://www.wakingup.com/your-privacy-choices | https://wakingup.com |
| Glyyd | (web) | | | | https://glyyd.com/privacy/data-subject-request | https://glyyd.com |
| Luzid (now Glasslake) | (web) | | | | https://www.luzid.io/data-subject-request | https://www.luzid.io |
| Adspark (Philippines) | (web) | | | | https://www.adspark.ph/data-subject-request (form is a fillable PDF: https://d15fzhw4120coi.cloudfront.net/media/data-subject-request-form.pdf) | https://www.adspark.ph |

## Notes per row

- **YNAB:** full DSR web form (on behalf of / relationship, name, email, country and US state of residence). Request types not fully read. Note the lookup count (61,988) is above the sweep's 30K cap because the gb storefront returned 3,001.
- **Astrology.com:** form with a request-type select (request your data, delete account data, correct account data), name, email, details. Readable.
- **Jam City:** form with email and game select; text offers access and erasure, plus opt-out of targeted advertising.
- **Grow Therapy:** Jotform-hosted "Individual Rights Request Form" under the company's own Jotform sub-domain, linked from its privacy policy (not seen linked from the listing; found by R4 on the site).
- **Corner Bakery Cafe:** right-to-know, access, correct, delete, restrict automated decisions, opt-out; country and state selects. A restaurant chain, not an app company.
- **Hatch:** the page embeds `https://my.datasubject.com/VBAKNbtknW/58374`, a vendor form that shows "You need to enable JavaScript". Wayback will be needed; not tried.
- **Waking Up:** a "Your Privacy Choices" form whose text covers state opt-out rights (sale, sharing, targeted ads, profiling) only; no access or delete types seen. Check the type list before extracting.
- **Glyyd:** the page text lists the request types (access, correct, delete, opt out, privacy complaint) and has a country select; the form fields are rendered by JavaScript, so there are no `<input>` names in the HTML.
- **Luzid:** B2B company with no app; form fields read in the HTML (region, relationship, request type with 8 options). The page says Luzid is now Glasslake.
- **Adspark:** a company with no app; the page is a three-step guide with a download link to a fillable PDF form. The PDF itself was not opened.

## Seen and not kept

- **Opt-out only (not a rights request form):** HER (weareher.com/your-privacy-choices, "do not sell my data"), Hooked on Phonics (do-not-sell, one email field), BoomHits (do-not-sell instructions), Hily (generic contact form with a "privacy issue" subject), BlackGentry (California notice, no form).
- **Email-only instructions:** MobilityWare (`/privacy-rights/`), Rapchat (`/privacy-choices`), Dope Capybara (`/data-deletion`).
- **Not the company's own form (rule 1):** Knowt, Zerion and Stone Street Coffee point to EDPO, Intercom's own form and Rakuten; Move With Us, Torrent Cycle (Arketa platform), SafeApp (Termly), Hatch's vendor shell is kept above only because it is the company's own linked page.
- **Large, left for the other slices to judge:** Bauer Media SAR form (`bauerlegal.co.uk`, form text not in HTML), Saxo Bank, Cheesecake Factory, Specialized, Yelp, Plaid.
- **Fetch gave no form text:** BitPay `/inc/legal/exercise-your-rights` (page text only, no fields), Sprout Social do-not-sell, Lex (CCPA notice only), Flipd (policy article).

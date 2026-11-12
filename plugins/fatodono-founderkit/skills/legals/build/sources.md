# Sample sources

Where the build branch finds samples. `build/build.md` step 1 fills its pool from *Candidates*,
*Routes* and *Documents*; `build/build-form.md` step 2 sets `source` from *Forms*. The template
(22) takes its text from the issuer per `build/build-template.md`. The tasks (24, 25, 37, 42, 43,
44, 50, 52, 53, 66, 68, 73) take their values from the authority per `build/build-task.md`.
Item numbers are those in `helpers/catalog.md`. Routes were checked on 2026-10-26.

## Candidates

A candidate qualifies when all of these hold:

1. **Own document.** It is the company's own text for its own product. It is served from the
   company's domain, its store listing, its trust center, or a file host (CDN, Notion, GitHub
   Pages) that those pages link to.
2. **Current.** It is the version reached from the company's live pages at fetch time. When the
   live page blocks fetching (403, bot wall), use the latest Wayback capture and record the
   capture URL. When `wayback/available` finds none for the URL, search the CDX index
   (`web.archive.org/cdx/search/cdx?url=<prefix>/*`), which lists every capture under a path.
3. **Target language.** Judged by the document's own text, not the page around it (an English
   page may link records in another language). `global`: English. A region run: the languages in the region's
   `region.md`. If the site has a language switcher, take that version. Sites redirect by the
   fetcher's location: `global` takes the default English version (`en-us` where the site
   splits by locale), a region run the region's version. Record the version taken.
4. **One text, one sample.** Templates and generated texts (Termly, iubenda, a platform's
   default contract) are valid samples: companies publish them and live with them. Samples
   whose whole text is the same count once: keep the first in pool order and record the others
   as copies of it in `research/<doc-id>/README.md`. Nobody searches for template sources;
   copies show up when the build merges the extraction tables (same headings in the same
   order, same quotes). A sample that shares only some sections with another stays a sample.
   A known template with parts removed counts as its own sample for prevalence but adds no
   patterns. A template's wording adds to patterns once, however many samples carry it, whole
   or as a block inside own text.
5. **One per group.** At most one candidate per company group per `doc_id`. Check groups when
   selecting the pool, before any extraction: brands of one owner (a retail holding's chains)
   are one group, and so are the colleges of one university.
6. **Right document.** A page that combines documents (privacy + cookies) qualifies when it has
   a distinct part for this `doc_id` that says more than one sentence; only that part is
   extracted, and when the topic is spread over several sections, all of them are. A part
   that is one sentence or a pointer ("see our Refund Policy") is followed to the page it
   names, and that page is the sample. A document split over sub-pages that one hub page
   links, or published as many files (a register with one file per activity), is one sample:
   the hub or index plus its parts; for many files, the index and three files.

Law-firm articles and template marketplaces (Law Insider, Rocket Lawyer, terms.law) are never
samples. Standard forms count only as *Few public samples* says.

**Sector.** Use the App Store primary category of the company's main app, lowercased and
kebab-cased (`productivity`, `shopping`, `health-fitness`, `finance`). For a company without
an app, use `b2b-saas`, `developer-tools` or `e-commerce`. If none of those fits, use the App
Store category its main product would take. Two values are reserved for alternative sources:
`public-sector` (government bodies, universities) and `standard-form`.

**Size.** Estimate the headcount from what you already know and the data in hand; never
research it. A wrong guess is fine, because size only keeps the pool mixed. More than 500 is
**large**, 51–500 is **mid**, 50 or fewer is **small**.

`standard-form` samples take `size: none` and are left out of the size thirds.

**Pool order.** Write `candidates.md` rotating size (large, mid, small) and sector, so that the
first batch of 15 is already mixed. A route's output order (chart rank) is not the pool order.

**Exhausted.** A pool counts as exhausted only after every route listed for the item in
*Documents* has run. Record the routes run in `research/<doc-id>/README.md`.

## Routes

| id | Route | How to run it |
|---|---|---|
| R1 | App Store charts | `https://itunes.apple.com/<cc>/rss/<feed>/limit=100/genre=<id>/json`. `feed` is `topfreeapplications`, `toppaidapplications` or `topgrossingapplications`. The genre id is the number in `https://apps.apple.com/<cc>/iphone/charts/<id>` (6007 Productivity, 6024 Shopping). The listing `https://apps.apple.com/<cc>/app/id<id>` shows *Developer Website*, *Privacy Policy*, and *License Agreement* (custom EULA only). `https://itunes.apple.com/lookup?id=<id>&country=<cc>` (or `bundleId=`) gives `sellerName`, `sellerUrl`, `primaryGenreName` and `userRatingCount`. |
| R2 | App Store long tail | `https://itunes.apple.com/search?term=<keyword>&entity=software&country=<cc>&limit=200`. Most results have under 1K ratings, so this is the route to small companies. |
| R3 | Play charts | `https://play.google.com/store/apps/category/<CATEGORY>?hl=<lang>&gl=<cc>` shows top free, paid and grossing. The listing `details?id=<pkg>` shows downloads; *App support* (Website, Support email, Privacy Policy); and *About the developer* (address, phone). |
| R4 | Company site | From the homepage, follow footer links and help-center articles. Try `/legal`, `/terms`, `/privacy`, `/cookies`, `/security`, `/subprocessors`, `/dpa`, `/sla`, `/aup`, `/accessibility`, `/brand`, `/impressum`. Then web-search `site:<domain> "<document title>"`. |
| R5 | Trust centers | `trust.<domain>` (SafeBase, Vanta, Whistic, Conveyor), e.g. `trust.openai.com`, `trust.linear.app`, `trust.zapier.com`. They publish subprocessors, the DPA, security overviews and sometimes a CAIQ. |
| R6 | Security contacts | `https://<domain>/.well-known/security.txt`: its `Policy:` field (RFC 9116). `program-list.json` in `github.com/disclose/diodb` (about 2,400 programs) gives `policy_url` and `securitytxt_url` per program. |
| R7 | Public registries | CSA STAR registry, with CAIQ downloads: `cloudsecurityalliance.org/star/registry/`. Registries kept under one region's law are in that region's `region.md`. |
| R8 | SEC EDGAR | Use `https://efts.sec.gov/LATEST/search-index?q="<title>"&forms=S-1,10-K,10-Q,8-K&startdt=<date>&enddt=<date>` (JSON; send a `User-Agent` header). The UI is `https://www.sec.gov/edgar/search/#/q=...`. Keep hits whose `file_type` starts with `EX-10`. The filer's 10-K states its headcount. |
| R9 | Standard forms | Common Paper: `commonpaper.com/standards` (CC BY 4.0). Bonterms: `bonterms.com/download-center/` (CC BY 4.0). oneNDA/oneDPA: `onenda.org` (CC BY-ND 4.0). Cooley GO: `cooleygo.com/documents/`. NVCA: `nvca.org/model-legal-documents/`. UK Private Capital (formerly BVCA): early-stage model documents (free account). |
| R10 | Public bodies | The European Commission's register of records of processing: `ec.europa.eu/dpo-register/` (JS app). The EDPS and other EU bodies publish theirs as PDFs. GOV.UK search API: `https://www.gov.uk/api/search.json?q="<title>"`. Dutch SLM Rijk DPIAs: `rijksoverheid.nl` › strategisch leveranciersmanagement (Microsoft, Google, AWS, Zoom). Universities: `"<title>" site:ac.uk filetype:pdf`, `"<title>" site:edu filetype:pdf`, then walk each university's data-protection pages, which link records these searches miss. |
| R11 | Regulator models | ICO documentation (RoPA) templates and DPIA template (`ico.org.uk`, guide to accountability). CNIL `registre-traitement-simplifie.ods` and the PIA tool (`github.com/LINCnil/pia`). SANS policy templates: `sans.org/information-security-policy`. CISA VDP template. GOV.UK sample accessibility statement. |
| R12 | GitHub code | `gh api "search/code?q=filename:<file>+<key>"`. Keep a repo only when it is an app with a live store listing: a README link, or the bundle id resolving through the R1 lookup. |

**Scripted R4.** For a document with a predictable link or path, a collector may script R4
across many developer sites: footer links containing the document's keyword first, then the
common paths; a page is kept when it loads and names the subject several times. A fallback
section inside a combined page is marked as a rule-6 candidate, for the extractor to confirm.
The slice file's header records the method and thresholds (see
`research/cookie-policy/pool/charts-us.md`: 1,317 sites scanned, 238 rows).

## Documents

| Items | Routes | Expected pool |
|---|---|---|
| A: 1–9 (privacy, terms, EULA, subscription, refund, cookies, deletion, OSS notices, contact) | R1–R3 → R4 | ≥30. EULA: listings with a *License Agreement* link, plus desktop software. An EULA sample's core is a licence grant for software the user installs; terms of use served at an EULA link are a different document. Subscription and refund: `topgrossing` feeds; refund pages come mostly from R4 and R2, R1 yields few. Deletion: Play's Data safety section does not show the deletion URL, so find it through R4. |
| 13 request form, 16 children | R1–R4. 13: privacy-policy "exercise your rights" links. 16: Kids category charts. | ≥30; 13 ≥20 |
| 17 sub-processors, 63 customer DPA, 64 SLA, 61 MSA | R5, R4 at B2B SaaS, R8 | ≥30 for 17, 63 and 64. ≥20 for 61 (public customer agreements). |
| 45 AUP, 46 community guidelines, 47 copyright policy | R1–R4 at social and UGC apps. | ≥30 |
| G: 54 disclosures, 55 newsletter notice | 54: R4 at companies with affiliate or creator programs. 55: R4 newsletter signup forms. | ≥20 |
| H: 56 AI disclosure, 57 accessibility, 58 disclaimers, 59 beta terms, 60 VDP | 56: R4 at AI-feature apps. 57: R4 `/accessibility`, plus public-sector statements (R10). 58: R1/R3 Health & Fitness, Medical and Finance charts. 59: `"beta terms"` web search. 60: R6. | ≥30 for 57 and 60, ≥20 for the rest |
| 65 security whitepaper / questionnaire | R5, R7 CSA STAR CAIQs | ≥30 |
| 74 brand guidelines | R4 `/brand`, `/media-kit`, trademark policy pages | ≥30 |
| C: 18–21, 23; I: 62, 67; J: 69–72 | *Few public samples* | per that section |

## Few public samples

Alternative sources count as samples on these terms:

- **Public-body documents (R10)** are full samples: sector `public-sector`, size by headcount.
- **EDGAR exhibits (R8)** are full samples. Sector and size come from the filer.
- **Standard forms and regulator models (R9, R11)** are `standard-form` samples. Each project
  or regulator counts once per `doc_id`, and they make up at most one in four samples; for an internal document (family
  `internal-compliance`), at most half, since companies never publish their own.
- **Exception:** for an internal document whose pool runs out with more models than real
  records, regulator and association models may pass that half; keep them all and say so in
  the skeleton's header.

| Item | Sources | Expected |
|---|---|---|
| 18 RoPA | R10 EU registers, R11 ICO/CNIL models | ≥20 |
| 20 DPIA | R10 GOV.UK, SLM Rijk, EU bodies; R11 ICO, CNIL | ≥20 |
| 21 breach procedure, 23 InfoSec policy | R10 universities and public bodies, R11 SANS | ≥20 |
| 62 Order Form | R9 Common Paper and Bonterms cover pages, R8 `"Order Form"`, R4 sample order forms | <20 |
| 67 NDA | R9 (Common Paper, Bonterms, oneNDA, Cooley GO, NVCA), university mutual CDAs (`"mutual CDA" site:edu`), R8 | ~20 |
| 69 Founders' / shareholders' agreement | R8 stockholders', shareholders' and voting agreements (EX-4, EX-9 and EX-10 exhibits), R9 SVCA founders' agreement, Seedcamp founder collaboration agreement, StartupTools shareholders' agreement, NVCA voting agreement, UK Private Capital shareholders' agreement (member login; use Wayback) | ≥20 |
| 70 IP assignment | R8 `"Proprietary Information and Inventions"` (hundreds of 10-K hits); R9 has no fetchable form (Cooley GO's CIIAA is a generator behind a bot wall) | ≥20 |
| 71 contractor agreements | R8 `"Consulting Agreement"`, R9 Common Paper Independent Contractor Agreement and PSA, Bonterms PSA | ≥20 |
| 72 employee notice | R10 university staff notices, plus R4 career pages ("candidate privacy notice") | ≥20 |

When the pool ends below 30 after every listed route has run, the build continues with what it
has and writes `saturated: false`, per `build/build.md` step 3.

Region runs take their routes from `regions/<code>/region.md` *Sources*, and so do items and
forms that exist under one region's law: they are listed there, not here.

## Forms

`sampled` when a public place shows per-app answers to the form's core questions; `official`
otherwise. A sampled form's pool comes from R1/R3 listings, or from R12 repos tied to a listing.

| # | Form | Answers public per app | Where | source |
|---|---|---|---|---|
| 26 | App Store Privacy Label | yes: data types by tracking/linked/not linked, per purpose | listing › *App Privacy* (full detail is in the page HTML); some repos also commit `app_privacy_details.json` (R12) | sampled |
| 27 | Play Data safety | yes: shared and collected types, purposes, optional, encryption in transit, deletion request; not the deletion URL | `play.google.com/store/apps/datasafety?id=<pkg>` | sampled |
| 28 | Privacy manifest | yes, open-source apps only | R12 `filename:PrivacyInfo.xcprivacy`; most hits are libraries, so filter | sampled |
| 29 | Permission usage strings | yes, open-source apps only | R12 `filename:Info.plist NS<…>UsageDescription` | sampled |
| 30 | ATT prompt | yes: prompt text in repos; whether the app tracks on the listing | R12 `NSUserTrackingUsageDescription`; listing › *Data Used to Track You* | sampled |
| 31 | Age rating (Apple, IARC) | partly: rating plus descriptors | Apple listing › *Age Rating* (Frequent/Infrequent descriptors; "Contains" Advertising, Messaging and Chat, User-Generated Content…). Play listing: rating, descriptors, interactive elements. | sampled |
| 32 | Play Target Audience & Content | no; the Data safety page shows only a "Play Families Policy" badge | — | official |
| 33 | Play Ads declaration | yes | Play listing "Contains ads" label | sampled |
| 34 | Encryption / export compliance | partly: the non-exempt-encryption answer, open-source apps only | R12 `ITSAppUsesNonExemptEncryption` | sampled |
| 36 | Play special declarations | no | — | official |
| 38 | App Review notes, demo account | yes, open-source apps only; expect a pool under 20 | R12 `filename:notes.txt path:fastlane/metadata/review_information`, `filename:demo_user.txt` | sampled |

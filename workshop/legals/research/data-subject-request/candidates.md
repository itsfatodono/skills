---
doc_id: data-subject-request
built: 2026-10-27
routes_run: [R1, R2, R4]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (3 slices: `dsar-us` R1 storefront us, then R4 on each
listing's privacy policy; `dsar-eu-uk` R1 storefronts gb and ie, then R4, plus EU/UK company
sites; `dsar-tail` R2 storefronts us and gb, then R4, plus 5 web searches for small companies'
own forms). This is the root run (PLAN.md decision 49): a region-neutral root with a global pool.
The `tr`, `eu` and `uk` blocks are built later. The document is the form or request page a
person uses to submit a data-protection rights request. A privacy-policy section that only
describes rights is not this document. Size is an estimate per `sources.md` and was not
researched.

**Short: 24 of 30 (10 large, 10 mid, 4 small).**
- **Small (4 of 10).** The first two slices had almost no small companies. Cal AI and Pi point
  to DataRep's generic form, Ebby Halliday to HomeSpotter's form, and both fail rule 1.
  Wellspring Meds (TrueVault), Blossom (Termly) and Home Store + More (Zendesk) are blocked,
  and there is no recipe for them. The long-tail slice `dsar-tail` (R2 over about 5,540
  sellers with 200–30,000 ratings, plus web search) found about 1 seller in 400 with a
  readable request form; most small apps give only an email address in the policy. Of its 10
  rows, 3 are small by estimate. Glyyd (c22) and Luzid (c23) pass; Waking Up is opt-out only
  (*Left out*). The other 7 rows are mid or large (judged below).
- **Mid (10 of 10).** Filled by Grow Therapy (c24) from the tail slice. The other valid mid
  rows from it (Adspark, Astrology.com, YNAB) go to *Reserve*. Bitcoin.com (M1) stays in
  reserve: mid is full.
- **Tail sizes, estimated (not researched).** Collector hints were checked, not taken as-is.
  - YNAB: mid (~200 staff; 61,988 ratings is reach, not headcount).
  - Astrology.com (Astrocenter): mid (~100).
  - Jam City: large (~700+ staff, several studios).
  - Grow Therapy: mid (~400–500), as the collector thought.
  - Corner Bakery Cafe: large, not mid as the collector thought. It runs ~180 cafés, so
    restaurant staff put it in the thousands.
  - Hatch: mid (~200).
  - Waking Up: small (~30–50).
  - Glyyd: small (~5–15; rowing-analytics startup in beta).
  - Luzid (now Glasslake): small (~20–40).
  - Adspark: mid (~100–200; Globe Telecom group's digital agency, PH).
- Record the small shortfall in `README.md`.

**Home-region mix.** 15 US and 9 EU/UK. The EU/UK rows have no mid or small companies, so all
9 of them sit in the large third. That leaves one US large company (OpenAI). The other US
large companies (Home Depot, Taco Bell, Take-Two and others) are first in *Reserve*. The
`eu`/`uk` blocks get GDPR and UK GDPR forms from 9 samples, 4 of them in the first batch. The
two small additions are estimated as US. Neither page names a country, but Luzid's policy
says it is not established in the EU or UK and names an Article 27 representative. Both
accept requests from any country (Luzid lists EU/EEA, UK and Brazil). The only non-US,
non-EU/UK row is Adspark (PH, reserve M3).

**Vendor (owner cap: at most a third of picks per portal vendor).**
- 7 of 24 run on OneTrust: c08, c11, c12, c16, c18, c19, c20. The cap is 8 of 24, so there is
  room for one more OneTrust row, and only one. At 30 picks the cap becomes 10.
- 1 runs on Transcend (c04).
- 1 runs on Jotform (c24), on the company's own Jotform sub-domain and linked from its privacy
  notice.
- 15 are the company's own form: 14 web forms and 1 PDF (c21).
- Recipes are in `plugins/fatodono-founderkit/skills/legals/helpers/sample-extractor.md` step 1 and `portal-probe.md`. On
  2026-10-27, all 26 OneTrust URLs in the pool (24 blocked rows, plus Aldermore and Philips,
  found behind open rows) returned a `/publish` entry. GEICO needs its `reDirectUrl` hop.
  OpenAI is read from Wayback (latest capture 2026-06-04, `privacyCenterSubjects.json`).

**Group check (rule 5), done at selection.**
- JD Sports and DTLR share one OneTrust org (`9c661b24`); JD bought DTLR. Taken once, as JD
  Sports.
- Virgin Media and O2 are both Virgin Media O2. Taken once, as Virgin Media.
- Rows taken once only: WeChat (one row per slice), Experian (US and UK), Rollic (a Take-Two
  studio, so the row is Take-Two's group form), Allianz UK / LV=, EE (BT Group).
- Tesco Bank's banking arm went to Barclays in 2024. Barclays is dropped (below), so Tesco Bank
  stays in reserve. If one of them comes back, only one may be used.
- TSB is being bought by Santander. Santander Consumer UK is blocked (bot wall), so there is no
  conflict.

**First-screen check (`build.md` step 1), done 2026-10-27.** Every picked URL was fetched with
curl, and its title and first screen read. OneTrust and Transcend rows were checked through
their form JSON (welcome text and request types). The fetcher sits in Turkey, so some sites
redirected to a TR locale. The checks were read in English.

**Tail rows, checked 2026-10-27** (curl, then title, first screen and form fields read).
All 10 URLs returned 200.
- Glyyd: the request-type select is in the server HTML (download my data, who accessed my
  data, correct, delete or anonymize, object, opt out of sale or sharing, other or complaint),
  with a country select and an authorized-agent box. The collector's "rendered by JavaScript"
  no longer holds.
- Luzid: a plain form. It has region, relationship and 8 request types (access, delete,
  correct, restrict, portability, object, withdraw consent, other). It carries a "Luzid is now
  Glasslake" banner, but the page is the live one (rule 2).
- Grow Therapy: "Individual Rights Request Form". It has relationship and 7 rights (access and
  portability, know, correct, withdraw consent or restrict, delete, profiling, opt out of
  sale).
- Waking Up: opt-out only (sale, sharing, targeted ads, profiling); no access, correct or
  delete type. Under this file's document definition it is the same case as Crunch and
  Prosper, so it is dropped.
- Adspark: a three-step page plus a fillable PDF on its CloudFront host. The PDF opened, and
  its request types are access, correct, erase, object and portability, under the Philippine
  Data Privacy Act.
- Hatch: the page body is a `my.datasubject.com` embed that needs JavaScript. There is no
  recipe for it (Wayback not tried).
- YNAB, Astrology.com, Corner Bakery and Jam City: readable forms. Jam City's form takes access
  and erasure only and sends opt-outs to a separate page.

Pool order rotates size and sector. The *Order* column below is the pool order. For the first
15, the sample id is `s` + the order number.
- **First batch: c01–c12, then the top-up s13–s15.** c01–c12 are 5 large, 5 mid and 2 small.
  The top-up is:
  - s13 = c22 Glyyd (small).
  - s14 = c23 Luzid (small).
  - s15 = c13 Bolt (large). Only 2 small tail rows are valid, so the third slot falls back to
    c13.

  The first batch is then 6 large, 5 mid and 4 small (all 4 small picks); the main session
  decides whether that holds. Small and large spares do not exist: a small pick that drops out
  has no same-size replacement.
- **Saturation (batches of 5, in this order):**
  - Batch 1: c14 Nav (M), c15 Vodafone UK (L), c24 Grow Therapy (M), c19 Philips (L), c16
    Transcarent (M).
  - Batch 2: c17 Virgin Media (L), c18 TaxAct (M), c21 Co-op (L), c20 Stadium Goods (M).
  - No small picks are left after the first batch, so batches alternate mid and large. Mid
    leads because the first batch is large-heavy. Sector also rotates, so batch 1 has finance,
    utilities, health-fitness, lifestyle and medical.
  - After c20, use *Reserve* (same size only).

| Order | # | Company | App (store id) | URL | Sector | Size | Base | Language | Vendor | Size evidence | Route |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | c01 | Booking.com | Booking.com Travel Deals (367003839) | https://www.booking.com/content/dsar.en-gb.html | travel | large | EU (NL) | en | own web form | ~20K staff; 1.3M ratings | R1 (gb), R4 |
| 2 | c02 | Dave, Inc | Dave: Credit, Cash & Money App (1193801909) | https://dave.com/ccpa-request/ | finance | mid | US | en | own web form | listed fintech, ~300 staff | R1, R4 |
| 3 | c03 | Copilot Money, Inc. | Copilot: Track & Budget Money (1447330651) | https://www.copilot.money/consumer-request-webform | finance | small | US | en | own web form | small app company, ~30–50 staff; 31K ratings | R1, R4 |
| 4 | c04 | OpenAI OpCo, LLC | ChatGPT (6448311069) | https://privacy.openai.com/ (Wayback 2026-06-04: `web.archive.org/web/20260604162123id_/https://privacy.openai.com/static/privacy.openai.com/privacyCenterSubjects.json`) | productivity | large | US | en | Transcend | ~3K+ staff | R1, R4 |
| 5 | c05 | Timely Telehealth, LLC | TimelyCare Health & Well-being (1502432982) | https://timelycare.com/privacy-rights-request-form/ | medical | mid | US | en | own web form | telehealth company, ~300–500 staff | R1, R4 |
| 6 | c06 | Becausal, Inc. | ScanLife PowerShopper (285324287) | https://www.becausal.com/data-subject-requests | shopping | small | US | en | own web form | small data company; 401 ratings | R1, R4 |
| 7 | c07 | Automobile Association Developments | The AA (405476192) | https://www.theaa.com/help-support/data-subject-access-request | travel | large | UK | en | own web form | breakdown and insurance group, ~6K+ staff | R1 (gb), R4 |
| 8 | c08 | GPD Holdings, LLC (CoinFlip) | CoinFlip Crypto Wallet (6502452721) | https://privacyportal.onetrust.com/webform/36bdb9d1-f751-4a50-9ca1-e6a57e5f036c/49aaa221-9589-46fd-9101-d20e6c5b5dfd | finance | mid | US | en | OneTrust | crypto-ATM operator, ~200–400 staff | R1, R4 |
| 9 | c09 | Intercom | (web) | https://www.intercom.com/privacy-form | b2b-saas | large | EU (IE) | en | own web form | ~1K staff, Dublin/SF | R4 |
| 10 | c10 | 1stdibs.com | 1stDibs: Shop Antique & Modern (938157117) | https://www.1stdibs.com/info/forms2/california-consumer-privacy-act/ | shopping | mid | US | en | own web form | listed marketplace, ~250–300 staff | R1, R4 |
| 11 | c11 | JD Sports Fashion | JD STATUS (6449736895) | https://privacyportal.onetrust.com/webform/9c661b24-1df6-4962-8375-8dab4483ae39/7a82c8cc-0b5f-429c-b9de-74a244a15b41 | shopping | large | UK | en | OneTrust | listed retailer, 70K+ staff | R1 (gb), R4 |
| 12 | c12 | NHL Interactive Cyberenterprises, LLC | NHL Fantasy Stars (6744072431) | https://privacyportal.onetrust.com/webform/c48a335c-3316-4893-8bc6-fcacbf57fc4a/5b38eaa6-1ff7-462b-9f7e-e26b7d448b46 | sports | mid | US | en | OneTrust | league digital arm, ~200–400 staff | R1, R4 |
| 13 | c22 | Glyyd | (web) | https://glyyd.com/privacy/data-subject-request | sports | small | US (est.) | en | own web form | rowing-analytics startup in beta, ~5–15 staff | web search, R4 |
| 14 | c23 | Luzid (now Glasslake) | (web) | https://www.luzid.io/data-subject-request | b2b-saas | small | US (est.) | en | own web form | SAP-transformation startup, ~20–40 staff | web search, R4 |
| 15 | c13 | Bolt | Bolt: Request a Ride (675033630) | https://bolt.eu/en/privacy/data-subject/ | travel | large | EU (EE) | en | own web form | mobility company, ~4K staff; 178K ratings | R1 (gb), R4 |
| 16 | c14 | Nav Technologies, Inc | Nav Business Funding Roadmap (1139884313) | https://www.nav.com/privacy/ccpa-request/ | finance | mid | US | en | own web form | fintech, ~200 staff | R1, R4 |
| 17 | c15 | Vodafone UK | (web) | https://www.vodafone.co.uk/forms/static/gdpr-sars | utilities | large | UK | en | own web form | telecom operator, ~10K staff | R4 |
| 18 | c24 | Grow Care, Inc. (Grow Therapy) | Grow Therapy (6744416231) | https://growtherapy.jotform.com/240836997526068 | health-fitness | mid | US | en | Jotform | therapy-practice startup, ~400–500 staff; 10.9K ratings | R2 (us), R4 |
| 19 | c19 | Koninklijke Philips | (web) | https://www.philips.co.uk/c-e/privacy-request.html (form: https://privacyportal-de.onetrust.com/webform/415349a7-6194-4ac8-a922-31a9f8ef1b39/38e2998c-8432-4e1b-8063-a54f86824c86) | lifestyle | large | EU (NL) | en | OneTrust | listed group, ~65K staff | R4 |
| 20 | c16 | Transcarent, Inc. | 98point6 by Transcarent (1157653928) | https://privacyportal.onetrust.com/webform/dbb1e0a9-5dc2-4908-9125-990fb1894729/ec6eab84-cd95-4615-8652-90f299ae2c03 | medical | mid | US | en | OneTrust | health-benefits startup, ~400–600 staff | R1, R4 |
| 21 | c17 | Virgin Media (Virgin Media O2) | (web) | https://www.virginmedia.com/help/dsar | utilities | large | UK | en | own web form | telecom operator, ~15K staff | R4 |
| 22 | c18 | DS Admiral Bidco, LLC (TaxAct) | TaxAct Mobile (6755056246) | https://privacyportal.onetrust.com/webform/639512f3-cde9-4ef9-8392-da36efd85d4f/fb57339b-80d6-46f2-889d-b037ebe1f0c5 | finance | mid | US | en | OneTrust | tax-software company, ~300 staff | R1, R4 |
| 23 | c21 | Co-operative Group | (web) | https://assets.ctfassets.net/bffxiku554r1/6lGVbYHGWRCCMQKl1mnyBL/faa12375c1bbdfa546c198c264b46631/GDPR_SAR_Form_-_July_2023__3_.pdf | shopping | large | UK | en | own PDF form | retail co-operative, ~50K staff | R4 |
| 24 | c20 | Stadium Enterprises LLC (Stadium Goods) | Stadium Goods - Buy Sneakers (1288719040) | https://privacyportal-de.onetrust.com/webform/9bd9cc08-5003-449f-baca-5874242c6ade/7d242d58-9b8c-4a49-8e16-ddf40d9406f4 | shopping | mid | US | en | OneTrust | sneaker retailer, ~150–300 staff | R1, R4 |

**Sectors.** Finance and shopping 5 each; travel 3; medical, utilities, b2b-saas and sports 2
each; productivity, lifestyle and health-fitness 1 each. No sector is above a quarter of 24
(6). Glyyd has no app; its product is a coaches' sports-analytics tool, so it takes `sports`.

**EU/UK rows.** c01, c07, c09, c11 and c13 (first batch, c13 as s15), then c15, c19, c17, c21.

**Group check, tail rows.** No tail row shares a group with a pick or reserve. Jam City is
independent of Take-Two (L3). Adspark belongs to the Globe Telecom group, which has no other
row.

## Reserve

Used in this order, same size only, when a candidate drops out. The first-screen check and the
group check are done for every row. OneTrust (`OT`) is at 7 of 24, and the cap is 8. So one
non-OneTrust pick may be replaced by an `OT` reserve. After that, skip `OT` reserves when the
row being replaced is not on OneTrust.

| # | Company | App (store id) | URL | Sector | Size | Base | Vendor | Route |
|---|---|---|---|---|---|---|---|---|
| L1 | The Home Depot, Inc. | The Home Depot (342527639) | https://www.homedepot.com/privacy/Exercise-My-Privacy-Rights | shopping | large | US | own web form | R1, R4 |
| L2 | Taco Bell (Yum! Brands) | Taco Bell Fast Food & Delivery (497387361) | https://privacy.tacobell.com/ | food-drink | large | US | Transcend | R1, R4 |
| L3 | Take-Two Interactive (Rollic row) | Parking Order! (1667253521) | https://www.take2games.com/data-request/ (form in iframe) | games | large | US | own web form | R1, R4 |
| L4 | Ethan Allen (Intiaro row) | Ethan Allen inHome (1385071267) | https://privacy.ethanallen.com/consumer/ (the raw row's `/donotsell` is one request type of this portal) | lifestyle | large | US | Truyo | R1, R4 |
| L5 | Ryanair | Ryanair (504270602) | https://privacyportal-de.onetrust.com/webform/e12acd0a-fa4e-45df-999a-2d2066658f49/22fc437a-98d6-40a3-adef-5ed53e74d0ce | travel | large | EU (IE) | OT | R1 (gb), R4 |
| L6 | Bank of Ireland | Bank of Ireland Mobile Banking (520821023) | https://www.bankofireland.com/privacy/data-protection-notice/data-subject-rights/ | finance | large | EU (IE) | own web form | R1 (ie), R4 |
| L7 | Adyen | (web) | https://www.adyen.com/policies-and-disclaimer/privacy-form | b2b-saas | large | EU (NL) | Marketo form | R4 |
| L8 | Starbucks Coffee Company | Starbucks (331177714) | https://privacyportal.onetrust.com/webform/f9975fc5-c93f-4ff8-8169-846d8f6cd4d2/2e24ae7b-8edf-411f-a11d-14a16ddaa413 | food-drink | large | US | OT | R1, R4 |
| L9 | TSB Bank | (web) | https://www.tsb.co.uk/privacy/tsb-dsar-form.pdf | finance | large | UK | own PDF form | R4 |
| L10 | Crocs, Inc. | Crocs (1588314651) | https://privacyportal.onetrust.com/webform/83de35f2-0e1f-46c1-b853-5b776616e328/49efe979-5061-4080-9415-f46d3ea5e41f | shopping | large | US | OT | R1, R4 |
| L11 | EE (BT Group) | (web) | https://btprivacy.my.onetrust.com/webform/a0327856-31fc-4f51-b6d3-1c9e883e1ecf/c93b80f8-333b-4150-bf54-cce1e455207f | utilities | large | UK | OT | R4 |
| L12 | Ulta Beauty | Ulta Beauty: Makeup & Skincare (561930308) | https://privacyportal.onetrust.com/webform/8621deee-797a-4513-9df5-8f408f3caad9/5822e256-953c-4a59-a0b4-8115be5c3c5c | shopping | large | US | OT | R1, R4 |
| L13 | Tesco Bank | (web) | https://www.tescobank.com/assets/data-subject-access-request-application-form/data-subject-access-request-application-form.pdf | finance | large | UK | own PDF form | R4 |
| L14 | Simon & Schuster | Pimsleur (1405735469) | https://simon-privacy.my.onetrust.com/webform/42b48037-2185-4e2d-96d2-a4301bbc3f8a/b3c0395b-4ed8-404f-b14b-3d388bec653d | education | large | US | OT | R1, R4 |
| L15 | ManpowerGroup | My Manpower (1569784517) | https://privacy-portal-manpowergroup.my.onetrust.com/webform/1ef6af7e-5375-472f-9219-c7092454fa4f/draft/7b233c35-edb1-40ad-80a6-383cd8d826a5 | business | large | US | OT | R1, R4 |
| L16 | GEICO | GEICO Mobile (331763096) | https://privacyportal.onetrust.com/webform/3f71504a-d28e-4b48-9b8c-e803409ca65d/17574c5f-6ee0-4ad4-b11b-6b0fbf224811 (follow `reDirectUrl`) | finance | large | US | OT | R1, R4 |
| L17 | Allianz UK / LV= | (web) | https://privacyportal-de.onetrust.com/webform/6e169bd0-974f-447d-9d66-cbc7c16a4ace/0cdbfa11-f106-492d-828d-cd58307468d9 | finance | large | UK (DE group) | OT | R4 |
| L18 | Next Retail | NEXT (348364305) | https://next-privacy.my.onetrust.com/webform/ed3af7a2-8a20-4164-91fc-f042d4368382/1b3fa915-24a2-474a-b082-7d0943cc6aaa | shopping | large | UK | OT | R1 (gb), R4 |
| L19 | Nationwide Building Society | Nationwide Mobile Banking (542355130) | https://privacyportal-uk.onetrust.com/webform/1910e69e-c02c-4ecb-938d-a98166329b56/095cba51-20de-46d0-b107-4d25b9ca0727 | finance | large | UK | OT | R1 (gb), R4 |
| L20 | NatWest | NatWest Mobile Banking (334855322) | https://www.sars.natwestgroup.com/webform/2007c284-c892-42a4-b9f7-a09bc007c61f/639c6944-fd3d-47cf-9bf4-119812c8e6ba | finance | large | UK | OT | R1 (gb), R4 |
| L21 | Aldermore Bank | (web) | https://aldermoregroup-privacy.my.onetrust.com/webform/63221982-bc44-414a-acc2-3660e1366603/1d0f6ff8-64dc-4eb1-ab7d-ce746bb881a6 (linked from aldermore.co.uk/legal/data-subject-access-request) | finance | large | UK | OT | R4 |
| L22 | Coventry Building Society | (web) | https://privacyportal-uk.onetrust.com/webform/e35d0618-b837-4b42-bc6b-8e1adafaa8dd/2ab506fc-0609-4b95-880f-0782f4697491 | finance | large | UK | OT | R4 |
| L23 | 1st Source Bank | 1st Source Bank Mobile Banking (771775441) | https://www.1stsource.com/app/uploads/2022/10/Privacy-ccpa_request_form_06-22-1-003.pdf | finance | large | US | own PDF form | R1, R4 |
| M1 | Saint Bitts LLC (Bitcoin.com) | Bitcoin.com: Crypto Wallet (1252903728) | https://www.bitcoin.com/legal/dsar-form/ (embedded Google Form) | finance | mid | other (KN) | Google Forms | R1, R4 |
| M2 | Investor's Business Daily (News Corp) | MarketSurge (433822602) | https://privacyportal.onetrust.com/webform/8930e991-baac-4a05-89f0-fc400879fa8a/bdaf0a94-20d6-4a9a-82f3-3085b7cdfd12 | finance | mid | US | OT | R1, R4 |
| L24 | Jam City, Inc. | Genies & Gems: Puzzle & Quests (1032443533) | https://support.jamcity.com/privacyrequest/ (access and erasure only; opt-outs at `/stateoptout/`) | games | large | US | own web form | R2 (us), R4 |
| L25 | CBC Restaurant Corp (Corner Bakery Cafe) | Corner Bakery Cafe (783177433) | https://cornerbakerycafe.com/my-privacy-choices/ | food-drink | large | US | own web form | R2 (us), R4 |
| M3 | AdSpark, Inc. | (web) | https://www.adspark.ph/data-subject-request (form: https://d15fzhw4120coi.cloudfront.net/media/data-subject-request-form.pdf) | b2b-saas | mid | other (PH) | own PDF form | web search, R4 |
| M4 | Astrocenter.com (Astrology.com) | Astrology Plus (327586041) | https://www.astrology.com/us/privacy-request.aspx | lifestyle | mid | US | own web form | R2 (us), R4 |
| M5 | You Need A Budget LLC | YNAB (1010865877) | https://www.ynab.com/privacy-policy/data-subject-rights-request | finance | mid | US | own web form | R2 (us), R4 |

There is no small reserve. The R2 tail slice ran, and no further small row qualified. Finance
is at 5 of 24, and the cap is 6. So one non-finance pick may be replaced by a finance reserve
(L6, L9, L13, L16, L17, L19–L23, M1, M2, M5). After that, a finance reserve replaces only a
finance pick.

## Left out

- **Blocked, no recipe** (per `portal-probe.md`):
  - SixFifty: Dutch Bros, Ace Parking.
  - Zendesk forms: McDonald's UK, Home Store + More.
  - DataGrail: MyFitnessPal.
  - Relyance: Opendoor.
  - Typeform: Perplexity.
  - Termly: Blossom.
  - datasubject.com (JavaScript embed): Hatch (mid, tail; Wayback not tried).
  - Pipedrive webforms: Pipedrive.
  - Salesforce: eBay.
  - In-house SPAs: Capital One, Experian US, Wells Fargo, Sainsbury's Bank, WeChat US, Instacart,
    Klarna.
  - Bot walls: Walmart, Ledger, At Home, Santander Consumer, Severn Trent, Jet2.
- **Open rows that fail now:**
  - JavaScript shells with no readable form: WeChat EU, easyJet, Hastings Direct, Zendesk,
    Target (its intake form "unable to load"), OKX.
  - Login-gated: UNiDAYS.
  - Session-gated, landing on a timeout page: Barclays.
  - Bot walls: Wayfair (429), CrazyLabs (Cloudflare 403).
  - 404 or moved: Spotify, Arm, IKEA.
  - HP: the form link leads to a language chooser, then a 404.
- **Not a request form:**
  - Experian UK: a rights information page.
  - Passport Labs: US state privacy notice (a policy section).
  - Crunch Fitness: opt-out only (TrueVault), and its request page is an empty template.
  - Prosper: an opt-out-only OneTrust form with one request type.
  - National Rail: a OneTrust `draft` form with one request type.
  - Next Insurance: deletion only.
  - Waking Up (small, tail): opt-out only (sale, sharing, targeted ads, profiling).
  - Tail "seen and not kept" rows (HER, Hooked on Phonics, BoomHits, Hily, BlackGentry):
    opt-out only or no form, per `pool/dsar-tail.md`.
- **Rule 1 (not the company's own form):**
  - Cal AI and Pi: DataRep's generic representative form.
  - Ebby Halliday: HomeSpotter's form.
- **Not used:**
  - Wellspring Meds: TrueVault page with only 404 placeholders and no recipe.
  - ALDI US: German group, US-only form. The large third is full and the OneTrust cap is met.
- **Group duplicates:** DTLR (JD Sports), O2 PDF (Virgin Media), Experian UK/US, WeChat second
  row.

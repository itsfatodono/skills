---
doc_id: oss-notices
built: 2026-10-27
routes_run: [R1, R4]
raw_rows: pool/
---

Selected from the raw rows in `pool/oss.md` (one slice, 39 rows: App Store listings plus
web-only developer sites). Small creator build (PLAN.md decision 48), so `build.md` *User run*
numbers apply: up to 15 candidates, mixed sizes, no size thirds. English only. Size is an
estimate per `sources.md`, never researched. Taken: 5 large, 5 mid, 5 small.

**What counts.** A web-reachable list of third-party open-source components with their licences
(names, licence ids or full texts, notices, source offers). Template and generated lists are
valid samples (decision 26); the generator is noted where the page names it or its layout
gives it away. Not samples: a licence for the company's own open-source project, and a generic
legal hub that only links to notices.

**Group check (rule 5), done at selection.** Amazon (Blink via Immedia Semiconductor, Kindle)
taken once as Blink. Microsoft taken nowhere (its row is a hub, below). Venmo is PayPal, Evernote
is Bending Spoons, Parsec is Unity, Pandora is SiriusXM: each the only row of its group.

**Re-attributed row.** The raw row "Apption Labs (MEATER)" points at
`customerthermometer.com/open-source-attribution/`, which is Customer Thermometer's own notice
for its own web service, not MEATER's. Under rule 1 it is taken as Customer Thermometer
(UK feedback SaaS), not as MEATER. Its intro wording ("compiled with reference to third-party
software incorporated into the services as of the date the list was generated") is the same as
Mill's (reserve M2): a shared template block, so expect a partial match at merge.

**First-screen check (`build.md` step 1), done 2026-10-27.** Every URL below and in *Reserve*
was fetched and its title and first screen read. Dropped (11):
- Not the document: Microsoft `third-party-notices` (generic legal hub, links only); Docker
  `components-licenses` (no component list in the page; its header is about Docker's own
  Apache-2.0 projects); Otter `open-source-licenses` (the slug resolves as a public profile
  name in the app shell, no notice).
- No readable text without JS: Zillow help article (empty shell), Peekie (shell plus base64
  assets only), JetBrains `third-party-software` (product picker; the list is not in the HTML).
- Blocked or erroring: PuttView (Cloudflare block), Zoom (bot wall), Box
  (bot wall), ADT (403), Meta Quest notices (HTTP 400). Wayback not tried: the 15 picks filled
  without them.

Pool order rotates size (large, mid, small) and sector; c01–c05 are the first batch, then the
saturation batch c06–c10, then c11–c15 as spares.

| Order | # | Company | App (store id) | URL | Sector | Size | Base | Language | Size evidence | Generator | Route |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | c01 | TikTok Pte. Ltd. | TikTok - Videos, Shop & LIVE (835599320) | https://www.tiktok.com/legal/page/global/open-source/en | entertainment | large | SG | en | ByteDance subsidiary; 18.4M ratings | none visible; Android and iOS sections, LGPL written offer | R1 |
| 2 | c02 | Granola Inc. | Granola - AI Meeting Notes (6739429409) | https://www.granola.ai/third-party-licenses | productivity | mid | US | en | funded AI startup, ~100 staff; 14.6K ratings | `generate-license-file` (npm), named on the page | R1 |
| 3 | c03 | Chau Duong (EchoManage) | Set Up & Control Smart Speaker (6761295368) | https://www.echonx.com/license.html?lang=en | reference | small | unknown | en | sole developer; 1.7K ratings | `license-checker`, named on the page with generation timestamp | R1 |
| 4 | c04 | Lyft, Inc. | Lyft (529379082) | https://www.lyft.com/legal/licenses | travel | large | US | en | listed company, ~3K staff | none visible; own preamble on OPEN LICENSE terms | R1 |
| 5 | c05 | Cantina, Inc. | Cantina: AI Video & Characters (1018368216) | https://cantina.com/licenses | photo-video | mid | US | en | startup, ~100 staff; 110K ratings | not named; generated table (2,187 components by platform, licence texts at end) | R1 |
| 6 | c06 | Zed Industries | (web) | https://zed.dev/attributions | developer-tools | small | US | en | editor startup, ~50 staff | not named; licence-grouped counts ("MIT License (100)") match the `cargo-about` template | R4 |
| 7 | c07 | The Delancey Corporation (Venmo) | Venmo (351727428) | https://help.venmo.com/cs/articles/open-source-attribution-page-for-venmo-vhel275 | finance | large | US | en | PayPal subsidiary; 15.5M ratings | none visible; component list then licence texts | R1 |
| 8 | c08 | Propel Inc | Propel: EBT, SNAP, WIC, & more (1112719759) | https://www.propel.app/open-source-acknowledgements/ | finance | mid | US | en | fintech, ~100 staff; 609K ratings | not named; generated package/licence table (710 packages, 17 licences, "last reviewed" date) | R1 |
| 9 | c09 | Duncan Cuthbertson (YourMyDS) | (web) | https://yourmyds.com/open-source-licenses | health-fitness | small | unknown | en | sole developer | not named; "compiled list" of full licence texts | R4 |
| 10 | c10 | Figma, Inc. | Figma (1152747299) | https://www.figma.com/open-source/ | graphics-design | large | US | en | listed company, ~1.7K staff | none visible; per-library full licence texts | R1 |
| 11 | c11 | Anysphere Inc. (Cursor) | Cursor (6767085653) | https://cursor.com/licenses | developer-tools | mid | US | en | AI startup, ~300–500 staff | none visible; per-component notices, dated | R1 |
| 12 | c12 | Customer Thermometer Ltd | (web; raw row filed under MEATER) | https://www.customerthermometer.com/open-source-attribution/ | b2b-saas | small | UK | en | small SaaS team | not named; shared intro template (see above) | R1 row, R4 page |
| 13 | c13 | Immedia Semiconductor (Blink) | Blink Home Monitor (1013961111) | https://apphelp.immedia-semi.com/en/license/Attribution.html | utilities | large | US | en | Amazon subsidiary; 508K ratings | none visible; per device and app, with source-code tarballs | R1 |
| 14 | c14 | Socotra, Inc. | (web) | https://ccdocs.socotra.com/open-source-attribution.html | b2b-saas | mid | US | en | insurtech, ~100–200 staff | not named; tables grouped by licence (software, version, copyright) | R4 |
| 15 | c15 | Callers (Really Clicking LLC) | (web) | https://docs.callers.ai/documentation/legal/open-source-attribution | b2b-saas | small | US | en | small SaaS team | none; hand-written, one component (Activepieces, MIT) | R4 |

Sectors: b2b-saas 3; finance, developer-tools 2; entertainment, productivity, reference,
travel, photo-video, health-fitness, graphics-design, utilities 1.

## Reserve

Used in this order, same size first, when a candidate drops out. First-screen check and group
check done.

| # | Company | App (store id) | URL | Sector | Size | Base | Generator | Route |
|---|---|---|---|---|---|---|---|---|
| L1 | Pandora Media, LLC | Pandora: Personalized Music (284035177) | https://pandora.com/legal/opensource | music | large | US | none visible | R1 |
| L2 | Smartsheet Inc. | Smartsheet: Projects & Teams (568421135) | https://www.smartsheet.com/legal/acknowledgements | business | large | US | none visible; downloadable software only, mobile notices are in-app | R1 |
| L3 | Aptean, Inc. | (web) | https://www.aptean.com/en-US/osa-notice-aptean-respond | b2b-saas | large | US | none visible; one product (Respond) | R4 |
| M1 | Raycast Technologies Inc | Raycast: AI, Notes and more (6503428327) | https://www.raycast.com/acknowledgements | productivity | mid | UK | not named; Acknowledgements-style full texts | R1 |
| M2 | Mill Industries, LLC | Mill: Kitchen Bin Companion (1637998905) | https://www.mill.com/legal/open-source-software-disclosure | lifestyle | mid | US | not named; same intro template as c12 | R1 |
| M3 | Evernote Corporation | Evernote: AI Notes & Notebook (281796108) | https://evernote.com/legal/open-source | productivity | mid | US | none visible; dated, per-component texts | R1 |
| M4 | Tempo Software (Structure for Jira) | (web) | https://help.tempo.io/structure-dc/latest/open-source-licenses | b2b-saas | mid | US | none; component/licence link table | R4 |
| M5 | LightningLink Networks Pte. Ltd. | X-VPN: VPN Fast & Secure (1250312807) | https://xvpn.io/open-source-licenses | productivity | mid | SG | none visible; grouped by licence | R1 |

No small reserve: all five small rows that passed the screen are picks.

Valid but not taken: Aura Frames `auraframes.com/oss` (GPL source offer naming only U-Boot and
the Linux kernel; mid, hardware); Parsec `parsec.app/acknowledgements` (Unity group; mid);
Spotify `developer.spotify.com/third-party-licenses` (developer SDKs only, not the consumer
app); Okta Verify PDF (Windows Shared product, file dated 2022-04, currency not confirmed);
Amazon Kindle (group duplicate of Blink).

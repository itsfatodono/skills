# contractor-agreement: build record

Built 2026-11-12 (pre-built run, no sector, no region; backlog no. 71). Skeleton:
`plugins/fatodono-founderkit/skills/legals/skeletons/contractor-agreement.md`.

## Files

- `candidates.md`: the fit rule, the pool of 30 and the reserve, and who was left out at selection.
- `pool/`: raw rows from seven `pool-collector` slices.
- `extractor-notes.md`: the notes every `sample-extractor` got besides its helper file.
- `samples/sNN.md`: one extraction table per valid sample. `invalid.md`: samples that failed.
- `section-map.md`: each table row mapped to a section id (the basis of every count).
- `merge.md`: section ids, merged list, order and folds, the IP decision, saturation log, document
  level, *Regional content*.
- `progress.md`: the run's working log.

## Run

- **Routes run:** R8 (SEC EDGAR full-text search) in six slices: `r8-consulting-a` ("Consulting
  Agreement", 10-K/10-Q), `r8-consulting-b` (same, 8-K/S-1), `r8-contractor` ("Independent
  Contractor Agreement", "Consulting Services Agreement"), `r8-freelance-topics` (long tail:
  consulting or contractor agreements with software, web, design, social-media and marketing
  terms), `r8-large` (large accelerated filers only, by the SEC filer category), `r8-forms`
  ("Form of Consulting Agreement" and similar company forms). R9 (standard forms) in one slice,
  widened to public models: Common Paper, Bonterms, Cooley GO, Orrick, AIGA, Freelancers Union,
  the NYC Department of Consumer and Worker Protection. 93 raw rows.
- **Pool:** 30 candidates (8 large, 8 mid, 9 small, 5 standard forms) plus a reserve. No sector
  above 7 of 30. Group check (rule 5) at selection.
- **First batch:** 14 valid tables (large s01 s04 s07 s10; mid s08 s18 s22 s26 s31; small s03 s06
  s09 s15 s19). Nine extracted texts failed the fit rule and were replaced by the next same-size
  candidate; the large pool ran out, so the first batch is 14, not 15.
- **Saturation:** batch s16 s20 s23 s24 s27, all not new. Five in a row: saturated at s27.
  `saturated: true`, `sample_count: 19`, 31 section ids. c28 (AIGA), c29 and c30 were not
  extracted.
- **Stop reason:** saturation.
- **Interruption:** a usage-limit stop killed three running extractors; s19 and s26 had written
  complete tables, s25 was resumed from its saved raw text.

## Fit rule (judgement call)

The skeleton serves a startup or solo developer engaging a freelancer or a small firm. Most EDGAR
"Consulting Agreements" are filed because they are related-party deals: a departing executive
kept on as a consultant, an officer or director engaged through a consulting contract. Their texts
often carry separation, vesting and board terms that a freelancer deal never has. Selection skipped filers whose consultant had just
left an executive post (from the first screen and general knowledge), and extraction judged each
text: a text carrying another relationship's terms (separation, transition, retirement, continued
vesting, an officer or board appointment) failed rule 6 (scope). A clean services engagement
passes even when the performer also sits on the board (s07; s08, whose text records the
consultant's independent directorship but sets no board duties; s18, whose text keeps any board
service out of the billed services) or later became an officer (s15).
The rule was restated twice in `candidates.md`, each time in place: first so that the text decides
rather than who the consultant is (s07 was first marked invalid and then extracted), then to keep
fractional roles only without an officer title (s05, s12).

The 16 EDGAR samples are mostly advisory engagements of small listed companies (business
development, investor relations, finance, scientific advice); several pay in shares. The patterns
a designer or developer engagement needs (deliverables, acceptance, the contractor's own and
open-source materials, licence or assignment per deliverable) come mostly from the three standard
forms and from s07, s09 and s31.

## Standard forms

`standard-form` samples are `size: none`: Common Paper Independent Contractor Agreement (s16),
Bonterms Professional Services Agreement (s20), NYC model Freelance Work Agreement (s24). 3/19,
within the one-in-four cap. Common Paper's PSA was not taken (one sample per project). Cooley GO
(US, UK, Singapore) and Orrick forms sit behind a generator with a bot wall or JavaScript and were
kept as reserve F1 and F2, never reached. The Freelancers Union contract (c30) and the AIGA design
form (c28) were in the pool past the stop point. Contract Killer (sold) and the Graphic Artists
Guild (paid handbook) were not free.

## Size thirds

4 large, 5 mid, 7 small, 3 none. **Large shortfall:** of the 8 large texts read, 4 carried
departure terms (c13 Under Armour, c17 Clear Secure, c21 Marcus & Millichap, c25 Aviat), and 13
further large filers were skipped at selection as known departure or director deals (Super Micro,
Zynex, Innovex, SentinelOne, Sage, Pacira, Pure Storage, Etsy, Arena, Akebia, Azenta, Open Text,
Roivant). Large filers file a consulting agreement mostly when it keeps a departing executive;
ordinary vendor and freelancer contracts are not material enough to file. **Mid** lost four of eight to the same cause
(s02 s05 s11 s14) and was refilled from the reserve (s31). Small filers were plentiful.

## Invalid

All rule 6 (scope); text in `invalid.md`, raw texts kept for the copy check.

| Sample | Company | Size | Reason |
|---|---|---|---|
| s02 | Immunome, Inc. | mid | separation agreement kept in force; options keep vesting under it |
| s05 | Data I/O Corporation | mid | the firm's executive appointed interim CFO with D&O cover |
| s11 | Arvinas, Inc. | mid | retiring R&D head; equity keeps vesting while consulting |
| s12 | Astrotech Corporation | small | the firm takes CFO and subsidiary board offices |
| s13 | Under Armour, Inc. | large | transition of the consultant's former organisation; RSUs keep vesting |
| s14 | Trecora Resources | mid | retiring SVP; keeps company email and assets for an orderly transition |
| s17 | Clear Secure, Inc. | large | departing General Counsel; equity forfeiture and employment agreements carried over |
| s21 | Marcus & Millichap, Inc. | large | retiring COO; post-employment obligations and equity kept |
| s25 | Aviat Networks, Inc. | large | retiring SVP handing over to his successor |

Several extractors confirmed a departure from the filer's own 8-K or 10-K beside the exhibit; the
judgement still rests on terms in the text (vesting, assets, transition).

## Copies

None (rule 4). s09 reads as a free do-it-yourself template; VenHub's five same-form exhibits gave
one sample (s23).

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | Schrödinger, Inc. | https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231xxex1024fries.htm | b2b-saas | large | en | 2026-11-12 |
| s03 | HUMBL, Inc. | https://www.sec.gov/Archives/edgar/data/1119190/000149315223026900/ex10-1.htm | finance | small | en | 2026-11-12 |
| s04 | REX American Resources Corp. | https://www.sec.gov/Archives/edgar/data/744187/000093041326000937/c115944_ex10-f.htm | business | large | en | 2026-11-12 |
| s06 | Ludwig Enterprises, Inc. | https://www.sec.gov/Archives/edgar/data/1960262/000190359623000540/ex10-10.htm | medical | small | en | 2026-11-12 |
| s07 | Forescout Technologies, Inc. | https://www.sec.gov/Archives/edgar/data/1145057/000114505719000031/a06072019101.htm | utilities | large | en | 2026-11-12 |
| s08 | Athena Bitcoin Global | https://www.sec.gov/Archives/edgar/data/1095146/000168316823007999/athbitcoin_ex1040.htm | finance | mid | en | 2026-11-12 |
| s09 | Fashionista Distributor Holdings Inc. | https://www.sec.gov/Archives/edgar/data/2004256/000173112224000879/e5692_ex10-6.htm | lifestyle | small | en | 2026-11-12 |
| s10 | CareCloud, Inc. | https://www.sec.gov/Archives/edgar/data/1582982/000149315226009872/ex10-40.htm | medical | large | en | 2026-11-12 |
| s15 | Nexscient, Inc. | https://www.sec.gov/Archives/edgar/data/1976663/000147793223007753/nexscient_ex104.htm | b2b-saas | small | en | 2026-11-12 |
| s16 | Common Paper (Independent Contractor Agreement v1.0) | https://commonpaper.com/documents/common-paper-independent-contractor-agreement-docx | standard-form | none | en | 2026-11-12 |
| s18 | Ceribell, Inc. | https://www.sec.gov/Archives/edgar/data/1861107/000095017024113073/cbll-ex10_28.htm | medical | mid | en | 2026-11-12 |
| s19 | Mangoceuticals, Inc. | https://www.sec.gov/Archives/edgar/data/1938046/000149315223002627/ex10-33.htm | health-fitness | small | en | 2026-11-12 |
| s20 | Bonterms (Professional Services Agreement v1.2) | https://framerusercontent.com/assets/3owa7Qh705NnKztfpxY5tU0Nfs.pdf | standard-form | none | en | 2026-11-12 |
| s22 | Nuvve Holding Corp. | https://www.sec.gov/Archives/edgar/data/1836875/000183687525000095/nvve-102bristolconsultinga.htm | utilities | mid | en | 2026-11-12 |
| s23 | VenHub Global, Inc. | https://www.sec.gov/Archives/edgar/data/1972234/000121390026074328/ea029640801ex10-12.htm | shopping | small | en | 2026-11-12 |
| s24 | NYC Department of Consumer and Worker Protection (model Freelance Work Agreement, 2025-01-23) | https://www.nyc.gov/assets/dca/downloads/pdf/workers/Model-Contract-Freelance.pdf | standard-form | none | en | 2026-11-12 |
| s26 | CaliberCos Inc. | https://www.sec.gov/Archives/edgar/data/1627282/000110465923044483/tm2230806d15_ex10-15.htm | finance | mid | en | 2026-11-12 |
| s27 | Aureus Greenway Holdings Inc. | https://www.sec.gov/Archives/edgar/data/2009312/000149315226012209/ex10-3.htm | sports | small | en | 2026-11-12 |
| s31 | FDCTECH, Inc. (reserve M1) | https://www.sec.gov/Archives/edgar/data/1722731/000149315226044195/ex10-13.htm | finance | mid | en | 2026-11-12 |

s09 is filed by the consultant, not the client; s23's filer signed five agreements on one form.
s20 also takes its cover page and SOW examples from the Bonterms download page; s16's docx holds
the cover page and the terms.

## Proposed catalog row

Not added (the build may not edit `helpers/catalog.md`). A new family is needed: none of
`privacy-notices`, `terms`, `commerce`, `licensing`, `internal-compliance` fits an agreement the
company signs with someone who works for it. Proposed `team-agreements`, which the sibling items
69 (founder agreement) and 70 (IP assignment) would share.

```markdown
| contractor-agreement | Freelancer / Contractor Agreement | document | team-agreements | Does the company engage freelancers, consultants or contracting firms (a designer, a developer, a marketer, an agency) to do work for it? One agreement per contractor sets the work, the pay, the contractor's independent status and who owns what they make. If a contractor already works under a signed agreement that covers these, say so rather than writing one. | `skeletons/contractor-agreement.md` |
```

## Facts

Appended to `helpers/facts-schema.md`: three company keys every contract skeleton can reuse
(`facts.company.entity_form`, `facts.company.contract_law`, `facts.company.signatory`) and a new
`contractor` group of 17 keys (party, services, work_arrangements, fees, payment_terms, expenses,
term, termination, ip_terms, confidentiality, restrictions, subcontracting, liability, insurance,
data_access, portfolio_use, prior_work). No sibling had added a key when they were appended.

## For the owner's review

1. **Fit rule.** EDGAR deals that keep a departing executive or a director on as a consultant are
   left out; nine extracted texts failed on it. s07 and s08 (the performer is a sitting director) and s15
   (the owner became an officer six weeks later) were kept because their texts are clean
   engagements. Confirm the text-decides line. Borderline under it: s01 (a co-founder; §7 gives
   him "such benefits as are generally provided to executive employees", minus health cover), kept
   because no departure, officer or board term appears; the skeleton records it as 1/17 in
   `independent-contractor`.
2. **Large third short (4).** Cause above. A further R8 pass is unlikely to help: half the large
   texts read, and most large hits seen at selection, were departure deals.
3. **19 samples, below the expected 20.** Saturated at s27, so the AIGA design form, the
   Freelancers Union contract and Miami Breeze were not extracted. The AIGA form is the one
   designer-specific source; consider it for a sector run.
4. **Advisory-heavy evidence.** Deliverable, acceptance and open-source patterns rest on few
   samples (3/19 to 4/19). A user run in a design or software sector would sample closer to the
   target user.
5. **New family `team-agreements`** for the catalog; the sibling builds may propose another name.
6. **Facts schema.** The *Keys* intro's "Groups:" line does not list `contractor`: the build may
   only append. `facts.company.contract_law` sits beside `facts.company.governing_law` (user
   terms); merge them if one key should serve both.
7. **IP section kept in the agreement**, not pointed to the `ip-assignment` document (`merge.md`
   *IP*). `facts.contractor.ip_terms.placement` lets a user drop it.
8. **Equity as pay** (9/19) stays a pattern in `fees`; the fact's *Ask* recommends cash, and the
   securities terms are US regional content.
9. **Regional content is US only.** No UK (IR35), EU, German or Turkish sample exists in the
   pool; those region runs start from their own routes. The NYC Freelance Isn't Free Act model
   (s24) is a city-law source for a `us` block.
10. **Raw texts.** Two extractors redacted email addresses in `raw/s04.txt` and `raw/s10.txt`;
    other raw texts keep the contact emails in the filings. `raw/` is git-ignored.

## Lessons

- **EDGAR's consulting route is mostly a departure route.** About two in five EDGAR texts read
  (9 of 25) failed scope, and first screens rarely show it: the vesting or transition terms sit in
  an exhibit. For people-related contracts, a pre-check against the filing's 8-K Item 5.02 at
  selection would save extractions.
- **"Form of Consulting Agreement" is thin.** Company forms are clean by design, but few are filed
  as exhibits (5 rows); public standard forms carry the target user's patterns better.
- **The first batch can fall short of 15** when a size runs out mid-batch; build.md's "or the pool
  is empty" covered it.

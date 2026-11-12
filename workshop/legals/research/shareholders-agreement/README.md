# shareholders-agreement: build record

Built 2026-11-12 (backlog item 69, pre-built run: no sector, no region). Skeleton:
`plugins/fatodono-founderkit/skills/legals/skeletons/shareholders-agreement.md`. 29 samples,
`saturated: true` (stop point s21), 31 sections.

## What the skeleton is for

The agreement two or more founders sign about the company they own together: shareholdings, board
and decisions, deadlock, founders' roles, IP and covenants, vesting and leavers, transfer rules
(first refusal, tag, drag), exit, and the closing clauses. It stays the same document when early
holders or investors join; investor-stage add-ons (class rights, information rights, company
undertakings) are rare sections with an *Applies when* on investors being present.

Which samples fit: any contract among the shareholders of one **private** company about owning
it (`extract-notes.md` *What the document is*). In: founders' agreements, shareholders' and
stockholders' agreements, voting agreements among a private company's holders, two- or
three-owner joint-company agreements, and their model forms. Out: anything that starts at or after
an IPO, M&A support agreements, registration or investors' rights agreements alone, stock purchase
agreements, operating agreements and articles. Owner-level texts (founders, early holders, joint
companies: 16) and investor-stage texts (13) are counted separately in the skeleton where they
split.

## Files

- `candidates.md`: standard forms f1–f8, pool c01–c30 (10/10/10), reserve, dropped at selection.
- `extract-notes.md`: scope, EDGAR recipe, row granularity and `[law: …]` rules given to every
  worker.
- `pool/`: raw rows from five `pool-collector` slices.
- `samples/sNN.md`: one extraction table per sample; `raw/` (git-ignored) holds the texts.
- `section-map.md`: every table row mapped to a section id (the basis of every count).
- `merge.md`: section ids, first-batch list, saturation log, folds, merged list, document level,
  *Regional content*.
- `invalid.md`: s01, s24.
- `progress.md`: the run's working log.

## Run

- **Routes run:** R8 (EDGAR full-text search) in four slices, R9 (standard forms) in one; together
  they are every route `sources.md` lists for item 69. Raw rows: `r8-founders` 2,
  `r8-shareholders` 60, `r8-voting` 27, `r8-buysell` 27 (the long-tail slice: buy-sell, stock
  restriction and closely held shareholders' agreements of small filers, Regulation A included),
  `r9-models` 23 (12 projects).
- **Selection:** 30 sized candidates (10 per size) and 8 standard forms, one per project. Every URL
  opened at selection; after s01 came back invalid, each candidate's term clause was also read, and
  four more were dropped (`candidates.md` *Dropped at selection*). No sector above 7 of 30.
- **Workers:** `pool-collector` (Sonnet, medium) and `sample-extractor` (Opus, high), at most 3 at a
  time. The usage limit stopped three extractors (s06, s07, s08) after they had saved their raw
  text; they were resumed after the reset and finished.
- **First batch:** s02–s16 (s16 took the large position of invalid s01) and standard forms s31–s35.
- **Saturation:** s17–s21 judged in pool order; none brought a section the list lacked, so the
  run is saturated at s21. The next batch, s22–s26, was dispatched before that judgement was done
  (by step 3 the run would have ended at s21 without it); its samples are kept past the stop
  point (s24 invalid). c27–c30 and standard forms f6–f8 were not extracted.
- **Stop reason:** five non-new samples in a row (s17–s21). `saturated: true`, `sample_count: 29`.

## Invalid

| Sample | Company | Rule | Reason |
|---|---|---|---|
| s01 | On Holding AG | 6 | The founders' pool agreement takes effect at the NYSE listing (post-IPO). |
| s24 | Forward Pharma A/S | 6 | Takes effect at the Nasdaq listing and replaces the pre-IPO agreement. |

## Size thirds

Samples: 8 large, 9 mid, 7 small, plus 5 standard forms (17%, under the one-in-four cap). The pool
held 10 of each size; the thirds are short because saturation stopped the run before c27–c30 and
because both invalid samples were F-1 filings that start at an IPO (one large, one small). Small
filers were not scarce once the long-tail slice ran: EDGAR's small companies file closely held
shareholders' and buy-sell agreements, mostly with registration statements and Regulation A
offerings. Large filers are mostly investor-stage or joint-venture texts.

## Standard forms

Used: SVCA/SAL VIMA founders' agreement (s31), Seedcamp founder collaboration agreement (s32),
StartupTools Finland shareholders' agreement without investors (s33), NVCA voting agreement (s34),
UK Private Capital shareholders' agreement, Feb 2023 Wayback copy (s35; the 2025 edition needs a
member login). Not used: MaRS, SECA, CVCA (reached after the stop point). Unreachable: Startup
Estonia founders' agreement (JavaScript-only share pages), Seedsummit (Dropbox links disabled),
AirTree and Startup Commons (email or web forms). The Seedcamp `.doc` loaded at selection; the
extractor found the link dead later and used the identical PDF capture.

## Templates and copies

No two samples share a whole text (rule 4). Shared layouts are listed in `merge.md` *Copies and
templates*.

## Judgement calls

- **Scope:** private company only; an agreement that starts at or after an IPO is out, one that ends
  at it is in. It mattered: s01 and s24 came back invalid as post-IPO texts, and D-Market, trivago
  and Avast were dropped at selection for the same reason.
- **Exhibit types:** `sources.md` R8 keeps `EX-10` hits; this item also kept `EX-4`, `EX-9` and
  Regulation A `EX1A` exhibits, because shareholders' agreements are filed as instruments defining
  holders' rights. 9 of the 24 sized samples are `EX-4`, `EX-9` or `EX1A` exhibits.
- **Long-tail slice:** `r8-buysell` searched phrases beyond the item's named titles (buy-sell,
  stock restriction, close corporation). It is still R8, and without it the small third was empty.
- **Stage groups:** extractors corrected the candidate stage on 10 samples from the text; the
  skeleton's owner/vc split uses the samples' corrected stage.
- **Folds** at merge (`merge.md` *Folds*): 39 ids became 31 sections. The broadest ids
  (`parties` with the business clause, `capitalisation` with class rights and the option pool,
  `general` with warranties and remedies) made it hard for a sample to be "new"; see the owner's
  review.
- **Sectors** of EDGAR filers follow `sources.md` (the App Store category of the main product);
  industrial filers are `business` (7 of 30, at the cap).

## For the owner's review

- **sources.md note on item 69:** it says founders' collaboration agreements have no reputable
  public model. Seedcamp publishes one (s32, CC BY-NC-SA) and SVCA a founders' agreement (s31);
  Startup Estonia publishes a 2026 founders' agreement that was unreachable only for technical
  reasons. Worth updating the note and the item's sources (R9: SVCA, Seedcamp, StartupTools,
  Startup Estonia, MaRS, SECA, CVCA).
- **Founder subjects are rare in the data:** vesting (3/29), founder roles (4/29), deadlock
  (3/29) and IP (9/29) are rare because US investor-stage practice moves them into separate
  documents. The skeleton keeps them as rare sections with *Applies when* on the founders' facts.
  A founder-only sample set (more owner-level texts) would likely make them common; the public
  supply of such texts is small.
- **Saturation with broad ids:** 39 ids over 29 samples saturated at s21. Decision 27 counts new ids
  only, and broad ids absorb a lot (s23's founders' compensation for missed targets was judged to
  fit `share-rights`). A stricter reading could have reset the count at s23, after the stop point.
- **Proposed id and title:** 24 of 29 samples, and the UK, Finnish, Canadian and Swiss models, call
  the document a shareholders' or stockholders' agreement (3 are voting agreements); only SVCA and Seedcamp say founders' agreement, for the
  version before investors join. Proposal: id `shareholders-agreement`, title "Shareholders'
  Agreement", with the trigger question asking about founders. Kept `shareholders-agreement` here, since
  shared files may not be renamed in this run.
- **New family:** no catalog family fits. Proposed `company` (company and ownership documents: this
  item, the IP assignment, incorporation), matching the "Company contract keys" and "Team keys"
  groups the sibling builds added to `facts-schema.md`.
- **No Turkish sample:** the only Turkish candidate (Hepsiburada) takes effect at its IPO. A `tr`
  region run needs TTK-governed samples (A.Ş. and Ltd. Şti. share transfer rules, notarised Ltd.
  transfers).
- **New fact keys** (*Ownership keys* in `helpers/facts-schema.md`): `share_structure`,
  `founder_commitment`, `founder_vesting`, `board`, `decision_rules`, `share_transfer_rules`,
  `funding_terms`. Their recommendations (48-month vesting with a 12-month cliff, a short reserved
  list needing all founders, no casting vote between equal founders, a drag only above a
  threshold all founders accept) come from the samples' defaults; check that they read as advice
  you want the skill to give.
- **Region check on covenants:** founders' non-competes appear in 9/29; the root keeps them as a
  pattern. Region blocks should mark them *Avoid* where a law voids them (for example California),
  as `formats/region-format.md` *Avoid on root sections* describes.

## Proposed catalog row

| Id | Title | Kind | Family | Trigger question | Skeleton |
|---|---|---|---|---|---|
| shareholders-agreement | Founders' Agreement | document | company | Does the company have, or is it about to have, more than one shareholder: two or more founders, or a founder plus an investor or an early team member holding shares? Co-owners need written terms on who owns what, how decisions are taken and what happens when one of them leaves. A company with a single owner needs none, so say so rather than writing one. | `skeletons/shareholders-agreement.md` |

## Samples

| Sample | Company | URL | Sector | Size | Base | Stage | Language | Fetched |
|---|---|---|---|---|---|---|---|---|
| s02 | IronPlanet, Inc. | https://www.sec.gov/Archives/edgar/data/1481441/000095012310043696/f55123a1exv10w11.htm | e-commerce | mid | US | vc | en | 2026-11-12 |
| s03 | Collective Wisdom Technologies, Inc. | https://www.sec.gov/Archives/edgar/data/1741298/000121390018011367/f1a2018a1ex3_collective.htm | productivity | small | US | founder | en | 2026-11-12 |
| s04 | Materialise NV | https://www.sec.gov/Archives/edgar/data/1091223/000119312514153215/d655315dex43.htm | graphics-design | large | EU (BE) | early | en | 2026-11-12 |
| s05 | Tennessee Commerce Bancorp, Inc. | https://www.sec.gov/Archives/edgar/data/1323033/000110465905019396/a05-7681_1ex4d1.htm | finance | mid | US | founder | en | 2026-11-12 |
| s06 | Royal Bakery Holdings, Inc. | https://www.sec.gov/Archives/edgar/data/1594485/000121390013007493/fs12013ex9i_royalbakery.htm | food-drink | small | CN (HK) | founder | en | 2026-11-12 |
| s07 | SFX Entertainment, Inc. (ID&T) | https://www.sec.gov/Archives/edgar/data/1553588/000104746913008772/a2216461zex-4_7.htm | entertainment | large | EU (NL) | jv | en | 2026-11-12 |
| s08 | Merus B.V. | https://www.sec.gov/Archives/edgar/data/1651311/000119312516434605/d29248dex1011.htm | medical | mid | EU (NL) | vc | en | 2026-11-12 |
| s09 | Lantis Laser Inc. | https://www.sec.gov/Archives/edgar/data/1413299/000114420408036539/v117346_ex10-14.htm | medical | small | US | jv | en | 2026-11-12 |
| s10 | Wix.com Ltd. | https://www.sec.gov/Archives/edgar/data/1576789/000119312513407296/d541565dex101.htm | productivity | large | IL | vc | en | 2026-11-12 |
| s11 | ReWalk Robotics Ltd. (Argo Medical Technologies) | https://www.sec.gov/Archives/edgar/data/1607962/000119312514270079/d724635dex1010.htm | medical | mid | IL | vc | en | 2026-11-12 |
| s12 | VME Companies, Inc. (VME Process) | https://www.sec.gov/Archives/edgar/data/2113640/000157587226000691/vmec004_ex10-3.htm | business | small | US | early | en | 2026-11-12 |
| s13 | IPG Photonics Corporation | https://www.sec.gov/Archives/edgar/data/1111928/000095013506006288/b61608a2exv10w43.txt | business | large | US | vc | en | 2026-11-12 |
| s14 | First Mercury Financial Corp. | https://www.sec.gov/Archives/edgar/data/929186/000095013706010763/c05689a3exv10w23.htm | finance | mid | US | vc | en | 2026-11-12 |
| s15 | Monaker Group, Inc. | https://www.sec.gov/Archives/edgar/data/1372183/000158069521000020/ex10-31.htm | travel | small | EU (CH) | jv | en | 2026-11-12 |
| s16 | Transport America (Patriot Holding Corp.) | https://www.sec.gov/Archives/edgar/data/1582854/000104746913011241/a2217600zex-4_2.htm | business | large | US | jv | en | 2026-11-12 |
| s17 | Advanced Accelerator Applications S.A. | https://www.sec.gov/Archives/edgar/data/1611787/000157104915000062/t1402271_ex4-3.htm | medical | mid | EU (FR) | early | en | 2026-11-12 |
| s18 | Pure Play Media Holdings, Inc. | https://www.sec.gov/Archives/edgar/data/1328784/000112785506000394/pureplayexh10_2.htm | entertainment | small | US | early | en | 2026-11-12 |
| s19 | Wanda Sports Group Co. Ltd. | https://www.sec.gov/Archives/edgar/data/1771279/000104746919003772/a2239004zex-10_7.htm | sports | large | CN | vc | en | 2026-11-12 |
| s20 | Techwell, Inc. | https://www.sec.gov/Archives/edgar/data/1171529/000104746906004838/a2169110zex-10_9.htm | business | mid | US | vc | en | 2026-11-12 |
| s21 | Solar Night Industries, Inc. (Farmergy) | https://www.sec.gov/Archives/edgar/data/1371659/000101376207000078/ex1018.htm | utilities | small | US | jv | en | 2026-11-12 |
| s22 | VIA optronics AG | https://www.sec.gov/Archives/edgar/data/1769116/000104746920004927/a2242386zex-10_1.htm | business | large | EU (DE) | jv | en | 2026-11-12 |
| s23 | YX Asset Recovery Ltd | https://www.sec.gov/Archives/edgar/data/1752234/000104746919005965/a2239926zex-10_19.htm | finance | mid | CN | vc | en | 2026-11-12 |
| s25 | Kona Grill, Inc. | https://www.sec.gov/Archives/edgar/data/1265572/000095015305001671/p70737a2exv4w2.txt | food-drink | large | US | vc | en | 2026-11-12 |
| s26 | Eloqua, Inc. | https://www.sec.gov/Archives/edgar/data/1375271/000095012312007922/w83941a5exv4w3.htm | b2b-saas | mid | US | vc | en | 2026-11-12 |
| s31 | SVCA and Singapore Academy of Law (VIMA 2.0) | https://www.svca.org.sg/sites/default/files/2022-09/VIMA%202.0%20Model%20Founders%27%20Agreement%20%28Revised%29%20%28clean%29.docx | standard-form | none | SG | founder | en | 2026-11-12 |
| s32 | Seedcamp (Seedhack) | https://seedcamp.com/wp-content/uploads/2012/11/Seedhack_Founder_Collaboration_Agreement.doc | standard-form | none | UK | founder | en | 2026-11-12 |
| s33 | Startup Foundation (seriesseed.fi, StartupTools) | https://raw.githubusercontent.com/seriesseedfi/seriesseedfi_documents/master/seriesseed.fi%20StartupTools%20FI%20-%20Shareholders'%20Agreement%20(without%20investors)%202021-03-09.docx | standard-form | none | EU (FI) | founder | en | 2026-11-12 |
| s34 | NVCA (National Venture Capital Association) | https://nvca.org/wp-content/uploads/2026/06/Voting-Agreement-Updated-June-2026.docx | standard-form | none | US | vc | en | 2026-11-12 |
| s35 | UK Private Capital (formerly BVCA) | https://web.archive.org/web/20230311044021if_/https://www.bvca.co.uk/Portals/0/Documents/Policy/Model%20Documents%20for%20Early-Stage%20Investments/2023/02-23%20-%20BVCA%20-%20Shareholders'%20Agreement.docx | standard-form | none | UK | vc | en | 2026-11-12 |

## Lessons

- **Read the term clause at selection.** For shareholders' agreements filed with an IPO
  registration statement, the title and parties do not show whether the agreement ends at the IPO
  or starts there. Grepping the term clause for the IPO trigger before dispatch would have saved
  two extractions (s01, s24).
- **Model forms keep their notes outside the body.** `textutil` drops Word footnotes (SVCA, NVCA,
  UK Private Capital) and comments (StartupTools); read `word/footnotes.xml` and
  `word/comments.xml` too.
- **Row granularity varies with the text, not the rule.** Tables ran from 10 to 67 rows. Mapping
  rows to ids in `section-map.md` and counting by script kept the merge checkable, as in the terms
  of service.

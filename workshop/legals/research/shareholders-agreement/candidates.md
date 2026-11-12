---
doc_id: shareholders-agreement
built: 2026-11-12
routes_run: [R8, R9]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (5 slices). Scope (what counts as this document) is in
`extract-notes.md` *What the document is*. Size is an estimate per `sources.md`, from the filer;
for a joint-venture agreement the filer is the party that filed it. Standard forms (`size: none`)
are listed separately, one per project, and kept to at most one in four samples; they are
numbered from s31 so the sized pool keeps s01–s30.

## Standard forms

Pool order for the standard forms: founder-stage models first (the skeleton's purpose), then the
two `sources.md` names (NVCA, UK Private Capital), then the rest. Each project counts once
(`sources.md` *Few public samples*); the project's other documents in `pool/r9-models.md` are not
candidates. Every URL below was opened at selection (title and first screen read).

| # | Sample | Project | Document | URL | Law | Stage | Words |
|---|---|---|---|---|---|---|---|
| f1 | s31 | SVCA and Singapore Academy of Law (VIMA 2.0) | Model Founders' Agreement (revised, clean), Sept 2022 | https://www.svca.org.sg/sites/default/files/2022-09/VIMA%202.0%20Model%20Founders%27%20Agreement%20%28Revised%29%20%28clean%29.docx | SG | founder | ~9,500 |
| f2 | s32 | Seedcamp | Seedhack Founder Collaboration Agreement v2.0, Nov 2012 | https://seedcamp.com/wp-content/uploads/2012/11/Seedhack_Founder_Collaboration_Agreement.doc | UK | founder (pre-incorporation) | ~500 |
| f3 | s33 | Startup Foundation (seriesseed.fi, StartupTools) | Shareholders' Agreement (without investors), 9 Mar 2021, CC BY 3.0 | https://raw.githubusercontent.com/seriesseedfi/seriesseedfi_documents/master/seriesseed.fi%20StartupTools%20FI%20-%20Shareholders'%20Agreement%20(without%20investors)%202021-03-09.docx | FI | founder | ~9,300 |
| f4 | s34 | NVCA | Voting Agreement, updated June 2026 | https://nvca.org/wp-content/uploads/2026/06/Voting-Agreement-Updated-June-2026.docx | US-DE | vc | ~9,700 |
| f5 | s35 | UK Private Capital (formerly BVCA) | Model Shareholders' Agreement, Feb 2023 (Wayback copy of the bvca.co.uk file; the Feb 2025 edition needs a member login) | https://web.archive.org/web/20230311044021if_/https://www.bvca.co.uk/Portals/0/Documents/Policy/Model%20Documents%20for%20Early-Stage%20Investments/2023/02-23%20-%20BVCA%20-%20Shareholders'%20Agreement.docx | UK | vc | ~16,300 |
| f6 | s36 | MaRS Discovery District | Sample Shareholders Agreement (Ontario start-ups) | https://learn.marsdd.com/wp-content/uploads/2013/10/Sample-Shareholders-Agreement.doc | CA-ON | founder / seed | ~8,700 |
| f7 | s37 | SECA (Swiss Private Equity & Corporate Finance Association) | Shareholders Agreement, light edition | https://www.seca.ch/media/nnvph3c2/c-seca-shareholders-agreement_light.docx | CH | seed | ~7,800 |
| f8 | s38 | CVCA | Unanimous Shareholder Agreement (not NVCA), Nov 2018 | https://www.cvca.ca/download/unanimous-shareholders-agreement-not-nvca-2018/?wpdmdl=1260 | CA | vc | ~39,500 |

Unreachable at selection (not candidates): Startup Estonia Founders' Agreement 2026 (Frontify
share pages render only with JavaScript), Seedsummit Denmark collaboration agreements (the
Dropbox shared links are disabled), AirTree Open Source VC (email form), Startup Commons (web form).

## Pool

Pool order rotates size (large, mid, small), stage (`founder`, `early`, `jv`, `vc`; see
`extract-notes.md`) and base, so the first batch mixes founder-level texts with the investor-stage
agreements that make up most of EDGAR. Founder-level and few-owner agreements are placed early in
each size. Every URL was opened at selection (title, parties, first screen), and the term clause
was read to keep out agreements that start at an IPO. Group check (rule 5) done: no two candidates
share an owner group. Sector cap: no sector above 7 of 30 (business 7, medical 5).

c01 was dispatched before the term check and came back invalid (it starts at the IPO); the
selection was then finished with the term check, and the large position it held is filled by the
next large candidate (c16), per `build.md` step 2.

| # | Sample | Company | Document | URL | Sector | Size | Base | Stage | Words | Route |
|---|---|---|---|---|---|---|---|---|---|---|
| c01 | s01 | On Holding AG | Shareholders' Agreement (founders' pool) | https://www.sec.gov/Archives/edgar/data/1858985/000119312521265974/d175570dex101.htm | shopping | large | EU (CH) | founder | ~9,300 | R8 |
| c02 | s02 | IronPlanet, Inc. | Third Amended and Restated Voting Agreement (company, founder, holders) | https://www.sec.gov/Archives/edgar/data/1481441/000095012310043696/f55123a1exv10w11.htm | e-commerce | mid | US | vc | ~2,900 | R8 |
| c03 | s03 | Collective Wisdom Technologies, Inc. | Form of Shareholders Agreement (founders and later shareholders) | https://www.sec.gov/Archives/edgar/data/1741298/000121390018011367/f1a2018a1ex3_collective.htm | productivity | small | US | founder | ~6,000 | R8 |
| c04 | s04 | Materialise NV | Shareholders' Agreement (founders, family holding companies, investors) | https://www.sec.gov/Archives/edgar/data/1091223/000119312514153215/d655315dex43.htm | graphics-design | large | EU (BE) | early | ~2,800 | R8 |
| c05 | s05 | Tennessee Commerce Bancorp, Inc. | Shareholders' Agreement (founding shareholders of a start-up bank) | https://www.sec.gov/Archives/edgar/data/1323033/000110465905019396/a05-7681_1ex4d1.htm | finance | mid | US | founder | ~2,500 | R8 |
| c06 | s06 | Royal Bakery Holdings, Inc. | Agreement Among the Shareholders | https://www.sec.gov/Archives/edgar/data/1594485/000121390013007493/fs12013ex9i_royalbakery.htm | food-drink | small | CN (HK) | early | ~5,100 | R8 |
| c07 | s07 | SFX Entertainment, Inc. (ID&T) | ID&T Worldwide Shareholders' Agreement (two corporate owners) | https://www.sec.gov/Archives/edgar/data/1553588/000104746913008772/a2216461zex-4_7.htm | entertainment | large | EU (NL) | jv | ~24,300 | R8 |
| c08 | s08 | Merus B.V. | Shareholders' Agreement (company, all shareholders, a founder) | https://www.sec.gov/Archives/edgar/data/1651311/000119312516434605/d29248dex1011.htm | medical | mid | EU (NL) | vc | ~21,600 | R8 |
| c09 | s09 | Lantis Laser Inc. | Joint Venture Shareholders Agreement | https://www.sec.gov/Archives/edgar/data/1413299/000114420408036539/v117346_ex10-14.htm | medical | small | US | jv | ~3,400 | R8 |
| c10 | s10 | Wix.com Ltd. | Amended and Restated Shareholders Agreement | https://www.sec.gov/Archives/edgar/data/1576789/000119312513407296/d541565dex101.htm | productivity | large | IL | vc | ~12,600 | R8 |
| c11 | s11 | ReWalk Robotics Ltd. (Argo Medical Technologies) | Fourth Amended and Restated Shareholders Agreement | https://www.sec.gov/Archives/edgar/data/1607962/000119312514270079/d724635dex1010.htm | medical | mid | IL | vc | ~2,500 | R8 |
| c12 | s12 | VME Companies, Inc. (VME Process) | Shareholder Agreement (company, shareholders and their spouses) | https://www.sec.gov/Archives/edgar/data/2113640/000157587226000691/vmec004_ex10-3.htm | business | small | US | early | ~12,700 | R8 |
| c13 | s13 | IPG Photonics Corporation | Stockholders Agreement (company, founder, investors) | https://www.sec.gov/Archives/edgar/data/1111928/000095013506006288/b61608a2exv10w43.txt | business | large | US | early | ~15,100 | R8 |
| c14 | s14 | First Mercury Financial Corp. | Stockholders Agreement (company, investors, management holders) | https://www.sec.gov/Archives/edgar/data/929186/000095013706010763/c05689a3exv10w23.htm | finance | mid | US | early | ~9,800 | R8 |
| c15 | s15 | Monaker Group, Inc. | Founding Shareholders' Agreement (investor, founder, other shareholders of a new company) | https://www.sec.gov/Archives/edgar/data/1372183/000158069521000020/ex10-31.htm | travel | small | EU (CH) | founder | ~9,500 | R8 |
| c16 | s16 | Transport America (Patriot Holding Corp.) | Shareholders' Agreement (company and two holder groups) | https://www.sec.gov/Archives/edgar/data/1582854/000104746913011241/a2217600zex-4_2.htm | business | large | US | early | ~8,400 | R8 |
| c17 | s17 | Advanced Accelerator Applications S.A. | Shareholders Agreement (all shareholders, form) | https://www.sec.gov/Archives/edgar/data/1611787/000157104915000062/t1402271_ex4-3.htm | medical | mid | EU (FR) | vc | ~2,500 | R8 |
| c18 | s18 | Pure Play Media Holdings, Inc. | Shareholders Agreement (five shareholders and the company) | https://www.sec.gov/Archives/edgar/data/1328784/000112785506000394/pureplayexh10_2.htm | entertainment | small | US | early | ~12,100 | R8 |
| c19 | s19 | Wanda Sports Group Co. Ltd. | Shareholders' Agreement (two corporate owners and co-investors) | https://www.sec.gov/Archives/edgar/data/1771279/000104746919003772/a2239004zex-10_7.htm | sports | large | CN | jv | ~20,000 | R8 |
| c20 | s20 | Techwell, Inc. | Second Amended and Restated Voting Agreement (company, preferred holders, founders) | https://www.sec.gov/Archives/edgar/data/1171529/000104746906004838/a2169110zex-10_9.htm | business | mid | US | vc | ~7,500 | R8 |
| c21 | s21 | Solar Night Industries, Inc. (Farmergy) | Shareholders Agreement (company, two individuals, corporate owner) | https://www.sec.gov/Archives/edgar/data/1371659/000101376207000078/ex1018.htm | utilities | small | US | early | ~3,100 | R8 |
| c22 | s22 | VIA optronics AG | Shareholders' Agreement (company, founders, investor) | https://www.sec.gov/Archives/edgar/data/1769116/000104746920004927/a2242386zex-10_1.htm | business | large | EU (DE) | early | ~6,400 | R8 |
| c23 | s23 | YX Asset Recovery Ltd | Shareholders Agreement (company, founders, corporate holders) | https://www.sec.gov/Archives/edgar/data/1752234/000104746919005965/a2239926zex-10_19.htm | finance | mid | CN | early | ~20,000 | R8 |
| c24 | s24 | Forward Pharma A/S | Shareholders' Agreement (company and venture funds) | https://www.sec.gov/Archives/edgar/data/1604924/000104746914007586/a2221285zex-4_4.htm | medical | small | EU (DK) | vc | ~3,900 | R8 |
| c25 | s25 | Kona Grill, Inc. | Stockholders' Agreement (company, preferred investors, common holders) | https://www.sec.gov/Archives/edgar/data/1265572/000095015305001671/p70737a2exv4w2.txt | food-drink | large | US | vc | ~4,700 | R8 |
| c26 | s26 | Eloqua, Inc. | Amended and Restated Stockholders Agreement | https://www.sec.gov/Archives/edgar/data/1375271/000095012312007922/w83941a5exv4w3.htm | b2b-saas | mid | US | vc | ~13,700 | R8 |
| c27 | s27 | Mobile Global Esports, Inc. | SII-MOGO Founders Agreement (company and founder entity) | https://www.sec.gov/Archives/edgar/data/1886362/000121390022013901/ea156941ex10-3_mobile.htm | sports | small | US | founder | ~7,100 | R8 |
| c28 | s28 | RealPage, Inc. | Fifth Amended and Restated Shareholders Agreement | https://www.sec.gov/Archives/edgar/data/1286225/000095012310056348/d71244a1exv4w7.htm | b2b-saas | large | US | vc | ~11,700 | R8 |
| c29 | s29 | Sequans Communications S.A. | Shareholders' Agreement (founders, investors, company) | https://www.sec.gov/Archives/edgar/data/1383395/000119312511087400/dex41.htm | business | mid | EU (FR) | vc | ~47,000 | R8 |
| c30 | s30 | Stalwart Tankers Inc. | Shareholders Agreement (two individual owners) | https://www.sec.gov/Archives/edgar/data/1586023/000156761914000152/s000115x7_ex10-4.htm | business | small | GR | founder | ~150 | R8 |

Sizes: 10 large, 10 mid, 10 small. Sectors: business 7 (c13 c16 c20 c22 c29 c30, c12); medical 5;
finance 3; productivity, entertainment, sports, food-drink, b2b-saas 2; e-commerce, graphics-design,
travel, utilities 1. Bases: US 16, EU 9 (NL 2, FR 2, CH 2, BE, DE, DK), IL 2, CN 2, GR 1.

## Reserve

Used in this order, same size only, when the pool runs out of a size.

| # | Company | Document | URL | Sector | Size | Base | Stage |
|---|---|---|---|---|---|---|---|
| L1 | NXP Semiconductors (SSMC) | Shareholders Agreement (three corporate owners) | https://www.sec.gov/Archives/edgar/data/1413447/000119312510151243/dex104.htm | business | large | SG | jv |
| L2 | Tuya Inc. | Fifth Amended and Restated Shareholders' Agreement | https://www.sec.gov/Archives/edgar/data/1829118/000119312521079368/d75491dex44.htm | developer-tools | large | CN | vc |
| L3 | Applied Medical Corp | Amended and Restated Voting Agreement (founders) | https://www.sec.gov/Archives/edgar/data/1534727/000119312512397400/d253118dex41.htm | medical | large | US | founder |
| L4 | Yandex N.V. | Second Amended and Restated Shareholders Agreement | https://www.sec.gov/Archives/edgar/data/1513845/000104746911004772/a2203977zex-10_1.htm | utilities | large | EU (NL) | vc |
| M1 | Ambrx Biopharma Inc. | Shareholders Agreement | https://www.sec.gov/Archives/edgar/data/1836056/000119312521189441/d108474dex44.htm | medical | mid | US | vc |
| M2 | Isilon Systems, Inc. | Fourth Amended and Restated Voting Agreement | https://www.sec.gov/Archives/edgar/data/1373671/000089102006000330/v23215a2exv10w31.txt | b2b-saas | mid | US | vc |
| M3 | EqualLogic Inc. | Third Amended and Restated Stockholders Agreement | https://www.sec.gov/Archives/edgar/data/1157743/000104746907007332/a2179778zex-10_18.htm | b2b-saas | mid | US | vc |
| M4 | Gmarket Inc. | Shareholders Agreement (two principal holders; runs past the IPO, check at extraction) | https://www.sec.gov/Archives/edgar/data/1365241/000114554906000800/h00223a1exv4w3.txt | shopping | mid | KR | jv |
| S1 | Nanotailor, Inc. | Shareholder's Agreement | https://www.sec.gov/Archives/edgar/data/1444819/000143209309000017/ex10-4.htm | business | small | US | jv |
| S2 | Triangle 9 Real Estate, Inc. | Shareholders Agreement (founding and investing shareholders) | https://www.sec.gov/Archives/edgar/data/1878137/000147793221006427/tria_ex101.htm | lifestyle | small | US | founder |
| S3 | Peru Copper Inc. | Shareholders' Agreement | https://www.sec.gov/Archives/edgar/data/1307111/000119312505037460/dex1040.htm | business | small | CA | early |
| S4 | Ultimax Digital, Inc. | Voting Agreement | https://www.sec.gov/Archives/edgar/data/1878543/000147793222008639/ultimax_109.htm | entertainment | small | US | early |
| S5 | Nexvet Biopharma plc | Shareholders' agreement | https://www.sec.gov/Archives/edgar/data/1618561/000119312515019154/d775834dex42.htm | medical | small | IE | vc |

## Dropped at selection

| Company | Slice | Reason |
|---|---|---|
| D-Market (Hepsiburada) | r8-shareholders | Takes effect at the IPO and replaces the pre-IPO agreement (rule 6, *Out*). |
| Mimecast Limited | r8-shareholders | A short deed that ends the original agreement and binds the parties to a similar one with the new holding company; the agreement itself is not in it. |
| trivago (travel B.V.) | r8-shareholders | Amended and restated in connection with the IPO; governs the listed company. |
| Avast Software N.V. | r8-shareholders | Part of its rights start after the IPO. |
| Airbnb, Inc. | r8-voting | Founders' voting agreement for board seats after the IPO. |
| Sprout Social, Inc. | r8-voting | Founder proxy tied to the IPO's dual-class structure. |
| Rackable Systems, Inc. | r8-founders | Only an amendment is filed; the original founders agreement is not on EDGAR. |
| Ultrapar Holdings | r8-shareholders | Controlling holders of an already listed company. |

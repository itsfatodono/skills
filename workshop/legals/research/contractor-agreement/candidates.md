---
doc_id: contractor-agreement
built: 2026-11-12
routes_run: [R8, R9]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (7 slices: `r8-consulting-a`, `r8-consulting-b`,
`r8-contractor`, `r8-freelance-topics`, `r8-large`, `r8-forms`, `r9-forms`). Size is an estimate per
`sources.md` (headcount from what is known, never researched). Sector per `sources.md`: the App
Store category the filer's main product would take, or `b2b-saas`, `developer-tools`,
`e-commerce`.

## Fit rule (judgement call)

The skeleton serves a startup or solo developer engaging an outside freelancer or firm (a
designer, a developer, a marketer, an accountant). Most EDGAR "Consulting Agreements" are filed
because they are material related-party deals: a departing executive kept on as a consultant, a
director paid for advice, a founder's continuing role. Those are a different deal (they carry
separation releases, equity vesting carry-overs, board duties) and were left out at selection:

- **Kept:** an agreement under which a company engages an outside individual or firm for defined
  services, whatever the trade (software, design, marketing, accounting, scientific, business
  development), including a fractional functional role that carries no officer title (an acting head of
  sales and marketing, an outsourced bookkeeping team), and an agreement filed by the
  consultant rather than the client.
- **Left out:** a text that carries the terms of another relationship with the consultant: a
  departure from employment or board service (separation or transition terms, a retirement,
  continued vesting under a separation agreement), or an appointment as a corporate officer or
  director (an officer or board title, D&O cover, board duties); also an investor's advisory
  fee and a reverse related-party expense deal. The text decides. At selection only the first
  screen and general knowledge are in hand, so a filer whose consultant had just left an
  executive post or sat on the board was skipped there as likely to carry such terms; once a
  text is read, a clean services engagement is kept even if the performer also sits on the
  board (s07). A text that fails is recorded in `invalid.md` (rule 6, scope) and replaced by the
  next unused same-size candidate in pool order.

## Group check (rule 5)

One candidate per filer group. Aviat Networks and Aviat U.S. are one group; eXp World Holdings
and AGNT are one group; VenHub filed five consulting agreements on one form (exhibits 10.8–10.12),
one taken. Allogene and Bello Capital are not taken. No other two filers share an owner.

## Pool

Pool order rotates size (large, mid, small) for the first 15 and then sets one standard form
after every three company samples. `standard-form` samples are `size: none`, outside the size
thirds, and at most one in four samples (`sources.md` *Few public samples*); each project counts
once (Common Paper's ICA is taken, its PSA is not).

| # | Company | Exhibit / form | URL | Sector | Size | Base | Language | Route |
|---|---|---|---|---|---|---|---|---|
| c01 | Schrödinger, Inc. | Consultant Agreement, Richard Friesner (EX-10.24, 10-K 2026) | https://www.sec.gov/Archives/edgar/data/1490978/000149097826000010/sdgr-20251231xxex1024fries.htm | b2b-saas | large | US | en | R8 |
| c02 | Immunome, Inc. | Consulting Agreement, task-order form (EX-10.33, 10-K 2024) | https://www.sec.gov/Archives/edgar/data/1472012/000155837024004247/tmb-20231231xex10d33.htm | medical | mid | US | en | R8 |
| c03 | HUMBL, Inc. | Master Consulting Services Agreement, BRU LLC (EX-10.1, 8-K 2023) | https://www.sec.gov/Archives/edgar/data/1119190/000149315223026900/ex10-1.htm | finance | small | US | en | R8 |
| c04 | REX American Resources Corp. | Consulting Services Agreement, Mercury Public Affairs (EX-10.(F), 10-K 2026) | https://www.sec.gov/Archives/edgar/data/744187/000093041326000937/c115944_ex10-f.htm | business | large | US | en | R8 |
| c05 | Data I/O Corporation | Independent Contractor Agreement and Statement of Work, TAG CXO (EX-10.38, 10-Q 2025) | https://www.sec.gov/Archives/edgar/data/351998/000165495425009427/daio_ex1038.htm | business | mid | US | en | R8 |
| c06 | Ludwig Enterprises, Inc. | Consulting Agreement, The Fannon Group (EX-10.10, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1960262/000190359623000540/ex10-10.htm | medical | small | US | en | R8 |
| c07 | Forescout Technologies, Inc. | Consulting Agreement, Night Dragon II LLC (EX-10.1, 8-K 2019) | https://www.sec.gov/Archives/edgar/data/1145057/000114505719000031/a06072019101.htm | utilities | large | US | en | R8 |
| c08 | Athena Bitcoin Global | Consulting Agreement, 4C LLC (EX-10.41, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1095146/000168316823007999/athbitcoin_ex1040.htm | finance | mid | US | en | R8 |
| c09 | Fashionista Distributor Holdings Inc. | Design Consulting Agreement, filer as consultant (EX-10.6, S-1/A 2024) | https://www.sec.gov/Archives/edgar/data/2004256/000173112224000879/e5692_ex10-6.htm | lifestyle | small | TW | en | R8 |
| c10 | CareCloud, Inc. | Consulting Agreement, Stochastic Solutions LLC (EX-10.40, 10-K 2026) | https://www.sec.gov/Archives/edgar/data/1582982/000149315226009872/ex10-40.htm | medical | large | US | en | R8 |
| c11 | Arvinas, Inc. | Consulting Agreement, Jan Taylor (EX-10.4, 10-Q 2026) | https://www.sec.gov/Archives/edgar/data/1655759/000162828026052554/exhibit104-fullitaylorco.htm | medical | mid | US | en | R8 |
| c12 | Astrotech Corporation | Independent Contractor Agreement, With Finance Team LLC (EX-10.3, 8-K/A 2025) | https://www.sec.gov/Archives/edgar/data/1001907/000143774925001818/ex_769151.htm | business | small | US | en | R8 |
| c13 | Under Armour, Inc. | Consulting Services Agreement, Yassine Saidi (EX-10.48, 10-K 2026) | https://www.sec.gov/Archives/edgar/data/1336917/000133691726000073/ua-03312026xex1048consulti.htm | shopping | large | US | en | R8 |
| c14 | Trecora Resources | Consulting Services Agreement, Joseph Tanner (EX-10.15, 10-K 2021) | https://www.sec.gov/Archives/edgar/data/7039/000000703921000036/tannerconsultingservices.htm | business | mid | US | en | R8 |
| c15 | Nexscient, Inc. | Consulting Agreement, MJP Consulting LLC (EX-10.4, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1976663/000147793223007753/nexscient_ex104.htm | b2b-saas | small | US | en | R8 |
| c16 | Common Paper | Independent Contractor Agreement (cover page, SOW and standard terms in one docx) | https://commonpaper.com/documents/common-paper-independent-contractor-agreement-docx | standard-form | none | US | en | R9 |
| c17 | Clear Secure, Inc. | Consulting Services Agreement, Matthew Levine (EX-10.16, 10-K 2024) | https://www.sec.gov/Archives/edgar/data/1856314/000185631424000023/consultingagreement-levine.htm | travel | large | US | en | R8 |
| c18 | Ceribell, Inc. | Consulting Agreement, Josef Parvizi (EX-10.28, S-1/A 2024) | https://www.sec.gov/Archives/edgar/data/1861107/000095017024113073/cbll-ex10_28.htm | medical | mid | US | en | R8 |
| c19 | Mangoceuticals, Inc. | Consulting Agreement, Justin Baker (EX-10.33, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1938046/000149315223002627/ex10-33.htm | health-fitness | small | US | en | R8 |
| c20 | Bonterms | Professional Services Agreement v1.2 (standard terms pdf, cover page docx) | https://framerusercontent.com/assets/3owa7Qh705NnKztfpxY5tU0Nfs.pdf | standard-form | none | US | en | R9 |
| c21 | Marcus & Millichap, Inc. | Consulting Services Agreement, L5K Investments (EX-10.1, 10-Q 2020) | https://www.sec.gov/Archives/edgar/data/1578732/000119312520138459/d183092dex101.htm | finance | large | US | en | R8 |
| c22 | Nuvve Holding Corp. | Consulting Services Agreement, Bristol Capital LLC (EX-10.2, 8-K 2025) | https://www.sec.gov/Archives/edgar/data/1836875/000183687525000095/nvve-102bristolconsultinga.htm | utilities | mid | US | en | R8 |
| c23 | VenHub Global, Inc. | Consulting Agreement, Worldwide Acquisitions LLC (EX-10.12, S-1/A 2026) | https://www.sec.gov/Archives/edgar/data/1972234/000121390026074328/ea029640801ex10-12.htm | shopping | small | US | en | R8 |
| c24 | NYC Department of Consumer and Worker Protection | Freelance Work Agreement (model contract), 2025-01-23 | https://www.nyc.gov/assets/dca/downloads/pdf/workers/Model-Contract-Freelance.pdf | standard-form | none | US | en | R9 |
| c25 | Aviat Networks, Inc. | Independent Contractor Agreement, Bryan Tucker (EX-10.2, 8-K 2023) | https://www.sec.gov/Archives/edgar/data/1377789/000137778923000037/independentcontractoragree.htm | business | large | US | en | R8 |
| c26 | CaliberCos Inc. | Sponsor Consulting Agreement, Skyway Capital Markets (EX-10.15, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1627282/000110465923044483/tm2230806d15_ex10-15.htm | finance | mid | US | en | R8 |
| c27 | Aureus Greenway Holdings Inc. | Advisory / Consulting Services Agreement, C&H Capital (EX-10.3, 8-K 2026) | https://www.sec.gov/Archives/edgar/data/2009312/000149315226012209/ex10-3.htm | sports | small | US | en | R8 |
| c28 | AIGA | Standard Form of Agreement for Design Services (2020) | https://www.aiga.org/sites/default/files/2021-04/standard-form-of-agreement-for-design-services.pdf | standard-form | none | US | en | R9 |
| c29 | Miami Breeze Car Care Inc. | Independent Marketing Consultant Agreement, Sky Breeze Capital (EX-10.2B, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1872066/000152013823000469/miam-s1a5ex10z2b.htm | lifestyle | small | US | en | R8 |
| c30 | Freelancers Union | Contract Creator (freelance contract) | https://freelancersunion.org/contract/ | standard-form | none | US | en | R9 |

## Reserve

Used in this order, same size only, when a size's candidate is unreachable, a copy, or out of
scope.

| # | Company | Exhibit / form | URL | Sector | Size | Base | Route |
|---|---|---|---|---|---|---|---|
| M1 | FDCTECH, Inc. | Consulting Agreement, LUX Limited (EX-10.13, S-1/A 2026) | https://www.sec.gov/Archives/edgar/data/1722731/000149315226044195/ex10-13.htm | finance | mid | US | R8 |
| M2 | Foghorn Therapeutics Inc. | Consulting Agreement, scientific co-founder (EX-10.18, S-1/A 2020) | https://www.sec.gov/Archives/edgar/data/1822462/000119312520271564/d12441dex1018.htm | medical | mid | US | R8 (`r8-forms`) |
| S1 | Healing Co Inc. | Independent Contractor Agreement, KET Consulting (EX-10.7, 10-Q 2022) | https://www.sec.gov/Archives/edgar/data/1441082/000147793222001015/thcc_ex107.htm | health-fitness | small | US | R8 |
| S2 | Vertical Data Inc. | Consulting Agreement, Conway Merchants (EX-10.2, S-1/A 2025) | https://www.sec.gov/Archives/edgar/data/2033264/000164117225008151/ex10-2.htm | developer-tools | small | US | R8 |
| S3 | RVeloCITY, Inc. | Amended & Restated Consulting Agreement, GFH Consulting (EX-10.18, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1886444/000149315223008980/ex10-18.htm | travel | small | US | R8 |
| S4 | Alternative Ballistics Corp | Business Consulting Services Agreement, Aries Capital (EX-10.25, S-1 2026) | https://www.sec.gov/Archives/edgar/data/1834868/000149315226046881/ex10-25.htm | business | small | US | R8 |
| S5 | Adaptin Bio, Inc. | Consulting Agreement, Adamanteus LLC (EX-10.16, S-1/A 2025) | https://www.sec.gov/Archives/edgar/data/1938571/000121390025058957/ea024660901ex10-16_adaptin.htm | medical | small | US | R8 |
| S6 | General Enterprise Ventures, Inc. | Consulting Agreement, Nanuk Warman (EX-10.7, S-1/A 2025) | https://www.sec.gov/Archives/edgar/data/894556/000164033425000946/gevi_ex107.htm | business | small | US | R8 |
| S7 | Eloxx Pharmaceuticals, Inc. | Consulting Agreement, Danforth Advisors (EX-10.16, S-1/A 2026) | https://www.sec.gov/Archives/edgar/data/1035354/000119312526251655/d35071dex1016.htm | medical | small | US | R8 |
| S8 | Acasti Pharma Inc. | Independent Contractor Agreement, PFC Business Advisory (EX-10.6, 10-K 2021) | https://www.sec.gov/Archives/edgar/data/1444192/000117184321004462/exh_106.htm | medical | small | CA | R8 |
| S9 | Rapid Therapeutic Science Laboratories | Independent Contractor Agreement, We the 23 LLC (EX-10.1, 8-K 2021) | https://www.sec.gov/Archives/edgar/data/1575659/000139390521000284/rtsl_ex101.htm | health-fitness | small | US | R8 |
| S10 | Flewber Global Inc. | Consulting Agreement, Carmit Cohen (EX-10.42, S-1/A 2023) | https://www.sec.gov/Archives/edgar/data/1864776/000121390023099113/fs12023a8ex10-42_flewber.htm | travel | small | US | R8 |
| S11 | iSpecimen Inc. | Form of Consulting Agreement, IR Agency LLC (marketing and advertising) (EX-10.47, S-1/A 2026) | https://www.sec.gov/Archives/edgar/data/1558569/000121390026078869/ea029813601ex10-47.htm | medical | small | US | R8 (`r8-forms`) |
| S12 | Veri MedTech Holdings, Inc. | Form of Consulting Agreement, blank (EX-10.3, S-1/A 2026) | https://www.sec.gov/Archives/edgar/data/2078149/000109690626000221/vrhi_ex10z3.htm | b2b-saas | small | US | R8 (`r8-forms`) |
| S13 | JOFF Fintech Acquisition Corp. | Form of Consulting Agreement, MFA Growth LLC (EX-10.9, S-1/A 2021) | https://www.sec.gov/Archives/edgar/data/1824149/000121390021004688/ea134047ex10-9_jofffintech.htm | finance | small | US | R8 (`r8-forms`) |
| F1 | Cooley GO | Form of Consulting Agreement (US), generator | https://www.cooleygo.com/documents/form-consulting-agreement/ (blocked) | standard-form | none | US | R9 |
| F2 | Orrick | Consulting Agreement, Start-Up Forms Library | https://www.orrick.com/en/tech-studio/forms/Consulting-Agreement (blocked) | standard-form | none | US | R9 |

## Left out at selection

By the fit rule above (first screen): Perpetua Resources, Trinity Place, Allogene, Generation
Bio, CervoMed, BeiGene, Cushman & Wakefield, Arbutus, Open Text, Roivant, USA Compression,
Werner (departing executive, director or retiree); Entera Bio, Go Green Global, iSpecimen,
Firefly Neuroscience, Apimeds, SeqLL, Retension (officer or board title); Emulate Therapeutics,
Edison Oncology (founders' own consulting roles); VisitIQ (investor's advisory fee); USBC
(reverse related-party expense deal). Left out from general knowledge that the consultant had
just left an executive post at the filer (8-K departure filings): Super Micro (Kao), Zynex
(Moorhead), Innovex (McClure), SentinelOne (Warner), DiaMedica (Gruis), Pliant (Lefebvre).
From `r8-large`, left out from general knowledge that the consultant had just left an
executive post or sat on the board (the first screen did not say): Sage (Robichaud), Pacira
(Reinhart), Pure Storage (Riitters), Etsy (Fish Scalability), Arena (Spector), Akebia (Canute,
director), Azenta (8-K departure filing). Common Paper PSA: same project as c16. Not taken because the small third was already full and
their fit is weaker (unnamed "services", a principal's family tie, a scientific founder's open
retainer): Adamas One, JanOne, Ocean Biomedical. Seen by a collector but beyond its row target:
Gaming Technologies, SOS Hydration. From `r8-forms`: Union Acquisition Corp. II (a SPAC's
consultant on listing, closest to an officer role) not taken. iSpecimen's earlier row (a CEO
engaged as contractor) was never a candidate, so its marketing-agency form (S11) is its group's
only candidate.

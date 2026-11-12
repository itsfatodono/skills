# ip-assignment / r8-small-tail

Route: R8 (SEC EDGAR full-text search, `efts.sec.gov/LATEST/search-index`). Run 2026-11-12. Date range for all queries: 2017-01-01 to 2026-11-01. Pages of 100 hits; every query was read to its last page (all results were 1-3 pages).

## Queries run

Regulation A, forms `1-A,1-A/A,1-A POS,1-K`:

| Phrase | Hits | Pages |
|---|---|---|
| "Invention Assignment" | 184 | 2 |
| "Inventions Assignment" | 13 | 1 |
| "Proprietary Information and Inventions" | 25 | 1 |
| "Confidential Information and Invention" | 14 | 1 |
| "Intellectual Property Assignment" | 109 | 2 |
| "Confidentiality and Invention Assignment" (extra) | 66 | 1 |
| "Inventions Agreement" (extra) | 27 | 1 |
| "Proprietary Information Agreement" (extra) | 37 | 1 |
| "Intellectual Property Contribution" (extra) | 9 | 1 |

Small registrants, forms `10-12G,10-12G/A,S-1,S-1/A,8-K`:

| Phrase | Hits | Pages |
|---|---|---|
| "Confidentiality and Invention Assignment Agreement" | 40 | 1 |
| "Non-Disclosure and Invention Assignment" | 256 | 3 |
| "Employee Invention Assignment" | 146 | 2 |
| "Inventions and Confidentiality Agreement" | 6 | 1 |
| "Employee Proprietary Information Agreement" | 14 | 1 |
| "Invention Assignment and Confidentiality" | 169 | 2 |

Shell and very small companies: "Proprietary Information and Inventions", forms `S-1,S-1/A,8-K,10-K`, `sics=6770,8742,7389,8900,9995`: 15 hits, 1 page.

## Screening

- Hits read: 1,010 (871 distinct filing/file ids after removing repeats across queries).
- Hits that are not exhibits (offering circular / prospectus bodies, `PART II AND III`, `S-1/A` main documents): 606, not screened (the agreement is not a file of its own there).
- Exhibit files fetched and read (title, first screen, attached-agreement check): 230 files from 88 filers.
- Kept: 10 rows (one per company, latest filing).
- Skipped: 78 filers, by reason:
  - 62: offer letter, employment agreement, board/consulting agreement, equity plan or severance letter that only mentions the agreement or has the terms inline (no separate agreement attached): Prometheum, Venator, MongoDB, Passage Bio, Kiromic, Dropbox, DoorDash, Flywire, Airbnb, Compass, Gitlab, Figma, Knightscope, CaliberCos, Turo (11 letters: they only refer to an agreement signed earlier) and others.
  - 6: the exhibit has the attachment heading but no text after it (Tivic Health, Lyft, LegalZoom, Nordicus Partners, Tranquil Healthcare Fund, NAVA Health: its exhibit is a non-compete/NDA, no invention assignment).
  - 1: image-only / unreadable text (BiologX, IP assignment agreement, text length 113 characters).
  - 5: corporate-to-corporate transfers, placement/underwriting agreements, securities exchange (Moving iMage Technologies, TerraCycle, Draxo, Anteris, GME Innotainment).
  - 4: other (plans, retention letters, Reg A subscription forms).
- A company with several filings or several exhibits (Opti-Harvest, SpotitEarly, iSpecimen, FlexEnergy, Nordicus, SOS Hydration, Consumer Cooperative Group) counts once; the latest filing is kept.
- Yield is below the target of about 25: the Regulation A and small-registrant tail on EDGAR rarely files the agreement itself as an exhibit. The queries are exhausted; no further queries run beyond the four extra Reg A phrases above.

## Rows

| Company | Filing (form, date) | CIK | Exhibit (type, title as written) | SIC | Headcount (as filed) | Document URL | Filing index |
|---|---|---|---|---|---|---|---|
| SpotitEarly, Inc. | 1-A/A, 2025-11-26 | 2077992 | EX1A-6, Consulting Agreement with Shlomi Madar (Exhibit B: Non-Competition, Proprietary Information and Inventions Agreement) | 8071 | 23 | https://www.sec.gov/Archives/edgar/data/2077992/000109690625001941/spot_ex6z2.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/2077992/000109690625001941/ |
| iSpecimen Inc. | S-1/A, 2021-04-02 | 1558569 | EX-10.25, Executive Employment Agreement (Exhibit D: Noncompetition, Nonsolicitation, Nondisclosure and Inventions Agreement) | 8731 | 41 | https://www.sec.gov/Archives/edgar/data/1558569/000110465921046101/tm2035427d11_ex10-25.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1558569/000110465921046101/ |
| FlexEnergy Green Solutions, Inc. | S-1/A, 2022-01-11 | 1841227 | EX-10.5, Executive Employment Agreement (Confidential Information and Invention Assignment Agreement) | 3620 | 104 | https://www.sec.gov/Archives/edgar/data/1841227/000110465922003239/tm214441d26_ex10-5.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1841227/000110465922003239/ |
| Immunovant, Inc. | S-1/A, 2020-04-08 | 1764013 | EX-10.16, Separation Agreement and General Release (Exhibit C: Employee Non-Disclosure, Invention Assignment and Restrictive Covenant Agreement) | 2836 | 18 (subsidiary; parent none) | https://www.sec.gov/Archives/edgar/data/1764013/000119312520100937/d781885dex1016.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1764013/000119312520100937/ |
| Allovir, Inc. | S-1/A, 2020-07-23 | 1754068 | EX-10.16, Executive Employment Agreement (Exhibit A: Employee Invention Assignment and Confidentiality Agreement) | 2836 | 21 | https://www.sec.gov/Archives/edgar/data/1754068/000119312520197425/d932810dex1016.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1754068/000119312520197425/ |
| Opti-Harvest, Inc. | S-1/A, 2023-02-03 | 1753945 | EX-10.5, Employment Agreement (Exhibit B: Proprietary Information and Inventions Agreement) | 3523 | | https://www.sec.gov/Archives/edgar/data/1753945/000149315223003502/ex10-5.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1753945/000149315223003502/ |
| Greene Concepts, Inc | 1-A/A, 2020-01-10 | 1585380 | Exhibit 6.8, offer letter with Employee Confidential Information and Inventions Assignment Agreement | 2086 | 2 | https://www.sec.gov/Archives/edgar/data/1585380/000172186820000018/f2sinkw010720regaaex6_8.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1585380/000172186820000018/ |
| SOS Hydration Inc. | S-1/A, 2022-09-02 | 1861785 | EX-10.12, offer letter (Exhibit B: Employee Invention Assignment and Confidentiality Agreement) | 2080 | | https://www.sec.gov/Archives/edgar/data/1861785/000190359622000562/f2ssos1a042122ex10_12.htm (attached: rule 6) | https://www.sec.gov/Archives/edgar/data/1861785/000190359622000562/ |
| Consumer Cooperative Group Inc | 1-A/A, 2021-12-16 | 1742162 | EX1A-6, Intellectual Property Contribution and Assignment Agreement (founder to company) | 6500 | 2 | https://www.sec.gov/Archives/edgar/data/1742162/000174216221000016/ipassignmentagreement.htm | https://www.sec.gov/Archives/edgar/data/1742162/000174216221000016/ |
| Naoris Quantum Protocol Inc. | 1-A/A, 2026-09-14 | 2145466 | EX1A-6, Intellectual Property Assignment Agreement (title on cover) / Intellectual Property Acquisition Agreement (title in body) with David Carvalho | | 37 | https://www.sec.gov/Archives/edgar/data/2145466/000121390026099378/ea030277101ex6-8.htm | https://www.sec.gov/Archives/edgar/data/2145466/000121390026099378/ |

Notes:

- Headcount comes from the offering circular or prospectus: SpotitEarly "23 employees" (company and subsidiary); iSpecimen "41 full time employees" at 2020-12-31; FlexEnergy "104 full-time employees" at 2021-11-30; Immunovant "no employees ... subsidiary IMVT Corporation had 18"; Allovir "21 full-time employees" at 2020-07-01; Greene Concepts "two employees"; Consumer Cooperative Group "2 full-time employees"; Naoris "approximately 37 employees engaged through employer-of-record arrangements". Opti-Harvest and SOS Hydration: no count sentence found in the main document, left blank.
- Most rows are the "attached" kind: the filer files an employment or consulting agreement that carries the full invention assignment agreement as an exhibit inside the same file. Standalone documents are Consumer Cooperative Group and Naoris, both founder or contributor assignments and not the employee form; the builder decides whether they qualify.
- Immunovant and Allovir are not small by headcount in the usual sense but are Reg-S-1 registrants returned by the slice; no size call made.
- SIC for Naoris not given in the search index.

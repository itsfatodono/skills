---
doc_id: ip-assignment
built: 2026-11-12
routes_run: [R8, R9]
raw_rows: pool/
---

Selected by the builder from the raw rows in `pool/` (4 R8 slices, 136 raw rows; the R9 slice
yielded no obtainable text, see `pool/r9-forms.md`). Size is an estimate per `sources.md`: the
headcount the filing states where the slice recorded one, otherwise what the builder knows of the
filer. Sector is the App Store category the filer's main product would take (`medical` for biotech
and devices, `business` for industrial and semiconductor firms).

**Selection rules applied.**

- 10 large, 10 mid, 10 small; no sector above 5 of 30 (cap 7).
- **Signer mix.** The item covers founders and employees. Every founder assignment R8 returned comes
  from a filer with 50 or fewer staff: larger companies signed theirs years before they filed and do
  not file them. So size and form are confounded: all six founder forms sit in the small third, beside
  three small-company employee forms and one consultant form. Six founder forms (20%) is the least
  that lets founder-only content reach the *rare* tier instead of *Commonly omitted*, so the
  skeleton can judge whether one document serves both.
- Pool order rotates size (large, mid, small) and sector; the first batch (c01–c15) holds three
  founder forms and two employee forms among its five small.
- **Rule 5 (one per group).** Checked at selection: no two picks share an owner. Duplicates across
  slices (Hawkeye, SITO Mobile, First Advantage, Consumer Cooperative Group, Naoris) are one row each.
  Immunovant (Roivant group) and Vimeo (former IAC) have no sibling in the pool.
- **Rule 4 watch (copies).** Several picks carry common law-firm form titles. Watch, at merge, by
  comparing `raw/` texts: "Employee Invention Assignment and Confidentiality Agreement" (c01 and
  reserves Lyft, Upwork, Samsara, Nextdoor, Intapp, Allovir, authID); "Confidential Information and
  Invention Assignment Agreement" (c11, c13, c16, c17, c27); "Proprietary Information and Inventions
  (Assignment) Agreement" (c05, c07, c08, c19, c20, c22, c28, c29); the Israeli "Non-Competition,
  Proprietary Information and Inventions Agreement" (c21, c23). Reserve shells filed by one agent
  with the same "Proprietary Information, Inventions and Non-Competition Agreement" attached to a
  "Director Retainer Agreement" (King Resources, Tianci, AS Capital, Kronos, Cosmos) are one template:
  at most one of them may be used. Reserve founder forms Cashlin and Spin AI (one filing agent, 2026),
  and Catalyst Crew, Quantum Genesis and Hawkeye (one filing agent, 2025–2026), are likely one template each.
- **Title check.** Every pick was opened (curl, HTML stripped) and its title and first screen read on
  2026-11-12. Where the exhibit is a host agreement (offer letter, employment, consulting, separation,
  compensation), the attached agreement's heading and first-person assignment text were confirmed in
  the same file (rule 6). None dropped.

## Pool

| # | Company | Filing | URL | Sector | Size | Base | Language | Signer | Form in file | Route (slice) |
|---|---|---|---|---|---|---|---|---|---|---|
| c01 | Squarespace, Inc. | S-1 2021-04-16, EX-10.13 | https://www.sec.gov/Archives/edgar/data/1496963/000110465921051251/tm213918d7_ex10-13.htm | business | large | US | en | employee | standalone | R8 (r8-tech) |
| c02 | Molekule Group, Inc. | 10-K/A 2023-04-03, EX-10.11 | https://www.sec.gov/Archives/edgar/data/1872356/000155837023005401/aerc-20221231xex10d11.htm | lifestyle | mid | US | en | employee | standalone | R8 (r8-other) |
| c03 | Modular Medical, Inc. | S-1/A 2019-09-09, EX-10.5 | https://www.sec.gov/Archives/edgar/data/1074871/000101905619000521/ex10_5.htm | medical | small | US | en | founder | standalone | R8 (r8-founder) |
| c04 | Dutch Bros Inc. | 10-Q 2025-11-06, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1866581/000186658125000227/a20250730-dutchbrosxariz.htm | food-drink | large | US | en | employee | standalone | R8 (r8-other) |
| c05 | Rush Street Interactive, Inc. | S-1 2021-02-05, EX-10.8 | https://www.sec.gov/Archives/edgar/data/1793659/000119312521030959/d124075dex108.htm | games | mid | US | en | employee | attached to offer letter | R8 (r8-other) |
| c06 | AppTech Payments Corp. | S-1/A 2021-12-17, EX-10.24 | https://www.sec.gov/Archives/edgar/data/1070050/000157570521000860/ex10_24.htm | finance | small | US | en | employee | attached to employment agreement | R8 (r8-tech) |
| c07 | Snowflake Inc. | 10-K 2025-03-21, EX-10.16 | https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/ex-1016snowflakefy2025q4.htm | developer-tools | large | US | en | employee | attached to employment letter | R8 (r8-tech) |
| c08 | Hippo Holdings Inc. | 8-K 2024-10-09, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1828105/000182810524000043/exhibit101-yuvalharrysep.htm | finance | mid | US | en | employee | attached to separation letter | R8 (r8-other) |
| c09 | Atlan Media, Inc. | S-1/A 2016-08-24, EX-10.3 | https://www.sec.gov/Archives/edgar/data/1673731/000114420416120812/v447586_ex10-3.htm | entertainment | small | AU | en | founder | standalone (deed) | R8 (r8-founder) |
| c10 | Neuronetics, Inc. | 10-K 2025-03-27, EX-10.23 | https://www.sec.gov/Archives/edgar/data/1227636/000155837025003833/stim-20241231xex10d23.htm | medical | large | US | en | employee | standalone | R8 (r8-other) |
| c11 | Credo Technology Group Holding Ltd | S-1 2022-01-03, EX-10.11 | https://www.sec.gov/Archives/edgar/data/1807794/000162828022000095/exhibit1011-sx1.htm | business | mid | US | en | employee | standalone | R8 (r8-tech) |
| c12 | Foxx Development Holdings Inc. | 8-K 2024-10-02, EX-10.37 | https://www.sec.gov/Archives/edgar/data/2013807/000121390024084719/ea021499501ex10-37_foxxdev.htm | b2b-saas | small | US | en | employee | standalone | R8 (r8-tech) |
| c13 | Pinterest, Inc. | 8-K 2026-10-05, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000139/cfo_offerxletterx-xsigne.htm | social-networking | large | US | en | employee | attached to offer letter | R8 (r8-tech) |
| c14 | Codexis, Inc. | 10-K 2023-02-27, EX-10.23A | https://www.sec.gov/Archives/edgar/data/1200375/000120037523000012/sriryaliofferletter_ex1023a.htm | medical | mid | US | en | employee | attached to offer letter | R8 (r8-other) |
| c15 | Consumer Cooperative Group Inc | 1-A/A 2021-12-16, EX1A-6 | https://www.sec.gov/Archives/edgar/data/1742162/000174216221000016/ipassignmentagreement.htm | finance | small | US | en | founder | standalone, with technology assignment exhibit | R8 (r8-founder) |
| c16 | Figure Technology Solutions, Inc. | 10-K 2026-03-16, EX-10.23 | https://www.sec.gov/Archives/edgar/data/2064124/000206412426000009/exhibit1023compensationagr.htm | finance | large | US | en | employee | attached to compensation agreement | R8 (r8-other) |
| c17 | ContextLogic Inc. | 10-K 2024-03-05, EX-10.7 | https://www.sec.gov/Archives/edgar/data/1822250/000095017024025210/wish-ex10_7.htm | shopping | mid | US | en | employee | attached to offer letter | R8 (r8-other) |
| c18 | Loop Industries, Inc. | 10-K 2017-05-30, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1504678/000147793217002605/llpp_ex101.htm | business | small | CA | en | founder | standalone | R8 (r8-founder) |
| c19 | Torrid Holdings Inc. | 10-K 2024-04-02, EX-10.33 | https://www.sec.gov/Archives/edgar/data/1792781/000162828024014351/a230323-mizickomarkxexecut.htm | shopping | large | US | en | employee | attached to employment agreement | R8 (r8-other) |
| c20 | Interactive Strength, Inc. | S-1 2023-01-17, EX-10.8 | https://www.sec.gov/Archives/edgar/data/1785056/000119312523008845/d379507dex108.htm | health-fitness | mid | US | en | employee | attached to offer letter | R8 (r8-other) |
| c21 | SpotitEarly, Inc. | 1-A/A 2025-11-26, EX1A-6 | https://www.sec.gov/Archives/edgar/data/2077992/000109690625001941/spot_ex6z2.htm | medical | small | IL | en | consultant | attached to consulting agreement | R8 (r8-small-tail) |
| c22 | Duolingo, Inc. | 8-K 2026-01-12, EX-10.2 | https://www.sec.gov/Archives/edgar/data/1562088/000162828026001730/duolingo-munsonofferlett.htm | education | large | US | en | employee | attached to offer letter | R8 (r8-tech) |
| c23 | Kaltura, Inc. | 10-K 2026-03-16, EX-10.36 | https://www.sec.gov/Archives/edgar/data/1432133/000162828026018182/lironsharonemploymentand.htm | b2b-saas | mid | IL | en | employee | attached to employment agreement | R8 (r8-tech) |
| c24 | Luxurious Travel Corp. | S-1/A 2014-04-18, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1536394/000114420414023484/v375090_ex10-1.htm | travel | small | US | en | founder | standalone | R8 (r8-founder) |
| c25 | Civitas Resources, Inc. | 10-K 2024-02-27, EX-10.49 | https://www.sec.gov/Archives/edgar/data/1509589/000150958924000012/ex1049formofrestrictivecov.htm | business | large | US | en | employee | standalone | R8 (r8-other) |
| c26 | Volato Group, Inc. | 8-K 2024-01-16, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1853070/000114036124002350/ny20018249x2_ex10-1.htm | travel | mid | US | en | employee | standalone | R8 (r8-other) |
| c27 | Adapti, Inc. | 8-K 2025-11-24, EX-10.02 | https://www.sec.gov/Archives/edgar/data/1420924/000149315225024849/ex10-02.htm | entertainment | small | US | en | employee | standalone | R8 (r8-other) |
| c28 | Procore Technologies, Inc. | 8-K 2025-09-22, EX-10.3 | https://www.sec.gov/Archives/edgar/data/1611052/000119312525211312/d937821dex103.htm | b2b-saas | large | US | en | employee | standalone | R8 (r8-tech) |
| c29 | Impinj, Inc. | 10-K 2024-02-12, EX-10.28 | https://www.sec.gov/Archives/edgar/data/1114995/000095017024013874/pi-ex10_28.htm | business | mid | US | en | employee | attached to employment agreement | R8 (r8-tech) |
| c30 | Santaro Interactive Entertainment Co | S-1/A 2010-06-07, EX-10.1 | https://www.sec.gov/Archives/edgar/data/1487347/000138713110000642/ex-10_1.htm | games | small | US | en | founder | standalone | R8 (r8-founder) |

## Reserve

In order of use per size. URLs are in the named slice file. Small reserves alternate founder and
employee forms so a replacement keeps the signer mix.

- **Large:** Hain Celestial (food-drink, r8-other), Green Thumb Industries (lifestyle, r8-other),
  Sunrun (utilities, r8-other), Cooper Companies (medical, r8-other), Lyft (travel, r8-tech),
  SentinelOne (b2b-saas, r8-tech), Guardant Health (medical, r8-other), Eventbrite (entertainment,
  r8-tech), Vimeo (photo-video, r8-tech), Box (productivity, r8-tech), Upwork (business, r8-tech),
  Datadog (developer-tools, r8-tech), Sportsman's Warehouse (shopping, r8-other), RealPage
  (b2b-saas, r8-tech), Proofpoint, Palo Alto Networks, Varonis, Samsara, UiPath, PagerDuty, Cloudera,
  Teradata, Omnicell, NIC, National Instruments, Intapp, SmartRent, Navan, New Relic, MobileIron,
  First Advantage, Weave (all r8-tech or r8-other).
- **Mid:** Nextdoor (social-networking, r8-tech), Skillz (games, r8-tech), Aterian (shopping,
  r8-other), ProSomnus (medical, r8-other), Silvaco (developer-tools, r8-tech), Castellum (b2b-saas,
  r8-other), Everspin (business, r8-tech), FlexEnergy Green Solutions (utilities, r8-small-tail),
  Honest Company (shopping, r8-other), Veritone, Airgain, Peraso, SITO Mobile, Star Equity, Cibus,
  AIRO Group, ElectraMeccanica, Freenome.
- **Small:** Cashlin (founder, r8-founder), Allovir (employee, r8-small-tail), SpineEx (founder),
  KonaRed (consultant, r8-other), Relmada Therapeutics (founders), Greene Concepts (employee,
  r8-small-tail), Helpful Alliance (founders), iSpecimen (employee), Genvor (founder), MGO Global
  (employee), Signal Advance (founder), Advanced Container Technologies (employee), Voice Life,
  Avanyx, Patent Properties, Apimeds (founder forms); Force Protection Video, Spine Injury Solutions,
  authID, Banzai, Immunovant, Opti-Harvest, SOS Hydration, Astrotech (contractor), RenovaCare
  (consultant), Trxade, King Resources (employee and consultant forms).

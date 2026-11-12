# ip-assignment: build record

Built 2026-11-12, a pre-built run (no sector, no region) of `build/build.md` steps 1–7. Skeleton:
`plugins/fatodono-founderkit/skills/legals/skeletons/ip-assignment.md`. Catalog item 70, kind
`document`, family `company` (shared with `contractor-agreement` and `shareholders-agreement`).

## Files

- `candidates.md`: the pool of 30 (c01–c30) and the reserve by size.
- `pool/`: raw rows of the four R8 slices (`r8-tech`, `r8-other`, `r8-founder`, `r8-small-tail`,
  136 rows) and the R9 note (`r9-forms.md`).
- `extract-notes.md`: item rules every extractor followed (which part of a host filing is the
  sample, row granularity, law tags, extra *Document* lines).
- `samples/sNN.md`: one extraction table per sample (s01–s25).
- `section-map.md`: every table row mapped to a section id, the basis of every count. Rows of a
  host agreement are marked `host` and never counted.
- `merge.md`: section ids and meanings, first-batch list, saturation log, folds, merged list,
  section-level counts, document level, *Regional content*, copies.
- `progress.md`: the run's working log.

## Run

- **Routes run:** R8 (SEC EDGAR full-text search) in four slices: technology filers, other
  industries (pharma capped), founder technology assignments, and a long tail of Regulation A and
  small registrants. R9: Cooley GO's CIIAA is a document generator behind a Cloudflare bot wall
  (403), with no Wayback capture of any output; Common Paper, Bonterms, oneNDA and NVCA publish no
  IP assignment; UK Private Capital needs an account and was not run. So no standard form is in
  the pool.
- **R8 quirks:** `forms=` with a comma list returned one form only and `sics=` returned cached
  results, so collectors queried one form at a time and filtered SIC on each hit. Most hits are
  offer letters that only mention the agreement; collectors opened each exhibit and kept it only
  when it is the agreement or attaches it in full (rule 6).
- **Selection:** 30 candidates, 10 large, 10 mid, 10 small; no sector above 5 of 30; one per
  company group (rule 5) checked at selection; every pick opened and its title and first screen
  read. Six founder forms in the small third (see *Founders and employees*).
- **First batch:** s01–s15, all valid.
- **Saturation:** judged in pool order from s16 (`merge.md`). s18 added `closing`; s19–s23 added
  nothing: five non-new in a row.
- **Stop reason:** saturated at s23 (`saturated: true`). s24 and s25 were already dispatched and
  are kept past the stop point. c26–c30 were not extracted. `sample_count: 25`.

## Invalid

None. No candidate was unreachable or the wrong document.

## Copies and templates

Rule 4: no two samples share their whole text (highest 6-word-shingle containment of `raw/`
texts: s07–s08 0.36). Several samples share a law-firm form family with their own edits, all kept:
the "Proprietary Information and Inventions (Assignment) Agreement" family (s05 s07 s08 s19 s20
s22), the "Confidential Information and Invention Assignment Agreement" family (s06 s11 s13 s14 s16
s17), the "Employee Invention Assignment and Confidentiality Agreement" family (s01, with s04's
footer title), and an Israeli "Non-Competition, Proprietary Information and Inventions Agreement"
(s21 s23, 0.10 overlap). The reserve held one shell-company template filed by one agent for five
filers; none was used.

## Size thirds

Of the 25 samples: 9 large, 8 mid, 8 small. The pool held 10/10/10; the stop at s23 (pool order
rotates sizes) left the counts uneven. Small is short in kind, not in number: EDGAR's small filers
are mostly shell and micro-cap companies, and few file their staff agreement as its own exhibit
(`pool/r8-small-tail.md`: 10 rows from every Reg A and small-registrant query). Every founder
assignment R8 returned comes from a filer with 50 or fewer staff, because larger companies signed
theirs years before filing. So the small third is mostly founder forms (s03 s09 s15 s18 s24) beside
three small-company employee or consultant forms (s06 s12 s21).

## Founders and employees

**Decision: one skeleton serves both.** The five founder forms use a subset of the employee
forms' sections (`parties`, `assignment`, `assistance`, `governing-law`, `general`, and in some
`confidentiality`, `prior-inventions`, `moral-rights`, `enforcement`), plus `warranties` (5/5) and
their own consideration (`compensation`, 5/5). No section is founder-only, and the founder forms
lack only the sections of an ongoing relationship (disclosure, records, leaving, covenants). The
skeleton therefore describes the ongoing agreement every founder, employee and contractor signs,
and treats a founder's pre-company work as a pattern of `assignment` with two sections that apply
only when `facts.company.founder_prior_work` lists something (`warranties`) or speak to it
(`compensation`). Every founder sample is its own short instrument, none part of an employee
agreement, so the writer sets the founder's assignment as a separately signed part. R8 returned no
founder assignment embedded in a stock purchase agreement; s15's is a separate exhibit tied to a
founder stock purchase.

## Samples

| Sample | Company | URL | Sector | Size | Signer | Language | Words | Fetched |
|---|---|---|---|---|---|---|---|---|
| s01 | Squarespace, Inc. | https://www.sec.gov/Archives/edgar/data/1496963/000110465921051251/tm213918d7_ex10-13.htm | business | large | employee | en | 3412 | 2026-11-12 |
| s02 | Molekule Group, Inc. | https://www.sec.gov/Archives/edgar/data/1872356/000155837023005401/aerc-20221231xex10d11.htm | lifestyle | mid | employee | en | 4464 | 2026-11-12 |
| s03 | Modular Medical, Inc. | https://www.sec.gov/Archives/edgar/data/1074871/000101905619000521/ex10_5.htm | medical | small | founder | en | 1636 | 2026-11-12 |
| s04 | Dutch Bros Inc. | https://www.sec.gov/Archives/edgar/data/1866581/000186658125000227/a20250730-dutchbrosxariz.htm | food-drink | large | employee | en | 4995 | 2026-11-12 |
| s05 | Rush Street Interactive, Inc. | https://www.sec.gov/Archives/edgar/data/1793659/000119312521030959/d124075dex108.htm | games | mid | employee | en | 2526 | 2026-11-12 |
| s06 | AppTech Payments Corp. | https://www.sec.gov/Archives/edgar/data/1070050/000157570521000860/ex10_24.htm | finance | small | employee | en | 4919 | 2026-11-12 |
| s07 | Snowflake Inc. | https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/ex-1016snowflakefy2025q4.htm | developer-tools | large | employee | en | 4891 | 2026-11-12 |
| s08 | Hippo Holdings Inc. | https://www.sec.gov/Archives/edgar/data/1828105/000182810524000043/exhibit101-yuvalharrysep.htm | finance | mid | employee | en | 3916 | 2026-11-12 |
| s09 | Atlan Media, Inc. | https://www.sec.gov/Archives/edgar/data/1673731/000114420416120812/v447586_ex10-3.htm | entertainment | small | founder | en | 1630 | 2026-11-12 |
| s10 | Neuronetics, Inc. | https://www.sec.gov/Archives/edgar/data/1227636/000155837025003833/stim-20241231xex10d23.htm | medical | large | employee | en | 15390 | 2026-11-12 |
| s11 | Credo Technology Group Holding Ltd | https://www.sec.gov/Archives/edgar/data/1807794/000162828022000095/exhibit1011-sx1.htm | business | mid | employee | en | 3962 | 2026-11-12 |
| s12 | Foxx Development Holdings Inc. | https://www.sec.gov/Archives/edgar/data/2013807/000121390024084719/ea021499501ex10-37_foxxdev.htm | b2b-saas | small | employee | en | 4050 | 2026-11-12 |
| s13 | Pinterest, Inc. | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000139/cfo_offerxletterx-xsigne.htm | social-networking | large | employee | en | 2800 | 2026-11-12 |
| s14 | Codexis, Inc. | https://www.sec.gov/Archives/edgar/data/1200375/000120037523000012/sriryaliofferletter_ex1023a.htm | medical | mid | employee | en | 4546 | 2026-11-12 |
| s15 | Consumer Cooperative Group Inc | https://www.sec.gov/Archives/edgar/data/1742162/000174216221000016/ipassignmentagreement.htm | finance | small | founder | en | 2377 | 2026-11-12 |
| s16 | Figure Technology Solutions, Inc. | https://www.sec.gov/Archives/edgar/data/2064124/000206412426000009/exhibit1023compensationagr.htm | finance | large | employee | en | 5089 | 2026-11-12 |
| s17 | ContextLogic Inc. | https://www.sec.gov/Archives/edgar/data/1822250/000095017024025210/wish-ex10_7.htm | shopping | mid | employee | en | 3971 | 2026-11-12 |
| s18 | Loop Industries, Inc. | https://www.sec.gov/Archives/edgar/data/1504678/000147793217002605/llpp_ex101.htm | business | small | founder | en | 13587 | 2026-11-12 |
| s19 | Torrid Holdings Inc. | https://www.sec.gov/Archives/edgar/data/1792781/000162828024014351/a230323-mizickomarkxexecut.htm | shopping | large | employee | en | 2882 | 2026-11-12 |
| s20 | Interactive Strength, Inc. | https://www.sec.gov/Archives/edgar/data/1785056/000119312523008845/d379507dex108.htm | health-fitness | mid | employee | en | 5090 | 2026-11-12 |
| s21 | SpotitEarly, Inc. | https://www.sec.gov/Archives/edgar/data/2077992/000109690625001941/spot_ex6z2.htm | medical | small | consultant | en | 3420 | 2026-11-12 |
| s22 | Duolingo, Inc. | https://www.sec.gov/Archives/edgar/data/1562088/000162828026001730/duolingo-munsonofferlett.htm | education | large | employee | en | 3034 | 2026-11-12 |
| s23 | Kaltura, Inc. | https://www.sec.gov/Archives/edgar/data/1432133/000162828026018182/lironsharonemploymentand.htm | b2b-saas | mid | employee | en | 3828 | 2026-11-12 |
| s24 | Luxurious Travel Corp. | https://www.sec.gov/Archives/edgar/data/1536394/000114420414023484/v375090_ex10-1.htm | travel | small | founder | en | 1255 | 2026-11-12 |
| s25 | Civitas Resources, Inc. | https://www.sec.gov/Archives/edgar/data/1509589/000150958924000012/ex1049formofrestrictivecov.htm | business | large | employee | en | 6084 | 2026-11-12 |

s15 is two linked files: the agreement above and its technology-assignment exhibit,
`https://www.sec.gov/Archives/edgar/data/1742162/000174216221000016/ipassignmenttechn.htm`. Where an
exhibit is a host agreement (offer letter, employment, separation, consulting), only the attached
assignment and the host clauses that point to it were extracted; *Words* counts that part.

## For the owner's review

1. **One skeleton or two.** The samples support one skeleton (above), but a founder's
   pre-company assignment is always a separate instrument in them. If the write branch should
   produce two files (the ongoing agreement and a founder technology assignment), the catalog needs
   a second item or the writer a rule for it; today the skeleton asks for a separately signed part.
2. **Region trigger.** What one law requires here depends on where each signer works, not on where
   the product's users are. `formats/region-format.md` triggers blocks on `facts.users.regions`;
   this item needs `facts.company.staff_locations` (added). A method change, so left for you.
3. **No standard form.** Cooley GO, the only R9 source listed for item 70, cannot be fetched. Fix
   the route in `build/sources.md` or accept EDGAR-only builds for this item.
4. **Executive copies.** Most EDGAR copies are signed by executives, so covenants (non-compete
   10/25, customer non-solicit) may be more common than in rank-and-file forms.
5. **s18 kept.** Loop Industries' founder sale is an asset-purchase-shaped deal (price, escrow,
   royalties, closing conditions). It is an individual assigning IP to the company, so it stays,
   but it alone added `closing` (1/25, under 20%) and stretches the founder length range.
6. **Reused key.** `facts.company.contract_law` (added by the contractor build) now also sets the
   law of employee agreements; its *Means* names contractors, founders and partners. Confirm it
   covers employees, or split it.
7. **New keys.** Six `facts.company.*` keys under a new *Team keys* heading in
   `helpers/facts-schema.md`: `founders`, `founder_prior_work`, `ip_signers`, `business_scope`,
   `staff_locations`, `staff_restrictions`. `founders` is kept to names and roles so the
   shareholders-agreement build can reuse it.
8. **Unverified law tags.** Extractors tagged some cells from wording, not from a named statute
   (s10's state covenant addenda, s18's Quebec articles, several California § 16600 tags). Check
   before a region run relies on them.
9. **Host rows.** `build.md` does not say how to count clauses of a host agreement that point to
   the assignment; this build marked them `host` and left them out of every count (s19's DTSA
   notice and governing law sit only in its host).
10. **No UK, EU or Turkish sample.** Employee-invention rules there (UK Patents Act ss. 39–43,
    German ArbnErfG compensation, Turkish Law no. 6769 arts. 113 ff.) need region runs with their
    own sources.

## Proposed catalog row

| Id | Title | Kind | Family | Trigger question | Skeleton |
|---|---|---|---|---|---|
| ip-assignment | IP Assignment for founders and employees | document | company | Do founders, employees or contractors without an IP clause of their own create code, designs or content for the company? A founder who built anything before the company existed assigns that too. If everyone who works on the product already signed an agreement that assigns their work to the company, say so rather than writing one. | `skeletons/ip-assignment.md` |

The catalog row as added (`helpers/catalog.md`), family `company`.

## Lessons

- **EDGAR hits are mostly mentions.** Of about 1,700 technology-filer exhibits the collectors
  opened, fewer than 50 companies attached the agreement in full; offer letters naming it are the
  norm. Collectors must open each exhibit.
- **Host agreements need a mark.** Thirteen samples are attachments; a `host` mark kept the host's
  clauses out of the counts without losing them.
- **Founder forms need a quota.** Six founder forms in the pool (20%) was the least that could keep
  founder-only content above the *Commonly omitted* line. The stop at s23 left five in 25 samples,
  exactly 20%; `warranties` (8/25) clears the line only because three employee or consultant forms
  carry it too.

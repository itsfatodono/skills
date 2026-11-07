# Runs

## 2026-10-27, session 1
Checkpoint commit `37aada5` (rename to founders-legals, write branch v0, rule-4 progress) before
dispatch. Three background runs launched in parallel (see [dispatch.md](dispatch.md)):

| Run | PLAN.md todo | Writes to | Status |
|---|---|---|---|
| rule-4 re-judge | Phase 2 "Re-judge the rule-4 drops" | privacy-policy + its eu/uk/us blocks, tr-distance-sales | done, `5872d6e` |
| RoPA `uk` block | Phase 2 "Build the RoPA's eu and uk blocks" | `regions/uk/`, `research/regions/uk/` | done, `cf89140` |
| RoPA `eu` block | same | `regions/eu/`, `research/regions/eu/` | done, `d4460f6` |

RoPA `eu` result (`d4460f6`): 7 samples (2 real records: Wexford CoCo, Maynooth; 4 regulator
models; 1 GAA model), `saturated: false`, 5 sections. Ran without subagents. Proposed shared key
`facts.company.processor_customers`. Three open questions for the owner: the model cap (5 of 7 are
models), whether the EUDPR registers of EU institutions count, and whether a region block in a tabular
document should be columns rather than a section. Report: `research/regions/eu/ropa/README.md`.

On 2026-10-27 the owner answered all three, and they became PLAN.md decisions 35 (models above
the cap allowed for internal documents), 36 (EUDPR registers count, tagged) and 37 (a region block
in a tabular document is columns). The same `eu` session was resumed to apply 35 and 36. Decision
37 waits for the `uk` block.

RoPA `uk` result (`cf89140`): 26 samples (9 large, 7 mid, 9 small, plus the ICO template),
saturated at s27, 9 sections. Every sample is a public body, college or charity, and 5 of the 7 mid
samples are Oxford colleges sharing one column set. This run also had no subagent tool. Its
lessons: mark law-driven cells in root extractions, there is no "present but empty" marker,
and the Wayback CDX index finds pages a per-URL check misses. Report:
`research/regions/uk/ropa/README.md`.

On 2026-10-27 the owner answered the `uk` questions. Fact-gated rare sections were approved.
Recognised legitimate interests stays under commonly omitted. The Oxford colleges count as one
sample. Result `82e256d`: 22 samples (9 large, 3 mid, 9 small), saturated at s44, no section lost,
reshaped into "UK: …" columns per decision 37. The run added "Column" and "Header line" fields
per section, and these still have to go into `region-format.md`.

RoPA `eu` after decisions 35 and 36 (`abe10f9`): 15 samples (10 real records, 8 of them EUDPR, plus 5
models), still `saturated: false` because no saturation batch was possible. As an informal check, 10
samples in a row brought nothing new. `eu-processor-record` fell to rare. The `sources.md` exception
for models was added. On 2026-10-27 the `eu` session was resumed again to apply decision 37 to
`region-format.md` and the `eu` block.

Rule-4 re-judge result (`5872d6e`): tr-distance-sales has 34 samples (s27, s33 and s35 are copies
of s15 and count once; s21 is a cut-down template, kept as its own sample) and saturates after s30.
privacy-policy has 32 samples and saturates after s25. `security` fell from core to common and
`eu-transfers` from common to rare. Open for the owner: whether a cut-down template counts as a
copy, whether template blocks count in patterns, the drop of `security`, and the first-batch
size (20 vs 15). Found a data error: the `platform-disclosures` row cites s25/s27, but the skeleton
quotes s31. Lesson: copies can be spotted from the extraction tables alone, in minutes.

On 2026-10-27 the owner answered all four, and they became PLAN.md decisions 38–41. The rule-4
session was resumed to apply them. Decision 37 was applied in `5409742` (`region-format.md`,
`skeleton-format.md`, root `ropa.md`, `eu` block reshaped; new section `eu-law` 13/15, core). The `eu`
session was resumed to fit `doc-writer`, `doc-checker` and `SKILL.md` to the tabular rule.

Write branch fitted to the tabular rule: `d10bc73` (one edit each in `doc-writer`,
`doc-checker`, `SKILL.md`).

EULA build started on 2026-10-27, the first build where the chief of staff dispatches directly.
Three Sonnet collectors ran in parallel: `charts-ios` (R1), `longtail-ios` (R2) and `desktop`
(Mac charts + R4), writing to `research/eula/pool/`. Next steps are to select 30 candidates and run
15 extractors. Pool result: 74 raw rows (desktop 29, longtail-ios 15, longtail-2 19, charts-ios
11). Most apps link Apple's standard EULA, so custom ones are rare. An Opus helper selected 30
(10/10/10, no shortfall) into `research/eula/candidates.md`. The owner approved, and 15 Opus extractors
(s01–s15 = c01–c15) were launched at once. To watch: c09 (Moodworks) and c10 (Dolby) link pages titled
"terms", which may turn out to be a different document. The first batch came back with all 15
valid. The merge helper found 45 ids, but s12 and s14 are terms of use at an /eula URL, and s09, s10
and s13 are borderline. The owner chose decision 42 (an EULA's core is a licence grant), and it was
written to `sources.md` row A. Plan: c21 (small) replaces s12, c23 (mid) replaces s14, and c22 (large)
fills the saturation batch slot of the invalid s20 (TrapCall, Bending Spoons group with c25).
Numbering keeps sNN = cNN. To watch: c17 MacroFactor, c21 Flashka and c26 Todoist link `/terms`
pages, so s17 must be re-qualified under decision 42. Result (`08a9efb`): c21 invalid (ToS), and
c24 replaced s12. Re-qualification: s17 invalid, s09 borderline but valid (an app licence built on
Apple's standard licence), s10 and s13 valid. Still 45 ids. Saturation batch 1: s16, s18, s19 and s22 not
new, s17 does not count, so 4 non-new in a row. The next batch is c25–c29. In batch 2, s25 (the Vimeo
/eula URL is a user profile) and s26 (Todoist ToS) were invalid. **EULA skeleton done (`c347961`):**
22 valid samples (9 large, 6 mid, 7 small), saturated at s27, 44 sections (10 core, 21 common,
13 rare), 10 new fact keys. `copyright-complaints` went to Regional content (`us`). Overlap with
ToS is listed in `research/eula/README.md` (31 pairs). Findings: an EULA has restrictions, transfer,
updates, OSS components, telemetry, activation and audit sections, and gives a limited positive
warranty in 7/21 samples versus 1/30 in ToS. Open: the catalog row and trigger, whether
overlapping sections may point to the ToS, and B2B-only content.
Lesson for the dispatch method: it took about 30 extractor runs for 22 valid samples. Most
invalids were ToS pages behind EULA or terms URLs, which the selection helper did not screen.
The owner settled the EULA questions on 2026-10-27, committed as `6e33973`. The catalog trigger is
installed software, or a store app with its own licence (mobile-only apps rely on Apple's
standard EULA). EULA stands alone, with no pointers to the ToS. `copyright-complaints` stays out
of the root, the median order is kept, and B2B content stays rare. `audit` is gated by
`facts.product.licence_terms.usage_reporting`, and confidentiality has no section of its own.
On 2026-10-27 the owner approved a first-screen check of each picked URL, added to `build.md` step 1
*Select*, so wrong documents are dropped before an Opus extractor runs.
The lessons fold waits until the rule-4 agent releases `build.md`/`sources.md`. *(Superseded: folded in `973f0ed`, see below.)*

Folded in `973f0ed` (superseding the list below): Wayback CDX search, data-protection menus
(R10), image-only models, `[law: …]` cells, the present-but-empty count, and Oxford-style groups
under rule 5. "Column"/"Header line" were already in `region-format.md` since `5409742`.

*(Superseded by `973f0ed` above.)* Not yet folded into `build.md`/`sources.md` (as of `bf48b4d`): Wayback CDX search, walking data-protection menus
on region routes, rendering image-only models (DPC), marking law-driven cells in root
extractions, a "present but empty" marker, and what to do with no subagent tool (see
[dispatch.md](dispatch.md)).

## 2026-10-27, session 2
Resumed at `c88c1bf`. The chief of staff proposed running the noteable trial (Phase 5) before
more builds, so format problems surface before ~40 more skeletons. The owner chose cleanup first.
Two background runs (Opus medium), on separate files:

| Run | PLAN.md todo | Writes to | Status |
|---|---|---|---|
| facts consolidation | Phase 3 "Consolidate `helpers/facts-schema.md`" | proposal only: `research/facts-consolidation.md` | done, awaits owner |
| region classification | Phase 3 "Region-classify the rest of the seed catalog" | `build/sources.md`, `regions/*/region.md`, region `catalog.md` | done, `b176809` |

The facts run only proposes changes, because key merges rename `facts.*` references inside skeletons. The owner approves before anything is applied.

Region classification result (`b176809`): 35, 48 and 49 are `eu`-only, and their hints are now in `regions/eu/region.md`
under new *Documents* / *Forms* headings. 47, 56, 57, 16 and 41 stay shared items with `eu`/`us` blocks.
Planned rows went into no region `catalog.md`, because decision 30 lists built items only. Regulator models R10/R11
stay in `sources.md`. Four questions are open for the owner (see PLAN.md Phase 3).

The owner settled the region questions on 2026-10-27, recorded as PLAN.md decision 43 (`dae738b`).

The facts consolidation proposal (`research/facts-consolidation.md`, uncommitted) found no key merges. It found
16 near-duplicates kept separate, 4 field-level overlaps to trim (lifetime plans, single-item deletion,
refundability, proration) and 1 left as is, 6 keys referenced but never defined (all are examples in format
or build docs, so builders copy them), and 1 promotion due (`eu.processor_customers` → `company.*`, because
the uk RoPA needs it).
Lesson: nothing checks mechanically that a referenced `facts.*` key exists.

Facts apply run: on 2026-10-27 the owner approved trims 1–4, the example-key fixes, dropping `content`, and `tools/check-facts`.
The owner did not approve the `processor_customers` promotion, and the question is still open. The run also added `facts.sales.plan_changes` to the refund-policy
cancellation section, because after trim 4 that data no longer comes from `partial_refunds`.
`tools/check-facts` uses only the python3 standard library and takes about 0.03 s. Its allowlist holds 3 (file, key) example pairs. On the commit
before the fixes it flagged `data.sources`, `sales.direct` and `processors`. **Run it after any edit that touches `facts.*`.**

Promotion `facts.eu.processor_customers` → `facts.company.processor_customers` applied on 2026-10-27 after the owner said
"do whatever is next". It is also on the `uk-processor-record` Facts line; root `processor-activities` is unchanged, because its Covers asks for no customers.

Noteable trial prep (2026-10-27): noteable was already written with this skill on 2026-10-26 (noteable
`0d000270`: privacy, terms, account deletion, `legal/facts.md` of 957 lines). So the trial tests a **re-run**
(facts kept, patch mode) plus the subscription-terms and refund-policy skeletons that were not run there.
The noteable working tree has uncommitted website changes, so the trial must use a separate worktree. How to run
it (owner in Claude Code, or headless `claude -p`) was asked; the owner dismissed the question.

Noteable trial: on 2026-10-27 the owner said they had already done it (the 2026-10-26 run) and that noteable is not to be touched.
PLAN.md Phase 5 item closed (`f5fbe8d`). Re-run and patch mode are not yet tested; they need another app.

Cookie-policy build started 2026-10-27 (`f5fbe8d`). The owner decided the build covers the policy only (no banner text) and the pool uses 4 slices.
Four Sonnet collectors run in parallel: `charts-us` (R1 us), `longtail` (R2), `charts-ie` (R1 ie), `web-only` (R4),
writing to `research/cookie-policy/pool/`. Next: one Opus helper selects 30 candidates, now including the
first-screen check (`c88c1bf`), then the owner approves and 15 extractors run.
Lesson: the Code Mode `execute` runtime has no `subagent` tool, so subagents are dispatched only with direct tool calls.
Cookie pool: `web-only` 21 rows, 31 skipped. The owner declined the raw-text cache / `invalid.md` proposal
(see [owner-preferences.md](owner-preferences.md)). Under the method as it stands, extractors keep tables only.
Cookie pool done: 452 raw rows (charts-us 238, charts-ie 148, longtail 45, web-only 21). The selection helper picked 30
(`8169dcd`): all dedicated pages, 9 EU/UK, and 6 dropped by the first-screen check (the first build where the check ran at selection).
On 2026-10-27 the owner approved, and 15 Opus extractors (s01–s15 = c01–c15) were launched at once. To watch: c04 Klarna
("Tracking technology notice", possibly JS-loaded), and small-size template copies (Termly/iubenda) under rule 4.
Cookie first batch: 15 of 15 valid (`7d19053`), so for the first time no first-batch sample was invalid. Merge (`c8b693c`, merge session
`ses_e83db5fbaffeOmf2S8Gr0sO55f`): 26 ids (22 root, 4 law-only), no copies. s06, s08 and s09 are full generator templates,
each counted once. Regional: eu/uk `consent-tool`/`legal-basis`/`transfers`; us `sale-share`/`opt-out-signals`.
Saturation batch 1 (s16–s20) launched. The plan is to resume the merge session to judge new/non-new.
Saturation batch 1 (`6ec660c`): s16, s17, s19 and s20 not new. s18 was new only through a "binding English version" clause.
The owner chose decision 44 (`eaefdb0`): drafting boilerplate in a notice is not a section. While writing it, the chief of staff
saw that ToS/EULA have a real closing-clauses section, so the rule was limited to notices. **Lesson: grep the existing
skeletons before writing a method rule.** The build is saturated at s20 with 20 samples, and 5 extractor runs were saved. The merge session was resumed to
write the skeleton and the README (no region blocks; catalog row only proposed).
**Cookie-policy skeleton done** (2026-10-27): 20 samples, 20 sections (6 core / 8 common / 6 rare), new keys
`data.cookie_controls`, `data.cookie_list`, `data.ad_consent_frameworks`, `product.offsite_components`, plus 4 optional
fields on `data.tracking`. Region recommendation: build `us` now (9/20 samples), `eu` through its own region run, `uk` copied
from eu or deferred. This took 20 extractor runs for 20 valid samples, compared with ~30 for 22 on the EULA, thanks to the first-screen check.
The owner asked to stop here before any new document.

KVKK and commerce batch started 2026-10-27 (decisions 45–49). The owner chose: 3 tracks, drop pre-7499 samples for 11 and 12,
add a guide check for 12, a small build for OSS, 13 as root plus regions. The chief of staff did not apply the 7499 cut-off to 13
(Arts. 11 and 13 unchanged) and told the owner. Doc ids: `tr-kvkk-notice`, `tr-explicit-consent`, `data-subject-request`,
`tr-pre-contract-info`, `oss-notices`. Deviation from `build.md` step 1: one shared pool for three items at
`research/regions/tr/kvkk-pool/`, with one row per site and labelled URLs per document. Open: the skeleton-format field
for decision 47's "wrong pattern" mark, to settle before 12 is merged.
Wave 1 (pool collection, Sonnet): kvkk `tr-apps`, `tr-large`, `tr-tail`; ÖBF `obf-relocate` (finds ÖBF URLs for the
distance-sales pool sites); `oss` (one slice); DSAR global `dsar-us`, `dsar-eu-uk`.
Wave 1: `tr-tail` done, 42 rows (`ses_e83c57149ffenQv6SXqjQ2GM0c`). It ran only R2 and R4, no Turkish web searches, and did not log skips,
so its "0 skipped" means nothing. The rows are above the target, so it was not re-run; web-only small sellers may be thin at selection.
Wave 1: `tr-large` done, 28 rows, 0 skipped (`ses_e83c58913ffe7cydUD0Scehk15`).
Wave 1: ÖBF `relocate` done, 113 rows, about 105 skipped (`ses_e83c55c59ffeEjSp1Q6B4sfgZg`).
ÖBF pool: 113 rows, 13 `(in MSS)`, 3 `(blocked)`, 0 `(checkout)`. On 2026-10-27 the owner decided: embedded ÖBF (inside the MSS) counts as a sample,
tagged `embedded`. Owner approved starting ÖBF selection before the other pools finished. Selection helper: `ses_e83c0bd4cffe6e109voH33RkKV` (Opus).
Wave 1: `dsar-eu-uk` done, 41 rows, 11 skipped (`ses_e83c5241cffeGn3uTOtzep0mOp`).
Wave 1: `tr-apps` done, 49 rows, 518 skipped (`ses_e83c59f5affeBbaYjpPsRkCazO`). KVKK pool complete.
KVKK pool stats (2026-10-27, 119 rows): aydınlatma 113, açık rıza 29, başvuru 41, only 12 show a date (all 2024+).
So decision 46 mostly works through the Art. 9 tools test. The owner decided: inline signup consent text counts as a
`tr-explicit-consent` sample, tagged `(inline)`, when the full text shows without an account. Launched: aydınlatma
selection `ses_e83bb9305ffe3r1J08V0VIzn1J` (Opus; counts drops by cause, including "no transfer section, no date",
which decision 46 drops literally; raise it with the owner if it is large), and collector `tr-consent` `ses_e83bb7a54ffe1JGfUgE91NLceO` (Sonnet).
`dsar-eu-uk`: 18 of 41 rows `(blocked)`, likely JS portals that Wayback does not capture; decide at DSAR selection.
Wave 1b: `tr-consent` done, 40 rows, 0 skipped. Açık rıza total about 69 rows before the 7499 filter.
ÖBF selection done (`ses_e83c0bd4cffe6e109voH33RkKV`): 30 picks (10/10/10), 4 embedded, reserve 14, 3 dropped at first screen. 10 Shopify shops were not screened because the host returned 429, so they are left out (they stay in the last reserve). The shared templates are labelled T1–T5, and T1 (platform default) is the most copied.
ÖBF first batch: on 2026-10-27 the owner said "ok", and 15 Opus extractors (s01–s15 = rows 1–15) were launched at once. This is heavy track 1 of 3.
ÖBF first batch: 15 of 15 valid (s01–s15, 9–23 rows each).
Wave 1: `dsar-us` done, 55 rows, 14 skipped (`ses_e83c5364affeAxcBjWPyW4t7Dr`).
DSAR pool complete: 96 rows, 50 `(blocked)` (dsar-us 32/55, dsar-eu-uk 18/41). Large companies sit mostly behind JS portals, so selecting
from readable rows only would bias toward small companies. The owner approved a probe: `ses_e83b35b36ffeKYTSAqCz5h2HQV` writes
`research/data-subject-request/portal-probe.md`. If a recipe works, it goes into `sample-extractor.md` step 1 *Fetch* (an environment fix, not a one-off).
ÖBF: the owner approved running the merge and saturation batch 1 in parallel. Merge session `ses_e83b3aaa1ffeaaHfYRydyQ9GnN`
(resume it to judge s16–s20). s16–s20 extractors launched.
Aydınlatma selection (`ses_e83bb9305ffe3r1J08V0VIzn1J`): 25 picks (10 large / 5 mid / 10 small), reserve 25 (1 large, 24 small, 0 mid).
48 dropped: 5 old-style transfer, **20 no transfer section and no date**, 23 other; 8 more by the group rule. Mid is 5 short.
Opet: hub page, its customer-notice link was used. Türk Telekom: extract only the individual-customer part.
Decision 46 narrowed (owner, 2026-10-27): keep undated no-transfer notices unless they rest on Art. 6 explicit consent; tag `no-transfer`. The aydınlatma selection session was resumed to re-judge the 20 rows. ÖBF saturation batch 1: s16–s20 all valid (8–18 rows); waiting on the merge to judge them.
Wave 1: `oss` done, 38 rows, about 25 skipped (`ses_e83c548d6ffe3l51fKocQ19xrm`). All wave-1 collectors finished.
Aydınlatma reselection: 30 picks (10/10/10), 19 of 20 kept as `no-transfer`, RE/MAX dropped at the Art. 6 check. Reserve: 6 large, 0 mid, 33 small. Salonia (self-described sample text) is last in the small reserve.
DSAR probe (`ses_e83b35b36ffeKYTSAqCz5h2HQV`): there are 49 blocked rows, not 50. curl recipes work for OneTrust (24) and Transcend (2), and TrustArc works but has 0 rows here.
The other 23 rows have no recipe (DataGrail, SixFifty, Zendesk, 7 in-house SPAs, 6 bot walls, 4 others). The recipes were added to
`plugins/fatodono-launchkit/skills/legals/helpers/sample-extractor.md` step 1 *Fetch* on 2026-10-27, so later builds get them by default. Readable DSAR rows: 46 + 26 = 72.
ÖBF merge (`ses_e83b3aaa1ffeaaHfYRydyQ9GnN`): 28 ids (9 core, 9 common, 7 at 20–27%, 3 rare), 23 reuse tr-distance-sales names,
no copies in s01–s15. Accepted by the chief of staff: signature/date blocks are document level (decision 44, form treated as a notice);
s01's built-in KVKK consent is flagged under decision 47. The session was resumed to judge s16–s20.
Aydınlatma first batch: 15 extractors launched (owner approved). OSS selection launched (`build.md` *User run* numbers).
ÖBF saturated at s20 (s16–s20 not new; s19 Tekzen shares 45% with s01 Karaca but is not a copy). The owner approved decision 50
(the *Avoid* field in skeleton-format, a doc-writer rule, doc-checker check 4) and the skeleton write; the merge session was resumed for steps 4–7.
Aydınlatma first batch: 15 of 15 valid (6–28 rows; s09 has only 6, so check it at merge).
Aydınlatma: merge session `ses_e83a39ba3ffegJR2w4ovq2EJfS` (it previews facts mapped to existing keys, lists Avoid candidates, and checks s09). s16–s20 extractors launched in parallel (owner ok).
OSS selection (`ses_e83a70db7ffeziisuC0tuAsKg0`): 15 picks (5/5/5), reserve 8 (0 small), 11 dropped at first screen.
Aydınlatma saturation batch 1: s16–s20 all valid (5, 7, 16, 7, 9 rows). Worry: the short `no-transfer` mid picks may make saturation look
reached sooner than it is, since a thin text cannot bring a new id. Raise it at judging.
OSS first batch: 5 extractors (s01–s05) launched on the owner's "go". Told to record structure and per-entry fields, not every entry.
OSS first batch: 5 of 5 valid (8–18 rows).
OSS: merge session `ses_e839f3d63ffeZ3o63CSXmo1yHs` and s06–s10 extractors launched in parallel (owner ok).
OSS saturation batch: s06–s10 all valid (6, 4, 4, 6, 5 rows; short, as expected for this document).
**ÖBF skeleton done** (2026-10-27, `ses_e83b3aaa1ffeaaHfYRydyQ9GnN`): `regions/tr/tr-pre-contract-info.md`, 20 samples, saturated, 25 sections
(9 core / 9 common / 7 rare), 3 folded. One new key, `facts.tr.after_sales`. Trigger is the same as tr-distance-sales. *Avoid* in `personal-data`
cites the KVKK Board page on explicit consent and its decision on making a service conditional on consent. Found: tr-distance-sales has "4/18 take marketing
consent inside the contract" with no *Avoid* (decision 50 came after it).
Aydınlatma merge (`ses_e83a39ba3ffegJR2w4ovq2EJfS`): 23 ids (9/4/10), no copies, transfer 15/15 (no `no-transfer` sample in the first batch),
controller 11/15 common. 5 Avoid candidates. 6 proposed `facts.tr.*` keys: legal_bases, transfer_tools, verbis, controller_representative,
collection_channels, destruction_policy. s09 is a genuinely short notice.
OSS merge (`ses_e839f3d63ffeZ3o63CSXmo1yHs`): 12 ids (3/4/5), no copies. Owner: `warranty-disclaimer` stays an id (the licences require it,
so it is not decision-44 boilerplate); `component-list` covers only components shipped to the user, and listing server components is a pattern.
Owner rulings 2026-10-27, for the Aydınlatma skeleton write: the 6 `facts.tr.*` keys are approved, but `legal_bases` and `controller_representative` must first be
compared with the `eu` keys (promote under decision 29, or align the names). All 5 Avoid candidates go to *Avoid*. Retro Avoid sweep approved:
the helper moves tr-distance-sales' marketing-consent pattern to *Avoid*; other skeletons are reported only, in `research/avoid-sweep.md`.
OSS saturated at s10 (s06–s10 not new, 12 ids: 2 core, 1 common, 9 rare). Rulings logged in merge.md *Changes*.
Aydınlatma judged: s16–s20 not new, saturated at s20 by the rule. Counted over dated/art9 samples only, the run would be 3. The helper suggested one more batch as a check.
The chief of staff (delegated) followed the rule instead, because the helper's own data showed thinness is not a no-transfer trait (s16, art9, is just as thin) and the
richest sample s18 brought nothing new. Transfer is 18/20 (the 2 missing are the no-transfer s17 and s20); retention dropped to common (13/20).
Skeleton write launched in the same session, with the owner's facts and Avoid rulings.
Also launched (owner: "continue sub-tasks without asking"): OSS skeleton write, açık rıza selection `ses_e8398b6c5ffeu70ewLl2w9RfHZ`
(ETK at most 3 of 30, chief-of-staff call), DSAR root selection `ses_e83989b3dffesy9FCG7MroTmor` (no vendor above 1/3; US vs EU/UK balanced),
DSAR tr selection `ses_e8398873dffeG1JrEuMIl6ligC` (from the kvkk-pool Başvuru column; no 7499 filter).
Retro Avoid sweep (`ses_e8399f265ffeqwRzp8ycn5qXvd`): tr-distance-sales `personal-data` now has *Avoid* (4/18, s07 s16 s19 s23). It cites the KVKK
consent guide and decision, plus the ETK rules (Law 6563 Arts. 6 and 8 and its regulation; the citation is the helper's, the chief of staff found it plausible).
It found 28 candidates in other skeletons (`research/avoid-sweep.md`). They are not applied, because it is outside the batch, and the root-vs-region citation question is open. Added to the PLAN Phase 3 todo.
2026-10-27: **the API usage limit was hit** ("regain access on 2026-11-01"). Four runs died mid-work: the Aydınlatma skeleton write (its 6 tr keys were in
`regions/tr/facts.md`, the skeleton was not), the OSS skeleton write (looked complete, not confirmed), açık rıza selection, DSAR root selection. The owner connected
a new API key and the four sessions were resumed. DSAR tr selection finished (`ses_e8398873dffeG1JrEuMIl6ligC`): 24 picks (10/8/6),
reserve 7 (all large); mid and small are short because the pool has few form URLs, and 3 tail rows were signup forms. Its extraction waits for the root merge.
Lesson: this batch ran about 75 Opus runs in one day. At "start the next heavy step", check the usage budget, not only the 3-track cap.
**OSS skeleton done** (2026-10-27): `skeletons/oss-notices.md`, 10 samples, saturated, 8 sections (2 core / 1 common / 5 rare), with 4 ids folded (noted in merge.md *Changes*).
New keys `facts.product.source_code_offer` and `data_attributions`. `third_party_components` was narrowed to shipped components and given optional fields. New family `licensing`.
Two *Avoid* lines cite licence texts, so the chief of staff widened the *Avoid* wording in skeleton-format to "guidance or a binding text (a law, a licence)".
DSAR root selection (`ses_e83989b3dffesy9FCG7MroTmor`): 21 picks (10/9/2), 12 US and 9 EU/UK (EU/UK all large), OneTrust 7/21, and all 26 OneTrust URLs readable.
Small companies rarely publish a form (they say "email us"), yet small founders are this skill's users. So the chief of staff launched a cheap Sonnet `dsar-tail`
collector (small only, R2 us/gb + R4 + web) before the first batch. If it is still short, record the shortfall in the README and go on.
**Aydınlatma skeleton done** (2026-10-27): `regions/tr/tr-kvkk-notice.md`, 20 samples, saturated, 20 sections (8 core / 5 common / 7 rare), 3 folded, 5 *Avoid*.
Art. 10(1) items are written in every notice, so controller always appears. Keys: 6 new `facts.tr.*` (legal_bases, transfer_tools, verbis, representative,
collection_channels, destruction_policy). legal_bases stays in tr: eu has no such key and reads the basis from `facts.data.purposes`. The representative key is named
like `facts.eu.representative`. Chief-of-staff calls: keep the name `transfer_tools` (it has a different shape from eu/uk transfer_mechanisms). verbis plus `facts.uk.ico_registration`
meet decision 29, so a helper promotes them. The same helper removes the stale check-facts allowlist entry and verifies the Board guide titles cited in every tr *Avoid*.
Açık rıza selection, first pass: 19 picks (2/7/10). 22 dropped as undated transfer-consent texts and 9 at the Art. 6 check (clinic and hotel health consents).
**Chief-of-staff error:** the Art. 6 check, which the chief of staff proposed when narrowing decision 46, was legally wrong. Explicit consent stays a lawful basis for special
categories after 7499, so it does not date a text. The transfer test also does not fit item 12 (consent to transfer abroad is its subject, and it is still lawful for occasional transfers).
On 2026-10-27 the owner approved revising decision 46: the Art. 6 check is withdrawn, there is no cut-off for 12, and regular-transfer consent is caught by decision 47 → *Avoid*. The
RE/MAX drop in tr-kvkk-notice is left as is (1 sample). Lesson: **check a proposed legal test against the amended law text before it becomes a rule.**
Facts promotion (`ses_e8390477effeSibLchyk7VRl4Y`): `facts.tr.verbis` and `facts.uk.ico_registration` became `facts.registrations.privacy_regulator`, a list with one entry per region,
with 5 references updated. Behaviour change accepted by the chief of staff: the uk RoPA "ICO registration number" header line now shows only when the entry is `registered`, not
`exempt`, since an "exempt" value under a number heading made no sense. The check-facts allowlist entry was removed. Citations: all 11 confirmed, and 1 claim moved to the right source
(the "no consent when another basis applies" rule is in decision Icerik/5412, not the consent page Icerik/2037).
Açık rıza reselection: 27 picks, and 28 after the chief of staff re-admitted VakıfBank (rule 5 is about a shared legal team, and two state banks under TVF are not one group) → 8/10/10,
with 18 `transfer-consent`, 2 `etk`. First batch s01–s15: 15 extractors launched, told to record per consent item what is asked and how acceptance is taken.
Açık rıza first batch: 15 of 15 valid (3–15 rows; consent texts are short).
Açık rıza: merge session `ses_e838afdb9ffeEFlnOhcDBblEs5` (decision 47 guide check, facts reuse from tr-kvkk-notice) and s16–s20 extractors launched in parallel.
Açık rıza saturation batch 1: s16–s20 all valid (4, 3, 7, 3, 6 rows).

## Resume here (session ended 2026-10-27 because the context window was full)

KVKK and commerce batch (decisions 45–50). Done: `tr-pre-contract-info`, `tr-kvkk-notice`, `oss-notices` skeletons. Open:

1. **`tr-explicit-consent`**: the merge session `ses_e838afdb9ffeEFlnOhcDBblEs5` was still running at session end (merge.md, decision-47 Avoid list,
   facts preview). s16–s20 are extracted (`a50484d`). Next: resume that session to judge s16–s20, then write the skeleton (`regions/tr/tr-explicit-consent.md`,
   Avoid fields, reuse `facts.tr.*` from tr-kvkk-notice, catalog row, README). If the merge.md is missing or partial, resume the session to finish first.
2. **`data-subject-request` root**: 21 candidates (10/9/2, `5095bbe`). The `dsar-tail` collector `ses_e83912e2effeWa0wNt5OPxw1N5` (small companies) was still running.
   Next: resume the selection session `ses_e83989b3dffesy9FCG7MroTmor` to add the small picks from `pool/dsar-tail.md`, then first batch (5 per size, all if fewer),
   merge + saturation in parallel, skeleton with `eu`/`uk` blocks from *Regional content* (decision 49).
3. **`data-subject-request` `tr` block**: 24 candidates (`069e6d4`). Its extraction may run before the root merge (the owner was offered this to save time; no answer).
   Merge against the root ids, then write `regions/tr/data-subject-request.md` as a block.
4. After the batch: owner review of the 5 skeletons; the retro Avoid sweep (PLAN Phase 3 todo); the root-vs-region Avoid citation question.

Owner preferences in force: continue sub-tasks without asking, no new document types (owner-preferences.md). Commit only named paths (dispatch.md).
`raw/` folders are gitignored.
Update after the handoff: açık rıza merge finished (`ses_e838afdb9ffeEFlnOhcDBblEs5`). 19 ids (7 core / 1 common / 11 rare), no copies. Avoid: regular-transfer consent 12/15,
consent despite another basis 5/15, blanket consent 3/15, service conditional on consent 1/15. One new key, `facts.tr.consent_capture`. s07 and the other short ones are short texts, not thin extractions.
**For the skeleton write:** `transfer-abroad` is core, but its majority pattern is *Avoid*. Its *Applies when* must be limited to occasional transfers without Art. 9 tools
(`facts.tr.transfer_tools`), and its Default pattern must be s06's per-case wording. Next step 1 above is now: resume this session to judge s16–s20, then write the skeleton.

## Session 2 (2026-10-27)

The owner: "finish what is left under Resume here, then stop, no new items; don't ask me, I'm AFK." Scope: items 1–3; item 4 waits for the owner.
The old helpers could not be resumed (see [dispatch.md](dispatch.md)), and `pool/dsar-tail.md` was never written. Launched fresh:
- açık rıza skeleton helper `ses_e8379e334ffeSk1L910UT4PXDR` (Opus), working from merge.md;
- `dsar-tail` collector, rerun from scratch, `ses_e8379d0a9ffeAxjceg1c3Tu3tz` (Sonnet);
- DSAR `tr` first batch: 15 extractors, s01–s15 = rows 1–15 (Opus). DSAR is built with `build.md`, not `build-form.md`, because `build-form.md` covers console questionnaires.
Root DSAR first batch waits for the tail collector and free agent slots (~20 per session).
DSAR `tr` first batch: 15 of 15 valid (7–21 rows), `ac1957a`. Notes for the merge: s12 leaves out Art. 11/1 (d), (e), (f), (ğ), and its business petition copies the user one.
s11 (TürkKEP) has no legal name or address in its text. s08 is an OCR'd PDF, with section C restored by hand.
Root first batch launched: 12 extractors for c01–c12 (5 large, 5 mid, 2 small), as candidates.md defines it. Small picks from the tail are added after the collector finishes.
The `tr` merge waits for the root merge (`tr` ids follow the root ids).
Root first batch: 12 of 12 valid (8–26 rows), `a4cec07`. Root merge helper `ses_e8374957affeHjPdVavschS4ZJ`; it serves the whole root build, so resume it in this session only.
**Açık rıza skeleton done** (2026-10-27, helper `ses_e8379e334ffeSk1L910UT4PXDR`): 20 samples, saturated (s16–s20 added no ids), 17 sections (`intro` and `rights` folded in).
`recipients` and `transfer-abroad` dropped from core to common by count. The chief of staff kept transfer-abroad's fixed *Applies when* and Default. New key `facts.tr.consent_capture`.
Chief-of-staff calls, made without the owner (AFK): no extra batch, even though 3 of the 5 saturation samples are under 140 words. Short texts are typical (12/20).
`withdrawal` is always written (9/20 write it). The reason is cited, but it is an inference: no source says the text must state it. One unticked choice per consent is required (guide 2025 p. 10).
New *Avoid* 13/20: a single acceptance covering several purposes. Also a 1/20 *Avoid* (s19, consent bundled into the notice).
For the owner's review: the withdrawal-always inference, and the 13/20 *Avoid*, which goes against the majority pattern.
DSAR root first-batch merge: 25 ids (6 core / 10 common / 7 rare, plus 2 us-only: `sale-status`, `opt-out-signals`), no copies, 26 regional rows (15 us, 6 eu, 3 uk), so a `us` block is justified.
The first batch must reach 15, so 3 are owed. The chief of staff's call: wait for `dsar-tail` and take the 3 small picks from it (keeping the thirds at 5/5/5). c13–c15 only if the tail has no valid small rows.
`fees-refusal` stays a rare root id (GDPR, UK GDPR, CCPA and KVKK all have it). Proposed key `facts.users.request_handling`: before adding it, check its overlap with the existing `facts.users.rights_channels`.
Tail: 10 rows; small companies almost never publish a form (about 1 request page per 400 sellers). Selection (`035634b`): c22 Glyyd and c23 Luzid/Glasslake are small; c24 Grow Therapy is mid.
24 picks (10/10/4). Top-up: s13 = c22, s14 = c23, s15 = c13 Bolt (only 2 small were valid). Saturation batch 1, s16–s20 = c14, c15, c24, c19, c16; batch 2 = c17, c18, c21, c20.
8 extractors (s13–s20) launched together, so saturation batch 1 runs alongside the top-up.
Owner: "the DSARs are not that important, what we have is enough" ([owner-preferences.md](owner-preferences.md)), so s20 is the last root sample.
**DSAR root skeleton done** (2026-10-27): `saturated: false` at 20 samples. s18 brought `appeal` and s20 `non-discrimination`, both US state law in the `us` block. The 23 root ids have been stable since s15.
Files: `skeletons/data-subject-request.md` (20 sections), plus blocks `eu` (3), `uk` (4) and `us` (7). New shared key `facts.users.request_handling` (alongside `rights_channels`), and `facts.us.appeal_process`.
`us` *Avoid*: s02 asks for a full SSN and makes requesters accept its terms; s10's exemption notices lapsed in 2023 (CCPA citations verified).
Chief-of-staff calls: `fees-refusal` (1/20) is folded into `timeline` by the format rule. `uk-complaints` (1/20) is kept because the law requires it (DPA 2018 s.164A, in force since 2026-06-19).
Weakness: the eu and uk blocks rest on at most 7 and 4 samples, all from large companies.
**DSAR `tr` block done** (2026-10-27, `ses_e8352bb33ffezT5VyYvycRVIHR`): 15 samples, `saturated: false` (the pool was closed by the owner), no copies. One tr-only id, `tr-complaint`, plus 6 tr sections mapped to root ids.
4 *Avoid*: paper-only channels 3/15, required phone/fax/e-mail 3/15, an answer by phone call 2/15, asking consent for the application's data 3/15. No new keys.
With no Board text against them, these stayed patterns: reserving the right to ask for an ID copy (7/15), "this form is mandatory", and s13's ban on applying for a relative. The chief of staff removed the duplicate item-13 mention from `regions/tr/region.md` row 36.
**Session 2's Resume-here items 1–3 are done.** Only item 4, the owner's review, is open: the skeletons from both sessions, the retro *Avoid* sweep, and the root-vs-region *Avoid* citation question.
Update: `dsar-tail` finished, 34 small rows (many skips: policy-only or email-only pages). Not committed by the collector; committed with this note. Next step 2 starts at "resume the selection session".

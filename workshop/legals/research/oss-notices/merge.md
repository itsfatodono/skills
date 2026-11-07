# oss-notices: merged section list

First batch: s01–s05 (c01–c05 in pool order; 2 large, 2 mid, 1 small, since the *User run* has no size
thirds). This is a small creator build (PLAN.md decision 48), so `build/build.md` *User run* numbers apply:
first batch 5, one saturation batch of 5 (s06–s10). This list was written before any saturation sample
was read (`build/build.md` step 3). All 5 are valid; none was replaced. Saturation batch 1 (s06–s10) is
judged under *Saturation* and folded into the counts below. It added no id, so the build is saturated at
s10 with 10 samples. The *First-batch samples* column stays as written before saturation. Each meaning
below is fixed from here: change one only with a dated note under *Changes*. One sample row can map to
more than one id when it gives more than one kind of fact (s04 §1 gives `scope`, `governing-licences`
and `warranty-disclaimer`).

**One list, not one id per entry.** The repeated per-component entries (one per package, licence,
font, crate, image or model) are one id, `component-list`. The fields an entry carries (name,
version, licence id, copyright, URL, licence text) and how entries are grouped are patterns under
*Patterns*, never ids. A group of entries for a different kind of component (fonts, AI models, native
libraries) is still `component-list`.

**This is a notice** (decision 44): drafting boilerplate that gives the reader no fact about the
components (which language version applies, for example) is not a section and never makes a sample new.
Such text is listed under *Not sections*. `warranty-disclaimer` is not boilerplate (owner ruling,
2026-10-27: the licences require it and it tells the reader something).

**A saturation sample is compared against the 12 ids in *Section ids*.** None is regional (see
*Regional content*).

## Section ids

| Id | Meaning | First-batch samples |
|---|---|---|
| scope | Opening: that the product contains third-party open-source software, which products, apps, platforms or builds the notice covers, and what each entry holds or which dependencies are included. | s01 s03 s04 s05 |
| governing-licences | Which terms govern the components: their own open-source licences, not the company's terms, plus any terms the company alone offers on top. | s04 s05 |
| accuracy | Limits of the list: it may be incomplete or wrong, it is not legal advice, and how to report an error. | s03 s04 |
| other-locations | Where else the notices are kept: plain-text or downloadable files, copies inside the app or container, or another page. | s03 |
| licence-summaries | Plain-language summaries of what each licence family allows or requires. | s03 |
| source-offer | Offer of the source code for copyleft components: which licences, what is supplied, for how long, to whom, at what cost, or a direct download link. | s01 |
| warranty-disclaimer | That the open-source components come without warranty or liability from the company or their authors. | s01 s04 |
| contact | Where to send open-source requests or questions, and what a request must contain. | s01 s04 |
| component-list | The third-party components shipped to the user (in the app, the client or the downloaded software), each with its licence; one id however the entries are cut, grouped or laid out. Listing server-side components that are never shipped is a pattern, not part of this id (owner ruling, 2026-10-27; see *Changes*). | s01 s02 s03 s04 s05 |
| licence-texts | The full text of the licences the components are under (and their exceptions), wherever it sits: inside each entry, in an appendix, as a per-row excerpt or in a linked file. | s01 s02 s03 s04 s05 |
| notice-files | Contents of upstream NOTICE files (Apache-2.0 §4(d)) or which components carry one and where it is reproduced. | s03 |
| data-attributions | Attribution notices for third-party data or content that is not software (map data, datasets), including a supplier's required notice. | s04 |

Not sections (document level, step 4): page titles (s01 §1, s02 §1, s06 §1, s07 §1, s10 §1); platform
or product-surface part headings (s01 §2, §13; s06 §2, §4), which group `component-list`; s02 §2's
generator credit line ("This file was generated with…"), which names the tool and gives no fact about
the components; s03 §1's regenerate command, internal file paths and maintainer-notes file, and s03 §9's
back link to the app's login (the plain-text file links in §9 map to `other-locations`); s05 §2's
contents list with per-platform counts; s08 §2's summary figures (package count, licence count, "Last
reviewed" date) and its "Back to top" link; s09 §6's timestamp (its upkeep sentence is a
`component-list` pattern); s07's help-center "Related Articles" (site chrome); s04's note that the
component notices stay in English (decision 44: language version), and s04 §5, the French copy of the
preamble, which repeats §1–§4 and adds no fact.

## Mapping notes

- In-text pointers to a later part of the same page do not count as the id's first row: s05 §1's
  "full text… reproduced at the end" is `scope`, and `licence-texts` starts at §10. s01 §9 ("License
  Information", inside the LGPL offer, pointing to the LGPL text) is part of `source-offer`.
- When one row gives both, `component-list` is ranked before `licence-texts` (the entry names the
  component, then gives the text).
- s01: §3 and §14 (the all-caps "may be contained" line, once per platform) to `scope`; §4, §7 and §9
  to `source-offer` (Android part only); §5 and §6 to `contact`; §8 (GNU "in the hope that it will be
  useful" wording) to `warranty-disclaimer`; §10, §11, §15, §17 and §18 to `component-list` and
  `licence-texts`; §12 and §16 (the AI model, its base models and RAIL licence) to `component-list`
  and `licence-texts`, since a model is a component with a licence.
- s02: no company framing. §3–§8 to `component-list` and `licence-texts`; the Rust and Go banners
  (§5, §6) carry SPDX ids only, so those entries give no `licence-texts`. The Microsoft ONNX Runtime
  notices reproduced whole in §8, including Microsoft's own $5 source-by-mail offer, are an upstream
  notice nested in an entry: a `component-list` pattern, not Granola's `source-offer`.
- s03: §1 to `scope` (purpose, what each entry holds, transitive deps in, devDependencies out); §2's
  "not legal advice" and copyleft caveat to `accuracy`, its index of notice files to
  `other-locations`; §3 to `licence-summaries`; §4 (frontend, shipped) and §8 (CDN fonts loaded in the
  user's browser) to `component-list`, with the per-row licence excerpts to `licence-texts`; §5
  (backend) and §6 (Docker images) list server-side components, a `component-list` pattern under the
  2026-10-27 ruling; §7 to `notice-files`; §9's plain-text file links to `other-locations`.
- s04: §1 splits into `scope`, `governing-licences` (OPEN LICENSE governs; own terms offered by Lyft
  alone) and `warranty-disclaimer`; §2 to `accuracy`; §3 and §4 to `contact`; §6 and §7 (the
  SwiftProtobuf runtime exception, rendered as its own heading) to `component-list` and
  `licence-texts`; §8 (OpenStreetMap, ODbL) and §9 (TomTom, proprietary) to `data-attributions`.
- s05: §1 to `scope` and `governing-licences` ("each component is used under the license shown");
  §3–§5 (iOS, Android, Web) to `component-list`; §6–§9 (media infrastructure and backends) list
  server-side components, a `component-list` pattern; §10 to `licence-texts`.

- Saturation batch 1:
  - s06: §3 (web fonts, one per bullet) and §5 (licence types with a dependency count each, no
    component named) to `component-list`; §6's pointer to the licence view inside the app to
    `other-locations`. No licence text on the page, so no `licence-texts`.
  - s07: §2's index to `component-list`; §3 (MIT and Apache texts once each) to `licence-texts`; §4's
    per-component notice blocks to `component-list` and `licence-texts`.
  - s08: §1 to `scope` (the same stock "sets forth attribution notices… may be contained in portions"
    sentence as s01 §3; see *Copies*); §3 to `component-list`; §4 to `licence-texts`.
  - s09: §1 to `scope`; §2 (Apache HTTP Server with its subcomponent notices) and §3–§5 to
    `component-list` and `licence-texts`; the server, PHP runtime and CodeIgniter entries are
    server-side components (pattern), the front-end libraries are shipped; §6's "updated periodically"
    sentence to `component-list` as an upkeep pattern (as cookie-policy kept list cadence under its
    list id).
  - s10: §2, §4 (icons and fonts) and §5 (proprietary and source-available components) to
    `component-list` and `licence-texts`; §3 (hunspell-asm, licence by URL only) to `component-list`,
    a by-reference `licence-texts` pattern.

## Section map

First-row order of ids per sample (the basis of every count and median below).

```
s01 scope source-offer contact warranty-disclaimer component-list licence-texts
s02 component-list licence-texts
s03 scope accuracy other-locations licence-summaries component-list licence-texts notice-files
s04 scope governing-licences warranty-disclaimer accuracy contact component-list licence-texts data-attributions
s05 scope governing-licences component-list licence-texts
s06 component-list other-locations
s07 component-list licence-texts
s08 scope component-list licence-texts
s09 scope component-list licence-texts
s10 component-list licence-texts
```

## Merged list (s01–s10, final)

Median position is the first row's rank divided by the sample's id count less one (0 = first, 1 =
last). Tiers per `formats/skeleton-format.md` (core ≥80%, common 40–79%, rare <40%); they are final:
the build is saturated at s10. *Commonly omitted* = fewer than 20% (1/10).

| Id | Count | Tier | Median pos. | Note |
|---|---|---|---|---|
| scope | 6/10 | common | 0.00 | |
| source-offer | 1/10 | rare | 0.20 | commonly omitted; licence-driven (LGPL/GPL), not law: root |
| governing-licences | 2/10 | rare | 0.24 | |
| accuracy | 2/10 | rare | 0.30 | |
| warranty-disclaimer | 2/10 | rare | 0.44 | |
| contact | 2/10 | rare | 0.49 | |
| licence-summaries | 1/10 | rare | 0.50 | commonly omitted; its one sample puts it before the list |
| component-list | 10/10 | core | 0.50 | |
| other-locations | 2/10 | rare | 0.67 | s03 near the top, s06 at the end |
| licence-texts | 9/10 | core | 1.00 | s06 keeps its texts in the app only |
| notice-files | 1/10 | rare | 1.00 | commonly omitted |
| data-attributions | 1/10 | rare | 1.00 | commonly omitted |

By count: 2 core, 1 common, 9 rare (12). Since the first batch, `scope` moved from core to common (4/5 →
6/10), and `governing-licences`, `accuracy`, `warranty-disclaimer` and `contact` from common to rare (2/5
→ 2/10): the saturation batch was all bare lists with little or no company text.

## Patterns (s01–s10)

Decision 39 applies to fixed tool sentences (s02's "The following npm package may be included in this
product:", repeated 1,182 times, counts once) and to the stock scope sentence shared by s01 and s08
(counts once).

- **component-list, layout:** 6/10 a block per entry, heading then notice or licence text (s01 s02 s04
  s07 s09 s10); 3/10 a table, one row per component (s03 s05 s08); s06 short bullets. 3/10 put a
  compact index before the texts (s05 and s08 tables linked to a licence appendix; s07 a name-and-licence
  index, of which 15 of 42 entries get no notice block).
- **component-list, unit of entry:** 7/10 one entry per component (s03 s04 s05 s07 s08 s09 s10; s02's
  tail too); s01 one entry per licence, split again per copyright holder (MIT ×21 on iOS), with package
  names in brackets, and one entry per font; s02's npm part one block per identical licence text, so the
  same MIT text recurs with different copyright lines; s06's app part one line per licence type with a
  dependency count, naming no component.
- **component-list, fields:** component name 9/10 (s06's app part names none). Licence named as a
  label 8/10 (SPDX ids s03 s05 s08 and s02's Rust/Go tail; short or long licence names s01 s06 s07 s09);
  s04 and s10 name no licence, so it is read from the text. Version 4/10 (s02 s03 s05; s07 now and
  then; s05 writes semver ranges, commit hashes and "latest" as found). Project or repository URL 5/10
  (s01 sometimes, s03, s05 in some tables, s09, s10). Copyright line given 7/10 (s01 s04 s07 s09 s10 as
  a line or upstream header, s02 and s03 inside the licence text); none in s05 s06 s08 (s05 leaves
  appendix placeholders unfilled, s08 drops the lines from its texts). Publisher 1/10 (s03).
- **component-list, grouping:** 5/10 group by platform, build target or product surface (s01
  Android/iOS/fonts; s02 npm bundle, Rust module, Go helper binary, native C++, ML; s03 frontend,
  backend, Docker, CDN; s05 seven platforms with counts; s06 website and app); 5/10 one flat list
  (alphabetical s04 s08 s10; no order s07 s09). s01 also orders by licence inside each part.
- **component-list, what is listed:** server-side components that are never shipped 3/10 (s03 backend
  and Docker, s05 three backend tables, s09 web server, PHP and framework); out of the id's meaning by
  the 2026-10-27 ruling. Transitive dependencies 4/10 (s02 s03 s05 s08; s03 says so). Fonts or design
  assets 4/10 (s01 bundled, s03 CDN-loaded, s06 web fonts, s10 icons and fonts with a trademark
  condition); AI models 2/10 (s01 with base models and use restrictions; s02 with file, source
  revision, training-data licence, changes made and an attribution line). Proprietary or
  source-available components in the same list 4/10 (s01 Facebook SDK; s05 "Commercial / Proprietary";
  s08 FSL-1.1; s10 Intel MKL and Fair Source with a 100-user limit), never marked as not open source
  except s05. The company's own open-source projects beside third-party ones 1/10 (s04). Upstream
  notices nested whole inside an entry 4/10 (s02 ONNX Runtime, s04 CardIO, s09 Apache HTTP Server
  subcomponents, s10 multi-licence explanations for AWS Libcrypto, ring, LLVM, ICU4C).
- **component-list, upkeep:** 1/10 says how the list is kept current (s09 "updated periodically as
  dependencies change"); s07's copyright years end in 2013, so it looks long unrevised.
- **component-list, size:** about 1,000 entries (s01), 1,182 blocks over about 3,180 packages (s02),
  about 400 (s03), 13 (s04), 2,187 (s05), about 190 dependencies in 10 licence lines plus 4 fonts (s06),
  42 (s07), 710 (s08), about 22 (s09), 88 (s10).
- **licence-texts, placement:** 6/10 inside each entry, so a text repeats per entry (s01 the OFL per
  font, s02, s04, s07's blocks, s09 Apache ×3, s10 Apache ×4); 3/10 an appendix with each licence once,
  linked from the list (s05, s07, s08; s08 one block per SPDX expression, a dual-licence block holding
  only one option's text); s03 a collapsible excerpt per row (sometimes the README when no LICENSE file
  exists), plus a plain-text bundle; s06 none on the web, only inside the app. Entries by reference
  only: s02's Rust and Go entries (SPDX only), s03's Docker rows, s10's hunspell-asm (URL), s07's Apache
  blocks (short header pointing to the licence URL). Generic texts with the copyright slot empty: s05
  s07.
- **scope:** one sentence 5/10 (s01 all caps and hedged "may be contained", repeated per platform, and
  s08 the same stock sentence with the app named; s05 with the total count; s03 lead that also names
  the tool and what is included; s09 "compiled list"); s04 a dense legal paragraph with defined terms in
  capitals; none 4/10 (s02 s06 s07 s10), where only the title says what the page is.
- **contact:** 2/2 list what a request must contain (product and version, component, return address);
  s01 email plus postal address (inside the source offer), s04 postal only with named staff.
- **source-offer:** s01 only, Android part only: the LGPL-2.1 §6(c) / GPL-2.0 §3(b) written-offer
  form, three years from last shipment, to any recipient, free except media and shipping. The iOS part,
  which also lists copyleft licences, has none; s10 lists LGPL-3.0 and MPL-2.0 components with no offer.
- **warranty-disclaimer:** s01 the GNU wording for the LGPL parts; s04 a general disclaimer on behalf
  of the company and the upstream authors.
- **governing-licences:** s04 with defined terms and a carve-out for terms Lyft alone offers; s05 one
  clause in the opening sentence.
- **accuracy:** s04 framed as a request to verify and report errors; s03 "not legal advice", plus a
  caveat telling the reader to review copyleft terms.
- **other-locations:** s03 companion plain-text files and container copies; s06 a menu path in the app
  that holds the full list and texts (the web page is a summary only).

## Document level (s01–s10)

- **Words:** median about 17,800 (range 105–462,931); the count is driven by repeated licence texts
  (s01's font part is about three quarters of its words). s06 (105) is a summary page.
- **Carrier:** 9/10 one web page on the company's site; s07 a help-center article. None split across
  pages. s03 links two companion plain-text files; s06 sends the reader into the app.
- **Title:** "Open Source Software Notices" (s01), "Third Party Licenses" (s02), "Third-Party Open
  Source Licenses" (s04), "Open Source Licenses" (s05), "Attributions" (s06), "Open Source Attribution
  Page For Venmo" (s07), "Open source acknowledgements" (s08), "Open Source Notices" (s09), "Open Source
  Libraries" (s10), a descriptive title (s03).
- **Generator or tool:** named on the page 2/10 (s02 `generate-license-file` for the npm part, with a
  hand-written tail for non-npm components; s03 `license-checker` with a UTC timestamp and the npm
  regenerate command, in the developer's own page template); generated but not named 3/10 (s05:
  uniform tables, per-platform counts, `#license-<SPDX>` anchors; s06: per-licence counts in the form
  `cargo-about` prints, most likely that tool; s08: uniform rows, SPDX slug anchors, package and licence
  counts, on an Astro site); hand-kept 5/10 (s01 inconsistent spacing and duplicate font headings; s04
  pasted LICENSE files with markdown left in; s07 inconsistent names between index and blocks; s09 three
  entry header styles and missing separators; s10 mixed heading forms and links).
- **Structure:** contents list 1/10 (s05, with counts); summary figures 3/10 (s05 per platform, s06 per
  licence, s08 package and licence totals); headings per platform part 5/10 (see `component-list`
  grouping); no numbering in any sample.
- **Register:** the company's own words are a small share or none: none at all below the title 4/10
  (s02 apart from tool lines and provenance notes, s06 apart from one pointer, s07, s10); one or two
  sentences 3/10 (s05 s08 s09); a short header and offer (s01); a formal legal preamble (s04);
  technical and maintainer-facing (s03).
- **Recurring elements:** a date 3/10 (s03 generation timestamp, s08 "Last reviewed", s09 "Last
  Updated" with time zone); none 7/10. Language versions: s04 English preamble plus a French copy; s03
  an EN / Traditional Chinese switcher. s08 thanks the open-source community.
- **Not sections:** see the note under *Section ids*.

## Regional content

No extraction table in s01–s10 carries a `[law: …]` cell. The copyleft source offer (s01) and the
Apache NOTICE duty (s03) come from the licences, not from a law, and stay in the root.

| Region | Content | Id | Samples |
|---|---|---|---|
| ca (qc) | French copy of the preamble beside the English one; the extractor guesses it is for Quebec users; untagged, no law named | scope, governing-licences, warranty-disclaimer, accuracy, contact | s04 |

## Copies (rule 4)

None in s01–s10: no two tables share headings in the same order or quotes beyond one stock sentence.
s02 and s03 are both npm tool output, but from different tools with different layouts; s05's and
s08's generators are not named and their layouts differ (s05 version column and platform tables; s08
two columns with summary figures). Generated samples count as their own samples (decision 26):

- s02 Granola: whole `generate-license-file` output for the npm part, with its fixed sentences
  unedited, plus a hand-written tail.
- s03 EchoManage: `license-checker` data inside the developer's own page template.
- s05 Cantina: an unnamed generator's tables and licence appendix.
- s06 Zed: likely `cargo-about` counts, on a hand-written page with web fonts.
- s08 Propel: an unnamed generator's package table and licence blocks.

A shared block, not a copy: s01 §3 and s08 §1 open with the same stock attribution sentence ("The
following sets forth attribution notices for third party software that may be contained in portions
of…"), confirmed in the `raw/` texts; s08 names the app and adds a line of thanks. Their tables share
nothing else, so both stay samples; the sentence counts once in patterns (decision 39).

c12 Customer Thermometer and reserve M2 Mill share one intro block (`candidates.md`); neither was
extracted.

## First-batch qualification

All 5 valid. Borderline ones:

| Sample | Verdict | Why |
|---|---|---|
| s02 Granola (mid) | valid | desktop app only; no company framing at all, so it gives only `component-list` and `licence-texts`. |
| s03 EchoManage (small) | valid, borderline | written for a maintainer or distributor rather than the end user (internal paths, regenerate command); it is the live public notice, so rule 4 keeps it. |
| s05 Cantina (mid) | valid, borderline | licence appendix leaves `<year> <copyright holders>` unfilled and many cells read "See package"; it is the live notice. |

## Saturation

A sample is new only when it has a section whose content fits no id in *Section ids*; how it writes a
known id never makes it new (`build/build.md` step 3). *User run*: `saturated: true` when all of s06–s10
are non-new; otherwise stop at s10 with `saturated: false`.

Batch 1 in pool order: s06–s10 (c06–c10). All valid: each is the company's own live notice in English,
and each company is its own group (rule 5: Zed Industries, PayPal for Venmo, Propel, YourMyDS, Figma;
none shares an owner with s01–s05). No copies (rule 4; see *Copies* for the shared s01/s08 sentence).
s06 is borderline: a 105-word web summary whose full list and texts sit inside the app; it is the
company's live web notice, so it is kept.

| Sample | Verdict | Why |
|---|---|---|
| s06 Zed (small) | not new | web fonts and per-licence dependency counts to `component-list` (no component named in the app part: a pattern); the pointer to the in-app licence view to `other-locations`. 1 non-new |
| s07 Venmo (large) | not new | no intro; name-and-licence index and per-component notice blocks to `component-list`; licence texts once each plus per-block texts to `licence-texts`. 2 |
| s08 Propel (mid) | not new | the stock "may be contained" sentence to `scope`; package table to `component-list`; per-licence blocks to `licence-texts`; summary figures and "Last reviewed" date are document level. 3 |
| s09 YourMyDS (small) | not new | lead to `scope`; hand-compiled entries, including the web server's nested subcomponent notices, to `component-list` and `licence-texts`; server-side entries and the upkeep sentence are patterns; timestamp is document level. 4 |
| s10 Figma (large) | not new | 88 library entries, design assets and proprietary components to `component-list` and `licence-texts`; the one licence given by URL is a by-reference pattern. 5 |

**Stop:** all 5 of s06–s10 are non-new: `saturated: true` at s10. No id was added after the first
batch: 12 ids throughout. c11–c15 are not extracted.

Valid samples: 10 (s01–s10); by size 4 large, 3 mid, 3 small. Invalid: none.

## Changes

- 2026-10-27 (owner ruling): `warranty-disclaimer` stays an id. The licences require the disclaimer
  and it tells the reader something, so it is not decision-44 boilerplate. No count changed.
- 2026-10-27 (owner ruling): `component-list` covers only components shipped to the user. Listing
  server-side components that are never shipped (s03 §5–§6, s05 §6–§9, and from batch 1 s09's web
  server, PHP runtime and framework entries) is a pattern, not part of the id's meaning. The meaning was
  changed to say so before s06–s10 were judged. No count changed: every sample also lists shipped
  components.
- 2026-10-27 (step 4): all 12 ids stay ids here; the skeleton folds four rare ones that no fact
  decides (`skeleton-format.md`, rare drafting section): `governing-licences` (2/10) and `accuracy`
  (2/10) into `scope`, `contact` (2/10) into `source-offer` (the request channel the offer needs;
  s04's channel without an offer is a pattern there), `licence-summaries` (1/10) into
  `licence-texts`. `warranty-disclaimer` stays a section (owner ruling), gated on copyleft
  components. The skeleton has 8 sections: 2 core, 1 common, 5 rare.

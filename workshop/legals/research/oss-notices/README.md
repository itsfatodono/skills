# oss-notices: build record

Built 2026-10-27. Skeleton: `plugins/fatodono-founderkit/skills/legals/skeletons/oss-notices.md`. This was a small
creator build (PLAN.md decision 48): `build/build.md` *User run* numbers apply instead of the
pre-built ones, because tools generate most of an open source notice and its structure is short.
That means one collector slice, up to 15 candidates of mixed sizes with no size thirds, a first batch
of 5 and one saturation batch of 5.

## Files

- `candidates.md`: the pool of 15, the reserve, the drops at the first-screen check.
- `pool/oss.md`: raw rows from the one `pool-collector` slice.
- `samples/sNN.md`: one extraction table per sample, s01–s10.
- `raw/`: stripped sample texts (git-ignored, never committed).
- `merge.md`: section ids and meanings, mapping notes, section map, merged list with counts and
  median positions, patterns, document level, *Regional content*, copies, first-batch
  qualification, saturation log, changes.

## Run

- **Routes run:** R1 (App Store listings) and R4 (web-only developer sites), in one slice of 39 raw
  rows.
- **Pool:** 15 candidates (5 large, 5 mid, 5 small, by pool order, not by quota), English only.
  Group check (rule 5) and first-screen check at selection; 11 URLs dropped (not the document, no
  text without JavaScript, or blocked). One raw row was re-attributed: the "MEATER" row's URL is
  Customer Thermometer's own notice (c12).
- **What counts:** a web-reachable list of third-party components with their licences. A licence
  for the company's own open-source project, or a legal hub that only links to notices, is not a
  sample. Generated lists are valid samples (decision 26).
- **First batch:** s01–s05 (c01–c05). All valid; none replaced.
- **Saturation:** one batch, s06–s10 (c06–c10), all valid and all non-new. No section id was added
  after the first batch.
- **Stop reason:** all 5 samples of the *User run* saturation batch are non-new:
  `saturated: true`. `sample_count: 10`. c11–c15 and the reserve were not extracted.

## Owner rulings

- `warranty-disclaimer` stays an id: the licences require it and it tells the reader something, so
  it is not decision-44 boilerplate.
- `component-list` covers only components shipped to the user. Lists of server-side components
  (s03, s05, s09) are a pattern; the skeleton tells the writer to leave them out.

## Invalid

None. Borderline but valid (details in `merge.md`): s03 is written for a maintainer rather than the
end user; s05 leaves licence placeholders unfilled; s06 is a 105-word web summary whose full list sits
inside the app.

## Templates and copies

Rule 4: no copies. Five samples are tool output and count as their own samples (decision 26): s02
(`generate-license-file`, named), s03 (`license-checker`, named), s05 and s08 (unnamed generators), s06
(most likely `cargo-about`). s01 and s08 open with the same stock attribution sentence, which counts
once in patterns (decision 39). c12 and reserve M2 share an intro block; neither was extracted.

## Sizes

Valid samples: 4 large, 3 mid, 3 small. No size thirds apply in a *User run*.

## Samples

All fetched 2026-10-27, language `en`.

| Sample | Company | URL | Sector | Size |
|---|---|---|---|---|
| s01 | TikTok Pte. Ltd. | https://www.tiktok.com/legal/page/global/open-source/en | entertainment | large |
| s02 | Granola Inc. | https://www.granola.ai/third-party-licenses | productivity | mid |
| s03 | Chau Duong (EchoManage) | https://www.echonx.com/license.html?lang=en | reference | small |
| s04 | Lyft, Inc. | https://www.lyft.com/legal/licenses | travel | large |
| s05 | Cantina, Inc. | https://cantina.com/licenses | photo-video | mid |
| s06 | Zed Industries | https://zed.dev/attributions | developer-tools | small |
| s07 | The Delancey Corporation (Venmo) | https://help.venmo.com/cs/articles/open-source-attribution-page-for-venmo-vhel275 | finance | large |
| s08 | Propel Inc | https://www.propel.app/open-source-acknowledgements/ | finance | mid |
| s09 | Duncan Cuthbertson (YourMyDS) | https://yourmyds.com/open-source-licenses | health-fitness | small |
| s10 | Figma, Inc. | https://www.figma.com/open-source/ | graphics-design | large |

Versions taken: s01 the global English page; s03 the English default of its EN / Traditional Chinese
switcher.

## Skeleton

8 sections: 2 core (`component-list`, `licence-texts`), 1 common (`scope`), 5 rare
(`source-offer`, `warranty-disclaimer`, `other-locations`, `notice-files`, `data-attributions`).

Of the 12 ids in `merge.md`, 4 are folded, since they are rare and no fact decides them:
`governing-licences` and `accuracy` into `scope`, `contact` into `source-offer`, and
`licence-summaries` into `licence-texts`. None is out of the root.

Two sections carry an *Avoid* line taken from the licences themselves, not from a regulator's
guidance: copyleft components with no source offer (`source-offer`, 2/10) and licence texts with
the copyright line dropped (`licence-texts`, 3/10).

## Relation to the EULA

`skeletons/eula.md` has a `third-party-components` section (10/22) that points to these notices.
Both read `facts.product.third_party_components`. When a product gets both, the EULA section stays
short and points here.

## Facts

Two keys added to `helpers/facts-schema.md`: `facts.product.source_code_offer` (download or written offer,
request channel and details, period, cost) and `facts.product.data_attributions` (map data, datasets
and other non-code sources that need an attribution line).

One existing key extended: `facts.product.third_party_components` now covers only shipped
components and gains optional fields: per component `version`, `copyright`, `url`, `kind`, `target`
and `notice`, plus `other_copies` and `generator`. Its *Look* now names lockfiles and the notice
generators (`oss-licenses-plugin`, AboutLibraries, `Acknowledgements.plist`, LicensePlist, Flutter
`LicenseRegistry`, `license-checker`, `generate-license-file`, `cargo-about`, `go-licenses`,
`pip-licenses`). The first fields and their meaning are unchanged, so the EULA reads it as before.

Reused: `facts.product.name`, `facts.product.services_in_scope`, `facts.company.legal_name`,
`facts.company.contact_email`, `facts.company.address`. `tools/check-facts` exits 0.

## Regional content

No extraction table carries a `[law: …]` cell. One sample (s04) adds a French copy of its preamble,
probably for Quebec; no law is named. No region block is warranted.

## Catalog

Row added to `helpers/catalog.md` under the new family `licensing`. Trigger: does the shipped
product contain open-source or other third-party components (answered from
`facts.product.third_party_components`)? An in-app acknowledgements screen that already lists every
component and licence can stand instead, and the writer says so.

## Open for the owner

- **Family name.** `licensing` is a new family; no existing family (`privacy-notices`, `terms`,
  `commerce`, `internal-compliance`) fits.
- **Avoid from licences.** `skeleton-format.md` describes *Avoid* as "the authority's guidance". Here the
  authority is the licence text. Keep both lines, or move them to *Patterns*?
- **`warranty-disclaimer` gate.** It is rare and needs a fact condition, so it applies only when copyleft
  components ship. Its two samples were one GNU-wording case and one general case. Gate it on
  something else, or make it `always`?

## Lessons

- **The company writes almost nothing.** 4/10 have no own words below the title. The skeleton's
  value is the frame around a tool's list: scope, the source offer when copyleft code ships, and
  the copyright and NOTICE duties that the samples often break.
- **Server lists creep in.** 3/10 list backend components that never reach the user; the shipped-only
  rule keeps the notice to what the licences actually require.

# Region format

A region is one law area: `eu` (GDPR), `uk` (UK GDPR), `us` (federal and state laws, together),
`tr` (KVKK and Turkish commerce law), `br` (LGPD). Everything a region adds to the skill lives
in its own folder, `regions/<code>/`, and nowhere else. The skill finds regions by listing
`regions/`; no shared file names a region.

Adding a region is adding its folder. Removing a region is deleting its folder. Neither changes
any other file. This is what lets a contributor add a region without touching existing work
(*Contributions*).

## Folder

```
regions/<code>/
  region.md          ← required: the region's header and sample sources
  facts.md           ← the region's own fact keys; omitted when it has none
  catalog.md         ← items only this region needs; omitted when it has none
  <doc-id>.md        ← one per catalog item the region contributes to
```

`<code>` is lowercase, two to four letters, and unique; use the ISO 3166-1 alpha-2 code for a
country and `eu` for the European Union.

### region.md

```yaml
code: br
name: Brazil
laws: [LGPD (Lei 13.709/2018)]
languages: [pt]                 # sample and default output languages
storefront: br                  # App Store / Play country code for R1–R3
added: 2026-11-02
```

Body: `## Sources`, where samples for this region are found, in the shape of `build/sources.md`
*Routes* and *Documents*: storefronts, keyword sets, company lists, footer labels, sites that
block fetching. Shared routes (R1–R12) are named, not repeated.

### facts.md

Keys in the format of `helpers/facts-schema.md`, named `facts.<code>.<name>`
(e.g. `facts.br.encarregado` for a Brazil region). A region file names only shared keys from `helpers/facts-schema.md` and its
own `facts.<code>.*` keys, never another region's.

### catalog.md

Rows in the format of `helpers/catalog.md`, for items no other region needs (Turkey's
Mesafeli Satış Sözleşmesi, Germany's Impressum). Ids carry the code as prefix
(`tr-distance-sales`) so they never collide.

### <doc-id>.md

A region's contribution to one catalog item. Its frontmatter is the item's own format
(`formats/skeleton-format.md`, `formats/form-format.md`, `formats/template-format.md`, `formats/task-format.md`) plus:

```yaml
region: br
part: block                     # block | variant | whole
```

- **block:** additions to a shared document. The root skeleton holds the region-neutral
  sections; this file holds `## Sections` that apply only in the region (the Brazil part of the
  privacy policy). *Applies when* is implied by the region; a section adds a condition only
  when it needs a further one. A root item that exists only because laws require it (the
  RoPA) is **region-triggered**: its `helpers/catalog.md` trigger is "a region in
  `facts.users.regions` has a `block` for this item", so the root stays region-neutral and
  each region that requires the document says so by holding a block.
  In a **tabular** document (the root is a grid with one row per activity, as the RoPA), a
  block is columns, not a section. Each per-activity section adds one column after the root's
  columns and names it in a **Column** field; each record-level section adds one line to the
  root's controller block and names it in a **Header line** field. Both start with the code in
  capitals ("UK: Lawful basis (UK GDPR Art. 6)"). Every section has one of the two fields.

  **Avoid on root sections.** A block may end with `## Avoid on root sections`: one
  `### <root-section-id>` heading per root section, each with one **Avoid:** field in the format
  of `skeleton-format.md`. It marks a root pattern that this region's law makes invalid. The root
  keeps the pattern, since it is lawful elsewhere. A block may hold this part alone, with no
  `## Sections`, when the region adds no text to the document: its `## Document` then has only
  *Purpose*, and its `sample_count` and `scanned` are the root's, since its counts are the root's.
- **variant:** the region's version of a form, template or task that differs per authority
  (the trademark task at TÜRKPATENT, the KVKK standard contract).
- **whole:** a complete skeleton for an item in this region's `catalog.md`.

Its own `sample_count` and `scanned` date: a region file is built and refreshed on its own.

## Shared files stay region-neutral

The root skeletons, forms, templates, tasks, `helpers/catalog.md`, `helpers/facts-schema.md` and `build/sources.md`
never name a region code, a region's law, or a region's fact key. A root section may say that
regional additions follow; it never says which. `facts.users.regions` takes the folder codes
present plus `other`.

## Written documents

`doc-writer` writes the root skeleton's sections, then one regional part: a heading
("Regional notices", in the document's language) with one subheading per region in
`facts.users.regions` that has a `block` with `## Sections` for this document, in alphabetical
order of code. A table of contents, if any, lists the regional part's heading, not each region.
With no applicable block, the regional part is left out.

The document is one text for all its regions, so an *Avoid on root sections* entry in the block
of any region in `facts.users.regions` applies to the whole document.

So adding a region to a user's existing document adds one subheading and its text; removing one
deletes them. In patch mode that is the whole change.

A tabular document has no regional part. The writer adds each applicable block's columns
after the root's columns (regions in alphabetical order of code) and its header lines to the
controller block; a column that does not apply to a row reads "N/A". Adding or removing a region
adds or deletes only its own columns and lines.

## Contributions

A region is built and contributed on its own: its files stay under `regions/<code>/` and
`research/regions/<code>/`, and no other file names it. Who may change what is in the repo's
`CONTRIBUTING.md`.

A fact a region needs that `helpers/facts-schema.md` lacks is defined in its own `facts.md` as
`facts.<code>.*`, even when the fact is not specific to the region (a phone number, payment
methods). A key that looks shared gets a `- **Proposed shared key:** \`facts.<group>.<name>\``
line in its definition.

Promoting a key is the maintainer's job: when a second region needs the same fact, the
maintainer adds a shared key to `helpers/facts-schema.md` and renames the region keys to it in one
release. Contributors never promote keys.

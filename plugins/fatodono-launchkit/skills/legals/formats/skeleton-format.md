# Skeleton format

A skeleton describes how companies write one document. The build branch writes it;
`doc-writer` fills it; `doc-checker` checks a document against it. Every document skeleton
follows this format exactly. Forms, templates and tasks have their own formats:
`formats/form-format.md`, `formats/template-format.md`, `formats/task-format.md`.

## Header

YAML frontmatter:

```yaml
doc_id: privacy-policy          # matches helpers/catalog.md
title: Privacy Policy
kind: document
family: privacy-notices
sample_languages: [en]
sample_count: 23
saturated: true                 # 5 samples in a row added nothing new
scanned: 2026-11-02
format_version: 2
```

## Document level

`## Document` holds what applies to the whole document:

- **Purpose:** one sentence.
- **Shape:** how the document is laid out (single page, short summary + full text,
  tables vs prose), with counts.
- **Register:** plain language or legal register, sentence length, "we/you" or third person.
- **Recurring elements:** "last updated" line, definitions block, contact block, and so on,
  with counts.
- **Commonly omitted:** what most samples leave out of the document as a whole.

## Sections

`## Sections` lists sections in their typical order. Each section:

```markdown
### data-collected: Data we collect

- **Covers:** what personal data the service collects, grouped by source.
- **Prevalence:** 23/23 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.data.third_party_sources`
- **Patterns:**
  - 17/23 group by source (you give us / collected automatically / from third parties).
  - 9/23 use a table: data type, purpose, retention.
  - Categories are named ("device identifiers"), not individual fields.
- **Detail:** categories with "such as" examples (20/23); 3/23 list fields. No SDK or vendor names.
- **Quote:** "We collect information you provide directly to us." (s07)
- **Commonly omitted:** field-level lists; SDK names.
```

Field rules:

- **Section id:** kebab-case, unique within the skeleton.
- **Prevalence:** `count/sample_count (percent), tier`. Tiers:
  - **core** (≥80%): written in every document unless *Applies when* is false.
  - **common** (40–79%): written when its facts have values.
  - **rare** (<40%): written only when *Applies when* is true.

  A field a sample keeps but leaves empty ("n/a", a blank column) counts as present; *Patterns*
  then says how many filled it ("3/3 left it empty").
- **Applies when:** `always`, or a condition on fact keys
  (`facts.sales.purchase_channels` contains `web-direct`). The writer marks a section "not applicable" only through
  this field. A rare section needs a fact condition here, or the writer has no reason to
  include it; a rare drafting section that no fact decides (definitions, notices, evidence)
  is folded into the section it serves, as a pattern there.
- **Facts:** keys defined in `helpers/facts-schema.md` that the section may draw on; its
  *Patterns* decide which it states, and at what level. A skeleton never describes how to find
  a fact.
- **Patterns:** how samples write the section, with counts when a choice splits the samples.
- **Avoid:** optional. A pattern some samples use that breaks a binding text (a law, a
  regulation, a licence), or that the authority enforcing it calls invalid, with its count and
  the source it breaks ("2/20 build KVKK consent into the form; KVKK Board explicit-consent
  guide"). Wrong information is *Avoid* too: a period, limit or rule the law sets differently
  ("delivery within 3 months" against a 30-day maximum). A pattern that is only open to challenge
  (a term on an indicative unfair-terms list, a point courts decide case by case) is not *Avoid*;
  it stays in *Patterns*. The writer never writes an *Avoid* pattern, whatever its prevalence,
  even when the user asks for it.
- **Detail:** the level the section writes at: what the majority names and what it keeps
  general, with counts where samples split. It is the samples' depth, so it also says what none
  of them names when a product's facts would tempt a writer to (vendor names, hosts, settings,
  mechanisms, the product's own numbers). `doc-writer` writes at this level; `overshare-checker`
  checks against it. A skeleton scanned before 2026-11-07 may lack it; there the majority
  pattern sets the level.
- **Quote:** optional, at most one sentence, tagged with its sample id from `research/<doc-id>/`.
- **Commonly omitted:** what most samples leave out of this section.

## Regions

Root skeletons are region-neutral: no *Applies when* on `facts.users.regions`, no pattern that
names a specific law, no region's fact key. What one law requires goes to that region's
`block` file, per `formats/region-format.md`. So does an *Avoid* that rests on one region's law:
the root keeps the pattern, which is lawful elsewhere, and the region's block marks it *Avoid*
(region-format.md, *Avoid on root sections*). A root *Avoid* rests on a text that binds in
every region, such as a licence. A region file in this format adds `region` and `part` to
the header. A block for a tabular document adds one field to each section, after *Covers*:
**Column** (the column heading it adds) or **Header line** (the line it adds to the controller
block), both starting with the region code in capitals.

## Valid skeleton

A skeleton is done when every section has every field, every prevalence count is
≤ `sample_count`, every fact key exists in `helpers/facts-schema.md` (or, in a region file, in its
region's `facts.md`), and a root skeleton breaks no rule of *Regions*. Every entry under a block's
*Avoid on root sections* names a section id of the root skeleton.

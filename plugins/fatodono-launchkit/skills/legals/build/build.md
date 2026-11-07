# Build a skeleton

Produces `skeletons/<doc-id>.md` from real company documents. Read `formats/skeleton-format.md` first;
the skeleton you write must be valid by its rules.

Inputs: a `doc_id` from `helpers/catalog.md` (or a new document's id, title and family), optionally a
region code (*Region run*), and optionally a sector. A pre-built run has no sector; a sector run samples only that sector.

The steps below build a `document`. For the other kinds in `helpers/catalog.md`, follow
`build/build-form.md`, `build/build-template.md` or `build/build-task.md` instead.

## Steps

1. **Pool.** Gather up to 30 candidate documents into `research/<doc-id>/candidates.md`:
   company, URL, sector, size, base, language. *Base* is the company's home region (`US`,
   `EU (FR)`, `UK`), so the regional mix can be balanced and regional content traced (see
   `research/cookie-policy/candidates.md`).
   - **Collect.** Split the item's routes in `build/sources.md` into slices (a group of chart
     genres, a keyword set, a Play category group) and dispatch one `pool-collector` per
     slice, all at once. Each writes raw rows to `research/<doc-id>/pool/<slice>.md`; a
     re-dispatched collector writes to a new slice file, never over one another collector may
     still be writing. Plan
     the slices for about 90 raw rows in total, with at least one long-tail slice (R2) for
     small companies.
   - **Select.** Read the raw rows and pick the 30 yourself:
     - Pre-built run: no sector above a quarter of the pool; 10 each of large, mid and small
       companies (sizes per `build/sources.md`).
     - Sector run: that sector only, mixed sizes.
     - Region run: companies whose users include the region, documents in its language, from
       the routes in `regions/<code>/region.md`.

     - Every run: one candidate per company group (`build/sources.md` rule 5), checked now.
     - Every run: open each picked URL and read its title and first screen; a page that is
       another document (terms of use at an EULA link, a profile page) is dropped now, not at
       extraction.
     - A size that runs short stays short; never fill it from another size. Record the
       shortfall and its cause in `README.md` (most small sellers using one shared template,
       for example).

   Done when the pool holds 30 candidates or `build/sources.md` is exhausted.
2. **First batch.** Dispatch one `sample-extractor` per candidate for the first 15, 5 per size (all of them
   if fewer exist). Each writes `research/<doc-id>/samples/sNN.md`. A candidate that is
   unreachable or turns out to be a different document is replaced by the next unused
   candidate of the same size, so the size thirds hold. You may dispatch the next same-size
   candidates before a result comes back; spares that turn out unneeded are kept as later
   samples, and every judgement still goes in pool order.
   Done when 15 valid extraction tables exist, or the pool is empty. The first batch is 15 for
   every skeleton, since its size decides the saturation stop point.
3. **Saturation.** Extract further samples in batches of 5, in pool order, all of a batch at
   once. Judge them one at a time in pool order; samples past the stop point are kept. Before
   the first batch, write the merged section list of the first batch to
   `research/<doc-id>/merge.md` (step 4's ids). A sample is **new** only when it has a section
   whose content fits no id in the merged section list; that id is added. How a sample writes a
   known section (prose, a list, a table, a pointer to another page, folded into another
   section) never makes it new: record it, and step 4 counts the splits as patterns. A sample
   whose table matches an earlier one (`build/sources.md` rule 4) is a copy: it is not judged and
   does not count. To confirm a copy, compare the extractors' `raw/` texts first, before
   re-fetching.
   **Section ids.** An id is one kind of fact the document gives the reader (how to cancel;
   when money comes back; what is kept after deletion), not a heading. Content that gives the
   same kind of fact is one id, whatever its heading, place or length; content that gives a
   different kind is a new id even under a shared heading. Write each id's meaning in one line
   in `merge.md` before judging, and change it only with a note there. Site chrome (related
   articles, "still need help?" boxes, cookie banners) is never a section. In a notice (a
   document that informs, such as a privacy or cookie policy), neither is drafting boilerplate
   that gives the reader no fact about the subject (which language version binds, severability):
   it is noted in `merge.md` and never makes a sample new. In a contract, closing clauses are
   one section, as in the terms of service.
   Stop at 5 non-new samples in a row (`saturated: true`), or when the pool runs out
   (`saturated: false`).
4. **Merge.** Map every sample's sections to section ids: the same content under different
   headings is one id. For each id: prevalence count, median position (sets the order),
   patterns with counts where samples split (format among them: "17/30 write it as a list"),
   the level the section writes at, from the samples' *How it is written* (goes to *Detail*),
   and content found in fewer than 20% of samples
   (goes to *Commonly omitted*). Do the same for the document level.
   Content one law requires (GDPR legal bases, US state categories) is left out of the root
   skeleton, wherever the sample put it; the root keeps only what applies to every user. Record
   it in `merge.md` under *Regional content* with its sample ids, so a region run can start
   from it.
5. **Facts.** For each section, list the facts a writer needs. Reuse keys in `helpers/facts-schema.md`;
   add a missing key there with its question and where to look in code.
6. **Write.** Write `skeletons/<doc-id>.md`. Done when it is valid per `formats/skeleton-format.md`.
7. **Record.** Write `research/<doc-id>/README.md`: the sample list (id, company, URL, sector,
   size, language, fetch date) and the stop reason.

## User run

A run in the user's own repo (`SKILL.md` *Build branch*) is a sector run sized for one user. It
replaces the numbers above:

- **Pool:** one `pool-collector`, one slice: the chart (R1, R3) and keyword search (R2) of
  `facts.product.category`. Select up to 15 candidates, mixed sizes; no size thirds.
- **First batch:** 5 samples.
- **Saturation:** one batch of 5. `saturated: true` when all 5 are non-new; otherwise stop there
  with `saturated: false`.

Every other rule of the steps holds.

## Region run

Builds one region's files under `regions/<code>/` (`formats/region-format.md`). It never edits a
file outside that folder and `research/regions/<code>/`.

1. **Region.** If `regions/<code>/region.md` does not exist, write it: header and sources.
   Done when its sources name at least one route that lists companies in the region.
2. **Items.** For each catalog item the region adds to, run the build for that item's kind with
   the region as input:
   - `block` for a root document: steps 1–7, where the extractor reads only the content that
     applies in this region. A global pool's samples that carry the region (`merge.md`
     *Regional content*) count toward the batch.
   - `variant` for a form, template or task: its build file, against this region's authority.
   - `whole` for an item only this region needs: add its row to `regions/<code>/catalog.md`,
     then steps 1–7.
   New fact keys go to `regions/<code>/facts.md`, never to `helpers/facts-schema.md`.
3. **Record.** Research files go to `research/regions/<code>/<doc-id>/`.

Removing a region deletes `regions/<code>/` and `research/regions/<code>/`.

Patterns are described in your own words. A quote is at most one sentence. No sample's full
text is stored anywhere but the git-ignored `raw/` folder, which is never committed or shipped.

## Extraction table

One file per sample, `research/<doc-id>/samples/sNN.md`:

```markdown
---
sample: s07
company: Example Inc.
url: https://example.com/privacy
sector: productivity
size: large            # large | mid | small | none (standard forms)
language: en
fetched: 2026-11-02
words: 4120
---

## Document
- Shape: summary box on top, full text below.
- Register: plain, "we/you", short sentences.
- Recurring elements: last updated date; contact email at the end.

## Sections
| # | Heading as written | Covers | Format | How it is written | Quote (≤1 sentence) |
|---|---|---|---|---|---|
| 1 | What we collect | personal data by source | table | groups by source; categories, not fields | "We collect information you provide directly to us." |
```

*Format* is `prose`, `list` or `table`, or one of the layout marks `pointer`, `embedded`.
Numbered clauses are prose, field blocks are a list; a prose section with one bulleted line
stays prose.
*Covers* states what kind of fact the section gives (retention periods, processor
categories), never the company's actual values.
*How it is written* includes how deep the section goes: what it names (fields, vendors, hosts,
numbers, mechanisms) and what it keeps general ("recipients by category, one tool named as an
example"; "safeguards in general terms").
In a root run, a cell whose content one law requires starts with `[law: <law and article>]`, so a
region run can read the table again instead of fetching the sample.

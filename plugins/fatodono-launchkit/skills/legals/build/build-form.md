# Build a form skeleton

Produces `skeletons/<doc-id>.md` for one console questionnaire. Read `formats/form-format.md` first;
the skeleton you write must be valid by its rules.

Inputs: as in `build/build.md`. A sector applies only to a sampled form.

Every question and every **Rule** comes from the platform's official documentation. Samples
only fill **Common answers**.

## Steps

1. **Questions.** From the platform's official documentation, list the live form's questions
   in the form's own order, each with a q-id, its allowed answers and its rule. A question the
   form repeats per item (each data type in a privacy label) gets one q-id per item. Fill the
   **Form** block from the same documentation and the upload tool's documentation. Record each
   page in `research/<doc-id>/README.md` under *Sources*: URL, fetch date, the q-ids it supports.
   Done when every q-id is supported by a source, and every question in the output file's own
   schema (an export template or upload format) is in the list.
2. **Source.** Set `source: sampled` when `build/sources.md` names a public place that shows this
   form's answers per app; otherwise set `source: official` and go to step 7.
3. **Pool.** As `build/build.md` step 1, with apps in place of companies: each candidate is a store
   listing (app, developer, URL, store category, size). The store's primary category is the
   app kind that *Common answers* counts by.
4. **First batch.** As `build/build.md` step 2. Each `sample-extractor` receives the step 1 question
   list and writes `research/<doc-id>/samples/sNN.md` per the extraction table below. A
   listing that shows no answers for this form is replaced from the pool.
5. **Saturation.** As `build/build.md` step 3, with this test: a sample is **new** when it records a
   (q-id, answer) pair not yet in the tally, or has an *Unmapped* row. Before the next sample,
   settle every *Unmapped* row in step 1: add the missing question and re-map earlier samples
   to it, or note under *Sources* why the item is outside the form.
6. **Tally.** For each q-id, count each answer per store category (`n/N`, N = samples in that
   category) and in total. A question no sample shows gets "not visible on listings".
   Done when every q-id has *Common answers*.
7. **Facts.** As `build/build.md` step 5. A rule names fact keys and how they decide the answer; how
   to find each fact lives in `helpers/facts-schema.md`.
8. **Pitfalls.** For each question, list:
   - rejection or enforcement reasons the platform's official documentation names for this
     form (review guidelines, policy pages, help pages on form issues), added to *Sources*;
   - each other catalog item that states the same facts (the privacy policy, the other
     platform's form, the privacy manifest), by `doc_id`: the answer must agree with it.

   Done when every question has pitfalls traced to a source or a `doc_id`, or
   "none documented".
9. **Write.** Write `skeletons/<doc-id>.md`. Done when it is valid per `formats/form-format.md`.
10. **Record.** Complete `research/<doc-id>/README.md`: *Sources*, the sample list (id, app,
    developer, URL, category, size, fetch date) and the stop reason, or `source: official`.

Rules and pitfalls are written in your own words. Records hold URLs, dates and mapped
answers; the pages themselves stay on the web.

## Extraction table

One file per sample, `research/<doc-id>/samples/sNN.md`:

```markdown
---
sample: s07
app: Example Notes
developer: Example Inc.
url: https://apps.apple.com/app/id0000000000
category: Productivity   # the store's primary category
size: mid                # large | mid | small
fetched: 2026-11-02
---

## Answers
| q-id | Shown on listing | Answer |
|---|---|---|
| email-address | Email Address; Linked to You; App Functionality | collected; linked; app-functionality |

## Unmapped
| Shown on listing | Why no q-id fits |
|---|---|
```

*Answer* uses the q-id's allowed values from step 1. *Shown on listing* is the listing's own
label, one line at most. A question the listing does not show gets no row.

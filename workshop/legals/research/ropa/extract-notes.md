# ropa: extraction notes

Item-specific additions to the extraction table in `build.md`, given to every
`sample-extractor` for `ropa`. They fix what one sample is and what a "section" is, so the
tables merge.

## What one sample is

A RoPA is a record set, not one page.

- **One file with many rows** (a spreadsheet, a PDF table, a data audit): read all of it, every
  sheet or tab, plus the landing page that links it.
- **A register of one file per activity** (EU bodies, some universities): read the register
  page (the index), then three records: the first listed, one about staff or HR, and one about
  the body's core work. When the records share one form, extract the form once and note in
  *Document* how the three differ.
- **A standard form or regulator model** (`size: none`): read the blank form and its
  instructions or worked example. Rows are its fields; the instructions say how to fill them,
  which goes in *How it is written*.

## Document notes

Besides Shape, Register and Recurring elements, write these lines under `## Document`:

- **Status:** full internal record, public summary of it, FOI release, or blank model.
- **Activities:** number of records or rows.
- **Grouping:** how the rows are grouped or ordered (by department, by data subject, by
  system, none).
- **Unit of one row:** a processing activity, a department, a data asset or system, a data
  category.
- **Scope:** controller record only, or also a processor record (activities done for others).
- **Record fields:** the field or column labels as written, in order.
- **Absent:** usual RoPA content the sample does not have.
- **Size:** words, and for a spreadsheet the rows times columns.

## Sections

One row per field or column of the record, and one per document-level block (title,
introduction, statement of the legal duty, controller and DPO block, review or version line,
glossary, contact). *Heading as written* is the field label.

*Format*:

- `table`: a column in a grid where each row is an activity;
- `list`: a labelled field in a per-record form ("Purpose: ...");
- `prose`: running text;
- `embedded`: the content sits inside another field (say which);
- `pointer`: the field points to another document instead of giving the content (a retention
  schedule, a privacy notice).

*How it is written* states the kind of value (free text, a fixed vocabulary, yes/no, a period,
a reference), how long the typical entry is, and how specific (categories or named systems and
vendors). When a field exists because of one law, or names a law, an article or a law's
vocabulary (Art. 6 bases, Art. 9 conditions, a schedule of a national act, Reg. (EU)
2018/1725, a national registry), start the cell with `[law: <law and article>]`.

*Covers* names the kind of fact, never the body's values.

No template search: rule 4 is checked by the build across samples.

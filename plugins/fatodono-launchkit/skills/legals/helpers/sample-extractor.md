You read one sample and record how it is written. You see only this sample; the build branch
merges all samples later.

Paths to the skill's files are relative to the skill folder the dispatch names.

The dispatch gives you:

- `doc_id`, the sample id (`sNN`), and the candidate row: company or app, URL, sector, size,
  language;
- the recipe that defines your extraction table: `build/build.md` (documents) or `build/build-form.md`
  (forms), and, for a form, the question list;
- the path of `build/sources.md` and the output path `research/<doc-id>/samples/<sNN>.md`.

## Steps

1. **Fetch.** Fetch the URL with `curl` and strip the HTML yourself; WebFetch returns a
   summary and loses sections. A help center that renders with JavaScript or blocks bots often
   serves the text elsewhere: Zendesk at `/api/v2/help_center/<locale>/articles/<id>.json`,
   Intercom in its plain HTML, Apple in the `<noscript>` block, Shopify shops at
   `/policies/<name>`. Privacy request portals publish their form as data: OneTrust inline in
   `<script id="dsar-components-state">` (decode `&q;` `&a;` `&s;` `&l;` `&g;`, read the
   `/publish` entry; follow a `reDirectUrl` when the form is disabled), Transcend at
   `https://<host>/static/<host>/privacyCenterSubjects.json` with `privacyCenterMessages-en.json`,
   TrustArc at `submit-irm.trustarc.com/services/validation/api/v1/forms/<formId>/render?locale=en`
   (`intakeFormId` in the page script). When none of these works, use the latest Wayback capture, per
   rule 2 of *Candidates* in `build/sources.md`, and record the capture URL. A document held as
   images (a regulator's model inside a guidance note) is rendered and read from the images. Save
   the stripped text to `research/<doc-id>/raw/<sNN>.txt` (beside the output's `samples/`
   folder); the build compares these texts for copies. Done when you hold the
   full text of the document, or of the listing for a form.
2. **Qualify.** Check the sample against every rule of *Candidates* in `build/sources.md` except
   rule 4, which the build checks across samples. Done when
   each rule passes, or one fails: then write no table, append one line
   `sNN | url | rule | reason` to `research/<doc-id>/invalid.md`, and reply
   `invalid sNN: <rule>: <reason>`.
3. **Extract.** Fill the extraction table from the recipe, every row the sample has, in the
   sample's own order. *Covers* names the kind of fact a section gives, never the company's
   values. Patterns are your own words; a quote is at most one sentence.
   Done when every section of the document (or every answer the listing shows) has a row.
4. **Write.** Write the table to the output path. Reply `ok sNN: <rows> rows`.

The output file holds the table only: no copy of the page. Besides it you write only the
`raw/` text and, for an invalid sample, the `invalid.md` line.

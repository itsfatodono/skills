# Build a template

Produces `templates/<doc-id>.md` (the official text) and `skeletons/<doc-id>.md` (its blanks
and choices) for a `template` in `helpers/catalog.md`. Read `formats/template-format.md` first; the skeleton
you write must be valid by its rules. The copy ships with the plugin, so writing a filled
template needs no network.

Inputs: a `doc_id` from `helpers/catalog.md` (or a new template's id, title and issuer), and optionally a region
code (`build/build.md` *Region run*).

One doc id covers one text as its issuer publishes it. Modules inside one text are choices
(the EU SCCs: one text, four modules). Variants published as separate texts are separate doc
ids (the KVKK standard contracts: four texts, one per transfer type), each listed under the
same item in `helpers/catalog.md` with its own *Applies when*.

## Steps

1. **Source.** Find the text on the issuer's own site; other sites' copies only point to it.
   Record in `research/<doc-id>/README.md`: `official_url` (the issuer's page that publishes
   the text), the file URL, the fetch date, and `text_version`. `text_version` is the issuer's
   identifier: the instrument and its date (`(EU) 2021/914 of 4 June 2021`; KVKK Board decision
   `2024/959 of 4 June 2024`), plus the latest amending act if any; the publication date shown
   on the issuer's page only when it gives no identifier. Save the fetched file under
   `research/<doc-id>/source/` with its sha256. When the issuer publishes the text in several
   languages, fetch each and record which one binds (KVKK: signatures go on the Turkish text;
   EU: all official languages are equally authentic, ship English).
   EUR-Lex answers scripted requests with an empty 202; the Publications Office serves the
   same Official Journal text at `https://publications.europa.eu/resource/celex/<CELEX>` with
   `Accept: application/xhtml+xml`.
   Done when the source file, its hash and the issuer's `text_version` are recorded.
2. **Copy.** Write `templates/<doc-id>.md`: frontmatter `doc_id`, `text_version`, `language`,
   `source_url`, `fetched`, then the text **verbatim**: every word, number and punctuation
   mark of the source, in source order, footnotes included. Drop only layout: page numbers,
   running headers, line-break hyphenation. Markdown adds `#` headings for clause and annex
   titles and tables where the source has them. Blank markers stay exactly as the issuer
   wrote them (`[Specify time period]`, `……`, an empty `Address:`). Further official languages
   go to `templates/<doc-id>.<lang>.md`, built the same way.
   Done when the file holds the whole text, first heading to last annex.
3. **Verify.** For each copy, extract the source's text (`pdftotext`, or HTML stripped of
   tags) and strip the copy of frontmatter, HTML comments and the Markdown syntax step 2
   added. Normalize both (Unicode NFKC, whitespace collapsed to one word per line) and `diff`
   them. Fix the copy until it matches.
   Done when the diff is empty, or every remaining hunk is a layout artefact listed in the
   research README.
4. **Blanks and choices.** Walk the copy top to bottom and mark every place the text varies,
   with an HTML comment beside it: `<!-- blank:<blank-id> -->` or
   `<!-- choice:<choice-id>=<option> -->` (comments leave the verbatim check untouched).
   - **Choices:** modules (`MODULE TWO`), numbered options (`OPTION 1`, `1. SEÇENEK`),
     optional clauses (`Clause 7 – Optional`, `(Tarafların tercihine bağlı olarak sözleşmede
     yer verilebilir.)`), inline alternatives (`[Veri aktaran/Veri alıcısı]`), conditional or
     module-scoped text (`[Where the data exporter is established in an EU Member State:]`,
     `[For Module Three: …]`). For each, record how an unselected option is rendered (removed,
     or kept and marked), from the text's own drafting notes or the issuer's guidance.
   - **Blanks:** bracketed instructions, underscore or dotted leaders, empty labelled fields
     (party and signature blocks), annex fields and their explanatory notes. A blank that only
     the signatories fill (signature, signing date) gets `Fill: left for the signatories`.
   Done when a search of the copy for each marker form finds no unmarked occurrence.
5. **Facts.** As `build/build.md` step 5, keyed by blank and choice instead of section. A choice
   that is the parties' preference (sub-processor authorisation, governing law) still gets a
   key; its "where to look" says the code cannot show it.
   Give every choice a **Default** per `formats/template-format.md`.
   Done when every blank and choice, except those left for the signatories, has fact keys
   that exist in `helpers/facts-schema.md`, and every choice has a default.
6. **After signing.** From the issuer's official pages (the law, implementing rules,
   announcements), record: whether the signed text must be filed or notified; the deadline
   and the event that starts it; who files (possibly a choice, as in Article 16 of KVKK
   contract 2); the channels; what goes with the filing; duties triggered later (KVKK: notify
   again when Annex I or III changes); any transition period for contracts signed on an
   earlier `text_version`. Cite each point's page and fetch date in the research README. Example:
   KVKK requires notification within five business days of the last signature, by hand,
   registered e-mail (KEP) or the online notification module, with documents proving the
   signatories' authority.
   Done when every point has a value with its source, or reads "none stated" with the pages
   checked.
7. **Write.** Write `skeletons/<doc-id>.md` per `formats/template-format.md`: one *Choices* entry per
   `choice` comment id, one *Blanks* entry per `blank` comment id.
   Done when the skeleton is valid per `formats/template-format.md` and each distinct comment id in
   the copies has exactly one entry.
8. **Record.** Complete `research/<doc-id>/README.md` with the verification result and the
   watch list: the pages where the issuer announces new versions, amendments, repeals and
   new instruments for the same case.
   Done when the README holds the step 1, 3 and 6 records and a non-empty watch list.

## Refresh

1. Re-fetch the source file and compare its sha256 with the research record. If it changed,
   re-extract its text and diff it against the copy as in step 3; only a word difference
   counts as a new text.
2. Check the watch list since `scanned`: an amending or repealing act, or a new decision
   number, is a new `text_version` even when the old file is still online. A new instrument
   for a case the template does not cover (e.g. the Commission's planned SCCs for importers
   directly subject to the GDPR) is a new catalog item, not a new version.
3. Re-check the step 6 pages; deadlines and channels change on their own (the KVKK module
   opened in October 2024).

Done when the template is either unchanged, with `scanned` updated and the check recorded,
or rebuilt through steps 1–8 under its new `text_version`, with the previous version's hash
and identifier kept in the research README for the creator's diff review.

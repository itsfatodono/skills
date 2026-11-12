# contractor-agreement: notes for every sample-extractor

These notes add to `helpers/sample-extractor.md` and `build/build.md` *Extraction table*; they
never replace them. `research/...` means `/Users/fth/Projects/fatodono-skills/workshop/legals/research/...`.

1. **Fetch.**
   - SEC EDGAR exhibit: `curl -s -H 'User-Agent: fatodono-legals-research admin@example.com' <url>`
     (exactly that User-Agent; never a real person's email). Strip the HTML with a small python3
     script, save to `research/contractor-agreement/raw/<sNN>.txt`, then read the raw text in
     parts (it may be long). An EDGAR exhibit is the filer's own text as filed and counts as
     current (`build/sources.md` *Few public samples*: EDGAR exhibits are full samples).
   - Standard form (docx, pdf, web generator): download into a new empty folder under `/tmp/`,
     never inside the repo. Read a docx with `textutil -convert txt -stdout <file>` and a pdf
     with `pdftotext -layout <file> -` (or python3 if pdftotext is missing). Save the text to the
     raw path. A form's cover page, statement of work and standard terms are one sample (rule 6:
     one document split over parts). Fill-in blanks and drafting notes are part of the form:
     record what the blank asks for, not a value.
2. **Qualify, scope.** Besides the *Candidates* rules, apply the *Fit rule* in
   `research/contractor-agreement/candidates.md`, judged on the text: if the text carries the
   terms of another relationship with the consultant (a departure from employment or board
   service: separation or transition terms, retirement, continued vesting under a separation
   agreement; or an appointment as a corporate officer or director: an officer or board title,
   D&O cover, board duties), it fails rule 6 (scope). Then write
   `<sNN> | <url> | 6 (scope) | <reason>` to `research/contractor-agreement/invalid.md` and reply
   `invalid <sNN>: 6 (scope): <reason>`. A consultant who is a founder, shareholder, director or
   scientific adviser but whose text is a clean engagement for defined services passes; say so
   in *Parties*.
3. **Document block.** Besides Shape, Register and Recurring elements, add:
   - `- Parties:` who engages whom (roles, not names: "a company engages an individual"),
     whether the contractor is an individual or a firm acting through a named person, the kind
     of services, and any relationship with the company the text states.
   - `- Attachments:` each exhibit or schedule (statement of work, compensation schedule, form of
     task order, a separate confidentiality or invention-assignment agreement) and whether its
     text is included or only referenced.
4. **Rows.** One row per numbered section or heading, in the sample's order. A sub-clause that
   gives a different kind of fact from its section (an IP assignment inside a confidentiality
   section, a non-solicit inside the term section) gets its own row, headed
   `<section heading> (<sub-topic>)`. Each attached exhibit or schedule gets its own row(s).
   Closing boilerplate: one row per clause. The signature block is one row.
5. **Cells.** *Covers* names the kind of fact, never the parties' values (no names, amounts,
   rates, dates). *How it is written* says how deep it goes: what it names (fee basis, invoice
   cadence, payment days, notice days, a cap, a mechanism) and what it keeps general.
6. **Law tags.** This is a root run: a cell whose content one jurisdiction's law requires or is
   drafted for starts with `[law: <law and section>]`. Examples: California Labor Code § 2870
   invention notice; Defend Trade Secrets Act 18 U.S.C. § 1833(b) immunity notice; IRS Form
   1099 / W-9 reporting; IRC § 409A; US securities law (insider trading, Regulation FD); HIPAA;
   FCPA; a worker-classification test (California AB5, IRS common-law test, UK IR35); New York
   City's Freelance Isn't Free Act. A clause naming a governing law as the parties' choice is not
   a law tag.
7. `words` in the frontmatter counts the agreement with its exhibits.
8. Quotes: at most one sentence, and never one that carries a party's name or a fee value.

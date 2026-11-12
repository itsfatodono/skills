# ip-assignment: extraction notes

Item-specific rules every `sample-extractor` of this build follows, on top of
`helpers/sample-extractor.md` and the extraction table in `build/build.md`. Written by the builder
before the first batch, 2026-11-12.

## Fetch

- EDGAR (`www.sec.gov/Archives/...`) refuses requests without a `User-Agent` header: send
  `-H "User-Agent: fatodono research fth@example.com"`. EDGAR exhibits are the filer's own
  document (rule 1) and the filed version is current (rule 2) unless the candidate row says
  otherwise.
- Strip HTML yourself (drop `<script>`/`<style>`, turn `</p>`, `<br>`, `</div>`, `</tr>` into new
  lines, remove tags, unescape entities). Save the stripped text, whole, to `raw/<sNN>.txt`. Read
  it in parts.

## Which part is the sample (rule 6)

- The sample is the IP assignment agreement: the employee or consultant form (PIIA, CIIAA,
  invention assignment and confidentiality agreement) or the founder form (technology or IP
  assignment by an individual to the company).
- When the exhibit is another agreement (offer letter, employment, stock purchase) with the
  assignment attached in the same file, extract only the attached assignment, plus any clause of
  the host agreement that assigns IP or points to the attachment (one row each, marked `embedded`
  in *Format*). Say in *Document* what the host is.
- Exhibits and schedules of the assignment itself (prior-inventions list, a state-law notice, a
  termination certificate, a list of excluded companies, a form of assignment for one patent) are
  part of the sample: one row each, in place.

## Rows

- One row per numbered section, or per heading where the text is not numbered. A sub-clause
  gets its own row only when it gives a different kind of fact from its section (a moral-rights
  waiver or power of attorney inside the assignment section; a non-solicit inside "Covenants").
  Do not split one section into one row per sentence.
- *Covers* names the kind of fact (what is assigned, the period after leaving during which
  inventions are presumed the company's), never the values (names, dates, salary, the
  inventions listed).
- *How it is written* says how deep the clause goes: what it lists (kinds of IP, kinds of
  confidential information, the duration of a covenant as "a fixed number of months"), whether
  the obligation is one-way or mutual, what triggers it, and what it keeps general.
- A blank in the form (`[____]`, "[Company Name]", an empty schedule) is a field the signer or
  company fills: record it as a blank, with what it asks for.

## Law-tagged cells

In a root run, a cell whose content one law requires starts with `[law: <law and section>]`. For
this item, typical ones (tag what the sample actually shows; name the law the sample names, or the
one its wording comes from when it names none):

- US state invention-assignment limits and their notices: California Labor Code §§ 2870–2872,
  Washington RCW 49.44.140, Illinois 765 ILCS 1060, Minnesota § 181.78, Delaware 19 Del. C. § 805,
  Kansas K.S.A. 44-130, North Carolina G.S. 66-57.1, Utah 34-39, Nevada NRS 600.500, New Jersey
  N.J.S.A. 34:1B-265, New York Labor Law § 203-f.
- US federal: Defend Trade Secrets Act whistleblower immunity notice (18 U.S.C. § 1833(b)); SEC
  whistleblower carve-outs (Rule 21F-17); NLRA Section 7 carve-outs.
- US state restrictive-covenant rules: California Business and Professions Code § 16600 and
  Labor Code § 925, Massachusetts Noncompetition Agreement Act, and similar.
- Other countries: UK Patents Act 1977 ss. 39–43, German ArbnErfG, Turkish Industrial Property
  Law no. 6769 art. 113 ff., and any other named statute.

A clause that a law shapes but every user would still write (a general "to the extent permitted
by law" carve-out) is not tagged.

## Document block

Add these lines to `## Document` besides Shape, Register and Recurring elements:

- **Signer and context:** who signs (employee, consultant, founder, officer), what the agreement
  is given for as written (employment, shares, the payment of a nominal sum), and the host
  document if any.
- **Form origin:** what the text itself shows about its origin ("Form of", a law-firm footer or
  document number, the filer's name only in blanks, a title shared with other forms). Never search
  for the template source.

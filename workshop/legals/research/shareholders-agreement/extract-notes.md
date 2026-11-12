# shareholders-agreement: extraction notes

Item-specific additions to the extraction table in `build.md`, given to every `pool-collector`
and `sample-extractor` for `shareholders-agreement`. They fix what one sample is and what a section
is, so the tables merge.

## What the document is

The skeleton is for the agreement two or more founders sign about the company they own together:
what each holds, how founder shares vest and come back when a founder leaves, roles and
commitment, IP and confidentiality owed to the company, how decisions are taken and deadlocks
broken, how shares may be transferred or sold, and how the agreement ends. Founder-stage texts
are rare in public, so the pool also takes later agreements that govern the same relationship
among a private company's owners.

**In (the document named in the dispatch):** a contract among the shareholders (stockholders,
members of a company limited by shares) of one **private** company, with or without the company
as a party, that sets how they hold, govern, transfer or exit their shares, or what founders owe
the company as owners. Titles seen: Founders' Agreement, Co-founder Agreement, Shareholders'
Agreement, Stockholders' Agreement, Voting Agreement among a private company's holders,
Joint Venture or Shareholders' Agreement between the few owners of one company, the shareholder
part of a Subscription and Shareholders' Agreement, a model or programme template of any of these.

**Out (another document, `sources.md` rule 6):**

- M&A support or voting agreements (holders agree to vote for a merger or tender);
- agreements of a **listed** company with its sponsor or holders that start at or after the IPO
  (director nomination, governance, sponsor stockholders' agreements); a pre-IPO agreement that
  ends at the IPO is in;
- investors' rights or registration rights agreements, lock-ups, standstills;
- stock purchase, subscription or restricted stock purchase agreements standing alone, option
  agreements;
- LLC operating agreements, articles, charters, bylaws (the constitution, not an agreement among
  owners);
- agreements called "Founders Agreement" that are something else (a parent's management-fee or
  royalty agreement with a subsidiary, a services contract with a founder).

When the title is ambiguous, the parties and recitals on the first screen decide.

## EDGAR

- Full-text search: `https://efts.sec.gov/LATEST/search-index?q="<phrase>"&forms=<forms>&startdt=<date>&enddt=<date>`
  (JSON, `&from=<n>` pages by 100). Send `User-Agent: fatodono-research research@example.com`;
  never put a real person's email in it.
- A hit's `_id` is `<accession>:<file name>`; the document is
  `https://www.sec.gov/Archives/edgar/data/<CIK without leading zeros>/<accession without dashes>/<file name>`.
- File types: keep `EX-10*`, and for this item also `EX-4*` and `EX-9*` (shareholders' agreements
  are often filed as instruments defining holders' rights or as voting trusts).
- Size and sector come from the filer; estimate, never research (`sources.md` *Size*). Base is
  the filer's home country (`US`, `UK`, `IL`, `EU (DE)`, `CN`).

## Document notes

Besides Shape, Register and Recurring elements, write these lines under `## Document`:

- **Stage:** `founder` (founders only, at or near formation), `early` (founders with angel or
  seed holders), `vc` (preferred-stock investors), `jv` (two or three corporate or individual
  owners of a joint company), `model` (blank form).
- **Parties:** kinds and number (founders only; founders and company; company, investors and key
  holders; two corporate owners).
- **Status:** signed exhibit, executed form with blanks, or blank model.
- **Companion documents named:** other documents the agreement relies on (charter or articles,
  investors' rights agreement, stock purchase or vesting agreement, IP assignment, employment
  agreements), and which subjects it leaves to them.
- **Absent:** usual shareholders-agreement subjects the sample does not have (vesting and leavers,
  IP, non-compete, deadlock, decision rules, transfer restrictions, exit).
- **Size:** words.

## Sections

One row per article or top-level numbered section, in the sample's order. Split a section into
more rows only when a sub-clause gives a different kind of fact (a right of first refusal and a
tag-along under one "Transfers" article are two rows; five sub-clauses of one right of first
refusal are one row). The definitions article is one row (say how many terms and which key ones
it defines). Each schedule or exhibit (joinder or deed of adherence, spousal consent, list of
holders, valuation method) is one row. The signature block is one row. The closing
miscellaneous clauses may be one row per clause, or one row listing them.

*How it is written* says how deep the clause goes: what it fixes as a number or mechanism
(notice days, a vesting schedule, a valuation method, a quorum, a percentage threshold) and what
it leaves to a schedule, the board or later agreement. Never record the company's own values
(names, share counts, prices, percentages specific to this deal); say "a percentage threshold",
"a fixed number of days".

When a clause exists because of one jurisdiction's law, or names a statute or a law's own
mechanism (Delaware General Corporation Law sections, a "Section 83(b)" election, the UK
Companies Act 2006, the Turkish Commercial Code, Israeli Companies Law, securities-law legends,
a stamp-duty or tax rule), start the cell with `[law: <law and section>]`.

*Covers* names the kind of fact (transfer restrictions on founder shares; the board's size and
who appoints it), never the deal's values.

Word models: `textutil` and a plain strip of `word/document.xml` drop footnotes and endnotes,
where model forms keep their drafting notes; read `word/footnotes.xml`, `word/endnotes.xml` and `word/comments.xml` too
(footnotes on s31, comments on s33).

No template search: rule 4 is checked by the build across samples.

Read nothing but the files the dispatch names, `helpers/need-to-know.md` and the two format
files below. Write nothing.

You find **overshare** in one finished document: text past **need-to-know**, as
`helpers/need-to-know.md` defines it. Its writer had every fact about the product; you have none
on purpose, so you judge each sentence by what its section's patterns call for, never by whether
it is true. You report; the main agent fixes.

Paths to the skill's files are relative to the skill folder the dispatch names.

The dispatch gives you the document, its skeleton and region files, and for a patched document
the headings its writer changed: check only those, the rest is the user's own text. The
skeleton's fields are in `formats/skeleton-format.md`; the regional part's layout in
`formats/region-format.md` *Written documents*.

## Overshare

A sentence (a table row, a list item) is need-to-know when a pattern of its section carries it,
at the level `helpers/need-to-know.md` sets. What the law asks is need-to-know however it is
worded: its fix is the level's wording, never a cut. Copied text stays out of the check.

Overshare comes in four kinds:

- **depth:** a fact below its pattern's level: fields for a category; how a safeguard, sign-in
  or limit works; an internal component, hostname, storage path or setting; a timing, count or
  threshold the product holds to that no law or store rule asks for; how the technology works,
  past the one sentence that says what data it uses.
- **surface:** what only the team sees: the address of an admin, staff or internal tool; a
  staff-only or hidden feature or mode, named anywhere, a prohibition included.
- **repeat:** an identity detail (the postal address, registry numbers, KEP) outside the one
  section `helpers/need-to-know.md` gives it.
- **stray:** a sentence that no pattern of its section carries.

## Steps

1. **Read.** Read the skeleton's and the region files' sections. Done when you can name, for
   each section, the level it writes at, in a few words.
2. **Check.** Read the document sentence by sentence against its section. Done when every
   sentence is need-to-know or a finding with its kind.
3. **Reply.** `clean`, or one line per finding:
   `<file>:<line> <depth|surface|repeat|stray>: <what it says> → <the need-to-know wording, or "cut">`.

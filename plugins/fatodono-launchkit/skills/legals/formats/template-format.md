# Template format

A template skeleton describes an official text whose wording is fixed by its issuer (the
KVKK standard contract, the EU SCCs). Only the blanks change. The build branch writes it per
`build/build-template.md`; `doc-writer` fills it; `doc-checker` checks the blanks against it.

Header: `doc_id`, `title`, `kind: template`, `issuer`, `official_url`, `text_version`,
`scanned`, `format_version`.

## Template
- **Purpose:** one sentence.
- **Fixed text:** `templates/<doc-id>.md`, a verbatim copy of the official text at
  `text_version`, with blanks and choices marked by `<!-- blank:<id> -->` and
  `<!-- choice:<id>=<option> -->` comments. Further official languages sit at
  `templates/<doc-id>.<lang>.md`; the skeleton names which language binds.
- **After signing:** filing or notification steps, who files, the deadline.

## Choices
### <choice-id>: <where it sits in the text>
- **Options:** each option, and how an unselected one is rendered (removed, or kept and marked).
- **Facts:** keys that pick the option.
- **Default:** the option to recommend, with a one-line reason: the one the facts point to;
  when the facts cannot decide, the one the issuer's guidance names, else the first.

## Blanks
### <blank-id>: <where it sits in the text>
- **Facts:** keys.
- **Fill:** how the facts become the text.

Valid when every blank and choice comment in the copies has exactly one entry here, and
every choice has a default.

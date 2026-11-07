# Build a task skeleton

Produces `skeletons/<doc-id>.md` for a `task`: a registration or filing (VERBİS, ETBİS, İYS),
a set of agreements (DPAs with processors), or a check of the user's own product (unsubscribe
mechanism, price display). Every value comes from the authority's own procedure. Read
`formats/task-format.md` first; the skeleton you write must be valid by its rules.

Inputs: a `doc_id` from `helpers/catalog.md` (or a new task's id and title), and optionally a region code
(`build/build.md` *Region run*). Tasks are not sampled: there is no sector and no pool.

## Steps

1. **Authorities.** Name who runs the procedure: an agency (KVKK for VERBİS, GİB for
   e-Arşiv), a platform (Apple), a standard's owner (AICPA for SOC 2), or, for DPAs, the
   processors themselves. A task split across authorities that each have their own procedure,
   fee and outcome (trademarks at TÜRKPATENT, EUIPO and USPTO) becomes one skeleton per
   authority, `<doc-id>-<authority>`, each listed under the item in `helpers/catalog.md` with its own
   *Applies when*. Run the remaining steps once per skeleton.
   Done when every skeleton id has one authority and one `official_url`, its main procedure
   page (for DPAs, the legal text that requires them).
2. **Sources.** Collect the official sources (see *Sources*) into the research record and
   write every value the skeleton will state into its *Values* table with source ids:
   conditions and exemptions, outcome, fees with currency and as-of date, processing times,
   deadlines, renewal duties, prerequisites, and the steps in the authority's order.
   Done when every field `formats/task-format.md` asks for has a Values row with an official source,
   or a row marked **thin** where the official sources leave it open.
3. **Thin fields.** Fill each thin row from secondary sources, per *Sources*. Done when no row
   is thin: each has secondary sources or reads "not published by <authority>".
4. **Facts.** As `build/build.md` step 5. Keys are needed for each prerequisite, each condition and
   exemption in *Applies when*, each route choice, and the outcome when other items use it
   (e.g. VERBİS registration's outcome, `facts.registrations.privacy_regulator`). The rule's numbers stay in the condition; the facts carry
   the user's values (e.g. VERBİS: a future `facts.company.employees` against the current Board threshold).
   A prerequisite that is another task's outcome names that task's doc id.
   Done when every prerequisite, condition, route choice and used outcome has a key in
   `helpers/facts-schema.md`.
5. **Steps.** Write the steps in the authority's order, each with its official page and who
   does it (see *Who does a step*). Phrase each action so its end is visible: a confirmation
   screen, an email, an application number, a file.
   - **Routes:** alternative routes to the same outcome (Apple enrollment as an individual or
     an organisation; e-Arşiv through GİB's portal or a private integrator) become a fact key,
     and each route-specific step carries its own *Applies when*. Every route ends in the
     outcome.
   - **Checks** of the user's product follow *Checks*.
   - **Repeated steps**, done once per item of a list fact (one DPA per entry in
     `facts.processors.list`), are written once with the variants the procedure takes (DPA part of
     the terms, accepted in the console, signed on request). Find the variants by reading
     widely used vendors' pages until 5 in a row add no new variant (`build/build.md` step 3).

   Done when every step has an action, an official page and a who, and every route's last
   step ends in the outcome.
6. **Afterwards.** List every catalog doc id where the outcome must appear: documents whose
   skeleton names the outcome's key, and documents the authority's rules tie to it (a signed
   DPA → the sub-processor list; VERBİS registration → the retention and destruction policy).
   A target skeleton that does not name the key yet goes under *Follow-ups* in the record.
   Done when every listed doc id exists in `helpers/catalog.md`.
7. **Write.** Write `skeletons/<doc-id>.md` in English. Systems, forms, menus and buttons keep
   the authority's own names (e-Devlet, MERSİS, "Başvuru Yap") so the user finds them on
   screen. Mark each value from a secondary source `(secondary: r07)`.
   Done when it is valid per `formats/task-format.md`.
8. **Record.** Finish `research/<doc-id>/README.md` per *Research record*. Done when every
   value in the skeleton traces to a Values row.

## Sources

**Official** sources set the values: the authority's own pages (procedure, FAQ, system help,
fee schedule, announcements); the legal text it applies, from the official publisher
(mevzuat.gov.tr, EUR-Lex, eCFR, the Federal Register) with its amending decisions; a
platform's developer documentation; a vendor's own DPA page. When they disagree, the legal
text decides duties, thresholds and deadlines, the procedure pages decide how a step is done,
and the newest dated fee schedule decides the fee; note the conflict in the Values row.

**Secondary** sources fill thin rows only: guides by professional bodies and law, accounting
or audit firm guides dated within the last 12 months. One is enough for screen-level detail
(which menu, which button). A fee, threshold, deadline or duty needs two independent secondary
sources that agree, and goes under *Review* for the creator.

## Who does a step

- `agent`: finishable with the repo, `legal/facts.md` and public web pages: find a vendor's
  DPA page, gather what a form asks, draft the text to paste, check the code.
- `user`: needs the user's identity or authority: a login (e-Devlet, Apple Account, a vendor
  console), a signature, a payment, a phone or postal verification, a declaration in the
  user's name, or a wait on the authority with its stated time.

A step that needs both becomes two: the `agent` step prepares what the `user` step submits.

## Checks

A task that checks the user's own product turns each requirement of the official text into a
check step with the fields `formats/task-format.md` gives. *Passes when* names something the code or
the running product shows as true or false; a rule in judgement words ("clear and
conspicuous") takes the concrete form the official guidance gives. Who: `agent` when the code
or a local run answers it, `user` when it needs production (a received email, a live store
page). The outcome is every check passing, dated.

## Research record

`research/<doc-id>/README.md`:

```markdown
---
doc_id: developer-registration-apple
scanned: 2026-11-02
---

## Sources
| id | kind | publisher | url | page date or version | fetched |
|---|---|---|---|---|---|
| r02 | platform-doc | Apple | https://developer.apple.com/help/account/membership/D-U-N-S/ | — | 2026-11-02 |

## Values
| field | value | sources | note |
|---|---|---|---|
| duration | D&B up to 5 business days, then up to 2 for Apple | r02 | |

## Review
## Follow-ups
## Changes
```

*Kind* is one of `procedure`, `guide`, `fees`, `announcements`, `legal-text`, `platform-doc`,
`vendor-page`, `secondary`. *Changes* logs each refresh: date, field, old value, new value,
source.

## Refresh

1. Re-fetch every source and re-extract every Values row; a changed value updates the
   skeleton and is logged under *Changes*.
2. Look for rules issued since `scanned` in the authority's announcements and the legal
   text's amendment history (VERBİS exemptions have changed by Board decision several times).
   A new rule becomes a source, and the fields it touches run through steps 2–7 again.
3. A source that moved or vanished is replaced from the authority's site; with no
   replacement, its rows go back to thin.

Done when every Values row is re-confirmed or updated, the skeleton is valid again, and
`scanned` is the refresh date.

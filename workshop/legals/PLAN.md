# fatodono-legals: plan

Name: `legals`

## Goal

A Claude Code plugin that writes a startup's legal and compliance documents for its own app.
The skill reads the user's codebase, asks only what the code cannot answer, and fills
pre-built **skeletons**. A skeleton is learned from how real companies write that document:
which sections they include, how common each section is, how they phrase it, and what they
leave out.

Roles:

- **Creator** (us): builds the skeletons once with the builder, ships them, refreshes them.
- **User**: installs the plugin and runs it on their own app. Normally never samples anything.

## Structure

```
workshop/legals/                     ← development folder in fatodono/skills
  PLAN.md                            ← goal, structure, decisions
  plans/                             ← one file per item: what is built, what is open
  CONTRIBUTING.md                    ← how to add or remove a region
  tools/check-contribution           ← fails a contribution diff that edits existing files
  tools/check-overshare              ← counts overshare in a written legal/ folder (decision 57)
  tests/local/                       ← per-product rules for check-overshare; git-ignored
  research/<doc-id>/                 ← builder records: sample URLs, scan dates, extraction tables
                                       (no full sample texts; not shipped)
  research/regions/<code>/<doc-id>/  ← the same, per region
  ../../plugins/fatodono-launchkit/  ← what ships; everything above stays in workshop/legals/
    .claude-plugin/plugin.json
    skills/legals/
      SKILL.md                       ← two branches: write (default) and build
      helpers/
        <name>.md                    ← each subagent's instructions; no harness-specific agent files
        catalog.md                   ← every document: id, family, trigger questions, skeleton path
        facts-schema.md              ← every fact key: question text + where to look in code
        grill.md                     ← how the user is asked: fact tree, rounds, recommendations
        de-slop.md                   ← the line edit slop-editor runs (decision 51)
        need-to-know.md              ← how much a document says; doc-writer and overshare-checker (decision 57)
      formats/
        skeleton-format.md           ← format for documents
        region-format.md             ← the region folder; the contribution rule
        form-format.md               ← format for console forms
        template-format.md           ← format for fixed official texts
        task-format.md               ← format for registrations and checks
      build/
        build.md                     ← the builder method for documents; routes the other kinds
        build-form.md
        build-template.md
        build-task.md
        sources.md                   ← where samples are found, per family
      skeletons/<doc-id>.md          ← one per catalog item, dated, region-neutral
      templates/<doc-id>.md          ← official texts, versioned
      regions/<code>/                ← one folder per law area (eu, uk, us, tr, ...):
        region.md                      header and sample sources
        facts.md                       facts.<code>.* keys
        catalog.md                     items only this region needs
        <doc-id>.md                    its block, variant or whole skeleton per item
```

Why it is shaped this way:

1. **One skill, two branches.** A separate builder skill would add an always-loaded
   description for every user. The build branch lives inside `legals`.
2. **Fact lookups live in `helpers/facts-schema.md`, not in skeletons.** A skeleton names fact keys
   (e.g. `facts.sdks`); how to find each fact is written once.
3. **`skeleton-format.md` is the single format** both branches read, so all skeletons match.
4. **Each skeleton has a header:** sample count and scan date. The skill uses the date to
   detect a stale skeleton. The sample list stays in `research/<doc-id>/`, so it never loads
   into a writer's context.
5. **Context boundaries come from subagents, not from splitting the skill.** The main agent
   knows the whole sequence but only does the light steps. The heavy steps run in subagents
   that see only their own task, so knowing what comes next cannot pull them into rushing.

## Write branch (user side)

| Step              | Who                               | Sees                                                             | Done when                                                                                                      |
| ----------------- | --------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 0. Disclaimer     | Main agent                        | —                                                                | "Not legal advice" said once                                                                                   |
| 1. Pick documents | Main agent                        | whole flow, `helpers/catalog.md`                                       | every catalog entry marked needed / not needed from the fixed trigger questions; user approved the list        |
| 2. Scan the code  | `code-scanner`                    | fact keys of the chosen skeletons, the repo, existing legal docs | every needed fact key has an entry in `legal/facts.md` with status `found`, `missing` or `conflict`            |
| 3. Ask the gaps   | Main agent                        | `legal/facts.md`                                                 | every key is `found` or `answered`; asked via AskUserQuestion, 4 per round, recommendation first               |
| 4. Draft          | one `doc-writer` per document     | its skeleton + `legal/facts.md` (+ the existing doc, if any)     | a draft in `legal/.drafts/` where every skeleton section is written or marked "not applicable" with a reason   |
| 5. De-slop        | one fresh `slop-editor` per draft | the draft, `helpers/de-slop.md`                                          | every edited sentence carries its original's term; the final file is written to `legal/` and the draft deleted |
| 6. Trim           | one fresh `overshare-checker` per document | the document, its skeleton and region files                | every sentence is need-to-know: carried by a pattern of its section, at that pattern's level                   |
| 7. Check          | `doc-checker`                     | documents, skeletons, `legal/facts.md`                           | every document covers its skeleton and matches `facts.md`; no two documents contradict                         |

Details:

- Output goes to `legal/` in the user's repo as Markdown. Documents are written in the language
  the user asks for. Skeletons are in English.
- **Existing document:** default is patch mode: keep the user's text, add missing sections, fix
  what contradicts `facts.md`. Full rewrite on request. The existing document may be in any
  format and place; the result always goes to `legal/<doc-id>.md` as Markdown and the original
  is never touched. Carrying it into the site's own format is the user's job. The existing document is also read as a
  source of facts.
- **Store forms** (App Store privacy label, Play data safety) are a branch of the same flow. The
  output is a file (fastlane JSON, Play CSV). Upload is offered if the user has the credentials
  and tools; otherwise the skill gives the upload command.
- **Stale skeleton:** older than 12 months → warn and offer a refresh through the build branch.
- **De-slop scope:** text the AI writes for other people to read: documents, and the
  human-facing strings in form outputs (permission usage strings, ATT prompt, App Review
  notes). Not official template text, not form data, not `legal/facts.md`, not task steps, and
  never the build branch. `slop-editor` keeps every fact, name, number, defined term, legal
  term of art, heading and region block; it changes wording, not meaning. `doc-checker` runs
  after it, so a meaning change is caught.
- **Regions:** adding or removing a region in a user's document adds or removes that region's
  subheading only (`region-format.md` _Written documents_). In patch mode this is the whole
  change.

## Build branch (creator run; user run)

The method lives in `plugins/fatodono-launchkit/skills/legals/build/build.md`: a pool of up to 30 candidates (10 each
large, mid, small), a first batch of 15 (5 per size), saturation (5 non-new samples in a row,
cap = the pool), merge, facts, skeleton, record. A region run builds one region block the same
way and touches nothing outside `regions/<code>/`.

A user run uses the same method, smaller (decision 33), for: a sector-specific sample, a document not in the
catalog, a stale skeleton.

## Decisions

Numbers are stable because research files cite them; a gap is a decision that no longer holds.

1. Sampling: mixed sectors and sizes for pre-built skeletons; same-sector only in a user run.
2. Region and language: regional documents sampled from Turkish companies, the rest from global English ones.
3. Quotes: patterns described, at most one-sentence quotes.
4. Scope: v1 covers all documents in the catalog.
5. Output: Markdown in `legal/`, facts in `legal/facts.md`; documents in the user's language, skeletons in English.
6. Staleness: warn after 12 months; creator refreshes every 3 months.
7. Name: `legals`.
8. Pricing: open, does not block v1.
9. Market: Turkey + global. Regional documents appear only when the trigger questions call for them.
10. Distribution: a Claude Code plugin (`fatodono-launchkit`); other agents get the same skill
    through skills.sh.
11. Location: `workshop/legals/` and `plugins/fatodono-launchkit/skills/legals/` in fatodono-skills.
    History before 2026-11-04 is in `~/Projects/legal-docs`.
13. Document selection uses fixed trigger questions from `helpers/catalog.md`.
14. Existing documents: patch mode by default.
15. Store forms: file output, upload optional.
16. Disclaimer: once, at the start.
17. Four kinds of catalog item, each with its own format and build file: `document` (sampled
    from companies), `form` (sampled from public store listings where answers are visible,
    otherwise from platform docs), `template` (official fixed text, blanks only; the official
    copy ships with the plugin), `task` (steps from the authority's procedure pages).
18. A catalog item lists one or more skeletons, each with its own _Applies when_: one per
    authority for a task (trademarks at TÜRKPATENT, EUIPO, USPTO), one per separately
    published text for a template (the four KVKK standard contracts). A region's skeletons are
    `variant` files in its folder (`regions/tr/trademark.md`).
19. Template choices carry a **Default** so the write branch can lead with a recommendation.
20. Sampling size: pool 30 (10+10+10 by size), no separate cap.
22. Regions: one block per law area (`eu`, `uk`, `us`, `tr`, `br`...), in both skeleton and
    written document; root sections are region-neutral; adding or removing a region touches
    only its block.
23. Items 14 (GDPR additions) and 15 (CCPA notice) are the `eu` and `us` blocks of the privacy
    policy, not separate documents. Item 11 (KVKK Aydınlatma Metni) stays separate, because
    Turkish companies publish it as its own page; the privacy policy's `tr` block links to it.
24. Regions are contributable. Each region is a folder, `regions/<code>/`, and the skill finds
    regions by listing them; no shared file names a region. Region-only items (Turkey's
    distance sales contract, Germany's Impressum) also live in their region's folder. A
    contributor defines every missing fact as `facts.<code>.*`, even a generic one. Updating a
    published region stays with the maintainer. Rules: `region-format.md`, `CONTRIBUTING.md`.
25. Build dispatch: a session runs about 20 subagents at once, shared by every agent in it;
    parallel builds keep at most 3 running each, and retry a subagent that dies on an overload
    (529). One merge helper serves the whole build and is resumed for each step, so the section
    ids stay in one context. An extractor's dispatch names its candidate by id (`c07` in
    `candidates.md`) rather than copying the row.
26. Templates are valid samples. A template or generated text is what companies publish, so it
    is not excluded and nobody searches for template sources. Samples with the same whole text
    count once (`sources.md` rule 4).
27. Saturation counts new sections only. A sample is new only when it brings a section id the
    list lacks; formats and layouts are counted as patterns but never reset the count. An id
    is one kind of fact for the reader, not a heading (`build.md` step 3).
28. Region-triggered root items. A document that exists only because laws require it (the
    RoPA) keeps a region-neutral root; its catalog trigger is "a region in
    `facts.users.regions` has a block for it" (`region-format.md`).
29. Region keys are promoted on use. A `facts.<code>.*` key with a "Proposed shared key" line
    moves to `helpers/facts-schema.md` only when a root skeleton or a second region needs it, never
    ahead of a consumer: a second consumer may cut the fact differently, which is cheaper to
    settle at promotion than to change a shared key after it.
30. Write branch scope: the catalog lists only items that have a skeleton. Forms, templates and
    tasks join the write branch and the description when their first item is built.
31. Build output: the run is decided by the working repo. In the skill's own repo it is a
    creator run, full size, written into the skill. In any other repo, including the owner's
    own apps, it is a user run (decision 33): research to `legal/.research/<doc-id>/`,
    skeleton and region files to `legal/.skeletons/` at their path inside the skill, new keys
    to `legal/.skeletons/facts-schema.md`; a file there replaces or adds the skill's file at
    the same path. The load path cannot decide it: a plugin installed from a local folder is
    read from that folder.
32. Asking leave: with a skeleton for every chosen item the write branch runs straight through;
    it stops only to ask facts. Before any build it checks in, in two or three plain sentences:
    which document has no data, how it will be researched, the cost, where the result goes;
    then it waits for an okay.
33. User runs are small: one `pool-collector` on the user's own field, a first batch of 5 and
    one saturation batch of 5 (`build/build.md` _User run_). The sample is the user's sector
    only, so a full 30-sample pool buys little.
34. Grill: everything the skill needs from the user (regions, the product's field, which
    documents, missing facts) is asked by `helpers/grill.md`: look first, ask the frontier of the fact
    tree in rounds, recommendation first. Every message to the user uses plain words, never the
    skill's own terms. The product's field is a fact, `facts.product.category`, which a user
    run's pool samples.
35. Models in internal documents: for an internal document that companies do not publish (the
    RoPA), regulator and association models may exceed the "at most half" cap in `sources.md`;
    the header says so.
36. EUDPR registers count: EU institutions' records under Regulation 2018/1725 count as `eu`
    RoPA samples, since its Art. 31 mirrors GDPR Art. 30. They are tagged `EUDPR`, and no
    GDPR-specific wording is taken from them.
37. Region blocks in tabular documents: where the document is a table (the RoPA), a region
    block is extra columns whose headings carry the region code, not a separate section.
    Adding or removing a region still touches only its own columns.
38. Cut-down templates: a sample that is a known template with parts removed counts as its own
    sample for prevalence (what it kept is the seller's choice) but adds no patterns.
39. Template wording counts once in patterns: a template's wording adds to patterns once,
    however many samples carry it, whether whole or as a block inside own text.
40. Class follows the data: no section is forced to a class against its prevalence, except
    under decision 53. A common section's fact gate must be a key the code scan nearly always
    fills.
41. First batch is 15 for every creator-run skeleton; the first batch size decides the stop
    point, so `build.md` states it.
42. What an EULA sample is: its core is a licence grant for software the user installs. Terms
    of use served at an EULA link are a different document and are replaced (`sources.md`
    row A).
43. Single-law seed items: 49 is only the DSA transparency report, an `eu`-only item. Its
    moderation-policy content goes into 46 community guidelines and the terms of service's
    `eu` block (DSA Art. 14 puts it in the terms). 10 Imprint stays `de`/`tr`: a separate
    imprint page is German practice, and the e-Commerce Directive Art. 5 duty is met by 9
    contact and the terms' `eu` block. 41 and 16 get `uk` blocks when built; 56 gets a `us`
    hint for state AI laws, with effective dates checked at build time.
44. Drafting boilerplate in a notice is not a section: in a document that informs (privacy,
    cookie policy), a clause that gives no fact about the subject (binding language version,
    severability) never makes a saturation sample new (`build.md` step 3). Contracts keep
    closing clauses as one section (terms of service, EULA `general`).
45. Shared KVKK pool: one `tr` pool (`research/regions/tr/kvkk-pool/`) feeds 11
    (`tr-kvkk-notice`), 12 (`tr-explicit-consent`) and the `tr` block of 13; 11 defines the
    `facts.tr.*` keys (purposes, legal bases, recipients, transfers) the other two reuse. 40
    (`tr-pre-contract-info`) reuses the `tr-distance-sales` pool.
46. KVKK 7499 cut-off: the 2024 amendment (Law 7499, in force 2024-06-01) changed Art. 6 and
    Art. 9. A sample of 11 is kept only if it is dated on or after 2024-06-01, its transfer
    section uses the new Art. 9 tools (adequacy decision, standard contract, binding corporate
    rules, occasional transfer), or it is undated with no transfer section (tagged
    `no-transfer`). The cut-off does not apply to 12 (consent to transfer abroad is still
    lawful for occasional transfers, Art. 9(6); a consent used for regular transfers is caught
    by decision 47) or to 13 (Arts. 11 and 13 are unchanged).
47. Consent guide check: during the merge of 12, every section and pattern is checked against
    the KVKK Board's guidance on explicit consent. A pattern the guidance calls wrong (consent
    asked for processing that has another legal basis, consent bundled with the notice or the
    contract) is _Avoid_ (decisions 50, 53), whatever its prevalence.
48. Small creator build for 8: `oss-notices` uses user-run numbers (one collector, up to 15
    candidates, first batch 5, one saturation batch of 5), because tools generate most of its
    content and its structure is short.
49. 13 is root plus regions: `data-subject-request` has a region-neutral root from a global
    pool, plus `tr`, `eu` and `uk` blocks (`us` only if the samples show it). The `tr` block
    comes from the shared KVKK pool (decision 45).
50. _Avoid_ field: an optional section field in `skeleton-format.md`. It names a pattern the
    authority's guidance calls wrong, with its count and the guidance. `doc-writer` never
    writes it, and `doc-checker` check 4 reports any match.
51. Build method: R4 may be scripted across many developer sites (`sources.md`). Candidates
    record each company's `base` region (`build.md` step 1). The agent running `SKILL.md` runs
    a build itself and never hands it to a subagent. Extractors save the stripped text to
    `research/<doc-id>/raw/<sNN>.txt`, which is git-ignored and never shipped, so rule 4
    compares these before re-fetching; invalid samples get one line in `invalid.md`. Open: a
    user run writes to `legal/.research/`, which the user's repo does not ignore.
52. De-slop: in the write branch, a fresh `slop-editor` runs `helpers/de-slop.md` on every AI-written,
    human-facing text before its file is written. `helpers/de-slop.md` is a line edit written for
    legal text from blader/humanizer and petergyang/no-ai-slop (MIT,
    `plugins/fatodono-launchkit/THIRD-PARTY-NOTICES.md`): words change inside each sentence,
    and each edited sentence is checked against its original, because in a legal document
    every sentence is a term. The open-source notices skip it: they are copied licence texts.
53. _Avoid_ means invalid. A pattern that breaks a law or regulation, that the enforcing
    authority calls invalid, or that states the law wrongly ("delivery within 3 months"
    against a 30-day cap) is _Avoid_ and is never written, even when the user asks. A pattern
    only open to challenge (an indicative unfair-terms list, a point courts decide case by
    case) is grey: it stays a pattern, the writer follows the usual majority rule, and the user
    may ask for it. An _Avoid_ resting on one region's law goes in that region's block under
    _Avoid on root sections_, since the same pattern is lawful elsewhere; a block may hold only
    that part, and an _Avoid_ in any of the user's regions applies to the whole document
    (`region-format.md`). The writer takes the user's requests in its dispatch and reports the
    ones an _Avoid_ refuses.
54. Contributions: a contributor may build a backlog document or a region. A pull request
    covers one document or one region and only adds: new files, plus appended lines in
    `helpers/catalog.md`, `helpers/facts-schema.md` and a region's `facts.md` / `catalog.md`. No existing line
    changes, the method files are closed, and deleting a region is the maintainer's job. Claims
    go through an issue; the maintainer keeps `plans/`. Rules: `CONTRIBUTING.md`.
55. Effort by job: an agent that only dispatches or records runs at medium: the main agent and
    `pool-collector` (Sonnet). One that reads, writes or judges runs at high or above:
    `sample-extractor`, `code-scanner`, `doc-writer`, `slop-editor`, `overshare-checker` and
    `doc-checker` at high;
    the merge helper at xhigh. In a creator run the merge helper does the judging (first-batch
    merge, saturation, merge, facts, skeleton) so the main agent stays a dispatcher.
56. Agents live in the skill. Each subagent's instructions are `helpers/<name>.md` inside the
    skill folder, so skills.sh carries them to Codex and OpenCode too. There are no plugin
    agent files and the files carry no frontmatter: the main agent starts each subagent fresh
    with its file, sets the effort `SKILL.md` lists for it and picks the model. Tool limits are written in the instructions, since no
    harness-neutral way enforces them.
57. Need-to-know. A document says what its skeleton's patterns call for, at the level the
    majority pattern writes; a fact in `legal/facts.md` is evidence that a sentence is true,
    never a reason to write one. The first syncflash run (2026-11-06) wrote every detail its
    51 KB `facts.md` held: admin and internal tool addresses, sign-in and rate-limit mechanics,
    cookie settings, internal components, a hidden staff mode named in a prohibition, the
    company address five times. A skeleton records only what samples do, so it cannot name what
    none of them does; the writer read that silence as leave. Every stage guarded completeness
    and none cut. So `doc-writer` writes need-to-know, and a fresh `overshare-checker` per
    document, blind to `facts.md` so it never weighs a sentence by its truth, reports depth,
    surface, repeat and stray text before `doc-checker` runs; `doc-checker`'s coverage then
    catches anything the law asks for that the trim lost. *Facts* in a skeleton section lists
    what it may draw on, not what it must state.

## Todo and the item list

Moved to [`plans/`](plans/README.md) on 2026-11-04: one file per item, plus
[`plans/skill.md`](plans/skill.md) for skill-wide work. The finished todo list and the seed
catalog are in the history of `~/Projects/legal-docs`.

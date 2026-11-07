# Contributing to legals

> [!CAUTION]
> **Building a document uses a lot of tokens.** One full build is about 35 subagents and can
> use up a good part of a usage window. Building several documents at once can use up all of it.
> Build one document at a time, and check the cost before every build.

Read the [root CONTRIBUTING.md](../../CONTRIBUTING.md) first. This file covers what is specific
to legals.

## How a document becomes part of the skill

The skill holds no templates. For each document it holds a **skeleton**: a record of how real
companies write that document. When the skill runs, an agent fills the skeleton with one app's
facts. A skeleton is built in eight steps:

**Collect → Pick 30 → Read 15 → Read until nothing is new → Merge → Name the facts → Write the
skeleton → Record**

| #   | Step                      | Who                                                | What happens                                                                                                            | Output                  |
| --- | ------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 1   | Collect                   | 5 `pool-collector`s, at once                       | Each goes through one slice of store charts, searches or web lists. About 90 companies in total.                        | `pool/`                 |
| 2   | Pick 30                   | main agent                                         | Picks 30: 10 large, 10 mid-size, 10 small. Opens each link once to make sure it is the right document.                  | `candidates.md`         |
| 3   | Read 15                   | 15 `sample-extractor`s, at once                    | Each reads one document and writes down its sections: what each one tells the reader and how.                           | `samples/sNN.md`        |
| 4   | Read until nothing is new | 5 `sample-extractor`s per round; merge helper judges  | 5 more documents per round. Stops after 5 in a row that add no new section.                                             | `merge.md`              |
| 5   | Merge                     | merge helper                                       | For each section: how many have it, where it sits, how they write it. Content only one law requires goes to its region. | `merge.md`              |
| 6   | Name the facts            | merge helper                                       | For each section, what the writer must know about the app (`facts.sales.free_trial`).                                   | `helpers/facts-schema.md`       |
| 7   | Write the skeleton        | merge helper                                       | The skeleton file, in the shape of `formats/skeleton-format.md`.                                                        | `skeletons/<doc-id>.md` |
| 8   | Record                    | main agent                                         | Which documents we read, which we threw out and why, and why we stopped.                                                | `README.md`             |

Research files are under `research/<doc-id>/`; the skeleton and the facts schema are under
`plugins/fatodono-founderkit/skills/legals/` (from the repo root). The full method is in `build/build.md`.

## A few rules worth knowing:

- **A section is one kind of fact**, such as "how to cancel" or "when the money comes back", not a
  heading.
- **Saturated** means 5 documents in a row added no new section. If the candidates run out
  first, the skeleton says `saturated: false`.
- **How common a section is decides whether it gets written:** 80% or more always, 40–79% when
  the app has the facts for it, under 40% only when a fact says the app needs it.
- **No full text is committed.** Only short notes and one-sentence quotes; the full text stays in
  the git-ignored `raw/` folder.

Forms, templates and tasks are built the same way, with their own build files
(`build/build-form.md`, `build/build-template.md`, `build/build-task.md`).

### What happens to the skeleton

**Pick the documents → Read the code → Ask the user → Fill the skeleton → Edit the wording →
Trim → Check**

| #   | Step               | Who                                   | What happens                                                                                                                                               |
| --- | ------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Pick the documents | main agent                            | Asks where the users are, takes a light look at the repo and lists the documents the app needs.                                                            |
| 2   | Read the code      | 1 `code-scanner`                      | Finds the app's facts in its code and existing policies and writes them to `legal/facts.md`.                                                               |
| 3   | Ask the user       | main agent                            | Asks only what the code could not answer.                                                                                                                  |
| 4   | Fill the skeleton  | 1 `doc-writer` per document, at once  | Writes the document from the skeleton and the facts.                                                                                                       |
| 5   | Edit the wording   | 1 `slop-editor` per document, at once | Makes the text read like a person wrote it. It never sees the facts, so it cannot change a promise.                                                        |
| 6   | Trim               | 1 `overshare-checker` per document, at once; main agent fixes | Finds text past what the document needs to say: internal detail, staff-only tools, repeats. It never sees the facts, so it judges what a sentence says, not whether it is true. |
| 7   | Check              | 1 `doc-checker`; main agent fixes     | Checks each document against its skeleton, the facts and the other documents. The main agent fixes what it finds and sends it back until it finds nothing. |

## Agents

The **main agent** is the session the user talks to. Everything else is a **subagent** it
starts. Each subagent's instructions are in `plugins/fatodono-founderkit/skills/legals/helpers/`, so they ship
with the skill to every harness.

- **Only the main agent starts subagents.** A subagent cannot start one of its own, so a build is
  never handed to a subagent as a whole. The main agent runs it and starts every collector and
  extractor itself.
- **One subagent, one job.** Each gets only what its job needs, writes its result to a file and
  replies in a few lines. The main agent's context holds the replies, never the documents.
- **Some agents are kept blind on purpose.** `slop-editor` starts in a fresh context and sees only
  the draft and `helpers/de-slop.md`. `overshare-checker` sees the document and its skeleton,
  never the facts. Neither checker writes.
- **Models and effort.** Each agent's effort is at the top of its file in
  `plugins/fatodono-founderkit/skills/legals/helpers/`; the merge helper's is in `SKILL.md` *Creator run*.
  The main agent sets them on every dispatch, with the model (`SKILL.md`).
- **Cost.** A full build in this repo is about 35 subagents per document. A build in a user's repo
  is smaller: 1 collector and 10 extractors. The skill asks the user before any build.
- **Limits.** A session runs about 20 subagents at once. Build several documents at once only
  when asked; then each document keeps at most 3 subagents running. A subagent that dies on an
  overload (529) is started again.
- **Merge helper.** In this repo the judging goes to one merge helper, resumed through the
  build: steps 4–7, so the section list stays in one context. It cannot start extractors; the
  main agent does.

## Contributing a document or a region

You can contribute two things: a **document** from [`plans/backlog/`](plans/README.md), or a
**region** (a law area such as Brazil). Nothing else is open to contributions. To fix or change
something that already exists, open an issue.

### Before you start

1. Open an issue named `Build <id>` (for a region, `Region <code>`). If one is already open,
   pick something else or ask there. The maintainer moves the plan file to `in-progress/`.
2. Build in a clone of this repo. A run here is full size: about 35 subagents per document and a
   good part of a usage window.

### Example prompt

Start Claude Code at the repo root with the plugin loaded (`claude --plugin-dir plugins/fatodono-founderkit`), set
`/effort medium` (the skill sets every subagent's own level), then:

```text
Build the skeleton for `beta-terms` (plans/backlog/beta-terms.md, issue #12).

Use the legals build branch. This is the skill's own repo, so it is a full-size
creator run. Read CONTRIBUTING.md first and keep to "What a pull request may change" and
"Never": add files, append only new rows and keys, leave the method files and plans/ alone.

Before you start collecting, tell me the slices, how many subagents and roughly what it costs,
and wait for my okay.

When it is done, run tools/check-facts and `npm run check` at the repo root, list every file
you added or appended to, and stop. Don't commit.
```

For a region, swap the first line for: `Build the "br" region (Brazil, LGPD), issue #12: its
region.md and its privacy-policy block.`

### What a pull request may change

One document or one region per pull request.

| You contribute                | You add                                                                                                               | You may append to (new lines only)                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| A document                    | `skeletons/<doc-id>.md`, `research/<doc-id>/`, and its region blocks `regions/<code>/<doc-id>.md` with their research | `catalog.md`: its row. `helpers/facts-schema.md`: new keys. A region's `facts.md`: new keys. |
| A region                      | `regions/<code>/` and `research/regions/<code>/`                                                                      | nothing                                                                              |
| A region's part of a document | `regions/<code>/<doc-id>.md` and `research/regions/<code>/<doc-id>/`                                                  | that region's `facts.md`: new keys. That region's `catalog.md`: its row.             |

### Never

- **Change or delete an existing line.** Not in a skeleton, a region, a fact key, or your own
  earlier contribution. Once it is merged, it belongs to the maintainer.
- **Change the method:** `SKILL.md`, `build/`, `formats/`, `helpers/`. If the
  method does not fit your document, say so in the issue.
- **Commit a sample's full text.** A quote is one sentence at most. Full texts stay in the
  git-ignored `raw/` folder.
- **Move a region key into `helpers/facts-schema.md`, or rename a key.** The maintainer does that when a
  second region needs the same fact.
- **Touch `plans/`.** The maintainer updates it when merging.

### Done means

- The skeleton is valid by its format file (`formats/skeleton-format.md`, or the one for its kind).
- `research/<doc-id>/README.md` lists every sample read and says why the build stopped.
- `tools/check-facts` exits 0, and so does `npm run check` at the repo root.
- The pull request goes to `staging`. Don't write a changeset.

The first form, template or task also needs the write branch to learn that kind. The maintainer
adds that after merging.

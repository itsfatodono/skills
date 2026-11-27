---
name: playbook
description: Load the design skills a piece of work needs before grilling or wayfinding, check a finished spec against them with `/playbook check`, and review code against them with `/playbook review`.
argument-hint: "[check <spec> | review <fixed point>]"
disable-model-invocation: true
---

# Playbook

The design skills are rule pools. This skill decides which of them a piece of work runs under, checks that the spec carries what they require, and reviews the code against their rules. The calling workflow (grilling, wayfinder, to-spec, implementation) keeps its own steps; the playbook runs around it.

## Catalog

| Area | Skill | Runtime or engine files, by stack |
|---|---|---|
| Frontend | `frontend-design` | `REACT.md` when the UI runtime is React |
| Backend | `backend-design` | `SERVERLESS.md` when the code runs on serverless or edge functions |
| Database | `database-design` | `POSTGRES.md` for PostgreSQL, `D1.md` for Cloudflare D1 |

The files sit in the skill's own folder.

## Asking the user

Every question this skill asks goes in plain chat text, in the grilling format: numbered, each with your recommended answer, worded so "yes" accepts it. Then wait for the reply. The harness's question tool stays unused here.

## `/playbook`: load

1. **Pick the areas and the stack.** Take what the conversation already states, then what the repo shows (`package.json`, `wrangler.toml` / `wrangler.jsonc`, database config, migrations folder). Whatever is still unknown, ask: which areas, and which catalog row applies for each. "Not decided yet" is a valid answer for a stack; a new product usually picks its stack during grilling.
2. **Write the playbook line** in chat, one line naming every selected skill and file, with undecided stacks marked:
   `Playbook: frontend-design + REACT.md · backend-design + SERVERLESS.md · database-design (engine: pending)`
   When a wayfinder map is in play, add the same line to the map's Notes, so every later session consults the same skills.
3. **Load.** Invoke each selected skill with the Skill tool, then read its CHOICES.md and each selected file now, before the calling workflow asks anything.
4. **Hand back** to the calling workflow.

**Pending stacks:** when grilling settles a stack, read the matching file from the catalog before the next question that touches it, and restate the playbook line with the file filled in.

## `/playbook check`: audit a spec

1. **Find the spec.** In order: the argument (a path or an issue); the spec written in this session. Otherwise ask for it. Read its full text once.
2. **Pick the skills.** Use the playbook line if it is in context; otherwise derive the areas and stack from the spec and ask about anything it leaves open. Write the playbook line.
3. **Dispatch one sub-agent per selected skill, in parallel**, each with a fresh context window. Give each:
   - the spec's path, with the instruction to read it with the Read tool (a shell `cat` truncates a long spec);
   - the instruction to invoke its skill with the Skill tool, then read its selected files from that skill's folder;
   - the paths of the project's ADRs and glossary, when they exist; an ADR overrides the skill;
   - this brief: "Go through the skill's *ready when* list item by item. Mark each item **covered** (quote the spec line), **assumed** (quote the stated assumption), **not applicable** (one-line reason), or **missing**. Then read the rest of the skill and its runtime or engine files, and list every point where the spec contradicts a rule (quote both). Contradictions are limited to decisions your skill owns; a spec line that states another selected skill's default is out of scope. For each missing item and contradiction, give the default the skill or its CHOICES.md recommends, or mark it **decision** when the skill offers alternatives without a default. Every *ready when* item appears in your report. Under 500 words."
4. **Ask.** Turn the reports into one grilling round, grouped by skill: every missing item and contradiction is a numbered question, its recommended answer the sub-agent's default. Items marked **decision** carry your recommendation and the alternatives.
5. **Write the answers into the spec**, where it lives (file or tracker issue), under Implementation Decisions. An answer that deviates from a skill default also gets an ADR. Accepted assumptions are written as assumptions.

The check is done when every *ready when* item of every selected skill is covered, assumed, or not applicable in the spec, and no contradiction is left unanswered.

## `/playbook review`: review code

1. **Pin the fixed point.** Take it from the argument (a commit, branch or tag); otherwise ask. Capture `git diff <fixed-point>...HEAD` and `git log <fixed-point>..HEAD --oneline`, and confirm the diff is non-empty before going further.
2. **Pick the skills from the diff.** An area is selected when the diff touches its code: frontend for components, routes, client state and data fetching; backend for handlers, queue consumers, integrations and webhooks; database for schema, migrations, queries and data access. Take the stack from the playbook line if it is in context, otherwise from the repo. Write the playbook line.
3. **Dispatch one sub-agent per selected skill, in parallel**, each with a fresh context window. Give each:
   - the diff command and commit list;
   - the instruction to invoke its skill with the Skill tool, then read its selected files from that skill's folder;
   - the paths of the project's ADRs and `CODING_STANDARDS.md` / `CONTRIBUTING.md`, when they exist;
   - this brief: "Check every hunk in your area against every section of the skill and its runtime or engine files that the hunk touches. Report each violation with the rule (section and quote) and the hunk (file and quote), marked **hard** or **judgement**. A project ADR or coding standard overrides the skill. Skip what tooling already enforces. Under 400 words."
4. **Report** the findings grouped by skill, then one line naming every rule violated, so the user can decide which belong in the project's `CODING_STANDARDS.md`. Fix findings the user approves.

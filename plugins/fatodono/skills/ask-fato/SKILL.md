---
name: ask-fato
description: Ask which fatodono skill fits your situation. A router over every fatodono kit and skill.
disable-model-invocation: true
---

# Ask Fato

You don't remember every fatodono skill, so ask.

Before you say what a skill does or recommend skipping one of its steps, read its `SKILL.md`. The summaries here are only for orientation.

Route by the user's **situation**, not by kit. A **kit** is only the plugin a skill ships in; it matters once the skill turns out not to be installed (see the end).

## The launch flow: working app → store

The route an app takes from "it works" to "it's in the stores".

1. **`legals`** writes the legal documents the app needs (privacy policy, terms of service, subscription terms, refund policy, account deletion page, and region-specific ones such as the Turkish distance sales contract) and works out which of them this app actually needs. It reads the facts from the code and asks only what the code can't show (company name, support address, refund rules), so the later it runs, the fewer questions it asks. Drafts, not legal advice. It's model-invoked: the user can just say "write the legal documents for my app".

## After launch

- **The app changed** (a new SDK, a new country, a new paid plan) → **`legals`** again. It finds the documents the app already has, in the repo or on its site, and updates them instead of starting over.

## Skills and kits

| Skill    | Kit                  |
| -------- | -------------------- |
| `legals` | `fatodono-founderkit` |

## When the right skill is not installed

Each kit is its own plugin, so the user may have installed only some of them. A skill that isn't installed has no `SKILL.md` to read: say only what its summary here says, tell the user that, and give them the install command for its kit:

```bash
claude plugin install <kit>@fatodono
```

In an agent other than Claude Code, they install the single skill instead:

```bash
npx skills@latest add itsfatodono/skills --skill=<skill>
```

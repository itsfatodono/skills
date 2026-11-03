---
name: ask-fato
description: Ask which fatodono skill fits your situation. A router over every fatodono kit and skill.
disable-model-invocation: true
---

# Ask Fato

Map the user's situation to the fatodono skill that fits, then say how to run it.

Before you say what a skill does, read its `SKILL.md`. The summaries below are only for orientation.

## Kits

### fatodono-launchkit

Skills for releasing an app to the stores.

No skills yet.

## When the right skill is not installed

Each kit is its own plugin, so the user may have installed only some of them. If the skill that fits belongs to a kit they don't have, give them the install command for that kit:

```bash
claude plugin install <kit>@fatodono
```

In an agent other than Claude Code, they install the single skill instead:

```bash
npx skills@latest add itsfatodono/skills --skill=<skill>
```

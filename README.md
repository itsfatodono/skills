# Fatodono Skills

## The Mindset

The skills here were designed so that models do this work at maximum efficiency and more reliably. These are the things every plugin has tried to do toward this goal:

- Keep the context window as small as possible.
- Have agents do one job at a time. (In fact, if an agent knows what its next job will be, it skimps on the job in front of it, which means every job except the last. Prevent this too.)
- Force agents to work as deterministically as possible.
- Push complexity down into the depths of `deep modules` and present a clean interface.
- Learn from real-world samples. These skills were NOT written by asking a model to "write me a skill for X".

## Installation

Pick one per agent, because installing both gives you every skill twice.

<details>
<summary><b>Claude Code plugin</b>: auto-update</summary>

```bash
claude plugin marketplace add itsfatodono/skills
claude plugin install fatodono-founderkit@fatodono
```

Every kit installs the `fatodono` router with it.

**Updates:** automatic once you enable auto-update for this marketplace (`/plugin` → Marketplaces → `fatodono` → Enable auto-update). Claude Code leaves it off by default for third-party marketplaces. To update by hand, run `claude plugin marketplace update fatodono`.

</details>

<details>
<summary><b>Codex plugin</b>: auto-update</summary>

```bash
codex plugin marketplace add itsfatodono/skills
codex plugin add fatodono-founderkit@fatodono
codex plugin add fatodono@fatodono
```

Codex doesn't install plugin dependencies, so the last line installs the `fatodono` router. The kits work without it; you only lose `ask-fato`.

**Updates:** automatic. Codex refreshes Git marketplaces and the plugins you installed from them on its own. To update by hand, run `codex plugin marketplace upgrade fatodono`.

</details>

<details>
<summary><b>Any agent</b> (skills.sh): manual-update</summary>

```bash
npx skills add itsfatodono/skills
```

Pick the skills, agents and scope when it asks. The files are copied into your project and you can edit them.

**Updates:** manual. Run `npx skills update`. The router doesn't come along on its own; pick `ask-fato` too if you want it. There are no kits here; you get standalone skills.

</details>

## The Skillset

### founderkit

Skills for the work around your app that isn't code.

#### [/legals](plugins/fatodono-founderkit/skills/legals)

Writes your app's legal documents from your own code: privacy policy, terms of service, subscription terms, refund policy, account deletion page, and the documents your users' countries require, such as the KVKK texts for Turkey. [details](plugins/fatodono-founderkit/skills/legals/README.md#what-it-writes-today)

- **Simple to use.** Just say what you want; you don't need to learn the skills. [examples](plugins/fatodono-founderkit/skills/legals/README.md#run-it)
- **Distilled from 360+ different real companies' documents.** For each document we read 25 to 30 real ones and learned which sections companies include and how they write them.
- **Your code is the source of truth.** It reads your repo first (the data you collect, your SDKs, sign-in, payments) and asks only what the code can't show, each question with a recommended answer.
- **You can trace every promise.** `legal/facts.md` lists each fact the documents rely on and where it came from: a file in your code or one of your answers.
- **Laws are add-ons.** Every document has a global part, and the EU, TR, UK and US parts are added only when you have users there.
- **It can build the document you need.** If you ask for one it has no skeleton for, it builds one the same way: it reads 10 documents from apps in your field and learns their common sections. That takes 11 agents and a good part of your usage limit, so it asks before it starts.

14 of the 72 planned items are ready. The documents are drafts, so have a lawyer read them before you publish.

### fatodono

The router. Every kit installs it, and it covers all of them.

#### [/ask-fato](plugins/fatodono/skills/ask-fato/SKILL.md)

Ask it anything about the fatodono skills `/ask-fato`: which one fits your situation, how to use one, or whether you can skip one of its steps. It knows the skills you haven't installed, too.

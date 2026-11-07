# brand-naming

Names your app, company, product or feature, or judges the names you already have. It follows
the process professional naming researchers have described in public interviews and talks: a
strategy brief first, hundreds of candidates from separate passes, sound chosen on purpose, and
screening down to 3-5 finalists.

**Screening is a pre-screen, not trademark clearance.** Have a trademark attorney check the name
you pick before you commit to it.

## How to use

### Install

Pick one per agent, because installing both gives you the skill twice.

<details>
<summary><b>Claude Code plugin</b>: auto-update</summary>

```bash
claude plugin marketplace add itsfatodono/skills
claude plugin install fatodono-founderkit@fatodono
```

**Updates:** automatic once you enable auto-update for this marketplace (`/plugin` → Marketplaces → `fatodono` → Enable auto-update). To update by hand, run `claude plugin marketplace update fatodono`.

</details>

<details>
<summary><b>Codex plugin</b>: auto-update</summary>

```bash
codex plugin marketplace add itsfatodono/skills
codex plugin add fatodono-founderkit@fatodono
```

**Updates:** automatic. Codex refreshes Git marketplaces and the plugins you installed from them on its own. To update by hand, run `codex plugin marketplace upgrade fatodono`.

</details>

<details>
<summary><b>Any agent</b> (skills.sh): manual-update</summary>

```bash
npx skills add itsfatodono/skills --skill brand-naming
```

**Updates:** manual. Run `npx skills update`. The router doesn't come along on its own; add `--skill ask-fato` if you want it.

</details>

The morpheme matrix step runs `scripts/combine.py`, so it needs Python 3 (standard library only).

### Run it

Ask in your own words:

- "We still call this app SyncFlash. Find it a real name."
- "Need a name for our new export feature."
- "Is Tambora a good name for a drum-learning app?"
- "Here are my five candidates, score them and pick one."

### Modes

| Mode | When | You get |
|---|---|---|
| **Full** | A company, product line, or anything you'll live with for years | Brief, 400+ candidates, screening, 3-5 finalists |
| **Fast** | An internal tool, a feature, a side project | Short brief, 100+ candidates, 5-8 finalists |
| **Evaluate** | You already have candidates | A scored critique and fixes, no new names unless you ask |

Each finalist comes shown in use (a headline, an app icon label, next to two real competitors),
with why it sounds the way it does, where it came from in the candidate pool, and its risks. Every
trademark or domain conflict is marked verified or unverified, and the candidate list is kept in a
file so you can go back to it when a finalist doesn't clear.

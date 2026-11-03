# Ship each kit as one plugin, and keep dev material out of the plugin folders

## Context

Claude Code enables and disables plugins only as a whole. `skillOverrides` doesn't apply to plugin skills, so users can't turn off a single skill inside a plugin. skills.sh, by contrast, lets users pick individual skills.

Some skills need far more material to develop than to run. The legals skill is built from a corpus of collected legal documents, while users only need the skeletons distilled from that corpus.

## Decision

- **One plugin per kit** (`fatodono-launchkit`, later `fatodono-devkit`), as in mattpocock/skills. Users who want individual skills use skills.sh. We considered one plugin per skill plus bundle plugins, and rejected it because it costs a manifest and a version per skill for a choice that skills.sh already offers.
- **A separate router plugin, `fatodono`,** that every kit depends on. The router comes with whichever kit a user installs, and one `ask-fato` can map every kit.
- **`plugins/` and `workshop/` in one repo.** Each marketplace entry's source is `./plugins/<plugin>`, so only that folder is copied into a user's plugin cache. Contributors still get the whole pipeline in one place.
- **Plugin names start with `fatodono-`.** Names in `claude-plugins-official` are global, and a bare `launchkit` would likely collide there.

## Consequences

- The Claude Code marketplace clone and the skills.sh temporary clone both download `workshop/`. Neither puts it in the agent's context.
- Raw third-party material in `workshop/` (for example, legal samples) must stay out of git. Commit only what we derived from it, plus the source URLs.
- Auto-update is off by default for a self-hosted marketplace, and `marketplace.json` has no field to change that. Users turn it on once. It would be on by default only after a listing in `claude-plugins-official`.

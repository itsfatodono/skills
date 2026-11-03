## Layout

- `plugins/` holds only what ships to users. A marketplace entry's source is its plugin folder, so nothing outside it reaches a user's machine.
- `workshop/` holds what is needed only to develop a skill: research, tools, tests, fixtures.
- `fatodono` is the router plugin. Every other plugin depends on it. Its skill `ask-fato` names every skill, so update it whenever you add, rename or remove a skill.

[ADR 0001](./.agents/adr/0001-kits-as-plugins.md) records why.

## Checks

Run `npm run check` and `claude plugin validate . --strict` after touching `plugins/` or `.claude-plugin/`.

## Releases

Plugins are versioned with changesets. Before merging a change to `plugins/<plugin>/`, run `npx changeset` and write one line about the change in the user's terms. Contributors don't write changesets. Never edit `version` in `plugin.json` by hand.

# Skill-wide work

Work that belongs to no single item. Item work is in the item's own file ([README.md](README.md)).

## Move into the new repo

- [x] Move the plugin into `plugins/fatodono-founderkit/` and rename the skill from `founders-legals` to `legals`. Update `ask-fato`.
- [x] Decide what happens to this folder's own git history (87 commits): kept only in the old repo (`legal-docs`).
- [ ] Shipped files cite `PLAN.md`, which users never get: `regions/tr/tr-distance-sales.md`, `tr-pre-contract-info.md`, `tr-kvkk-notice.md` (decision 47), `regions/eu/ropa.md`, `regions/uk/ropa.md` (decision 37), and `regions/eu/region.md`, `regions/de/region.md` (seed catalog numbers, now in `plans/README.md`). Say the rule itself instead of citing it.

## Contributions

- [ ] `tools/check-contribution`: enforce `CONTRIBUTING.md` *What a pull request may change* and *Never* on a diff (one document or one region; new files plus appended lines only; no method files, no `plans/`). It also runs `tools/check-facts`.
- [ ] The CI job that runs it on contribution pull requests.
- [ ] Rehearse a contribution: add `br` from a fork as an outsider would. The check must pass and nothing outside `regions/br/` may change.

## Quality

- [ ] Spot-check a few skeletons per family.
- [ ] Run the skill on a different app (web sales or user-generated content). Re-runs, patch mode, subscription and refund are not tested yet. Not noteable: the owner ruled it out on 2026-10-27.
- [ ] Prune: remove sentences that change no behaviour and repeated meanings.
- [ ] Need-to-know: rerun the write branch on syncflash's first `facts.md` (commit `05e0aa1`) and run `tools/check-overshare` with `overshare-generic.txt` and `tests/local/syncflash.txt`. The first run hit 42 rules; the target is 0.
- [ ] Once the first form is built, check that the description fires for store forms. If not, consider splitting that branch out.

## Upkeep

- [ ] Refresh: a scheduled agent re-runs the builder every 3 months; review the skeleton diffs before release.

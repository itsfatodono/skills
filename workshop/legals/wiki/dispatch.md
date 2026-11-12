# Dispatch

- 2026-10-27: the owner asked that every subagent in this session use the **Anthropic** provider,
  because several providers are configured and they should not be mixed. Model IDs used:
  - build agents, `sample-extractor`, helpers: `anthropic/claude-opus-5-5#medium`
  - `pool-collector`: `anthropic/claude-sonnet-5-5#medium`
  This applies PLAN.md decision 25 (Opus medium, Sonnet medium for the collector) to this harness.
- 2026-10-27: heavy build runs in parallel are capped at about 3. Decision 25 records that a
  parallel high-effort run used up the usage window on 2026-10-26.
- 2026-10-27: parallel agents are told not to edit `PLAN.md` and not to commit. The chief of staff
  folds results into `PLAN.md` and commits after each one, so every run's diff stays separate.

- 2026-10-27 (`44096aa`): every dispatch that edits skeletons, region blocks or facts files tells the
  agent to run `tools/check-facts`, which must exit 0 before it reports back.

- 2026-10-27, cookie-policy build (`8169dcd`…`0cc1ed2`): the two dispatch patterns that worked (one
  merge helper resumed through the build, extractors given the candidate id) were added to PLAN.md
  decision 25 at the owner's request. **Build method goes in PLAN.md decisions, not in the wiki.**
  The wiki keeps only harness notes and a pointer.
  - Code Mode (`execute`) has neither `subagent` nor `edit`. Dispatch and edit with direct tool calls.
  - In OpenCode, resuming a helper means passing its `sessionID` to the subagent tool.
- 2026-10-27: before writing a method rule into `build.md`, grep the existing skeletons for what it
  touches. Decision 44's first draft contradicted the ToS/EULA closing-clauses section.

See also [runs.md](runs.md).

- 2026-10-27: **commit only the finished run's paths, never `git add -A` while other runs write files.** The chief of staff's
  `git add -A` commits (`91d0893`, `57bcc1b`) pulled in the ÖBF skeleton writer's unfinished skeleton, catalog row,
  `facts.md` key and part of `merge.md`. Nothing was lost, but those commits no longer map to one run. Use
  `git add <research/...> <skill files the run named>`.

- 2026-10-27 (second session): **a subagent session can be resumed only by the session that started it.** Resuming
  `ses_e838afdb…` and `ses_e83912e2…` from a new chief-of-staff session failed with "is not a child of the current session".
  So a "Resume here" note must never depend on resuming a helper. Hand off through files (merge.md, candidates.md, pool slices)
  and start a fresh helper with pointers to them. A collector that has not written its slice yet loses its work at session end,
  so collectors should write their file early.

- 2026-11-12: in a build, collectors, extractors and the merge helper each run as their own agent; the build agent only dispatches.
- 2026-11-12: in Claude Code a subagent can start subagents.

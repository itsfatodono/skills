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

- 2026-10-27: **subagents in this harness cannot start subagents.** The RoPA `eu` run reported
  having no tool for it, so it collected and extracted itself. This means a build agent's
  context also holds every sample. Decision 25's nesting (build agent → collector and extractors)
  works only when the chief of staff dispatches the collector and extractors directly. Open:
  either flatten the dispatch (the chief of staff runs the pool and extraction steps) or note in
  `build.md` what a builder does without a subagent tool.
- 2026-10-27: the OpenCode config (`~/.config/opencode/opencode.json`) has no setting that
  disables nested subagents, so this is the harness default. Claude Code has the same limit, so
  the plugin's build method must assume two levels as well. The direction the owner was told
  about, not yet decided: the main agent runs the build (pool, saturation, merge), and workers
  only collect one slice or extract one sample.

- 2026-10-27: **the owner decided not to write this as a rule.** In this session the chief of staff
  acts as the builder's dispatcher: it starts `pool-collector`s (Sonnet) and `sample-extractor`s
  (Opus) directly, judges saturation from their short replies, and hands only the merge or
  skeleton writing to one helper. As of `d10bc73`, `build.md` step 1 already says the build branch
  dispatches the collectors, so it fits a main-agent builder. The nesting assumption sat only
  in how the 2026-10-26/27 runs were dispatched (one agent per whole build).

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

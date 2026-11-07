# Owner preferences

- 2026-10-27: writes to the chief of staff in Turkish; files stay in English.
- 2026-10-27: wants independent work run in parallel when possible.
- 2026-10-27: wants a checkpoint commit before parallel runs, and a wiki at `wiki/` inside the
  repo (outside `plugin/`, so it never ships).
- 2026-10-27: **tell the owner before starting any new work** (a new agent or task). Follow-ups
  inside an already agreed task count as new work too: the owner said this right after the extra
  `longtail-2` collector was launched without asking.
- 2026-10-26 (from Claude Code memory `~/.claude/projects/-Users-fth-Projects-legal-docs/memory/confirm-agent-fanout.md`,
  which OpenCode does not load): before a parallel run, state the agent count (including extractors
  and collectors), the effort and a rough cost, and offer a cheaper sequential or medium option. "Let's
  finish X" is not consent to a large parallel run. Raised after 4 Opus-high builders used up the
  usage window.
- 2026-10-27: method and dispatch rules belong in PLAN.md decisions. The wiki holds tribal knowledge
  and points to them.
- From AGENTS.md: wants measured pushback, not agreement by default.
- 2026-10-27: during a build the owner wants no new process changes ("no innovations, continue").
  The proposal to save raw text to a gitignored `raw/` and log invalid samples in `invalid.md` was declined for now.
  Bring such proposals up between builds, not in the middle of one.
- 2026-10-27: "when cookie finishes, let's stop before moving to a new one." After the cookie-policy skeleton
  is done and reported, do not start the next document (or any new work) without the owner's go-ahead.
- 2026-10-27 (supersedes the "tell before any new work" rule for this batch): "continue the sub-tasks yourself without asking me,
  do not move to a new document type." Within the KVKK and commerce batch (decision 45: 11, 12, 13, 40, 8), the chief of staff runs every
  step without asking, including selection, extraction, merge, skeleton and the judgement calls. It reports results and does not start any item outside the batch.
- 2026-10-27: "I don't care that much about the DSARs. What we have is enough, don't search for new material." For `data-subject-request` (root and `tr`), no new
  collection or extra saturation batches. The skeleton is written from the samples already extracted (root s01–s20, `tr` s01–s15), with `saturated: false` if needed.

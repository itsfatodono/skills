# Checks

`store-shots check` (and the `check` stage of `build`) runs every rule below and prints the first
problem; `.store-shots/logs/check.log` lists all of them as `<source>: <file>: <message>`. Each
problem is fixed in the stage that owns its file, never in an output.

The limits live in the engine beside their source: slot sizes, panel maximums and the feature
graphic size in `engine/store_shots/catalog.py`. A problem names the limit it broke.

The catalog holds the stores' rules as its `SOURCES` read on its `CHECKED` date. A store that
rejects an image `check` passed, or asks for a size or device it does not list, means the catalog
is out of date. Open both `SOURCES` pages, tell the owner what differs, and file it at
https://github.com/itsfatodono/skills/issues: the fix is an update of this skill, never a change in
the project.

| Source | Checks | Fix in |
|---|---|---|
| `catalog` | each target's size is one its slot takes; at most the slot's panel count; every slot a store requires for `runs_on` has a target; the feature graphic is the size Play takes | config (`targets`, `runs_on`) |
| `storyboard` | each panel has `evidence`, and every file an entry names exists | storyboard |
| `image` | each image the targets need and each unframed image exists, is a PNG at its exact size, has no alpha and an sRGB profile, and its recorded copy holds no banned phrase and, on the App Store, no other platform's name (an unframed image records none) | compose (rebuild), copy (the text) |
| `copy` | every `feature_graphic` key the feature page shows, in each Play language | copy |

Rules that surprise:

- Other platforms' names (Android, Windows, Google Play, Play Store, Samsung, S Pen, and the rest
  in `checks.OTHER_PLATFORMS`) match as whole, case-sensitive words. They count in App Store
  images' recorded copy, including a per-store `app_store:` panel variant. "Play" alone passes.
- A banned phrase is checked only in the languages its entry lists; a new language needs its own
  patterns.
- An App Store image that records no copy fails, because its text cannot be checked; images the
  tool composes always record it.

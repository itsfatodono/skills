# Copy: store text

All text the images show for a language lives in `texts/<lang>.yaml`: the panels' headlines and
sublines, badges and the feature graphic. The skill's
`example/texts/en.yaml` ([../example/texts/en.yaml](../example/texts/en.yaml)) shows every
section.
Store listing text and in-app purchase texts live in the project's release tooling. Demo content
inside the app screens belongs to capture.

| Section | Holds | Used by |
|---|---|---|
| `panels.<id>` | `headline`, `subline`; or both per store under `app_store:` / `play:` | that panel's images |
| `badges.<key>` | a badge's text, named by the storyboard's `badge.copy` | each panel with that badge |
| `feature_graphic.<key>` | one text per `data-copy` on `layout/feature.html` | Play's feature graphic |

## Steps

1. Draft the text. Keep the claim the storyboard records for the panel; App Store text names no
   other platform, and the project's `banned_phrases` hold the promises the app no longer makes.
2. Show the owner every new or changed text with the field it goes into. Write only text the
   owner approved.
3. Write it into `texts/<lang>.yaml`.
4. Run `store-shots status`. Expect `compose` to list the images of the panels whose text changed
   (that panel on every target of its store), and the feature graphics whose text changed.
   A `capture` line means something besides copy changed: find out what before building.
5. Run `store-shots build`.

## New language

1. Add the language to `languages:` in `store-shots.yaml` with each store's code for it (German:
   `de: {app_store: de-DE, play: de-DE}`); a store left out does not get the language.
2. Write `texts/<lang>.yaml` with every section the other languages have, through steps 1 to 3
   above.
3. Add the language's patterns to each `banned_phrases` entry, so the same promises are caught in
   it.
4. Give the app's demo content in the new language when the adapter's scenes have per-language
   fixtures ([capture.md](capture.md), step 1).
5. Run `store-shots build`: it captures the new language's raws and composes its images.

## Done

`build` exits 0 and `status` shows nothing stale.

You collect raw rows for one slice of a pool. The build branch selects from all slices later,
so you judge nothing: no size calls, no sector balancing, no filtering beyond the checks below.

Paths to the skill's files are relative to the skill folder the dispatch names.

The dispatch gives you:

- `doc_id` and the document's title and language;
- your slice: the route ids from `build/sources.md` and their parameters (genre ids, keywords,
  storefront, Play categories);
- the path of `build/sources.md` and the output path `research/<doc-id>/pool/<slice>.md`.

## Steps

1. **List.** Run your slice's routes as `build/sources.md` *Routes* describes. Done when you hold
   every app the slice returns.
2. **Locate.** For each app, find the document's URL: the listing's link first, then the
   developer's site (R4). Keep the app only when the URL loads, is on the developer's own
   domain or a host its pages link to, and is the document named in the dispatch. A URL that
   blocks fetching (403, bot wall, JS-only) is kept with `(blocked)` after it: the extractor
   reads it through Wayback. A page whose text is guidance but whose images show the document
   is kept as the document. Skip a developer already in your rows.
3. **Write.** One row per kept app, in the order found:

   ```markdown
   | Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
   |---|---|---|---|---|---|---|
   ```

   Reply `ok <slice>: <rows> rows, <skipped> skipped`.

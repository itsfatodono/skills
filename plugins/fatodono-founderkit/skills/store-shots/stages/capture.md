# Capture: raw app screens

Capture turns app screens into raws, `raw/<target>/<lang>/<target>-<scene>.png`, through the
project's adapter. The contract, the gates and how to choose a capture tool are in
[../docs/adapter.md](../docs/adapter.md).

Every raw records the hash of the adapter's declared inputs, app code included, so a changed app
screen makes exactly the raws that depend on it stale, and `build` captures those alone.

## Steps

1. Make the change in the app, a scene, or the demo content. Teach the adapter each new scene,
   and after any change to the adapter itself run `store-shots adapter test` until it shows no
   `FAILED` line. Demo content (the notes, recordings and language-specific text shown inside the
   app) lives in the adapter's fixtures; a fixture glob with `{lang}` or `{scene}` in the
   adapter's `inputs` makes only that language's or scene's raws stale.
2. Run `store-shots status`. Its `capture` lines name each stale raw and why; its `compose` lines
   show the images waiting on them.
3. Run `store-shots build`. On a `capture: FAILED` line, read
   `.store-shots/logs/capture-<target>.log`.
4. A cut-off text in the adapter's report fails the capture. Show the owner the report line; the
   owner picks the fix: a shorter text in the app's translation, another scene, or a change to the
   app's layout. A line the owner accepts goes, exactly as written, into the config's
   `adapter.accepted`.

`store-shots capture --force` is for a change the adapter's inputs cannot show (a new simulator
runtime, a new emulator image); narrow it with `--target` and `--scene`.

## Done

`store-shots adapter test` shows no `FAILED` line, the `capture` line says `ok`, and `status`
lists no stale raw.

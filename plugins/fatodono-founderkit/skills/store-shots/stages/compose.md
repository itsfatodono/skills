# Compose: framed store images

Compose renders each target, language and panel into `out/<store>/<code>/<target>-<panel>.png`
and, when the config has `feature_graphic`, Play's feature graphic per Play language into
`out/play/<code>/feature-graphic.png`. Each unframed image in the config is its raw, saved opaque
and sRGB into `out/unframed/<name>.png`. Each image records the hashes of its raws, copy, placement,
layout and mockup files, and the copy it shows. `build` composes the stale images, runs the checks
and refreshes one contact sheet per store and language.

## Steps

1. Run `store-shots build`.
2. On `compose: FAILED`, the line names the panel and what it lacks (a copy key, a device's
   `--screen-w`, a cluster for a store); fix it in the stage that owns it.
   `.store-shots/logs/compose.log` holds the rest.
3. On `check: FAILED`, the line names the first problem and `.store-shots/logs/check.log` all of
   them, each with its file. [../docs/checks.md](../docs/checks.md) says how to fix each kind.
4. Look at the contact sheet of each store and language you changed,
   `.store-shots/sheets/<store>/<code>.png`. Tiles are labelled `<target> <panel>` (an unframed
   image `unframed <name>`); open the
   full-size image under `out/` only for a tile that looks wrong. `store-shots sheet` refreshes
   the sheets without a build.

## Done

`build` exits 0, and every sheet you looked at shows each panel's text whole and each device in
place.

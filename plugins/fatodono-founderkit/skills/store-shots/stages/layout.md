# Layout: the placement

The project's `layout/` folder holds its look, which [design.md](design.md) makes, and where every
element sits, as data (`placement.yaml`). Layout moves and sizes the elements of a look the owner
has approved; a change to the look itself is design's. The engine draws the device frames and
status bars. The format is in [../docs/layout.md](../docs/layout.md).

## Steps

1. Make the change in `placement.yaml`: a device, card, badge, cluster member or copy block's
   position or size in its entry, under `panels.<id>` when only that panel changes, and under the
   frame's `landscape` entry for a target turned to landscape. A capture
   holds the app only, so a margin, a frame or an offset is always a layout value.
2. Run `store-shots status`. Once the images exist, expect only `compose` to list images: one
   panel's for a `panels.<id>` entry, a frame kind's for its shared entry.
3. Before the raws exist, `store-shots preview --panel <id>` shows the change on placeholder
   screens. Once they exist, run `store-shots build` and look at the contact sheets
   (`.store-shots/sheets/<store>/<code>.png`) for the panels you changed.

## New device

1. Add a target to `store-shots.yaml` ([../docs/config.md](../docs/config.md)): its slot, its
   store image size and, when the raw differs, its screen size.
2. Give it placement: an entry for its frame kind in `placement.yaml` when the kind is new to the
   project, or a target-id entry where it must differ from its kind.
3. Teach the adapter the new device id ([capture.md](capture.md)), then run `store-shots build`.

## Done

`build` exits 0, `status` shows nothing stale, and the contact sheet shows every changed panel as
intended. Before the raws exist: `preview` exits 0 and its sheet shows every changed panel as
intended.

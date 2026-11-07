# Layout: the panel page and placement data

A project's `layout/` folder holds its design, written once: `panel.html`, its stylesheet, badge
icons under `icons/<name>.svg`, and `placement.yaml`. The engine supplies the device frames and
status bars (`engine/store_shots/mockups/`); the layout never draws a device itself.

## Who owns what

- **Mockup (engine):** each frame kind's inside: bezel, radii, camera cutout, status bar (iOS or
  Android, `normal`, `airplane` or `none`), the Mac's title bar and base. Frame kinds: `iphone`,
  `ipad`, `mac`, `android_phone`, `android_tablet`. A cluster member is drawn at the store-listing
  cluster's proportions, a single device at the single-frame ones. A device whose raw is landscape
  lies on its side: the iPhone's Dynamic Island and the Android phone's camera move to the left
  edge, and an iPhone shows no status bar, as iOS does. Mockups hold no text but the clock.
- **Layout (project):** background, typography, the card's and the badge's look, and where every
  element sits.
- **Copy (project):** every text, the badge's included (`badges.<key>` in `texts/<lang>.yaml`).

## The page

The page is plain HTML. The engine adds the mockup stylesheets, the panel's data and the runtime;
the page marks what the runtime fills:

| Attribute | Meaning |
|---|---|
| `data-copy="key"` | takes the copy text `headline`, `subline` or `badge`; removed when the panel has none |
| `data-stop` | a closing `.` `!` or `?` goes in `span.stop` (colour it with `--accent`) |
| `data-fit-lines="N"` | the font shrinks in 0.5 px steps until the text takes at most N lines |
| `data-fit-above` | ...and until it ends 0.8vh above the top of every device under it (a device beside it does not count) |
| `data-stage` | where the devices go (default: `body`) |
| `data-place="name"` | takes `name`'s placement as inline style |
| `data-place="card"` | holds an `img` for the card raw; removed when the panel has no card |
| `data-place="badge"` | holds a `[data-icon]` for the icon; removed when the panel has no badge |

The runtime builds each device as `.ss-device[data-kind][data-place][data-orientation]` in the
stage: `data-place="device"` for a single device, `cluster.<frame>` for each cluster member, back
to front; `data-orientation` is `portrait` or `landscape`, by the device's raw. `body` carries
`data-frame`, `data-panel`, `data-status` and `data-orientation` (the image's).

## placement.yaml

```yaml
iphone:                                   # a frame kind, or a target id
  copy: {top: 7vh}                        # any data-place name: CSS property: value
  device: {--screen-w: 69vw, left: 6vw, top: 25vh}
  card: {left: 27vw, width: 68vw, top: 61vh, border-radius: 4vw}
  badge: {left: 41vw, top: calc(61vh - 6.8vw), font-size: 4vw}
  cluster:
    mac: {--screen-w: 84vw, left: 8vw, top: 23.5vh}
  panels:
    p4:                                   # this panel only
      card: {left: 21vw, width: 74vw, top: 68vh}
  landscape:                              # a target turned to landscape
    copy: {left: 6vw, right: auto, width: 32vw, top: 50vh, transform: translateY(-50%), text-align: left}
    device: {--screen-w: 56vw, left: 41vw, top: 20vh}
    panels:
      p4: {card: {left: 52vw}}
```

- A device's size is its screen width, `--screen-w`; the height follows the raw. Compose fails
  when a shown device has none.
- For one image the entries merge property by property: frame kind, its `panels.<id>`; on a
  target turned to landscape (a phone or tablet target at a landscape size), the frame kind's
  `landscape` entry and its `panels.<id>`; then the target id, its `panels.<id>`. A target entry
  is needed only where that target differs from its frame kind.
- A landscape image is wide, so its `landscape` entry usually puts the copy beside the device
  rather than above it. The example's has one per phone and tablet frame kind.
- Use `vw` / `vh` so one entry serves every size of a frame.
- An image records only its own merged placement, so editing a `panels.<id>` entry re-composes
  that panel alone; editing a frame's shared entry re-composes that frame's panels.

## Storyboard fields the layout serves

A panel's `scene`, `card`, `badge`, `status` and `cluster` decide which places the page gets; see
[storyboard.md](storyboard.md). The size each raw is captured at is in
[adapter.md](adapter.md#the-contract).

## The feature graphic page

A project with `feature_graphic` in its config also holds `layout/feature.html`: Play's feature
graphic, rendered once per Play language at `feature_graphic.size` (Play takes 1024x500) into
`out/play/<code>/feature-graphic.png`. A project without `feature_graphic` gets none.

- Every `data-copy="key"` on the page takes `feature_graphic.<key>` from the copy; each one is
  required. `data-stop` and `data-fit-lines` work as on the panel page; there is no device.
- `body` carries `data-frame="feature"`. Its places come from placement.yaml's `feature_graphic:`
  entry (`<place>: {<css property>: <value>}`, no `panels`).
- A layout file belongs to the page of its own stem: `feature.*` is an input of the feature
  graphics only, `panel.*` of the screenshots only; every other file (a shared stylesheet, fonts,
  icons) is an input of both.

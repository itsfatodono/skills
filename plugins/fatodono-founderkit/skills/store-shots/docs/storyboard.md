# storyboard.yaml

The panels in store order. The storyboard stage writes it; capture reads its scenes, compose its panels.
The skill's `example/storyboard.yaml` ([../example/storyboard.yaml](../example/storyboard.yaml))
holds each kind of panel.

```yaml
panels:
  - id: p2                                      # unique; names the copy entry and the image
    claim: Recognition runs on the device, with no network.
    scene: editor                               # the device's raw
    card: editor-card                           # optional: a second raw, cut to an element
    badge: {icon: airplane-mode, copy: offline} # optional
    status: airplane                            # normal (the default), airplane or none
    evidence:
      - lib/recognition/engine.dart#RecognitionEngine.recognize  # code that makes the claim true
  - id: p3
    claim: The same notes open on every device.
    cluster:                                    # replaces scene and card
      app_store: [{frame: mac, scene: everywhere-mac}, {frame: iphone, scene: everywhere-iphone}]
      play: [{frame: mac, scene: everywhere-mac}, {frame: android_phone, scene: everywhere-android_phone}]
    evidence: [lib/sync/drive_sync.dart]
```

| Field | Meaning |
|---|---|
| `id` | The panel's id: its text is `panels.<id>` in each copy file, its image `<target>-<id>.png`, its placement override `panels.<id>`. |
| `claim` | The one thing the panel tells a store visitor. |
| `scene` | The scene the adapter captures for the device, at the target's screen. |
| `card` | A scene captured as an element (a search result, a menu); it must fit within the screen. The layout places it and draws its margin. |
| `badge` | `icon`: `layout/icons/<icon>.svg`; `copy`: the key of its text under `badges` in each copy file. |
| `status` | The status bar the mockup draws: `normal`, `airplane` for an offline claim, or `none` for a full-screen app or game that hides it. The app is never put in airplane mode for it. |
| `cluster` | Per store, the devices the panel shows, back to front, each a frame kind (`iphone`, `ipad`, `mac`, `android_phone`, `android_tablet`) and its own scene, sized as [adapter.md](adapter.md#the-contract) says. Every store the project makes images for needs an entry, so the App Store shows no Android device. |
| `evidence` | The code that makes the claim true, one entry per place: a file path relative to the project folder (`..` allowed), optionally followed by `#` and a symbol in it (`lib/sync/drive_sync.dart#DriveSync.pull`). `check` fails a panel without evidence and an entry whose file does not exist; the symbol is for the reader. It is how a later app change can be checked against the claims. |

Scene names are exact names the adapter knows, never prefixes. A scene used by several panels is
captured once. No image shows `claim` or `evidence`, so editing them re-composes nothing.

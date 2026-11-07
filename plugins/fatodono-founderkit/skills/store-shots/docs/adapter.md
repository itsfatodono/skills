# Adapters

An adapter is the project's own program that turns app screens into raw captures. It can be written
in any language and use any capture tool. The engine knows nothing about the app. It hands the
adapter a request, runs it and judges only what it wrote. Two adapters that pass the same gates
give the engine the same thing, whatever they do inside.

## The contract

### What the adapter gets

The config names the command and the files whose change makes the captures stale:

```yaml
adapter:
  command: [uv, run, --quiet, --script, adapter/adapter.py]   # a list; a string is split POSIX-style
  inputs: [adapter/**, ../app/src/**, ../app/package-lock.json]
  textless: []                          # scenes that show no text at all
  accepted: []                          # report lines the owner accepted, exactly
```

Write `command` as a list: it then runs the same on Windows, macOS and Linux, with no shell in
between. `init` writes a starter `adapter/adapter.py` that uv runs, and any program on the `PATH`
works as well (`[node, adapter/capture.mjs]`, `[xcrun, …]`, `[./gradlew, …]`).

A change to any file `inputs` matches makes every raw stale. `{scene}` and `{lang}` in a glob stand
for the raw's own scene and language, so `'fixtures/{lang}/**'` makes only that language's raws
stale (quote such a glob inside a `[...]` list). Files the tool writes never count: `raw/`, `out/`
and `.store-shots/`.

The engine runs the command from the project folder:

```sh
<command> --device <target> --langs en,tr --scenes home,home-card --out <dir> --request <file>
```

- `--device` is a target id from `targets:`. The adapter maps it to a simulator, emulator,
  browser viewport or window, boots what it needs and shuts down what it booted.
- `--langs` are the project's language codes, used as folder names.
- `--scenes` are exact scene names, never prefixes. An empty value asks for no scene.
- `--out` is a fresh, empty folder. The adapter writes there and nowhere else.
- `--request` is a JSON file holding everything the adapter needs to know, so it never reads the
  project's own files:

```json
{
  "contract": 1,
  "target": {"id": "iphone69", "store": "app_store", "device": "iphone", "frame": "iphone",
             "screen": [1320, 2868]},
  "langs": {"en": "en-US", "tr": "tr"},
  "scenes": {
    "home":           {"role": "screen", "size": [1320, 2868]},
    "home-card":      {"role": "card", "max_size": [1320, 2868]},
    "everywhere-mac": {"role": "member", "frame": "mac", "shape": [2560, 1600]},
    "__probe_fullbleed":  {"role": "screen", "size": [1320, 2868], "probe": "fullbleed", "fill": "#FF00FF"},
    "__probe_truncation": {"role": "screen", "size": [1320, 2868], "probe": "truncation", "text": "…"}
  },
  "out": "/abs/path/to/out",
  "report": "/abs/path/to/out/report.txt"
}
```

`langs` maps each language to its code in the target's store, which is the locale to run the app
in. The probes appear only in `adapter test`.

### What the adapter writes

- `<out>/<lang>/<target>-<scene>.png`, for every language and scene: the app's pixels only. There
  is no status bar, navigation bar or home indicator (the mockup draws the status bar), and no
  margin. Each raw's size depends on its scene's `role`:
  - `screen`: exactly `size`.
  - `card`: one element or a group of elements, cut at their own bounds with no padding, within
    `max_size`.
  - `member`: a cluster device's screen, at any resolution. With `shape`, its aspect ratio is
    within 1% of it. With `orientation` instead, it only has to be landscape or portrait. The
    mockup draws the device at the raw's own shape. A member is landscape on a target turned to
    landscape, and a Mac always is.
- `<out>/report.txt`, UTF-8, one line per fact:
  - `checked <lang>/<target>-<scene>.png texts=<n>` for every raw: the adapter looked at the `n`
    texts on it for cut-off text.
  - `<lang>/<target>-<scene>.png: <problem>` for each problem: a cut-off text, a scene the
    adapter does not have, an error the app threw.

A cut-off text is a label showing fewer lines or characters than its text has: an ellipsis,
clipping, or a line past its maximum. Every adapter checks for these, because a truncated
translation in a store image is the failure nobody notices in review.

### What fails a run

The capture fails, and no raw changes, when:

- the command exits non-zero;
- `report.txt` is missing, or holds a problem line not listed in `accepted`;
- a raw is missing, is not a PNG, or is the wrong size for its role;
- a raw has no `checked` line, or its line says `texts=0` and its scene is not in `textless`;
- `--out` holds any other file;
- a scene not in `textless` is the same image in every language, which means the app's locale was
  not set.

The console line names the first problem. The full list and the command's own output go to
`.store-shots/logs/capture-<target>.log`. On success the raws are merged over
`raw/<target>/<lang>/`, so scenes left out of the run keep their raws.

## Building an adapter, gate by gate

`store-shots adapter test` holds the adapter to the contract in eight small gates, in order. Each
gate is its own run of the adapter, and a target stops at its first failure, with a line saying
what the gate expected. The test writes no raw, and its log is
`.store-shots/logs/adapter-test-<target>.log`. Build the adapter in this order, running the test
after each step:

| Gate | It asks for | To pass it |
|---|---|---|
| `runs` | no scene | Parse the arguments, read the request, write an empty `report.txt`, exit 0. |
| `unknown-scene` | `__no_such_scene` | Exit non-zero, or report `<lang>/<target>-__no_such_scene.png: …`. |
| `full-bleed` | `__probe_fullbleed` | Show a screen of only `fill`, edge to edge, capture it at `size` and report it `checked … texts=0`. Any pixel that is not the fill is a status bar, an inset, a letterbox or a scale error, and the gate says where. |
| `cut-off-text` | `__probe_truncation` | Show `text` in one line in a box narrower than the text, capture it, and report both its `checked` line (`texts=` at least 1) and a problem line saying it is cut off. This proves the cut-off check works. |
| `one-scene` | the first scene, first language | Teach the adapter the scene, with demo content. |
| `languages` | the first scene, every language | Run the app in each language's locale. |
| `every-scene` | every scene, every language | Cards cut at element bounds, cluster members at their frame's shape. |
| `repeatable` | the last run, again | The same pixels twice: a fixed clock, no animation or cursor blink, fixed demo data. |

The gates after `cut-off-text` skip until the storyboard names scenes, `languages` skips for a
store with one language, and `every-scene` for a target with one scene. A skipped gate is not a
failure: the test passes when it shows no `FAILED` line.

The probes are scenes like any other, shown through the same capture path the real scenes use.
Their screens live in test-only code kept out of the release build: a debug route, a launch
argument, a test harness widget, a static page.

The gates prove the adapter keeps the contract. They cannot prove that a scene shows the right
screen or believable demo content. That is the owner's call, on the contact sheets in review.

## Choosing the capture tool

Pick the tool from the app's own stack and the machine it runs on; the gates judge the result,
whatever the tool. What the gates cannot see is whether the raw looks like the app on a device, so
hold the choice to these:

- **The platform's real text rendering.** Capture where the app's fonts and text layout are the
  ones users get: a simulator, an emulator, a device or the browser. A renderer that runs without
  one can wrap text differently, and every gate still passes. When the adapter uses one, compare a
  raw with a device screenshot once, with the owner.
- **Cut-off text from the layout engine, not from pixels.** Each UI toolkit knows when a text
  was ellipsized, clipped or ran past its line limit. Read that for every text inside the capture.
- **Screens from demo data.** Drive each scene from fixtures the adapter controls, never from a
  live backend or the developer's own account.
- **App pixels only, by hiding system UI.** Hide the status bar, navigation bar and home
  indicator in the app rather than cropping by a guessed height; `full-bleed` checks the result.

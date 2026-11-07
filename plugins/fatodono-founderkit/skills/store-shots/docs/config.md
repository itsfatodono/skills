# store-shots.yaml

The project's one config file. Paths in it are relative to it. The skill's
`example/store-shots.yaml` ([../example/store-shots.yaml](../example/store-shots.yaml)) uses
every key; `languages`, `targets` and `adapter` are required, the rest optional.

## languages

```yaml
languages:
  en: {app_store: en-US, play: en-US}
  de: {app_store: de-DE, play: de-DE}
```

The key is the copy language (`texts/<key>.yaml`, the adapter's `--langs`, `raw/<target>/<key>/`).
Each value maps a store to its own language code (the `out/<store>/<code>/` folder name). The
stores a language lists are the stores the project makes images for; a store a language leaves
out does not get that language.

## targets

```yaml
targets:
  iphone69: {slot: app_store/iphone_69, size: [1320, 2868]}
  android_phone: {slot: play/phone, size: [1440, 2560], screen: [1080, 2342]}
```

A target is one store image size the project fills. `slot` picks a store slot from the engine's
catalog (`engine/store_shots/catalog.py`: each slot's store, frame kind, accepted sizes and panel
maximum); `size` is the store image; `screen` is the raw screen size when it differs from `size`
(Android raws leave out the system bars). The target id is the adapter's `--device` and the
placement key for that target.

A target is portrait or landscape by its numbers, width first: `size: [2868, 1320]` makes the
iPhone target landscape, with `screen` turned the same way. Every phone and tablet slot takes its
sizes turned to landscape (Play's 9:16 as 16:9); the Mac's are always landscape. A target turned
to landscape gets landscape raws, a device on its side, its frame's `landscape` placement
([layout.md](layout.md#placementyaml)) and landscape cluster members. Each target has its own
orientation, so a project can be portrait on iPhone and landscape on iPad.

## runs_on

```yaml
runs_on: {app_store: [iphone, ipad, mac], play: [phone, tablet]}
```

What the app runs on in each store, which decides the slots `check` requires. Without it: iphone,
and phone on Play.

## banned_phrases

```yaml
banned_phrases:
  - says: there is no account
    en: ['(?i)\bno\s+account\b']
    de: ['(?i)\bkein\s+Konto\b']
```

Promises the app must not make. Each entry has `says` (what the phrase claims, shown in the
problem) and a list of Python regular expressions per language; a language without a list is not
checked for that entry. Patterns are case-sensitive unless they start with `(?i)`. They are
checked in every image's recorded copy.

## adapter

```yaml
adapter:
  command: [uv, run, --quiet, --script, adapter/adapter.py]   # a list (a string is split POSIX-style)
  inputs: [adapter/**, ../app/src/**, 'fixtures/{lang}/**']
  textless: [splash]                  # optional: scenes that show no text at all
  accepted: ["tr/iphone69-home.png: 'Ayarlar' shows 6 of 7 characters"]   # optional
```

`command` captures the raws and `inputs` are the files that make them stale. `textless` lists the
scenes whose report may say `texts=0`. `accepted` lists report lines the owner accepted, matched
exactly. [adapter.md](adapter.md) has the contract.

## feature_graphic

```yaml
feature_graphic: {size: [1024, 500]}
```

Renders Play's feature graphic per Play language from `layout/feature.html` into
`out/play/<code>/feature-graphic.png`; needs a language that lists `play`. Without this key no
feature graphic is made.

## unframed

```yaml
unframed:
  premium_monthly: {scene: paywall-monthly, target: iphone69, lang: en}
```

Images that are one raw as captured, with no frame, layout or copy: an in-app purchase's App Store
review screenshot, say. Each entry names its image (letters, digits, `_`, `.`, `-`), the scene
the adapter captures for it at the target's screen size, and the one language it is captured in.
Compose saves it opaque and sRGB as `out/unframed/<name>.png`; the check holds it to the image
rules at the target's `screen` size, and the contact sheet of its store and language shows it. Its
scene needs no panel. What uses the image afterwards (an upload) is the project's own tooling.

## paths

```yaml
paths: {raw: captures/raw, out: captures/out}
```

Moves a folder: `storyboard` (`storyboard.yaml`), `copy` (`texts/`; `init --copy <folder>` writes it),
`layout`, `raw`, `out`, and under `.store-shots/`: `logs`, `work`, `sheets`, `preview`. Commit `raw/` and
`out/` with their `.inputs.json` sidecars, so a fresh checkout is not stale; ignore
`.store-shots/` (an `init` project's `.store-shots/.gitignore` does).

# Setup: a project for an app

Setup gives an app its store-shots project: the folder holding `store-shots.yaml`, the layout and
the adapter. `store-shots init` writes it from the example project; the storyboard and the copy
start empty, for the storyboard and copy stages to fill, and the layout holds the example's look until design
replaces it.

## Steps

1. Read the app to learn what the project needs, and confirm each answer with the owner:
   - the stores it ships in and the devices it runs on in each: `iphone`, `ipad`, `mac` on the
     App Store; `phone`, `tablet` on Play (its iOS, macOS and Android targets, its tablet layouts);
   - on each phone and tablet, whether it runs portrait or landscape: its supported orientations
     (`UISupportedInterfaceOrientations` in `Info.plist`, `android:screenOrientation` in
     `AndroidManifest.xml`, Flutter's `setPreferredOrientations`). An app that runs both shows
     the one it is mostly used in;
   - its first copy language and that language's store code (`en=en-US`); the other languages
     come later through copy's "New language" section;
   - how its screens can be captured: the platform, and a capture tool that fits its stack and
     the machine, held to "Choosing the capture tool" in [../docs/adapter.md](../docs/adapter.md);
   - whether this machine can capture every device: `iphone`, `ipad` and `mac` need macOS with
     Xcode and its simulators (`xcrun simctl list runtimes` lists an iOS runtime), `phone` and
     `tablet` need the Android SDK's emulator or a connected device (`adb devices`), a web app
     a browser. Check it yourself. A device it cannot capture goes to the owner before `init`:
     capture that device on another machine, or leave it out;
   - where the project folder goes. The default keeps all store work in a `publishing/` folder at
     the repo root, with the project in `publishing/store-shots/`. The project holds everything
     store-shots uses, the texts the images show included, in its `texts/` folder.
2. Run `init` into that folder, with one `--runs-on` per store:
   `store-shots --project publishing/store-shots init --runs-on app_store=iphone,ipad --runs-on play=phone --lang en=en-US`.
   Pass `--copy <folder>` only when the owner keeps the texts somewhere else.
   Each device gets the example's target and placement; a Play project also gets the feature
   graphic. `init` writes into a folder with no project files only.
   For a device the app runs landscape on, swap the two numbers of its target's `size` and
   `screen` in `store-shots.yaml` (`size: [2868, 1320]`); its frame's `landscape` placement then
   applies ([../docs/config.md](../docs/config.md#targets)).
3. Correct a store code that differs between stores in `languages:`
   ([../docs/config.md](../docs/config.md)).
4. Tell the owner, before you start, what the adapter is in plain words (the code that opens each
   app screen on the simulator or emulator and saves it), which files it adds to the app, and
   that it takes a while. Wait for their go ("Between steps" in `SKILL.md`).
   Write the adapter, following "Building an adapter, gate by gate" in
   [../docs/adapter.md](../docs/adapter.md). `init` writes a starter
   `adapter/adapter.py` that parses the arguments. Replace it with whatever the platform needs,
   and point `adapter.command` and `adapter.inputs` at it and at the app's sources. Run
   `store-shots adapter test` after each gate's change. Scenes come with the storyboard, in capture.

## Done

`.store-shots/logs/check.log` holds no `catalog:` line after `store-shots check`, and
`store-shots adapter test` passes `runs`, `unknown-scene`, `full-bleed` and `cut-off-text` for
every target. The later gates skip until the storyboard names scenes.

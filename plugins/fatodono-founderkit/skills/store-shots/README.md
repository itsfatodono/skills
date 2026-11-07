# store-shots

Built for startups and solo developers who need store screenshots for their app, at launch and
every time the app, its text or its languages change.

## What it does

Makes your App Store and Google Play screenshots, plus Play's feature graphic, from your app's
real screens. It frames them in device mockups, captions them in each of your languages and
checks them against each store's rules.

It doesn't upload them. The images land in a folder in your repo, and your release tooling (or
you) take them from there.

## How to use

### Install

Pick one per agent, because installing both gives you the skill twice.

<details>
<summary><b>Claude Code plugin</b>: auto-update</summary>

```bash
claude plugin marketplace add itsfatodono/skills
claude plugin install fatodono-founderkit@fatodono
```

**Updates:** automatic once you enable auto-update for this marketplace (`/plugin` → Marketplaces → `fatodono` → Enable auto-update). To update by hand, run `claude plugin marketplace update fatodono`.

</details>

<details>
<summary><b>Codex plugin</b>: auto-update</summary>

```bash
codex plugin marketplace add itsfatodono/skills
codex plugin add fatodono-founderkit@fatodono
```

**Updates:** automatic. Codex refreshes Git marketplaces and the plugins you installed from them on its own. To update by hand, run `codex plugin marketplace upgrade fatodono`.

</details>

<details>
<summary><b>Any agent</b> (skills.sh): manual-update</summary>

```bash
npx skills add itsfatodono/skills --skill store-shots
```

**Updates:** manual. Run `npx skills update`. The router doesn't come along on its own; add `--skill ask-fato` if you want it.

</details>

It needs [uv](https://docs.astral.sh/uv/), Google Chrome (or Chromium, or Edge on Windows) and
the simulators or emulators you capture on: Xcode and its simulators for iPhone, iPad and Mac,
the Android SDK's emulator or a connected device for Android.

### Run it

Open your app's repo and ask in your own words:

- "Make App Store and Play screenshots for my app."
- "Add German to my store screenshots."
- "Change the second screenshot's headline."
- "We redesigned the editor screen, update the screenshots."
- "Add iPad screenshots."

You don't need to know the steps below. It finds out what is out of date and starts at the step
your change needs.

### What happens

Before every step it tells you what it will do, what that changes and about how long it takes,
and waits for your go.

1. **It sets up.** It reads your app for the stores you ship in, the devices you run on, portrait
   or landscape, and your first language, checks that this machine can capture each device, and
   confirms all of it with you. Then it writes the capture code: a small program in your app's
   repo that opens each screen on the simulator or emulator and saves it. It uses a tool that fits
   your stack (XCUITest, Paparazzi, a Flutter integration test, Detox, Playwright) and tests it in
   eight small gates until it passes.
2. **It picks what the screenshots say.** It reads your code, store listing and current
   screenshots for the claims worth making, keeps only the ones it can point to code for, and
   ranks them: the first three carry the most, because that is what search results show. It
   captures just those screens so you can see them. You add, drop, reword or reorder.
3. **It designs the look.** It reads your app's colours, fonts and icon, then asks whether you
   have a look in mind: a description, a reference (your site, another app's store page, a brand
   guide), or nothing. It shows every screenshot on one preview sheet and changes it until you
   approve.
4. **It writes the text.** Headlines, sublines, badges and the feature graphic's text, in each of
   your languages. You approve every text before it goes in.
5. **It captures and builds.** It captures every screen on every device in every language,
   frames and captions them, and checks each image against the store's rules. A translated text
   cut off on screen stops the build here, and you pick the fix.
6. **You review.** One sheet per store and language shows every image at once. A change you ask
   for goes back to its step, and only the images it touches are rebuilt.

### What you get

Everything goes to one folder, by default `publishing/store-shots/` in your repo:

- `out/<store>/<language>/`: the finished images, one per device and screenshot, and on Play the
  feature graphic.
- `storyboard.yaml`: each screenshot's claim, the screen that shows it and the code that makes it
  true.
- `texts/<language>.yaml`: every text the images show, one file per language.
- `layout/`: the look, as an HTML page and its stylesheets. Edit it like any web page.
- `.store-shots/sheets/<store>/<language>.png`: the contact sheets you review.

What's left for you:

- Upload the images, or point your release tooling at `out/`.
- Run it again when the app changes. It re-captures only the screens your change touched.

## How it works

**Claims backed by code.** Every screenshot names the files that make its claim true, and the
check fails a screenshot that names none or names a file that doesn't exist. The listing never
promises a feature the app doesn't have. Promises the app no longer makes go in a list of banned
phrases, checked in every language.

**Small changes stay small.** Every capture and every image records the inputs it was made from:
your app's code, the text, the look, the placement. A new headline redoes only that screenshot,
and an app change re-captures only the screens that depend on it. You never rebuild everything
to fix one thing.

**Any platform.** The tool knows nothing about your app. It hands your capture code a request
and judges only what comes back. `store-shots adapter test` checks the capture code in eight
small gates, in order: that it runs, that it rejects a screen it doesn't know, that it captures
edge to edge with no status bar or letterbox, that it reports cut-off text, and then your real
screens in every language, and that two runs give the same pixels.

**Cut-off text is caught where it happens.** Your app's UI toolkit knows when a text was cut
off or ran past its line limit, so the capture code asks it instead of guessing from pixels. A
cut-off translation fails the build before it reaches a store.

**The stores' rules, with dates.** Image sizes, the number of screenshots per device, required
devices, no transparency, sRGB, and no other platform's name on App Store images: each image is
checked against them. The rules carry the date they were read from Apple's and Google's pages. If
a store rejects an image the check passed, the rules are out of date; [open an
issue](https://github.com/itsfatodono/skills/issues).

**No house style.** The look is yours, as plain or as wild as you want. It keeps a few rules:
the tool draws the devices and the screen shows as captured, never painted over, because the
screen is the proof of the claim. Every text comes from your text files so it can be translated
and checked, and every text box leaves room for a translation a third longer than the English.

**It asks, then gets out of the way.** It settles what your code and listing already show and
asks you only what is left, each question with a recommended answer. Once you say go, a step runs
without asking again.

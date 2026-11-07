# Design: the look

Design decides how the images look: the background, the typography and colours, the card's and
the badge's look, the feature graphic, and how the devices sit in the composition. Its output is
the project's `layout/` folder: the page, its stylesheets, fonts and icons, and the
`placement.yaml` the composition needs. The format is in [../docs/layout.md](../docs/layout.md).
`init` gives a project the example's look so that it builds from the start; design replaces it
with one made for the app.

There is no house style. The look can be as plain or as wild as the owner wants, as long as it
keeps the rules below.

## What every design keeps

- The page keeps the engine's contract ([../docs/layout.md](../docs/layout.md#the-page)): a
  `<head>` and a `</body>`, which rendering needs, and `data-place="card"` and
  `data-place="badge"` when the storyboard has cards or badges; without them a card or badge
  silently goes missing.
- Every text comes from the copy through `data-copy`, so it is translated and checked like the
  rest. The page holds no words of its own; a logo is an image.
- The engine draws the devices and status bars, and the app's screen shows as captured. The page
  may move, scale, rotate, crop or overlap a device, but never draws one, paints over a screen or
  changes its colours: the screen is the proof of the claim.
- Text grows: a translation can run a third longer than the English. Keep `data-fit-lines` on
  every text block, and leave the text room to grow rather than a box only the English fits.
- Lengths are in `vw` / `vh`, so one page serves every size of a frame kind. A target turned to
  landscape is a wide image: its frame's `landscape` placement entry puts the copy and devices
  where a wide image has room, and `body[data-orientation="landscape"]` styles the page for it.
- The headline reads at search-result size, about a tile's size on the full preview sheet, and
  its contrast with what is behind it is at least 4.5:1.
- The feature graphic keeps its texts and logo off the edges, where Play may crop it.
- A font comes from the app, or from wherever the project already gets it, referenced from the
  stylesheet. Chrome silently uses another font when one does not load, so check on the sheet
  that the intended one rendered. Compose tracks only the files inside `layout/`: a font file
  kept elsewhere makes no image stale when it changes.

## Steps

1. Read the app's look: its colours (Flutter's `ThemeData`, the iOS asset catalog's colour sets,
   Android's `colors.xml` and `themes.xml`, CSS variables or a Tailwind config), its fonts and
   where their files are, its icon and logo, and whether it runs light or dark. When the colours
   are a framework's defaults, the icon is the better source of the brand.
2. Open with one plain-text question, before any choices, and end your turn: does the owner have
   a look in mind? They can describe it, point to a reference (their website, another app's store
   page, a brand guide, a designer's file, an earlier screenshot set), or leave it to you. Put
   what you found in a sentence above the question (the app's main colours and its font), so they
   have something to react to.
3. Settle what their answer leaves open through the ask tool, each choice recommended from what
   they gave: read a reference they point to before you ask. Show each colour as its hex value and
   where the app uses it. When the owner leaves it to you, propose a look built from the app's own
   and say why.
4. Write the look into `layout/`: the page and its stylesheets, fonts, badge icons, the
   placement the composition needs, and `feature.html` when the project has a feature graphic.
5. Run `store-shots preview`. It renders every panel on every target, and the feature graphic,
   in the config's first language onto one sheet, `.store-shots/preview/<lang>/sheet.png`. A
   screen not captured yet is a grey placeholder named by its scene, and a panel without copy
   shows its claim as the headline, with a placeholder subline. `--panel` narrows it to the
   panels you are working on and `--lang` picks another language.
6. Check the sheet against the rules above, then show it to the owner and say which parts are
   placeholders. Change what the owner asks and preview again, until they approve the look.

## Done

The owner approved the look on the preview sheet, and `store-shots preview` exits 0. The images
themselves are approved in review, on the real screens and copy.

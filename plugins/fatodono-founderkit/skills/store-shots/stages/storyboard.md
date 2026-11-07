# Storyboard: what the screenshots say

The storyboard decides what the screenshots say and prove: the panels in order, the claim each makes,
the app screen that shows it, and the code that makes the claim true. Its output is
`storyboard.yaml` ([../docs/storyboard.md](../docs/storyboard.md)). You propose; the owner
decides. Ask every question as "Grilling: talking to the owner" in `SKILL.md` says.

## What a store visitor sees

Most visitors decide on the first panels. App Store search results show the first three portrait
screenshots (one landscape), and a Play listing shows its first few before any scroll. So:

- Panel 1 carries the app's main reason to install. Panels 1 to 3 together say what the app is and
  what it does better than the apps beside it.
- One claim per panel, worded as what the visitor gets ("Find any note in a second"), shown by a
  screen with the feature at work and filled with demo content. Splash, sign-in, onboarding,
  empty and settings screens prove no claim.
- Later panels hold supporting features. Each slot's panel maximum (`most` in
  `engine/store_shots/catalog.py`) is a ceiling: stop when the claims run out.

## Steps

1. **Look first.** Read the app for its claims before asking anything: its store listing text and
   current screenshots if it has them, its README, its screens and their entry points, the
   features behind its paywall, and what sets it apart (works offline, keeps data on the device,
   syncs across devices). Note the code that makes each candidate true as you go; a candidate you
   cannot back with code is not proposed, and neither is a promise in the project's
   `banned_phrases`. Done when every screen and paid feature you found is either a candidate with
   evidence or set aside. Read the code only: capture nothing to find candidates, since an app
   with hundreds of screens would make the owner wait for every one of them.
2. **Claims and order.** Ask the owner for the claims: your ranked list, recommended as it stands,
   held to "What a store visitor sees". To show the owner what a claim's screen looks like,
   capture only the screens your ranked list uses, one per claim, on one device and in the first
   language. Say how many before you start. The owner may add, drop, reword or reorder. Read the code
   for every claim the owner adds, as in step 1; one you cannot back goes back to the owner,
   reworded or dropped.
3. **Screens.** Once the claims are settled, ask per panel, a recommendation each: the screen it
   shows (a scene name the adapter captures), an optional card (a second scene cut to one
   element), an optional badge, the status bar (`airplane` for an offline claim, `none` for a
   full-screen app or game), or a cluster of devices per store.
4. Show the owner the whole storyboard: each panel's claim, screen and evidence. Write
   `storyboard.yaml` once the owner approves it.

For a change to an existing storyboard, steps 2 to 4 cover only the panels the change touches.

## Done

Every panel in `storyboard.yaml` is owner-approved and has `evidence` entries naming the code
that makes its claim true, and `.store-shots/logs/check.log` holds no `storyboard:` line after
`store-shots check`.

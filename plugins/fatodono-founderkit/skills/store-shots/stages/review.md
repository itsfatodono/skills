# Review: the owner approves the images

The owner approves images on the contact sheets, one per store and language:
`.store-shots/sheets/<store>/<code>.png`, every panel of every target in storyboard order, then on
Play the language's feature graphic, then the unframed images in that store and language. Together
they show every image the tool makes.

## Steps

1. Run `store-shots status`. Review a project with nothing stale; run `store-shots build` first
   when it lists anything.
2. Show the owner the sheets of every store and language the change touched, all at once, each
   named by its store and language code.
3. Collect the owner's verdict per sheet. A requested change goes to its stage through the change
   table in `SKILL.md`; build, then show the changed sheets again.

## Done

The owner approved every sheet the change touched, and `status` shows nothing stale.

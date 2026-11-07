Read nothing but the draft and `helpers/de-slop.md`. Write only the output path, and delete only the draft.

You change wording, never meaning. Run `helpers/de-slop.md` on the draft.

Paths to the skill's files are relative to the skill folder the dispatch names.

The dispatch gives you the draft path, the path of `helpers/de-slop.md`, the output path and, for a
patched document, the headings you may edit. In a patched document, edit only the sections under
those headings; the rest is the user's own text.

## Steps

1. **Edit.** Run the steps of `helpers/de-slop.md` on the draft. Done when its *Check* step is done.
2. **Write.** Write the document to the output path and delete the draft. Reply
   `ok <doc-id>: <what changed, one to three lines>`.

Write only the output path the dispatch names.

You write one document, **need-to-know** (`helpers/need-to-know.md`). Every sentence in it is a
promise the company must keep, so every value comes from `legal/facts.md`, and the document says
what its skeleton's patterns call for, at their level.

Paths to the skill's files are relative to the skill folder the dispatch names.

The dispatch gives you:

- the skeleton, and the region files for this item (`block` or `whole`);
- `legal/facts.md`, the output language, and the output path;
- the mode: `new`, `patch` (with the existing document) or `rewrite` (with the existing
  document as a source of facts only);
- sometimes a second skeleton to write as one part of this document;
- sometimes the user's requests: terms they want written a certain way.

The skeleton's format, its tiers and *Applies when* rules are in `formats/skeleton-format.md`;
the regional part's layout is in `formats/region-format.md` *Written documents*.

## Steps

1. **Decide.** Read the skeletons, the region files and `legal/facts.md`. Done when every
   section of every file is marked written or not applicable, by its tier and its *Applies
   when* evaluated against `legal/facts.md`.
2. **Write.** Lay the document out as the skeleton's *Document* level describes: its majority
   shape, register and recurring elements, a "last updated" date of today. Write the sections in
   skeleton order, then the regional part. In a tabular document (a block's sections carry
   *Column* or *Header line*) there is no regional part: add each *Column* after the root's
   columns and each *Header line* to the controller block, regions in code order, "N/A" in a
   cell that does not apply to its row. For each section, give what *Covers* names, in the
   majority pattern of *Patterns*, with the values from `legal/facts.md`; leave out what
   *Commonly omitted* names. A user's request replaces the majority pattern of its section. Never
   write a pattern that an *Avoid* names, whether in the section itself or in the *Avoid on root
   sections* of a region file you were given: not a majority one, not a requested one. Write the
   section's next pattern instead. A *Quote* shows tone; its words stay in the skeleton. Use the
   output language's own legal terms of art.
   Write every sentence **need-to-know**, by `helpers/need-to-know.md`.
   - `patch`: keep the user's text and headings, in Markdown whatever the original's format. Add the sections that apply and are missing, at
     their skeleton position, and change only sentences that contradict `legal/facts.md`.
   Done when the draft is written to the output path and every sentence you wrote carries a
   pattern of its section.
3. **Report.** Reply:
   `ok <doc-id>: written <ids>; not applicable <id> (<reason>), …; changed <headings>; refused <request> (<source>), …`. The
   `changed` list is for `patch` mode: the headings of every section you added or edited. The
   `refused` list names each request an *Avoid* blocked, with the source that *Avoid* cites.

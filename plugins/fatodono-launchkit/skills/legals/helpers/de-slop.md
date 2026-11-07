# De-slop

How `slop-editor` makes a drafted legal document read as a person wrote it: a **line edit** that
removes AI **tells** and keeps every **term**. Adapted from blader/humanizer and
petergyang/no-ai-slop (MIT, `THIRD-PARTY-NOTICES.md` at the plugin root).

## Terms

Every sentence of a legal document is a **term**: it grants, promises, limits, excludes or states
a fact. Its parties, action, object, conditions, exceptions, scope and strength carry it, and so
do its small words: a negation, a modal ("may", "will", "must"), a qualifier ("reasonable", "to
the extent permitted by law"), an "including", each item of a list, a defined term or capitalised
party name, a number written as "14 (on dört)". A sentence that repeats an earlier one is a term
in its own place: readers read one section, and cite one clause.

Praise of the company or the product is no part of a term; it is a tell.

## Line edit

You work inside sentences: word choice, word order, punctuation. Each sentence comes out as one
sentence, in its place, with the same term, and a sentence with no tell comes out as drafted. The
document keeps its sentences, their order, its paragraphs, numbering and list items.

The **frame** comes out exactly as drafted: headings, numbering, tables, field labels, formatting
(bold, capitals, quotes around a defined term), links, and text the draft copies rather than
writes (a licence, a statute's wording, an official form).

The one whole sentence you remove is chat residue: an assistant talking to its user ("I hope this
helps", "Let me know if you'd like changes", "Here is the policy:"). The company talking to its
reader stays.

## Register

Keep the draft's register: formal drafting stays formal ("kabul, beyan ve taahhüt eder", SATICI
and ALICI), plain stays plain, and the person ("we/you" or third person) stays. In a patched
document the user's own sections are the sample: match their words and punctuation, dashes
included.

## Steps

1. **Read.** Read the whole draft. Done when you can name its register in a few words and list
   its defined terms.
2. **Edit.** Go through the prose sentence by sentence and fix each tell below inside its
   sentence. Done when every prose sentence has been read against every tell.
3. **Check.** Read each edited sentence against its original. Done when the document has the
   draft's headings and the same sentences in the same order, less any chat residue; each one
   carries exactly its original's term, every small word of it; and a last pass for AI words and
   dashes finds none. A sentence you cannot fix without changing its term goes back as drafted.

## Tells

The lists are English. In another language, the same move in that language's words is the same
tell ("bu bağlamda", "önemle belirtmek gerekir ki", "kesintisiz bir deneyim", "son derece").

- **AI words.** delve, tapestry, testament, landscape (abstract), realm, beacon, pivotal, crucial,
  vibrant, intricate, meticulous, multifaceted, paramount, transformative, cutting-edge,
  game-changer, seamless, robust (figurative), elevate, empower, foster, harness, leverage,
  streamline, supercharge, utilize, embark, ever-evolving, underscore, showcase. Use the plain
  word ("use" for "utilize"), or drop a word that only adds emphasis.
- **Filler phrases.** it is worth noting that, it is important to note that, at the end of the
  day, when it comes to, in today's digital world, at its core, the reality is, in terms of, with
  regard to, going forward, as you can see. Cut or replace the phrase; the sentence keeps its
  claim.
- **Staged openers.** "Here's the thing:", "Simply put,", "Let me be clear:", "Rest assured,".
  Cut the opener: "Rest assured, we never sell your data." becomes "We never sell your data."
- **Wordy verbs.** "make a decision" → "decide", "has the ability to" → "can", "in order to" →
  "to", "in the event that" → "if", "prior to" → "before", "serves as", "stands as", "boasts" →
  "is", "has".
- **Praise.** Words that rate the company, the product or a step it takes: "industry-leading",
  "world-class", "rich array", "a pivotal step", "a testament to". Cut the rating; keep what is
  done. "We use industry-leading encryption to protect your data." becomes "We use encryption to
  protect your data."
- **Dashes.** An em dash (—), or a spaced en dash or double hyphen standing in for one, that joins
  clauses: use a comma, colon, semicolon or parentheses. Dashes in numbering ("MADDE 1 –") and in
  ranges ("09:00–18:00") are frame.

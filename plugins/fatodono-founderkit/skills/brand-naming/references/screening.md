# Screening Reference

Screening is where roughly 90% of a shortlist dies. A professional naming team runs a fully staffed trademark team
(paralegals, URL search specialists, attorneys) plus a network of 100+ linguists across 75 countries,
screening 10-25 languages per project depending on the client's markets — and still expects to hand
the client only 3-4 survivors.

Two consequences for how you work:

- **Keep the long candidate file.** You will come back to it. A finalist dying at the legal gate is
  the normal case, not the failure case.
- **Screen in cost order.** Fluency is free, legal pre-screen is cheap, real clearance is expensive.
  Don't spend effort on a name that can't be said out loud.

---

## Gate 1 — Processing fluency (free, do it first)

Run each shortlist candidate through all six. A failure on 2+ is usually disqualifying.

1. **Say it aloud.** Does it trip? Do consonant clusters collide at the seam (`Vercelll`, `Strathm`)?
2. **Spell it over the phone.** If the answer requires "no, with two f's," that's a permanent tax
   on every word-of-mouth referral. This alone is why Codeium became Windsurf.
3. **Hear it once, write it down.** Ask honestly whether a stranger would produce the right spelling.
4. **Read it in a sentence.** "We're building X." "I'll send it via X." "Just X it." Some names only
   work as nouns and break the moment anyone tries to verb them.
5. **Visualize it.** The researchers' rule: we remember what we understand and can picture. `Outback`
   produces an image; `Synergix` produces nothing.
6. **Non-native pronunciation.** Have a speaker of a target-market language attempt it cold.

---

## Gate 2 — Legal pre-screen

**State plainly, every time: this is a pre-screen, not clearance.** You are eliminating obvious
conflicts so the user doesn't pay an attorney to review names that were never viable. A name is not
"available" until a trademark attorney says so in the relevant classes and jurisdictions, and you
should never imply otherwise.

What to check, in order:

1. **Exact and near-identical marks in the relevant Nice classes.**
   - USPTO Trademark Search (`tmsearch.uspto.gov`) — US
   - EUIPO eSearch plus (`euipo.europa.eu`) — EU
   - WIPO Global Brand Database (`branddb.wipo.int`) — international, covers many national registers
   - National office for the user's home market if outside these
2. **Common-law use.** Plain web search plus GitHub, npm/PyPI/crates for developer tools, and the
   App Store / Play Store for apps. An unregistered but established user in the same space can still
   block you.
3. **Phonetic equivalents, not just spellings.** Trademark conflict turns on likelihood of confusion,
   which includes sound. `Fybre` conflicts with `Fiber`. Search how it sounds, not how it's typed.
4. **Company registry** in the jurisdiction of incorporation.

**Reduce conflict risk at the design stage** rather than the screening stage: coined words and
transplanted-from-another-domain real words clear far more easily than descriptive ones. A
descriptive name has a second legal problem beyond conflict — descriptive marks are weak or
unregistrable on their own (this is why `ProMop` and `EasyMop` were unavailable to P&G in the first
place).

---

## Gate 3 — Linguistic and cultural screening

Screen every finalist against every market the user actually operates in or plans to enter. Ask what
those markets are; don't assume English-only.

Check for:

- **Obscenity and taboo**, including near-homophones. This is the classic catastrophic failure and
  the reason professional teams keep linguists on retainer rather than using dictionaries.
- **Unintended meaning.** A word that's neutral in one language and comic, medical, or religious in
  another.
- **Mispronunciation.** Which sounds don't exist in the target language, and what does the name
  become when they're substituted? (No /θ/ in most languages; /r/ and /l/ merge in Japanese; Spanish
  speakers prepend an /e/ to initial `s`+consonant, so `Sprint` → `Esprint`.)
- **Transliteration.** In CJK markets, what characters would be used, and what do they mean? Chinese
  transliteration is a second naming project — the characters carry meaning independent of sound.
  Arabic and Hebrew drop short vowels, which can collapse a name into a different word.
- **Script and casing.** Does it survive all-caps, a favicon, and a non-Latin keyboard?
- **Existing strong association.** A word that's already a major brand, a political figure, or a
  news event in a target market is spent territory.

**Be honest about your own limits here.** You can catch the obvious cases and flag the risky
phonetic shapes; you cannot replace a native speaker in each market. Recommend native-speaker checks
for any market that matters commercially, and say which candidates you couldn't verify.

---

## Gate 4 — Digital

Report this; **do not rank by it.**

Placek's position is worth quoting to users who are anchored on the domain: *"the .com has become
just an area code."* Search behavior has moved to AI assistants and app stores, and premium domains
typically transact in the $15-30K range — cheap relative to what a company spends building a brand,
and trivially cheap relative to shipping a worse name for a decade.

Check and report:

- **.com status.** Registered, parked, actively used, or for sale — and rough acquisition cost if
  parked. "Taken" is not a verdict; taken-and-actively-used-by-a-competitor is.
- **Alternatives:** `.ai`, `.io`, `.co`, `get-`/`use-`/`try-` prefixes, or `<name>hq`. Many strong
  current brands run on these.
- **Social handles** across the platforms the user actually needs.
- **Search collision.** Google the bare name. If page one is dominated by an established entity in
  an adjacent field, that's a real acquisition-cost problem — more real than domain availability.
- **Package/registry namespace** if it's a developer product (npm, PyPI, crates.io, Docker Hub).

**The failure mode to name explicitly:** letting domain availability drive selection guarantees you
choose from the set of names nobody else wanted. If a user is rejecting a strong candidate purely on
the .com, say so directly and give them the cost comparison.

---

## Presenting screening results

For each finalist, a compact risk block beats a table of green checkmarks:

```
NAME
  Fluency    ✓  spellable on first hearing; verbs cleanly ("just X it")
  Legal      ⚠  live mark in class 9 (US) for adjacent product — needs attorney review
  Language   ✓  clean in EN/TR/DE/ES;  ⚠ initial cluster hard for JP speakers
  Digital    ⚠  .com parked (~$20K est.);  .ai and all handles free
```

Ranking finalists by risk-free-ness is the wrong instinct — it reproduces the comfort bias the whole
method exists to defeat. Present the risks, recommend on strategy, and let the user trade off
knowingly.

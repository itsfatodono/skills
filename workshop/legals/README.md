# legals

A plugin that writes your app's legal documents from your own code: privacy
policy, terms of service, subscription terms, refund policy, account deletion page, and the
documents a region's law adds.

**It is not legal advice.** It writes drafts that follow how real companies write these
documents. Have a lawyer read them before you publish.

## What it writes today

| Document                                                    | Built from                                  |
| ----------------------------------------------------------- | ------------------------------------------- |
| Privacy Policy, with EU, UK and US parts                    | 30 companies                                |
| Terms of Service                                            | 30 companies                                |
| Subscription Terms                                          | 30 companies                                |
| Refund Policy                                               | 25 companies                                |
| EULA (installed software)                                   | 22 companies                                |
| Cookie Policy                                               | 20 companies                                |
| Account / Data Deletion page                                | 25 companies                                |
| Record of Processing Activities (internal)                  | 30 records; turns on once a region needs it |
| Mesafeli Satış Sözleşmesi (Turkish distance sales contract) | 29 Turkish sellers                          |

Any other document can be built on request (see _Building a skeleton_), but that costs much
more.

## How to use it

Until it is published, load it from this repo:

```sh
claude --plugin-dir /path/to/fatodono-skills/plugins/fatodono-launchkit
```

Then, in your app's repo, ask in your own words: "write our privacy policy and terms", "update
our refund policy", "which legal documents do we need before launch?". You can also type
`/fatodono-launchkit:legals`.

A run goes like this:

1. It says once that this is not legal advice.
2. It asks where your users are, works out which documents your app needs, and shows you the
   list.
3. It reads your code (SDKs, store metadata, sign-in, payments, existing policies) and writes
   what it found to `legal/facts.md`.
4. It asks you only what the code could not answer, four questions at a time, each with a
   recommended answer.
5. It drafts every document, edits the wording, and checks the documents against your facts
   and against each other.

You get Markdown files in `legal/`: `legal/privacy-policy.md`, `legal/terms-of-service.md` and
so on. If you already have a policy, it keeps your wording and adds or fixes only what is
missing or wrong. Your original file is never touched. Moving the text into your website or app
is up to you.

Run it again after your app changes. Your earlier answers in `legal/facts.md` are kept, and
everything else is checked against the code again.

## The ideas behind it

**Learn from real documents, not from a template.** For each document we read 25 to 30 real
ones from large, mid-size and small companies, and kept reading until five in a row added
nothing new. The result is a _skeleton_: which sections companies include, how many of them
include each one, how they usually write it, and what they leave out. A section nearly everyone
has is always written; a rare one is written only when your app needs it. Each skeleton carries
the date it was built and warns you when it is over a year old.

**Your code is the source of truth.** A legal document is a list of promises. Every value in
yours comes from your code or from your answers, and nothing is promised that the facts do not
show. That is why it reads your repo first and asks second.

**The legal minimum, said once.** It recommends what the law or the app stores require of your
app, says why once, and accepts your answer if you say no. It does not push extra clauses on
you.

**Laws are add-ons.** The main document is the same for everyone. What one law requires (GDPR,
US state laws, Turkish consumer law) sits in its own regional part, added when you have users
there. Adding or dropping a region changes only that part.

**Separate eyes for separate jobs.** Different agents read the code, write each document, edit
the wording, and check the result, each with only the context its job needs. The editor never
sees your facts, so it can only change the words, and it checks every sentence it edits against
the original; the checker then checks the facts.

**Readable, but exact.** The editor removes the habits that make AI text tiring to read, one
sentence at a time. It changes words, never which sentences are there or what they promise.

## Building a skeleton

When you ask for a document it has no skeleton for, it builds one from apps in your own field:
it reads 10 of their documents and learns the common sections from them. That takes 11 agents
and a good part of a usage window, so it tells you in a few words what it will research and
waits for your okay. This is the only time it stops to ask leave; with a ready skeleton it
runs straight through. The result goes to `legal/.skeletons/` and `legal/.research/` in your
repo.

## Inside the repo

The skill ships from `plugins/`; paths under it are from the repo root. Everything else is in
this folder (`workshop/legals/`) and never ships.

- `plugins/fatodono-launchkit/skills/legals/`: the skill. `SKILL.md` is the entry point; skeletons are in
  `skeletons/`, regions in `regions/<code>/`, formats in `formats/`, the building method in
  `build/`.
- `plugins/fatodono-launchkit/skills/legals/helpers/`: the instructions of each agent the skill dispatches.
- `research/`: how each skeleton was built: candidates, extraction tables, merge notes. Not
  shipped.
- `PLAN.md`: goal, structure and decisions.
- `plans/`: one file per document: what is built and what is still open.

A region (say Brazil) can be contributed as one new folder, without editing any existing file.
The rules are in `formats/region-format.md`.

`helpers/de-slop.md` is adapted from [blader/humanizer](https://github.com/blader/humanizer) and
[petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT); their notices are in
`plugins/fatodono-launchkit/THIRD-PARTY-NOTICES.md`.

// Her ne kadar 400+ firmadan distilled olsa da avukatınıza gösteriniz
// Readme ' ye yazalım eğer legal dökümanları sizi daha fazla korumasını evil bi yerden yaklaşmasını istiyorsanız bunu söyleyin facts.md' ye yazacaktır. bundan sonra ona göre yapar ama önermiyorum.

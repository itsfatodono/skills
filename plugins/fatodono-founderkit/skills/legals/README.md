# legals

Built for startups and solo developers who need their app's legal documents, before launch or long after it. The 17 items
ready today are distilled from about 430 real companies' documents; the target is about 2100
across all 72 items. Feel free to contribute.

## What it does

Writes your app's legal documents from your own code: privacy policy, terms of service,
subscription terms, refund policy, account deletion page, and the extra documents your users'
countries require, such as the KVKK texts for Turkey. It also writes the company's own
agreements: a founders' / shareholders' agreement, an IP assignment and a contractor agreement.

**It is not legal advice.** It writes drafts that follow how real companies write these
documents. Have a lawyer read them before you publish.

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
npx skills add itsfatodono/skills --skill legals
```

**Updates:** manual. Run `npx skills update`. The router doesn't come along on its own; add `--skill ask-fato` if you want it.

</details>

It runs several agents side by side, so your agent must support subagents.

### Run it

Open your app's repo and ask in your own words:

- "Write the legal documents for my app."
- "Which legal documents do I need before launching on the App Store?"
- "Write a contractor agreement for the designer we're hiring."
- "Update my privacy policy, we added RevenueCat."
- "I sell in Turkey, write my KVKK texts."
- "Make legals more in favor of the company"

You don't need to name a skill or know which documents exist. It works out what your app
needs.

### What happens

1. **It picks the documents.** It looks at your repo (store metadata, sign-in, payment SDKs),
   asks where your users are if the code doesn't show it and which language the documents
   should be in, and shows you which documents your app needs and why. Documents that only one
   country's law requires are written in that country's language. It does not translate; you
   can translate the documents yourself afterwards. If you already have a privacy policy or terms, in the repo or on your
   site, it updates those instead of starting over.
2. **It reads your code.** It finds every fact the documents need: what data you collect,
   which SDKs and services get it, how sign-in, payments and account deletion work.
3. **It asks what the code can't show.** Things like your company's legal name, your support
   address or your refund rules. Every question comes with a recommended answer, so most of
   them take one click. It asks a few at a time, and only what is still open.
4. **It writes, edits and checks.** Once your answers are in, it drafts each document, edits
   the wording, cuts detail the document doesn't need and checks every document against your
   facts. You don't need to do anything during this part.

### What you get

Everything goes to a `legal/` folder in your repo:

- `legal/<document>.md`: one Markdown file per document, e.g. `legal/privacy-policy.md`.
- `legal/facts.md`: every fact the documents rely on, and where it came from (a file in your
  code, or your answer). Read it first. If a fact is wrong, the documents are wrong too.

What's left for you:

- Have a lawyer read the documents.
- Put each one on your site or in your app, in whatever format they use.
- Link them from the app and from your store listings.

When your app changes (a new SDK, a new country, a new paid plan), run it again. It updates
the documents you already have.

## What it writes today

`legals` aims to cover 72 items: 47 documents, 12 forms, 1 template and 12 tasks. 17 are
ready; the other 55 are waiting for my weekly usage limit to reset.

Every document has a global part that works anywhere. A region adds what its laws require.

- ✅ the region has its own sections in the document
- ☑️ checked against the region's laws: it needs no sections of its own, only marks what the
  shared text must not say there

<!-- coverage:start -->
| Document | Global | EU | TR | UK | US | Updated |
|---|---|---|---|---|---|---|
| Privacy Policy | ✅ | ✅ | ☑️ | ✅ | ✅ | 2026-10-26 |
| Terms of Service | ✅ | ☑️ | ☑️ | ☑️ | ☑️ | 2026-10-26 |
| End User License Agreement | ✅ | ☑️ | ☑️ | ☑️ |  | 2026-10-27 |
| Subscription Terms | ✅ |  |  |  |  | 2026-10-26 |
| Refund Policy | ✅ |  |  |  |  | 2026-10-26 |
| Cookie Policy | ✅ | ☑️ | ☑️ | ☑️ |  | 2026-10-27 |
| Account / Data Deletion page | ✅ |  |  |  |  | 2026-10-26 |
| Open Source Notices | ✅ |  |  |  |  | 2026-10-27 |
| Data Subject Request Form | ✅ | ✅ | ✅ | ✅ | ✅ | 2026-10-27 |
| Record of Processing Activities | ✅ | ✅ |  | ✅ |  | 2026-10-27 |
| Founders' / Shareholders' Agreement | ✅ |  |  |  |  | 2026-11-12 |
| IP Assignment for founders and employees | ✅ |  |  |  |  | 2026-11-12 |
| Freelancer / Contractor Agreement | ✅ |  |  |  |  | 2026-11-12 |
| Mesafeli Satış Sözleşmesi |  |  | ✅ |  |  | 2026-10-26 |
| Ön Bilgilendirme Formu |  |  | ✅ |  |  | 2026-10-27 |
| KVKK Aydınlatma Metni |  |  | ✅ |  |  | 2026-10-27 |
| KVKK Açık Rıza Metni |  |  | ✅ |  |  | 2026-10-27 |
<!-- coverage:end -->

Planned regions:

- Germany (`de`): the Impressum, then its parts in the documents above
- Brazil (`br`, LGPD): its parts in the documents above, starting with the Privacy Policy

Planned for the regions above: an own EU part for the Cookie Policy, and a Turkish part for the
Record of Processing Activities (the VERBİS inventory; it waits for samples, as no company
publishes a filled one).

**A. Public core documents**

<details>
<summary>Not built yet (2)</summary>

- Contact / Support page
- Imprint / Künye

</details>

**B. Privacy and data protection (public)**

<details>
<summary>Not built yet (2)</summary>

- Children's Privacy Notice (COPPA, GDPR-K)
- Sub-processor List

</details>

**C. Internal compliance (not public)**

<details>
<summary>Not built yet (7)</summary>

- KVKK retention and destruction policy
- DPIA
- Data breach response procedure
- Cross-border transfer standard contract (KVKK) / SCC (GDPR) — template
- Information Security Policy
- DPAs with processors — task
- VERBİS registration — task

</details>

**D. App Store / Play forms and declarations**

<details>
<summary>Not built yet (13)</summary>

- App Store Privacy Label — form
- Play Data Safety form — form
- Apple Privacy Manifest (`PrivacyInfo.xcprivacy`) — form
- Permission usage strings — form
- App Tracking Transparency prompt — form
- Age rating questionnaires (Apple, Play IARC) — form
- Play Target Audience & Content form — form
- Play Ads declaration — form
- Encryption / export compliance declaration — form
- EU DSA trader status declaration — form
- Play special declarations — form
- Developer registration, D-U-N-S, tax and banking forms — task
- App Review notes and demo account — form

</details>

**E. Commerce and payment**

<details>
<summary>Not built yet (4)</summary>

- Withdrawal right notice and digital-content waiver
- ETBİS registration — task
- Invoicing (e-Arşiv / e-Fatura) — task
- Price and tax display rules — task

</details>

**F. Content and platform (user-generated content)**

<details>
<summary>Not built yet (6)</summary>

- Acceptable Use Policy
- Community Guidelines
- Copyright / DMCA policy and notice procedure
- DSA notice-and-action and point of contact
- DSA transparency report
- Law 5651 hosting-provider duties — task

</details>

**G. Marketing and communication**

<details>
<summary>Not built yet (5)</summary>

- Commercial electronic message consent text
- İYS registration — task
- Unsubscribe mechanism (CAN-SPAM / GDPR) — task
- Affiliate, sponsorship or influencer disclosure
- Newsletter privacy notice

</details>

**H. AI, accessibility and sector-specific**

<details>
<summary>Not built yet (5)</summary>

- AI use disclosure (EU AI Act)
- Accessibility Statement (European Accessibility Act)
- Disclaimers (health, finance, legal advice)
- Beta / TestFlight test terms
- Vulnerability Disclosure Policy and `security.txt`

</details>

**I. B2B / enterprise sales**

<details>
<summary>Not built yet (7)</summary>

- MSA
- Order Form
- DPA (with customers)
- SLA
- Security whitepaper and questionnaire answers
- SOC 2 / ISO 27001 reports — task
- NDA

</details>

**J. Company and intellectual property**

<details>
<summary>Not built yet (4)</summary>

- Incorporation documents and tax registration — task
- Employee privacy notice (KVKK)
- Trademark registration (TÜRKPATENT, EUIPO, USPTO) — task
- Domain and brand usage guidelines

</details>

## How it works

**Learn from real documents, not from a template.** For each document we read 25 to 30 real
ones from large, mid-size and small companies, and kept reading until five in a row added
nothing new. The result is a _skeleton_: which sections companies include, how many of them
include each one, how they usually write it, and what they leave out. A section nearly everyone
has is always written; a rare one is written only when your app needs it. Each skeleton carries
the date it was built, and you get a warning when it is over a year old.

**Your code is the source of truth.** A legal document is a list of promises. Every value in
yours comes from your code or from your answers, and it promises nothing the facts do not
show. That is why it reads your repo first and asks second.

**The legal minimum, said once.** It recommends what the law or the app stores require of your
app, says why once, and accepts your answer if you say no. It does not push extra clauses on
you.

**Laws are add-ons.** The main document is the same for everyone. What one law requires (GDPR,
US state laws, Turkish consumer law) sits in its own regional part, added when you have users
there. Adding or dropping a region changes only that part.

**Separate eyes for separate jobs.** Different agents read the code, write each document, edit
the wording, and check the result, each with only the context its job needs. The editor never
sees your facts, so it can only change the words. It compares every sentence it edits with the
original. A trimmer that never sees your facts either reads each document against how real
companies write it, and flags what they leave out: internal tools, how your defences work, your
code's timings. Then the checker checks the facts.

**Only what readers need.** Your code knows far more than your documents should say. Each
document says what real policies say, at their level: data by category, safeguards in general
terms. Every extra detail is a promise you must keep and a map for an attacker.

**Readable, but exact.** The editor removes the habits that make AI text tiring to read, one
sentence at a time. It changes words, never which sentences are there or what they promise.

## Building a new type of document

When you ask for a document it has no skeleton for, it builds one from apps in your own field:
it reads 10 of their documents and learns the common sections from them. That takes 11 agents
and a good part of your usage limit, so it tells you in a few words what it will research and
waits for your okay. Apart from its questions about your app, this is the only time it stops;
with a ready skeleton it runs straight through. The result goes to `legal/.skeletons/` and `legal/.research/` in your
repo.

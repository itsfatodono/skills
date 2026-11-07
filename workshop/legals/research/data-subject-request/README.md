# data-subject-request (root): build record

Built 2026-10-27. Root skeleton: `plugins/fatodono-launchkit/skills/legals/skeletons/data-subject-request.md`.
Region blocks: `regions/eu/data-subject-request.md`, `regions/uk/data-subject-request.md`,
`regions/us/data-subject-request.md`. The `tr` block is built from the KVKK pool (PLAN.md
decisions 45 and 49) and maps against this build's ids (`merge.md` *Section ids*). The document is
the form or request page a person uses to send a data-protection rights request. A privacy-policy
section that only describes rights is not this document.

## Files

- `candidates.md`: the pool (24 of 30), the reserve and the rows left out.
- `pool/`: raw rows from three `pool-collector` slices (`dsar-us`, `dsar-eu-uk`, `dsar-tail`).
- `portal-probe.md`: how each hosted-portal vendor's form was read (OneTrust `/publish` JSON,
  Transcend via Wayback), and which vendors have no recipe.
- `samples/sNN.md`: one extraction table per sample, s01–s20. `raw/` (git-ignored) holds the
  stripped texts.
- `merge.md`: the 27 section ids and their meanings, mapping notes, section map, merged list,
  patterns, document level, *Regional content*, facts, copies, qualification, saturation log,
  decisions, changes.

## Run

- **Routes run:** R1 (App Store storefronts `us`, `gb`, `ie`), then R4 on each listing's privacy
  policy; R4 on EU and UK company sites without an app; R2 (long tail, storefronts `us` and `gb`)
  plus 5 web searches for small companies' own forms.
- **Pool:** 24 candidates (10 large, 10 mid, 4 small). Group check (rule 5) and first-screen check
  at selection. A cap of one third of picks per portal vendor (7 OneTrust picks of 21 at
  selection).
- **First batch:** s01–s15. c01–c12 (5 large, 5 mid, 2 small), then the top-up s13 = c22 Glyyd and
  s14 = c23 Luzid (the only valid small rows from the tail) and s15 = c13 Bolt (large, as no
  third small row existed). All valid; none replaced.
- **Saturation:** batch 1 s16–s20 = c14 Nav, c15 Vodafone UK, c24 Grow Therapy, c19 Philips, c16
  Transcarent; all valid. s18 brought a new id (`appeal`, a right to appeal a refusal) and s20
  another (`non-discrimination`). Both are US-state content and sit outside the root, so the 23
  root ids did not change after the first batch.
- **Stop reason:** the owner closed the pool after batch 1 (no more extraction or collection).
  The last non-new run was 0 samples long (s20 was new), so `saturated: false`,
  `sample_count: 20`. c17, c18, c20, c21 and the reserve were not extracted.

## Invalid

None. Borderline but valid (details in `merge.md` *First-batch qualification* and *Saturation*):
s04 OpenAI read from a Wayback copy of its portal data (2026-06-04); s07 The AA and s17 Vodafone
take access requests only; s10 1stDibs has no request-type field and out-of-date California
exemption notices; s11 JD Sports leaves out about 45 OneTrust fields that never show; s14 Luzid's
submit button sends nothing (its wording is counted as published).

## Templates and copies

Rule 4: no copies. Five forms run on OneTrust (s08 s11 s12 s19 s20) and share its default
verification and thank-you wording; each has its own fields and request types, so all count, and
the shared wording adds to patterns once (decision 39). s04 runs on Transcend.

## Shortfalls

- **Small companies: 4 of 10.** Small companies rarely publish a request form: most small apps
  give only a privacy email in the policy. The `dsar-tail` slice (R2 over about 5,540 sellers with
  200–30,000 ratings, plus web searches) found about 1 seller in 400 with a readable form of its
  own. Of its 10 rows, 3 were small and 2 passed (Glyyd, Luzid); Waking Up was opt-out only.
  Other small leads failed rule 1 (Cal AI and Pi use DataRep's generic form; Ebby Halliday uses
  HomeSpotter's) or sit on vendors with no recipe (TrueVault, Termly, Zendesk). Valid samples by
  size: 8 large, 8 mid, 4 small.
- **US/EU split.** By home region: 13 US, 4 EU (NL, IE, EE, NL) and 3 UK. Every EU and UK sample
  is a large company, because the EU/UK slice found no mid or small company with a readable form.
  By content: 14 of 20 carry US state content, 8 EU content and 4 UK content (several carry more
  than one). The `eu` and `uk` blocks rest on few samples (7 and 4 counted rows at most) and are
  marked `saturated: false`.
- **Vendors with no recipe** (blocked, not sampled): SixFifty, Zendesk forms, DataGrail, Relyance,
  Typeform, Termly, Pipedrive, Salesforce, in-house single-page apps and bot walls. See
  `candidates.md` *Left out* and `portal-probe.md`.

## Regional content not built

Rows under `merge.md` *Regional content* for regions with no block. They are kept for a
contributor who adds the region.

- **Canada (`ca`):** s12's menu for Canadian residents under PIPEDA and Quebec Law 25 (access,
  correct, delete, opt-outs from profiling, sharing and social-media matching).
- **China (`cn`):** s01's bundle has a "Withdraw consent" option with a cookie note (PIPL Art. 15),
  not rendered for its locale; s19 asks for a phone in place of email, and notes that some apps
  are unavailable, when the country is China.
- **Brazil (`br`):** s14 lists Brazil as a region option and ships a Portuguese version of the
  form; no Brazil-specific content.

## Facts

- Added shared key `facts.users.request_handling` (how a request is handled: tool, identifiers,
  verification, representatives, response time, status tracking, reply channels, attestation).
  `facts.users.rights_channels` keeps the routes. The root skeleton uses the new key, so decision
  29 allows it.
- Added region key `facts.us.appeal_process` (appeal channel, decision time, attorney general
  link) for the `us` block.

## Samples

All fetched 2026-10-27, language `en`.

| Sample | Company | URL | Sector | Size |
|---|---|---|---|---|
| s01 | Booking.com | https://www.booking.com/content/dsar.en-gb.html | travel | large |
| s02 | Dave, Inc | https://dave.com/ccpa-request/ | finance | mid |
| s03 | Copilot Money, Inc. | https://www.copilot.money/consumer-request-webform | finance | small |
| s04 | OpenAI OpCo, LLC | https://privacy.openai.com/ (Wayback capture 2026-06-04 of its portal data) | productivity | large |
| s05 | Timely Telehealth, LLC | https://timelycare.com/privacy-rights-request-form/ | medical | mid |
| s06 | Becausal, Inc. | https://www.becausal.com/data-subject-requests | shopping | small |
| s07 | Automobile Association Developments Ltd (The AA) | https://www.theaa.com/help-support/data-subject-access-request | travel | large |
| s08 | GPD Holdings, LLC (CoinFlip) | https://privacyportal.onetrust.com/webform/36bdb9d1-f751-4a50-9ca1-e6a57e5f036c/49aaa221-9589-46fd-9101-d20e6c5b5dfd | finance | mid |
| s09 | Intercom | https://www.intercom.com/privacy-form | b2b-saas | large |
| s10 | 1stdibs.com, Inc. | https://www.1stdibs.com/info/forms2/california-consumer-privacy-act/ | shopping | mid |
| s11 | JD Sports Fashion | https://privacyportal.onetrust.com/webform/9c661b24-1df6-4962-8375-8dab4483ae39/7a82c8cc-0b5f-429c-b9de-74a244a15b41 | shopping | large |
| s12 | NHL Interactive Cyberenterprises, LLC (NHL) | https://privacyportal.onetrust.com/webform/c48a335c-3316-4893-8bc6-fcacbf57fc4a/5b38eaa6-1ff7-462b-9f7e-e26b7d448b46 | sports | mid |
| s13 | Glyyd | https://glyyd.com/privacy/data-subject-request | sports | small |
| s14 | Luzid (now Glasslake) | https://www.luzid.io/data-subject-request | b2b-saas | small |
| s15 | Bolt | https://bolt.eu/en/privacy/data-subject/ | travel | large |
| s16 | Nav Technologies, Inc | https://www.nav.com/privacy/ccpa-request/ | finance | mid |
| s17 | Vodafone Limited (Vodafone UK) | https://www.vodafone.co.uk/forms/static/gdpr-sars | utilities | large |
| s18 | Grow Care, Inc. (Grow Therapy) | https://growtherapy.jotform.com/240836997526068 | health-fitness | mid |
| s19 | Koninklijke Philips | https://philips-privacy.my.onetrust.com/webform/415349a7-6194-4ac8-a922-31a9f8ef1b39/38e2998c-8432-4e1b-8063-a54f86824c86 | lifestyle | large |
| s20 | Transcarent, Inc. (with Accolade and 2nd.MD) | https://privacyportal.onetrust.com/webform/dbb1e0a9-5dc2-4908-9125-990fb1894729/ec6eab84-cd95-4615-8652-90f299ae2c03 | medical | mid |

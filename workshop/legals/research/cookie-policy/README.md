# cookie-policy: build record

Built 2026-10-27. Skeleton: `plugins/fatodono-founderkit/skills/legals/skeletons/cookie-policy.md`. Scope
(owner, 2026-10-27): the policy only; consent-banner text is a separate seed item.

## Files

- `candidates.md`: the pool of 30 and the reserve.
- `pool/`: raw rows from the four `pool-collector` slices.
- `samples/sNN.md`: one extraction table per sample, s01–s20.
- `merge.md`: section ids and meanings, mapping notes, section map, merged list with counts and
  median positions, patterns, document level, *Regional content*, copies, first-batch
  qualification, saturation log, changes.

## Run

- **Routes run:** R1 (App Store charts, storefronts `us` and `ie`: `charts-us`, `charts-ie`), R2
  (App Store long tail, `longtail`), R4 (company sites without an app, `web-only`). 452 raw rows.
  R3 (Play) was not run: the pool reached 30 dedicated cookie pages without it.
- **Pool:** 30 candidates, 10 large, 10 mid, 10 small; no sector above 3 of 30; 9 of 30 EU/UK-based
  (owner); group check (rule 5) and first-screen check at selection. Every candidate is a
  standalone cookie page; no rule-6 privacy page was needed.
- **First batch:** s01–s15 (c01–c15, 5 per size). All valid; none replaced.
- **Saturation:** batch 1 s16–s20 (c16–c20), all valid. Non-new in a row: s16, s17, s18, s19, s20.
  s18 was first judged new (its "the English version binds" clause became an id,
  `language-version`); under decision 44 drafting boilerplate in a notice is not a section, so
  the id was dropped and s18 is not new. No section id was added after the first batch.
- **Stop reason:** 5 non-new samples in a row, at s20: `saturated: true`. `sample_count: 20`.
  c21–c30 were not extracted.

## Invalid

None. Borderline but valid (details in `merge.md` *First-batch qualification*): s02 and s13
announce a cookie list the served page lacks; s03 is an AI-drafted text with placeholders left
in; s04 was last updated in 2020 and covers one site.

## Templates and copies

Rule 4: no copies. Three samples are whole generator texts and count as their own samples
(decision 26); none is cut down (decision 38): s06 (a widely circulated older generator cookie
policy), s08 (CookieYes, checked against CookieYes's own sample) and s09 (GetTerms, checked
against its template). s07 and s10 share a consent tool's stock category descriptions inside
their own texts. Each template's wording adds to patterns once (decision 39). s19 and s20 share
one stock UK cookie definition, nothing else.

## Size thirds

Valid samples: 7 large, 7 mid, 6 small. No size ran short; the uneven third is only where the
stop fell (s16–s20 were large, mid, small, large, mid).

## Samples

All fetched 2026-10-27, language `en`.

| Sample | Company | URL | Sector | Size |
|---|---|---|---|---|
| s01 | LinkedIn Corporation | https://www.linkedin.com/legal/cookie-policy | business | large |
| s02 | Photoroom | https://www.photoroom.com/legal/cookie-policy | photo-video | mid |
| s03 | Hot Ice Studio, LLC (Lucen) | https://lucen.app/cookie-policy | lifestyle | small |
| s04 | Klarna Bank AB | https://www.klarna.com/international/cookie-policy/ | finance | large |
| s05 | Tailscale Inc. | https://tailscale.com/cookie-notice | utilities | mid |
| s06 | Ever Accountable | https://everaccountable.com/cookie-policy/ | health-fitness | small |
| s07 | Chipotle Mexican Grill, Inc. | https://www.chipotle.com/cookie-policy | food-drink | large |
| s08 | DSSV, Inc. (brightwheel) | https://mybrightwheel.com/cookie-policy/ | education | mid |
| s09 | 4040 Media Limited (Project.co) | https://project.co/cookies-policy/ | productivity | small |
| s10 | SoundCloud Global Limited & Co KG | https://soundcloud.com/pages/cookies | music | large |
| s11 | Gametime United Inc. | https://gametime.co/policies/cookies-policy/ | entertainment | mid |
| s12 | Nifty Technologies, Inc. | https://niftypm.com/cookie-policy/ | business | small |
| s13 | Headspace Inc. | https://www.headspace.com/cookie-policy?origin=footer | health-fitness | large |
| s14 | What3Words Limited | https://what3words.com/cookies | navigation | mid |
| s15 | Journey Rewards Inc. | https://www.journey.com/cookies | travel | small |
| s16 | Dropbox, Inc. | https://help.dropbox.com/security/cookies | productivity | large |
| s17 | Suno Inc. | https://suno.com/cookie-policy | music | mid |
| s18 | Tessirion, s.r.o. (Eppika) | https://eppika.com/en/legal/cookies_policy | education | small |
| s19 | Guardian News & Media Ltd | https://www.theguardian.com/info/cookies | news | large |
| s20 | Taptap Send, Inc. | https://www.taptapsend.com/en/legal/cookie-policy-en | finance | mid |

Versions and parts taken: s01 the policy plus its linked cookie-table page (rule 6); s07 the
`en-us` default; s14 the EN version from the language switcher; s16 the help-center article that
the old `/accounts-billing/security/cookies` URL redirects to (it covers Dropbox Sign, DocSend and
FormSwift too); s18 the `/en/` version; s20 the English version, current version tab only.

## Skeleton

20 sections: 6 core (`intro`, `what-are-cookies`, `purposes`, `refusal-effects`, `consent-tool`,
`browser-controls`), 8 common (`privacy-link`, `similar-technologies`, `data-collected`,
`third-parties`, `cookie-list`, `ad-opt-outs`, `changes`, `contact`), 6 rare (`off-site-tracking`,
`retention`, `data-sharing`, `ad-framework`, `account-controls`, `device-controls`).

Of the 26 ids in `merge.md`:

- **Folded (2):** `acceptance` (2/20, visiting or using counts as agreeing) into `intro` as a
  pattern, since no fact decides it (`skeleton-format.md`, rare drafting section); `security`
  (1/20, a generated checklist only) into `privacy-link`, since the privacy policy's `security`
  section carries it.
- **Out of the root (4):** `legal-basis`, `transfers`, `sale-share`, `opt-out-signals`: their whole
  content is what one law requires (*Regional content* below).

## Relation to the privacy policy

`skeletons/privacy-policy.md` has a `cookies` section (24/32) and a `signals` section; 4/24 of
those privacy policies point to a separate cookie policy instead. When a product gets both
documents, the writer should make the privacy policy's `cookies` section a short summary plus a
pointer, and keep the cookie policy's `privacy-link` pointing back. Both read
`facts.data.tracking`, so the trackers named match.

## Facts

Four keys added to `helpers/facts-schema.md`: `facts.data.cookie_controls` (consent tool, settings link,
app and account paths, per-category choice, default for non-essential trackers),
`facts.data.cookie_list` (where the item-level list lives and how it is kept current),
`facts.data.ad_consent_frameworks` (IAB TCF / GPP) and `facts.product.offsite_components`
(plugins, widgets, sign-in buttons, tags or SDKs that set the company's cookies on other sites).

One existing key extended: `facts.data.tracking` gains four optional fields (`names`, `party`,
`duration`, `opt_out_url`) for the cookie list and the ad opt-outs. The first four fields and
their meaning are unchanged, so the privacy policy and the store forms read it as before.

Reused: `facts.data.tracking`, `facts.data.purposes`, `facts.data.collected`,
`facts.data.retention`, `facts.data.targeted_ads`, `facts.data.other_recipients`,
`facts.data.deidentified_use`, `facts.processors.list`, `facts.product.services_in_scope`,
`facts.product.name`, `facts.product.has_accounts`, `facts.company.*` (legal name, address,
published policies, change notice, contact email, phone, DPO). `tools/check-facts` exits 0.

## Regional content: what blocks would get

No region block was written (owner's instruction). Counts are over the 20 samples; rows and
sample ids are in `merge.md` *Regional content*.

| Region | Samples carrying it | What its block would hold | Keys it would read | Block warranted? |
|---|---|---|---|---|
| us | 9/20 (s01 s03 s05 s07 s11 s15 s16 s17 s19) | `sale-share` (8/20): whether cookie data is sold or shared for cross-context ads, and the "Do Not Sell or Share" / "Your Privacy Choices" link or banner button (in `consent-tool` for 7 samples); `opt-out-signals` (6/20): GPC honoured (5), Do Not Track stance (2); a no-sale statement (2) | `facts.us.sells_or_shares`, `facts.data.sells`, `facts.data.honors_gpc`, `facts.data.honors_dnt`, `facts.data.targeted_ads` | **Yes.** The most common regional content, consistent across samples, and every key already exists (the privacy policy's `us` block uses them). Cheap to build from the existing samples' tagged rows. |
| eu | about 10/20 (s01 s02 s03 s04 s10 s12 s14 s15 s18 s20; s17 untagged) | Consent before non-essential cookies, banner choices, withdrawal at any time (8); `legal-basis` (2: consent, legitimate interest with a balancing test); controller identity and DPO (2); `transfers` (1 tagged, 1 untagged); consent records (1); what does not count as consent (1) | `facts.data.cookie_controls` (`non_essential_default`), `facts.data.purposes` (legal basis), `facts.company.legal_name`, `facts.company.address`, `facts.company.dpo_contact`, `facts.eu.transfer_mechanisms` | **Yes, but sample it.** Prior consent is the reason most EU companies publish a cookie policy, so the block matters more than its count suggests. But beyond the consent mechanics the content is thin (legal basis 2, transfers 1–2): an `eu` region run, with EU-based samples, should set it rather than these 10 rows. |
| uk | 3/20 (s01 s03 s19) | The same consent content under PECR and UK GDPR; objecting to legitimate-interest ad cookies (1, untagged) | as `eu`, with `facts.uk.transfer_mechanisms` | **Probably, as a mirror of `eu`.** Too few samples to stand alone (two UK-based samples, s09 and s14, carry no tagged UK content). Build it in the same run as `eu`, or defer it. |
| fr | 1/20 (s02) | Consent choice kept for 6 months (CNIL guidance) | — | No: one sample; at most a pattern note in a later `eu` block. |
| au | 1/20 (s19, untagged) | Opt-out of personalised ads for Australian residents | — | No. |

IAB TCF (`ad-framework`, 2/20) is an industry framework, not a law, so it stays in the root.

## Proposed catalog row

Not added to `helpers/catalog.md` (owner's to add):

| Id | Title | Kind | Family | Trigger question | Skeleton |
|---|---|---|---|---|---|
| cookie-policy | Cookie Policy | document | privacy-notices | Does the product's website or web app set cookies or similar trackers beyond strictly necessary ones (analytics, ads, session replay, embedded videos or social widgets)? Answer from `facts.data.tracking`. With strictly necessary cookies only, or for an app with no website, the privacy policy's cookies section is enough, so say so rather than writing one. | `skeletons/cookie-policy.md` |

## Open for the owner

- **Region blocks.** The table above recommends `us` now, `eu` from its own region run, and `uk`
  with `eu` or later. Which ones to build, and when?
- **Trigger scope.** The proposed trigger skips sites with only strictly necessary cookies and
  app-only products. 7 of 20 samples cover apps too (SDKs, ad identifiers), but no sample is
  app-only. Should an app with ad or analytics SDKs and no website also get a cookie policy?
- **`facts.data.tracking` extended.** Four optional fields were added to a shared key instead of
  a new inventory key. If you prefer to keep the key as it was, the alternative is a separate
  `facts.data.cookie_inventory`.
- **Folded ids.** `acceptance` (implied consent by use, 2/20) is only a pattern in `intro`; since
  most regimes that require consent reject implied consent, the writer should not use it unless
  the user asks. `security` (1/20) is folded into `privacy-link`. Keep both decisions?
- **Banner text.** `facts.data.cookie_controls` already describes the banner (tool, link label,
  per-category choice, default). The separate banner item can reuse it.

## Lessons

- **Cookie pages are short and generic.** The median is about 920 words, and the two most common
  sections after the opening (`what-are-cookies`, `browser-controls`) are textbook text that says
  nothing about the company. The skeleton's value is in `purposes`, `cookie-list` and
  `consent-tool`, which most samples write thinly.
- **Lists are often missing.** 9 of 20 have no usable item-level list (7 none, 2 announced but
  absent), and 4 leave it to the consent tool. The skeleton tells the writer to give the list or
  the pointer, never a promise of one.
- **The section list was stable from the first batch.** The only id added in saturation was
  boilerplate (decision 44); every other sample mapped onto the first batch's 26 ids.

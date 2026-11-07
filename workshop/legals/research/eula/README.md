# eula: build record

Built 2026-10-27. Skeleton: `plugins/fatodono-launchkit/skills/legals/skeletons/eula.md`.

## Files

- `candidates.md`: the pool of 30 and the reserve.
- `pool/`: raw rows from the four `pool-collector` slices.
- `samples/sNN.md`: one extraction table per sample; s12, s14 and s17 are kept, marked invalid in
  their front matter.
- `merge.md`: section ids and meanings, first-batch qualification, saturation log, merged list
  with counts and median positions, section map, document level, *Regional content*, changes.

## Run

- **Routes run:** R1 (US App Store charts, `charts-ios`), R2 (App Store long tail, `longtail-ios`
  and `longtail-2`), R4 (desktop software sites, `desktop`). 74 raw rows. R3 (Play) was not run:
  Play listings show no licence agreement link, and the pool reached 30 without it.
- **Pool:** 30 candidates, 10 large, 10 mid, 10 small; no sector above 5 of 30; group check (rule
  5) at selection. Most store apps link Apple's standard EULA, so custom EULAs come mostly from
  desktop software (R4).
- **First batch:** s01–s11, s13, s15, s23, s24 (5 per size). s12 and s14 were dropped under
  decision 42 and replaced by s24 and s23.
- **Saturation:** batch 1 s16–s22 (s17, s20, s21 invalid), batch 2 s25–s29 (s25, s26 invalid).
  Non-new in a row: s16, s18, s19, s22, s27. No section id was added after the first batch.
- **Stop reason:** 5 non-new samples in a row, at s27: `saturated: true`. s28 and s29 came in the
  same batch and are kept and counted. `sample_count: 22`.

## Invalid

| Sample | Company | Why |
|---|---|---|
| s12 | Boards.com | terms of use served at `/terms/eula` (decision 42); replaced by s24 |
| s14 | iMemories | terms and conditions served at `/terms/eula` (decision 42); replaced by s23 |
| s17 | MacroFactor | terms of service; grants access to services, not a licence for installed software (decision 42) |
| s20 | TrapCall | rule 5 and decision 42; not extracted |
| s21 | Flashka | rule 5 and decision 42; not extracted |
| s25 | Vimeo | `vimeo.com/eula` is a user profile named "eula", not a document; no extraction file |
| s26 | Todoist | the candidate URL is the terms of service (decision 42); no extraction file |

## Templates and copies

Rule 4: no copies. s06 follows Apple's Standard Licensed Application EULA and s15 the TermsFeed
EULA generator; their texts differ, so both count. s24 carries s15's TermsFeed wording with parts
removed plus its own consumer-law preamble: it counts for prevalence, and its template sections
add no patterns beyond s15's (decisions 38–39).

## Size thirds

The pool held 10 per size. Valid samples: 9 large, 6 mid, 7 small. Mid lost four candidates (s14,
s17 and s26 were terms of use or service, s20 fell to rule 5) and small lost two (s12, s21), so the
judged samples lean large. No size ran short in the pool; the gap comes from decision 42.

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | LinkedIn Corporation | https://www.linkedin.com/legal/eula | business | large | en | 2026-10-27 |
| s02 | Sketch B.V. | https://www.sketch.com/eula/ | graphics-design | mid | en | 2026-10-27 |
| s03 | Sublime HQ Pty Ltd | https://www.sublimehq.com/eula | developer-tools | small | en | 2026-10-27 |
| s04 | Gen Digital Inc. (Norton) | https://us.norton.com/legal/lsa | utilities | large | en | 2026-10-27 |
| s05 | Ableton AG | https://www.ableton.com/en/eula/ | music | mid | en | 2026-10-27 |
| s06 | Good.iWare, Inc. (GoodReader) | https://goodreader.com/end-user-license-agreement | productivity | small | en | 2026-10-27 |
| s07 | Wondershare Technology (Filmora) | https://www.wondershare.com/company/end-user-license-agreement.html | photo-video | large | en | 2026-10-27 |
| s08 | Hex-Rays SA (IDA Pro) | https://hex-rays.com/eula | developer-tools | mid | en | 2026-10-27 |
| s09 | Moodworks Inc. (Shmoody) | https://www.shmoody.com/terms-and-conditions | health-fitness | small | en | 2026-10-27 |
| s10 | Dolby Laboratories, Inc. (Dolby On) | https://www.dolby.com/about/legal/dolby-on-terms-of-use/ | music | large | en | 2026-10-27 |
| s11 | Omni Development, Inc. (OmniFocus) | https://www.omnigroup.com/legal/eula | productivity | mid | en | 2026-10-27 |
| s13 | Broadcom Inc. (VMware Fusion / Workstation) | https://docs.broadcom.com/doc/end-user-agreement-english | developer-tools | large | en | 2026-10-27 |
| s15 | Twopeople Software LLC (Mate) | https://matetranslate.com/en/eula | reference | small | en | 2026-10-27 |
| s16 | AO Kaspersky Lab | https://products.s.kaspersky-labs.com/homeuser/Kaspersky4Win2021/21.27.6.532/english-INT-0.22.0/1347c7f21ac043e6b8c68f98c2253eed/kis_eula_en.txt | utilities | large | en | 2026-10-27 |
| s18 | Cockos Incorporated (REAPER) | https://www.reaper.fm/license.txt | music | small | en | 2026-10-27 |
| s19 | Corel Corporation (CorelDRAW) | https://www.corel.com/en/eula/ + https://www.corel.com/en/eula/licensing-terms/ | graphics-design | large | en | 2026-10-27 |
| s22 | TeamViewer Germany GmbH | https://www.teamviewer.com/en/legal/eula/ | business | large | en | 2026-10-27 |
| s23 | Maxon Computer GmbH (Cinema 4D) | https://www.maxon.net/en/legal/eula | graphics-design | mid | en | 2026-10-27 |
| s24 | MTW Labs (CleanShot X) | https://cleanshot.com/eula | utilities | small | en | 2026-10-27 |
| s27 | XK72 Limited (Charles) | https://www.charlesproxy.com/eula/ | developer-tools | small | en | 2026-10-27 |
| s28 | Malwarebytes Inc. | https://www.malwarebytes.com/eula | utilities | large | en | 2026-10-27 |
| s29 | MobiSystems, Inc. (OfficeSuite) | https://mobisystems-storage.mobisystems.com/officesuite/android/eula/mobiroo/en/EULA.html | business | mid | en | 2026-10-27 |

Versions and parts taken: s04 the Americas English version; s07 the base EULA, the generative-AI
addendum and the Filmora addendum (other product addenda left out); s13 the Foundation Agreement
and Software Module §§ 1–7 (hardware, SaaS and services modules left out); s16 the global English
non-GDPR edition from the product CDN; s19 the hub plus the CorelDRAW specific terms; s22 parts A,
B and E (C hardware and D professional services are other contract modules); s29 the English file
the Android build links.

## How an EULA differs from a terms of service

The EULA licenses a copy of software; the terms of service govern use of a service. In the
samples this shows as:

- **Sections the ToS skeleton has no id for:** `restrictions` (22/22) as its own section,
  `transfer` (13/22), `special-licences` (13/22), `updates` (18/22, core), `support` (16/22),
  `third-party-components` (10/22), `telemetry` (12/22), `ip-claims` (9/22), `activation`
  (7/22), `system-requirements` (6/22), `online-services` (5/22), `bundled-content` (4/22),
  `data-after-end` (4/22), `audit` (4/22).
- **Weaker in the EULA:** `account` (8/22, rare; ToS 23/30), `user-content` (7/22; ToS 23/30),
  `acceptable-use` (10/22; ToS 28/30), `indemnity` (13/22; ToS 28/30), `dispute-resolution`
  (12/22; ToS 24/30). Content moderation, promotions, dealings between users and account closure
  do not appear at all; copyright complaints appear once, as US DMCA text.
- **Warranty:** 7/21 give a limited positive warranty (works as documented for N days, with a
  fix, replace or refund remedy); the ToS samples give one in 1/30.
- **Termination:** ends with a duty to delete every copy (about 12/21), sometimes certified,
  rather than with account closure.

## Overlap with terms-of-service

These EULA sections cover the same kind of fact as a section of
`skeletons/terms-of-service.md`. They stay in the EULA skeleton, because an EULA must stand alone
(it is shown in an installer or a store listing without the terms). When a product ships both
documents, the writer should align them: the same facts feed both (`facts.company.governing_law`,
`facts.company.dispute_forum`, `facts.company.liability_cap`, `facts.company.change_notice`,
`facts.sales.*`), so the values match; the wording, caps style and section names should match too,
and neither document should contradict the other on forum, cap or refunds.

| EULA section | ToS section | Note for the writer |
|---|---|---|
| intro | intro | EULA adds "licensed, not sold" and install-time acceptance. |
| incorporated-terms | incorporated-terms | When both exist, the EULA can name the ToS for the online service (s01 does). |
| eligibility | eligibility | Same minimum age and organisation rule. |
| account | account | Keep identical; the EULA version is shorter. |
| licence-grant | licence | ToS `licence` covers the service; EULA's is the core. Make the app licence in the ToS a pointer to, or a copy of, the EULA grant. |
| restrictions | licence, acceptable-use | ToS folds software restrictions into `licence`; keep the lists the same. |
| company-ip | company-ip | Same. |
| beta-features | beta-features | Same. |
| fees-payment | fees-payment | Same values; the EULA adds licence-conditional-on-payment. |
| subscriptions | subscriptions | Same renewal and cancel terms (also in `subscription-terms` when separate). |
| refunds | refunds | Same rule (also in `refund-policy`). |
| app-stores | app-stores | Same Apple-required clauses; write them once per document, not differently. |
| feature-terms | feature-terms | Same feature list. |
| feedback | feedback | Same. |
| acceptable-use | acceptable-use | ToS is the full version; the EULA can be shorter but must not allow more. |
| user-content | user-content | Same ownership and licence-back terms. |
| ai-features | ai-features | Same. |
| communications | communications | Same. |
| privacy | privacy | Same pointer. |
| third-party-services | third-party-services | Same. |
| software-changes | service-changes | Same right to change; the EULA adds discontinued-product terms for perpetual licences. |
| terms-changes | terms-changes | Same notice rule, unless the EULA binds only per version. |
| termination | termination | Licence end versus account end; the EULA adds delete-all-copies. |
| data-after-end | account-closure | Same deletion timing. |
| warranty | disclaimers | Same disclaimer; the EULA may add a limited warranty. |
| liability | liability | Same cap. |
| indemnity | indemnity | Same. |
| export-sanctions | export-sanctions | Same. |
| dispute-resolution | dispute-resolution | Same forum; a conflict here is the most harmful mismatch. |
| governing-law | governing-law | Same law and courts. |
| general | general | Same. |
| contact | contact | Same. |

EULA-only sections (no ToS id): `special-licences`, `activation`, `system-requirements`, `updates`,
`transfer`, `support`, `online-services`, `third-party-components`, `telemetry`, `ip-claims`,
`audit`, `bundled-content`.

## Facts

Ten keys added to `helpers/facts-schema.md`: `facts.product.eula_acceptance`,
`facts.product.licence_terms`, `facts.product.activation`, `facts.product.system_requirements`,
`facts.product.update_policy`, `facts.product.third_party_components`, `facts.product.support`,
`facts.product.bundled_content`, `facts.product.software_warranty`,
`facts.data.telemetry_controls`. Every other key the skeleton names already existed.

## Open for the owner

- **No catalog row.** `helpers/catalog.md` has no `eula` row yet; the skeleton takes `family: terms` by
  analogy with the terms of service. The row (trigger question, family) is the owner's to add.
- **`copyright-complaints` out of the root.** Its only sample (s10) is the US DMCA procedure, so it
  went to *Regional content* (`us`) instead of a rare root section.
- **Standalone versus pointer.** The skeleton repeats every overlapping section, as asked. One
  sample (s01) instead sends the service and its rules to the main terms (the User Agreement). If the write branch
  should let a product with both documents write the overlap as pointers, that is a write-branch
  rule, not a skeleton change.
- **Order by median.** `bundled-content`, `ai-features` and `feature-terms` land near the end
  because two of their four or five samples carry them in addenda. The skeleton follows the median
  as `build.md` says; a writer may prefer them after `restrictions`.
- **Large-company lean.** 9 of 22 valid samples are large (see *Size thirds*); B2B samples (s13,
  s22) bring `audit`, confidentiality and order-of-precedence content that small apps rarely need.
  Their sections stay rare or common by count.

## Lessons

- **"EULA" links lead to many documents.** 6 of the 30 candidates (s12, s14, s17, s21, s25, s26)
  were terms of use or service, or not a document at all. Store-app EULAs are mostly Apple's
  standard text, so custom ones come from desktop software; a future pool should weight R4 desktop
  slices more and check the page title before selection.
- **Section count was stable from the first batch.** No id was added after s15's batch; every later
  sample mapped onto the 45 ids, which is why saturation came quickly once the qualification rule
  (decision 42) was settled.

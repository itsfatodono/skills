# account-deletion: merged section list

Formats: prose, list, table. Layout marks: pointer (links to a separate page), embedded (folded
into another section or a step). Help-center chrome (related-article lists, a site-wide "Still
need help?" box, feedback widgets) is not a section; it is noted at the document level.

## Section ids (fixed before judging, 2026-10-26)

| Id | Title | Means |
|---|---|---|
| intro | About this page | a distinct opening: what the page explains, which app or accounts, what deletion means, sometimes framed as the user's right |
| alternatives | Alternatives to deleting | downgrade, deactivate, change a setting, sign out, or contact support instead of deleting |
| before-you-delete | Before you delete | data export or access copy, and prerequisites (uninstall from managed devices, sign in, clear balances) |
| subscriptions | Subscriptions and payments | deletion does not cancel store subscriptions, cancel first, refunds, balances, lost purchases' billing |
| self-service-steps | How to delete | in-product deletion steps, in the app and/or on the web |
| request-route | Request deletion without the app | email, web form or support route, incl. for users who cannot sign in; what to include |
| confirmation | Verification and confirmation | identity checks, email confirmation link, typed confirmation, completion email, what to do when it fails |
| what-is-deleted | What is deleted | data and content removed, what the user loses, irreversibility |
| timeline | When it happens | processing time, grace period and reactivation, re-using the email or phone afterwards |
| retention | What we keep | backups, legal or security retention, de-identified data, local device data, third-party records, situations where deletion is refused |
| shared-content | Content shared with others | public content, groups, households and what remains after deletion |
| other-accounts | Other account types and linked accounts | business/organisation/admin accounts, secondary roles or profiles, partner accounts, sister products, deceased users |
| partial-deletion | Deleting part of your data | deleting individual items (chats, backups) or correcting data without closing the account |
| contact | Contact | a page-specific contact line for questions |
| ai-training | Model training | whether the user's content was or is used to train AI models |
| inactivity | Automatic deletion | the account is deleted automatically after a period of inactivity (added at s20) |

Note (at s16): a lost-access route or a password-reset pointer for users who cannot sign in maps
to request-route; a confirmation that fails or never arrives maps to confirmation.

## First batch (s01–s15)

| Id | Count | Formats | Samples |
|---|---|---|---|
| self-service-steps | 13/15 | prose, list, embedded | s01 s02 s03 s04 s05 s07 s08 s09 s10 s11 s13 s14 s15 |
| what-is-deleted | 12/15 | prose, list, embedded | s01 s02 s04 s05 s06 s07 s08 s09 s10(emb) s11 s13 s14 |
| intro | 9/15 | prose | s02 s04 s06 s09 s11 s12 s13 s14 s15 |
| subscriptions | 9/15 | prose, list | s02 s04 s06 s07 s08 s09 s10 s11 s13 |
| request-route | 9/15 | prose, list, pointer | s02 s04 s05 s06 s09 s11 s12 s13 s15 |
| confirmation | 9/15 | prose, list, embedded | s04 s06(emb) s07(emb) s08(emb) s09 s10 s12 s13 s14 |
| other-accounts | 8/15 | prose, list, pointer | s02 s03 s04 s08 s10 s11 s13 s14 |
| timeline | 7/15 | prose, list, embedded | s01 s06 s07(emb) s08(emb) s10 s13 s15(emb) |
| before-you-delete | 6/15 | prose, list, pointer, embedded | s02 s04 s07 s08 s09(ptr) s11(emb) |
| alternatives | 5/15 | prose, list, embedded | s01 s02(emb) s08(emb) s10 s13 |
| retention | 5/15 | prose, list, pointer, embedded | s06 s11(ptr) s12 s13 s15 |
| shared-content | 3/15 | prose, list, embedded | s04 s09(emb) s11 |
| partial-deletion | 3/15 | prose, pointer | s12 s13 s15 |
| contact | 2/15 | prose | s06 s15 |
| ai-training | 1/15 | prose | s13 |

Mapping notes:
- s02 r6 ("Please note" bullets): cancel subscription and refunds → subscriptions; "contact support
  instead of deleting for technical issues" → alternatives (embedded).
- s04 r7 (spam-folder tip) and s13 r9/r19 (flow fails, error message) → confirmation.
- s04 r8 (duplicate accounts) and r12 (linked developer community account) → other-accounts.
- s05 r4 and s13 r20 are help-center contact boxes (chrome), not contact.
- s07 r1 is a title only; s01 opens with alternatives, s10 with the delete/deactivate choice:
  no intro for those three.
- s10 r3 (business balances) → subscriptions and other-accounts; r12 (deceased user) → other-accounts.
- s12 r5 (deletion refused: open support case, suspected abuse) → retention (list).
- s13 r14, r15, r17 (email and phone reuse, no reactivation) → timeline; r16, r18 → alternatives.
- s15 r2 names the email route only in the intro sentence → request-route (prose).
- Privacy-policy links (s06, s07, s11, s12) are a document-level recurring element.

## Saturation judgements

In pool order, from s16. "Streak" counts non-new samples in a row.

| Sample | Ids found (format) | New? | Streak |
|---|---|---|---|
| s16 Vinted | self-service-steps (list), before-you-delete (emb), timeline (prose), retention (prose), request-route (prose), confirmation (emb), what-is-deleted (list) | no | 1 |
| s17 Polarsteps | intro (prose), self-service-steps (list), request-route (pointer, password reset), contact (prose, with exit feedback) | no | 2 |
| s18 PlanWiz | what-is-deleted (list), subscriptions (emb), self-service-steps (list), request-route (list, request form) | no | 3 |
| s19 Snap | timeline (prose), self-service-steps (list), request-route (prose, password reset), retention (prose), before-you-delete (prose, download window) | no | 4 |
| s20 Telegram | self-service-steps (prose), what-is-deleted (prose), shared-content (prose), confirmation (prose), alternatives (emb), timeline (prose), **inactivity (prose)**, partial-deletion (**list**) | yes: new section `inactivity`; new format list for partial-deletion | 0 |
| s21 Critique AI | request-route (prose) | no | 1 |
| s22 Fiverr | alternatives (prose, list), before-you-delete (list), subscriptions (emb, balance), timeline (prose), self-service-steps (list), what-is-deleted (prose), request-route (emb), shared-content (list, FAQ) | no | 2 |
| s23 Feedly | what-is-deleted (prose), self-service-steps (list), timeline (prose, re-login), contact (prose) | no | 3 |
| s24 LangX | intro (prose), self-service-steps (list), timeline (prose), what-is-deleted (emb), retention (list), before-you-delete (prose), partial-deletion (list), subscriptions (prose), request-route (list), confirmation (emb) | no | 4 |
| s25 Life360 | what-is-deleted (prose), self-service-steps (list), confirmation (emb), other-accounts (prose), subscriptions (prose) | no | 5 |

Stop: saturated after s25 (s21–s25 non-new). `sample_count: 25`. No copies (rule 4): no two
tables share headings, order and quotes. s22's text is published under three article ids at
the same company; it was extracted once.

## Final merge (s01–s25)

| Id | Count | Tier | Formats | Samples |
|---|---|---|---|---|
| self-service-steps | 22/25 | core | prose, list, embedded | s01 s02 s03 s04 s05 s07 s08 s09 s10 s11 s13 s14 s15 s16 s17 s18 s19 s20 s22 s23 s24 s25 |
| what-is-deleted | 19/25 | common | prose, list, embedded | s01 s02 s04 s05 s06 s07 s08 s09 s10(emb) s11 s13 s14 s16 s18 s20 s22 s23 s24(emb) s25 |
| request-route | 16/25 | common | prose, list, pointer, embedded | s02 s04 s05 s06 s09 s11 s12 s13 s15 s16 s17(ptr) s18 s19 s21 s22(emb) s24 |
| subscriptions | 13/25 | common | prose, list, embedded | s02 s04 s06 s07 s08 s09 s10 s11 s13 s18(emb) s22(emb) s24 s25 |
| timeline | 13/25 | common | prose, list, embedded | s01 s06 s07(emb) s08(emb) s10 s13 s15(emb) s16 s19 s20 s22 s23 s24 |
| confirmation | 13/25 | common | prose, list, embedded | s04 s06(emb) s07(emb) s08(emb) s09 s10 s12 s13 s14 s16(emb) s20 s24(emb) s25(emb) |
| intro | 11/25 | common | prose | s02 s04 s06 s09 s11 s12 s13 s14 s15 s17 s24 |
| before-you-delete | 10/25 | common | prose, list, pointer, embedded | s02 s04 s07 s08 s09(ptr) s11(emb) s16(emb) s19 s22 s24 |
| other-accounts | 9/25 | rare | prose, list, pointer | s02 s03 s04 s08 s10 s11 s13 s14 s25 |
| retention | 8/25 | rare | prose, list, pointer, embedded | s06 s11(ptr) s12 s13 s15 s16 s19 s24 |
| alternatives | 7/25 | rare | prose, list, embedded | s01 s02(emb) s08(emb) s10 s13 s20(emb) s22 |
| shared-content | 5/25 | rare | prose, list, embedded | s04 s09(emb) s11 s20 s22 |
| partial-deletion | 5/25 | rare | prose, list, pointer | s12 s13 s15 s20 s24 |
| contact | 4/25 | rare | prose | s06 s15 s17 s23 |
| ai-training | 1/25 | rare | prose | s13 |
| inactivity | 1/25 | rare | prose | s20 |

Skeleton decisions:
- `contact` is a rare drafting section that no fact decides: folded into `request-route` as a
  pattern. `ai-training` (1/25) is folded into `retention` as a pattern.
- Order: warnings and choices first (intro, alternatives, what-is-deleted, before-you-delete,
  subscriptions), then the routes (self-service-steps, confirmation, request-route), then what
  follows (timeline, retention, shared-content), then special cases (other-accounts,
  partial-deletion, inactivity). Estimated from where each id sits in the tables, not computed
  as an exact median.

## Document level (s01–s25)

- Kind of page: help-center article 16/25; dedicated standalone page 7/25 (s06 s08 s12 s15 s18
  s21 s24; six of them small companies); part of a larger page 2/25 (s14, s20).
- Words: median 306, range 36–1,465.
- Title phrased as the user's question: 8/25 (s03 s04 s05 s07 s17 s19 s20 s23).
- Per-platform split (tabs, toggles or subheadings): 7/25 (s04 s10 s13 s16 s17 s19 s22); the
  rest give one path for all platforms.
- Covers deletion together with deactivation (s10 s16 s19 s22) or data access (s02 s07).
- Date visible to readers: 7/25 certain (s03 s04 s05 s06 s13 s23 s24); s19 and s25 carry one in
  the help-center metadata.
- Privacy-policy link in the body: 8/25 (s02 s06 s07 s11 s12 s16 s17 s19).
- Support email named on the page: 11/25.
- Deletion possible without the app (web self-service or a contact route): 23/25; web
  self-service 13/25; email request as the only route 3/25 (s06 s12 s21).
- Help-center chrome (related articles, "Still need help?", feedback widget) on most
  help-center articles; not extracted as sections.

## Regional content

- s10 r2: one US state's residents must contact support before reactivating (`us`).
- s12 r6: a Data Protection Officer contact for partial correction or deletion (`eu`).
- s19 r2, r8: one country (India) gets a longer deletion period and download window, "in
  adherence with local guidelines" (no region folder yet).

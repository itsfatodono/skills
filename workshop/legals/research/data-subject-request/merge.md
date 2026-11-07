# data-subject-request (root): merged section list

First batch: s01–s15 (6 large, 5 mid, 4 small). s01–s12 are c01–c12 in pool order; the top-up
is s13 = c22 Glyyd (small), s14 = c23 Luzid (small), s15 = c13 Bolt (large), per `candidates.md`
(`035634b`; only 2 small tail rows were valid, so the third slot fell back to c13). All 15 are
valid; none was replaced. The top-up added no id. The *Section ids* list was written before
the saturation batch (`build/build.md` step 3). Saturation batch 1 (s16–s20) is judged under
*Saturation* and folded into the counts below. It added 2 ids, both regional-only (`appeal` from
s18, `non-discrimination` from s20). By owner decision it was the last batch, so the build ends
at 20 samples with `saturated: false`. Each meaning below is fixed from here: change one only with a
dated note under *Changes*. One sample row can map to more than one id when it gives more than
one kind of fact (s08 §1 gives `intro`, `eligibility`, `contact`, `privacy-link` and
`verification`).

The document is the form or portal page a person uses to send a data-protection rights request
(PLAN.md decision 49). An id is one kind of fact the page gives or asks for. A field group counts
as a section when it asks for one kind of fact (who you are, what you want, where you live); the
field labels are its "heading". This is a region-neutral root: content one law requires is
recorded under *Regional content* and left out of the root, wherever the sample put it.

**Final id list: 27 ids** in *Section ids* (23 root ids and 4 regional-only ids, marked
*(regional)*). The `tr` block maps its samples against these ids: a `tr` section that fits a
root id is a regional addition to that id; content that fits none is a new `tr` section. The
skeleton folds 3 rare root ids into others (`steps` into `intro`, `fees-refusal` into
`timeline`, `response-method` into `confirmation`; see *Changes*). The ids stay here, so the
`tr` helper can still map to them.

## Section ids

| Id | Meaning | First-batch samples |
|---|---|---|
| intro | Opening: what the form or portal is for, the rights framing ("rights you may have under applicable law"), and that rights depend on where the person lives. | s01 s02 s03 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 |
| eligibility | Who may use this form and who may not: residency or region limits, an age floor, groups the form does not cover, and where those left out go instead. | s03 s06 s08 s10 s12 |
| privacy-link | Pointer to the privacy notice or policy for how data is used and which rights exist, including what the company holds in general. | s01 s02 s03 s04 s05 s06 s07 s08 s09 s10 s12 s13 |
| contact | How to reach the company or its privacy team with questions about a request: email, phone with hours, postal address, legal entity, DPO or privacy officer. | s04 s05 s08 s11 s12 |
| steps | How to fill in and send the form, or what to have ready before starting. | s03 s07 s12 |
| data-use | How the details given in the form are used and protected: only to verify, locate data and answer; who processes them; who runs the portal. | s03 s04 s05 s06 s07 s09 s11 |
| verification | How the requester's identity is checked: email link, account sign-in, matching against records, references from past use, ID documents or a signed declaration, and what happens if it fails. | s01 s02 s03 s04 s05 s06 s07 s08 s10 s11 s12 s13 s14 s15 |
| other-routes | Requests or choices this form does not take and where they go: customer service, other forms, in-app or account settings, cookie preferences, device settings, help centre. | s01 s02 s04 s06 s07 s08 s10 s12 |
| handler | Which entity or team receives and answers the request: the company's privacy team, an affiliate for some products, affiliates with their own policies, the vendor that runs the portal. | s01 s04 s07 s12 s15 |
| representative | Requests made for someone else: whether the form takes them (agent, parent for a minor, other relationship), the representative's details, and the proof of authority asked for. | s03 s05 s06 s08 s10 s11 s13 |
| requester-type | The person's relationship to the company (customer, account holder or not, employee or applicant, other), asked as a field. | s04 s05 s07 s08 s09 s11 s12 s13 s14 s15 |
| residence | The person's country, state or province, asked as a field, often deciding which requests appear. | s03 s04 s06 s08 s09 s12 s13 s14 s15 |
| identity-fields | The person's identifying and contact details asked in the form: name, email, phone, address, date of birth, account or product identifiers, past identifiers. | s01–s15 |
| request-types | Which requests the form takes and how the person picks one: the menu or list of rights, single or several choices, glosses per option, or a form fixed to one request. | s01–s15 |
| request-details | Details of the request itself: free-text description, which data or which correction, a date range, the request date, fields specific to one request type. | s01 s02 s04 s05 s06 s07 s08 s09 s11 s12 s13 s14 s15 |
| request-effects | What a given request does or returns and its limits: what deletion keeps and ends, what access returns, what an opt-out stops and what continues. | s04 s07 s10 s12 |
| timeline | How long the company takes to answer or carry out the request, when the clock starts, extensions. | s02 s03 s06 s07 s09 s12 |
| status | Checking an earlier request, and what happens when one is already open (duplicates blocked). | s01 s04 |
| alt-channels | Other ways to send the same request or its documents, or to carry it out without the form: in the app (request or self-service tools), by email, to the DPO when the form or the inbox fails. | s01 s02 s06 s10 s13 s15 |
| fees-refusal | Whether a request costs anything and when it may be refused (unfounded, excessive), with reasons given. | s09 |
| attestation | The requester's statement that the details are true and that they are the person or are authorised (checkbox, submit-means-confirm, signed declaration). | s03 s04 s05 s06 s08 s10 s14 |
| confirmation | What happens right after sending: confirmation screen or email, request reference, review and reply by email, status messages through the request's life. | s01 s02 s04 s06 s07 s08 s11 s12 s13 s14 s15 |
| response-method | How the person wants the answer sent (channel such as email or post, or the language of the reply), asked as a field. | s05 s15 |
| sale-status *(regional)* | Whether the company sells personal data, stated on the form. | s02 |
| opt-out-signals *(regional)* | Whether browser opt-out signals (GPC) are honoured and how far they reach. | s12 |
| appeal *(regional)* | What the person can do when the company declines a request or they disagree with the answer: an appeal to the company, how and where. Added from s18 in saturation batch 1; s08's appeal request type re-mapped to it. | (s08) |
| non-discrimination *(regional)* | That the person will not be treated worse for using their rights. Added from s20 in saturation batch 1. | — |

Not sections (document level, step 4): submit and "Continue" buttons (s01 §8, s03 §11, s07 §17,
s08 §13, s10 §13, s12 §23); captchas and honeypots (s07 §15, the reCAPTCHA in s03, s05, s08, s11,
s12, s09's hidden field); step headings with no text; language switchers; "Powered by OneTrust";
"required field" markers; site chrome (s02's banking-partner footer, s07's menus). s05's
version stamp in the page title is a document-level element. No drafting boilerplate of the
kind decision 44 names turned up.

## Mapping notes

- s01: §1 to `intro` and `handler` (routed to the privacy team), §2 (a transport affiliate may
  answer) to `handler`; §3 to `privacy-link` and `other-routes` (other rights via the notice); the
  email help text in §4 to `verification`; §5's one-line glosses are a pattern of `request-types`,
  not `request-effects`; §6 (correction categories) to `request-details`; §7 to `other-routes`;
  §9 (booking reference) to `verification`; §10's DPO fallback to `confirmation` and
  `alt-channels`; §11 to `status` (active request exists) and `alt-channels` (failure → DPO). The
  bundle's US and China variants are not sections (the extractor recorded them for region runs);
  they appear under *Regional content*.
- s02: §1 (title names the CCPA) to `intro` with a regional row; §2 to `intro`, `timeline` ("as
  soon as possible") and `alt-channels` (in-app request); §5 to `request-details` and
  `other-routes` (correction sent to support); §6 to `verification`; §7 splits into `sale-status`
  (regional) and `privacy-link` (a consent line that links the privacy policy and terms; see
  *Patterns*); §8 to `confirmation`.
- s03: §1 to `intro`, `eligibility` (US states listed) and `privacy-link`; §2 to `privacy-link`
  and `data-use`; §3 to `verification` (matching by identifier) and `timeline`; §4 and §7 to
  `representative`; §5 to `steps`; §6 to `identity-fields` and `residence`; §9 to
  `verification`; §10 to `attestation`.
- s04: §2 to `other-routes`, `privacy-link` and `contact`; §3, §13 and §15 to `status`; §4 to
  `requester-type`; §5 to `verification` and `identity-fields` (sign-in or email); §6 to
  `request-types` and `residence` (region asked on the form gates the menu); §7–§10 explainers to
  `request-effects` (each option is also a `request-types` entry); §11 to `request-details`, its
  law-specific framing regional; §12 to `attestation`; §14 to `confirmation`; §16 to `handler`
  (vendor runs the portal) and `data-use` (encryption); §17 to `contact`.
- s05: §3 to `representative`, `data-use` and `verification`; §4 to `verification` and
  `data-use`; §5 to `contact`; §7 and §8 to `representative` (§8 regional); §9 to
  `requester-type`; §11 (limit field) to `request-details` with a regional row; §12 to
  `response-method`; §13 to `attestation`.
- s06: §1 to `intro`, `eligibility` and `request-types`; §2 to `other-routes` (device location
  settings) with a regional row; §3 to `verification` and `data-use`; §4 and §9 to
  `representative`, §9's email fallback also to `alt-channels`; §5 to `privacy-link`; §6 to
  `identity-fields` and `residence`; §10 to `attestation`; §11 to `confirmation`, `timeline` and
  `alt-channels` (error → email).
- s07: §2 to `privacy-link`; §3 (one fixed right) to `request-types`; §4 and §20 to `timeline`
  (regional rows), §20 also to `request-effects` (copy limited to data one is entitled to); §5 to
  `steps`; §7–§8 to `request-details`; §9 and §16 to `data-use` (§16 also repeats the
  `privacy-link`); §10–§14 to `identity-fields`; §18 to `handler` and `confirmation`; §19 to
  `verification`; §21 to `other-routes`.
- s08: §1 to `intro`, `eligibility`, `contact`, `privacy-link` and `verification`; §3 to
  `residence`; §4 to `requester-type`; §6 to `representative`; §7, §9, §10 to `request-details`;
  §8 to `other-routes` (opt-outs done in cookie and device settings) with regional rows; §11 to
  `attestation`; §12 (upload, "do not attach") and §16 to `verification`; §14 to `contact`; §15 to
  `confirmation`.
- s09: no intro text (title only); §2's "do not add personal data" is a `request-details`
  pattern; §3 to `requester-type`; §5 to `residence`; §6 to `data-use`; §7 splits into
  `timeline` and `fees-refusal`; §8 to `privacy-link`.
- s10: §1 to `intro` and `eligibility`; §2 (rights list, no selector) and §6 to `request-types`,
  §6 also to `request-effects` (deletion exceptions); §3 and §7 to `verification`; §4 to
  `eligibility` (age floor) and `representative` (parent for a minor); §5 to `other-routes`; §9 to
  `attestation`, `verification` and `alt-channels` (email the declaration); §10 to
  `representative`; §11 and §12 to `eligibility` (exempt groups) with regional rows, §11's pointer
  to the policy to `privacy-link`, §12's link to `other-routes`.
- s11: §1 to `intro`, `data-use` ("processed by JD Sports"), `contact` and `confirmation` (a
  confirmation email promised); its "your own personal data" line is framing, not
  `eligibility`, since §3 takes agents and minors; §2 (date of request) to `request-details`; §3
  to `representative`; §4 to `requester-type`; §10 and §12 to `verification` (§10 also takes an
  agent's mandate); §11 to `contact`; §13 to `confirmation`.
- s12: §1 to `intro`, `privacy-link` and `handler` (affiliated clubs under their own policies);
  §2 and §22 to `other-routes` (cookie and app privacy settings), §22 also to `opt-out-signals`;
  §3 to `steps` and `verification`; §4 to `eligibility` and `other-routes`; §5 and §26 to
  `contact`; §6 and §8 to `residence`; §9–§12 to `request-types` (regional rows), §13 to
  `request-types` and `request-details`; §15–§20 to `request-effects`, §19's processing window
  also to `timeline`; §24 to `verification`; §25 to `confirmation`.
- s13 (top-up): §1's "or someone you represent" is framing; `representative` is counted at §8
  (parent and agent roles) and §12 (agent box). §2 (export, deletion and access logs in the app's
  settings) and §3 (privacy inbox) to `alt-channels` (another way to carry out the same request;
  as s02's in-app route), §3's handling pointer also to `privacy-link`; §4 (complaints via "Other"
  or email) to `alt-channels`; §5 to `verification`, `confirmation` (no automatic receipt for
  every submission) and `privacy-link`; §6 to `residence`; §7 and §11 (login email) to
  `identity-fields`; §8 to `requester-type` and `representative`; §9 to `request-types` (role
  filters the menu), with regional rows; §10 (product data categories) and §13 to
  `request-details`; §14 to `confirmation`. The footer's "Do Not Sell or Share" link is site
  chrome.
- s14 (top-up): §1's link goes to a privacy vendor's glossary article, not the company's policy,
  so it is not `privacy-link` (the policy is linked only in the footer, chrome); §2 to
  `identity-fields` and `residence` (five broad regions); §3 to `requester-type`; §4 to
  `request-types` (regional rows); §5 to `request-details` (with a time period); §6 to
  `verification`; §7 to `attestation`, whose "or an authorized agent" is the only agent mention
  (a pattern there, not `representative`: the form takes no agent details); §8 to `confirmation`.
  The submit button only shows a browser alert and sends nothing; the wording is counted as
  written (see *First-batch qualification*).
- s15 (top-up): §1 to `intro` and `handler` (the form also reaches the DPO), with regional rows;
  §2 (in-app Help as another way to send the request) to `alt-channels`; §3 (each right glossed)
  to `request-types`, as s10's rights list; §4 to `identity-fields` and `verification` (email
  and phone must match the account); §5 (which service line) and §11 (optional supporting
  documents) to `request-details`; §6 to `requester-type`; §7 to `request-types`; §8 to
  `request-details`; §9 (country the request concerns, not residence) to `residence`; §10
  (reply language) to `response-method` (meaning widened, see *Changes*); §12 to `verification`
  and `confirmation`; §13 to `verification`. The post-submit link to the Privacy Hub is not
  counted as `privacy-link`.
- s08, re-mapped 2026-10-27 after `appeal` was added: the appeal request type (§5) and its
  detail field (§9) to `appeal` as well as `request-types` and `request-details`.

- Saturation batch 1:
  - s16: §1's effective date is document level; §2 to `intro` and `eligibility` (California
    residents), with regional rows; §3 to `privacy-link` (a separate CCPA notice) and `timeline`
    ("consistent with applicable law"); §4 to `other-routes` (cookie banner, footer link) and
    `opt-out-signals` (GPC); §5 is a sub-heading; §6 to `requester-type`; §7 to
    `identity-fields`; §8 to `request-types` (three rights with glosses, several at once); §9
    (exemptions may be claimed) to `request-effects`, regional.
  - s17: §2 to `intro`, `request-types` (fixed to access, like s07) and `representative`; §3 and
    §6 to `timeline` and §3 also to `confirmation` (reply by email), regional rows; §4 to
    `other-routes` (bills via the account), `verification`, `representative` and `steps`
    (guidance notes to read first); §5 to `verification` and `representative`; §7 (unregistered
    prepaid users cannot be verified) to `eligibility`; §8 and §16–§21's retention and court-order
    notes to `request-effects`; §9 to `alt-channels` (post, phone) and `representative`; §11–§13
    to `identity-fields`; §14 (others on the account; their data withheld) to `request-details`
    and `request-effects`; §15–§22 to `request-details` (date range, record-category checklist);
    §23 to `attestation`; §24–§25 to `verification` (ID documents) and `representative`; §26 to
    `privacy-link` (submitting confirms the policy was read, as s02); §28 to `other-routes`.
  - s18: §1 is the title; §2 to `intro` and `privacy-link`; §3 to `verification` and `data-use`;
    §4 (no medical-records requests) to `other-routes`; §5 to `requester-type` and
    `representative`; §6 to `request-types` (regional rows); §7 to `other-routes` (cookie tool);
    §8 to `identity-fields` and `residence`; §9–§10 to `representative`; §11 to
    `request-details`; **§12 (a right to appeal a refusal) fits no id: new id `appeal`**; §13 to
    `attestation` (agreed by submitting).
  - s19: §1 to `intro`, `privacy-link` and `other-routes` (customer service); §2 to
    `residence`; §3, §4, §9 to `requester-type`; §5, §10, §12 to `request-types` (branch-gated
    menus); §6 (current staff sent to the HR portal) to `eligibility` and `other-routes`; §7, §8,
    §16–§18, §20 to `identity-fields`; §11 and §14 to `request-effects`; §13 (app availability in
    China) gives no fact about requests and is not a section; §15 to `request-types`,
    `other-routes` and `opt-out-signals`, regional; §19 to `request-details`; §21 to
    `privacy-link`; §22 to `verification`; §23 to `confirmation`.
  - s20: §1 is the title; §2 to `intro` and `handler` (parent and two subsidiaries); §3 to
    `eligibility` and `other-routes` (HIPAA data and members sent elsewhere), regional; §4 to
    `requester-type` and `representative`; §5 and §9 to `request-types` (regional rows); §6 to
    `confirmation`, `appeal` and `verification`; §7 to `other-routes` and `opt-out-signals`; §8
    and §11 to `residence`; §10 to `request-effects` (what health-data rights reach); §12 to
    `identity-fields`; §13 to `representative`; §14 to `verification`, `confirmation`, `appeal`
    and, **for "We will not treat you unfairly for exercising your privacy rights", no id: new
    id `non-discrimination`**.

## Section map

First-row order of ids per sample (the basis of every count and median below).

```
s01 intro handler privacy-link other-routes identity-fields verification request-types request-details confirmation alt-channels status
s02 intro timeline alt-channels identity-fields request-types request-details other-routes verification sale-status privacy-link confirmation
s03 intro eligibility privacy-link data-use verification timeline representative steps identity-fields residence request-types attestation
s04 intro other-routes privacy-link contact status requester-type verification identity-fields request-types residence request-effects request-details attestation confirmation handler data-use
s05 intro privacy-link representative data-use verification contact identity-fields requester-type request-types request-details response-method attestation
s06 intro eligibility request-types other-routes verification data-use representative privacy-link identity-fields residence request-details alt-channels attestation confirmation timeline
s07 intro privacy-link request-types timeline steps requester-type request-details data-use identity-fields handler confirmation verification request-effects other-routes
s08 intro eligibility contact privacy-link verification identity-fields residence requester-type request-types appeal representative request-details other-routes attestation confirmation
s09 request-types request-details requester-type identity-fields residence data-use timeline fees-refusal privacy-link
s10 intro eligibility request-types verification representative other-routes request-effects identity-fields attestation alt-channels privacy-link
s11 intro data-use contact confirmation request-details representative requester-type request-types identity-fields verification
s12 intro privacy-link handler other-routes steps verification eligibility contact residence requester-type request-types request-details request-effects timeline identity-fields opt-out-signals confirmation
s13 intro alt-channels privacy-link verification confirmation residence identity-fields requester-type representative request-types request-details
s14 intro identity-fields residence requester-type request-types request-details verification attestation confirmation
s15 intro handler alt-channels request-types identity-fields verification request-details requester-type residence response-method confirmation
s16 intro eligibility privacy-link timeline other-routes opt-out-signals requester-type identity-fields request-types request-effects
s17 intro request-types representative timeline confirmation other-routes verification steps eligibility request-effects alt-channels identity-fields request-details attestation privacy-link
s18 intro privacy-link verification data-use other-routes requester-type representative request-types identity-fields residence request-details appeal attestation
s19 intro privacy-link other-routes residence requester-type request-types eligibility identity-fields request-effects opt-out-signals request-details verification confirmation
s20 intro handler eligibility other-routes requester-type representative request-types confirmation appeal verification opt-out-signals residence request-effects identity-fields non-discrimination
```

## Merged list (s01–s20, final)

Median position is the first row's rank divided by the sample's id count less one (0 = first,
1 = last). Tiers per `formats/skeleton-format.md` (core ≥80%, common 40–79%, rare <40%) are
final: the build ended at s20. *Commonly omitted* = fewer than 20% (≤3/20). Counts are over the
20 valid samples.

| Id | Count | Tier | Median pos. | Note |
|---|---|---|---|---|
| intro | 19/20 | core | 0.00 | carries regional parts |
| eligibility | 9/20 | common | 0.11 | carries regional parts |
| handler | 6/20 | rare | 0.11 | |
| privacy-link | 16/20 | core | 0.20 | |
| contact | 5/20 | rare | 0.22 | |
| data-use | 8/20 | common | 0.31 | |
| other-routes | 13/20 | common | 0.33 | carries regional parts |
| timeline | 8/20 | common | 0.39 | carries regional parts |
| steps | 4/20 | rare | 0.40 | drafting; folded into `intro` in the skeleton |
| verification | 18/20 | core | 0.41 | carries regional parts |
| requester-type | 14/20 | common | 0.46 | carries regional parts |
| representative | 10/20 | common | 0.46 | carries regional parts |
| request-types | 20/20 | core | 0.52 | carries regional parts |
| residence | 12/20 | common | 0.55 | carries regional parts |
| identity-fields | 20/20 | core | 0.59 | |
| status | 2/20 | rare | 0.63 | commonly omitted |
| appeal | 3/20 | (out of root) | 0.64 | regional only (us) |
| request-details | 16/20 | core | 0.71 | carries regional parts |
| request-effects | 8/20 | common | 0.71 | carries regional parts |
| alt-channels | 7/20 | rare | 0.71 | |
| opt-out-signals | 4/20 | (out of root) | 0.73 | regional only (us) |
| sale-status | 1/20 | (out of root) | 0.80 | regional only (us) |
| fees-refusal | 1/20 | rare | 0.88 | commonly omitted; root id (chief of staff); folded into `timeline` in the skeleton |
| confirmation | 14/20 | common | 0.90 | |
| response-method | 2/20 | rare | 0.90 | commonly omitted; folded into `confirmation` in the skeleton |
| attestation | 9/20 | common | 0.93 | carries regional parts |
| non-discrimination | 1/20 | (out of root) | 1.00 | regional only (us) |

By count: 6 core, 10 common, 7 rare root ids (23); 4 ids out of the root as regional-only. The
skeleton folds `steps`, `fees-refusal` and `response-method`, so it has 6 core, 10 common and 4
rare sections (20). Since s01–s15: `eligibility` and `request-effects` rose to common (5/15 →
9/20; 4/15 → 8/20); `alt-channels` fell back to rare (6/15 → 7/20). `verification` sits early
(0.41) because many samples announce it in the intro; its fields and screens come late.

## Patterns (s01–s20)

Vendor wording counts once (decision 39): s08, s11, s12, s19 and s20 share OneTrust's default
strings for the email-verification screen ("Please check your email for confirmation, click
confirm and we will start your request.") and the thank-you screen, and the field help lines s11
and s19 keep.

- **request-types:** 13/20 one request per submission (radio, dropdown or buttons in s01 s02 s03
  s05 s11 s13 s14 s15 s18 s19; one per flow in s04; fixed to access in s07 and s17), 6/20 several
  at once (s06 s08 s09 s12 s16 s20), s10 no selector at all. Option count from 2 (s02) to 13
  (s08). 9/20 name options as rights ("Right to Correct"; s03 s05 s06 s08 s09 s11 s12 s16 s18),
  6/20 as first-person goals ("Download my data"; s01 s04 s13 s14 s15 s20). 6/20 explain each
  option or right in a line (s01 s04 s16 s18 by option; s10 s15 a rights list above the form).
  5/20 change the menu by residence (s04 s08 s12 s19 s20), 2/20 by role or product (s13 s19).
  7/20 add choices of the company's own beside the legal ones: marketing unsubscribe, group or
  partner sharing, model training, account or app deletion, access log, contacting the DPO (s01
  s04 s11 s12 s13 s15 s19). 3/20 take complaints as a type (s11 s13 s15). Access is offered by
  20/20, deletion 18/20 (not s07 or s17), correction 14/20 (not s02, which sends it to support,
  s04, s07, s10, s17, s19). 2/20 merge two regimes' names in one label ("Deletion/Erasure", s05;
  "rectification/correction", s09).
- **identity-fields:** 19/20 ask name and email, or sign in (s04's account holders); s15 asks
  email and phone, no name. Postal address required in 4/20 (s05 s07 s10 s17), optional in 2/20
  (s18 s20); phone required in 5/20 (s05 s08 s10 s15 s20); date of birth in s02 and s20 (s07
  optional); s02 a full national ID number. 5/20 an account, product or staff identifier (s07
  s13 s15 s17 s19); 3/20 past names or identifiers (s05 s10 s19). 3/20 note the email is used
  for verification (s01 s08 s11).
- **verification:** 9/20 an email confirmation link (s01 s04 s06 s08 s11 s12 s15 s19 s20;
  OneTrust default wording counts once), s04 account sign-in for account holders, s01 a booking
  reference, 4/20 match the details against records or the account (s03 s05 s10 s15). ID
  documents: s17 requires proof of ID with a checklist and upload, s11 offers an optional
  upload, s02 warns ID "may be required"; s10 a signed declaration. 4/20 say only that more
  information may be asked (s13 s14 s18 s20; s14 "only if strictly necessary"). s07 leaves it to
  the privacy team; s09 and s16 say nothing. s08 keeps an upload box labelled "Do Not Attach Files
  Unless Requested". s06 says an unverified request may be refused; s04 and s08 say an
  unconfirmed request is cancelled; s15 tells non-users to resubmit as non-users.
- **request-details:** 14/20 a free-text box, 4/20 with a character cap (50 s09, 400 s05, 512
  s07, 5,000 s11 and s19); 3/20 tell the person not to add personal data there (s09 s11 s19);
  3/20 show detail fields only for certain request types (s08 s12 s18); 3/20 a date range or time
  period (s07 s14 s17); 2/20 a checklist of the product's data or record categories (s13 s17); s01
  a correction dropdown, s11 a "date of request" field, s15 the service line and optional
  supporting documents.
- **privacy-link:** 16/20 link the privacy notice (none in s11 s15 s20; s14 only a third-party
  glossary article). 2/20 link it twice (s03 s07). 2/20 make submitting the form a confirmation
  that the policy was read or agreed (s02 adds the terms and payment agreements; s17).
- **representative:** 7/20 a self-or-agent choice in the form (s03 s06 s08 s11 s13 s18 s20), s05
  a relationship dropdown with optional agent fields, s10 an upload only, s17 a postal route for
  third parties. Proof: 4/20 signed written authority uploaded or enclosed (s10 s11 s17 s18; s18
  rejects unsigned forms), s06 a link or email, s05 and s20 "we will contact you", 3/20 ask for
  nothing (s03 as served, s08, s13). 3/20 cover parents of minors (s10 s11 s13). s14 names agents
  only in its attestation and takes no agent details.
- **requester-type:** 6/20 customer / employee or applicant / other (s07 s08 s09 s11 s14 s19), 4/20
  the product's own user roles (s05 s13 s15 s18), s04 account holder or not, s16 a single
  "customer?" checkbox, s20 consumer or agent, s12 one option only. 5/20 offer a no-account or
  visitor option (s04 s13 s15 s18 s19). s19 branches on the answer into further questions.
- **residence:** 4/20 a US state picker (s03 s06 s08 s18), 4/20 every country (s09 s13 s19 s20),
  s12 eligible countries then state or province, s14 five broad regions, s15 the country the
  request concerns rather than residence, s04 a region field with no visible label. 6/20 gate
  later fields on it (s04 s06 s08 s12 s19 s20); 2/20 prefill it by geolocation (s12 s19).
- **eligibility:** 5/20 limit the form to US-state residents (s03 s06 s08 s10 s16), s12 to listed
  regions with a fallback contact form; 3/20 turn away groups whose data is handled elsewhere
  (s19 current staff, s20 patients and plan members, s17 unregistered prepaid users who cannot be
  verified); s10 an 18+ floor with a parent route and two exempt groups.
- **other-routes:** 6/20 send cookie or ad-tracking opt-outs to the cookie tool or a footer link
  (s08 s12 s16 s18 s19 s20); 2/20 device settings (s06 s08); 3/20 separate customer service from
  privacy requests (s01 s07 s19); 3/20 a separate form or portal (s07 s10, s19 the HR portal);
  3/20 help centre or support email (s01 s02 s04); 3/20 account settings or self-service (s04 s12
  s17); 2/20 data handled under other rules (s18 medical records, no pointer; s20 clinic notices).
- **alt-channels:** 3/20 the app (s02 and s15 an in-app request; s13 self-service tools), 3/20
  email (s06 s10 for documents, s13 the privacy inbox), s17 post and phone (post required for
  third parties), s01 the DPO when the form or inbox fails.
- **data-use:** 7/20 one purpose-limit sentence (verify, locate, respond); s04 names the portal
  vendor and encryption instead.
- **timeline:** 12/20 say nothing. Of the 8 that do: 2/20 a number (one month: s07, s17 with an
  extension notice), 4/20 "the timeframe required by law" or similar (s03 s06 s09 s16), s02 "as
  soon as possible", s12 a processing window for opt-outs only. s09 alone says requests are free
  and when they may be refused (`fees-refusal`).
- **attestation:** 6/20 a required checkbox or confirm list (s03 s04 s05 s06 s14 s17), 2/20
  agreement by submitting (s08 s18), s10 a signed PDF declaration. 3/20 make it sworn (s03 s05
  s10).
- **confirmation:** 14/20 describe it; 5/20 "a representative will review and reply by email"
  (s08 s11 s12 s19 s20, OneTrust wording once); s11 shows a request ID; s04 status states through
  the request's life; s20 an acknowledgement email; s17 a reply by email within the deadline; s13
  "request received" with a warning that not every submission gets a receipt; s14 a browser alert
  only (its submit sends nothing). 6/20 have no post-submit text (s03 s05 s09 s10 s16 s18). 2/20
  ask how the answer should be sent (s05 email or post; s15 reply language).
- **request-effects:** 4/20 what deletion removes and keeps, or its knock-on effect on linked
  services (s04 s10 s12 s19); 2/20 what an access request returns and its limits (s07; s17
  retention per record category, records released only by court order, others' data withheld);
  s12 what each opt-out stops; s16 that legal exemptions may limit the answer; s20 which data the
  rights reach.
- **contact:** 3/20 a footer with postal address and privacy email (s08 s11 s12; s08 adds legal
  entity and phone), s05 phone and hours only, s04 a support email. 15/20 give no contact beyond a
  request channel.
- **handler:** 3/20 a named privacy team or the DPO (s01 s07 s15), s01 an affiliate for some
  product lines, s12 affiliates under their own policies, s20 the group companies covered, s04 the
  portal vendor.
- **steps:** 4/20 say what to have ready or read first, or list the steps (s03 s07 s12 s17).

## Document level (s01–s20)

- **Words:** median about 570 (range 190–1,750). Large about 510 (8: s01 s04 s07 s09 s11 s15 s17
  s19), mid about 655 (8: s02 s05 s08 s10 s12 s16 s18 s20), small about 495 (4: s03 s06 s13 s14).
  The longest are portals with per-request notices (s04, s12) and s17's access form with record
  categories.
- **Carrier:** 13/20 a form on the company's own site (s01 s02 s03 s05 s06 s07 s09 s10 s13 s14
  s15 s16 s17; s13 posts to HubSpot), s18 a Jotform form on the company's sub-domain, 5/20
  OneTrust-hosted (s08 s11 s12 s19 s20; s19 framed in the company's page), s04 a Transcend portal.
  16/20 one page; 4/20 in steps or pages (s01 s04 s07 s18). s10 adds a PDF declaration; s17 a
  postal PDF form and guidance notes.
- **Title:** "Privacy (Rights) Request Form", "Individual Rights Request Form" or "Privacy
  Portal" in most; "Data Subject (Access) Request" or "Subject Access Request" (s01 s07 s13 s14
  s17 s20); "Personal Data Request" (s15); 3/20 name a law or state (s02, s10, s16).
- **Structure:** intro block above the fields 19/20 (s09 none); headed field groups 8/20 (s05 s06
  s07 s09 s10 s12 s14 s17); s13 a "Before you submit" box; s19 a branching question tree; field
  labels as the only headings in the rest.
- **Register:** 20/20 "we/you" in notices; 12/20 switch to the first person in labels, options or
  the attestation ("I declare", "I reside", "Download my data").
- **Recurring elements:** reCAPTCHA or honeypot 9/20; required-field asterisks; helper lines under
  fields (s11 s15 s19); language switcher 5/20 (s04 s08 s11 s12 s19); a dated line 1/20 (s16's
  effective date; s05's page title carries a version stamp).
- **Commonly omitted:** response time (12/20), any statement of fees (19/20), post-submit text
  (6/20), a contact beyond the request channel (15/20).

## Regional content

From the `[law: …]` cells of s01–s15, plus untagged rows that carry the same content (marked
"untagged"). Left out of the root; region runs start from these. The samples justify a `us` block
(10 of 15 carry US-state content: s01 bundle, s02, s03, s05, s06, s08, s09, s10, s12, s13). 4/15
offer GDPR-style rights (restrict, object, portability) to every country with no law named (s09
s13 s14 s15): the root's region-neutral menu keeps access, correction and deletion; the rest goes
to the blocks as below.

| Region | Content | Id | Samples |
|---|---|---|---|
| us | Form limited to residents of US states with privacy laws; state picker decides the rights shown (CCPA/CPRA and the other state acts) | eligibility, residence | s03 s06 s08 s10 (s12) |
| us | Title or framing names the CCPA (Cal. Civ. Code §1798.130) | intro | s02 s10 |
| us | Request types in state-law wording: right to know categories vs specific pieces, sources, purposes, third parties; access/portability; correction; deletion (CCPA §§1798.100–.110; state acts) | request-types, request-details | s03 s05 s06 s08 s10 s12 (s09) |
| us | Opt-out of sale or sharing and of targeted advertising as request types (CCPA §1798.120; state acts) | request-types | s05 s08 s09 s10 s12 s13 |
| us | Limit use of sensitive personal information, as a type, a detail field or a consent withdrawal via device settings (CPRA §1798.121) | request-types, request-details, other-routes | s05 s06 s08 s12 |
| us | Appeal of an earlier decision, with date, request ID and reason (VCDPA, CPA, CTDPA and later acts) | request-types, request-details | s08 |
| us | Opt-out of sale/sharing done through the cookie preference centre or a separate do-not-sell form, not this form (CCPA §§1798.120, 1798.135) | other-routes | s08 s10 s12 |
| us | Authorized agent: option in the form and proof of authority (CCPA §1798.135, 11 CCR §7063; CPA/CTDPA); s01's bundle has an agent toggle not rendered for its locale | representative | s05 s06 s08 s10 (s01) |
| us | Verifiable consumer request: identity checked before acting, refusal if unverified, government ID may be asked (CCPA §1798.140(ak), 11 CCR §7060) | verification | s02 s06 |
| us | Signed declaration under penalty of perjury (11 CCR §7062 for specific pieces without an account); untagged | attestation | (s03 s05 s10) |
| us | Employee or job-applicant data as a requester type (CCPA covers it since 2023) | requester-type | s08 |
| us | Notices that employees and B2B contacts are exempt (CCPA §1798.145(m), (n)); both exemptions lapsed on 2023-01-01, so the text is out of date | eligibility | s10 |
| us | 12-month lookback in the rights list; "Beginning January 1, 2020" (CCPA §1798.130(a)(2)); out of date | request-types | s10 |
| us | No-sale statement (CCPA §1798.120) | sale-status | s02 |
| us | GPC honoured where required, per browser (11 CCR §7025; state opt-out preference signals) | opt-out-signals | s12 |
| eu | Restriction, portability and objection as request types, or as free-text options (GDPR Arts. 18, 20, 21) | request-types, request-details | s09 s12 s13 s14 s15 (s05) |
| eu | Withdraw consent for sensitive data; processing stops for that purpose (GDPR Arts. 7(3), 9(2)(a)) | request-types, request-effects | s12 |
| eu | Removal of personal data from model outputs, weighed against freedom of expression (GDPR Art. 17) | request-details, request-effects | s04 |
| eu | Reply without undue delay within the legal deadline, notice of extension (GDPR Art. 12(3)) | timeline | s09 |
| eu | Free of charge; unfounded or excessive requests may be refused, with reasons (GDPR Art. 12(4)–(5)) | fees-refusal | s09 |
| eu | Withdraw consent as a request type (GDPR Art. 7(3)); s13's "withdraw consent or restrict sharing" untagged | request-types | s14 (s13) |
| eu | Rights listed and glossed above the form in GDPR terms without naming the law, objection folding in direct marketing, profiling and automated decisions (GDPR Arts. 15–18, 20–22) | intro, request-types | s15 |
| eu | DPO as the fallback for failed requests, as a request option, or as a recipient of the form (GDPR Art. 38(4)); untagged | alt-channels, request-types, handler | (s01 s15) |
| uk | Subject access request named as such, one-month deadline from receipt of the request or of verification documents, ICO guidance link (UK GDPR Arts. 12(3), 15) | timeline, request-types | s07 |
| uk | Restriction, portability, objection and review of automated decisions as request types (UK GDPR Arts. 18, 20, 21, 22) | request-types | s11 |
| uk | Same EEA/CH/UK menu as the `eu` rows | request-types | s12 |
| other (ca) | PIPEDA and Quebec Law 25 menu (access, correct, delete, profiling and sharing opt-outs) | request-types | s12 |
| other (cn) | Withdraw consent option with a cookie-consent note (PIPL Art. 15), in s01's bundle only | request-types | (s01) |
| other (br) | Brazil as a region option and a Portuguese form version in the script; no Brazil-specific content; untagged | residence | (s14) |

Added from saturation batch 1 (s16–s20). With these, 14 of 20 samples carry US-state content
(s01 bundle, s02, s03, s05, s06, s08, s09, s10, s12, s13, s16, s18, s19, s20), 8 carry EU content
(s01 untagged, s04, s05, s09, s12, s13, s14, s15) and 4 UK content (s07, s11, s12, s17).

| Region | Content | Id | Samples |
|---|---|---|---|
| us | California-only page; title and browser title name the CCPA (Cal. Civ. Code §1798.130) | intro, eligibility | s16 |
| us | Rights framed under "applicable U.S. privacy law", varying by state; US-state picker | intro, residence | s18 (untagged) |
| us | State-law request types: know categories (12 months), access/portability, correction (with insurance fields), limit or withdraw consent, deletion, sale/sharing opt-out (CCPA §§1798.100–.121) | request-types, request-details | s16 s18 |
| us | List of specific third parties shared with, for Oregon and Minnesota residents (OCPA, MCDPA); untagged | request-types | (s20) |
| us | Consumer health data rights for Washington and Nevada residents: view or copy, delete, correct (WA My Health My Data Act, RCW 19.373; NV SB 370) | request-types, residence, request-effects | s20 |
| us | Opt-out of sale/sharing or targeted ads through the cookie banner, the footer link or a US-only branch, not the form (CCPA §§1798.120, 1798.135) | other-routes, request-types | s16 s18 s19 s20 |
| us | GPC honoured as an opt-out, per browser (11 CCR §7025; state opt-out preference signals) | opt-out-signals | s16 s19 s20 |
| us | Legal exemptions may limit the answer (CCPA §1798.145) | request-effects | s16 |
| us | Authorized agent with written authorization signed by agent and consumer; unsigned forms rejected; agent's own details (CCPA §1798.135(c), 11 CCR §7063); s20's tooltip untagged | representative | s18 (s20) |
| us | Right to appeal a refusal (Va. Code §59.1-577(C), the extractor's §59.1-578(C) corrected; CPA and later acts); s08's appeal request type moved here | appeal | s08 s18 (s20) |
| uk | A "complaint" request type in a UK company's form: the route DPA 2018 s. 164A requires since 19 June 2026; untagged (s13 and s15 offer the same outside the UK, root `request-types`) | request-types | (s11) |
| us | Acknowledgement email that explains how to appeal; untagged | appeal, confirmation | (s20) |
| us | Non-discrimination for using one's rights (CCPA §1798.125); untagged | non-discrimination | (s20) |
| us | HIPAA protected health information excluded from the form; patients and members sent to Notices of Privacy Practices (HIPAA Privacy Rule, 45 CFR 164.524, 164.526) | eligibility, other-routes | s20 |
| uk | Subject access request named under UK GDPR Art. 15 and DPA 2018; one calendar month, extension with notice, reply by email (UK GDPR Art. 12(3)) | request-types, timeline, confirmation | s17 |
| uk | Others' data withheld unless their authorisation is enclosed (UK GDPR Art. 15(4); DPA 2018 Sch. 2 para. 16); untagged | request-effects, request-details | (s17) |
| other (cn) | Phone in place of email, and an app-availability note, when the country is China; untagged | identity-fields | (s19) |

No `tr` content: the root pool has no Turkish company. The `tr` block merges its own pool against
these ids (decision 49).

## Facts (step 5)

Settled at skeleton time (chief of staff: check overlap before adding).

- `facts.users.rights_channels` (list of right and route) already answers *which rights and
  where*: it feeds `request-types`, `other-routes` and `alt-channels`. Its meaning is unchanged.
- No existing key covers *how a request is handled*: the identifiers asked, the verification
  method, representatives and proof, the response time, a status page, reply channels.
  `facts.product.deletion_verification` covers only deletion, and stretching `rights_channels`
  from a route list into a handling record would change it for the 9 files that use it. So one
  shared key is added, **`facts.users.request_handling`** (a record). Decision 29 allows this
  because the root skeleton uses it now.
- The `us` block needs the appeal route, which no shared key holds and which only US state laws
  require: **`facts.us.appeal_process`** in `regions/us/facts.md`.
- The `eu` and `uk` blocks reuse shared keys only (`facts.company.dpo_contact`,
  `facts.product.account_roles`, `facts.product.ai_features`, `facts.users.request_handling`).

| Id | Keys |
|---|---|
| intro (+ steps) | `facts.product.name`, `facts.company.legal_name`, `facts.product.services_in_scope` |
| eligibility | `facts.product.min_age`, `facts.data.subject_categories` |
| handler | `facts.company.legal_name`, `facts.company.group_companies`, `facts.company.joint_controllers`, `facts.company.privacy_owner` |
| privacy-link | `facts.company.published_policies` |
| contact | `facts.company.contact_email`, `facts.company.phone`, `facts.company.address`, `facts.company.dpo_contact` |
| data-use | `facts.users.request_handling`, `facts.processors.list` |
| other-routes | `facts.users.rights_channels`, `facts.data.cookie_controls`, `facts.product.data_deletion_controls`, `facts.product.support` |
| timeline (+ fees-refusal) | `facts.users.request_handling` |
| verification | `facts.users.request_handling`, `facts.product.has_accounts` |
| requester-type | `facts.data.subject_categories`, `facts.company.collects_applicant_data`, `facts.product.account_roles` |
| representative | `facts.users.request_handling`, `facts.product.min_age` |
| request-types | `facts.users.rights_channels`, `facts.marketing.email`, `facts.marketing.sms`, `facts.product.ai_features` |
| residence | `facts.users.regions` (as a value only; the root has no *Applies when* on it) |
| identity-fields | `facts.users.request_handling`, `facts.product.has_accounts` |
| status | `facts.users.request_handling` |
| request-details | `facts.users.rights_channels` |
| request-effects | `facts.data.kept_after_deletion`, `facts.product.deletion_blockers`, `facts.product.account_roles` |
| alt-channels | `facts.users.rights_channels`, `facts.company.contact_email`, `facts.company.dpo_contact` |
| confirmation (+ response-method) | `facts.users.request_handling` |
| attestation | `facts.users.request_handling` |

## Copies (rule 4)

None in s01–s20: no two tables share headings in the same order or quotes, and no `raw/` pair
was flagged. The five OneTrust forms (s08 s11 s12 s19 s20) share vendor default strings
(verification screen, thank-you screen, field help lines), each inside its own configuration: a
shared block, not a copy. It adds to patterns once (decision 39). s11 is close to the bare
OneTrust template (only its welcome and footer are the company's own words) but differs from the
others in fields, order and request types, so it stays a sample. s13 and s14 are both short
Next.js pages titled "Data Subject Request", but their fields, options and wording differ: own
texts.

## First-batch qualification

All 15 valid. Borderline ones:

| Sample | Verdict | Why |
|---|---|---|
| s01 Booking.com (large) | valid | rows 6 and 9–11 read from the page's translation bundle (later steps rendered by script); US/China variants recorded only under *Regional content*. |
| s04 OpenAI (large) | valid, borderline | read from a 2026-06-04 Wayback capture of the portal's JSON (live site blocks curl); a portal, not a single form. |
| s06 Becausal (small) | valid | takes US-state residents only; its sections still map to root ids. |
| s07 The AA (large) | valid, borderline | access requests only; no request menu. Counts toward `request-types` as "fixed to one request". |
| s10 1stDibs (mid) | valid, borderline | no request-type field at all; California only, with lapsed exemption notices (out of date text, kept as published, rule 4). |
| s11 JD Sports (large) | valid | ~45 configured OneTrust fields never show and are left out; the rendered form is the sample. |
| s13 Glyyd (small) | valid | role-dependent parts and post-submit text read from the page script; submissions post to HubSpot, but the page and wording are the company's own. |
| s14 Luzid (small) | valid, borderline | the submit button only shows a browser alert and sends nothing (a broken form; recorded under `confirmation`). Its published wording is counted as written (chief of staff, 2026-10-27). Company now trades as Glasslake. |
| s15 Bolt (large) | valid | dropdown options and post-submit strings read from the page's embedded form data. |

## Saturation

A sample is new only when it has a section whose content fits no id in *Section ids*; how it
writes a known id never makes it new (`build/build.md` step 3). Stop at 5 non-new in a row.

Batch 1 in pool order: s16–s20 = c14 Nav, c15 Vodafone UK, c24 Grow Therapy, c19 Philips, c16
Transcarent. All valid: each is the company's own live request form in English, and each company
is its own group (rule 5). No copies (rule 4).

| Sample | Verdict | Why |
|---|---|---|
| s16 Nav (mid) | not new | California page; every row is a known id: opt-outs routed to the cookie banner and footer link (`other-routes`), GPC (`opt-out-signals`), three glossed rights (`request-types`), exemptions caveat (`request-effects`). 1 non-new |
| s17 Vodafone UK (large) | not new | long access-only form, all known ids: record-category checklist and date range (`request-details`), retention and court-order limits and others' data withheld (`request-effects`), ID documents (`verification`), postal route (`alt-channels`), unregistered prepaid users (`eligibility`). 2 |
| s18 Grow Therapy (mid) | **new** | §12 states a right to appeal a refusal. No id holds what a person can do after a refusal (`fees-refusal` covers when a refusal may happen, not what follows), so `appeal` is added (regional-only, US). The count resets. 0 |
| s19 Philips (large) | not new | branching OneTrust tree; relationship, account and app menus to `requester-type` and `request-types`; deletion knock-on notices to `request-effects`; staff sent to the HR portal to `eligibility` and `other-routes`; US opt-out branch to regional rows. 1 |
| s20 Transcarent (mid) | **new** | §14's "We will not treat you unfairly for exercising your privacy rights" fits no id, so `non-discrimination` is added (regional-only, US). Its appeal sentences map to the new `appeal`. 0 |

**Stop:** the pool was closed by the owner after batch 1 (no more extraction or collection), with
0 non-new samples after the last new one (s20): `saturated: false`, `sample_count: 20`. Both new
ids are US-state content and out of the root, so the root's 23 ids did not change after the first
batch. c17, c18, c20, c21 and the rest of the reserve are not extracted.

Valid samples: 20 (s01–s20); by size 8 large, 8 mid, 4 small. Invalid: none.

## Decisions (chief of staff, 2026-10-27)

- Top-up: s13 = c22 Glyyd, s14 = c23 Luzid, s15 = c13 Bolt.
- `fees-refusal` stays a rare root id. The skeleton folds it into `timeline` as a pattern, because
  a rare section needs a fact condition (`skeleton-format.md`) and none decides it. See *Changes*.
- `facts.users.request_handling`: settled under *Facts (step 5)*.
- *Avoid* candidates go to the `us` block (s02's national ID number and its agreement to terms;
  s10's lapsed exemption notices), with the binding texts cited there.
- Batch 1 is the last (owner): outputs written with `saturated: false`.

## Changes

- 2026-10-27 (top-up s13–s15): no id added. `response-method` widened from "email or post" to
  also cover the reply language (s15 §10); `alt-channels` widened to name in-app self-service
  tools that carry out the same request (s13 §2) beside in-app requests (s02, s15). No other
  meaning changed. Tiers moved: `eligibility` and `contact` common → rare, `alt-channels` rare →
  common.
- 2026-10-27 (saturation batch 1): `appeal` added from s18 §12 and `non-discrimination` from
  s20 §14, both regional-only (US). s08's appeal request type re-mapped to `appeal` as well. No
  meaning of an existing id changed. 27 ids.
- 2026-10-27 (step 4): `steps` (4/20), `fees-refusal` (1/20) and `response-method` (2/20) stay
  ids here but are folded in the skeleton: `steps` into `intro` and `fees-refusal` into
  `timeline`, since they are drafting content and no fact decides them; `response-method` into
  `confirmation`, since it is a field about the reply. The 4 regional-only ids go to the `us`
  block. The skeleton has 20 sections.

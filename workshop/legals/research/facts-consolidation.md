# Facts consolidation (proposal)

PLAN.md Phase 3: "Consolidate `helpers/facts-schema.md`: merge keys that name the same fact differently."
Proposal only; nothing under `plugin/` was edited. Written 2026-10-27.

Scope read: `helpers/facts-schema.md` (95 keys), `regions/{eu,uk,us,tr}/facts.md` (5 + 7 + 1 + 16 keys),
and every `facts.*` reference under `plugin/` (skeletons, region blocks, agents, `SKILL.md`,
`helpers/catalog.md`, `helpers/grill.md`, `build/`, `formats/`). Paths below are relative to
`plugins/fatodono-founderkit/skills/legals/` unless they start with `plugin/`.

Test applied: merge only when the two keys would always get the same answer for the same company.

## Summary

| Finding | Count |
|---|---|
| Key merges proposed | 0 |
| Near-duplicates judged distinct | 16 |
| Field-level overlaps inside distinct keys (trim proposals) | 5 |
| Keys defined but never referenced | 0 |
| Keys referenced but never defined | 6 (all in format/build docs, none in a skeleton) |
| Promotion candidates outside the `tr` 7 | 1 now (`facts.eu.processor_customers`), others wait |

No pair passed the test. Every near-pair either describes a different document's version of
the fact (licence acceptance vs sales-contract acceptance), a legal regime's narrower or wider
definition (`data.sells` vs `us.sells_or_shares`), or a curated list that can leave out what a
dedicated key always holds (`published_policies` vs `tr.kvkk_notice_url`). The real duplication is
smaller: a few sub-facts sit in two keys at once, and the same answer can then be given
twice and drift apart. These are listed under *Field-level overlaps* as trims, not merges.

## 1. Proposed merges

None.

## 2. Near-duplicates judged distinct

The owner can overrule any of these. The line numbers point to the `### ` headings.

| Keys | Why they stay separate |
|---|---|
| `company.collects_applicant_data` (helpers/facts-schema.md:96) / `data.subject_categories` `job-applicants` (:562) / `company.internal_activities` recruitment (:162) | The first is only applications *through the website* (privacy-policy `job-applicants` gate, skeletons/privacy-policy.md:408). Applications by email or a job board make the other two true and the first false. |
| `product.business_use` (:274) / `company.acts_as_processor` (:184) | Admin-controlled org accounts are the usual signal for processor status, but a B2B product can have org accounts and still be controller (and a processor role can exist with no org accounts, e.g. an API). |
| `product.business_use` (:274) / `product.account_roles` (:348) | `account_roles` lists every role that *deletes differently* (family, deceased, partner); `business_use` is whether organisations use the product. Overlap only on the org-admin row. |
| `product.deletion_routes` (:299) / `users.rights_channels` (:837) | `rights_channels` covers every right; its "delete" row is a summary of `deletion_routes`, which carries per-route paths, sign-in need and platforms. |
| `data.deletion_lag` (:550) / `product.deletion_grace_period` (:322) | Lag is request-to-gone; the grace period is the restorable part of it. A product can have a 30-day lag and no grace period. |
| `data.retention` (:544) / `data.kept_after_deletion` (:582) | Retention is per category during the account's life; kept-after-deletion is what survives closure. Invoices appear in both, but most categories differ. |
| `data.sells` (helpers/facts-schema.md:514) / `us.sells_or_shares` (regions/us/facts.md:5) | US state laws count ad-identifier sharing as "sale/share"; a company with AdMob answers `false` to the first and `true` to the second. |
| `data.targeted_ads` (:520) / `data.tracking` with purpose `advertising` (:508) | Tracking with an advertising SDK used only for attribution of own campaigns is not always "targeted ads"; the bool is the user's call. |
| `company.dpo_contact` (:84) / `company.privacy_owner` (:194) | DPO is a legal role with its own contact; the record owner is whoever maintains the RoPA. Most small companies: no DPO, founder as owner. |
| `eu.dpf` / `uk.dpf` (regions/eu/facts.md:17, regions/uk/facts.md:17) | The UK Extension is an optional add-on to EU-US DPF certification; EU-only certification is common. |
| `eu.representative` / `uk.representative`, `eu.transfer_mechanisms` / `uk.transfer_mechanisms` | Different appointments and different instruments (SCCs vs IDTA/Addendum). |
| `company.governing_law` courts (:135) / `tr.merchant_court` (regions/tr/facts.md:149) | `merchant_court` is only for business buyers; consumer disputes in Turkey go to the consumer's court regardless of `governing_law`. |
| `company.published_policies` (:124) / `tr.kvkk_notice_url` (regions/tr/facts.md:101) | Same URL when listed, but `published_policies` is the curated "what these terms link to" list (its *Ask* is terms-specific) and can omit the KVKK notice. Merging would make the TR contract depend on a ToS choice. |
| `product.eula_acceptance` (:366) / `tr.acceptance_mechanism` (regions/tr/facts.md:76) | Different contracts accepted at different moments (installer vs checkout). This is the case decision 29 predicted: the EULA cut the fact as a list with other values, so a future `facts.sales.acceptance_mechanism` must not absorb `eula_acceptance`. |
| `sales.return_rules` window / payer (:813) / `tr.withdrawal_period_days`, `tr.return_shipping` (regions/tr/facts.md:109, :124) | Statutory withdrawal vs the seller's voluntary return policy: large Turkish retailers grant 30-day returns while the contract states 14-day withdrawal; `return_rules` also covers at-fault returns and only physical goods. |
| `sales.refund_request` channel (:796) / `tr.withdrawal_channels` (regions/tr/facts.md:117) | Asking for money back vs giving notice of withdrawal; the regulation requires the latter to be possible without a refund request. |

## 3. Field-level overlaps (trim proposals)

Not merges: both keys stay, but one sub-fact is held twice and can contradict itself. Each
trim names the side to cut; the owner may prefer the other side.

1. **Lifetime plans** in `sales.plans` (period `lifetime`, helpers/facts-schema.md:661–663) and
   `sales.one_time_purchases` (kind `lifetime`, "lifetime unlocks", :697–699). `sales.subscription`
   (:649–650) already says lifetime plans belong to `sales.plans`.
   Trim: remove `lifetime` from `one_time_purchases` (Means and kind enum, helpers/facts-schema.md:698–699).
   Would also change skeletons/subscription-terms.md:267 ("lifetime unlocks" in the one-time
   section's *Covers*, add a pointer to `facts.sales.plans` or name it in the section's Facts).
2. **Deleting single items** in `product.deletion_alternatives` ("delete individual items",
   helpers/facts-schema.md:342) and `product.data_deletion_controls` (:358–360). Both feed sections of
   skeletons/account-deletion.md (:70–71 and :263–264), so the same control can be written twice.
   Trim: drop "delete individual items" from `deletion_alternatives` Means (:342).
3. **Refundability** in `sales.refund_exclusions` (:785–788) and the `refundable` fields of
   `sales.one_time_purchases` (:699) and `sales.gifts` (:719). Consumers:
   skeletons/refund-policy.md:201 (exclusions), skeletons/subscription-terms.md:269–270
   (one-time). Trim option: keep the per-item `refundable` bools (they are product facts) and
   say in `refund_exclusions` Look/Ask "start from the non-refundable items in
   `one_time_purchases` and `gifts`", so the scanner fills one from the other. No key removed.
4. **Proration** in `sales.plan_changes` (`upgrade: immediate-prorated`, :675) and
   `sales.partial_refunds` ("on a plan change", :776–778). Trim: drop "on a plan change" from
   `partial_refunds` Means (:776–777) and its Ask (:781), leaving cancellation and
   discontinuation; plan-change money stays in `plan_changes`.
5. **Supported versions** in `product.update_policy.old_versions` (:415) and
   `product.support.supported_versions` (:436), both read by skeletons/eula.md. Likely the same
   answer for a small company, but security updates and customer support can differ. Left as is;
   flagged only.

## 4. Orphans and undefined keys

**Defined but never referenced: none.** Every key in `helpers/facts-schema.md` and the four region
`facts.md` files is named somewhere outside its definition. Weakest consumers: `product.category`
(only `SKILL.md` and `build/build.md`, by design, decision 34) and `users.regions` (no skeleton;
`SKILL.md`, `helpers/catalog.md`, `helpers/grill.md`, `helpers/doc-checker.md`, format docs).

Empty groups: `content` and `registrations` are listed in helpers/facts-schema.md:10 but have no keys.
`registrations` is the target of `uk.ico_registration`'s proposed name; `content` has no taker.
Option: drop `content` from the list until a key needs it.

**Referenced but never defined: 6**, all in format or build docs, none in a skeleton or region
block, so no write run hits them today. They are still copied by builders as examples.

| Key | Where | Proposal |
|---|---|---|
| `facts.data.sources` | formats/skeleton-format.md:46 | Example uses a non-key; change to `facts.data.third_party_sources`. |
| `facts.sales.direct` | formats/skeleton-format.md:66 | Example condition on a non-key; change to a real one, e.g. `facts.sales.purchase_channels` contains `web-direct`. |
| `facts.processors` | build/build-task.md:45 | Group, not a key; change to `facts.processors.list`. |
| `facts.tr.verbis` | build/build-task.md:31 | Illustrative future key; fine as an example, or reword "e.g. a future `facts.tr.verbis`". |
| `facts.company.employees` | build/build-task.md:32 | Illustrative, but a real latent need: `company.dpo_contact` (:88, "under 250 people"), `company.internal_activities` (:173, "only when the company has employees") and regions/uk/ropa.md:37 all lean on headcount without a key. Under decision 29 it waits for a section that names it. |
| `facts.br.encarregado` | formats/region-format.md:43 | Naming example for contributors; keep. |

Proposed-shared names that are not yet keys (expected, not defects): `facts.company.processor_customers`
(regions/eu/facts.md:39), `facts.data.legitimate_interests` (regions/uk/facts.md:35),
`facts.registrations.privacy_regulator` (regions/uk/facts.md:28), and the 7 `facts.sales.*` in
regions/tr/facts.md.

## 5. Region keys that are really region-neutral

**The 7 generic `tr` sales keys** (`sales_model`, `delivery`, `business_buyers`, `order_limits`,
`loyalty_program`, `acceptance_mechanism`, `contract_copy`): untouched per decision 29. One data
point for that later promotion is in §2: the EULA's acceptance fact came out differently, so
`acceptance_mechanism` should be promoted as a sales-contract fact only.

**Other `facts.tr.*` keys:**

| Key | Judgement |
|---|---|
| `seller_registry` | Turkey-specific identifiers (MERSİS, KEP). The generic idea (trade register number, VAT id) will recur in `de` (Impressum); a shared `facts.company.registration_ids` could be cut then. Wait. |
| `pre_info_form`, `kvkk_notice_url` | Turkey-specific documents. Keep. |
| `withdrawal_period_days`, `withdrawal_channels`, `withdrawal_exceptions`, `immediate_performance_consent`, `return_shipping` | Not root-neutral (the US has no withdrawal right), but the same shape exists in `eu` and `uk` (CRD Arts. 9–16, UK CCRs; the exceptions list is nearly the same as CRD Art. 16). Candidates for shared `facts.sales.withdrawal_*` when the EU withdrawal item (seed 41) is built. Same reasoning as decision 29: wait for that consumer. |
| `merchant_court` | Generic in idea, used only by `tr`. Keep. |

**Outside `tr`, one promotion is already due under decision 29:**

- `facts.eu.processor_customers` → `facts.company.processor_customers`. The second consumer
  already exists: regions/uk/ropa.md `uk-processor-record` (:187–203) asks for "the customers
  (controllers) it acts for with their contacts" (UK GDPR Art. 30(2)(a)) but its Facts line
  (:197) names only `acts_as_processor` and `processors.list`, so the writer has no key for the
  customer column. The root `processor-activities` (skeletons/ropa.md:389–390) also names
  customer categories without a key. Changes: add the key to helpers/facts-schema.md after
  `company.acts_as_processor` (after :192), delete regions/eu/facts.md:29–39, rename in
  regions/eu/ropa.md:174, add to regions/uk/ropa.md:197 (and optionally skeletons/ropa.md:390).
  Editing published `eu`/`uk` blocks is a maintainer change (decision 24), which this is.
- `facts.uk.legitimate_interests` → `facts.data.legitimate_interests`: no second consumer.
  regions/eu/ropa.md:115 lists the balancing test as *commonly omitted*, and the eu privacy
  policy's 6/24 pattern (regions/eu/privacy-policy.md:59) names no key. Wait.
- `facts.uk.ico_registration` → `facts.registrations.privacy_regulator`: the VERBİS twin exists
  only as an example (`facts.tr.verbis`, build/build-task.md:31). Wait.

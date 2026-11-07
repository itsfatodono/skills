# TR fact keys

Keys only the `tr` region uses, in the format of `helpers/facts-schema.md`. Added by the
`tr-distance-sales` pilot (2026-10-26).

Keys marked **Proposed shared key** describe facts that are not specific to Turkey. They are
defined here because a region run never edits `helpers/facts-schema.md`; the maintainer can move them
to the shared schema under the proposed name and update the skeleton that names them.
On 2026-10-26 the six that shared skeletons also need moved to `helpers/facts-schema.md`
(`facts.company.phone`, `facts.sales.offer_type`, `facts.sales.payment_methods`,
`facts.sales.payment_provider`, `facts.sales.subscription`, `facts.sales.return_address`); the
rest stay here until a second region or a shared skeleton needs them.

## Seller

### facts.tr.seller_registry
- **Means:** the seller's Turkish registration identifiers: MERSİS number, tax office and tax
  number, trade registry number, and KEP (registered e-mail) address.
- **Type:** record (mersis_no, tax_office, tax_no, trade_registry_no, kep_address); any field may be empty
- **Look:** existing legal docs, the website footer or "İletişim"/"Künye" page, e-invoice
  settings. Not otherwise in code.
- **Ask:** "What are the company's MERSİS number, tax office and number, trade registry number
  and KEP address?" No recommendation; leave empty fields out rather than guessing.

## What is sold and how

### facts.tr.sales_model
- **Means:** whether the company sells its own goods, or runs a marketplace where other sellers
  sell and the company is an intermediary.
- **Type:** enum [own-store, marketplace]
- **Look:** seller or vendor models, multi-vendor carts, payouts to third parties.
- **Ask:** "Do you sell your own products, or do other sellers sell through your platform?"
  Recommend "own-store" unless the code has seller accounts.
- **Proposed shared key:** `facts.sales.sales_model`.

### facts.tr.delivery
- **Means:** how and when the purchase reaches the buyer: maximum delivery or activation time,
  carriers, shipping fee and free-shipping threshold, pickup points.
- **Type:** record (max_days, carriers: list, shipping_fee, free_shipping_threshold, pickup_points: bool, digital_activation)
- **Look:** shipping and carrier integrations (Yurtiçi, Aras, MNG, PTT, UPS, DHL eCommerce,
  Hepsijet), shipping-fee rules in checkout, licence or account activation code.
- **Ask:** "How long does delivery take at most, which carriers do you use, and what does
  shipping cost?" Recommend the values configured at checkout; for digital products, "activated
  immediately on payment".
- **Proposed shared key:** `facts.sales.delivery`.

### facts.tr.business_buyers
- **Means:** whether businesses can buy (with a company invoice), which decides the clauses
  on business buyers and return invoices.
- **Type:** bool
- **Look:** checkout invoice type options (bireysel / kurumsal), tax-number fields.
- **Ask:** "Can businesses buy from you with a company invoice?" Recommend what the checkout
  shows.
- **Proposed shared key:** `facts.sales.business_buyers`.

### facts.tr.order_limits
- **Means:** the seller's order-cancellation rules: per-product quantity caps, retail-only
  sales, cancellation on obvious pricing errors or fraud suspicion.
- **Type:** list of (rule, detail)
- **Look:** cart quantity limits, fraud-check integrations, order-cancellation code.
- **Ask:** "Do you limit quantities per order, sell only to end consumers, or cancel orders
  placed at an obviously wrong price?" Recommend the limits found in code; otherwise none.
- **Proposed shared key:** `facts.sales.order_limits`.

### facts.tr.loyalty_program
- **Means:** points, coupons or gift cards earned or spent on orders, and what happens to them
  when an order is returned.
- **Type:** record (name, earn_on_orders: bool, spend_on_orders: bool, clawback_on_return: bool) or none
- **Look:** loyalty or points models, coupon and gift-card code.
- **Ask:** "Do buyers earn or spend points, coupons or gift cards on orders?" Recommend what
  the code shows.
- **Proposed shared key:** `facts.sales.loyalty_program`.

### facts.tr.after_sales
- **Means:** what the seller promises after the sale beyond the statutory rights: warranty
  documents and periods, the seller's own guarantees (freshness, expiry date), and the
  technical-support or after-sales service channel. Added by `tr-pre-contract-info`
  (2026-10-27).
- **Type:** record (warranty_documents: bool, warranty_period, own_guarantees: list of string, support_channels: list of string) or none
- **Look:** product data with warranty fields, warranty-registration or service-request flows,
  support or help-desk integrations, existing product pages.
- **Ask:** "Do your products come with a warranty certificate or a guarantee of your own, and
  where do buyers go for after-sales support?" Recommend none unless the catalogue or product
  pages show warranty periods or a support channel.

## Contract formation

### facts.tr.acceptance_mechanism
- **Means:** the act by which the buyer accepts the contract.
- **Type:** enum [checkout-checkbox, order-button, membership-signup]
- **Look:** checkout UI ("okudum, onaylıyorum" checkbox, buy button text), sign-up forms.
- **Ask:** "How does the buyer accept the contract: a checkbox at checkout, the order button,
  or at sign-up?" Recommend "checkout-checkbox" when one exists.
- **Proposed shared key:** `facts.sales.acceptance_mechanism`.

### facts.tr.contract_copy
- **Means:** how the buyer receives and keeps a copy of the contract, and how long the seller
  keeps it available.
- **Type:** record (channels: list of enum [email, account-page, public-page], retention)
- **Look:** order-confirmation e-mail templates, "my orders" pages that show documents.
- **Ask:** "How does the buyer get a copy of the contract, and for how long can they reach it?"
  Recommend "e-mailed with the order confirmation and shown in the account".
- **Proposed shared key:** `facts.sales.contract_copy`.

### facts.tr.pre_info_form
- **Means:** where the Ön Bilgilendirme Formu (pre-contract information form) is shown, which
  the contract refers to.
- **Type:** record (url or location, same_page: bool)
- **Look:** checkout templates and legal pages in the repo.
- **Ask:** "Where does the buyer see the Ön Bilgilendirme Formu: a separate page, or on the
  same page as this contract?" Recommend "a separate page shown at checkout".

### facts.tr.kvkk_notice_url
- **Means:** the URL of the KVKK Aydınlatma Metni the contract can point to.
- **Type:** string or none
- **Look:** legal pages in the repo, website footer links.
- **Ask:** "What is the address of your KVKK Aydınlatma Metni?" Recommend the URL found.

## Withdrawal

### facts.tr.withdrawal_period_days
- **Means:** the withdrawal period the seller grants, in days from delivery (or from contract
  formation for services).
- **Type:** number
- **Look:** existing returns or refund pages; return-window settings in code.
- **Ask:** "How many days do buyers have to withdraw?" Recommend the statutory minimum the
  samples state (14) unless the returns page grants more.

### facts.tr.withdrawal_channels
- **Means:** the channels a buyer can use to give notice of withdrawal.
- **Type:** list of enum [account-return-button, email, phone, post, form, other]
- **Look:** return-request flows in the app or website, support e-mail.
- **Ask:** "How can buyers tell you they withdraw?" Recommend the in-app or account return flow
  plus the support e-mail.

### facts.tr.return_shipping
- **Means:** who pays return shipping on withdrawal.
- **Type:** enum [seller-via-contracted-carrier, seller-always, buyer]
- **Look:** return-label integrations and carrier return codes.
- **Ask:** "Who pays return shipping when a buyer withdraws?" Recommend
  "seller-via-contracted-carrier" when a carrier return code exists.

### facts.tr.withdrawal_exceptions
- **Means:** which of the regulation's withdrawal exceptions can apply to the products sold.
- **Type:** list of enum [price-tied-to-markets, personalised, perishable, hygiene-sealed, mixed-after-delivery, sealed-media-or-software, periodicals, date-bound-leisure, instant-digital-content, service-started-with-consent, other]
- **Look:** product categories and offer type (`facts.sales.offer_type`).
- **Ask:** "Which of these apply to what you sell: <list>?" Recommend the categories that match
  the product catalogue.

### facts.tr.immediate_performance_consent
- **Means:** whether, and how, a buyer of digital content or a service agrees that performance
  starts before the withdrawal period ends.
- **Type:** record (asked: bool, mechanism) or none
- **Look:** checkout checkboxes for digital or service orders; code that unlocks content on
  payment.
- **Ask:** "Before access starts, do buyers tick a box agreeing that it starts now?" Recommend
  "yes, a checkout checkbox" when access is unlocked on payment.

## Disputes

### facts.tr.merchant_court
- **Means:** the city whose courts the seller names for disputes with business buyers, if any.
- **Type:** string or none
- **Look:** existing legal docs. Not in code.
- **Ask:** "Do you want to name a city's courts for disputes with business buyers?" Recommend
  the city of the company's registered address, or none.

## Personal data (KVKK)

Added by `tr-kvkk-notice` (2026-10-27). `tr-explicit-consent` and the `tr` block of
`data-subject-request` reuse them; `tr-explicit-consent` adds `facts.tr.consent_capture`.

### facts.tr.legal_bases
- **Means:** for each purpose in `facts.data.purposes`, the KVKK processing condition it rests
  on: explicit consent (Art. 5(1)); one of Art. 5(2)(a) expressly provided by law, (b) vital
  interest where consent cannot be given, (c) contract, (ç) legal obligation, (d) made public by
  the person, (e) establishing, exercising or protecting a right, (f) legitimate interest; and for
  special-category data the Art. 6(3) condition as amended by Law 7499 ((a) explicit consent to
  (g)). Where the condition is a law or a legal obligation, the statute behind it.
- **Type:** list of (purpose, condition: enum [5/1, 5/2-a, 5/2-b, 5/2-c, 5/2-ç, 5/2-d, 5/2-e, 5/2-f, 6/3-a, 6/3-b, 6/3-c, 6/3-ç, 6/3-d, 6/3-e, 6/3-f, 6/3-g], statute: string or none)
- **Look:** what each purpose does in code: account and order flows (contract), invoicing and
  record keeping (legal obligation: VUK, TTK), security logs and fraud checks (legitimate
  interest), marketing e-mail, SMS, push, profiling and ad SDKs (explicit consent); existing KVKK
  texts.
- **Ask:** "For each purpose, which KVKK condition applies? Proposed: <list>." Recommend 5/2-c for
  providing the service, 5/2-ç with the statute for invoices and legal records, 5/2-f for security
  and analytics that do not track users across services, 5/2-e for keeping evidence for disputes,
  and 5/1 only for marketing, profiling, ad tracking and occasional transfers abroad. Never
  recommend explicit consent for a purpose another condition covers (the Board's guide "Kişisel
  Verilerin İşlenme Şartları").
- **Not shared:** the shared `facts.data.purposes` already carries a basis in GDPR terms, which
  the `eu` region reads; `eu` has no legal-basis key of its own to promote with. KVKK's conditions
  are not a relabelling of GDPR Art. 6: law, made-public and legal-claims conditions stand on their
  own, there is no public-task basis, and Art. 6(3) differs from GDPR Art. 9(2). One purpose can
  rest on a different condition under each law, so one shared field cannot hold both (as
  `facts.uk.special_conditions` keeps the UK's own conditions).

### facts.tr.transfer_tools
- **Means:** each transfer of personal data abroad and the KVKK Art. 9 tool that covers it: an
  adequacy decision of the Board, an appropriate safeguard (the Board's standard contract,
  notified to the Authority within five business days of signing; binding corporate rules; a
  written undertaking with Board permission), or an occasional, non-repeating transfer under
  Art. 9(6).
- **Type:** list of (recipient, country, data, tool: enum [adequacy, standard-contract, bcr, undertaking, occasional], notified_on: date or none), or none
- **Look:** `facts.processors.list` and `facts.data.storage_locations` for providers and hosting
  outside Turkey; SDKs whose vendors are abroad (analytics, crash reporting, ads, AI); signed
  standard contracts and the Authority's notification receipts. Remote access from abroad counts
  as a transfer.
- **Ask:** "These providers handle data outside Turkey: <list>. Which Art. 9 tool covers each?"
  Recommend the standard contract, notified within five business days, for every regular
  transfer; adequacy only where the Board has announced a decision for that country; occasional
  transfer only for one-off cases. Never recommend explicit consent for a regular transfer.
  Recommend none only when no provider or hosting is outside Turkey.

### facts.tr.consent_capture
- **Means:** each explicit consent the company asks for (KVKK Art. 5(1), 6(3)(a), 9(6)(a)) and how
  it is taken: what it covers, where it is asked, whether it has its own unticked box or
  approve / do-not-approve choice, what refusing or withdrawing turns off and the alternative
  offered, the withdrawal path, and whether consent and refusal are logged. Added by
  `tr-explicit-consent` (2026-10-27).
- **Type:** list of (consent, purposes: list of string, location: enum [signup, feature-first-use, web-form, settings, paper, call, other], own_choice: bool, refusal_effect: string or none, alternative: string or none, withdrawal_path: string, logged: bool)
- **Look:** consent checkboxes and toggles in signup, settings and feature screens; consent
  models or tables (given_at, text version, source); İYS or consent-management integrations;
  feature flags gated on a consent; `facts.tr.legal_bases` rows with `5/1` or `6/3-a` and
  `facts.tr.transfer_tools` rows with tool `occasional` for what needs one.
- **Ask:** "For each consent you ask for (<list from the 5/1, 6/3-a and occasional-transfer
  rows>): where is it asked, does it have its own unticked box, what stops if the person says no
  or withdraws, how do they withdraw, and do you log the date and text version?" Recommend one
  unticked choice per consent at the point of use, refusal turning off only that feature, a
  withdrawal toggle in settings plus the support e-mail, and logging of date, text version and
  source for both consent and refusal.
- **Proposed shared key:** `facts.data.consent_capture`.

### facts.tr.representative
- **Means:** the data-controller representative (veri sorumlusu temsilcisi) in Turkey that a
  controller not established in Turkey appoints for VERBİS and Board correspondence.
- **Type:** record (name, address, email or KEP), or none
- **Look:** existing legal docs. Not in code.
- **Ask:** "Have you appointed a data-controller representative in Turkey? If so, give its name
  and contact." Recommend none when `facts.company.country` is TR.

### facts.tr.collection_channels
- **Means:** the channels outside the apps and websites in `facts.product.services_in_scope`
  through which personal data is collected (stores, call centre, paper forms, CCTV, events,
  e-mail), and whether each is fully automated, partly automated or non-automated (a filing
  system). Art. 10(1)(d) asks for the method of collection.
- **Type:** list of (channel, kind: enum [store, call-centre, paper-form, cctv, event, email, other], method: enum [automated, partly-automated, non-automated]), or none
- **Look:** call-centre or telephony integrations, in-store loyalty or POS code, support mailboxes.
  Stores, paper forms and CCTV are not in code.
- **Ask:** "Besides the app and website, do you collect personal data in stores, by phone, on paper
  forms, by CCTV or at events?" Recommend none for an app-only company, plus "e-mail" when a
  support address exists.

### facts.tr.destruction_policy
- **Means:** whether the company has a personal data retention and destruction policy (Saklama ve
  İmha Politikası) under the Regulation on the Deletion, Destruction or Anonymisation of Personal
  Data, where it is, and the interval of periodic destruction.
- **Type:** record (has_policy: bool, url: string or none, periodic_months: number), or none
- **Look:** existing legal docs; scheduled cleanup jobs and their interval.
- **Ask:** "Do you have a retention and destruction policy, and how often do you run periodic
  deletion?" Recommend a policy when `facts.registrations.privacy_regulator` has a `tr` entry
  with status `registered` (the Regulation requires it of controllers that must register), and
  periodic deletion every 6 months, the Regulation's longest interval.

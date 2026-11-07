# Catalog

Every item the write branch can produce, with the questions that decide whether a product
needs it. Step 1 of the write branch answers each row's trigger question, here and in the
`catalog.md` of every region in `facts.users.regions`. Only items with a built skeleton are
listed; a document the user needs that no catalog lists is built on demand (`SKILL.md`
*Build branch*).

Columns:

- **Id:** the `doc_id`; also the output file name, `legal/<doc-id>.md`.
- **Kind:** `document`, `form`, `template` or `task` (each has its own format file).
- **Trigger question:** asked or answered from the code; "yes" means needed. A region-triggered
  item's trigger is the condition in `formats/region-format.md` *block*.
- **Skeleton:** path from this folder.

| Id | Title | Kind | Family | Trigger question | Skeleton |
|---|---|---|---|---|---|
| privacy-policy | Privacy Policy | document | privacy-notices | Does the product collect any personal data (accounts, email, analytics, crash reports, device identifiers, payments), or is it listed on the App Store or Google Play? Both stores ask every app for a privacy policy link. | `skeletons/privacy-policy.md` |
| terms-of-service | Terms of Service | document | terms | Do users create accounts, pay, or publish content in the product? | `skeletons/terms-of-service.md` |
| eula | End User License Agreement | document | terms | Do users install the software (a desktop app, CLI, plugin or extension), or will a store app use its own licence in place of Apple's standard EULA? A mobile-only app can rely on Apple's standard EULA, so say so rather than writing one. | `skeletons/eula.md` |
| subscription-terms | Subscription Terms | document | commerce | Does the product sell auto-renewing subscriptions? `facts.sales.subscription_terms_placement` then decides whether they are their own file or a part of the terms of service. | `skeletons/subscription-terms.md` |
| refund-policy | Refund Policy | document | commerce | Does the product take payment, through an app store or directly? | `skeletons/refund-policy.md` |
| cookie-policy | Cookie Policy | document | privacy-notices | Does the product's website or web app set cookies or similar trackers beyond strictly necessary ones (analytics, ads, session replay, embedded videos or social widgets)? Answer from `facts.data.tracking`. With strictly necessary cookies only, or for an app with no website, the privacy policy's cookies section is enough, so say so rather than writing one. | `skeletons/cookie-policy.md` |
| account-deletion | Account / Data Deletion page | document | privacy-notices | Can users create an account? Both stores ask for a way to delete it, and Google Play for a public web link to that way. | `skeletons/account-deletion.md` |
| oss-notices | Open Source Notices | document | licensing | Does the shipped product (a mobile or desktop app, a web client's bundle, bundled fonts or models) contain open-source or other third-party components? Answer from `facts.product.third_party_components`; almost every app does. If an in-app acknowledgements screen already shows every component and its licence and no web page is wanted, say so rather than writing one. | `skeletons/oss-notices.md` |
| data-subject-request | Data Subject Request Form | document | privacy-notices | Does the product keep personal data about the people who use it (accounts, contact details, orders, analytics or device identifiers)? Data protection laws let those people ask for a copy, a correction or deletion, and a request form gives them one route with the details needed to find their data. If the product keeps no personal data, or users can already export, correct and delete everything in the app and a request email is enough, say so rather than writing one. | `skeletons/data-subject-request.md` |
| ropa | Record of Processing Activities | document | internal-compliance | Region-triggered: a region in `facts.users.regions` has `regions/<code>/ropa.md`. | `skeletons/ropa.md` |

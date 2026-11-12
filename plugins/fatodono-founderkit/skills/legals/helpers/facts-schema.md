# Facts schema

Every fact a skeleton can name, with how to find it. Skeletons name keys only; this file is the
one place that says what a key means, how to ask for it, and where to look in code. The build
branch adds keys here; the write branch reads them.

## Keys

A key is `facts.<group>.<name>` in snake_case. Groups: `company`, `product`, `data`,
`processors`, `sales`, `users`, `marketing`, `registrations`, `contractor`. Reuse a key whenever
the meaning matches, even if the wording in a skeleton differs. Keys only one region uses are
`facts.<code>.<name>` in `regions/<code>/facts.md` (`formats/region-format.md`), never here.

Each key:

```markdown
### facts.company.legal_name
- **Means:** the registered name of the entity that offers the product.
- **Type:** string        # string | bool | number | date | enum [a, b] | list of <type or fields>
- **Look:** where the scanner finds it: files, config keys, SDKs, API calls, existing legal
  docs. "Not in code" when code cannot show it.
- **Ask:** the question put to the user when the scan finds nothing, and how to pick the
  recommended answer.
```

## `legal/facts.md`

The user's facts live in `legal/facts.md` in their repo. `code-scanner` writes it, the main
agent completes it, every writer and the checker read it. One entry per key a chosen skeleton
names:

```markdown
## facts.company.legal_name
- Value: Example Teknoloji A.Ş.
- Source: user, 2026-11-02
- Status: answered
```

- **Value:** plain text, or a YAML block for lists and records, at the level the key's *Means*
  and *Type* set: a list of safeguards in general terms stays general, a cookie list keeps each
  cookie's name and duration. The code-level detail behind it (field names, settings, limits,
  hostnames) lives at the *Source* path, so the file can sit in a public repo.
- **Source:** `code <path>:<line>`, `doc <path>` (an existing legal document), or
  `user, <date>`.
- **Status:**
  - `found`: the scan found it in code or an existing document.
  - `missing`: the scan found nothing; the main agent asks.
  - `conflict`: code and an existing document disagree; both values are listed and the main
    agent asks.
  - `answered`: the user gave it; "none" and "declined" are answers.
- **Hint:** on a `missing` entry only, what the scan saw that bears on the answer (the store
  seller name, a currency list); the main agent recommends from it.

A key is settled when its status is `found` or `answered`.

A key whose *Look* ends with "The user decides." is a choice the code cannot make: it is never
`found`. The scan writes it as `missing` with everything it saw in the *Hint*, so the user is
always asked.

## Company keys

### facts.company.legal_name
- **Means:** the registered name of the entity that offers the product.
- **Type:** string
- **Look:** existing legal docs, App Store / Play seller name in fastlane or store metadata,
  copyright lines in the app or website footer.
- **Ask:** "What is the registered name of the company (or your full name, if you sell as an
  individual)?" Recommend the seller name found in store metadata.

### facts.company.country
- **Means:** the country where the entity is registered.
- **Type:** string (ISO 3166-1 alpha-2)
- **Look:** existing legal docs, store metadata, address in the website footer.
- **Ask:** "In which country is the company registered?" Recommend the country of the
  address found, if any.

### facts.company.address
- **Means:** the entity's registered postal address.
- **Type:** string
- **Look:** existing legal docs, website footer or contact page in the repo.
- **Ask:** "What is the company's registered address?" No recommendation.

### facts.company.contact_email
- **Means:** the address users write to about privacy and legal matters.
- **Type:** string
- **Look:** existing legal docs, support email in store metadata, `mailto:` links in the app
  or website.
- **Ask:** "Which email should users write to about privacy and legal questions?" Recommend
  the support email found.

### facts.company.dpo_contact
- **Means:** the data protection officer's name or role and contact, if one is appointed.
- **Type:** string
- **Look:** existing legal docs; `dpo@` or `privacy@` addresses in the app, website or store metadata.
- **Ask:** "Have you appointed a data protection officer? If so, how do users reach them?" Recommend "none appointed" for a company under 250 people with no large-scale sensitive processing.

### facts.company.group_companies
- **Means:** affiliates that receive or process users' data, with their role.
- **Type:** list of (name, country, role)
- **Look:** existing legal docs; store seller names that differ from the company; copyright lines.
- **Ask:** "Do any parent, sister or subsidiary companies receive users' data? Name each and what it does." Recommend "none" when nothing in the repo names another entity.

### facts.company.collects_applicant_data
- **Means:** whether job applicants' data is collected through the product's website.
- **Type:** bool
- **Look:** careers or jobs pages and application forms in the website code.
- **Ask:** "Do you collect job applications through your website?" Recommend "no" when no careers page exists.

### facts.company.change_notice
- **Means:** how, and how far ahead, users are told about material changes: to the terms and
  policies, and to prices or plans.
- **Type:** list of (change: enum [documents, prices], channels: list of enum [posting, email, in-app, store], days: number, applies_from: enum [posting, end-of-notice, next-renewal])
- **Look:** existing legal docs; in-app announcement or "what's new" mechanisms; email sending
  code; store price-increase consent flows (Apple and Google ask existing subscribers to accept
  increases).
- **Ask:** "How will you tell users about important changes to your terms and policies, and how
  far ahead will you tell them about price or plan changes?" For documents, recommend "posting
  plus in-app" for an app with accounts, "posting plus email" when email is collected. For
  prices, recommend 30 days by email and in-app, effective from the next renewal.

### facts.company.phone
- **Means:** a phone line users and buyers can call about the service, orders, returns and
  complaints, if the company offers one.
- **Type:** string or none
- **Look:** website footer, contact page, support settings, store metadata (App Store support
  phone, Play *About the developer*).
- **Ask:** "Is there a phone number users can call about the service, orders or complaints? If
  so, which?" Recommend the number on the contact page; none unless a support line is
  published.

### facts.company.published_policies
- **Means:** the company's other public legal documents that a document points to or makes part
  of itself (privacy policy, acceptable use policy, community guidelines, refund policy,
  subscription terms, copyright policy), with their URLs.
- **Type:** list of (title, url, incorporated: bool)
- **Look:** existing legal docs, footer and settings links in the app and website, the documents
  the current write run produces.
- **Ask:** "Which other policies should the terms link to, and which should be part of the
  terms?" Recommend every document this run writes plus those already published, with the
  privacy policy linked but not incorporated.

### facts.company.governing_law
- **Means:** the law that governs the terms and the courts where disputes go when they go to
  court.
- **Type:** record (law: country or state, courts: city or district)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Which law should govern the terms, and which city's courts should hear disputes?"
  Recommend the law and courts of the company's registered seat (`facts.company.country`,
  `facts.company.address`).

### facts.company.dispute_forum
- **Means:** how disputes with users are resolved: in court, or by binding individual
  arbitration; and whether an informal step comes first.
- **Type:** record (forum: enum [courts, arbitration], informal_first: bool, provider)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Should disputes go to court, or to binding individual arbitration? Do you want users
  to contact you first to try to settle?" Recommend courts with an informal step first;
  arbitration only on the advice of a lawyer in a country where consumer arbitration is
  enforceable.

### facts.company.liability_cap
- **Means:** the cap on the company's total liability to a user, if any.
- **Type:** record (basis: enum [greater-of, fees-paid, fixed, none], months, amount, currency)
- **Look:** existing legal docs. Not in code.
- **Ask:** "Should the terms cap your liability? A common choice is the greater of what the user
  paid in the last 12 months or a small fixed amount." Recommend `greater-of`, 12 months, 100 in
  the company's currency.

### facts.company.internal_activities
- **Means:** processing the company does for running itself rather than for the product:
  staff and payroll, recruitment, contractors, suppliers and bookkeeping, customer support,
  sales contacts, events.
- **Type:** list of (activity, data subjects, data, tool or provider)
- **Look:** existing legal docs (privacy policy, job pages); careers pages and application
  forms in the website code; support desk, CRM and accounting SDKs or integrations (Zendesk,
  Intercom, HubSpot, Xero, Stripe Billing). Payroll and HR are not in code.
- **Ask:** "Besides the product, which of these do you handle: staff and payroll, job
  applicants, contractors, suppliers and invoices, customer support, sales leads? For each,
  which tool do you use?" Recommend the activities the scan found plus "suppliers and
  invoices", which every company has; ask about staff only when the company has employees.

### facts.company.joint_controllers
- **Means:** other organisations that decide together with the company why and how some
  personal data is processed (a co-branded service, a research partner, a parent company that
  sets the purposes).
- **Type:** list of (name, contact, activity)
- **Look:** existing legal docs; partner agreements. Not in code.
- **Ask:** "Do you decide jointly with another organisation why and how any personal data is
  used (a co-branded service, a shared programme)? Name each." Recommend "none".

### facts.company.acts_as_processor
- **Means:** whether the company processes personal data on behalf of business customers,
  who decide the purposes (a B2B SaaS holding its customers' end users' data).
- **Type:** bool
- **Look:** team, workspace or organisation features where a customer's admin controls other
  people's accounts; a customer DPA among existing legal docs; business plans in pricing.
- **Ask:** "Do business customers use the product to handle their own people's data (their
  staff, their clients), with you acting on their instructions?" Recommend "yes" when
  workspace or admin features exist.

### facts.company.processor_customers
- **Means:** the business customers the company processes personal data for as a processor
  (GDPR Art. 30(2)(a)): each customer with a contact, or the customer categories and where the
  full list is kept.
- **Type:** record (customers: list of (name, contact) or categories, list_location)
- **Look:** customer DPAs among existing legal docs; workspace or organisation tables and
  admin or billing contacts in the data model; the CRM. Customer names are not in code.
- **Ask:** "You process data for business customers. Should the record name each customer
  with a contact, or name customer types and point to where your customer list is kept?"
  Recommend the pointer when there are more than about 20 customers.

### facts.company.privacy_owner
- **Means:** the person or role who keeps the record of processing up to date, and how often
  it is reviewed.
- **Type:** record (role, name, review interval)
- **Look:** existing legal docs; CODEOWNERS or security contacts. Not otherwise in code.
- **Ask:** "Who keeps this record up to date, and how often will it be reviewed?" Recommend
  the founder or DPO, reviewed every 12 months and whenever a new feature or provider handles
  personal data.

## Product keys

### facts.product.name
- **Means:** the product's public name.
- **Type:** string
- **Look:** app display name (`Info.plist` `CFBundleDisplayName`, Android `app_name`, `pubspec.yaml` `name`, `package.json` `productName`), store metadata.
- **Ask:** "What is the product called?" Recommend the store display name.

### facts.product.category
- **Means:** the product's field, as the stores file it, used to pick look-alike apps when a
  skeleton is built for this user.
- **Type:** record (store_category: string, keywords: list of string)
- **Look:** App Store primary genre and Play category in store metadata (fastlane
  `primary_category`, Play listing files); keywords from the store description.
- **Ask:** "What kind of app is it?" Recommend the store category found, with two or three words
  from the description ("Productivity: note-taking, handwriting").

### facts.product.language
- **Means:** the language the documents are written in, as an ISO 639-1 code. A document from a
  region's `catalog.md` is written in that region's first `languages` entry instead. The skill
  does not translate.
- **Type:** string
- **Look:** the language of existing legal documents, the app's localizations (`*.lproj`,
  Android `values-<lang>`, `l10n`/`i18n` folders, `supportedLocales`), store listing languages.
- **Ask:** always, even when the code shows it: "Which language should the documents be written
  in? You can translate them into other languages yourself afterwards, in any way you like.
  Documents that only one country's law requires are written in that country's language (for
  Turkey: Turkish)." Recommend the language of the existing documents, else the main language
  of the users' regions.

### facts.product.services_in_scope
- **Means:** every app, website and service the documents cover: the ones users or customers
  use. A backend or API that serves only the product's own apps is part of those apps; a public
  API that customers call is a service of its own. A tool only staff or developers use (an
  internal tools page, admin scripts, CI, staging, a developer docs site) is not one.
- **Type:** list of (name, kind [ios, android, macos, windows, web, api, other], url, used_by
  [public, customers, staff, developers])
- **Look:** platform folders in the repo (`ios/`, `android/`, `macos/`, `web/`), store
  metadata, website domains and subdomains in config, admin and internal tools, developer
  tooling. List each with who uses it. The user decides.
- **Ask:** "The documents will cover <the services users or customers use>, and leave out <the
  staff and developer tools>, since only your team uses them. Right?" Recommend exactly that
  split; never recommend a staff or developer tool.

### facts.product.has_accounts
- **Means:** whether users create accounts.
- **Type:** bool
- **Look:** sign-up and sign-in code, auth SDKs (Firebase Auth, Sign in with Apple, Google Sign-In, Auth0, Supabase).
- **Ask:** "Do users create an account?" Recommend what the code shows.

### facts.product.min_age
- **Means:** the minimum age to use the product.
- **Type:** number
- **Look:** age gates in code, store age rating, terms of service.
- **Ask:** "What is the minimum age to use the product?" Recommend 13; a region may add a higher age in its own facts.

### facts.product.child_directed
- **Means:** whether the product is directed to children (in the sense of children's privacy laws, Play Families, Apple Kids category).
- **Type:** bool
- **Look:** store category and age rating, kids or parental-control features.
- **Ask:** "Is the product made for children under 13?" Recommend "no" unless the store category is Kids or the content targets children.

### facts.product.public_content
- **Means:** whether users' content or profiles can be seen by other users or the public.
- **Type:** enum [none, shared-with-chosen-users, public]
- **Look:** sharing, collaboration, public profile, feed or link-sharing features.
- **Ask:** "Can other users or the public see anything a user creates?" Recommend what the code shows.

### facts.product.features
- **Means:** features users or customers meet that have their own data flow a general data
  category does not explain (sync, backup, contact matching, audio recording, payments inside
  the app, voice input). A mode or tool only staff can open is not one: the data it touches is
  covered by the purposes and recipients.
- **Type:** list of (name, data, where processed, third party, retention)
- **Look:** feature modules; permission requests (`NS*UsageDescription`, Android `uses-permission`); background services; cloud upload code.
- **Ask:** "Which features handle data in a special way? For each, what data, where it goes and how long it is kept." Recommend the list the scan built.

### facts.product.ai_features
- **Means:** features that send data to an AI model or use data to train one.
- **Type:** list of (name, data sent, provider, on-device or server, trains models)
- **Look:** AI SDKs and API calls (OpenAI, Anthropic, Gemini, Vertex, Core ML, ML Kit, TensorFlow Lite), prompt code.
- **Ask:** "Does any feature use AI? For each, which data is sent, to which provider, and is it used for training?" Recommend "no training" unless the code or provider terms say otherwise.

### facts.product.integrations
- **Means:** third-party services the user can connect, which then receive or send data.
- **Type:** list of (name, data exchanged)
- **Look:** OAuth clients, connector code, import and export to other services (Google Drive, Dropbox, calendars, health platforms).
- **Ask:** "Which outside services can users connect, and what data moves?" Recommend the list the scan built.

### facts.product.platform_disclosures
- **Means:** statements a platform requires in the policy, such as the Google API Services User Data Policy (Limited Use) or Google Play health-app disclosures.
- **Type:** list of (platform, requirement, scopes or data)
- **Look:** Google OAuth scopes in code (`drive`, `gmail`, `calendar`), HealthKit or Health Connect use, store health declarations.
- **Ask:** "Your app uses <scopes>. Google requires a Limited Use statement in the policy. Include it?" Recommend yes whenever restricted or sensitive Google scopes are requested.

### facts.product.business_use
- **Means:** whether organisations use the product as such: team or organisation accounts,
  accounts made on behalf of a company, brand accounts, admins who control members' accounts.
- **Type:** record (org_accounts: bool, admin_control: bool, separate_business_terms_url) or none
- **Look:** team, workspace, organisation or admin models; domain-based account linking; seat
  billing; business plans in pricing code.
- **Ask:** "Can companies or schools use the product as an organisation, with admins over their
  members' accounts?" Recommend what the code shows; none for a single-user app.

### facts.product.offsite_components
- **Means:** code the company runs on other parties' sites or apps that sets or reads its own
  cookies or identifiers there: share or follow buttons, embeddable widgets, a sign-in or
  checkout button for partners, an ad or conversion tag customers install, an SDK other apps
  embed.
- **Type:** list of (name, kind [plugin, widget, sign-in, tag, sdk], data collected)
- **Look:** published embed scripts, partner SDKs or packages, "add to your site" docs, partner
  OAuth or sign-in buttons the company provides.
- **Ask:** "Do you offer anything other sites or apps embed (buttons, widgets, sign-in, a tag or
  SDK) that sets your cookies there?" Recommend none unless such a component ships.

### facts.product.beta_features
- **Means:** whether the product offers beta, preview or early-access features to users.
- **Type:** bool
- **Look:** feature flags exposed to users, "beta" or "labs" labels, TestFlight or Play testing
  tracks offered publicly.
- **Ask:** "Do users get beta or preview features?" Recommend what the code shows.

### facts.product.risk_domains
- **Means:** areas where users might rely on the product's information or features in ways that
  risk their health, money, safety or legal position, which call for a specific disclaimer.
- **Type:** list of enum [health, fitness, mental-health, finance, tax, legal, navigation, outdoor-safety, other]
- **Look:** app category, health or finance SDKs (HealthKit, Health Connect, Plaid), workout,
  diagnosis, budgeting or route features, store age-rating and category answers.
- **Ask:** "Could users rely on the app for health, financial, legal or safety decisions?"
  Recommend the domains the category and code suggest; none for a general productivity tool.

### facts.product.deletion_routes
- **Means:** every way a user can delete their account: in the app, on the website, or by a
  request (email, web form, support), with the path or address and whether the user must be
  signed in.
- **Type:** list of (route [in-app, web, email, form, support], path or address, needs_sign_in: bool, platforms)
- **Look:** delete-account screens and API calls (`deleteUser`, `DELETE /account`, Firebase
  `user.delete()`, Supabase admin delete), settings menus, website account pages, support email
  in store metadata.
- **Ask:** "How can users delete their account: in the app, on the website, by email? Give the
  menu path or address for each." Recommend the in-app path the scan found plus the support
  email as the route for users who cannot sign in.

### facts.product.deletion_verification
- **Means:** how a deletion is confirmed and how the requester's identity is checked: confirm
  dialog, typed word, password or code re-entry, email confirmation link, completion email,
  identity details asked for in an emailed request.
- **Type:** record (in_product: list of string, request: list of string, completion_notice: bool)
- **Look:** the delete flow's dialogs and re-authentication calls (`reauthenticate`), emails
  sent on deletion (templates, transactional email code).
- **Ask:** "How is a deletion confirmed, and how do you check that an emailed request comes
  from the account owner?" Recommend "confirm dialog in the app; requests must come from the
  account's email address".

### facts.product.deletion_grace_period
- **Means:** time after a deletion request during which the account is only deactivated and can
  be restored, and how the user restores it.
- **Type:** record (days: number, restore_by [sign-in, email-link, support]) or none
- **Look:** soft-delete flags (`deleted_at`, `scheduled_deletion`), purge jobs and their delay,
  restore or reactivate code.
- **Ask:** "After a user asks to delete their account, can they change their mind for some days?
  How?" Recommend none when deletion runs at once in code.

### facts.product.deletion_blockers
- **Means:** what the user must do first, or what stops a deletion: an active subscription, a
  balance or open orders, an admin role over other users, devices to unlink, a blocked account.
- **Type:** list of (condition, what the user does)
- **Look:** checks in the delete flow that return early or show a warning; wallet, order,
  family-sharing or team-admin code.
- **Ask:** "Must users do anything before they can delete their account, or can anything stop
  it?" Recommend what the delete flow's checks show; "none" if it has none.

### facts.product.deletion_alternatives
- **Means:** lighter options the product offers instead of deleting: deactivate or pause,
  downgrade to a free plan, sign out. Deleting single items is
  `facts.product.data_deletion_controls`.
- **Type:** list of (option, effect, path)
- **Look:** deactivate or pause flags, plan downgrade screens.
- **Ask:** "Can users deactivate their account or downgrade instead of deleting it?" Recommend
  the options the code shows.

### facts.product.account_roles
- **Means:** kinds of account or membership that delete differently: business or organisation
  accounts managed by an admin, family or household owners and members, secondary profiles,
  accounts held by partners, accounts of deceased users.
- **Type:** list of (role, how deletion differs)
- **Look:** team, organisation, family or household models; admin roles; SSO-managed
  workspaces; partner account linking.
- **Ask:** "Are there account types (team admin, family member, business) that delete
  differently?" Recommend "none" when the code has a single account type.

### facts.product.data_deletion_controls
- **Means:** controls that delete specific data without closing the account (single items,
  history, backups, synced contacts) and the request route for the rest.
- **Type:** list of (data, path)
- **Look:** per-item delete actions, "clear history" settings, backup management screens.
- **Ask:** "Can users delete parts of their data without deleting the account? Where?"
  Recommend the controls the scan found.

### facts.product.eula_acceptance
- **Means:** where the user meets and accepts the licence agreement for installed software.
- **Type:** list of enum [installer-dialog, first-launch, checkout-checkbox, account-signup, store-listing, use-only]
- **Look:** installer licence settings (DMG `SLA` resources, NSIS `LicenseData`, Inno Setup
  `LicenseFile`, WiX `WixUILicenseRtf`, electron-builder `license`); first-launch agreement
  screens; a terms checkbox at checkout; the store listing's *License Agreement* link (App Store
  Connect custom EULA).
- **Ask:** "Where do users agree to the licence: in the installer, on first launch, at checkout,
  or only by using the app?" Recommend what the code shows; `store-listing` plus `use-only` for a
  store app with no in-app screen.

### facts.product.licence_terms
- **Means:** how the installed software is licensed: the licence models sold or given, what one
  licence covers, the permitted use, backup copies, whether a licence can pass to another person,
  and whether organisations must report usage.
- **Type:** record (models: list of enum [perpetual, subscription, free, trial, educational, oem, other], unit: enum [device, user, seat, site, none], limit: number, use: enum [personal, commercial, both], backup_copies: bool, transfer: enum [none, with-consent, allowed-with-conditions], usage_reporting: bool)
- **Look:** licence-key and entitlement code (Paddle, Lemon Squeezy, Keygen, Gumroad licence API,
  FastSpring, RevenueCat entitlements), device or seat checks and their limits, trial timers, free
  tiers, education discounts, the pricing page; for store-only apps, the store's own usage rules.
- **Ask:** "How is the software licensed: one-off purchase, subscription, free, trial? Does one
  licence cover a device, a user or a number of seats, for personal or commercial use? Can a
  buyer pass the licence on?" Recommend what the code shows. With nothing found: for a store-only
  app, devices the user owns or controls under the store's rules, personal use, no transfer; for
  direct desktop sales, one user on their own devices, commercial use allowed, transfer with
  consent. `usage_reporting` only for seat licences sold to organisations.

### facts.product.activation
- **Means:** how the software checks that a licence is valid: licence key, account sign-in or
  online check; whether it contacts the company's servers to do so; and what happens when the check
  fails or a licence expires.
- **Type:** record (method: enum [licence-key, account, online-check], phones_home: bool, offline_grace_days: number, on_failure: enum [stops, reduced-features, nag, none]) or none
- **Look:** licence validation calls and their endpoints, key formats, offline grace timers,
  feature gates on expiry, anti-tamper or DRM libraries.
- **Ask:** "Does the software check a licence key or account, online or offline, and what
  happens if the check fails?" Recommend what the code shows; none for a free app or one sold only
  through a store.

### facts.product.system_requirements
- **Means:** the platforms, minimum OS versions and connectivity the software needs.
- **Type:** record (platforms: list of string, min_os: list of (platform, version), internet: enum [required, some-features, none]) or none
- **Look:** deployment targets (Xcode `MACOSX_DEPLOYMENT_TARGET`, `IPHONEOS_DEPLOYMENT_TARGET`;
  Android `minSdkVersion`; Electron and Windows manifests); network calls the core features need.
- **Ask:** "Which platforms and minimum OS versions do you support, and does the software need
  internet access?" Recommend the deployment targets found.

### facts.product.update_policy
- **Means:** how updates reach users and what a licence includes: automatic or manual delivery,
  mandatory updates, which updates are free, paid upgrades, and how long old versions are
  supported.
- **Type:** record (delivery: enum [store, automatic, automatic-with-opt-out, manual], mandatory: bool, free_updates: enum [all, major-version, period, none], period_months: number, paid_upgrades: bool, old_versions: string)
- **Look:** updater frameworks and settings (Sparkle `SUAutomaticallyUpdate`, Squirrel,
  electron-updater, WinSparkle), forced-update or minimum-version checks, upgrade pricing in
  licence code or the pricing page.
- **Ask:** "Do updates install automatically? Are all updates free, or only those within a major
  version or a period? How long do you support old versions?" Recommend the store or updater
  settings found; free updates for the licence's life when there are no paid upgrades.

### facts.product.third_party_components
- **Means:** open-source and other third-party code shipped inside the software, where users find
  the notices, and whether any licence requires offering source code. Only what reaches the user
  counts (the app, the desktop build, the web client's bundle, bundled fonts and models); server-side
  dependencies that are never shipped are left out.
- **Type:** record (components: list of (name, licence, version, copyright, url, kind [library, font, model, asset, sdk, other], target, notice: bool), notices_at: string, other_copies: list of (where, location), generator: string, copyleft: bool, source_offer: bool) or none
- **Look:** lockfiles and manifests of the shipped targets (`Package.resolved`, `Podfile.lock`,
  `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `build.gradle` or `gradle.lockfile`,
  `pubspec.lock`, `Cargo.lock`, `go.sum`), skipping devDependencies and server-only packages;
  bundled LICENSE, COPYING and NOTICE files (`node_modules/*/NOTICE`, `META-INF/NOTICE` in jars,
  which set `notice`); notice generators already in the build (`oss-licenses-plugin` /
  `play-services-oss-licenses`, AboutLibraries, CocoaPods `Acknowledgements.plist`, LicensePlist,
  Flutter `LicenseRegistry` / `showLicensePage`, `license-checker`, `generate-license-file`,
  `cargo-about`, `go-licenses`, `pip-licenses`, Electron's `LICENSES.chromium.html`), which give
  `generator` and an in-app screen for `other_copies`; acknowledgements screens or `Settings.bundle`
  acknowledgements; font files with `OFL.txt`; model files (`.onnx`, `.tflite`, `.mlmodel`, `.gguf`)
  and their model cards. GPL, LGPL, AGPL or MPL entries mark `copyleft`. `target` is the platform or
  build the component ships in (ios, android, web, macos, windows); `other_copies` lists where else
  the notices live (an in-app screen, a text file in the download).
- **Ask:** "The scan found these open-source components: <list>. Where can users read their
  licences: an in-app screen or a web page?" Recommend the in-app acknowledgements screen if one
  exists, else a web page. The optional fields (`version` onward, `other_copies`, `generator`) are
  filled from the scan, not asked.

### facts.product.source_code_offer
- **Means:** how the company gives users the source code of copyleft components it ships: a
  download link or a written offer, where requests go, what a request must contain, for how long
  and at what cost.
- **Type:** record (method: enum [download, written-offer, both], download_url: string, request_channel: string, request_details: list of string, valid_years: number, cost: enum [free, media-and-shipping]) or none
- **Look:** GPL, LGPL, AGPL or MPL entries in `facts.product.third_party_components`; `COPYING` and
  `COPYING.LESSER` files; native libraries built from copyleft code (`jniLibs/*.so`, `.dylib`,
  `.framework`, FFmpeg or GStreamer builds); firmware or kernel images; an existing source archive
  or mirror repository. The request channel is not in code.
- **Ask:** "The build ships <copyleft components>. Their licences require you to give users the
  source code. Will you link to a download of the exact sources, or offer it on request? Which email
  or address takes requests?" Recommend a download link plus the contact email for requests; with no
  download, a written offer valid three years, free except media and shipping, which is the form
  the samples use.

### facts.product.data_attributions
- **Means:** third-party data or content in the product, other than code, whose licence or
  supplier requires an attribution line: map data and tiles, geocoding, datasets, model training
  data.
- **Type:** list of (source, licence, required_notice, url) or none
- **Look:** map SDKs and tile or style URLs (Mapbox, MapLibre styles, OpenStreetMap tiles, TomTom,
  HERE, Google Maps) and the attribution strings in their style JSON; bundled datasets with a licence
  file (ODbL, CC BY); model cards naming a training-data licence.
- **Ask:** "The product shows <sources>. Their licences ask for an attribution line. Add it to the
  open source notices?" Recommend each supplier's standard attribution text.

### facts.product.support
- **Means:** whether the company supports the software, how, and for which versions.
- **Type:** record (offered: enum [none, discretionary, included, paid], channels: list of string, supported_versions: string)
- **Look:** support email in store metadata, help-centre links, in-app support or chat SDKs
  (Intercom, Zendesk, Crisp), paid support plans in pricing code.
- **Ask:** "Do you support the software? Through which channels, and for which versions?"
  Recommend `discretionary` with the support email found, which most small-company samples state.

### facts.product.bundled_content
- **Means:** content shipped with the software for use in the user's own work (templates,
  samples, loops, fonts, stock media, presets), and the rules for using it.
- **Type:** list of (kind, own_work_use: bool, commercial_use: bool, attribution: string, standalone_redistribution: bool) or none
- **Look:** asset folders and content packs in the bundle or downloaded by the app, font files,
  template galleries, stock-media SDKs.
- **Ask:** "Does the software ship content users can put in their own work (templates, samples,
  fonts, stock media)? Can they use it commercially?" Recommend own-work and commercial use
  allowed, no redistribution as standalone files.

### facts.product.software_warranty
- **Means:** whether the company promises anything about the software itself, or provides it as
  is.
- **Type:** record (kind: enum [as-is, limited], days: number, remedy: enum [repair-or-replace, refund, either])
- **Look:** existing legal docs. Not in code.
- **Ask:** "Do you promise that the software works as documented for a period, or provide it
  as is?" Recommend `as-is`, which most samples choose; a limited warranty only when the company
  already offers one.

## Data keys

### facts.data.collected
- **Means:** the personal data the product collects, by category.
- **Type:** list of (category, examples, source [user, automatic, third-party], required or optional)
- **Look:** data models and database schemas, form fields, analytics events, crash and log payloads, SDKs in `pubspec.yaml`, `package.json`, `Podfile`, `build.gradle`, permission requests.
- **Ask:** "The scan found these data categories: <list>. Is anything missing?" Recommend the scanned list.

### facts.data.third_party_sources
- **Means:** outside parties that send the company data about users.
- **Type:** list of (source, data received)
- **Look:** social sign-in, attribution SDKs (AppsFlyer, Adjust), app store server notifications, payment webhooks, enrichment APIs.
- **Ask:** "Do you receive data about users from anyone else (sign-in providers, app stores, partners)?" Recommend the list the scan built.

### facts.data.sensitive
- **Means:** special-category or sensitive data (health, biometric, precise location, sexual life, children's data, government IDs, financial account data).
- **Type:** list of (category, purpose, legal basis or consent)
- **Look:** HealthKit, Health Connect, location permissions with high accuracy, camera or microphone use for face or voice features, ID upload.
- **Ask:** "Do you process any of these sensitive types: <list>?" Recommend what the code shows.

### facts.data.purposes
- **Means:** why each data category is used.
- **Type:** list of (purpose, categories, legal basis [contract, legitimate interests, consent, legal obligation])
- **Look:** where each collected field is read: feature code, analytics, email sending, ad SDKs, fraud checks.
- **Ask:** "Here are the purposes inferred from the code: <list>. Correct anything wrong." Recommend contract for service delivery, legitimate interests for security and analytics, consent for marketing and ads.

### facts.data.automated_decisions
- **Means:** whether the product makes decisions with legal or similarly significant effects by automated means alone.
- **Type:** bool
- **Look:** scoring, eligibility or ban logic without human review.
- **Ask:** "Does the product decide anything important about users automatically, with no human review?" Recommend "no" unless such logic exists.

### facts.data.deidentified_use
- **Means:** whether de-identified or aggregated data is used or shared beyond the stated purposes.
- **Type:** bool
- **Look:** analytics exports, published statistics, research datasets.
- **Ask:** "Do you use or publish aggregated statistics that no longer identify anyone?" Recommend "yes" when analytics is used.

### facts.data.telemetry_controls
- **Means:** whether users can turn off the usage, diagnostic and crash data the installed
  software sends to the company, where, and what the default is.
- **Type:** record (opt_out: bool, path: string, default: enum [on, off]) or none
- **Look:** analytics or crash-reporting toggles in settings or the installer (Sentry, Crashlytics,
  TelemetryDeck, PostHog opt-out calls), consent prompts at first launch.
- **Ask:** "Can users turn off usage or crash reporting? Where, and is it on by default?"
  Recommend what the settings show; none when the software sends no such data.

### facts.data.tracking
- **Means:** cookies, SDKs and similar technologies that track users on the web or in the app.
- **Type:** list of (technology, provider, purpose [necessary, analytics, advertising, functionality], surface [web, app], names: list of string, party [first, third], duration, opt_out_url)
  The last four fields are optional: a cookie policy's cookie list uses them (cookie names, who
  sets the cookie, how long it lasts, the provider's own opt-out page); other documents need only
  the first four.
- **Look:** analytics and ad SDKs, `<script>` tags on the website, cookie banners, mobile ad IDs (`AdSupport`, `ADVERTISING_ID` permission). For names, party and duration: the consent tool's scan report or cookie declaration, `document.cookie` and `Set-Cookie` writes in the code, the SDKs' documentation.
- **Ask:** "The scan found these trackers: <list>. Anything missing?" Recommend the scanned list.

### facts.data.cookie_controls
- **Means:** how users make cookie choices in the product itself: the consent tool, the link or
  button that reopens it, the in-app path, any account setting for analytics or ad
  personalisation, whether choice is per category, and whether non-essential trackers stay off
  until the user chooses.
- **Type:** record (tool: string or none, link_label: string, app_path: string or none, account_path: string or none, per_category: bool, non_essential_default: enum [off-until-choice, on]) or none
- **Look:** consent-manager scripts and config (OneTrust, Cookiebot, CookieYes, Didomi, Osano,
  Termly, iubenda, Google Consent Mode defaults); footer links ("Cookie settings", "Privacy
  choices"); privacy or tracking toggles in app and account settings screens.
- **Ask:** "How do users accept, refuse or change cookies on your site and in the app? Do
  analytics and ad trackers wait until they choose?" Recommend the tool and footer link found,
  with non-essential trackers off until the user chooses; none when only strictly necessary
  cookies are set.

### facts.data.cookie_list
- **Means:** where the list of individual cookies and trackers is published, and how it is kept
  current.
- **Type:** record (location: enum [this-page, linked-page, consent-tool], url: string or none, kept_current: enum [manual, scanner]) or none
- **Look:** a cookie declaration or scan-report embed from the consent tool; a cookie table in
  existing legal docs; scheduled cookie scans in the consent-tool config.
- **Ask:** "Should the cookie policy list each cookie itself, link to a separate list, or point to
  your consent tool's list?" Recommend the consent tool's auto-updated list when a tool with a
  scanner is present, otherwise a table on the page.

### facts.data.ad_consent_frameworks
- **Means:** industry frameworks the product joins to pass users' ad choices to advertising
  vendors (IAB Transparency and Consent Framework, IAB Global Privacy Platform).
- **Type:** list of string
- **Look:** consent-manager config (TCF or GPP enabled, CMP id), `__tcfapi` or `__gpp` calls, ad
  tags reading a TC string.
- **Ask:** "Does your consent tool run the IAB consent framework for ad vendors?" Recommend an
  empty list unless the config enables it.

### facts.data.sells
- **Means:** whether personal data is sold or rented to others for money.
- **Type:** bool
- **Look:** ad SDKs that share identifiers for cross-context advertising, data-broker integrations.
- **Ask:** "Do you sell or rent users' personal data to anyone?" Recommend "no" unless a data-broker integration is present.

### facts.data.targeted_ads
- **Means:** whether data is used to show or measure targeted ads, inside or outside the product.
- **Type:** bool
- **Look:** ad SDKs (AdMob, Meta Audience Network, AppLovin), ad pixels on the website, ATT prompt.
- **Ask:** "Do you show targeted ads or run ad campaigns that use users' data?" Recommend what the code shows.

### facts.data.honors_gpc
- **Means:** whether the website treats Global Privacy Control as an opt-out.
- **Type:** bool
- **Look:** consent-manager configuration, `navigator.globalPrivacyControl` checks.
- **Ask:** "Does your website honour Global Privacy Control signals?" Recommend "yes" when targeted ads run on the website.

### facts.data.honors_dnt
- **Means:** whether the website changes behaviour on a Do Not Track signal.
- **Type:** bool
- **Look:** `navigator.doNotTrack` checks.
- **Ask:** "Does your website respond to Do Not Track?" Recommend "no", which is what most samples state.

### facts.data.storage_locations
- **Means:** countries where personal data is stored or processed.
- **Type:** list of country codes
- **Look:** cloud region settings (Firebase, AWS, GCP, Cloudflare), processor locations.
- **Ask:** "Where is users' data stored and processed?" Recommend the regions found in config.

### facts.data.retention
- **Means:** how long each data category is kept, as a period or a trigger.
- **Type:** list of (category, period or trigger, reason)
- **Look:** TTLs, cleanup jobs, account deletion code, backup and log retention settings.
- **Ask:** "How long do you keep <category>?" Recommend "until account deletion" for account data and the configured period for logs and backups.

### facts.data.deletion_lag
- **Means:** time from an account deletion request to full deletion, including backups.
- **Type:** string
- **Look:** account deletion code, backup rotation settings.
- **Ask:** "After a user deletes their account, how long until the data is gone, including backups?" Recommend 30 days.

### facts.data.security_measures
- **Means:** the main safeguards for personal data, in general terms (encryption in transit,
  access control by role), not how they are built.
- **Type:** list of string
- **Look:** TLS config, encryption at rest, auth (MFA, passkeys), access controls, on-device storage choices.
- **Ask:** "Which security measures should the policy name?" Recommend the measures found in code, stated in general terms.

### facts.data.subject_categories
- **Means:** the groups of people whose personal data the company processes.
- **Type:** list of enum [users, customers, website-visitors, newsletter-subscribers, children, employees, job-applicants, contractors, supplier-contacts, business-contacts, other]
- **Look:** account and profile models (users), payment and billing code (customers),
  analytics on the website (visitors), newsletter forms, careers pages, team or B2B features.
- **Ask:** "Whose personal data do you hold? The scan found: <list>." Recommend the scanned
  list plus supplier contacts.

### facts.data.other_recipients
- **Means:** parties other than the company's processors that receive personal data:
  independent controllers (payment networks, app stores, banks, accountants, auditors),
  public authorities (tax office, regulators), partners, and other users or the public where
  the product shows data to them.
- **Type:** list of (recipient, role [independent-controller, public-authority, partner, other-users, public], data, purpose)
- **Look:** payment and app-store integrations, tax and invoicing integrations, partner API
  clients, sharing and publishing features.
- **Ask:** "Apart from your service providers, who receives personal data from you (app
  stores, payment networks, accountants, tax office, partners)?" Recommend the scanned list
  plus the tax authority for invoicing data.

### facts.data.kept_after_deletion
- **Means:** data that survives account deletion, and why: backups until they expire, records
  kept for legal, tax or security reasons, de-identified or aggregated data, copies other users
  hold, data on the user's own device, records held by app stores or payment providers.
- **Type:** list of (data, reason, period or trigger, form [as-is, de-identified])
- **Look:** backup retention settings, purge job exclusions, audit or ledger tables, local
  storage that the delete flow does not clear, existing privacy policy retention text.
- **Ask:** "After an account is deleted, does any data remain (backups, invoices, logs, others'
  copies)? For how long and why?" Recommend the backup period from config and "invoices kept as
  tax law requires" when payments exist.

### facts.data.inactivity_deletion
- **Means:** whether accounts are deleted automatically after a period of inactivity, the
  period, and whether the user can change it.
- **Type:** record (months: number, user_adjustable: bool) or none
- **Look:** scheduled jobs that find and delete inactive accounts; last-seen fields used in a
  cleanup query.
- **Ask:** "Do you delete accounts automatically after a period of inactivity?" Recommend none
  unless such a job exists.

### facts.data.dpia_done
- **Means:** impact assessments done or planned, per activity.
- **Type:** list of (activity, status [not-needed, planned, done], date or link)
- **Look:** existing legal docs (`legal/` DPIA files). Not in code.
- **Ask:** "Have you assessed the privacy risk of any activity (a DPIA)? Which, and when?"
  Recommend "not needed" except for activities on sensitive data, children's data, or
  large-scale tracking, for which recommend "planned".

## Processors keys

### facts.processors.list
- **Means:** service providers that process personal data for the company.
- **Type:** list of (name, purpose, data, location)
- **Look:** SDKs and API clients (analytics, crash reporting, email, hosting, payments, support desk, AI providers).
- **Ask:** "The scan found these service providers: <list>. Anything missing?" Recommend the scanned list.

## Sales keys

### facts.sales.offer_type
- **Means:** what the company sells: physical goods, digital content (files, codes, recorded
  courses, software access, in-app content, subscriptions to content), services (live classes,
  consultancy), or a mix.
- **Type:** enum [physical, digital-content, service, mixed]
- **Look:** product models and checkout code (shipping address required or not), cart line
  types, download or licence delivery code, in-app purchase and subscription products.
- **Ask:** "Do you sell physical goods, digital content, services, or a mix?" Recommend what
  the checkout code shows.

### facts.sales.purchase_channels
- **Means:** every place a buyer can pay for the product (app stores, the company's own
  checkout, a merchant of record, another platform, a partner bundle, a reseller or retailer,
  an employer or organisation that pays for access), and who decides and pays refunds for
  purchases made there. Empty when nothing is sold.
- **Type:** list of (channel: enum [app-store, google-play, other-app-store, web-direct, merchant-of-record, other-platform, partner-bundle, organisation, reseller, retail-store, other], name, refunds_by: enum [store, company, merchant-of-record, reseller, partner], store_window)
- **Look:** in-app purchase and subscription SDKs (StoreKit, Play Billing, RevenueCat platforms
  and store configuration); web checkout (Stripe, Paddle, Lemon Squeezy, FastSpring: the last
  three are merchants of record); licence-key, gift-card or partner entitlement grants; team or
  organisation billing; platform folders (`ios/`, `android/`, `macos/`, `web/`).
- **Ask:** "Where can buyers pay: the App Store, Google Play, your website, resellers, a
  partner or an employer? For each, who handles refunds?" Recommend every channel the code
  integrates, with "store" refunding app-store purchases, "company" refunding `web-direct`
  purchases, and a merchant of record refunding under its own policy.

### facts.sales.subscription
- **Means:** recurring plans or recurring deliveries: billing periods, whether they renew
  automatically, whether a reminder goes out before renewal, how the buyer cancels on each
  channel, the cancellation deadline, and what happens after cancelling. Free trials are
  `facts.sales.free_trial`; what each plan includes, lifetime plans among them, is
  `facts.sales.plans`.
- **Type:** record (periods: list, auto_renews: bool, renewal_notice: bool, cancel_path: list of (channel, path), cancel_deadline, after_cancel: enum [access-to-period-end, immediate-end], data_after_end) or none
- **Look:** subscription SDKs and product configs (RevenueCat offerings, StoreKit product ids,
  Play Billing base plans, Stripe Billing prices, Paddle, iyzico subscription API);
  recurring-order jobs; renewal-reminder emails or jobs; "manage subscription" and cancel
  screens; downgrade-to-free code.
- **Ask:** "Do you sell subscriptions or recurring deliveries? If so, which billing periods, do
  they renew automatically, and how does a buyer cancel on each platform?" Recommend what the
  code and product configs show; "access to the end of the paid period" after cancelling, and
  the stores' own cancel paths for store purchases.

### facts.sales.plans
- **Means:** the paid plans and what each adds over the free tier, including lifetime plans, add-ons, credits or quotas, and where the price is shown.
- **Type:** list of (name, period [week, month, year, lifetime, other], includes, price_shown_at)
- **Look:** paywall screens and their strings, entitlement checks in code, RevenueCat entitlements and offerings, store product metadata, the pricing page.
- **Ask:** "Which paid plans do you offer, and what does each unlock?" Recommend the plans and entitlements found; price shown "in the app and the store before purchase".

### facts.sales.free_trial
- **Means:** the free trial: length, whether a payment method is needed, whether it converts to paid automatically, who is eligible, and any reminder before it ends.
- **Type:** record (length, payment_method_required: bool, converts_automatically: bool, eligibility, reminder: bool) or none
- **Look:** introductory-offer configuration (StoreKit free trial, Play free-trial phase, Stripe `trial_period_days`), trial-ending notifications.
- **Ask:** "Do you offer a free trial? How long, and does it turn into a paid plan automatically?" Recommend what the product configs show; eligibility "new subscribers only, once".

### facts.sales.plan_changes
- **Means:** how upgrades, downgrades and switches between plans work: timing and proration.
- **Type:** record (upgrade: enum [immediate-prorated, next-renewal], downgrade: enum [period-end, immediate]) or none
- **Look:** subscription groups and upgrade levels (StoreKit), Play replacement modes, Stripe proration settings.
- **Ask:** "Can subscribers switch plans? When does an upgrade or downgrade take effect?" Recommend the store defaults: upgrades immediately with proration, downgrades at the end of the period.

### facts.sales.shared_plans
- **Means:** family, household, team or group plans: how many members, who pays, who can cancel.
- **Type:** record (kind [family, household, team, group], max_members: number, payer_controls_cancel: bool) or none
- **Look:** Family Sharing flag on store products, team or seat models, invite flows.
- **Ask:** "Can one subscription cover several people? Who pays and who can cancel?" Recommend what the code shows.

### facts.sales.pause
- **Means:** whether subscribers can pause instead of cancelling, for how long and how often.
- **Type:** record (max_length, per_period_limit) or none
- **Look:** Play subscription pause setting, pause flows in the account settings, Stripe `pause_collection`.
- **Ask:** "Can subscribers pause their subscription?" Recommend what the store and provider settings show.

### facts.sales.paid_feature_limits
- **Means:** limits that apply to the paid features themselves: devices, simultaneous streams, household-only use, countries, usage quotas, storage periods.
- **Type:** list of (limit, value) or none
- **Look:** device-count or concurrency checks, quota counters, region locks, storage-retention settings tied to entitlements.
- **Ask:** "Do paid features have limits (devices, usage quotas, countries)?" Recommend the limits found in code.

### facts.sales.one_time_purchases
- **Means:** non-recurring purchases sold under the same terms: consumables, virtual currency, credits, rentals. Lifetime plans are `facts.sales.plans`.
- **Type:** list of (name, kind [consumable, credits, rental, other], refundable: bool, expiry) or none
- **Look:** non-consumable and consumable product ids in StoreKit, Play in-app products, RevenueCat non-subscription products, credit balances in code.
- **Ask:** "Do you sell anything that is not a subscription or plan (credits, rentals, items)?" Recommend what the product configs show.

### facts.sales.promotions
- **Means:** promotional programmes beyond the free trial: introductory prices, discounts,
  promo codes, referral rewards, win-back offers, and contests the company runs or users run
  through the product; with eligibility and what the price becomes afterwards. Gift cards and
  gifted plans are `facts.sales.gifts`.
- **Type:** list of (kind: enum [intro-price, discount, promo-code, referral, win-back, contest, user-contest], eligibility, price_after) or none
- **Look:** StoreKit promotional and offer codes, Play offers, RevenueCat or store offer codes,
  Stripe coupons and promotion codes, referral and invite-link rewards, contest or giveaway
  features.
- **Ask:** "Do you run discounts, promo codes, referral rewards or contests?" Recommend what
  the code and product configs show.

### facts.sales.gifts
- **Means:** purchases made for someone else: items or plans bought as gifts, gift
  subscriptions, gift cards and redemption codes; whether a gifted plan turns into a renewing
  subscription, whether gifts are refunded, and when they expire.
- **Type:** record (kinds: list of enum [gift-purchase, gift-subscription, gift-card, redemption-code], converts_to_renewal: bool, refundable: bool, expiry) or none
- **Look:** gift options and gift-message fields at checkout, gift purchase pages, offer or
  redemption code flows, gift-card and voucher models.
- **Ask:** "Can buyers buy your product as a gift, or do you sell gift cards or redemption
  codes?" Recommend what the checkout and code show.

### facts.sales.payment_methods
- **Means:** the payment methods offered on the company's own checkout.
- **Type:** list of enum [card, card-instalments, bank-transfer, cash-on-delivery, wallet, gift-card, other]
- **Look:** payment SDK and checkout configuration (Stripe, PayPal, Apple Pay, Google Pay,
  iyzico, PayTR), instalment tables, cash-on-delivery flags, card-updater settings.
- **Ask:** "Which payment methods can buyers use on your own checkout?" Recommend the methods
  configured at checkout; for store-only products, "handled by the store".

### facts.sales.payment_provider
- **Means:** the payment institution that processes the payments the company takes directly
  (not through an app store), and whether the company stores card data itself.
- **Type:** record (name, stores_card_data: bool, three_d_secure: bool) or none
- **Look:** payment SDKs and API clients; card-vault or tokenisation code.
- **Ask:** "Which payment provider processes your direct payments, and do you store card
  numbers yourselves?" Recommend "does not store card data" when only a provider's hosted form
  or token is used; none for store-only products.

### facts.sales.taxes
- **Means:** whether shown prices include tax, and who collects it.
- **Type:** enum [included, added-at-checkout, collected-by-store, mixed]
- **Look:** store pricing (stores show tax-inclusive prices in most countries and remit tax); Stripe Tax or tax settings on the web checkout; price strings with "+ tax".
- **Ask:** "Do your prices include tax?" Recommend `collected-by-store` for store-only products and `mixed` when web checkout adds tax.

### facts.sales.failed_payment
- **Means:** what happens when a renewal charge fails: retries, grace period, and the effect on access.
- **Type:** record (retries: bool, grace_days: number, effect: enum [suspend, downgrade-to-free, cancel], backup_method: bool)
- **Look:** billing-retry and grace-period settings (App Store billing grace period, Play grace period and account hold, Stripe Smart Retries and dunning), entitlement handling for `BILLING_ISSUE` events.
- **Ask:** "If a renewal payment fails, do you retry, and does the user keep access for a while?" Recommend the store and provider settings found; otherwise "access ends until payment succeeds".

### facts.sales.subscription_terms_placement
- **Means:** where the subscription terms are published: their own page, or a section of the terms of service.
- **Type:** enum [separate-page, tos-section]
- **Look:** existing legal docs (a `subscription`, `terms-of-sale` or `paid-terms` page, or a subscription heading inside the ToS); links in the paywall and settings screens.
- **Ask:** "Should the subscription terms be their own page, or a section of your terms of service?" Recommend `tos-section` when one product sells one or two plans; `separate-page` when there are several products, plan types or purchase channels.

### facts.sales.refund_rule
- **Means:** the company's general refund rule for what it sells directly: the stance, the
  window, what it covers, its conditions, and whether refunds outside the rule are possible.
  Purchases refunded by an app store or another seller follow `facts.sales.purchase_channels`.
- **Type:** record (stance: enum [money-back-window, case-by-case, no-refunds-except-law], window_days, window_start: enum [purchase, delivery, first-payment], covers: list of enum [first-purchase, renewals, one-time-purchases, add-ons], conditions: list of string, discretionary: bool, law_prevails: bool)
- **Look:** existing refund, terms or help pages; refund endpoints and their time checks
  (Stripe `refunds.create` guarded by a purchase-date check, admin refund tools, RevenueCat
  refund handling); usage counters that gate a refund.
- **Ask:** "Do you give refunds? If so, within how many days of purchase, for the first
  purchase only or for renewals too, and on what conditions?" Recommend what an existing
  refund or terms page says. With none: for subscriptions sold only through app stores,
  `no-refunds-except-law` with case-by-case exceptions, which most terms and subscription
  samples state; for direct sales, a 14- or 30-day window on the first purchase, the most common
  windows in refund samples. Always `law_prevails: true`.

### facts.sales.partial_refunds
- **Means:** whether the unused part of a paid period is refunded: on cancellation, or when
  the company discontinues the product. Proration on a plan change is
  `facts.sales.plan_changes`.
- **Type:** record (unused_time: enum [none, prorated, discretionary], on_discontinuation: bool)
- **Look:** refund-on-cancel settings in the billing provider (Stripe `prorate` on
  subscription cancel), cancellation code, existing terms on discontinuation.
- **Ask:** "Do you refund the unused part of a period when a subscriber cancels, or if you
  discontinue the product?" Recommend `none` for unused time, which the samples that address it most often
  state, and a pro-rata refund of prepaid fees on discontinuation.

### facts.sales.refund_exclusions
- **Means:** purchases and cases that are never refunded, including refusals for abuse,
  repeat requests, chargebacks or account termination.
- **Type:** list of (item or case, reason)
- **Look:** consumable in-app products and credits, gift-card or code products, lifetime
  plans, chargeback webhooks (`charge.dispute.created`) that lock accounts, refund-count
  checks.
- **Ask:** "Are any purchases or cases never refunded (credits, gift cards, renewals, used
  items, after a chargeback, after a ban)?" Start from the items marked non-refundable in
  `facts.sales.one_time_purchases` and `facts.sales.gifts` so the two answers agree; recommend
  those, plus "no refund after a chargeback is opened" when disputes are handled.

### facts.sales.refund_request
- **Means:** how a buyer asks for a refund: channel, steps, what to include, and whether the
  decision is automatic or manual.
- **Type:** record (channel: enum [email, support-ticket, chat, account-button, cancel-flow, returns-portal, contact-form, help-site, mail-in], contact, steps, required_info: list, decision: enum [manual, automatic])
- **Look:** support email in store metadata and `mailto:` links, in-app support or chat SDKs
  (Intercom, Zendesk, Crisp), refund buttons or cancel flows in account screens.
- **Ask:** "How do buyers ask you for a refund, and what should they include?" Recommend
  the support email with the account email and order or receipt number.

### facts.sales.refund_processing
- **Means:** how an approved refund is paid and what follows it.
- **Type:** record (method: enum [original-payment-method, store-credit, wallet], typical_days, fees_deducted: bool, access_after_refund: enum [ends, kept-to-period-end], data_kept: bool)
- **Look:** payment provider refund calls, entitlement revocation on refund webhooks
  (`charge.refunded`, RevenueCat `CANCELLATION` with refund reason), store-credit code.
- **Ask:** "When you refund, where does the money go, how long does it take, and does access
  end at once?" Recommend "original payment method, 5–10 business days, access ends".

### facts.sales.return_rules
- **Means:** rules for returning physical goods.
- **Type:** record (window_days, window_start: enum [delivery, purchase], condition, return_shipping_payer: enum [seller, buyer, seller-if-at-fault], label_provided: bool, in_store_returns: bool, exchanges: bool, damaged_items_route, order_cancellation: bool)
- **Look:** return-label and returns-portal integrations (Loop, Narvar, Shopify returns),
  shipping settings, store-location data.
- **Ask:** "For physical goods: how many days to return, in what condition, who pays return
  shipping, and how are damaged or wrong items handled?" Recommend 30 days from delivery,
  unused in original packaging, and a free replacement or refund for damaged or wrong items.

### facts.sales.return_address
- **Means:** the address returned goods are sent to, when it differs from the company's address.
- **Type:** string or none
- **Look:** return-label integrations, warehouse settings, existing returns page.
- **Ask:** "Where should buyers send returns, if not to your company address?" Recommend "same
  as the company address".

## Users keys

### facts.users.regions
- **Means:** regions whose users the product serves, which decides the regional parts.
- **Type:** list of region codes: the folders under `regions/`, plus `other`
- **Look:** store availability settings, localisations, payment currencies.
- **Ask:** "Where are your users?" Recommend every region the store listing is available in.

### facts.users.rights_channels
- **Means:** how users exercise each right: in-app paths and request channels.
- **Type:** list of (right, route)
- **Look:** settings screens for export, delete and edit; support email.
- **Ask:** "How can users access, export, correct and delete their data?" Recommend the in-app paths found, with the contact email as fallback.

### facts.users.request_handling
- **Means:** how the company handles a data-protection rights request once it arrives, whatever
  the route (`facts.users.rights_channels` holds the routes): the form or tool used, the details
  asked to find the person's data, how identity is checked, whether someone may file for another
  person and what proof is asked, the response time committed to, whether a reference or status
  page exists, how the answer is sent, and whether the requester confirms the details are true.
- **Type:** record (tool: enum [own-form, hosted-portal, email-only], identifiers: list of string, verification: list of enum [email-link, sign-in, record-match, id-document, signed-declaration, none], representatives: record (allowed: bool, minors_by_parent: bool, proof: string or none), response_days: number or none, status_tracking: bool, reply_channels: list of string, attestation: bool)
- **Look:** privacy-request pages and routes (`/privacy-request`, `/dsar`, `/data-request`);
  embeds or links of OneTrust, Transcend, DataGrail, Ketch or TrueVault webforms; form-builder
  embeds (Jotform, Typeform, HubSpot forms) on a privacy page; request-handling code that sends a
  verification email; the rights section of the existing privacy policy.
- **Ask:** "When someone asks for a copy, correction or deletion of their data, how do you check
  it is them, how quickly do you answer, and can someone ask on another person's behalf?"
  Recommend: an email confirmation link to the address on the account (sign-in for account
  holders), no ID documents unless the details cannot be matched, an answer within 30 days,
  representatives allowed with signed written authority, and the answer sent by email.

## Marketing keys

### facts.marketing.email
- **Means:** whether marketing emails are sent.
- **Type:** bool
- **Look:** email marketing SDKs and APIs (Mailchimp, Customer.io, Braze, Resend audiences), newsletter forms.
- **Ask:** "Do you send marketing emails?" Recommend what the code shows.

### facts.marketing.push
- **Means:** whether push notifications are used, and for what.
- **Type:** enum [none, service-only, service-and-marketing]
- **Look:** push SDKs (FCM, APNs), notification permission requests.
- **Ask:** "Do you send push notifications, and are any of them promotional?" Recommend what the code shows.

### facts.marketing.sms
- **Means:** whether the company sends text messages to users (verification codes, service
  alerts, marketing).
- **Type:** enum [none, verification-only, service, service-and-marketing]
- **Look:** SMS providers (Twilio, Vonage, MessageBird, Firebase phone auth), phone-number
  fields, SMS templates.
- **Ask:** "Do you send text messages, and are any of them promotional?" Recommend what the code
  shows.

## Registrations keys

### facts.registrations.privacy_regulator
- **Means:** the company's registration with each data protection authority whose register
  applies to it: registered (with the registry's id or number and date), exempt under that
  authority's rules, or not registered. One entry per region (`facts.users.regions` code); `uk`: the ICO register of fee
  payers, where the number is issued when the data protection fee is paid; `tr`: VERBİS, the KVKK
  Board's data-controller registry.
- **Type:** list of (region: region code, registry: enum [ico, verbis, other], status: enum [registered, exempt, not-registered], registry_id: string or none, registered_on: date or none)
- **Look:** existing legal docs (privacy policy footer, KVKK notice); the authority's public
  register (ICO register of fee payers; VERBİS public query). Not in code.
- **Ask:** one question per region in `facts.users.regions` that has a register. UK: "Have you
  paid the ICO data protection fee? If so, what is your registration number?" Recommend checking
  the ICO's fee self-assessment; most companies that handle UK users' data must pay. TR: "Is the
  company registered in VERBİS, or exempt?" Recommend checking the Board's exemption decisions:
  controllers in Turkey with fewer than 50 staff and a small annual balance sheet are usually
  exempt unless their main activity is processing special-category data; controllers outside
  Turkey are not exempt on that ground.

## Company contract keys

Facts about the company that every agreement it signs (with a contractor, a founder, an IP
assignor) names. Added by the `contractor-agreement` build; other contract skeletons reuse them.

### facts.company.entity_form
- **Means:** the company's legal form and where it is registered, as a contract names it in the
  preamble ("a Delaware corporation", "a private limited company registered in England and
  Wales"), with its registration number where its law expects one.
- **Type:** record (form: string, registered_in: string, registration_number: string or none)
- **Look:** existing contracts and legal docs; incorporation documents in the repo; the company
  footer or imprint. Usually not in code.
- **Ask:** "What is the company's legal form and where is it registered (for example, a Delaware
  corporation, a private limited company in England and Wales, an A.Ş. in Istanbul)?" Recommend the form and place in the incorporation documents or the imprint.

### facts.company.contract_law
- **Means:** the law and courts the company chooses for its own business agreements (with
  contractors, founders, partners), and whether disputes go to court or to arbitration, with an
  informal step first. Separate from `facts.company.governing_law`, which governs the user terms.
- **Type:** record (law: country or state, courts: city or district, forum: enum [courts, arbitration], informal_first: bool)
- **Look:** existing contracts. Not in code. The user decides.
- **Ask:** "Which law should govern your agreements with contractors and partners, and which
  city's courts should hear disputes?" Recommend the law and courts of the company's seat
  (`facts.company.country`, `facts.company.address`), courts rather than arbitration, with a
  short good-faith talk first.

### facts.company.signatory
- **Means:** the person who signs agreements for the company, with their title.
- **Type:** record (name: string, title: string)
- **Look:** existing contracts; founders or officers named in incorporation documents. Not in
  code.
- **Ask:** "Who signs agreements for the company, and with what title?" Recommend the founder or
  director who runs the company.

## Contractor keys

One engagement with one freelancer, consultant or contracting firm. Every key here is a choice or
a fact of the deal, so the scan writes each as `missing` with what it saw in the *Hint*, and the
user is always asked. A user who engages several contractors keeps one set per contractor.

### facts.contractor.party
- **Means:** who the contractor is: an individual or a firm, its legal name and form, address
  and country, the email for notices, and, for a firm, the person who will do the work.
- **Type:** record (kind: enum [individual, firm], name: string, form: string or none, address: string, country: string (ISO 3166-1 alpha-2), notice_email: string, performer: string or none)
- **Look:** Not in code. The user decides.
- **Ask:** "Who are you engaging: a person working on their own account, or a company? Give their
  legal name, address and email, and for a company, the person who will do the work." Recommend
  naming the performer whenever the contractor is a firm.

### facts.contractor.services
- **Means:** what the contractor will do: the services, the deliverables if any, whether the
  company accepts deliverables before they count as done, and how work is ordered (one project,
  an ongoing role, or a master agreement with statements of work).
- **Type:** record (description: string, deliverables: list of (item, due) or none, acceptance: bool, structure: enum [single-project, ongoing, master-with-sows])
- **Look:** Not in code. The user decides. Project briefs or issue trackers in the repo may hint
  at the scope.
- **Ask:** "What will the contractor do, and what will they hand over? Is it one project, an
  ongoing role, or a series of projects?" Recommend listing deliverables with due dates for
  project work, and acceptance for deliverables the company has to test.

### facts.contractor.work_arrangements
- **Means:** how the work runs: the expected time (hours or days, or "as needed"), where it is
  done, the company's contact person, how often the contractor reports, who supplies tools and
  equipment, and what the company must supply (access, content, feedback).
- **Type:** record (time: string or none, place: enum [remote, on-site, mixed], contact: string, reporting: string or none, tools: enum [contractor, company, mixed], company_inputs: list of string)
- **Look:** Not in code. The user decides.
- **Ask:** "Roughly how much of their time do you expect, where will they work, who is their
  contact, and what do you need to give them to do the job?" Recommend remote work on the
  contractor's own tools, with one named contact.

### facts.contractor.fees
- **Means:** what the contractor is paid and on what basis, in which currency, with any cap on
  billable time or total, and any equity granted.
- **Type:** record (basis: enum [hourly, daily, fixed, retainer, milestone, equity, mixed], amount: string, currency: string (ISO 4217), cap: string or none, equity: string or none)
- **Look:** Not in code. The user decides.
- **Ask:** "How will you pay them: by the hour or day, a fixed price, a monthly retainer, or by
  milestone? How much, in which currency, and is there a cap?" Recommend a cap on billable hours
  for hourly work. Equity for a contractor needs a lawyer's advice, so recommend cash.

### facts.contractor.payment_terms
- **Means:** how money moves: invoice cadence and content, days to pay after an invoice, method,
  any deposit, and late-payment interest.
- **Type:** record (invoicing: string, payment_days: number, method: string, deposit: string or none, late_interest: string or none)
- **Look:** Not in code. The user decides; invoicing tools the company already uses may hint at
  the method.
- **Ask:** "How often will they invoice, and how many days do you take to pay?" Recommend
  monthly invoices (or one per milestone), paid within 30 days by bank transfer.

### facts.contractor.expenses
- **Means:** whether the company reimburses the contractor's expenses, which ones, above what
  amount prior approval is needed, and what proof is required.
- **Type:** record (reimbursed: bool, approval_above: string or none, proof: string or none)
- **Look:** Not in code. The user decides.
- **Ask:** "Will you pay their expenses (travel, software, stock assets)? Above what amount must
  they ask first?" Recommend reimbursing only expenses approved in writing in advance, against
  receipts.

### facts.contractor.term
- **Means:** when the engagement starts and ends: a start date, and either an end date, the end
  of the project, or no end date until either side ends it; any renewal.
- **Type:** record (start: date, end: enum [fixed-date, on-completion, open-ended], end_date: date or none, renewal: string or none)
- **Look:** Not in code. The user decides.
- **Ask:** "When does the work start, and when should the agreement end?" Recommend ending on
  completion for project work, and open-ended with notice for an ongoing role.

### facts.contractor.termination
- **Means:** how either side can end the engagement early: whether either may end it for
  convenience and on how many days' notice, the cure period for a breach, and what is paid on
  termination.
- **Type:** record (convenience: enum [either, company-only, none], notice_days: number or none, cure_days: number or none, pay_on_termination: string)
- **Look:** Not in code. The user decides.
- **Ask:** "Can either of you end it early without a reason, and with how much notice?"
  Recommend either side on 14 to 30 days' written notice, a cure period for breaches, and payment
  for work done up to the end.

### facts.contractor.ip_terms
- **Means:** who owns what the contractor creates: assigned to the company, licensed to it, or
  kept by the contractor; whether the contractor will build its own pre-existing materials,
  third-party or open-source components into the deliverables; whether a waiver of moral rights
  is wanted; and whether these terms sit in the agreement or in a separate IP assignment.
- **Type:** record (ownership: enum [assigned, licensed, contractor-keeps], background_materials: bool, third_party_components: bool, moral_rights_waiver: bool, placement: enum [in-agreement, separate-assignment])
- **Look:** Not in code. The user decides. A repo the contractor will commit to shows whether
  open-source components are likely.
- **Ask:** "Should the company own everything they make for you? Will they reuse their own code,
  designs or templates, or open-source parts?" Recommend assignment to the company for work made
  for the product, a licence for the contractor's pre-existing materials, and the terms in the
  agreement itself.

### facts.contractor.confidentiality
- **Means:** what the confidentiality duty covers: one-way (the company's information) or
  mutual, how long it lasts, and whether an NDA is already signed.
- **Type:** record (direction: enum [one-way, mutual], years_after: number or none, existing_nda: bool)
- **Look:** existing NDAs in the company's records. Not in code.
- **Ask:** "Should only the contractor keep things confidential, or both of you? Have you already
  signed an NDA?" Recommend one-way, lasting a set number of years after the engagement and
  without end for trade secrets.

### facts.contractor.restrictions
- **Means:** limits on the contractor beyond confidentiality: not soliciting the company's staff
  or customers, not working for competitors during the engagement, not disparaging the company,
  each with how long it lasts after the end.
- **Type:** list of (restriction: enum [non-solicit-staff, non-solicit-customers, no-competing-work, non-disparagement], months_after: number or none)
- **Look:** Not in code. The user decides.
- **Ask:** "Do you want any limits beyond confidentiality, such as not poaching your staff?"
  Recommend none, or a staff non-solicit only; limits on whom a contractor may work for can
  undermine their independent status.

### facts.contractor.subcontracting
- **Means:** whether the contractor may hand work to others (subcontractors, its own staff).
- **Type:** enum [not-allowed, with-consent, allowed]
- **Look:** Not in code. The user decides.
- **Ask:** "May they hand part of the work to someone else?" Recommend only with your written
  consent, the contractor staying responsible.

### facts.contractor.liability
- **Means:** the limits on each side's liability under the agreement: whether indirect damages
  are excluded, a cap and its basis, whom the limits protect, and which indemnities each side
  gives.
- **Type:** record (exclude_indirect: bool, cap: enum [fees-paid, fees-12-months, fixed, none], cap_amount: string or none, protects: enum [both, contractor, company], indemnities_by_contractor: list of enum [ip-infringement, breach, negligence, taxes], indemnities_by_company: list of enum [company-materials, negligence])
- **Look:** Not in code. The user decides.
- **Ask:** "Should either side's liability be capped, for example at the fees paid? Should the
  contractor cover you if their work infringes someone's rights?" Recommend a mutual cap at the
  fees paid, indirect damages excluded both ways, and an IP-infringement indemnity from the
  contractor kept outside the cap.

### facts.contractor.insurance
- **Means:** insurance the contractor must carry (professional liability, general liability),
  with amounts, if any.
- **Type:** list of (type: string, amount: string) or none
- **Look:** Not in code. The user decides.
- **Ask:** "Should they carry insurance, such as professional liability?" Recommend none for a
  small engagement unless a customer contract requires it.

### facts.contractor.data_access
- **Means:** what the contractor will reach: none of the company's systems, its systems or code,
  or personal data of users or staff.
- **Type:** enum [none, systems, personal-data]
- **Look:** Not in code; the user decides. Admin roles, deploy keys or database access to be
  granted are hints. When personal data is reached, the contractor is a processor
  (`facts.processors.list`).
- **Ask:** "Will they get access to your systems, code or user data?" Recommend the least access
  the work needs.

### facts.contractor.portfolio_use
- **Means:** whether the contractor may name the company or show the work (in a portfolio, case
  study or client list), and on what condition.
- **Type:** enum [not-allowed, with-approval, after-launch, allowed]
- **Look:** Not in code. The user decides.
- **Ask:** "May they show this work in their portfolio or name you as a client?" Recommend
  with your approval, and never before the work is public.

### facts.contractor.prior_work
- **Means:** whether the contractor started work before the agreement is signed, and from when,
  so the agreement covers that work too.
- **Type:** record (started_before: bool, since: date or none)
- **Look:** Not in code; commit history by the contractor before the start date is a hint.
- **Ask:** "Did they already start working for you before signing?" Recommend covering the earlier
  work in the agreement when they did.

## Team keys

The people who build the company and what the company's agreements with them bind them to. Used by
the IP assignment; a founder or employment document may reuse them.

### facts.company.founders
- **Means:** the people who founded the company, each with their full legal name and role.
- **Type:** list of (name: string, role: string)
- **Look:** incorporation documents or a cap table in the repo; the README or about page; the
  authors of the repository's earliest commits. Not reliably in code.
- **Ask:** "Who founded the company? Give each founder's full legal name and role." Recommend the
  names in the incorporation documents.

### facts.company.founder_prior_work
- **Means:** what each founder made for the business before the company existed or before they
  signed with it (code, designs, content, the domain, store or social accounts, the name and logo,
  patent filings); for each founder, whether it is already assigned to the company, and what the
  founder gets for assigning it.
- **Type:** list of (founder: string, items: list of (kind: enum [code, design, content, domain,
  account, brand, patent, other], description: string), already_assigned: bool, consideration:
  enum [shares, nominal-sum, none], consideration_detail: string or none)
- **Look:** repository history from before the incorporation date (first commits, a repository
  first held under a founder's personal account); domains, developer and store accounts registered
  to a person; patent filings in a founder's name. The user decides what is listed.
- **Ask:** "Before the company existed, did a founder build things it now uses: code, designs, the
  domain, app-store or social accounts, the name or logo, a patent filing? Has each been formally
  assigned to the company, and what does the founder get for it?" Recommend listing what the
  repository history shows, with the founder shares as the consideration when founders hold them;
  "none" only when the company existed before any work began.

### facts.company.ip_signers
- **Means:** who signs the company's invention assignment and confidentiality agreement: founders
  (for their work from now on), employees, contractors whose own agreement leaves IP to a separate
  assignment, advisors.
- **Type:** list of enum [founders, employees, contractors, advisors]
- **Look:** team or careers pages; payroll or HR integrations; repository contributors who are not
  founders; `facts.contractor.ip_terms` (`placement: separate-assignment`). Not reliably in code.
  The user decides.
- **Ask:** "Who should sign the IP and confidentiality agreement: founders, employees, contractors,
  advisors?" Recommend founders and everyone who writes code, designs or content for the company.

### facts.company.business_scope
- **Means:** the company's business now and as planned, in a sentence or two. The agreement uses it
  to say which inventions relate to the business and what the covenants protect.
- **Type:** string
- **Look:** README, store description, the website's about page, `facts.product.category`; roadmap
  files or feature flags for planned lines.
- **Ask:** "In a sentence or two, what is the company's business now, and what does it plan to do
  next?" Recommend the product description plus any planned line the repository shows.

### facts.company.staff_locations
- **Means:** the countries, and inside the US the states, where the people who sign the company's
  agreements with its team live and work. Their local law decides which invention, confidentiality
  and covenant rules apply.
- **Type:** list of (country: string (ISO 3166-1 alpha-2), region: string or none)
- **Look:** Not in code; a payroll or HR tool's settings, the team page.
- **Ask:** "Where do your founders, employees and contractors live and work? Name the country, and
  the state for anyone in the US." Recommend the company's country (`facts.company.country`).

### facts.company.staff_restrictions
- **Means:** what the agreement bars signers from beyond confidentiality: recruiting the company's
  staff, soliciting its customers or partners, competing, disparaging the company; each with how
  long it runs after the person leaves and, for a non-compete, where.
- **Type:** list of (restriction: enum [non-solicit-staff, non-solicit-customers, non-compete,
  non-disparagement], months_after: number or none, area: string or none)
- **Look:** existing agreements. Not in code. The user decides.
- **Ask:** "Beyond confidentiality, should signers agree not to recruit your staff, not to solicit
  your customers, not to compete, or not to disparage the company after they leave? For how many
  months?" Recommend a staff non-solicit for 12 months where the signers' law allows one (California, for
  one, voids it) and nothing more. No non-compete unless a
  lawyer where each signer works confirms it holds there: many places ban or limit them.

## Ownership keys

How the owners of the company hold, run and leave it. Added by the `shareholders-agreement` build; a
shareholders' agreement, a cap table note or an investment document may reuse them. The founders
themselves are `facts.company.founders`.

### facts.company.share_structure
- **Means:** who holds the company's shares and on what terms: the share classes and what each
  carries, every holder (founders, investors, employees, advisors) with their holding and what they
  paid, the employee option pool, and each holder's address for notices.
- **Type:** record (classes: list of (name: string, rights: string), holders: list of (name: string,
  kind: enum [founder, investor, employee, advisor, other], class: string, holding: string, paid:
  string or none, notice_contact: string), option_pool: string or none)
- **Look:** incorporation documents, a cap table, SAFE or convertible-note documents and existing
  shareholder agreements in the repo. Not in code.
- **Ask:** "Who owns the company today, in which share class, and how much did each holder pay? Is
  there an option pool for employees?" Recommend the split in the incorporation documents; when
  there are no investors yet, one class of ordinary shares held by the founders.

### facts.company.founder_commitment
- **Means:** what each founder gives the company besides money for shares: time, how they are
  engaged, what they are paid, and any cash, loan or asset they bring.
- **Type:** list of (founder: string, time: enum [full-time, part-time, none], engagement: enum
  [employee, contractor, director-only, none], pay: string or none, contribution: string or none)
- **Look:** not in code; payroll or contractor tools' settings show who is paid. The user decides.
- **Ask:** "For each founder: full-time or part-time, employed or contracting with the company, what
  pay, and anything they bring besides work (cash, a loan, equipment)?" Recommend full-time for
  every founder who holds a working founder's share, with the employment or service contract signed
  separately.

### facts.company.founder_vesting
- **Means:** whether founder shares vest, on what schedule, and what a founder who leaves keeps:
  who counts as a good or bad leaver, and the price the company or the other founders pay for the
  shares the leaver must give up.
- **Type:** record (applies: bool, months: number, cliff_months: number, frequency: enum [monthly,
  quarterly, annual], acceleration: enum [none, on-sale, on-sale-and-dismissal], bad_leaver: list
  of string, unvested_price: enum [nominal, cost, fair-value], bad_leaver_vested_price: enum [kept,
  cost, fair-value, discount])
- **Look:** existing founder or stock purchase agreements. Not in code. The user decides.
- **Ask:** "Should founder shares vest, so that a founder who leaves early gives some back? Over how
  long, with what cliff? Who counts as a bad leaver, and at what price are shares bought back?"
  Recommend vesting over 48 months with a 12-month cliff and monthly vesting after it (a common
  market default, not a legal requirement; 36 months and a 6-month cliff are also usual), unvested
  shares bought back at what the founder paid, and vested shares kept by a good leaver; the bad
  leaver list limited to resigning within the cliff, dismissal for cause and breach of the
  covenants.

### facts.company.board
- **Means:** the board: how many directors, who appoints and removes each, who chairs, whether
  the chair has a casting vote, and any observers.
- **Type:** record (size: number, appointments: list of (appointer: string, seats: number),
  chair: string or none, casting_vote: bool, observers: list of string)
- **Look:** incorporation documents and the articles; existing agreements. Not in code.
- **Ask:** "How many directors should the board have, and who appoints them? Should the chair have
  a casting vote?" Recommend one director per founder while the founder holds shares, and no
  casting vote when the founders hold equal stakes.

### facts.company.decision_rules
- **Means:** how the board's and the shareholders' decisions pass, which decisions need every
  founder's consent (or a named holder's), and what happens when the owners deadlock.
- **Type:** record (board_majority: string, shareholder_majority: string, reserved_matters: list of
  string, reserved_threshold: enum [unanimous, founder-majority, special-majority, named-holder],
  deadlock: list of enum [escalation, mediation, buy-sell, winding-up], in the order the steps
  run; empty when the agreement has no deadlock clause)
- **Look:** the articles and existing agreements. Not in code. The user decides.
- **Ask:** "Which decisions should need every founder's agreement (new shares, selling the company,
  large borrowing, changing the business, founders' pay)? If the founders cannot agree, what
  happens?" Recommend simple majorities for everything else, a short reserved list needing all
  founders, and for founders with equal stakes an escalation step, then mediation; a buy-sell
  (shotgun) only on a lawyer's advice, since it favours the founder with more money.

### facts.company.share_transfer_rules
- **Means:** the limits on founders and other holders selling, giving or pledging shares: a lock-in
  period, transfers allowed without consent, first refusal for the others, a tag-along, the
  drag-along threshold, and pre-emption on new shares.
- **Type:** record (lock_in_months: number or none, permitted_transferees: list of enum [family,
  family-trust, holding-company, affiliate], rofr: enum [none, company-first, holders-only],
  tag_along: bool, drag_threshold: string or none, pre_emption: bool)
- **Look:** the articles and existing agreements. Not in code. The user decides.
- **Ask:** "Can a founder sell or give away shares? Should the others have first refusal, the right
  to join a sale, or be able to force a sale of the whole company once enough holders agree? Do
  holders get first pick of new shares?" Recommend board consent for any transfer, free transfers
  only to the holder's own holding company or family trust, first refusal for the other holders,
  a tag-along, a drag-along only above a threshold every founder accepts, and pre-emption on new
  shares.

### facts.company.funding_terms
- **Means:** the money founders put into the company at the start (subscription, loans,
  guarantees), whether anyone must fund it later, and how profits are paid out.
- **Type:** record (initial: list of (holder: string, kind: enum [cash, loan, guarantee, asset],
  amount: string), further_funding: enum [none, pro-rata-if-agreed, required], dividend_policy:
  string or none)
- **Look:** bank or payment records are not in code; existing agreements, loan notes. The user
  decides.
- **Ask:** "What has each founder put in (cash, loans, guarantees)? Must anyone fund the company
  later? How should profits be paid out?" Recommend no duty to fund beyond what each has agreed,
  shareholder loans on written terms, and dividends only when all founders agree.

---
doc_id: cookie-policy
title: Cookie Policy
kind: document
family: privacy-notices
sample_languages: [en]
sample_count: 20
saturated: true
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** Tells visitors and users which cookies and similar trackers the website and app
  use, what each kind is for, who else sets them, and how to accept, refuse or remove them.
- **Shape:**
  - 19/20 one standalone web page; 1/20 a help-center article. 1/20 puts the cookie list on a
    linked page. Median about 920 words (range 490–2,750): large companies about 1,750, mid
    about 1,100, small about 820.
  - 7/20 number their sections; 8/20 phrase most headings as questions ("What are cookies?");
    2/20 open with a table of contents; 1/20 has no headings at all.
  - 7/20 carry an item-level cookie list on the page (4 as a table); 4/20 point to the consent
    tool for it; 7/20 give no list.
  - 5/20 place a cookie-settings button on the page, above the text or at its end.
- **Register:** 20/20 "we/you", plain, short to medium sentences, much of it generic explanation
  of how cookies work. 8/20 define one collective term for every tracker ("cookies",
  "tracking technologies"). 3/20 are generator texts with the company's details filled in.
- **Recurring elements:**
  - A dated "last updated" or "effective" line: 16/20, nearly always at the top.
  - A pointer to the privacy policy: 15/20.
  - A closing contact line: 14/20, usually one email.
  - A caveat that cookie names and numbers change: 4/20.
  - A list or archive of earlier versions: 2/20.
- **Commonly omitted:** an item-level cookie list (7/20 give none; 2/20 announce one the page
  lacks); cookie lifetimes as periods (12/20 give none); retention of cookie data (16/20); a
  contact (6/20); a date (4/20).

## Sections

Region-neutral. What one law requires (consent before non-essential cookies, legal bases,
transfers, opt-outs of sale or sharing, browser opt-out signals) is in the region's block,
`regions/<code>/cookie-policy.md`, written under the document's regional part
(`formats/region-format.md`).

### intro: About this policy

- **Covers:** who publishes the policy, which websites, apps and services it covers, what it
  explains, and the collective term it uses for cookies and similar technologies.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.product.name`, `facts.product.services_in_scope`
- **Patterns:**
  - About 15/20 name the surfaces covered (website, web app, mobile apps, subdomains); 1/20 covers
    a single site only.
  - About 7/20 name the legal entity; 3/20 add its registered address or register number.
  - 8/20 define one term for every tracker here and use it throughout.
  - 2/20 say partner sites or the company's other services have their own notices.
  - 2/20 treat visiting or continuing to use the service as agreeing to cookies or to the policy;
    the other 18 do not, and most offer a choice instead.
  - Usually one to three unheaded paragraphs under the title; 1/20 opens with a yes/no answer to
    "Do we use cookies?".
- **Quote:** "This Cookie Policy applies to any LinkedIn product or service that links to this policy or incorporates it by reference." (s01)
- **Commonly omitted:** what the product does; which countries the policy is written for.

### privacy-link: Relation to the privacy policy

- **Covers:** how the policy relates to the privacy policy and where to read about personal-data
  processing and rights.
- **Prevalence:** 15/20 (75%), common
- **Applies when:** `facts.company.published_policies` lists a privacy policy
- **Facts:** `facts.company.published_policies`
- **Patterns:**
  - 4/15 make the cookie policy part of the privacy policy or incorporated into it; 3/15 call it
    a supplement or say to read both together; the rest point there for processing and rights.
  - About 10/15 put the link in the opening; about 4/15 at the end, beside the contact.
  - 2/15 also send the reader there for the controller's identity, contact or children's data.
  - 1/20 adds how cookie data is protected; the privacy policy's security section usually
    carries that.
- **Quote:** "This Cookie Policy forms part of our Privacy Policy and should be read together with our Terms of Use." (s10)
- **Commonly omitted:** which privacy-policy section covers cookies.

### what-are-cookies: What cookies are

- **Covers:** what a cookie is in general, first- and third-party cookies, and session and
  persistent cookies as kinds.
- **Prevalence:** 19/20 (95%), core
- **Applies when:** always
- **Facts:** `facts.data.tracking`
- **Patterns:**
  - Almost all give a textbook definition: a small text file a site stores on the device to
    recognise it later.
  - 13/19 explain first- vs third-party cookies; 9/19 session vs persistent; several then say
    the company uses both.
  - About 4/19 add what cookies do on websites in general (stay signed in, remember settings).
  - 1/19 opens the whole policy with this explainer; most put it right after the opening.
- **Quote:** "A cookie is a small file that contains letters and numbers that is downloaded to your device when you visit a website." (s19)
- **Commonly omitted:** anything specific to the company; it is the most generic section.

### similar-technologies: Other tracking technologies

- **Covers:** which non-cookie trackers the company uses and what each is: pixels and web
  beacons (on pages and in emails), local storage, SDKs, device and advertising identifiers,
  fingerprinting.
- **Prevalence:** 15/20 (75%), common
- **Applies when:** `facts.data.tracking` lists a technology other than cookies
- **Facts:** `facts.data.tracking`
- **Patterns:**
  - Nearly all name pixels or web beacons; 8/15 local storage; 7/15 SDKs or device identifiers
    in apps; 3/15 fingerprinting; 3/15 pixels in marketing emails (open and click tracking).
  - 8/15 fold every technology into one defined term, so the rest of the policy says "cookies".
  - 4/15 a list or table with a one-line definition per technology; the rest prose.
  - 1/15 says beacons cannot be declined but are limited by blocking cookies.
- **Quote:** "For the purposes of this article, we'll refer to all of these technologies as "cookies."" (s16)
- **Commonly omitted:** which technologies run in the app as opposed to the website.

### purposes: Why we use cookies

- **Covers:** what the company uses cookies for, grouped by purpose or category, and for each
  category whether it can be switched off.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.tracking`, `facts.data.purposes`, `facts.data.targeted_ads`
- **Patterns:**
  - Most use four categories: strictly necessary, analytics or performance, functional or
    preference, advertising or targeting; some add social media or communications.
  - 5/20 cut by use or by tool instead (authentication, security, plugins; one clause per
    vendor).
  - 10/20 a list of categories, 4/20 a table (category and description, or a row per category
    with purpose, data, expiry and providers), 6/20 prose.
  - 11/20 say for each category whether it can be switched off; strictly necessary cookies are
    always the ones that cannot.
  - Each category usually gets one or two sentences and a "for example"; product-specific
    examples (stay signed in, remember the language) read better than generic ones.
  - 1/20 discloses session replay under analytics.
- **Quote:** "Some cookies are required for technical reasons in order for our Websites to operate as intended, and we refer to these as "strictly necessary" cookies." (s12)
- **Commonly omitted:** which category each named vendor belongs to, outside a cookie list.

### off-site-tracking: Our cookies on other sites

- **Covers:** cookies the company itself sets or reads on other parties' sites and apps through
  its plugins, widgets, sign-in buttons or tags.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.product.offsite_components != []`
- **Facts:** `facts.product.offsite_components`
- **Patterns:**
  - 1/2 a plugin row plus a separate cookie table for cookies set on partner sites, with
    retargeting of visitors to customers' sites.
  - 1/2 sign-in on partner sites, saying refusal does not block the user's account.
- **Quote:** "Our plugins use cookies and other technologies to provide analytics and recognize you on LinkedIn and third-party sites." (s01)
- **Commonly omitted:** which partner sites carry the components.

### data-collected: What cookies collect

- **Covers:** what information cookies and trackers collect and when it becomes linked to the
  person.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** always
- **Facts:** `facts.data.tracking`, `facts.data.collected`
- **Patterns:**
  - Categories, not fields: identifiers (cookie or device ID), IP address, browser and device
    data, pages viewed and clicks.
  - 2/9 per category or per vendor in the category blocks; the rest one list or sentence.
  - 2/9 say cookie data becomes linked to the person once combined with account data or email
    activity.
  - 1/9 says data is collected from devices that never engaged with the service.
- **Quote:** "In some cases we may use cookies to collect personal information if we combine the data with other information during or after sign up of our services." (s12)
- **Commonly omitted:** whether the data is used to build a profile.

### retention: How long cookies and their data last

- **Covers:** how long cookies or cookie data are kept, as periods or a rule, outside an
  item-level list.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.data.retention` has an entry for cookie or tracking data
- **Facts:** `facts.data.retention`, `facts.data.tracking`
- **Patterns:**
  - 2/4 a period per category (one counted from the last visit, one as a range from session to
    years); 1/4 one maximum lifetime for all persistent cookies.
  - 2/4 a general "only as long as necessary" rule, alone or beside the periods.
- **Quote:** "Dropbox only retains personal data for as long as necessary for the purposes for which it was collected." (s16)
- **Commonly omitted:** how long data collected through cookies is kept after the cookie expires.

### third-parties: Third parties that set cookies

- **Covers:** who else sets cookies through the service, by role or by name, why, that their own
  policies govern them, and how they are chosen.
- **Prevalence:** 14/20 (70%), common
- **Applies when:** `facts.data.tracking` lists a third-party provider
- **Facts:** `facts.data.tracking`, `facts.processors.list`
- **Patterns:**
  - 7/14 name the providers (inline per category, numbered entries, or a bare list), usually
    with links to their privacy policies; 7/14 describe them by role only (analytics, ad
    networks, social plugins, customers, payment and sign-in providers).
  - About 7/14 say the third parties' own policies govern their cookies.
  - 2/14 disclaim control over third-party cookies; 2/14 add an assurance that providers are
    vetted or bound by contract.
  - 1/14 places this inside each category instead of its own section.
- **Quote:** "Third-party cookies are covered by the third parties' privacy policy." (s10)
- **Commonly omitted:** which data each third party receives.

### data-sharing: Who receives cookie data

- **Covers:** who receives the data cookies collect beyond the company, and in what form.
- **Prevalence:** 7/20 (35%), rare
- **Applies when:** `facts.data.targeted_ads == true`, or `facts.data.other_recipients` lists a partner, or `facts.data.deidentified_use == true`
- **Facts:** `facts.data.other_recipients`, `facts.data.deidentified_use`, `facts.data.targeted_ads`, `facts.data.tracking`
- **Patterns:**
  - 3/7 say which vendors may use the data for their own purposes (one as a yes/no answer per
    category, one as a list of vendor names).
  - 2/7 share data with ad partners for interest-based ads and retargeting; 1/7 shares
    aggregate analytics with business customers.
  - 2/7 disclose identifiers to analytics providers as service providers.
- **Quote:** "Does Klarna share the collected data with a company that may use it for its own purposes?" (s04)
- **Commonly omitted:** whether recipients may combine the data with their own.

### refusal-effects: If you refuse cookies

- **Covers:** what happens when the user refuses, disables or deletes cookies.
- **Prevalence:** 16/20 (80%), core
- **Applies when:** always
- **Facts:** `facts.data.tracking`, `facts.data.targeted_ads`
- **Patterns:**
  - Nearly all warn that some features may not work; most in one sentence at the end of a
    controls section.
  - 5/16 add that refusing ad cookies means less relevant ads, not fewer ads.
  - 5/16 state it per category; 2/16 give it a short section of its own.
  - 2/16 say refusing non-essential cookies changes nothing in the service.
- **Quote:** "If you choose not to activate cookies or to later disable them, you can still visit our website, but your ability to use some features may be limited." (s13)
- **Commonly omitted:** that saved settings and sign-ins are lost when cookies are deleted (1/16 says).

### cookie-list: The cookies we use

- **Covers:** the item-level list of cookies and trackers (name or provider, purpose, duration,
  party, category), or where it is kept, and how it is kept current.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** `facts.data.tracking != []`
- **Facts:** `facts.data.tracking`, `facts.data.cookie_list`
- **Patterns:**
  - 4/13 a table on the page or a linked page: name, duration and description, often with
    provider, domain or category; 1/4 mixes web cookies and app SDKs.
  - 3/13 a list by provider (vendor and what it does) without cookie names.
  - 4/13 only point to the consent tool, which shows the current list.
  - 2/13 announce a list that the page does not show; write the list or the pointer, never a
    promise of one.
  - 4/13 add that names and numbers change; 2/13 say how the list is kept current (regular scans,
    a six-monthly review).
  - Durations, when given, are periods ("1 year") or just "session" and "persistent".
- **Quote:** "Please note that the names of cookies and similar technologies may change over time." (s01)
- **Commonly omitted:** first- or third-party marked per cookie; the domain that sets it.

### consent-tool: Your cookie settings

- **Covers:** the cookie settings in the product: banner, preference centre or settings link, and
  how to accept, refuse, change or withdraw a choice.
- **Prevalence:** 17/20 (85%), core
- **Applies when:** `facts.data.cookie_controls != none`
- **Facts:** `facts.data.cookie_controls`, `facts.product.services_in_scope`
- **Patterns:**
  - Most name the link or button that reopens the tool and where it is (footer "Cookie
    settings", "Privacy settings", a button on the policy page); 5/17 embed the button in the
    policy itself.
  - 4/17 describe the first-visit banner's choices (accept all, reject all, customise).
  - About 6/17 offer a choice per category; 1/17 also per vendor.
  - About 7/17 say a choice can be changed or withdrawn at any time; 1/17 that withdrawal takes
    effect at once.
  - 2/17 point to the app's own settings as well; 1/17 offers an email request where no banner is
    shown.
  - 7/17 route some users to a separate opt-out link that their region requires; that link
    belongs in the regional part.
  - Strictly necessary cookies are stated as outside the choice.
- **Quote:** "You may grant or withdraw consent by category (Functional, Analytics, Social Media, Advertising)." (s17)
- **Commonly omitted:** how long the choice is remembered (1/17 says); whether the choice
  carries across devices.

### ad-framework: Industry consent framework

- **Covers:** participation in an industry framework that passes users' ad choices to
  advertising vendors, and what it means for those choices.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.data.ad_consent_frameworks != []`
- **Facts:** `facts.data.ad_consent_frameworks`, `facts.data.cookie_controls`
- **Patterns:**
  - 2/2 name the framework inside the category or advertising text, not under its own heading.
  - 1/2 says the consent tool lists the framework's vendors and purposes; 1/2 points to the
    framework section of its privacy policy.
- **Commonly omitted:** the vendor list itself.

### browser-controls: Browser settings

- **Covers:** blocking or deleting cookies in the browser, and that such settings apply per
  device and browser.
- **Prevalence:** 19/20 (95%), core
- **Applies when:** always
- **Facts:** `facts.product.services_in_scope`
- **Patterns:**
  - 12/19 generic advice only ("see your browser's help or preferences").
  - 4/19 link each major browser's help page; 5/19 send the reader to an external help site on
    cookies.
  - 5/19 note that settings are per device and browser, or reset when cookies are cleared or a
    private window is used.
  - 2/19 make browser settings the only control on offer.
- **Quote:** "You can also manually delete previously stored cookies at any time." (s10)
- **Commonly omitted:** that browser settings do not reach app SDKs.

### account-controls: Settings in your account

- **Covers:** analytics or ad-personalisation controls inside the user's account settings.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.data.cookie_controls.account_path` is set
- **Facts:** `facts.data.cookie_controls`, `facts.product.has_accounts`
- **Patterns:**
  - 2/2 name the settings page or tab, and give signed-out visitors a separate route.
- **Quote:** "If you do not want SoundCloud to deliver “interest based” or personalized ads for third party products, you can adjust your settings in the “Advertising” tab." (s10)
- **Commonly omitted:** whether the account setting overrides the cookie choice.

### device-controls: Mobile device settings

- **Covers:** mobile operating-system settings for the advertising identifier and app tracking
  prompts, and how app tracking permission relates to the cookie choice.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.data.tracking` has an entry with surface `app` and purpose `advertising`
- **Facts:** `facts.data.tracking`, `facts.data.cookie_controls`
- **Patterns:**
  - 3/4 name the iOS and Android setting labels for limiting or resetting the ad identifier.
  - 1/4 says it does not use the iOS ad identifier for targeting; 1/4 that refusing app tracking
    does not block the account.
- **Quote:** "On your mobile device, disable the “Allow Apps to Request to Track” setting in your iOS phone’s settings, or enable the setting to “Opt Out of Ads Personalization” in your Android phone’s settings." (s10)
- **Commonly omitted:** in-app privacy toggles, which go to `consent-tool`.

### ad-opt-outs: Opting out of interest-based ads

- **Covers:** opting out of interest-based ads outside the site's own tool: industry
  programmes, vendors' own opt-outs, and the limits of opting out.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** `facts.data.targeted_ads == true`
- **Facts:** `facts.data.targeted_ads`, `facts.data.tracking`
- **Patterns:**
  - 5/9 link vendors' own opt-outs (analytics browser add-on, ad settings pages); 2/9 each named
    ad partner's privacy or ad-preferences page.
  - About 5/9 link industry opt-out programmes or resources for web and mobile.
  - 2/9 warn that opt-outs work per device and browser and are lost when cookies are cleared;
    1/9 disclaims the third-party tools it links.
- **Quote:** "You must separately opt-out on each device." (s11)
- **Commonly omitted:** which partners the industry programmes do not cover (1/9 says).

### changes: Changes to this policy

- **Covers:** how the policy changes, how users are told, and when a change takes effect.
- **Prevalence:** 11/20 (55%), common
- **Applies when:** always
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - 4/11 only post the new version and update the date; 5/11 promise notice of material
    changes (in the service or by email); 1/11 emails existing customers; 1/11 "reasonable
    means".
  - 2/11 treat continued use after a change as acceptance.
  - 1/11 says an update never switches on optional tracking without a new choice.
  - Usually two sentences near the end.
- **Quote:** "We give notice of material changes and do not treat a policy update as permission to activate optional tracking." (s15)
- **Commonly omitted:** a notice period.

### contact: Contact

- **Covers:** how to reach the company about cookies or the policy.
- **Prevalence:** 14/20 (70%), common
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.address`, `facts.company.phone`, `facts.company.dpo_contact`
- **Patterns:**
  - 10/14 one email; 3/14 email and postal address; 1/14 phone and post only.
  - 2/14 name a data protection officer or privacy team.
  - About 12/14 close the document; 2/14 give it in the opening.
- **Quote:** "If you have any questions about our use of cookies or other technologies, please email us at privacy@chipotle.com." (s07)
- **Commonly omitted:** a web form.

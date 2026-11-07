---
doc_id: data-subject-request
title: Data Subject Request Form, United States part
kind: document
family: privacy-notices
region: us
part: block
sample_languages: [en]
sample_count: 20
saturated: false                # the root pool was closed after one saturation batch; its last two new ids are this block's us-appeal content
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** What US state privacy laws (California's CCPA/CPRA and the states that followed)
  add to the request form: who the state-law form is for, the state-law request types, opt-outs
  of sale, sharing and targeted advertising, authorized agents, verification, deadlines, appeals
  and fair treatment.
- **Shape:** 14/20 forms carry US state content. 6/14 are US-only forms framed by a state law
  (3 name the CCPA in the title); 8/14 add US options to a wider form, often shown only when the
  country or state picked is in the US. A state picker drives the menu in 4/14.
- **Register:** the laws' own terms appear in option labels even when the rest is plain: "Right
  to Know", "sell or share", "sensitive personal information", "authorized agent", "verifiable
  consumer request". 3/14 make the closing statement sworn ("under penalty of perjury").
- **Recurring elements:** a pointer from the form to the cookie settings or a "Do Not Sell or
  Share" link for opt-outs (8/14); a Global Privacy Control statement (3/14).
- **Commonly omitted:** the response deadline as a number (0/14); the appeal channel and its
  deadline (3/14 mention appeals, none gives a channel or deadline); that opt-outs need no identity
  check.

Counts come from the 20 global request-form samples (`research/data-subject-request/`, *Regional
content*). The root pool was closed after one saturation batch (`saturated: false`); both ids it
added there (appeals, non-discrimination) are in this block.

## Sections

### us-scope: Who the state-law form covers

- **Covers:** that the form serves residents of US states with privacy laws, which state law it
  is under, and the data or people it leaves out.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** always
- **Facts:** `facts.users.regions`, `facts.data.subject_categories`, `facts.data.sensitive`
- **Patterns:**
  - 5/9 limit the form to US-state residents; 3/9 name the CCPA or California in the title; 1/9
    frames rights as varying "depending on the jurisdiction in which you reside" with no statute
    named.
  - 5/9 ask for the state; 2/9 change the request types with it.
  - 1/9 excludes health information covered by HIPAA and sends patients and plan members to the
    clinics' notices of privacy practices.
  - 1/9 tells employees and business contacts the law does not cover them (see *Avoid*).
- **Avoid:** telling employees, job applicants or business contacts that the CCPA does not apply
  to their data: 1/20 (s10). The employee and business-to-business exemptions in Cal. Civ. Code
  §1798.145(m) and (n) became inoperative on 1 January 2023 (§1798.145(m)(4), (n)(3)). The same
  sample still opens "Beginning January 1, 2020".
- **Quote:** "California residents, you may use this form to exercise your rights under the CCPA." (s16)
- **Commonly omitted:** the full list of states covered (2/9 name them).

### us-request-types: State-law request types

- **Covers:** the request types US state laws add or name differently: right to know (categories
  or specific pieces), access with portability, correction, deletion, limiting use of sensitive
  personal information, opting out of sale, sharing or targeted advertising, a list of specific
  third parties, consumer health data rights, appeal, and the exemptions that may limit an answer.
- **Prevalence:** 12/20 (60%), common
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.data.sensitive`, `facts.us.sells_or_shares`, `facts.data.targeted_ads`
- **Patterns:**
  - 6/12 name options with the statute's words ("Right to Know", "Right to Correct"); 3/12 tag
    options with the states they apply to, or show separate menus per group of states.
  - Right to know split into categories and specific pieces: 4/12; 2/12 keep a 12-month lookback.
  - Limit use of sensitive personal information: 5/12, as an option, a detail field or a pointer
    to the phone's location settings.
  - Opt-out of sale, sharing or targeted ads as a menu option: 7/12 (the others route it outside
    the form, see `us-opt-outs`).
  - 1/12 a list of the specific third parties data was shared with, for Oregon and Minnesota
    residents; 1/12 a consumer-health-data menu for Washington and Nevada residents.
  - 1/12 an appeal option with a box for the date, request ID and reason.
  - 1/12 warns that legal exemptions may be claimed; 1/12 lists deletion exceptions by example.
- **Quote:** "Right to Know: Right to know the categories of personal information we have collected about you in the past 12 months." (s18)
- **Commonly omitted:** that a know request may cover data older than 12 months collected since
  2022.

### us-opt-outs: Opting out of sale, sharing and targeted ads

- **Covers:** how a person opts out of the sale or sharing of their data and of targeted
  advertising (the cookie settings, a "Do Not Sell or Share" link, Global Privacy Control), and
  whether the company sells data.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** `facts.us.sells_or_shares == true` or `facts.data.targeted_ads == true`
- **Facts:** `facts.us.sells_or_shares`, `facts.data.targeted_ads`, `facts.data.honors_gpc`, `facts.data.cookie_controls`
- **Patterns:**
  - 6/8 send ad-tracking opt-outs to the cookie banner, a "Manage Cookie Preferences" link or a
    footer link rather than taking them in the form; 1/8 links a separate do-not-sell form.
  - 4/8 say Global Privacy Control is honoured, 3 of them adding that it covers only that browser
    or device.
  - 1/8 shows the opt-out branch only when the country is the United States, with two steps
    (turn off ad cookies, then submit the form).
  - 1/8 states "We don't sell your data" under the submit button.
- **Quote:** "If your browser or extension sends a Global Privacy Control signal, we will treat it as a valid request to opt-out of sharing for that browser, without you needing to do anything else." (s16)
- **Commonly omitted:** that an opt-out needs no identity check (11 CCR §7060(b)).

### us-agents: Authorized agents

- **Covers:** requests filed by an authorized agent: the agent option, the agent's and the
  consumer's details, and the written authorization asked for.
- **Prevalence:** 6/20 (30%), rare
- **Applies when:** `facts.users.request_handling.representatives.allowed == true`
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 5/6 an "authorized agent" option that opens agent fields or a note; 1/6 a principal-state
    choice for the states whose laws name agents.
  - Proof: 2/6 an upload (a power of attorney or other written authorization; 1 requires it signed
    by agent and consumer and rejects unsigned forms); 2/6 say the company will follow up; 1/6 a
    link or email; 1/6 asks for nothing.
- **Quote:** "You will need to provide proof to demonstrate that, as an authorized agent, you have the requisite authorization to act on behalf of the resident." (s06)
- **Commonly omitted:** that the company may ask the consumer to confirm the agent directly.

### us-verification: Verification and what the form may ask

- **Covers:** checking a "verifiable consumer request" before acting, the sworn statement some
  forms ask for, and limits on what may be asked to submit a request.
- **Prevalence:** 5/20 (25%), rare
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 1/5 says identity is checked before acting and an unverified request may be refused; 1/5
    warns government ID may be required.
  - 3/5 a declaration under penalty of perjury: a checkbox (2) or a printed, signed declaration
    (1).
- **Avoid:**
  - Asking for a full Social Security number to submit a request: 1/20 (s02). The CCPA
    regulations tell businesses to avoid collecting the identifiers in Cal. Civ. Code §1798.81.5(d)
    (Social Security number among them) unless necessary to verify the consumer (11 CCR
    §7060(c)(2)), and to match details already held whenever feasible (§7060(c)(1)).
  - Making the requester agree to the terms of service or payment agreements to submit a request:
    1/20 (s02). Request methods must be easy to execute, without unnecessary burden or friction
    (11 CCR §7004(a)(5)).
- **Quote:** "As part of this process, government identification may be required for authentication." (s02)
- **Commonly omitted:** that a correction request is verified on details other than the one being
  corrected (11 CCR §7060(h)).

### us-timeline: State-law deadlines

- **Covers:** the response deadline under state law.
- **Prevalence:** 3/20 (15%), rare
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 3/3 tie the answer to "the timeframe required by law" or "consistent with the law of your
    state", with no number.
- **Quote:** "We will fulfill verified requests within a timeframe consistent with the law of your state." (s03)
- **Commonly omitted:** the 45-day deadline and its one extension (Cal. Civ. Code
  §1798.130(a)(2)(A)); none of the 20 samples gives it.

### us-appeal: Appeals and fair treatment

- **Covers:** the right to appeal a refusal and how to do it, and that using one's rights brings
  no worse treatment.
- **Prevalence:** 3/20 (15%), rare
- **Applies when:** always
- **Facts:** `facts.us.appeal_process`
- **Patterns:**
  - 1/3 an appeal option in the request menu asking for the original request's date, ID and the
    reason; 1/3 one sentence that an appeal is possible, with no channel; 1/3 says the
    acknowledgement email explains how to appeal.
  - 1/20 adds a bold sentence on non-discrimination after submitting.
- **Quote:** "Note that you also have the right to appeal in the event that we decline to take action on a request to exercise one of your rights set forth above." (s18)
- **Commonly omitted:** the appeal channel, the decision deadline (60 days in Virginia, Va. Code
  §59.1-577(C)) and the attorney general contact for a denied appeal.

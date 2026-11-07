---
doc_id: privacy-policy
title: Privacy Policy, United States part
kind: document
family: privacy-notices
region: us
part: block
sample_languages: [en]
sample_count: 32
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** What US state privacy laws (California CCPA/CPRA and the states that followed)
  add to the privacy policy.
- **Shape:** 19/32 carry US state content. Placement: 11/19 inline; 8/19 a pointer to a separate
  state notice. 7/19 list the states covered by name.
- **Register:** statutory: the laws' own terms ("sell", "share", "sensitive personal
  information", "business purpose") appear here even when the main text avoids them.
- **Recurring elements:** a "Your Privacy Choices" or "Do Not Sell or Share" link (in the
  footer, outside the document).
- **Commonly omitted:** per-state differences (most give one combined list).

Counts come from the 32 global privacy-policy samples (`research/privacy-policy/`).

## Sections

### us-states: US state notices

- **Covers:** disclosures under US state privacy laws: statutory categories collected, sources,
  purposes, recipients, sensitive data.
- **Prevalence:** 19/32 (59%), common
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.us.sells_or_shares`, `facts.users.rights_channels`
- **Patterns:**
  - 6/19 map own categories to the statutory ones, 4 of them as a table (category, sources,
    purposes, recipients).
  - 5/19 add specifics: Shine the Light, Nevada sale opt-out, financial incentives, minors.
- **Quote:** "Reddit does not “sell” personal information as those terms are defined under applicable state privacy laws." (s19)
- **Commonly omitted:** per-state differences.

### us-sale-share: Sale and sharing

- **Covers:** whether targeted advertising counts as "sale" or "sharing" under state law, and
  the opt-out.
- **Prevalence:** 7/32 (22%), rare
- **Applies when:** `facts.data.targeted_ads == true` or `facts.us.sells_or_shares == true`
- **Facts:** `facts.us.sells_or_shares`, `facts.data.targeted_ads`, `facts.data.honors_gpc`
- **Patterns:**
  - 7/7 concede that ad cookies may count as "sale" or "sharing" while disputing the label.
  - Opt-out routes: a "Your Privacy Choices" link, honouring Global Privacy Control (8/32 say
    they honour it).
- **Commonly omitted:** the list of ad partners.

### us-requests: Requests, verification and appeals

- **Covers:** how state-law requests are verified, authorised agents, appeals, and
  non-discrimination.
- **Prevalence:** 9/32 (28%), rare
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`
- **Patterns:**
  - 9/32 describe verification, authorised agents and appeals.
  - 7/32 state non-discrimination.
- **Quote:** "You will not receive discriminatory treatment for exercising any of your privacy rights." (s01)
- **Commonly omitted:** the exact verification data asked for.

## Avoid on root sections

### changes

- **Avoid:** applying a material change to data already collected, with continued use as the
  only consent: part of the 13/32 that treat continued use as acceptance. The FTC's *Gateway
  Learning Corp.* order (2004) and its February 2024 statement "AI (and other) companies: quietly
  changing your terms of service could be unfair or deceptive": a retroactive material change
  needs affirmative express consent. Continued use as acceptance of prospective changes stays a
  pattern.

### deidentified

- **Avoid:** saying de-identified data may be used or disclosed without restriction, with no
  public commitment not to re-identify it: 6/12. Cal. Civ. Code §1798.140(m): data is
  de-identified only when the business publicly commits to keep it so and not to re-identify it,
  and binds its recipients to the same.

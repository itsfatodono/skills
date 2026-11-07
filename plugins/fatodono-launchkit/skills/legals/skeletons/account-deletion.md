---
doc_id: account-deletion
title: Account / Data Deletion page
kind: document
family: privacy-notices
sample_languages: [en]
sample_count: 25
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** Tells users how to delete their account and personal data, inside the product
  and without it, and what happens to their data, subscriptions and content afterwards; it is
  the public URL app stores ask for as the account-deletion link.
- **Shape:**
  - Short: median 306 words (range 36–1,465). One page; 2/25 have a table of contents.
  - 16/25 are help-center articles; 7/25 are a dedicated standalone page (six of these from
    small companies); 2/25 are one part of a larger help article or FAQ.
  - 8/25 phrase the title as the user's question ("How do I delete my account?").
  - 7/25 split the steps by platform (tabs, toggles or subheadings); the rest give one path for
    every platform.
  - 6/25 share the page with a related topic: deactivation (4) or getting a copy of one's data
    (2).
  - Many sections are a single sentence or a "Note:" callout without a heading; headings, when
    present, are task-shaped ("Before you start", "What happens after deletion").
- **Register:** 25/25 plain "we/you", short imperative sentences, UI labels in bold or quotes.
  No legal register; 2/25 open with a rights statement. Warnings are set off as "Note:" or
  "Please note:" callouts.
- **Recurring elements:**
  - A way to delete without the app (web self-service or a contact route): 23/25.
  - Support email named on the page: 11/25.
  - Privacy-policy link in the body: 8/25.
  - Visible "updated" or "effective" date: 7/25.
  - Links to sibling help articles (cancel subscription, reset password, export data): most
    help-center samples.
- **Commonly omitted:** what data is kept after deletion and for how long (17/25 say nothing);
  how long processing takes (21/25); a law or regulation by name (25/25); a deletion route for
  users who cannot sign in (9/25 give none); a date.

## Sections

Region-neutral. What one law requires goes in the region's block,
`regions/<code>/account-deletion.md`, written under the document's regional part
(`formats/region-format.md`).

### intro: About this page

- **Covers:** what the page explains, which app or accounts it applies to, and what deleting
  means.
- **Prevalence:** 11/25 (44%), common
- **Applies when:** always
- **Facts:** `facts.product.name`, `facts.company.legal_name`, `facts.product.services_in_scope`
- **Patterns:**
  - Most are one or two sentences under the title; the other 14 samples start straight with a
    warning, a choice or the steps.
  - 4/11 name the available routes up front ("in the app or by email").
  - 3/11 summarise what the page covers (how to delete, what is removed, how long it takes).
  - 2/11 frame deletion as the user's right; 2/11 route the reader by product or account role.
- **Quote:** "This page explains how to request deletion of your Bill Tracker Pro account, what data is removed, and how long it takes." (s06)
- **Commonly omitted:** the company's legal name; a definition of "account" or "personal data".

### alternatives: Alternatives to deleting

- **Covers:** lighter options instead of deleting: deactivate, downgrade to a free plan, or
  talk to support first. Deleting single items is in `partial-deletion`.
- **Prevalence:** 7/25 (28%), rare
- **Applies when:** `facts.product.deletion_alternatives != []`
- **Facts:** `facts.product.deletion_alternatives`
- **Patterns:**
  - Options split: deactivation 2/7, downgrading or stopping payment 2/7, deleting single items
    or changing a setting 2/7, contacting support first 2/7.
  - Placed before the deletion steps; 3/7 open the page with the choice.
  - Where deactivation is offered, it gets its own steps and a note on what stays visible and
    how to reactivate.
- **Quote:** "If you only want to stop paying, change your email address, change how you sign in, or remove a conversation, you may be able to do that without deleting your account." (s13)
- **Commonly omitted:** reasons to stay; retention offers beyond "contact us first".

### what-is-deleted: What is deleted

- **Covers:** the data and content removed, what the user loses (history, progress, purchases,
  balances), and that deletion cannot be undone.
- **Prevalence:** 19/25 (76%), common
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.product.features`
- **Patterns:**
  - 14/19 state that deletion is permanent or cannot be undone, usually before the steps.
  - 13/19 name what is lost by category (history, progress, saved settings, payment details).
  - 2/19 warn that paid content or funds are lost (purchased audiobooks, wallet balance).
  - 14/19 write prose or a one-line warning; 5/19 use a list or cards of data categories.
- **Quote:** "Deleting your account will permanently delete all history and driving events." (s25)
- **Commonly omitted:** field-level lists; data held by processors; a statement that deletion
  covers every platform the account is used on (3/19 say so).

### before-you-delete: Before you delete

- **Covers:** getting a copy of one's data first, and what the user must do before deletion is
  possible (uninstall from managed devices, finish orders, clear a balance, keep access to the
  sign-in email).
- **Prevalence:** 10/25 (40%), common
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.product.deletion_blockers`
- **Patterns:**
  - 8/10 offer a data export first, with a link to the export page or article; 2/10 treat a
    copy of one's data as its own request with its own route.
  - 4/10 list prerequisites as a checklist or numbered first steps; 2/10 say a balance or open
    orders block deletion.
  - 2/10 give a window after deletion in which data can still be downloaded.
- **Quote:** "Before you delete your account, download everything with Export Recipes." (s09)
- **Commonly omitted:** what the export contains; the export format.

### subscriptions: Subscriptions and payments

- **Covers:** whether deletion cancels a paid subscription, where to cancel it, and what happens
  to balances, refunds and invoices.
- **Prevalence:** 13/25 (52%), common
- **Applies when:** `facts.sales.subscription != none`
- **Facts:** `facts.sales.subscription`, `facts.product.deletion_blockers`
- **Patterns:**
  - 11/13 warn that deleting the account (or the app) does not cancel a store subscription and
    tell the user to cancel first, with a link to the cancellation article.
  - 7/13 name the app stores as the billing party; 2/13 add that web or directly billed
    subscriptions end automatically on deletion.
  - 2/13 add the reverse: cancelling a subscription does not delete the account.
  - 2/13 cover balances or unpaid charges; 1/13 refunds.
  - A highlighted "Note:" callout placed before the steps is the usual form.
- **Quote:** "Deleting your account, deleting the app, or leaving a Circle will not cancel your Life360 membership." (s25)
- **Commonly omitted:** pro-rata refunds; what happens to a running free trial.

### self-service-steps: How to delete

- **Covers:** the steps to delete the account inside the product, in the app and on the
  website.
- **Prevalence:** 22/25 (88%), core
- **Applies when:** `facts.product.deletion_routes` has an `in-app` or `web` route
- **Facts:** `facts.product.deletion_routes`
- **Patterns:**
  - 18/22 use numbered steps naming each menu item in bold or quotes ("Settings > Account >
    Delete account"); 4/22 write the path as one or two sentences.
  - 15/22 give one path for every platform; 7/22 split by platform (web / iOS / Android).
  - 13/22 give a website route, so the user needs no app; 5/22 hand off to a single web link or
    portal instead of listing steps.
  - The last step is usually "confirm" or "follow the prompts"; one sample shows a screenshot
    per step.
- **Quote:** "Scroll to the bottom and tap Delete Account." (s09)
- **Commonly omitted:** what the user sees after confirming; steps for each app version.

### confirmation: Verification and confirmation

- **Covers:** how the deletion is confirmed and how the requester's identity is checked: typed
  confirmation, password or code, email confirmation link, completion email, and what to do
  when it fails.
- **Prevalence:** 13/25 (52%), common
- **Applies when:** always
- **Facts:** `facts.product.deletion_verification`
- **Patterns:**
  - 6/13 describe identity checks for requests made outside the product: send from the
    account's email, give the username, answer ownership questions.
  - 4/13 require clicking a link in a confirmation email; 2/13 send an email once deletion is
    done.
  - 2/13 ask the user to type a word ("delete") to confirm; one uses a captcha, one a code sent
    to the app.
  - 2/13 add troubleshooting: check the spam folder, what to do if no confirmation appears.
  - 6/13 fold this into the steps or the request route rather than giving it its own block.
- **Quote:** "You will receive a confirmation email where you can complete the deletion process by clicking on the “Delete Your Account” link." (s04)
- **Commonly omitted:** what identity proof is enough; how long a confirmation link stays
  valid.

### request-route: Request deletion without the app

- **Covers:** how to ask for deletion outside the product (email, web form, support), for
  users who cannot sign in or do not have the app, and what to include in the request.
- **Prevalence:** 16/25 (64%), common
- **Applies when:** always
- **Facts:** `facts.product.deletion_routes`, `facts.company.contact_email`
- **Patterns:**
  - The route splits: email 8/16, web form or privacy portal 3/16, a generic "contact support"
    3/16, only a password-reset link 2/16.
  - 7/16 present it as the fallback for users who cannot sign in; 3/16 as the only route.
  - 8/16 ask the user to include the account's email or username.
  - 2/16 state a response time; one lists channels it does not accept (phone, post).
  - A page-specific contact line for questions closes 4/25 samples; it belongs here.
- **Quote:** "If you no longer have access to your account, please submit a "delete account" request here and include the email address of the account you would like to have deleted from our system." (s02)
- **Commonly omitted:** a response deadline; a web form that works without signing in.

### timeline: When it happens

- **Covers:** when deletion takes effect: immediately or after a grace period, how to restore
  the account within it, how long full deletion takes, and when the email or username can be
  used again.
- **Prevalence:** 13/25 (52%), common
- **Applies when:** always
- **Facts:** `facts.product.deletion_grace_period`, `facts.data.deletion_lag`
- **Patterns:**
  - 8/13 describe a grace period in which the account is deactivated and can be restored
    (signing in, an email link or support), stated in days or months; 2/13 say deletion is
    immediate.
  - 4/13 give a maximum processing time in days.
  - 6/13 say whether the email or username can be used to sign up again, and after how long;
    1/13 warns that signing in again creates a new, empty account.
- **Quote:** "After you close your account, we email you a link which you can use to reactivate it within 7 days." (s01)
- **Commonly omitted:** the time backups take to clear (see *What we keep*); notice to the user
  when the grace period ends.

### retention: What we keep

- **Covers:** data that survives deletion and why: backups, legal, tax or security records,
  de-identified data, data on the device, records held by stores or payment providers, and
  cases where deletion is refused.
- **Prevalence:** 8/25 (32%), rare
- **Applies when:** `facts.data.kept_after_deletion != []`
- **Facts:** `facts.data.kept_after_deletion`, `facts.data.retention`, `facts.product.ai_features`
- **Patterns:**
  - 4/8 name legal, security or business reasons for keeping some records; 2/8 point to the
    privacy policy for the periods instead of stating them.
  - 3/8 cover backups (2 give a period); 2/8 keep data in de-identified form; 1/8 says local
    data on the device stays until the app is removed.
  - 2/8 list cases where deletion is refused or delayed (open support case, suspected abuse,
    blocked account).
  - 1/8 claims nothing is kept and still names third-party receipts; 1/8 says whether past
    content was used to train AI models.
- **Quote:** "Your data will still be saved in backups that were made before your account deletion request." (s12)
- **Commonly omitted:** a period for each kept category; processors' retention.

### shared-content: Content shared with others

- **Covers:** what happens to content other users can see or hold: public posts, groups and
  clubs the user created, messages in others' chats, shared or family spaces.
- **Prevalence:** 5/25 (20%), rare
- **Applies when:** `facts.product.public_content != none`
- **Facts:** `facts.product.public_content`
- **Patterns:**
  - 2/5 say other users keep their copies or groups stay without the creator; 1/5 says content
    stays but is shown as anonymous; 1/5 keeps a licence to public content.
  - 2/5 explain the effect on a shared household or group.
  - 1/5 advises removing content or handing over ownership before deleting.
- **Quote:** "However, when your account is permanently deleted the content will appear as anonymous and will not be associated with you." (s22)
- **Commonly omitted:** how to delete shared content in bulk.

### other-accounts: Other account types and linked accounts

- **Covers:** accounts that delete differently: business or organisation accounts, family or
  household owners and members, secondary profiles, accounts held by partners, deceased users.
- **Prevalence:** 9/25 (36%), rare
- **Applies when:** `facts.product.account_roles != []`
- **Facts:** `facts.product.account_roles`
- **Patterns:**
  - Split: business or organisation accounts 3/9 (admin decides, or self-service is off);
    household or family roles 3/9 (owner vs member, each member deletes their own); secondary
    profiles in the same product 2/9; partner accounts that deletion does not reach 1/9;
    deceased users 1/9 (proof of death, no login details given).
  - Usually a short subheading or "Note:" with its own steps or a pointer to another article.
- **Quote:** "How you delete your account depends on your role in your household." (s11)
- **Commonly omitted:** what happens to data an admin can see after a member leaves.

### partial-deletion: Deleting part of your data

- **Covers:** deleting specific data (single items, history, backups, synced contacts) while
  keeping the account, and the route for the rest.
- **Prevalence:** 5/25 (20%), rare
- **Applies when:** `facts.product.data_deletion_controls != []`
- **Facts:** `facts.product.data_deletion_controls`
- **Patterns:**
  - 4/5 point to in-app controls, as a list of "to delete X, go to Y"; 2/5 give a contact route
    for anything else.
  - Placed after the account-deletion parts.
- **Quote:** "You can delete most of your data without deleting your Telegram account." (s20)
- **Commonly omitted:** a full list of what can be deleted item by item.

### inactivity: Automatic deletion

- **Covers:** accounts deleted automatically after a period of inactivity, what that erases, and
  how the user changes the period.
- **Prevalence:** 1/25 (4%), rare
- **Applies when:** `facts.data.inactivity_deletion != none`
- **Facts:** `facts.data.inactivity_deletion`
- **Patterns:**
  - One sample gives the default period, the reason (storage), and the setting that changes it.
- **Quote:** "You can change the exact period after which your inactive account will self-destruct in Settings." (s20)
- **Commonly omitted:** a warning sent before the automatic deletion.

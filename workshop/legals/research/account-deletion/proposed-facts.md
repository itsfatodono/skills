# account-deletion: proposed fact keys

Merged into `helpers/facts-schema.md` on 2026-10-26; see the key map below.

Keys the `account-deletion` skeleton names that `helpers/facts-schema.md` lacks. Written here because
this build may not edit `helpers/facts-schema.md` (batch-1 brief); the maintainer moves them under these
names. Format as in `helpers/facts-schema.md`.

## Shared with other proposals

### facts.sales.subscription
- **Means:** subscription plans: billing periods, automatic renewal, free trials, lifetime
  plans, and how the user cancels on each channel (App Store, Google Play, web).
- **Type:** record (periods, auto_renews: bool, trial_days, lifetime: bool, cancel_path per channel) or none
- **Look:** subscription SDKs and plans (RevenueCat, App Store / Play subscriptions, Stripe
  Billing), trial configuration, "manage subscription" screens.
- **Ask:** "Do you sell subscriptions? Which periods, is there a free trial, and how does the
  user cancel?" Recommend what the code shows.
- **Note:** same name and meaning as `facts.tr.subscription` (its *Proposed shared key*) and the
  `terms-of-service` proposal. The deletion page needs the billing channels, to say which
  subscriptions deletion does not cancel.

## New keys

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
  downgrade to a free plan, sign out, delete individual items.
- **Type:** list of (option, effect, path)
- **Look:** deactivate or pause flags, plan downgrade screens, per-item delete actions.
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

## Key map

| Proposed | Final | Note |
| --- | --- | --- |
| `facts.sales.subscription` | `facts.sales.subscription` | `trial_days` moved to `facts.sales.free_trial`, `lifetime` to `facts.sales.plans` |
| `facts.product.deletion_routes` | `facts.product.deletion_routes` |  |
| `facts.product.deletion_verification` | `facts.product.deletion_verification` |  |
| `facts.product.deletion_grace_period` | `facts.product.deletion_grace_period` |  |
| `facts.product.deletion_blockers` | `facts.product.deletion_blockers` |  |
| `facts.product.deletion_alternatives` | `facts.product.deletion_alternatives` |  |
| `facts.product.account_roles` | `facts.product.account_roles` |  |
| `facts.product.data_deletion_controls` | `facts.product.data_deletion_controls` |  |
| `facts.data.kept_after_deletion` | `facts.data.kept_after_deletion` |  |
| `facts.data.inactivity_deletion` | `facts.data.inactivity_deletion` |  |

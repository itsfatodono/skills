# Task format

A task skeleton describes something to do rather than a text to write: a registration, a
filing, a check (VERBİS, ETBİS, İYS, D-U-N-S). The build branch writes it per
`build/build-task.md`; `doc-writer` turns it into the user's checklist; `doc-checker` checks the
checklist against it.

Header: `doc_id`, `title`, `kind: task`, `authority`, `official_url`, `scanned`,
`format_version`.

## Task
- **What it is:** one sentence.
- **Applies when:** a condition on fact keys.
- **Outcome:** what exists afterwards (a registration number, a signed DPA).
- **Cost, duration, renewal.**

## Prerequisites
Each item the task needs, with its fact key.

## Steps
Ordered. Each step: the action, the official page, and who does it: `user` (needs the
user's identity, e.g. an e-Devlet login) or `agent` (can be prepared by the agent).
A route-specific step adds **Applies when:** a condition on fact keys.

A check of the user's own product is a step with these fields:

```markdown
3. **Check: opt-out takes one page visit.** `agent`
   - Inspect: unsubscribe links in the marketing email templates and the page each opens.
   - Rule: the recipient gives nothing beyond a reply email or a single page visit.
   - Passes when: every marketing template links to a page that unsubscribes on one visit,
     with no login and no field other than the email address.
   - Fix: a tokenised unsubscribe link in every marketing template.
   - Official page: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
```

## Afterwards
Where the outcome must appear, by doc id (e.g. the ETBİS number in the imprint).

Valid when the steps end in the outcome and every prerequisite has a fact key.

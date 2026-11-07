---
doc_id: data-subject-request
title: Data Subject Request Form
kind: document
family: privacy-notices
sample_languages: [en]
sample_count: 20
saturated: false                # pool closed by the owner after one saturation batch; s18 and s20 each added a region-only id
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** The web form or page a person uses to ask the company for access to, correction
  of or deletion of their personal data, and to make related requests. It also tells them how the
  request will be checked and answered.
- **Shape:**
  - A web form, not a policy text: a short intro block above the fields, then field groups, then
    a submit button and what happens next. 16/20 sit on one page; 4/20 run in steps or pages.
    13/20 are a form on the company's own site, 5/20 a hosted privacy-portal form, 1/20 a
    form-builder form on the company's sub-domain, 1/20 a request portal with sign-in.
  - Median about 570 words (range 190–1,750). Large companies about 510, mid about 655, small
    about 495. Portals that add a notice to each request type run longest.
  - Fields come in a common order: who you are and where you live, what you want, details, the
    confirming statement, then submit. 6/20 change later fields with the answer to residence, and
    2/20 with the answer to role.
  - 8/20 group fields under headings ("Your details", "Your request"); the rest use the field
    labels as the only headings.
- **Register:** 20/20 "we/you" in notices, short sentences, help-page tone. 12/20 switch to the
  first person in option labels or the confirming statement ("Download my data", "I confirm").
  Field labels are terse; notices are one to three sentences.
- **Recurring elements:**
  - Required-field asterisks; a bot check (reCAPTCHA or a hidden field) on 9/20.
  - A link to the privacy policy: 16/20.
  - An email confirmation link after submitting: 9/20.
  - A language switcher: 5/20.
  - A dated line: 1/20.
- **Commonly omitted:** a response time (12/20 give none); any word on fees (19/20); text after
  submitting (6/20 have none); a contact beyond the request channel (15/20).

Counts come from 20 forms (`research/data-subject-request/`). The pool was closed after one
saturation batch, and its last two samples each added an id that only one region's law requires. No
root id was added after the first 15, so the root sections are stable. The build is still marked
`saturated: false`.

## Sections

Region-neutral. What one law requires (state-law request types and opt-outs, authorised-agent
rules, appeals, statutory deadlines, the regime's extra rights) is in the region's block,
`regions/<code>/data-subject-request.md`, written under the document's regional part
(`formats/region-format.md`). The writer adds each region's request types to the root menu in
`request-types`, so the form offers one menu.

### intro: About this form

- **Covers:** what the form is for, which product or company it covers, that rights depend on
  where the person lives, and how to fill it in.
- **Prevalence:** 19/20 (95%), core
- **Applies when:** always
- **Facts:** `facts.product.name`, `facts.company.legal_name`, `facts.product.services_in_scope`
- **Patterns:**
  - One to five short paragraphs above the fields; 1/20 has only a title.
  - About 9/20 say rights depend on where the person lives or on "applicable law" without naming
    a law; 3/20 name a law or state in the title.
  - About 6/20 list the requests the form takes in the opening sentence.
  - 4/20 add what to have ready, what to read first, or the steps in order ("select your request
    type, complete the acknowledgement, and click Submit").
- **Quote:** "You may use this portal to exercise certain rights and choices you may have under data protection laws." (s12)
- **Commonly omitted:** what the product does; which surfaces (app, website) the form covers.

### eligibility: Who can use this form

- **Covers:** who may use the form and who may not: residence limits, an age floor, groups whose
  data is handled elsewhere, and where those left out go.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** always
- **Facts:** `facts.product.min_age`, `facts.data.subject_categories`
- **Patterns:**
  - 6/20 limit the form to residents of named places; 1/20 sends everyone else to a general
    contact form.
  - 3/20 turn away groups whose data is handled through another process: current staff (to an
    HR portal), patients or plan members (to other notices), users who cannot be identified.
  - 1/20 sets an 18+ floor and sends minors to a parent or guardian.
  - The forms with no limit say nothing about scope.
- **Quote:** "You must be eighteen (18) years of age or older to make a request; if you are under 18 years of age, your parent or legal guardian must make the request on your behalf." (s10)
- **Commonly omitted:** where staff and job applicants send their requests.

### handler: Who handles your request

- **Covers:** which company, affiliate or team receives and answers the request, and who runs the
  form.
- **Prevalence:** 6/20 (30%), rare
- **Applies when:** `facts.company.group_companies` is not empty, or `facts.company.privacy_owner`
  names a privacy team or officer
- **Facts:** `facts.company.legal_name`, `facts.company.group_companies`, `facts.company.joint_controllers`, `facts.company.privacy_owner`
- **Patterns:**
  - 3/6 name the privacy team or data protection officer that receives the form.
  - 3/6 deal with group companies: an affiliate may answer for some products, affiliates follow
    their own policies, or the form covers named subsidiaries.
  - 1/6 names the vendor that runs the request portal.
- **Quote:** "If your request relates to a rental car or taxi reservation, you may also receive a response from Booking.com Transport Limited." (s01)
- **Commonly omitted:** the legal entity that decides on the request.

### privacy-link: Privacy policy

- **Covers:** the pointer to the privacy policy for how data is used and which rights exist.
- **Prevalence:** 16/20 (80%), core
- **Applies when:** `facts.company.published_policies` lists a privacy policy
- **Facts:** `facts.company.published_policies`
- **Patterns:**
  - One sentence with a link, usually in the intro; 2/16 repeat it above the submit button.
  - 1/16 points to the policy's rights section specifically.
  - 2/16 make submitting the form a confirmation that the policy was read; 1 of them also makes
    the person agree to the terms of service and payment agreements, reused from a sign-up form.
- **Quote:** "Our privacy notice explains how and why we use your personal information – including what details we hold, who we might share it with, and your choices and rights." (s07)
- **Commonly omitted:** which part of the policy describes requests.

### contact: Questions about your request

- **Covers:** how to reach the company or its privacy team with questions about a request.
- **Prevalence:** 5/20 (25%), rare
- **Applies when:** `facts.company.dpo_contact` names a data protection officer, or
  `facts.company.phone` is set
- **Facts:** `facts.company.contact_email`, `facts.company.phone`, `facts.company.address`, `facts.company.dpo_contact`
- **Patterns:**
  - 3/5 a footer under the form with a postal address and privacy email; 1 adds the legal entity
    and a phone number.
  - 1/5 a phone number with business hours only; 1/5 a support email in the intro and footer.
  - The other 15/20 give no contact beyond the request channel itself.
- **Quote:** —
- **Commonly omitted:** a named privacy officer.

### data-use: How we use what you send

- **Covers:** how the details given in the form are used and protected.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** always
- **Facts:** `facts.users.request_handling`, `facts.processors.list`
- **Patterns:**
  - 7/8 one purpose-limit sentence: the details are used only to verify identity, find the data
    and answer.
  - 1/8 names the portal vendor and says the data is encrypted between the person and the
    company.
  - Usually in the intro or just above the submit button.
- **Quote:** "The information you provide here will be processed solely for the purpose of verifying your identity and residency, locating personal information related to you, and completing your request." (s09)
- **Commonly omitted:** how long request records are kept.

### other-routes: Requests this form does not handle

- **Covers:** requests or choices the form does not take and where they go instead.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.data.cookie_controls`, `facts.product.data_deletion_controls`, `facts.product.support`
- **Patterns:**
  - 6/13 send cookie or ad-tracking choices to the cookie settings or a footer link; 2/13 send
    location choices to the phone's settings.
  - 3/13 separate customer service from privacy requests and point to the help centre or bookings
    area.
  - 3/13 point to a separate form or portal; 3/13 to account settings or self-service pages; 3/13
    to a support email.
  - 2/13 exclude data handled under other rules (medical records), 1 of them without saying
    where to go.
- **Quote:** "We would like to remind you that this form is strictly for privacy-related requests." (s19)
- **Commonly omitted:** a link for every excluded request.

### timeline: When we will respond

- **Covers:** how long the company takes to answer, when the clock starts, extensions, and
  whether a request costs anything or may be refused.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 2/8 give a number of days or months, 1 with a notice of extension and that the clock starts
    once identity is verified.
  - 4/8 say "within the time required by law" with no number; 1/8 "as soon as possible".
  - 1/8 gives a processing window for opt-outs only.
  - 1/20 says requests are free and that unfounded or excessive requests may be refused, with
    reasons given (merged id `fees-refusal`).
- **Quote:** "We'll send you a copy of the relevant data you've requested within 1 month." (s07)
- **Commonly omitted:** a number (6/8 give none); fees (19/20).

### verification: How we verify your identity

- **Covers:** how the company checks that the requester is the person the data is about, and what
  happens if that fails.
- **Prevalence:** 18/20 (90%), core
- **Applies when:** always
- **Facts:** `facts.users.request_handling`, `facts.product.has_accounts`
- **Patterns:**
  - 9/18 an email confirmation link after submitting; the request starts only once it is clicked.
  - 1/18 sign-in for account holders; 4/18 matching the details against the account or records;
    1/18 a reference from a past order.
  - 3/18 ask for or allow ID documents (1 requires them with an upload checklist); 1/18 a signed
    declaration.
  - 4/18 say only that more information may be asked; 1 adds "only if strictly necessary".
  - 3/18 say what happens on failure: the request may be refused, an unconfirmed request is
    cancelled, or a mismatch must be resubmitted.
  - Often announced in the intro and repeated after submitting.
- **Quote:** "We will only request additional information if strictly necessary." (s14)
- **Commonly omitted:** which documents are accepted; what happens to verification data.

### requester-type: Your relationship to us

- **Covers:** the person's relationship to the company, asked as a field.
- **Prevalence:** 14/20 (70%), common
- **Applies when:** always
- **Facts:** `facts.data.subject_categories`, `facts.company.collects_applicant_data`, `facts.product.account_roles`
- **Patterns:**
  - 6/14 customer, employee or job applicant, or other; 4/14 the product's own roles (client,
    provider, coach, parent).
  - 5/14 offer a no-account or website-visitor option.
  - 1/14 a single "customer?" checkbox; 1/14 one option only.
  - 2/14 use the answer to change the request types or follow-up questions.
- **Quote:** "Please select this box if you have applied for a job or have worked for Intercom and you are invoking your rights in an employment capacity." (s09)
- **Commonly omitted:** a link to the staff privacy notice.

### representative: Requests for someone else

- **Covers:** whether someone may file for another person (an agent, a parent for a child), the
  representative's and the person's details, and the proof of authority asked for.
- **Prevalence:** 10/20 (50%), common
- **Applies when:** always
- **Facts:** `facts.users.request_handling`, `facts.product.min_age`
- **Patterns:**
  - 7/10 a self-or-representative choice in the form that opens the representative's fields; 1/10
    a relationship dropdown; 1/10 a postal route for third parties.
  - Proof: 4/10 signed written authority uploaded or enclosed (1 rejects unsigned forms); 2/10 "we
    will contact you"; 1/10 a link or email; 3/10 ask for nothing.
  - 3/10 cover parents filing for a child.
- **Quote:** "If you are submitting this request on behalf of another person, please attach a signed mandate" (s11)
- **Commonly omitted:** how the person represented is told or asked to confirm.

### request-types: What you want to do

- **Covers:** which requests the form takes and how the person picks one.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.marketing.email`, `facts.marketing.sms`, `facts.product.ai_features`
- **Patterns:**
  - 13/20 one request per submission (radio, dropdown or buttons; 2 fixed to access only); 6/20
    several at once; 1/20 no selector.
  - Access 20/20, deletion 18/20, correction 14/20; other request types come from the regional
    blocks.
  - 9/20 name options as rights ("Right to Correct"); 6/20 as first-person goals ("Download my
    data", "Delete my account"). 6/20 explain each option in one line.
  - 7/20 add choices of the company's own: unsubscribe from marketing, stop sharing within the
    group, opt out of model training, delete one app's account, see who accessed my data, contact
    the data protection officer. 3/20 take complaints as a type; most end with "Other".
  - 7/20 show different menus by residence or role.
- **Quote:** "Erase your personal data from our system." (s01)
- **Commonly omitted:** what each request does (14/20 give bare labels).

### residence: Where you live

- **Covers:** the person's country, state or region, asked as a field.
- **Prevalence:** 12/20 (60%), common
- **Applies when:** always
- **Facts:** `facts.users.regions`
- **Patterns:**
  - 4/12 every country; 4/12 a state picker; 1/12 a short list of broad regions; 1/12 only the
    countries served.
  - 6/12 change the request types or later questions with the answer; 2/12 prefill it from the
    visitor's location.
  - 1/12 asks which country the request concerns rather than residence.
- **Quote:** "Please tell us your country of residence." (s19)
- **Commonly omitted:** why residence is asked.

### identity-fields: Your details

- **Covers:** the identifying and contact details asked to find the person's data and reply.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.users.request_handling`, `facts.product.has_accounts`
- **Patterns:**
  - 19/20 name and email (or sign-in); 1/20 email and phone only.
  - Phone required in 5/20; postal address required in 4/20, optional in 2/20; date of birth in
    3/20.
  - 5/20 an account, product or staff identifier, often optional ("only if it differs from your
    contact email"); 3/20 past names, addresses or identifiers.
  - 3/20 say the email is used for verification.
  - 1/20 asks for a full national ID number.
- **Quote:** "We'll send an email to this address to verify your identity." (s01)
- **Commonly omitted:** why each detail is needed.

### status: Track your request

- **Covers:** checking an earlier request, and what happens when one is already open.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.users.request_handling.status_tracking == true`
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 1/2 a link that verifies the person and opens past requests, with a status for each stage
    (in progress, ready to download, completed, cancelled).
  - 2/2 block a second request of the same kind while one is open.
- **Quote:** "You seem to already have an active request." (s01)
- **Commonly omitted:** a reference number to quote.

### request-details: About your request

- **Covers:** details of the request itself: a description, which data or which correction, a
  time period, fields for one request type.
- **Prevalence:** 16/20 (80%), core
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`
- **Patterns:**
  - 14/16 a free-text box; 4/16 cap its length (50 to 5,000 characters); 3/16 ask not to put
    personal data in it.
  - 3/16 show detail fields only for some request types (the corrected values for a correction).
  - 3/16 a date range; 2/16 a checklist of the product's data or record categories.
  - 1/16 an optional upload for supporting documents.
- **Quote:** "In this description of your request, please do not submit personal information beyond that which is requested of you." (s09)
- **Commonly omitted:** an example of a useful description.

### request-effects: What your request does

- **Covers:** what a given request does or returns, and its limits.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** always
- **Facts:** `facts.data.kept_after_deletion`, `facts.product.deletion_blockers`, `facts.product.account_roles`
- **Patterns:**
  - 4/8 say what deletion removes and keeps: records kept for legal duties, the account closed,
    linked services lost, a narrower option suggested.
  - 2/8 say what an access request returns and its limits: records kept only for a period,
    others' data withheld.
  - 1/8 explains what each opt-out stops and what continues; 1/8 warns that legal exceptions may
    limit the answer.
  - Usually a notice shown when the request type is picked.
- **Quote:** "Deleting your MyPhilips account will remove your access to those services and delete your data associated with those services." (s19)
- **Commonly omitted:** what correction changes beyond the record named.

### alt-channels: Other ways to ask

- **Covers:** other ways to send the same request or its documents, or to carry it out without the
  form.
- **Prevalence:** 7/20 (35%), rare
- **Applies when:** `facts.users.rights_channels` lists a route other than the web form
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`, `facts.company.dpo_contact`
- **Patterns:**
  - 3/7 the app: an in-app request or self-service export and deletion.
  - 3/7 email, for the request or for documents; 1/7 post and phone (post required for third
    parties).
  - 1/7 the data protection officer's email when the form or the inbox fails.
- **Quote:** "If you have a Bolt account, you can also submit requests via the Help section of the Bolt app following these steps." (s15)
- **Commonly omitted:** whether the other routes are answered in the same time.

### confirmation: After you submit

- **Covers:** what happens right after sending: confirmation screen or email, a reference, review
  and reply, and how the answer is sent.
- **Prevalence:** 14/20 (70%), common
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 5/14 "a representative will review your request and reply by email" (hosted-portal default
    wording, counted once).
  - 1/14 shows a request ID; 1/14 a status for each stage; 1/14 an acknowledgement email.
  - 1/14 warns that not every submission gets a receipt; 1/14 shows only a browser alert and
    sends nothing (a broken form).
  - 2/20 ask how the answer should be sent: email or post, or the reply language (merged id
    `response-method`).
  - None gives the response time here.
- **Quote:** "Please check your email for confirmation, click confirm and we will start your request." (s11)
- **Commonly omitted:** a reference number (13/14 give none).

### attestation: Your confirmation

- **Covers:** the requester's statement that the details are true and that they are the person or
  are allowed to act for them.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 6/9 a required checkbox or confirm list just above submit; 2/9 agreement by submitting; 1/9 a
    signed declaration to print and upload.
  - One first-person sentence covering accuracy and identity or authority; 3/9 make it sworn.
  - 1/9 adds consent to be contacted for verification.
- **Quote:** "I confirm that the information provided is accurate and that I am the data subject or an authorized agent." (s14)
- **Commonly omitted:** what happens if the statement is false.

---
doc_id: ip-assignment
title: IP Assignment for founders and employees
kind: document
family: company
sample_languages: [en]
sample_count: 25
saturated: true
scanned: 2026-11-12
format_version: 2
# Samples: 25 SEC EDGAR exhibits (9 large, 8 mid, 8 small filers): 19 employee and 1 consultant
# invention assignment and confidentiality agreements, and 5 founder assignments of technology
# made before the company existed or took it over. The standard-form route (Cooley GO CIIAA) is a
# generator behind a bot wall, so no standard form is among them. One skeleton serves both
# signers: the founder form uses a subset of the employee form's sections plus `warranties` and
# its own consideration (`compensation`), and no section is founder-only. Every founder sample is
# a separate short instrument, so a founder's pre-company work is written as its own signed part
# (see `assignment`). Founder forms come only from small filers, so size and signer overlap.
---

## Document

- **Purpose:** The agreement under which a person who works for the company (founder, employee,
  contractor) keeps its information confidential and hands it the inventions and other IP they
  make for it, and under which a founder transfers what they built before the company existed.
- **Shape:**
  - Two shapes. 20/25 are an ongoing agreement for an employee or consultant (median about 4,000
    words, range 2,500–15,400). 5/25 are a one-off founder assignment of identified technology
    (median about 1,600 words, range 1,250–13,600, the top an asset-purchase form with closing
    conditions).
  - 12/25 stand alone; 13/25 are attached to another agreement that makes signing a condition of
    the job: an offer letter (8), an employment agreement (3), a separation letter (1), a
    consulting agreement (1).
  - 23/25 number their sections; 20/25 end with schedules: a prior-inventions list (16/25), a
    statement of the legal limit on what can be assigned (9/25), an exit certificate (3/25), in
    founder forms a schedule of the assigned technology (3/5).
- **Register:** 16/25 are written in the signer's first person ("I agree", "I hereby assign")
  with the company in the third person; 9/25 in the third person throughout ("Employee",
  "Assignor"), including all five founder forms. 1/25 is a plain-English rewrite with short
  sentences. Most use formal drafting with long "including without limitation" lists; about 14/25
  set the employment-status, advice-of-counsel or governing-law clause in capitals.
- **Recurring elements:**
  - A preamble naming the company (often widened to its group) and the signer, and stating the
    consideration: 25/25.
  - Signature blocks: 25/25, the company countersigning in most.
  - An effective date reaching back to the first day of any service: 9/25.
  - Defined terms set inline in quotes; a definitions block or clause in about 9/25.
  - 22/25 of the filed copies are signed, mostly executives' copies of the standard form; 3/25 are
    unsigned forms.
- **Commonly omitted:** a table of contents (25/25 have none); a summary; any duty on the company
  beyond paying (founder forms) or giving access to its information (1/25); arbitration (3/25 in
  the agreement, 3 more in a separate agreement beside it); the company's right to use the
  signer's name and likeness (4/25); closing conditions for a deferred transfer (1/25).

## Sections

Region-neutral. What one law requires (statutory limits on assigning own-time inventions and the
notice of them, trade-secret whistleblower notices, copyright ownership rules, compensation owed
for employee inventions, limits on non-competes, employment-status statements) is in the region's
block, `regions/<code>/ip-assignment.md`, written under the document's regional part
(`formats/region-format.md`). The region that applies is where each signer lives and works
(`facts.company.staff_locations`).

### parties: Parties and consideration

- **Covers:** who the agreement binds (the company, widened to its group, and the signer), why it
  is signed, from when it applies, and what the signer receives for signing.
- **Prevalence:** 25/25 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.entity_form`, `facts.company.address`, `facts.company.ip_signers`, `facts.company.founders`
- **Patterns:**
  - 20/20 employee and consultant forms open with one preamble sentence; 17/20 widen "the
    Company" to its subsidiaries, parents, affiliates, successors and assigns.
  - About 17/20 give employment (or the engagement) and its pay as the consideration, often "as a
    condition of" it; 3/20 add that the company will give access to its confidential information;
    2/20 have the signer accept the consideration as sufficient.
  - 9/25 make the agreement reach back to the first day of any earlier service, contracting
    included, or to work done for the company's predecessors or founders.
  - 5/20 add a recital of the company's interest in protecting its information and inventions.
  - 5/5 founder forms set out the parties with their roles ("Assignor", "Assignee"); 4/5 add
    recitals that the founder created the technology and the company wants it; 2/5 bring in a
    third signer (a parent company, an officer bound personally).
- **Detail:** names the parties and their roles; the consideration in kind ("employment", "the
  shares"), never as amounts. No addresses for the signer in 20/25.
- **Quote:** "Accordingly, in consideration of the mutual promises and covenants contained herein, Employer (on behalf of itself and Company) and I agree as follows:" (s04)
- **Commonly omitted:** a recital of the business (21/25); the signer's address.

### confidentiality: Confidential information

- **Covers:** what counts as the company's confidential information and what does not; the duty
  not to use or disclose it and for how long; information third parties entrusted to the
  company.
- **Prevalence:** 22/25 (88%), core
- **Applies when:** always
- **Facts:** `facts.company.business_scope`, `facts.company.ip_signers`
- **Patterns:**
  - 22/22 define it by a general test (non-public, belongs to or is held by the company) followed
    by an open list of kinds: technical (code, designs, know-how, inventions), business (plans,
    pricing, finances), customers and suppliers, staff.
  - 18/22 make the duty last during the relationship and after it with no end date; 2/22 set a
    fixed fallback period only where a court will not enforce an open-ended one.
  - 16/22 extend the duty to information third parties gave the company, used only as the
    company's agreement with them allows.
  - About 13/22 list exclusions: public through no fault of the signer, known before, made
    independently, received lawfully from others; the rest list none.
  - 7/22 require approval before publishing or lecturing on work topics; 3/22 ban reverse
    engineering; 2/22 oblige the signer to report misuse; 2/22 bind the signer to the company's
    security rules.
  - In founder forms (2/5) the duty covers the technology assigned and the terms of the deal; 1/5
    makes it mutual.
- **Detail:** kinds of information by category with "such as" examples; never the company's own
  products, codenames, customers or systems. Duration as "during and after", or a fixed number of
  years where one is set.
- **Quote:** "I agree that the restrictions in Section 1.1 are intended to continue indefinitely, even after my employment by Company ends." (s04)
- **Commonly omitted:** marking rules for confidential material; what happens to information
  that becomes public later (most exclusions cover only information public at the time).

### protected-disclosures: What confidentiality does not stop

- **Covers:** disclosures the confidentiality duty does not bar: reports of suspected wrongdoing
  to authorities, disclosures a law or court compels, and talk about pay, working conditions or
  unlawful acts at work.
- **Prevalence:** 13/25 (52%), common
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 12/13 allow reporting a suspected breach of law to officials or a lawyer in confidence; 6/13
    add filing a charge with or cooperating with government agencies without telling the company
    first, with agencies named as examples in 5/13.
  - 8/13 keep the signer free to discuss pay, working conditions or unlawful acts at work, as far
    as the law protects that talk.
  - 5/13 allow disclosure a court or law compels, after prompt notice so the company can seek a
    protective order.
- **Detail:** describes the kinds of disclosure in general terms; where agencies are named they
  are examples. A statutory notice or immunity text is the region block's.
- **Quote:** none
- **Commonly omitted:** a contact inside the company for reports (13/13).

### prior-obligations: Earlier duties to others

- **Covers:** the signer's promises about duties owed elsewhere: no conflicting agreement, and no
  bringing or using a former employer's or anyone else's confidential information.
- **Prevalence:** 19/25 (76%), common
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 19/19 have the signer represent that signing and doing the job breaches no other agreement,
    and promise to enter no conflicting one; 6/19 name non-competes and confidentiality agreements
    as examples.
  - 16/19 bar using or bringing onto company premises or systems a former employer's or other
    party's confidential information without that party's written consent.
  - 3/19 have the signer indemnify the company for breaching duties owed to others; 2/19 add that
    no claim over past work is pending.
  - 1/19 has the signer warrant a search of their devices and accounts for a former employer's
    material.
- **Detail:** one or two sentences of representation, in general terms; no former employer named.
- **Quote:** "I have not entered into, and I agree I will not enter into, any written or oral agreement in conflict with this Agreement." (s04)
- **Commonly omitted:** a list of the signer's existing agreements (19/19 have none).

### assignment: Who owns what the signer makes

- **Covers:** which inventions and works pass to the company, on what test, and how: the
  definitions of invention and IP rights, the present assignment, the period after leaving that
  the assignment still reaches, and onward assignment at
  the company's direction. For a founder, the identified technology made before the company and
  its transfer.
- **Prevalence:** 25/25 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.business_scope`, `facts.company.founder_prior_work`, `facts.company.founders`
- **Patterns:**
  - About 20/25 use present words of assignment ("hereby assign"); 6/25 add "and agree to assign"
    for inventions made later; 1/5 founder forms confirms an earlier assignment and 1/5 only agrees
    to assign at a later closing.
  - About 22/25 define the inventions by an open list of kinds (ideas, inventions, software in
    source and object code, designs, works of authorship, know-how, trade secrets) and the IP
    rights by type (patents, copyright, marks, trade secrets, moral rights, database rights) under
    any country's law.
  - The test splits: about 12/20 ongoing agreements take what relates to the business, results
    from the work or uses company resources; about 8/20 take anything made during the relationship,
    in or out of working hours.
  - 8/25 reach inventions made in a fixed period after leaving (months or years), by a presumption
    or a continuing disclosure duty.
  - 11/25 have the signer assign a given invention onward to a customer or government on the
    company's direction; 5/25 have inventions held in trust until assigned; 2/25 say the signer gets
    no licence to the company's IP.
  - Founder forms (5/5) transfer identified technology: all right, title and interest, with
    goodwill and the right to sue for past infringement (3/5); 3/5 describe it on a schedule
    (registered filings listed one per line, or the technology by type and parts), 2/5 in a
    one-line definition. All five are separate instruments, signed by the founder and by the
    company, often through the same founder as its officer.
- **Detail:** inventions and rights by kind, with "such as" lists; the business named in general
  terms. Founder forms are the only ones that name the assets (a platform, a technique, filings by
  number); ongoing agreements never list the company's products or repositories.
- **Quote:** "Executive hereby assigns to Company or its designee all of Executive's right, title and interest in and to all of the foregoing." (s02)
- **Commonly omitted:** a holdover period after leaving (17/25 have none); onward assignment
  (14/25); in founder forms, an assignment of future improvements.

### prior-inventions: What the signer keeps from before

- **Covers:** inventions the signer made before the relationship and keeps: the list of them,
  what an empty list means, and the licence the company gets when one is built into its work.
- **Prevalence:** 21/25 (84%), core
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`, `facts.company.founder_prior_work`
- **Patterns:**
  - 18/21 have the signer list them on a schedule (2 of these were not filed); 1/21 asks for a
    list within days of signing; 2/21 have the signer represent there are none, with no schedule.
  - 16/21 say that no list means there are none, as a representation.
  - 21/21 give the company a licence if the signer builds one into company work: non-exclusive,
    royalty-free, perpetual, irrevocable, worldwide, with the right to sublicense, in nearly every
    case; 3/21 ask the signer to tell the company before using one.
  - Schedule layouts: tick boxes for "none", "see below" and "extra sheets attached" (11/18);
    columns for title, date and an identifying number or short description (9/18). 2/21 add a
    second table for inventions the signer cannot describe because of a duty to someone else.
  - 7/21 limit the list to inventions that relate to the company's business.
- **Detail:** the schedule asks for a title, a date and a brief description, never technical
  detail; the licence is described by its terms, not by any product.
- **Quote:** "If no such list is attached, I represent and agree that it is because I have no Excluded Inventions." (s01)
- **Commonly omitted:** what happens if the signer later disputes the list (21/21).

### invention-disclosure: Telling the company about inventions

- **Covers:** the duty to tell the company promptly about inventions, during the relationship
  and for a time after it.
- **Prevalence:** 17/25 (68%), common
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 17/17 require prompt disclosure, written in 11/17; 6/17 cover every invention made during the
    relationship, including ones the signer believes are excluded, so the company can judge.
  - 7/17 keep the duty running for a fixed period after leaving, some covering patent
    applications filed in that period.
  - 2/17 hold the disclosed invention in trust for the company; 1/17 names the person to tell (the
    immediate supervisor).
- **Detail:** one or two sentences; the form, channel and deadline for a disclosure are left
  general ("promptly", "in writing").
- **Quote:** "I will promptly disclose to the Company all Employment Inventions." (s22)
- **Commonly omitted:** a disclosure form or channel (16/17); a deadline in days.

### compensation: What the signer gets for the IP

- **Covers:** what the signer receives for the IP itself, apart from the job: shares, a price, a
  nominal sum, royalties, or a statement that nothing more is owed.
- **Prevalence:** 11/25 (44%), common
- **Applies when:** always
- **Facts:** `facts.company.founder_prior_work`
- **Patterns:**
  - 5/5 founder forms state it: shares issued under a separate stock purchase (1/5), a nominal sum
    payable on signing (1/5), the acquisition of the founder's company (1/5), a price with royalties
    and escrow (1/5); 1/5 has the founder confirm nothing is owed.
  - 6/20 ongoing agreements say the pay already covers the IP and no royalty or extra payment is
    owed.
  - 1/20 adds that the company alone decides whether to exploit an invention.
- **Detail:** the kind of consideration (shares, a sum, royalties) named; amounts and share
  numbers sit in the deal documents or blanks, never in the clause text of the ongoing agreement.
- **Quote:** "Such shares shall be the only consideration required of Company with respect to the subject matter of this Agreement." (s15)
- **Commonly omitted:** any payment for employee inventions (14/20 ongoing agreements are silent).

### moral-rights: Moral rights

- **Covers:** the signer's waiver of moral rights (attribution, integrity) and of other rights
  that cannot be assigned, with a fallback.
- **Prevalence:** 16/25 (64%), common
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 8/16 say the assignment includes moral rights and, where they cannot be assigned, waive
    their enforcement and any claim against the company and its licensees.
  - 5/16 state a plain waiver and a promise never to assert them; 4/16 bind heirs and successors.
  - 7/16 define moral rights by kind (attribution, integrity, disclosure, withdrawal), some adding
    the French term.
  - 2/16 add a fallback licence where even a waiver is not allowed.
- **Detail:** the kinds of moral right named in general; no work, credit line or product named.
- **Quote:** none
- **Commonly omitted:** any credit the company will give the signer (16/16).

### assistance: Help to secure the rights

- **Covers:** the duty to help the company obtain, register, perfect and enforce its rights,
  during and after the relationship, and the power of attorney that backs it.
- **Prevalence:** 24/25 (96%), core
- **Applies when:** always
- **Facts:** `facts.company.signatory`
- **Patterns:**
  - 24/24 require signing applications, assignments and other papers on request, in any country;
    about 18/24 keep the duty after the relationship ends; about 15/24 at the company's expense, a
    few paying a fee for time spent after leaving.
  - 21/24 appoint the company and its officers attorney-in-fact to sign if the signer cannot or
    will not, irrevocable and "coupled with an interest" in most; 2/24 name one officer role.
  - 5/24 have the signer waive or quitclaim infringement claims against the company over the
    assigned rights.
  - Founder forms (4/5) oblige the founder to complete the transfer and, in 1/5, to hand over
    every document and know-how about the technology.
- **Detail:** the acts listed by kind (applications, oaths, assignments, testimony); no registry,
  office or filing named.
- **Quote:** "This appointment is coupled with an interest in and to the Inventions and Creative Works and shall survive Employee's death or disability." (s10)
- **Commonly omitted:** a limit on how long after leaving the duty lasts (24/24).

### warranties: The signer's promises about the IP

- **Covers:** the signer's warranties about the IP assigned (sole owner, no prior grant or
  encumbrance, no infringement, authority to sign) and the indemnity for a breach of them.
- **Prevalence:** 8/25 (32%), rare
- **Applies when:** `facts.company.founder_prior_work != []`
- **Facts:** `facts.company.founder_prior_work`
- **Patterns:**
  - 5/5 founder forms carry them: an enumerated list (sole owner, no earlier assignment, licence or
    encumbrance, full authority, no infringement known, no conflicting agreement) in 3/5; a short
    or knowledge-qualified warranty in 2/5.
  - 2/5 founder forms add an indemnity from the founder for infringement claims or a breach; 1/5
    makes the company give its own warranties of authority in return.
  - 3/20 ongoing agreements add a warranty that the signer's work will not infringe others'
    rights; 1/20 that delivered code carries no malicious code.
- **Detail:** warranties as a list of statements; knowledge qualifiers where used ("to the best of
  my knowledge"); no named third party or claim.
- **Quote:** none
- **Commonly omitted:** a time limit or cap on the warranties (8/8).

### records: Records of inventions

- **Covers:** the duty to keep records of inventions and to hand them over.
- **Prevalence:** 13/25 (52%), common
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 13/13 require adequate and current written records, in any form the company asks for; about
    10/13 name examples (notes, sketches, drawings, electronic files, notebooks).
  - About 9/13 say the records are the company's property, available to it at all times and handed
    over on leaving.
- **Detail:** one or two sentences; formats as examples; no tool, system or lab-notebook rule.
- **Quote:** "I will keep and maintain adequate and current written records with respect to all Employee Inventions (“Records”)." (s05)
- **Commonly omitted:** where records are kept.

### open-source: Open-source code in company work

- **Covers:** whether the signer may put open-source or other third-party code into company
  work.
- **Prevalence:** 5/25 (20%), rare
- **Applies when:** `facts.product.third_party_components != none`
- **Facts:** `facts.product.third_party_components`
- **Patterns:**
  - 5/5 bar code under licences that would force the company to disclose or license its own
    source code, without written permission or outside the company's policy; 3/5 name copyleft
    licences as examples.
  - 1/5 adds that delivered work must be free of harmful code.
- **Detail:** licences described by their effect, with one or two named as examples; no list of
  allowed licences.
- **Quote:** none
- **Commonly omitted:** the company's open-source policy itself (5/5 only point to it).

### excluded-inventions: What the signer keeps from the relationship

- **Covers:** inventions made during the relationship that the signer keeps (on their own time,
  without company equipment or information, unrelated to the business or the work), and how the
  signer claims one.
- **Prevalence:** 16/25 (64%), common
- **Applies when:** always
- **Facts:** `facts.company.business_scope`
- **Patterns:**
  - 13/16 use a three-part test: made entirely on the signer's own time, without the company's
    equipment, facilities or confidential information, and neither related to the business or its
    research nor resulting from work for the company.
  - 5/16 require the signer to disclose an invention they think is excluded, so the company can
    check, and put the burden of proof on the signer.
  - 1/16 ties the carve-out to outside activities the company has approved.
- **Detail:** the test in general terms, as the contract's own rule. A statute's wording or
  notice of the limit is the region block's.
- **Quote:** none
- **Commonly omitted:** a procedure or deadline for the company to answer a claim (16/16).

### conflicting-activities: Outside work during the relationship

- **Covers:** the duty of loyalty and the limits on outside work or conflicting interests while
  the relationship lasts.
- **Prevalence:** 16/25 (64%), common
- **Applies when:** always
- **Facts:** `facts.company.business_scope`
- **Patterns:**
  - 16/16 bar competing or conflicting employment or business during the relationship without
    written consent; about 12/16 limit it to the relationship, with no post-employment
    non-compete in the same clause.
  - 2/16 attach a conflict-of-interest policy (situations to avoid, gifts, outside roles); 1/16
    lists the signer's existing investments as allowed.
  - 4/16 add a duty of undivided loyalty, to act in the company's best interest or give full
    working time.
- **Detail:** activities by kind; no named competitor.
- **Quote:** none
- **Commonly omitted:** how to ask for consent (16/16).

### return-of-property: Leaving the company

- **Covers:** company property and information when the signer leaves: return, deletion from
  personal devices, inspection, no expectation of privacy on company systems, and the exit
  certificate.
- **Prevalence:** 20/25 (80%), core
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 20/20 require returning all company property and information (an open list of kinds:
    documents, data, devices, records, notes) on leaving or on request, keeping no copies.
  - 8/20 deal with company data on personal devices and accounts (hand it over, then delete it),
    3/20 in set steps; 4/20 bar copying, deleting or altering information on company devices
    before return.
  - 12/20 say there is no expectation of privacy in company systems or property, open to
    inspection; 2/20 extend inspection to personal devices used for work.
  - 14/20 have the signer certify the return in writing on leaving; 3/20 attach the certificate's
    form, which also restates the duties that go on.
  - 1/20 puts domains and social accounts made for the company in its name.
- **Detail:** property by kind; no system, tool or account named.
- **Quote:** "I will not copy, delete, or alter any information contained upon my Company computer or Company equipment before I return it to Company." (s04)
- **Commonly omitted:** a deadline in days for returning property; who to return it to.

### non-solicitation: No poaching after leaving

- **Covers:** after the relationship: no soliciting or hiring the company's staff, and no
  soliciting or interfering with its customers, suppliers or partners.
- **Prevalence:** 18/25 (72%), common
- **Applies when:** `facts.company.staff_restrictions` contains `non-solicit-staff` or `non-solicit-customers`
- **Facts:** `facts.company.staff_restrictions`
- **Patterns:**
  - 18/18 cover staff (employees and consultants), during the relationship and a fixed period
    after (months or years); about 8/18 also bar hiring them.
  - 12/18 cover customers, suppliers or partners; 5/18 limit that to those the signer dealt with.
  - 5/18 limit the post-employment bar to soliciting through the company's confidential
    information.
  - 3/18 carve out general job advertisements.
- **Detail:** the people covered by kind; the period as a number of months or years, which the
  filled copies set at 12 or 24 months.
- **Quote:** none
- **Commonly omitted:** a geographic limit on the non-solicit (18/18).

### non-compete: No competing after leaving

- **Covers:** a ban on competing with the company for a time after the relationship ends.
- **Prevalence:** 10/25 (40%), common
- **Applies when:** `facts.company.staff_restrictions` contains `non-compete`
- **Facts:** `facts.company.staff_restrictions`, `facts.company.business_scope`
- **Patterns:**
  - 10/10 set a fixed period after leaving and an area: worldwide (3/10), a state, county radius
    or the company's operating areas (3/10), or wherever the defined business is carried on.
  - 10/10 list the roles barred (owner, employee, consultant, lender) and 5/10 allow a small
    passive stake in a listed company.
  - 3/10 justify it by access to confidential information or goodwill.
  - 1/10 (founder form) binds the founder after selling the technology.
- **Detail:** the competing business by a defined term tied to the company's business; the period
  and area as values; no competitor named.
- **Quote:** none
- **Commonly omitted:** pay during the restricted period (10/10).

### non-disparagement: No disparaging the company

- **Covers:** a ban on disparaging the company, its people or its products.
- **Prevalence:** 5/25 (20%), rare
- **Applies when:** `facts.company.staff_restrictions` contains `non-disparagement`
- **Facts:** `facts.company.staff_restrictions`
- **Patterns:**
  - 5/5 one-way and unlimited in time, covering the company, its group, staff, customers and
    investors.
  - 3/5 carve out testimony, cooperation with government investigations and other protected
    statements.
- **Detail:** one or two sentences; statements by kind.
- **Quote:** none
- **Commonly omitted:** a matching duty on the company (4/5).

### notify-new-employer: Telling later employers

- **Covers:** telling the signer's later employers about the agreement: the company's right to
  notify them, and the signer's duty to show it.
- **Prevalence:** 17/25 (68%), common
- **Applies when:** always
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 17/17 let the company tell a new employer (and in 6/17 anyone the signer works for) about the
    signer's obligations, by a copy of the agreement or otherwise.
  - 2/17 also oblige the signer to show the agreement to a new employer before accepting.
- **Detail:** one sentence; no named employer.
- **Quote:** "In the event that I leave the employ of the Company, I hereby consent to the notification of my new employer of my rights and obligations under this Agreement." (s06)
- **Commonly omitted:** any notice to the signer before the company tells the new employer.

### enforcement: Remedies for breach

- **Covers:** remedies for breach (injunction without bond, legal costs, fixed sums), the
  signer's acknowledgement that the restrictions are reasonable, and court narrowing of terms
  that go too far.
- **Prevalence:** 20/25 (80%), core
- **Applies when:** always
- **Facts:** `facts.company.staff_restrictions`
- **Patterns:**
  - 19/20 call a breach irreparable harm and let the company seek an injunction, without bond in
    most; written one-way for the company in about 14/19.
  - 9/20 have the signer acknowledge that the restrictions are reasonable and needed; 9/20 ask a
    court to narrow an overbroad term rather than strike it.
  - About 6/20 shift legal costs, mostly one-way to the company; 1/20 sets fixed sums for breach.
  - 2/20 extend a covenant by the time it was breached.
- **Detail:** remedies by kind; no amounts, except where a form sets fixed sums.
- **Quote:** "I agree that any threatened or actual violation of this Agreement or any of its terms will constitute immediate and irreparable injury to the Company ..." (s01)
- **Commonly omitted:** remedies for the signer (most are one-way).

### general: Closing clauses

- **Covers:** standard closing clauses: entire agreement, amendment, waiver, severability,
  successors and assignment of the agreement, survival, notices, counterparts, effect of a change
  of role, advice of counsel.
- **Prevalence:** 25/25 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.address`, `facts.company.signatory`
- **Patterns:**
  - Clauses: entire agreement (22/25), amendment in writing (22/25), successors and assignment of
    the agreement, the company free to assign and the signer not (22/25), severability (21/25),
    waiver (18/25), survival after the relationship ends (16/25), counterparts and e-signature
    (16/25), a change of role or pay does not end the agreement (13/25), notices (11/25), advice of
    counsel or voluntary signing (9/25), export of technical data (5/25).
  - Most bundle them under one "General" or "Miscellaneous" heading, one or two sentences each.
- **Detail:** one or two sentences per clause; addresses for notices given only in 4/25.
- **Quote:** "This Agreement may be amended only by a written agreement executed by each of the parties hereto." (s01)
- **Commonly omitted:** a language clause (24/25); third-party beneficiaries (24/25).

### governing-law: Governing law and courts

- **Covers:** the law that governs the agreement and the courts that hear disputes.
- **Prevalence:** 24/25 (96%), core
- **Applies when:** always
- **Facts:** `facts.company.contract_law`, `facts.company.staff_locations`
- **Patterns:**
  - 24/24 name one law, 15/24 excluding its conflict rules; about 20/24 the law of the company's
    home state or country, 2/24 the law of the place where the signer works or lives.
  - 16/24 add consent to the courts of a named place; 4/24 send disputes first to a separate
    arbitration agreement.
- **Detail:** one or two sentences; the law and courts as values.
- **Quote:** none
- **Commonly omitted:** an informal step before court (24/24).

### no-employment-promise: Not an employment contract

- **Covers:** that the agreement is no contract of employment for any period, and leaves the
  terms on which the job can end unchanged.
- **Prevalence:** 13/25 (52%), common
- **Applies when:** `facts.company.ip_signers` contains `employees`
- **Facts:** `facts.company.ip_signers`
- **Patterns:**
  - 13/13 say the agreement promises no employment for any period and gives no right to continued
    employment; 3/13 add that the agreement is not a contract of employment.
  - A change of role or pay that leaves the agreement in force sits in `general` (13/25).
- **Detail:** one or two sentences. How and when the job can end is the employment contract's and
  the law's: a statement of the employment's legal status is the region block's.
- **Quote:** "I agree and understand that nothing in this Agreement shall give me any right to continued employment by Company, ..." (s07)
- **Commonly omitted:** notice periods (13/13).

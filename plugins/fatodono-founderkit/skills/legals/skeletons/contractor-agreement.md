---
doc_id: contractor-agreement
title: Freelancer / Contractor Agreement
kind: document
family: company
sample_languages: [en]
sample_count: 19
saturated: true
scanned: 2026-11-12
format_version: 2
# Samples: 16 SEC EDGAR exhibits in which a company engages an outside individual or firm for
# defined services (4 large, 5 mid, 7 small filers), and 3 standard forms (Common Paper
# Independent Contractor Agreement, Bonterms Professional Services Agreement, the New York City
# model freelance contract). Exhibits whose text carries another relationship's terms were left
# out: a departing executive's separation, transition or continued vesting, or an officer or board
# appointment. A clean engagement of a sitting director was kept (s07, s08). Most EDGAR samples are advisory engagements of small listed companies, so
# several pay in shares; the shares' securities terms are regional content, not root patterns.
---

## Document

- **Purpose:** The agreement under which a company engages an outside individual or firm to
  perform services: what is done and handed over, how it is paid, the contractor's independent
  status, who owns the work, what stays confidential, and how the engagement ends.
- **Shape:**
  - 19/19 one signed agreement; median about 3,000 words (range 1,200–10,400). Small filers run
    shortest (median about 2,100); the three standard forms run 1,200–7,000.
  - 12/19 put the services, and often the fees, in a separate part: an exhibit or schedule (9),
    a cover page that doubles as the statement of work (2), or a fill-in table (1). 7/19 write
    everything in the body.
  - 2/19 are a cover page of deal terms on top of fixed standard terms; 3/19 are a master
    agreement under which statements of work are signed.
  - 17/19 number their sections; 1/19 is a letter agreement countersigned by the contractor.
- **Register:** formal contract drafting in the third person with role names ("Company",
  "Consultant" or "Contractor", "Client", "Provider") in 19/19; capitalised defined terms set in
  the clause that first uses them. 3/19 (two standard forms, one public model) write plainer,
  shorter sentences. 4/19 set some waiver or liability clauses in capitals.
- **Recurring elements:**
  - A preamble naming both parties and the effective date: 19/19.
  - Recitals of the purpose and a consideration line: 11/19.
  - A survival clause listing what outlasts the agreement: 11/19.
  - A closing signature block with name, title and date per party: 19/19.
  - A definitions block: 2/19 (both cover-page standard forms); the rest define inline.
- **Commonly omitted:** acceptance of deliverables (16/19 have none); insurance (15/19); data
  protection (17/19); talks or arbitration before court (14/19).

## Sections

Region-neutral. What one law requires is in the region's block,
`regions/<code>/contractor-agreement.md`, written under the document's regional part
(`formats/region-format.md`). No region block exists yet; `research/contractor-agreement/merge.md`
*Regional content* lists what the US samples carry.

### parties: Parties and background

- **Covers:** who the company and the contractor are, the effective date, the defined role
  names, and why the company is engaging the contractor.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.entity_form`, `facts.company.address`, `facts.contractor.party`, `facts.contractor.term`, `facts.contractor.services`
- **Patterns:**
  - 19/19 open with one paragraph naming both parties and defining short role names; about 11/19
    give each party's legal form and place of registration, about 5/19 an address.
  - 11/19 add recitals: the company's business, the contractor's expertise and the purpose of
    the engagement, ending with a consideration line.
  - 3/19 name the individual who will do the work when the contractor is a firm.
  - 2/19 (standard forms) take names and addresses from cover-page fields; 1/19 has field blocks
    for name, business name, contact person, address, phone and email per party.
- **Detail:** names, legal form and place of registration; the purpose in one or two sentences.
  The company's postal address is written out here, once (`helpers/need-to-know.md`); the notices
  clause and the signature page point to this section. No tax ids or personal details beyond an
  address.
- **Quote:** "Contractor and Company are each referred to as a "Party" and, collectively, as the "Parties"." (s03)
- **Commonly omitted:** the contractor's address (about 14/19 give no address here, leaving it to
  the notices clause or the signature page).

### services: Services and deliverables

- **Covers:** what the contractor will do and hand over, how work is ordered, and when a
  deliverable counts as done.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.contractor.services`, `facts.contractor.party`
- **Patterns:**
  - 12/19 point to an exhibit, schedule, statement of work or cover page for the scope; 7/19
    describe it in the body.
  - About 8/19 keep the scope open: named kinds of work plus whatever the company "reasonably
    requests", "including but not limited to".
  - 3/19 are master agreements: each statement of work binds once both sign and the agreement
    governs them all.
  - 4/19 list deliverables with due dates; 3/19 add an acceptance step (a test period, notice of
    defects, deemed acceptance on silence); 1/19 a client approval loop with revisions.
  - 3/19 name the one person at a firm who must do the work.
  - Exhibits write the scope as a list (about 6/12) or a table of deliverables, due dates and
    completion tests (4/12).
- **Detail:** the kinds of work and, for project work, each deliverable with its due date. No
  hours, tools or methods here (those are `work-arrangements`); no service levels.
- **Quote:** "Consultant shall render services to Client as specified on Schedule 1 attached hereto (the "Services")." (s04)
- **Commonly omitted:** acceptance criteria (16/19); a limit on revision rounds (19/19).

### work-arrangements: How the work is done

- **Covers:** time commitment, place, contact person, reporting, who supplies tools, and what
  the company must provide.
- **Prevalence:** 15/19 (79%), common
- **Applies when:** always
- **Facts:** `facts.contractor.work_arrangements`
- **Patterns:**
  - About 7/15 set the time: hours or days a week, "as needed", or "the time reasonably
    necessary"; none sets a minimum the contractor must work.
  - About 5/15 require progress reports or regular updates; 1/15 weekly, 1/15 after each project
    step; the rest give no cadence.
  - About 4/15 have the company supply information, materials or access the work depends on;
    1/15 lets the contractor flag a missed dependency and move its dates.
  - 3/15 name a contact person or project lead on each side.
  - 2/15 say the contractor supplies its own tools and equipment; 2/15 set a place (on site on
    weekdays, or mutually agreed times and places).
  - 1/15 makes significant decisions subject to an advisory board's approval.
- **Detail:** the expected time in general terms, the contact by role or name, the inputs by
  kind. No working hours set by the company and no supervision of method (that would cut against
  `independent-contractor`).
- **Quote:** none
- **Commonly omitted:** a reporting format; consequences of the company's late inputs (14/15).

### term: Term

- **Covers:** when the agreement starts and ends, and any renewal.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.contractor.term`
- **Patterns:**
  - About 10/19 run for a fixed period to a stated end date; about 6/19 until the services are
    completed or the last statement of work ends; 2/19 month to month; 1/19 from signature with
    no end date.
  - 2/19 renew automatically for one-year periods unless either side gives notice; 4/19 allow
    extension by mutual written agreement.
  - 1/19 makes the agreement apply from the earlier date work began.
  - Usually one or two sentences, often joined with termination under one heading (about 5/19).
- **Detail:** a start date and an end rule. No renewal unless the facts set one.
- **Quote:** none
- **Commonly omitted:** automatic renewal (17/19).

### fees: Fees

- **Covers:** what the contractor is paid and on what basis.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.contractor.fees`
- **Patterns:**
  - Cash bases: a flat monthly retainer (about 8/19), an hourly rate (2/19, and two
    standard forms prompt for a rate), a fixed price for the whole job (2/19), or the fee set in
    each statement of work (3/19).
  - 9/19 pay at least partly in company shares, options or warrants, 4/19 only in equity, vesting
    by month or by accepted deliverable; this is a trait of the listed-company samples.
  - About 5/19 state that the fee is the contractor's whole compensation, with no benefits,
    royalties or other pay.
  - 2/19 cap billable hours (one requires approval above the cap); 1/19 raises the fee on a
    funding event.
  - About 10/19 put the amount in an exhibit or cover page; the body points to it.
- **Detail:** the basis, the amount and currency, any cap. Equity is named by number and class
  only; its plan and securities terms are not described here.
- **Quote:** none
- **Commonly omitted:** a rate review (18/19); a deposit (18/19).

### invoicing-payment: Invoicing and payment

- **Covers:** when the contractor invoices, how fast the company pays, and what happens when it
  is late or disputes an invoice.
- **Prevalence:** 14/19 (74%), common
- **Applies when:** `facts.contractor.fees.basis != equity`
- **Facts:** `facts.contractor.payment_terms`, `facts.contractor.fees`
- **Patterns:**
  - About 8/14 set a payment period in days from the invoice; 4/14 invoice monthly; 3/14 tie
    payment to delivery, a milestone or acceptance.
  - 4/14 charge interest or a late fee on overdue amounts, one capped at the legal maximum.
  - 3/14 let the company withhold only the disputed part of an invoice and pay the rest on time.
  - 1/14 lets the contractor suspend work until paid; 1/14 bars set-off; 1/14 lists what an
    invoice must contain; 1/14 sets an invoicing deadline after the work.
  - Often merged into the fees clause (about 9/14).
- **Detail:** cadence, days to pay, method. No bank details in the agreement.
- **Quote:** "In the event Client does not pay such fees and expenses as specified, Consultant may suspend Services until payment is made." (s04)
- **Commonly omitted:** the payment method (11/14).

### expenses: Expenses

- **Covers:** which of the contractor's expenses the company pays back, and on what conditions.
- **Prevalence:** 17/19 (89%), core
- **Applies when:** always
- **Facts:** `facts.contractor.expenses`
- **Patterns:**
  - 9/17 reimburse only expenses approved in advance; 4/17 need approval above a set amount only;
    1/17 for travel only.
  - About 10/17 require receipts or other proof; about 6/17 apply the company's own expense or
    travel policy.
  - 3/17 reimburse only what a statement of work provides for; 1/17 says no expenses are paid;
    1/17 has the company book and pay travel itself.
  - Travel is the one example named in most; none lists categories beyond it.
- **Detail:** approval rule, threshold, proof. No caps (none sets one).
- **Quote:** "Company will reimburse Contractor for all pre-approved, reasonable and documented out-of-pocket expenses" (s03)
- **Commonly omitted:** a cap on total expenses (17/17).

### scope-changes: Changes to the scope

- **Covers:** how the parties change or add to the work.
- **Prevalence:** 6/19 (32%), rare
- **Applies when:** `facts.contractor.services.structure != ongoing`
- **Facts:** `facts.contractor.services`, `facts.contractor.fees`
- **Patterns:**
  - 2/6 require a written change agreed by both; 2/6 have the contractor estimate the cost
    first, the company then accepting or withdrawing the request.
  - 1/6 sets a change-request procedure: a request by notice, a meeting within set days, a
    written change order before work starts.
  - 1/6 routes out-of-scope work to a separate addendum.
- **Detail:** who may ask, the estimate, the written change. No pricing of changes in advance.
- **Quote:** none
- **Commonly omitted:** what happens to dates when the scope changes (5/6).

### independent-contractor: Independent contractor status

- **Covers:** that the contractor is not an employee, partner or agent, gets no employee
  benefits, controls how it works, and cannot bind the company.
- **Prevalence:** 17/19 (89%), core
- **Applies when:** always
- **Facts:** `facts.contractor.party`, `facts.contractor.work_arrangements`
- **Patterns:**
  - 13/17 deny the contractor any authority to bind the company; about 8/17 exclude it from
    employee benefits, several listing them (health, pension, holiday, sick pay); 1/17 instead
    extends the company's executive benefits to the consultant.
  - About 5/17 give the contractor control over method, hours and its own staff.
  - About 4/17 make the contractor responsible for paying its own staff.
  - 3/17 deal with a challenge to the contractor's status: the contractor indemnifies the
    company's resulting tax costs (1), the company indemnifies the contractor (1), or benefits
    stay excluded even if the contractor is reclassified (1).
  - 2/17 state the status in one sentence only.
- **Detail:** the status and its consequences in general terms. No test from any country's
  classification rules (regional content).
- **Quote:** "Consultant shall not have any authority to enter into contracts or binding commitments in the name or on behalf of the Company." (s23)
- **Commonly omitted:** the contractor's right to send someone else in its place (17/17).

### other-work: Other work and conflicts

- **Covers:** whether the contractor may work for others, limits on competing work during the
  engagement, and conflicts with the contractor's other duties.
- **Prevalence:** 12/19 (63%), common
- **Applies when:** always
- **Facts:** `facts.contractor.restrictions`
- **Patterns:**
  - About 7/12 have the contractor warrant, and promise during the term, that it has no
    obligation that conflicts with this one (a former employer or a university are the examples).
  - About 5/12 say the contractor may work for others; 2/12 say the company may use other
    providers too.
  - 3/12 bar competing work during the term (for competitors, or substantially similar
    services); 1/12 bars only competitors.
  - About 4/12 add that the contractor will not bring others' confidential information into the
    work.
  - Often a warranty inside the representations (about 5/12).
- **Detail:** the freedom and the conflict rule in general terms; competitors by description, not
  by name.
- **Quote:** "Consultant acknowledges and agrees during the term of the Agreement not to accept work or enter into an agreement or accept an obligation, which is inconsistent or incompatible with Consultant's obligations hereunder." (s01)
- **Commonly omitted:** a definition of a competitor (11/12).

### taxes: Taxes

- **Covers:** who pays which taxes on the fees.
- **Prevalence:** 13/19 (68%), common
- **Applies when:** always
- **Facts:** `facts.contractor.party`
- **Patterns:**
  - 13/13 make the contractor pay its own income and social taxes.
  - 3/13 have the contractor indemnify the company for taxes assessed on its fees.
  - 2/13 say fees exclude sales, use or value-added taxes, which the company bears.
  - Often merged into the status clause (7/13).
- **Detail:** responsibility in general terms. No tax rates, registrations or form names, and no
  statement on whether the company withholds tax from the fees: each country's tax law decides
  that (regional content).
- **Quote:** none
- **Commonly omitted:** indirect taxes on the fees (11/13).

### termination: Termination

- **Covers:** how either side ends the engagement early, what is paid, what is handed over, and
  what survives.
- **Prevalence:** 17/19 (89%), core
- **Applies when:** always
- **Facts:** `facts.contractor.termination`, `facts.contractor.term`
- **Patterns:**
  - About 10/17 let either party end it for convenience on written notice (one with no notice
    period); 3/17 only the company; 1/17 only the contractor; 1/17 only by mutual agreement.
  - 11/17 allow termination for breach: 5/17 after a cure period in days, 6/17 at once for
    listed causes (dishonesty, material breach, insolvency, refusal to perform).
  - About 9/17 pay fees earned and approved expenses up to the end; 1/17 refunds prepaid fees.
  - 3/17 require delivery of all work in progress; 2/17 end the agreement on the contractor's
    death or disability.
  - 11/17 list the clauses that survive, by number and heading in most; 1/17 says everything
    survives.
- **Detail:** who may end it, notice in days, cure period, what is paid. No fees or penalties for
  ending early.
- **Quote:** "Neither Party will be liable to the other for terminating this Agreement in accordance with its Terms." (s03)
- **Commonly omitted:** a transition or handover period (16/17).

### warranties: Representations and warranties

- **Covers:** what each side promises about itself and the work: authority, standard of work,
  non-infringement, and what is disclaimed.
- **Prevalence:** 12/19 (63%), common
- **Applies when:** always
- **Facts:** `facts.contractor.services`
- **Patterns:**
  - About 7/12 have each side warrant its authority to sign and that the agreement binds it.
  - About 6/12 have the contractor warrant professional, workmanlike work to industry standards;
    2/12 add that deliverables will conform to the specifications, with re-performance as the
    remedy (1).
  - 3/12 warrant non-infringement of others' rights; 1/12 no harmful code.
  - 3/12 disclaim other warranties or guarantee no result (two written for the contractor).
- **Detail:** the promises in one sentence each. No warranty period except where the facts set
  acceptance.
- **Quote:** none
- **Commonly omitted:** a warranty period (11/12).

### ip-ownership: Ownership of the work

- **Covers:** who owns what the contractor creates, how ownership passes, and the contractor's
  help to secure it.
- **Prevalence:** 11/19 (58%), common
- **Applies when:** `facts.contractor.ip_terms.placement == in-agreement`
- **Facts:** `facts.contractor.ip_terms`
- **Patterns:**
  - About 6/11 assign all rights to the company in present words ("hereby assigns"), covering
    work made during and for the engagement; 2/11 say only that the work is the company's
    property, with no assignment.
  - About 5/11 require the contractor's help to register and enforce the rights, during and after
    the term; 4/11 back it with a power of attorney.
  - 4/11 require prompt disclosure of inventions and records of the work; 3/11 waive moral rights
    where they cannot be assigned.
  - 2/11 (forms) let the parties choose assignment or a licence per deliverable, one passing
    ownership only on final payment; 1/11 makes the contractor's staff sign over their rights to
    it first.
  - 0/19 put the contractor's IP terms in a separate assignment document; the 8/19 without an
    IP clause are advisory engagements with no deliverable.
- **Detail:** work product defined by a list of kinds (inventions, code, designs, documents,
  data) in about 7/11, tied to the engagement. No list of the specific deliverables, no
  registration numbers.
- **Quote:** none
- **Commonly omitted:** what the contractor keeps (see `contractor-materials`, 4/19); payment
  for the assignment beyond the fees (11/11).

### contractor-materials: The contractor's own materials

- **Covers:** pre-existing materials, tools and third-party or open-source components the
  contractor builds into the deliverables, and the licence the company gets to them.
- **Prevalence:** 4/19 (21%), rare
- **Applies when:** `facts.contractor.ip_terms.background_materials == true` or `facts.contractor.ip_terms.third_party_components == true`
- **Facts:** `facts.contractor.ip_terms`
- **Patterns:**
  - 3/4 let the contractor keep what it owned before and give the company a non-exclusive,
    royalty-free, perpetual, worldwide licence to use it as part of the deliverables; 1/4 asks
    for notice before such materials are built in.
  - 1/4 allows only third-party materials listed in the statement of work, the contractor
    securing the licences, and requires every open-source component to be listed with its
    licence, with copyleft code only if the statement of work allows it.
  - Placed right after the ownership clause in 4/4.
- **Detail:** the kinds of materials and the licence's scope. No component list in the body
  (the statement of work lists them where any are named).
- **Quote:** none
- **Commonly omitted:** removal of a component whose licence fails (4/4).

### prior-work: Work done before signing

- **Covers:** work the contractor did before the agreement and how the agreement treats it.
- **Prevalence:** 3/19 (16%), rare
- **Applies when:** `facts.contractor.prior_work.started_before == true`
- **Facts:** `facts.contractor.prior_work`
- **Patterns:**
  - 1/3 extends the confidentiality and ownership terms to an earlier period of work, named as a
    defined term.
  - 1/3 credits fees already paid against the new agreement; 1/3 has the contractor confirm it
    has been paid in full to a date.
  - 1/3 settles earlier unpaid invoices with mutual releases for the past work.
- **Detail:** the earlier period by its start date; which clauses reach back.
- **Quote:** none
- **Commonly omitted:** a list of what was delivered before signing (3/3).

### compliance: Compliance with laws and policies

- **Covers:** the laws, licences, company policies and site rules the contractor must follow.
- **Prevalence:** 11/19 (58%), common
- **Applies when:** always
- **Facts:** `facts.contractor.work_arrangements`, `facts.contractor.data_access`
- **Patterns:**
  - About 6/11 require compliance with applicable laws, most in one sentence or a warranty.
  - About 5/11 require the company's policies or site and safety rules when on its premises or
    systems; 1/11 limits system access to what a statement of work authorises.
  - 2/11 require the contractor to hold its own licences and permits; 1/11 that its staff may
    lawfully work; 1/11 bans bribery in both directions.
- **Detail:** the duty in general terms; policies by name only. No law named in the root.
- **Quote:** none
- **Commonly omitted:** which policies apply (9/11 say "the company's policies" only).

### confidentiality: Confidentiality

- **Covers:** what information is confidential, what the contractor may do with it, the
  exceptions, compelled disclosure, and how long the duty lasts.
- **Prevalence:** 18/19 (95%), core
- **Applies when:** always
- **Facts:** `facts.contractor.confidentiality`
- **Patterns:**
  - About 13/18 protect only the company's information; 4/18 are mutual; 1/18 is only an
    acknowledgement of access.
  - About 8/18 define it by a long list of categories (finances, customers, products, code,
    know-how), stating it need not be marked; 2/18 cover only what is marked or identified.
  - About 7/18 list the usual exclusions (already known, public, received from a third party,
    independently developed).
  - About 8/18 allow disclosure the law compels, after prompt notice so the owner can object.
  - Duration: about 4/18 a set number of years after the end, with trade secrets for as long as
    they stay secret; the rest without a stated end.
  - About 4/18 add that a breach causes irreparable harm and allows an injunction.
  - 2/18 keep the agreement's own terms confidential.
- **Detail:** information by category; use only to perform the services; disclosure only to
  staff who need it and are bound alike. No list of the company's actual secrets.
- **Quote:** "Confidential Information need not be novel, unique, patentable, copyrightable or constitute a trade secret in order to be designated Confidential Information." (s03)
- **Commonly omitted:** a standard of care beyond "reasonable" (about 15/18).

### return-of-materials: Return of materials

- **Covers:** returning or destroying the company's property and materials at the end or on
  request.
- **Prevalence:** 10/19 (53%), common
- **Applies when:** always
- **Facts:** `facts.contractor.work_arrangements`, `facts.contractor.data_access`
- **Patterns:**
  - 10/10 require delivery on termination or earlier on request; about 4/10 "immediately" or
    "promptly", with a set number of days in 1/10.
  - About 5/10 list the kinds (documents, files, data, devices, copies) and bar keeping copies;
    3/10 allow destruction instead of return, 1/10 with a written certificate.
  - About 4/10 sit inside the termination or confidentiality clause.
- **Detail:** kinds of materials, return or destruction. No inventory.
- **Quote:** none
- **Commonly omitted:** copies the law requires the contractor to keep (9/10).

### non-solicitation: Non-solicitation

- **Covers:** limits during and after the engagement on soliciting the company's staff or
  customers.
- **Prevalence:** 6/19 (32%), rare
- **Applies when:** `facts.contractor.restrictions` contains `non-solicit-staff` or `non-solicit-customers`
- **Facts:** `facts.contractor.restrictions`
- **Patterns:**
  - 6/6 bar soliciting or hiring the company's employees and contractors, for the term plus a set
    number of months or years.
  - 3/6 also bar soliciting or interfering with customers or suppliers, one limited to named
    lines of business.
  - 2/6 add that the parties accept the limits as reasonable and that a court may narrow them;
    1/6 extends the period by the time of a breach.
  - Usually placed after confidentiality (5/6).
- **Detail:** who is covered and for how long. No list of names.
- **Quote:** none
- **Commonly omitted:** a carve-out for general job advertisements (5/6).

### non-disparagement: Non-disparagement

- **Covers:** promises not to speak badly of the other party.
- **Prevalence:** 2/19 (11%), rare
- **Applies when:** `facts.contractor.restrictions` contains `non-disparagement`
- **Facts:** `facts.contractor.restrictions`
- **Patterns:**
  - 1/2 mutual for a set number of years; 1/2 binds only the consultant and its firm, with a
    remedy.
- **Detail:** one or two sentences.
- **Quote:** none
- **Commonly omitted:** a carve-out for truthful statements the law requires (2/2).

### indemnity: Indemnities

- **Covers:** which side covers the other's losses from third-party claims, and the procedure.
- **Prevalence:** 15/19 (79%), common
- **Applies when:** always
- **Facts:** `facts.contractor.liability`
- **Patterns:**
  - About 8/15 have the contractor indemnify the company: for its breach, negligence or
    misconduct, for infringement by its deliverables (3/15), or for taxes (2/15).
  - About 6/15 have the company indemnify the contractor for claims arising from the services,
    except its own negligence or misconduct; these are the contractor's own paper.
  - About 5/15 are mutual and fault-based.
  - About 5/15 set a procedure: prompt notice, control of the defence, no settlement without
    consent.
  - 1/15 gives the contractor's options on an infringement claim (secure the right, modify,
    replace or refund).
- **Detail:** who covers what, by kind of claim. No amounts.
- **Quote:** none
- **Commonly omitted:** a link to the liability cap (12/15 do not say whether the indemnity is
  capped).

### insurance: Insurance

- **Covers:** insurance either side must carry.
- **Prevalence:** 4/19 (21%), rare
- **Applies when:** `facts.contractor.insurance != none`
- **Facts:** `facts.contractor.insurance`
- **Patterns:**
  - 3/4 have the contractor carry its own insurance (professional liability, general
    liability, cover for its own workers), amounts set in the cover page or statement of work (1/4).
  - 1/4 has the company carry general liability cover naming the contractor.
  - 1/4 says the company insures nothing for the contractor.
- **Detail:** types of cover; amounts only where the facts give them.
- **Quote:** none
- **Commonly omitted:** proof of cover (4/4).

### data-protection: Personal data and security

- **Covers:** how the contractor handles personal data and secures the company's systems.
- **Prevalence:** 2/19 (11%), rare
- **Applies when:** `facts.contractor.data_access == personal-data`
- **Facts:** `facts.contractor.data_access`, `facts.processors.list`
- **Patterns:**
  - 1/2 requires the contractor to process personal data only for the services and to keep
    adequate staff, security and operational measures, with evidence on request.
  - 1/2 requires a separate data agreement.
- **Detail:** the duty in general terms; security measures by kind. No systems or hosts named.
- **Quote:** none
- **Commonly omitted:** breach notification (2/2).

### publicity: Publicity and portfolio use

- **Covers:** use of the other party's name, logo or the work in publicity, a portfolio or a
  publication.
- **Prevalence:** 4/19 (21%), rare
- **Applies when:** `facts.contractor.portfolio_use != allowed`
- **Facts:** `facts.contractor.portfolio_use`
- **Patterns:**
  - 2/4 bar using the other's name or logo without prior written approval, both ways.
  - 1/4 requires approval before the contractor presents or publishes anything about the work.
  - 1/4 lets the company use the contractor's name and likeness in its advertising.
- **Detail:** one or two sentences, both directions named.
- **Quote:** "Neither Party will use the other Party's name, logo, trademarks, or service marks in any advertising, publicity releases, or any other materials without that Party's prior written approval." (s04)
- **Commonly omitted:** when the contractor may show the work in a portfolio (4/4).

### subcontracting: Subcontracting and assignment

- **Covers:** whether the contractor may hand the work or the agreement to someone else.
- **Prevalence:** 13/19 (68%), common
- **Applies when:** always
- **Facts:** `facts.contractor.subcontracting`
- **Patterns:**
  - About 11/13 require the company's prior written consent to subcontract, delegate or assign;
    1/13 bans it outright, calling the services personal.
  - 3/13 keep the contractor responsible for subcontractors and require it to bind them to the
    same terms.
  - 2/13 let the contractor bring in assistants or extra resources freely, one billing them at
    cost.
  - About 8/13 sit in the closing clauses with assignment of the agreement.
- **Detail:** the consent rule and the contractor's responsibility. No named subcontractors.
- **Quote:** "This Agreement requires the personal services of Consultant and may not be assigned by him without the prior written consent of the Company." (s01)
- **Commonly omitted:** the company's right to assign (about 7/13 say nothing on it).

### liability: Limitation of liability

- **Covers:** excluded damages and caps on liability.
- **Prevalence:** 11/19 (58%), common
- **Applies when:** always
- **Facts:** `facts.contractor.liability`
- **Patterns:**
  - About 6/11 exclude indirect, consequential and lost-profit damages, mostly both ways.
  - About 7/11 cap liability, most at the fees paid under the agreement or in a recent period;
    1/11 at a sum set on the cover page; 1/11 either party's at the agreement's value.
  - Whom the limits protect follows whose paper it is: the contractor only (5/11), the company
    only (2/11), both (4/11).
  - 2/11 carve out fraud, gross negligence and wilful misconduct; 1/11 carves out
    confidentiality and indemnity claims.
  - 1/11 limits the contractor's liability for good-faith advice altogether.
- **Detail:** the exclusion and the cap basis. No amounts in the body unless the facts set a
  fixed sum.
- **Quote:** "Consultant shall bear no liability to Client for loss or damage in connection with advice or assistance given in good faith performance of the Services." (s04)
- **Commonly omitted:** carve-outs from the cap (8/11).

### disputes: Disputes

- **Covers:** how disputes are handled before or instead of court: talks, arbitration,
  injunctions and costs.
- **Prevalence:** 15/19 (79%), common
- **Applies when:** always
- **Facts:** `facts.company.contract_law`
- **Patterns:**
  - 8/15 let the company seek an injunction or specific performance for a breach of
    confidentiality or the covenants, without proving money damages; most one-way.
  - About 7/15 award reasonable attorneys' fees to the prevailing party.
  - 4/15 send disputes to binding arbitration under a named institution's rules; 3/15 require
    good-faith talks or an escalation between named leads first.
  - 1/15 (a public model) only warns, in a note, about private arbitration clauses.
- **Detail:** the steps in order. No institution named unless the facts choose arbitration.
- **Quote:** none
- **Commonly omitted:** mediation (15/15).

### governing-law: Governing law and courts

- **Covers:** the law that governs the agreement and the courts that hear disputes.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.contract_law`, `facts.company.country`
- **Patterns:**
  - 17/19 name one law, most excluding its conflict-of-law rules; the other 2/19 (cover-page
    forms) leave it blank.
  - About 12/19 name exclusive courts in one city or county; about 7/19 name the law only.
  - Usually one or two sentences; about 5/19 inside the closing clauses.
- **Detail:** one law and one place.
- **Quote:** none
- **Commonly omitted:** the reason for the choice (19/19).

### general: General terms

- **Covers:** closing clauses: entire agreement, amendment, waiver, severability, counterparts
  and electronic signatures, notices, assignment of the agreement, successors, headings and
  interpretation, force majeure.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.contractor.party`, `facts.company.address`, `facts.company.contact_email`, `facts.contractor.confidentiality`
- **Patterns:**
  - Entire agreement and amendment in writing (about 18/19), severability (about 16/19),
    counterparts with electronic signatures in about half, notices (about 13/19), waiver (about
    12/19), headings and interpretation (about 9/19), successors and assigns (about 9/19), no
    third-party beneficiaries (4/19), force majeure (3/19).
  - Notices: written, by hand, courier, mail or email, deemed received after set days or hours,
    addresses in the preamble, a schedule or the signature page. The company's address is in
    `parties`; the notices clause points to it.
  - 2/19 have each party acknowledge it read the agreement and could take legal advice; 2/19 bar
    reading ambiguities against the drafter.
  - About 3/19 name other agreements that stay in force or win on conflict (a statement of work
    for its own services, a separate agreement).
  - Usually one heading with lettered or numbered clauses (about 12/19).
- **Detail:** one or two sentences per clause; notice addresses by reference.
- **Quote:** "The headings of this Agreement are for convenience of reference only" (s03)
- **Commonly omitted:** a language clause (19/19).

### signatures: Signatures

- **Covers:** each party's execution of the agreement.
- **Prevalence:** 19/19 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.signatory`, `facts.contractor.party`
- **Patterns:**
  - 19/19 close with a block per party: name, signature, and for an entity the signer's name and
    title; about 12/19 add a date line.
  - 13/19 open it with a one-line "in witness whereof" sentence.
  - About 4/19 sign exhibits or statements of work separately; 1/19 asks for initials on every
    page.
- **Detail:** names and titles; no signatures' images or personal data.
- **Quote:** "IN WITNESS WHEREOF, the Parties hereto have entered into this Agreement as of the Effective Date noted above." (s04)
- **Commonly omitted:** witnesses (19/19).

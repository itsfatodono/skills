---
doc_id: shareholders-agreement
title: Founders' / Shareholders' Agreement
kind: document
family: company
sample_languages: [en]
sample_count: 29
saturated: true
scanned: 2026-11-12
format_version: 2
---

## Document

- **Purpose:** The contract the founders (and, once they join, the other shareholders) of one
  private company sign about owning it together: who holds what, how the company is run and
  decisions are taken, what founders owe it, how shares may be sold or must be given up, and how
  the agreement ends.
- **Shape:**
  - 29/29 one contract with numbered articles or sections; 8/29 open with a table of contents.
  - 28/29 open with recitals; 23/29 have a definitions block (18 of them at the start, the rest
    near the end or in a schedule).
  - 22/29 end with schedules or exhibits: the holders' list, a joinder or deed-of-adherence form,
    reserved-matter lists, the articles.
  - Median about 8,300 words (490 to 23,600). Owner-level samples about 6,100, investor-stage
    about 13,000; the one-page pre-incorporation form (s32) is 490.
- **Register:** formal contract drafting in the third person with defined labels ("the
  Founders", "the Company", "the Investors"); long single-sentence clauses; numbers of days,
  percentages and thresholds written as figures or left as blanks in the models. 1/29 (s32) is
  plain and short.
- **Recurring elements:**
  - A signature block for every party: 29/29; executed as a deed: 3/29.
  - The company as a party: 28/29.
  - A holders' list or cap table as a schedule: 18/29.
  - A joinder or deed-of-adherence form for later holders: 17/29.
  - References to the articles or charter, which the agreement overrides between the parties:
    16/29.
  - Companion documents named (articles, employment or service contracts, IP assignment, option
    plan, investment agreement): 22/29.
- **Commonly omitted:** founder vesting (26/29), founders' roles and time (25/29), a deadlock
  mechanism (26/29), an IP clause (20/29), a table of contents (21/29), plain-language summaries
  (29/29).

## Sections

Region-neutral. What one law requires (securities legends, appraisal waivers, statutory
pre-emption, notarial transfers, tax elections, community property) is in the region's block,
`regions/<code>/shareholders-agreement.md`, written under the document's regional part
(`formats/region-format.md`).

Founder-stage texts are rare in public, so the samples mix 16 agreements among founders and other
few owners (founders, early holders, two- or three-owner joint companies; "owner" below) with 13
investor-stage agreements of venture-backed private companies ("vc" below). 24 were filed by
companies with the SEC (all signed while the company was private); 5 are model forms (SVCA, Seedcamp,
StartupTools, NVCA, UK Private Capital), under the one-in-four cap. The skeleton is for the
founders' agreement; where owner and vc samples split, *Patterns* gives both counts. US
investor-stage practice moves vesting, IP and founder roles into separate documents, so those
sections are rarer here than in a founders' agreement; their *Applies when* includes them when
the founders' facts call for them.

### parties: Parties and background

- **Covers:** who signs and in what capacity (each founder, the company, other holders), the date,
  the recitals (the company, its business and capital, why the agreement is made).
- **Prevalence:** 29/29 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.entity_form`, `facts.company.address`, `facts.company.founders`, `facts.company.business_scope`
- **Patterns:**
  - 29/29 name the parties in a preamble; 28/29 make the company a party.
  - 22/29 list the holders in a schedule or signature pages rather than in the preamble.
  - 28/29 add recitals: the company's form and capital, the founders' holdings, the purpose of
    the agreement; 13/29 call the founders "Founders" as a defined group.
  - 8/29 add a clause on the company's business, plan or budget (name, purpose, the business
    plan the money is tied to, the financial year).
  - 10/29 replace an earlier shareholders' agreement and say so in the recitals.
- **Detail:** the company by legal name, form, place of registration and registered office; each
  founder by full name and address, or by a pointer to the schedule. The business in one sentence
  (8/29); none describe the product in detail.
- **Quote:** "The Company is a private company limited by shares." (s31)
- **Commonly omitted:** the founders' history together; the reason for the share split.

### definitions: Definitions and interpretation

- **Covers:** the defined terms and the rules for reading the agreement.
- **Prevalence:** 23/29 (79%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.founders`
- **Patterns:**
  - 18/23 give an alphabetical list or block; 6/23 define terms in context and add an index.
  - 18/23 put it first; 5/23 near the end or in a schedule.
  - 12/23 add interpretation rules (headings, gender and number, "including", days).
  - Key terms across samples: Transfer, Permitted Transferee, Affiliate, Sale of the Company,
    IPO or Listing, Good and Bad Leaver; the founders' model defines about 60 terms, the
    one-page form three.
- **Detail:** the terms the agreement uses, with "Transfer" defined widely (any sale, gift,
  pledge or grant of an interest) in most; no defined term that the text never uses.
- **Quote:** "'Shares' means, with respect to each Shareholder, all shares of capital stock of the Company now owned or hereafter acquired by such Shareholder." (s03)
- **Commonly omitted:** plain-language explanations of the terms.

### capitalisation: Shareholdings

- **Covers:** who holds what: the share split among founders, the share classes and what they
  carry, other holders, what each paid, the employee option pool.
- **Prevalence:** 21/29 (72%), common
- **Applies when:** always
- **Facts:** `facts.company.share_structure`, `facts.company.founders`
- **Patterns:**
  - 13/16 owner samples state the holdings; 8/13 vc samples (the rest leave them to the
    charter and the investment agreement).
  - 18/21 put the holdings in a table or list in a schedule; 9/21 state them only there.
  - 13/21 give each holder's percentage or the split (2/21 an equal split by default).
  - 12/21 name share classes; 5/21 set class rights in the agreement (preferred dividends,
    liquidation preference, anti-dilution, conversion; 4 of them vc), the rest in the charter.
  - 8/21 cover options, warrants or an employee pool; 1/21 says the pool dilutes all founders
    alike.
  - 9/21 state what each holder paid.
- **Detail:** each holder's name, class and number of shares or percentage in a table; the
  price paid per holder. Class rights in a sentence each, or a pointer to the charter. No
  valuation of the company.
- **Quote:** "Upon formation of the Start-Up Company, the entire issued share ownership of the Start-Up Company will be divided equally among the Collaborators." (s32)
- **Commonly omitted:** how the split was decided; what happens to the split when a founder
  joins later.

### board: Board of directors

- **Covers:** board size, who appoints and removes each director, vacancies, observers, the
  chair, directors' pay, and who appoints the officers or managing directors.
- **Prevalence:** 24/29 (83%), core
- **Applies when:** always
- **Facts:** `facts.company.board`, `facts.company.founders`, `facts.company.share_structure`
- **Patterns:**
  - 18/24 fix the board size; 18/24 let the holder who appoints a director remove and replace
    them; 10/24 cover vacancies.
  - 4/24 give each founder one seat while the founder holds shares (4 owner-level samples);
    investor-stage texts split seats among investors, common holders and the chief executive.
  - Most bind every holder to vote its shares for the designated directors (see `voting`).
  - 8/24 also say who appoints the officers, chief executive or managing directors; 5/24 deal
    with a chair or casting vote.
  - 4/24 give an investor an observer; 2/24 mirror the board in subsidiaries.
  - 21/24 write it as prose; 7/24 list the seats; 2/24 put it in a schedule table.
- **Detail:** the number of seats and who fills each, by role or holder group; removal and
  vacancy rules in a sentence each. 6/24 name the first directors; the rest set seats by role or
  holder group only.
- **Quote:** "… may remove its respective designated director at any time and from time to time, with or without cause …" (s02)
- **Commonly omitted:** meeting rules (see `decisions`); directors' duties; pay (3/24 cover it).

### decisions: How decisions are taken

- **Covers:** how the board and the shareholders decide (meetings, quorum, majorities, written
  resolutions), and the decisions that need every founder's or a named holder's consent.
- **Prevalence:** 14/29 (48%), common
- **Applies when:** always
- **Facts:** `facts.company.decision_rules`, `facts.company.board`
- **Patterns:**
  - 10/14 list reserved matters (lettered or numbered lists of 6–20 items: new shares, changes to
    the articles, sale or merger, borrowing or spending above a limit, new businesses, related-party
    deals, the budget, senior hires and pay, dividends, winding up).
  - Who holds the veto: the founders together in 2/14 (the founders' models), a supermajority of
    holders in about 5/14, an investor majority or investor director in about 6/14.
  - 6/14 set board or shareholder quorums; 5/14 tie decisions to an approved budget or plan.
  - 2/14 require unanimity for listed matters; the rest a fixed supermajority.
  - 1/14 leaves the list blank for the founders to fill in.
- **Detail:** the reserved matters by kind, with money thresholds as figures or blanks; the
  majority as a fraction or percentage. No list of current projects or budget figures.
- **Quote:** none
- **Commonly omitted:** written resolutions and remote meetings (1/14); what happens when a
  reserved matter is refused (see `deadlock`).

### voting: Voting undertakings

- **Covers:** the holders' promise to vote their shares (and have their directors act) so the
  agreement takes effect, and the proxies that enforce it.
- **Prevalence:** 16/29 (55%), common
- **Applies when:** always
- **Facts:** `facts.company.board`, `facts.company.decision_rules`
- **Patterns:**
  - 7/16 owner, 9/13 vc.
  - About 10/16 bind every holder to vote all shares, now held or later acquired, to give effect
    to the board and drag-along clauses; 6/16 add a general duty to do everything needed.
  - 7/16 back it with a proxy to a named person if a holder fails to vote; 5/16 make it
    irrevocable for the agreement's term.
  - 1/16 says expressly that the holders make no voting arrangement among themselves.
- **Detail:** the matters the vote covers and the proxy holder by role; no list of past votes.
- **Quote:** "The Parties shall exercise all voting and other rights and powers available to them so as to give effect to the provisions of this Agreement, to the fullest extent possible under law." (s08)
- **Commonly omitted:** how votes are cast at a meeting; voting by founders' holding companies.

### deadlock: Deadlock

- **Covers:** what counts as a deadlock among the founders or the board, and how it is escalated
  and broken.
- **Prevalence:** 3/29 (10%), rare
- **Applies when:** `facts.company.decision_rules.deadlock != []`
- **Facts:** `facts.company.decision_rules`, `facts.company.founders`
- **Patterns:**
  - 1/3 (the founders' model) defines a deadlock as no quorum or the same resolution failing at a
    set number of meetings, then a deadlock notice, a founders' meeting with one vote each, and,
    failing that, a founders' choice between winding up and a buy-sell in which any founder names
    a price for all the others' shares and the others must sell or buy at it.
  - 1/3 sends a tied management board to the supervisory board and a tied supervisory board to
    the shareholders.
  - 1/3 runs the company on last year's budget when the board cannot agree a new one.
- **Detail:** the trigger as a count of failed meetings, the notice periods in days, the order of
  steps; the buy-sell price is set by the offering founder, not a formula.
- **Quote:** "For the avoidance of doubt, a Deadlock Resolution Notice once issued may not be withdrawn." (s31)
- **Commonly omitted:** mediation (none provide for it; s31's drafting note suggests considering
  it).

### founder-roles: Founders' roles and commitment

- **Covers:** what each founder does for the company: role, time, whether employed or engaged as
  a contractor, and pay.
- **Prevalence:** 4/29 (14%), rare
- **Applies when:** `facts.company.founder_commitment` has a founder whose engagement is not `none`
- **Facts:** `facts.company.founders`, `facts.company.founder_commitment`
- **Patterns:**
  - 4/16 owner, 0/13 vc.
  - 2/4 (the founders' models) set a commitment duty: best efforts (1/4) or all business time
    while employed (1/4). 1/4 puts each founder's role in a schedule and requires a separate
    employment or service contract within a set period.
  - 2/4 (joint companies) set each owner's operational duties or a working holder's salary, which
    only all holders may change.
- **Detail:** each founder's role and time commitment; whether employee or contractor as a
  checkbox in 1/4. Pay: fixed in the agreement 2/4 (the joint companies), left to the board 1/4,
  not mentioned 1/4.
- **Quote:** none
- **Commonly omitted:** what happens if a founder cuts their time (the leaver clause covers it).

### funding: Funding and distributions

- **Covers:** what the founders put in at the start (subscriptions, loans, guarantees), whether
  anyone must fund the company later, and how profits are paid out.
- **Prevalence:** 11/29 (38%), rare
- **Applies when:** `facts.company.funding_terms.initial != []`, or
  `facts.company.funding_terms.further_funding != none`, or
  `facts.company.funding_terms.dividend_policy != none`
- **Facts:** `facts.company.funding_terms`, `facts.company.share_structure`
- **Patterns:**
  - 7/16 owner, 4/13 vc.
  - 3/11 state that no holder must fund the company, lend or guarantee unless it agrees in
    writing.
  - 6/11 set the initial funding or contributions; 5/11 cover shareholder loans and their
    repayment; 4/11 cover personal guarantees.
  - 7/11 set a dividend or distribution policy (only with a set majority, a minimum payout, or a
    waterfall that repays loans first).
  - 2/11 tie the use of the money raised to a business plan.
- **Detail:** amounts and dates where the agreement fixes a funding round; otherwise the rule
  only. Loan terms left to a separate loan agreement in most.
- **Quote:** none
- **Commonly omitted:** what happens if a founder cannot fund their share of a call.

### transfer-restrictions: Restrictions on transfer

- **Covers:** the general limits on selling, giving or pledging shares: consent, lock-in, indirect
  transfers, transfers in breach, notices on certificates.
- **Prevalence:** 26/29 (90%), core
- **Applies when:** always
- **Facts:** `facts.company.share_transfer_rules`
- **Patterns:**
  - 26/29 ban any transfer except as the agreement allows, usually as the first clause of the
    transfer article.
  - 14/26 extend the ban to pledges and other encumbrances; 6/26 to indirect transfers (a change
    of control of a founder's holding company).
  - 16/26 need board or holder consent; 4/26 add a lock-in period (on founder shares in 1/4, on
    investors' or other holders' shares in the rest); 4/26 ban sales to competitors.
  - 13/26 make a transfer in breach void, or bar the company from registering it.
  - 16/26, all of them US or US-style texts with share certificates, put a legend on the
    certificates referring to the agreement; the others rely on the void-transfer and
    register rules above.
  - 3/26 set one closing procedure for every sale under the agreement (deliveries, payment,
    power of attorney).
- **Detail:** the kinds of transfer caught and the consent needed; the lock-in as a number of
  months. No list of current pledges.
- **Quote:** "Any attempt to transfer Shares or any rights therein in violation of the preceding sentence shall be null and void ab initio …" (s03)
- **Commonly omitted:** transfers of economic interest only (1/26).

### permitted-transfers: Permitted transfers

- **Covers:** transfers allowed without the restrictions (to family, trusts, holding companies,
  affiliates) and their conditions.
- **Prevalence:** 20/29 (69%), common
- **Applies when:** `facts.company.share_transfer_rules.permitted_transferees != []`
- **Facts:** `facts.company.share_transfer_rules`
- **Patterns:**
  - 13/16 owner, 7/13 vc.
  - 12/20 allow transfers to family; 11/20 to family trusts or estate planning; 11/20 to
    affiliates; 7/20 to the holder's own holding company.
  - 14/20 require the transferee to sign the agreement first.
  - 1/20 makes the shares go back if the transferee stops qualifying; 1/20 keeps the original
    founder bound.
- **Detail:** the classes of permitted transferee, not named people.
- **Quote:** "No transfer to a Permitted Transferee shall be effective unless (i) the Permitted Transferee agrees in writing to become a party to this Agreement …" (s03)
- **Commonly omitted:** a limit on how much may move this way.

### rofr: Right of first refusal

- **Covers:** the other holders' (and often the company's) right to buy shares a holder wants to
  sell to an outsider.
- **Prevalence:** 18/29 (62%), common
- **Applies when:** `facts.company.share_transfer_rules.rofr != none`
- **Facts:** `facts.company.share_transfer_rules`
- **Patterns:**
  - 10/16 owner, 8/13 vc.
  - 8/18 offer the shares to the company first, then to the other holders; the rest to the
    other holders only.
  - 14/18 split the shares among the buyers pro rata to their holdings.
  - 8/18 start from a bona fide third-party offer and give the holders its price and terms;
    2/18 work as a first offer before any buyer is found; 1/18 as a last refusal.
  - 3/18 make it all-or-nothing, so the seller is not left with a part sale.
  - Each step has a fixed number of days; 3/18 set the closing mechanics in the clause.
- **Detail:** notice contents (buyer, number, price, terms), the periods in days and the order of
  buyers. No figures beyond the periods.
- **Quote:** "Each Shareholder, shall have the first right of refusal to purchase any Shareholder's shares of Stock." (s05)
- **Commonly omitted:** what happens to unsold shares after the period (most let the seller sell
  to the named buyer on no better terms).

### pre-emption: New shares

- **Covers:** holders' right to take up new shares the company issues, and its exceptions.
- **Prevalence:** 11/29 (38%), rare
- **Applies when:** `facts.company.share_transfer_rules.pre_emption == true`
- **Facts:** `facts.company.share_transfer_rules`, `facts.company.share_structure`
- **Patterns:**
  - 5/16 owner, 6/13 vc.
  - 8/11 offer new shares pro rata; 4/11 on a fully diluted basis.
  - 8/11 carve out employee options, conversions, splits and the IPO.
  - 7/11 let unsubscribed shares go to others or to outsiders on the same terms within a set
    period.
  - 3/11 give the right to investors only; 1/11 to one named holder.
  - 2/11 point to the right in the articles or the law instead of restating it.
- **Detail:** the basis of the pro rata share, the carve-outs by kind, the periods in days.
- **Quote:** none
- **Commonly omitted:** a founder's protection against dilution after vesting (1/11).

### tag-along: Tag-along

- **Covers:** other holders' right to join a sale on the same terms.
- **Prevalence:** 13/29 (45%), common
- **Applies when:** `facts.company.share_transfer_rules.tag_along == true`
- **Facts:** `facts.company.share_transfer_rules`
- **Patterns:**
  - 6/16 owner, 7/13 vc.
  - 9/13 let the others sell on the same price and terms; 8/13 pro rata to their holdings.
  - 5/13 apply it only when a controlling stake or a set percentage is sold; the rest on any sale
    the first refusal did not absorb.
  - About 5/13 bind every holder; about 4/13 give it to investors over founders' sales.
- **Detail:** the trigger, the share each may add, the notice period in days.
- **Quote:** "This Tag-along Right is not applicable to any Liquidation Event and shall terminate upon the completion of a Qualifying IPO." (s08)
- **Commonly omitted:** what happens if the buyer refuses the extra shares.

### drag-along: Drag-along

- **Covers:** the right of a majority (or a named holder) to make every holder join a sale of the
  whole company.
- **Prevalence:** 19/29 (66%), common
- **Applies when:** `facts.company.share_transfer_rules.drag_threshold != none`
- **Facts:** `facts.company.share_transfer_rules`, `facts.company.share_structure`
- **Patterns:**
  - 9/16 owner, 10/13 vc.
  - 16/19 trigger it by holders of a set percentage or majority; 7/19 also need board approval.
  - 11/19 protect dragged holders: a minimum price, the agreed liquidation order, or a return
    multiple.
  - 12/19 limit what dragged holders must give: several, capped warranties, a share of escrow
    and costs; 7/19 make them waive any statutory objection to the sale.
  - 6/19 give the others a right to match the offer before the drag.
  - 4/19 back it with a power of attorney or proxy.
  - 2/19 let the founders drag the investors, the reverse of the usual direction.
  - 1/19 (the pre-incorporation form) is one sentence with a plain majority.
- **Detail:** the threshold as a percentage, the conditions by kind, the notice period; no
  named buyer.
- **Quote:** none
- **Commonly omitted:** a time limit after which the drag lapses.

### joinder: New parties

- **Covers:** who else becomes bound and for which shares: transferees and new holders signing a
  joinder or deed of adherence, shares acquired later.
- **Prevalence:** 20/29 (69%), common
- **Applies when:** always
- **Facts:** `facts.company.share_structure`, `facts.company.share_transfer_rules`
- **Patterns:**
  - 17/20 attach the form a new holder signs; 8/20 make it a deed of adherence.
  - 5/20 extend the agreement to shares acquired later and to splits and dividends.
  - 2/20 bar the company from registering a holder who has not signed.
- **Detail:** the joinder form in full in a schedule; no names.
- **Quote:** "The Transferee hereby agrees to be bound by the Founders' Agreement in all respects as if the Transferee were a party to the Founders' Agreement as one of the Founders" (s31)
- **Commonly omitted:** what a new holder may decline (most bind it to the whole agreement).

### information-rights: Information rights

- **Covers:** what information holders receive and may inspect.
- **Prevalence:** 11/29 (38%), rare
- **Applies when:** `facts.company.share_structure` has a holder of kind `investor`, or `facts.company.founder_commitment` has a founder whose engagement is `none`
- **Facts:** `facts.company.share_structure`, `facts.company.founder_commitment`
- **Patterns:**
  - 6/16 owner, 5/13 vc.
  - 9/11 promise annual accounts (audited in most) and quarterly or monthly figures within set
    periods; 6/11 the annual budget.
  - 6/11 give a right to inspect books and meet management.
  - 7/11 limit it to holders above a set holding, or to investors.
  - 1/11 cuts off a holder with a conflict of interest.
- **Detail:** the reports by kind and deadline in days after period end; no figures.
- **Quote:** none
- **Commonly omitted:** confidentiality of what holders receive (left to `confidentiality`).

### ip: Intellectual property

- **Covers:** intellectual property the founders (or staff) owe the company: what they made
  before and what they make while working for it.
- **Prevalence:** 9/29 (31%), rare
- **Applies when:** `facts.company.founder_prior_work != []`, or `facts.company.founder_commitment` has a founder whose engagement is not `none`
- **Facts:** `facts.company.founder_prior_work`, `facts.company.founders`, `facts.company.business_scope`, `facts.company.ip_signers`
- **Patterns:**
  - 5/16 owner, 4/13 vc; all 3 founders' models have it.
  - 8/9 give the IP to the company (2/9 by a present assignment or declaration, the rest by an
    undertaking to assign); 3/9 deal with IP made before the company existed.
  - 5/9 point to a separate IP assignment or invention agreement that founders and staff sign.
  - 1/9 (a joint company) leaves each owner's IP with the owner and licenses it to the company.
  - 3/9 require founders to disclose inventions.
- **Detail:** the kinds of right in general terms (inventions, code, designs, marks); the prior
  work by category in a schedule (1/9 lists patents). No individual files.
- **Quote:** "the rights, title and interest in and to such Intellectual Property shall belong to and be the sole property of the Company" (s31)
- **Commonly omitted:** moral rights; what the founder gets for prior work.

### vesting: Vesting of founder shares

- **Covers:** the schedule over which founder shares stop being subject to buy-back, and what
  speeds it up.
- **Prevalence:** 3/29 (10%), rare
- **Applies when:** `facts.company.founder_vesting.applies == true`
- **Facts:** `facts.company.founder_vesting`, `facts.company.founders`
- **Patterns:**
  - 3/16 owner (the three founders' models), 0/13 vc: investor-stage texts keep it in each
    founder's stock purchase or restriction agreement.
  - 3/3 vest over years. 1/3 fixes it in the text (a quarter after a twelve-month cliff, then
    monthly over 36 months); 2/3 leave it to the drafter: a blank with a note suggesting three to
    four years and a 6–12-month cliff, or a bracketed choice of two to four years with no cliff.
  - 1/3 speeds vesting up when a sale of the company is followed by the founder being let go
    (double trigger).
  - 1/3 keeps shares from the employee option plan outside founder vesting.
- **Detail:** the period, cliff and step in months; the start date (signing or joining).
- **Quote:** "a portion of such shares shall be returned to the Start-Up Company [in accordance with the following vesting schedule: [ ]]" (s32)
- **Commonly omitted:** partial vesting for part-time work; what vesting a later founder gets.

### compulsory-transfers: Leavers and other forced sales

- **Covers:** the events that force a holder to offer or sell its shares (a founder leaving, death,
  incapacity, insolvency, divorce, breach, a change of control) and the price and payment.
- **Prevalence:** 17/29 (59%), common
- **Applies when:** always
- **Facts:** `facts.company.founder_vesting`, `facts.company.founders`, `facts.company.founder_commitment`, `facts.company.share_structure`
- **Patterns:**
  - 13/16 owner, 4/13 vc.
  - Triggers: leaving the company 12/17, death 7/17, divorce 6/17, breach or misconduct 6/17,
    insolvency 5/17, incapacity 5/17, change of control of a holder 2/17.
  - 9/17 split good and bad leavers: a bad leaver resigns early, is dismissed for cause or breaches
    the covenants, and gets the lower of cost or fair value for its shares.
  - 6/17 write the right as a call option for the company or the others; 5/17 add a put for the
    leaver or estate on death or incapacity.
  - Price: fair value 9/17, fixed by an independent expert or appraiser if not agreed 11/17; a
    formula or book value 4/17.
  - Payment: 6/17 allow instalments or a note; 4/17 fund death buy-outs with life insurance.
  - 1/17 (a two-owner company) lets the other owner dissolve the company after a default.
- **Detail:** each trigger, the buyer order, the price basis for each kind of leaver, the
  valuation steps and periods in days; the expert by profession. No figures for the price.
- **Quote:** "The determination of the independent appraiser shall be final and binding on the Involuntary Transferee and the Purchaser(s)." (s03)
- **Commonly omitted:** tax on the buy-back; what happens to the leaver's board seat (2/17).

### company-undertakings: Company undertakings

- **Covers:** what the company itself promises the holders (insurance, compliance, conduct of the
  business, giving effect to the agreement).
- **Prevalence:** 7/29 (24%), rare
- **Applies when:** `facts.company.share_structure` has a holder of kind `investor`
- **Facts:** `facts.company.share_structure`, `facts.company.business_scope`
- **Patterns:**
  - 2/16 owner, 5/13 vc.
  - 4/7 promise directors' and officers' insurance; 3/7 to act so the agreement takes effect
    (calling meetings, legends).
  - 1/7 lists operating undertakings (new opportunities only through the company, policies,
    compliance); 1/7 bans management fees to a holder.
- **Detail:** the undertakings by kind; no policy names or amounts.
- **Quote:** "All new business opportunities relevant to the Company shall only be taken up through the Company or a wholly-owned subsidiary of the Company." (s35)
- **Commonly omitted:** what holders can do if the company breaches them.

### restrictive-covenants: Non-compete and non-solicitation

- **Covers:** what founders or holders may not do: compete, solicit staff or customers, disparage
  the company.
- **Prevalence:** 9/29 (31%), rare
- **Applies when:** `facts.company.staff_restrictions != []`
- **Facts:** `facts.company.staff_restrictions`, `facts.company.business_scope`, `facts.company.staff_locations`
- **Patterns:**
  - 5/16 owner, 4/13 vc; 2 of the 3 founders' models have it.
  - 9/9 combine a non-compete and a non-solicit; 1/9 adds non-disparagement.
  - 7/9 run it while the person holds shares or works for the company and a set period after;
    the periods differ by leaver type in 1/9.
  - 5/9 limit it by territory or field; 2/9 carve out small listed holdings and unsolicited
    approaches.
  - 1/9 backs it with a fixed sum of damages; 1/9 makes each limb separate so a court can strike
    one.
  - 1/9 binds only founders who sit on the board.
- **Detail:** the activities barred, the period in months, the field and area in general terms.
  No named competitors.
- **Quote:** "Each restriction set out in this Clause 9 is separate and distinct and is to be construed separately from the other restrictions." (s31)
- **Commonly omitted:** payment for the restriction period.

### exit: Exit

- **Covers:** how the owners plan to exit: sale or listing intention, cooperation in a listing
  (lock-up), put and call options or a buy-sell between owners outside a deadlock.
- **Prevalence:** 17/29 (59%), common
- **Applies when:** always
- **Facts:** `facts.company.share_transfer_rules`, `facts.company.share_structure`
- **Patterns:**
  - 8/16 owner, 9/13 vc.
  - 11/17 bind holders to a lock-up after a listing at the underwriters' request.
  - 4/17 state an exit intention or horizon and a duty to support it.
  - 4/17 give one owner a put or call over the other's shares (a minority owner's put on a
    schedule; a put if there is no listing by a deadline).
  - 2/17 give any holder a buy-sell offer at a price it names, which the others must accept or
    match.
- **Detail:** the kind of exit, the lock-up length in days, the option windows; no target price.
- **Quote:** none
- **Commonly omitted:** who runs a sale process; how sale costs are shared.

### articles: Relation to the articles

- **Covers:** how the agreement relates to the company's articles, bylaws or charter.
- **Prevalence:** 16/29 (55%), common
- **Applies when:** always
- **Facts:** `facts.company.entity_form`
- **Patterns:**
  - 13/16 make the agreement prevail between the parties when it conflicts with the articles.
  - 12/16 oblige holders to vote to amend the articles to match.
  - 6/16 incorporate articles by pointer, or attach them.
- **Detail:** one or two sentences; the articles named, not quoted.
- **Quote:** none
- **Commonly omitted:** what happens if the articles cannot be amended.

### confidentiality: Confidentiality

- **Covers:** confidentiality of the company's information and of the agreement, and public
  announcements.
- **Prevalence:** 15/29 (52%), common
- **Applies when:** always
- **Facts:** `facts.company.business_scope`
- **Patterns:**
  - 9/16 owner, 6/13 vc.
  - 11/15 list exceptions (law, court, advisers, already public, consent).
  - 6/15 ban announcements about the agreement without consent.
  - 9/15 keep it after a holder leaves, for a set period or for good.
  - 1/15 points to a separate confidentiality agreement.
- **Detail:** the information by kind and the exceptions; no list of secrets.
- **Quote:** "The Parties undertake to keep all information regarding the Company and its business confidential, and not to use or disclose such information except:" (s04)
- **Commonly omitted:** return or deletion of information on leaving.

### term: Term and termination

- **Covers:** when the agreement starts and ends, a holder's release when it no longer holds
  shares, and what survives.
- **Prevalence:** 25/29 (86%), core
- **Applies when:** always
- **Facts:** `facts.company.share_structure`
- **Patterns:**
  - 22/25 end it at a listing; 15/25 on a sale of the company; 6/25 on dissolution; 3/25 when one
    holder owns all the shares.
  - About half run for a fixed term (with renewal in some) or to an end date; the rest until an
    end event.
  - 14/25 keep confidentiality, covenants and accrued rights alive after it ends.
  - 4/25 release a holder who sells all its shares.
- **Detail:** the end events by kind, fixed periods in years; no dates beyond the term.
- **Quote:** none
- **Commonly omitted:** notice to end it early (2/25).

### general: General provisions

- **Covers:** the closing clauses: entire agreement, severability, waiver, assignment,
  counterparts, costs, further assurance, third-party rights, no partnership, representations,
  remedies.
- **Prevalence:** 29/29 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.signatory`
- **Patterns:**
  - Clauses: entire agreement 24/29, severability 24/29, counterparts 23/29, assignment
    23/29, waiver 18/29, specific performance or injunction 15/29, third-party rights 10/29,
    further assurance 10/29, costs 9/29, independent advice or counsel's conflict 8/29, no
    partnership 6/29.
  - 5/29 add each holder's representations (authority, title, no conflicting commitments).
  - 2/29 add a contractual penalty for breach.
  - Most give each clause a sentence or two under one heading; 4/29 as a list.
- **Detail:** stock wording; nothing product-specific.
- **Quote:** "The terms and conditions of this Agreement shall inure to the benefit of and be binding upon the respective successors and assigns of the parties." (s02)
- **Commonly omitted:** a language clause (3/29).

### notices: Notices

- **Covers:** how notices are given and when they count as received.
- **Prevalence:** 26/29 (90%), core
- **Applies when:** always
- **Facts:** `facts.company.share_structure`
- **Patterns:**
  - 24/26 send notices to addresses in a schedule, the signature pages or the clause.
  - 15/26 allow email; 21/26 say when a notice counts as received (on delivery, after a set number
    of days by post).
- **Detail:** the methods and deemed-receipt periods in days; holders' addresses in a schedule.
  The company's address is not repeated: the clause points to *Parties and background*.
- **Quote:** "Failure to accept delivery shall constitute delivery." (s03)
- **Commonly omitted:** changing an address (most allow it by notice in one sentence).

### amendment: Amendment and waiver

- **Covers:** how the agreement is changed or a right waived.
- **Prevalence:** 24/29 (83%), core
- **Applies when:** always
- **Facts:** `facts.company.decision_rules`, `facts.company.share_structure`
- **Patterns:**
  - 20/24 require writing.
  - 7/24 need every party; 15/24 a set majority of holders (13 of them with the company too);
    the two founders' models offer both, unanimity first and a set majority as the alternative.
  - 8/24 add that a change that hits one holder or class more than the others needs its
    consent.
  - 2/24 say that adding a new holder by joinder is not an amendment.
- **Detail:** the majority as a fraction or percentage.
- **Quote:** "No amendment to this Agreement shall be effective unless made in a writing duly executed by each of the Shareholders." (s03)
- **Commonly omitted:** amendment by electronic signature (1/24).

### governing-law: Governing law

- **Covers:** which law governs the agreement.
- **Prevalence:** 27/29 (93%), core
- **Applies when:** always
- **Facts:** `facts.company.contract_law`, `facts.company.entity_form`
- **Patterns:**
  - 27/27 name one law, in almost all the law of the place where the company is registered.
  - 14/27 exclude conflict-of-law rules.
  - One sentence; 6/27 in the closing clauses.
- **Detail:** the country or state only.
- **Quote:** none
- **Commonly omitted:** the reason for the choice.

### disputes: Disputes

- **Covers:** how disputes are resolved: negotiation, mediation, arbitration or courts.
- **Prevalence:** 21/29 (72%), common
- **Applies when:** always
- **Facts:** `facts.company.contract_law`
- **Patterns:**
  - 18/21 send disputes to arbitration (an institution and seat named, one or three arbitrators);
    the rest to named courts; 20/21 name a court, at least for interim relief or enforcement.
  - 3/21 require negotiation first; 1/21 an optional mediation step.
  - 2/21 appoint an agent for service.
- **Detail:** the forum, the institution and seat, the number of arbitrators and the language.
- **Quote:** none
- **Commonly omitted:** costs of the dispute (most leave them to the tribunal).

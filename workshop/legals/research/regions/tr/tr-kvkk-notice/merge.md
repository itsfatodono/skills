# tr-kvkk-notice: merged section list

First batch: s01–s15 (5 large, 5 mid, 5 small; candidates 1–15 in pool order), written before any
saturation batch (`build/build.md` step 3). All 15 are valid; none was replaced. Saturation batch 1
(s16–s20) is judged under *Saturation* and added no id; it is folded into *Section map*, *Merged
list*, the transfer pattern and *Avoid*. Other pattern counts and *Document level* are still over
s01–s15 and are refreshed at step 4. The *First-batch samples* column stays as written. By the
step-3 rule the build is saturated at s20; see *Saturation* for the reservation. Region run `tr`,
kind `whole`: every section is KVKK content, so there is no *Regional content* split (step 4's
root/region rule does not apply). Each meaning below is fixed from here: change one only with a
dated note under *Changes*. One sample row can map to more than one id when it gives more than one
kind of fact (s05's Tablo 1 gives `data-categories`, `collection-method`, `purposes` and
`retention`). This is a notice, so drafting boilerplate that gives the reader no fact is not an id
(PLAN.md decision 44); see *Not sections*.

**A saturation sample is compared against the 23 ids in *Section ids*.**

## Section ids

| Id | Meaning | First-batch samples |
|---|---|---|
| intro | Opening: the law the notice is given under (KVKK Art. 10, the Aydınlatma Tebliği), the controller named in passing, whom the notice addresses (customers, users, data-subject groups covered or excluded), which channels and services it covers, and what it explains. | s01 s02 s04 s05 s06 s07 s08 s09 s10 s11 s12 s13 s14 s15 |
| controller | The controller identified as such (a "Veri Sorumlusu" line, block or section), with any identity and contact details: trade name, address, MERSİS, trade registry, tax number, KEP, e-mail, phone, VERBİS status, representative. A controller named only inside the intro's opening sentence is `intro`. | s01 s02 s03 s05 s06 s07 s08 s10 s12 s13 s15 |
| controller-role | Where the company is not the controller, or not alone: processor for business customers, another firm the controller for a product sold as agent, a content provider without access, a platform that is not party to users' dealings. | s03 s04 s06 s08 s12 |
| notice-status | What the notice is and is not: information only, no acceptance needed, not a consent text; its relation to separate consent texts and the user agreement. | s06 s12 |
| definitions | What KVKK terms mean in general: statutory definitions (personal data, special-category data, processing, controller), a glossary, "what is personal data?" explainers. Defined short names for the parties are drafting, not this id. | s01 s02 s04 s05 s10 |
| data-categories | Which personal data is processed, by category, with example fields; limits on what is collected or stored. | all 15 |
| collection-method | How and from where data is obtained (Art. 10(1)(d)): channels, sources (the person, third parties, public sources), fully/partly automated or non-automated method. | all 15 |
| special-categories | Whether special-category (özel nitelikli) data is processed, which, why and on which Art. 6 condition; or that none is sought. | s02 s04 s06 s08 s10 s12 s15 |
| purposes | Why data is processed and on which Art. 5/6 legal basis, per purpose, activity, data category or basis; cases where consent is not needed; explicit-consent purposes. | all 15 |
| user-duties | What the reader must do: inform third parties whose data they share, not post special-category or others' data, register only people they represent, keep data accurate. | s05 s08 s12 s15 |
| integrations | Third-party services the user connects and the data that moves (Google APIs with Limited Use, Apple Health / Health Connect). | s03 s06 |
| cookies-tracking | Cookies, SDKs and ad measurement in the notice: their use, basis and consent route, or a pointer to the separate cookie notice. | s02 s03 s04 s05 s06 s07 s12 s15 |
| recipients | Who receives data inside Turkey or in general (Art. 8, 10(1)(c)): recipient groups, purpose and basis per group, data shared, what is public or shown to other users, no-sale statements. | all 15 |
| transfer-abroad | Whether data goes abroad, to whom, why, and under which Art. 9 tool (adequacy, standard contract with notification, BCR, undertaking, occasional transfer), or that none is made. | all 15 |
| children | Minors' data: age limit, when it is processed, guardian consent or guardian-registered accounts. | s02 s04 s08 |
| consent-withdrawal | How to withdraw explicit consent and opt out of commercial messages, and the effect (future only, service not blocked). | s02 s03 s06 s12 s15 |
| retention | How long data is kept (periods or rule), the retention and destruction policy, periodic destruction, deletion method. | s02 s03 s04 s05 s06 s07 s08 s09 s10 s12 s13 s15 |
| automated-decisions | Automated decisions and profiling the company runs, and how to object (Art. 11(1)(g)). | s02 s03 s04 s12 |
| security | Technical and administrative measures, staff confidentiality, breach notification. | s01 s02 s04 s05 s06 s10 s12 |
| ai-use | Features that send data to AI services, what is and is not sent, provider terms. | s03 |
| rights | The data-subject rights of Art. 11, listed or referred to. | all 15 |
| application | How to exercise the rights: channels (post, notary, KEP, e-signature, registered e-mail, form), required contents, identity checks, proxies, 30-day reply and fee, complaint to the Board, in-app self-service routes. | all 15 |
| changes | How the notice is updated, how readers are told, when a change takes effect. | s02 s04 s06 s12 |

Not sections (document level, step 4): titles (s05 row 1, s08 row 0, s11 row 0, s14 row 1); dates
and version labels (s03 row 0, s12 and s15 date lines); s02's document-info block, table of contents
and version-history table (its update rules in §18 are `changes`); s06's table of contents and print
link; s02 §7 and s08 §3, headings that only hold sub-sections. Drafting boilerplate (decision 44):
defined short names ("Kanun", "Şirket", "Platform"; s06 §1's Kanun/Kurul/Kurum) and the restated
Art. 4 processing principles (s01 intro, s02 §1, s06 §5 opening), which state the law, not a fact
about the company; both are folded into the row they sit in.

**s06's annexes (Ek 1–6) are not this document** (`sources.md` rule 6): Ek 2, 3, 4A, 4B and 5 are
consent and permission texts (for `tr-explicit-consent`, item 51 and cookie consent), Ek 6 is
request guidance (for `data-subject-request`). Ek 1 (signup-screen short notice) and Ek 4 (spoken
pre-recording notice) are layered versions of this notice: recorded under *Document level*.

## Mapping notes

- s01: §1–§2 (Art. 3 glossary, "what is personal data") to `definitions`; each activity block of §3
  to `data-categories` and `purposes`; §6 splits into `recipients` and `transfer-abroad`; §7 iii to
  `controller` (the intro names the controller only in passing).
- s02: §0's controller name is document metadata; §5's closing note that consent is revocable and
  forward-only to `consent-withdrawal` (§15 is its main section); §6 CCTV to `purposes`,
  `retention` and `recipients` (an activity block, not an id of its own); 7.2's cookie paragraph to
  `cookies-tracking`; 7.4 to `application` (self-service) and `retention`; §9 with its unfilled
  alternatives to `transfer-abroad`; §12's breach notification to `security`.
- s03: no intro (title, then §1); §1's content-provider paragraph to `controller-role`; §2's source
  column to `collection-method`, 2a to `data-categories`; 2b to `integrations`; §3's cookie, opt-out
  and incidental-transfer-consent cells to `cookies-tracking`, `consent-withdrawal` and
  `transfer-abroad`; 3b to `cookies-tracking` and `retention`; §5's public posting to `recipients`.
- s04: the intro names the bank only in passing, so no `controller`; §2's cookie pointer to
  `cookies-tracking`; §3's statutory definition to `definitions`; ÖNEMLİ NOT to `controller-role`;
  foreign recipients inside the §4 image table to `transfer-abroad`; §6's mandatory application
  contents to `application`.
- s05: GİRİŞ's third-party-data paragraph and §7's accuracy request to `user-duties`; §1's quoted
  controller definition to `definitions`; row 7 (when consent is not needed) to `purposes`; rows
  8–10 to `recipients`.
- s06: §2.1 and §2.2 to `controller-role`; §2.3 and the annex bridge (row 20) to `notice-status`;
  §7 call recording to `purposes` and `retention`; §14 to `cookies-tracking`; §16's withdrawal
  paragraph and §19's separate permissions to `consent-withdrawal`.
- s07: each numbered activity block to `data-categories`, `purposes`, `recipients` and, where it has
  the standard-contract paragraph, `transfer-abroad`; block 10's public event photos to `recipients`;
  the controller line in the title block to `controller`.
- s08: §1 opens on the controller, then scope and the processor role (`controller`, `intro`,
  `controller-role`); 3.1's Önemli Not to `user-duties`, its Art. 6/3 rows to `special-categories`;
  3.2 to `children`; §5's closing sentence to `retention`.
- s09: the retention-for-limitation-period purpose row to `retention` (same fact, held in the
  purposes table); transfers abroad inside three recipient rows to `transfer-abroad`.
- s10: the intro's security commitment to `security`; §1's definition to `definitions`; §5's
  unmapped bases list to `purposes`; §6 (traffic and location data) to `purposes` and `retention`;
  §8 contact block to `controller`.
- s11: data categories named only inside purpose bullets to `data-categories`; §3's second
  paragraph to `transfer-abroad`.
- s12: §2 (data-subject groups) to `intro`; §3's request not to post special-category data to
  `user-duties`; 5.1 (public / counterpart / nobody) to `recipients`; §6's cookie-policy link to
  `cookies-tracking`; §10's in-product paths to `consent-withdrawal` and `application`.
- s13: the "Veri Sorumlusu" label with address in the title block to `controller`; both processing
  contexts to `data-categories`, `collection-method` and `purposes`.
- s14: no controller block (address and KEP only as application channels); 4.1 (Art. 5(2) list for
  domestic transfer) and 4.3 to `recipients`; 4.2 to `transfer-abroad`.
- s15: the special-category note between category blocks to `user-duties` and `special-categories`;
  the ad-measurement block to `cookies-tracking`, `transfer-abroad` and `consent-withdrawal`; the
  footer line repeats `controller`.

- Saturation batch 1:
  - s16: the intro names the controller only in passing (no `controller`); the context table to
    `purposes` and `data-categories`, its children's-size footnote to `children`, its profiling
    cells' channels and no-purchase/no-sale lines to `collection-method` and `recipients`, the
    cookie-notice link to `cookies-tracking`; §3's two named foreign providers to
    `transfer-abroad`; the missing first Art. 11 right is a pattern of `rights`.
  - s17: the intro's care-and-measures paragraph to `security` (as s10); §1 to `controller`; the
    per-category paragraphs to `data-categories` and `purposes`; §6's restated bases to
    `purposes`; §6 (apply) only refers to Art. 11, so `rights` by reference, as s08 and s09. No
    transfer fact.
  - s18: §1's opening sentence to `intro`, its field block to `controller`; §2's scope to `intro`
    and its "notice and consent are separate" paragraph to `notice-status`; each 3.x activity to
    `data-categories`, `collection-method` and `purposes`; 3.1's "do not type ID or health data" to
    `user-duties`; 3.3's named CAPTCHA provider to `recipients`; 3.4 (consent records) and 3.5 to
    `cookies-tracking`, 3.5's cookie-icon withdrawal to `consent-withdrawal`; 3.6 (handling
    requests) to `purposes`; §5 to `transfer-abroad` (services abroad named, no Art. 9 tool chosen);
    §9 to `changes`.
  - s19: §3's channel paragraph to `collection-method`, its table to `purposes`; §4's table and
    share-sale paragraph to `recipients`, its Art. 9 sentence to `transfer-abroad`; §7 to `changes`
    (the update date is document level).
  - s20: the intro names the controller only in passing; A's biometric line to
    `special-categories` (basis: anti-money-laundering law, not consent); C has no transfer-abroad
    statement; the closing line to `changes`.

## Section map

First-row order of ids per sample (the basis of every count and median below).

```
s01 intro definitions data-categories purposes collection-method security recipients transfer-abroad rights application controller
s02 intro definitions controller data-categories special-categories purposes consent-withdrawal retention recipients cookies-tracking application transfer-abroad collection-method security rights automated-decisions children changes
s03 controller controller-role data-categories collection-method integrations purposes cookies-tracking consent-withdrawal transfer-abroad automated-decisions retention ai-use recipients rights application
s04 intro collection-method cookies-tracking definitions data-categories special-categories children purposes controller-role recipients transfer-abroad automated-decisions rights application retention security changes
s05 intro user-duties controller definitions collection-method retention data-categories purposes recipients transfer-abroad cookies-tracking security rights application
s06 intro controller controller-role notice-status data-categories collection-method purposes special-categories retention recipients transfer-abroad integrations cookies-tracking security rights consent-withdrawal application changes
s07 intro controller cookies-tracking collection-method data-categories purposes transfer-abroad recipients retention rights application
s08 controller intro controller-role collection-method data-categories purposes special-categories user-duties children recipients transfer-abroad rights application retention
s09 intro data-categories purposes retention recipients transfer-abroad collection-method rights application
s10 intro security definitions data-categories special-categories purposes recipients transfer-abroad collection-method retention rights application controller
s11 intro purposes data-categories recipients transfer-abroad collection-method rights application
s12 intro notice-status controller controller-role data-categories collection-method special-categories user-duties purposes recipients transfer-abroad cookies-tracking retention security automated-decisions rights consent-withdrawal application changes
s13 intro controller data-categories collection-method purposes recipients transfer-abroad retention rights application
s14 intro data-categories purposes recipients transfer-abroad collection-method rights application
s15 intro controller data-categories purposes collection-method user-duties special-categories cookies-tracking transfer-abroad consent-withdrawal recipients retention rights application
s16 intro purposes data-categories children collection-method recipients cookies-tracking transfer-abroad rights application
s17 intro security controller purposes data-categories recipients collection-method rights application
s18 intro controller notice-status data-categories collection-method purposes user-duties recipients cookies-tracking consent-withdrawal transfer-abroad retention rights application changes
s19 intro data-categories collection-method purposes recipients transfer-abroad rights application changes
s20 intro data-categories special-categories purposes recipients collection-method rights application changes
```

## Merged list (s01–s20)

Median position is the first row's rank divided by the sample's id count less one (0 = first,
1 = last). Tiers per `formats/skeleton-format.md` (core ≥80% = 16+/20, common 40–79% = 8–15, rare
<40% = 7 or fewer). *Commonly omitted* = fewer than 20% (≤3/20). The *s01–s15* column is the
first-batch count.

| Id | Count | s01–s15 | Tier | Median pos. | Note |
|---|---|---|---|---|---|
| intro | 19/20 | 14/15 | core | 0.00 | |
| controller | 13/20 | 11/15 | common | 0.11 | Art. 10(1)(a) duty; the other 7 name the controller only in the intro |
| notice-status | 3/20 | 2/15 | rare | 0.14 | commonly omitted |
| controller-role | 5/20 | 5/15 | rare | 0.15 | |
| definitions | 5/20 | 5/15 | rare | 0.17 | |
| data-categories | 20/20 | 15/15 | core | 0.22 | |
| collection-method | 20/20 | 15/15 | core | 0.32 | Art. 10(1)(d) |
| special-categories | 8/20 | 7/15 | common | 0.33 | |
| purposes | 20/20 | 15/15 | core | 0.37 | Art. 10(1)(b), (d); carries an *Avoid* |
| user-duties | 5/20 | 4/15 | rare | 0.39 | |
| integrations | 2/20 | 2/15 | rare | 0.47 | commonly omitted |
| children | 4/20 | 3/15 | rare | 0.50 | |
| recipients | 20/20 | 15/15 | core | 0.54 | Art. 10(1)(c) |
| cookies-tracking | 10/20 | 8/15 | common | 0.55 | |
| transfer-abroad | 18/20 | 15/15 | core | 0.62 | the 2 without it are the 2 `no-transfer` samples; see *Patterns*; carries an *Avoid* |
| consent-withdrawal | 6/20 | 5/15 | rare | 0.67 | |
| automated-decisions | 4/20 | 4/15 | rare | 0.73 | |
| security | 8/20 | 7/15 | common | 0.74 | |
| retention | 13/20 | 12/15 | common | 0.75 | was core; Art. 10 does not require it |
| ai-use | 1/20 | 1/15 | rare | 0.79 | commonly omitted |
| rights | 20/20 | 15/15 | core | 0.86 | Art. 10(1)(e); 3/20 only refer to the article |
| application | 20/20 | 15/15 | core | 0.97 | |
| changes | 7/20 | 4/15 | rare | 1.00 | |

By count: 8 core, 5 common, 10 rare (23 ids). Since the first batch `retention` moved from core to
common (12/15 → 13/20): none of s16, s17, s19 or s20 says how long data is kept. Every Art. 10(1)
item is core except `controller`.

## Patterns (s01–s15)

Shared wording counts once (decision 39): the s07/s13 block and the s09/s11 stock frame under
*Copies*.

- **purposes:** 9/15 a table (s01 one per activity, s02 s03 s04 s05 s06 s08 s09 s12), 5/15 a list
  (s07 s10 s11 s14 s15), s13 prose. Cut by activity (s01 s07 s13), by legal basis (s08 s11), by data
  category (s05 s15) or one row per purpose (s02 s03 s04 s06 s09 s12). Bases cited by Art. 5
  letter in 5/15 (s02 s03 s06 s08 s12), in the statute's words or a paraphrase in 8/15; 2/15 name no
  basis per purpose (s10 lists bases apart, s14 says "at least one Art. 5/6 condition"). 4/15 use
  the VERBİS purpose names (s01 s05 s07 s13). 14/15 use explicit consent somewhere, mostly for
  marketing; s13 none. 7/15 tie commercial e-messages to a separate ETK/İYS permission (s02 s03 s06
  s07 s09 s11 s15).
- **data-categories:** 10/15 a separate inventory (s02 s03 s04 s05 s06 s09 s10 s12 s14 s15), 5/15
  name categories only inside activity blocks or purpose rows (s01 s07 s08 s11 s13). Most use the
  VERBİS category names with "örn." examples. 5/15 say what is not collected or stored (card data,
  ID number, location: s02 s03 s06 s09 s12).
- **collection-method:** 11/15 a section of its own, 4/15 per activity or as a column (s03 s07 s13
  s15). At least 7/15 use the statutory "fully or partly automated, or non-automated" formula (s01
  s02 s04 s06 s09 s12; s14 "oral, written or electronic"). 2/15 end the channel list open-ended
  ("ileride eklenebilecek sair yöntemler": s08 s09; see *Avoid*).
- **recipients:** 6/15 a table of groups (s02 s04 s06 s09 s12 s14), 6/15 a list (s03 s07 s08 s10
  s13 s15), 3/15 prose (s01 s05 s11). 3/15 add a no-sale statement (s02 s03 s06); 3/15 treat the
  public or other users as recipients (s03 s07 s12); s05 says recipients are named only by group
  because their identity is a trade secret.
- **transfer-abroad (decision 46), recounted over s01–s20:** 18/20 give the fact. **0 of the 18
  are `no-transfer`**; the 2 `no-transfer` samples so far (s17 BKM Kitap, s20 Paribu) both lack it,
  as their tag says. By tag: `art9` 11/11 have it (s16 s19 added), `dated`-only 7/7 (s18 added),
  `no-transfer` 0/2. The count still leans high because of the cut-off: `no-transfer` is 5/30 of
  the pool (rows 17, 20, 23, 26, 29), so if every other sample has the fact the floor is 25/30
  (83%) and the id stays core. Batch 1 added no Art. 9 tool to the patterns: s16 uses the standard
  contract and names two foreign providers; s18 names services abroad and the US but chooses no
  tool; s19 restates "a safeguard or an occasional transfer" without choosing, as s10 and s14 do
  (4/20 now name no specific tool without resting on a wrong basis: s10 s14 s18 s19). First-batch
  detail follows (s01–s15). Placement: 7/15 a section or sub-section (s02 s03 s05 s06 s10 s12 s14), 8/15
  folded into recipient rows, activity blocks or one sentence (s01 s04 s07 s08 s09 s11 s13 s15).
  Tool: 11/15 the standard contract (s01 s03 s05 s06 s07 s08 s09 s11 s12 s13 s15); 4/15 mention the
  5-business-day notification to the Authority (s02 s03 s06 s12); 2/15 restate the whole Art. 9
  ladder without saying which applies (s10 s14; s14 says "as a rule" no transfer), s02 leaves two
  bracketed alternatives unfilled; s03 and s12 keep occasional transfer with consent as a fallback
  only; s15 rests a regular SDK transfer on consent and s04 names no Art. 9 tool (both *Avoid*).
  2/15 name countries (s03 s12); 4/15 name foreign recipients (s04 by type, s11 s12 s15).
- **retention:** 4/15 a table of periods per data set (s02 s03 s06 s12); 4/15 a rule with at most
  one example (s04 s07 s13 s15); 4/15 one period or one data type (s05 s08 s10, s09 as a purpose
  row). 3/15 name a retention and destruction policy (s02 s07 s10); 3/15 a periodic destruction
  cycle (s02 s07 s12).
- **rights:** 13/15 list the Art. 11 rights (14 as a list, s02 a table); 2/15 only refer to the
  article (s08 s09).
- **application:** 9/15 link an application form (s01 s03 s04 s07 s08 s09 s11 s12 s13); s11 gives
  the form as its only route. 4/15 name the complaint to the Board (s02 s03 s06 s12); 4/15 point to
  in-app self-service (s02 s03 s08 s12). 2/15 publish unfilled placeholders for the address (s02
  s09).
- **controller:** 6/15 a full block with registry identifiers (s01 s02 s03 s06 s12 s15); 9/15 put it
  first, 2/15 last (s01 s10), s15 repeats it in a footer.
- **special-categories:** 3/15 say none is sought (s02 s06 s12); 3/15 name the data and the Art. 6
  condition (s04 s08 s10); s15 only warns users not to share it.
- **cookies-tracking:** 3/15 a pointer only (s04 s07 s12); 3/15 describe cookie consent (s02 s05
  s06); 2/15 cover app ad measurement with its consent route (s03 s15).
- **security:** 4/15 one general paragraph (s01 s04 s05 s10); 3/15 concrete measures (s02 s06 s12);
  2/15 breach notification (s02 s06).

### Avoid candidates (decisions 47, 50)

Patterns the guidance calls wrong; never a Default, whatever the count. Guidance: KVKK Arts. 5, 9
and 10; the Aydınlatma Yükümlülüğü Tebliğ (Art. 5(1)(f)–(j)); the Board's guidance on explicit consent
("Açık Rıza Alırken Dikkat Edilecek Hususlar") and on the processing conditions ("Kişisel Verilerin
İşlenme Şartları"; citation corrected 2026-10-27).

| Id | Pattern | Count | Guidance |
|---|---|---|---|
| purposes | Explicit consent stacked on, or used for, processing that has another basis | 3/20 (s04 pre-approved credit: contract, law, obligation and consent for one purpose; s07 loyalty events on consent plus legitimate interest, and a compliance purpose under consent; s17 lists explicit consent beside the Art. 5(2) bases under most data categories) | Board's guide on the processing conditions ("Kişisel Verilerin İşlenme Şartları"): where a condition other than consent applies, consent must not also be asked for. Tebliğ Art. 5(1)(h): name the condition relied on. s01's marketing block lists operational VERBİS purposes under consent: borderline, not counted. |
| purposes | Legal basis not named per processing | 4/20 (s14 none; s09 some rows blank; s10 bases listed apart from purposes; s17 "one or more of" the full list per category) | Tebliğ Art. 5(1)(h): the notice must state clearly which Art. 5/6 condition each processing rests on. |
| collection-method | Open-ended catch-alls ("and other methods that may be added later") | 2/20 (s08 s09; none in s16–s20) | Tebliğ Art. 5(1)(g): no general or vague wording; Art. 5(1)(i): state the method clearly. |
| transfer-abroad | Regular transfer abroad on explicit consent | 1/20 (s15: ad SDK to Meta) | KVKK Art. 9(6)(a) as amended by Law 7499: consent covers only occasional, non-repeating transfers. s12 says the same in its own text. |
| transfer-abroad | Transfer abroad with no Art. 9 tool (foreign recipients on Art. 5/6 or sector-law bases alone) | 1/20 (s04; s18 names no tool but rests on no wrong basis, so it is a pattern) | KVKK Art. 9(1)–(4): adequacy, appropriate safeguards or occasional transfer. s04 passed the screen on its date only. |

Looked for, not found in s01–s20: notice and consent bundled (0/20; s06 puts its consent texts on
the same page but as separate annexes with unticked choices, borderline, not counted; Tebliğ
Art. 5(1)(f)); a notice that asks for acceptance (0/20; s06's signup line is an acknowledgment it
calls "not consent", and s06, s12 and s18 say acceptance is not needed). Bare article references for
the rights (s08 s09 s17) and s16's list missing the first right are incomplete rather than called wrong: a pattern, not an *Avoid*.

## Document level (s01–s15)

- **Words:** median about 2,300 (range 1,440–6,080). Large about 1,920, mid about 1,980, small
  about 2,390: small companies write the longest texts (s06 6,080, s12 3,710).
- **Carrier:** 13/15 web pages; s05 a PDF, s14 a Word file saved as HTML. s10 is one tab of a
  page holding four group notices; s04 publishes its two main tables as images.
- **Title:** all "Aydınlatma Metni"; 9/15 name the audience (Müşteri: s01 s07 s09 s13; Kullanıcı: s05
  s08 s11; Yatırımcı Adayı: s14; Mobil Uygulama Kullanıcıları: s15).
- **Structure:** 12/15 numbered sections; s07 numbers activity blocks, s09 and s11 do not number.
  4/15 are built around processing activities (s01 s07 s13, s02 for CCTV and online). 2/15 a table
  of contents (s02 s06); 5/15 use question headings (s01 s03 s12 s13 s15, some or all).
- **Register:** 12/15 formal "siz" with long nominal sentences and statutory wording copied; s03
  informal "sen"; s06 and s12 plain "biz/siz".
- **Recurring elements:** a date 7/15 (s02 s03 s04 s06 s09 s12 s15), none 8/15; a version label 4/15
  (s02 s03 s12 s15); defined short names in nearly all; pointers to a separate cookie notice, consent
  texts, a KVKK policy (s05 s14) or the application form. Published placeholders or leftovers in
  4/15 (s02 brackets, s09 "[●]", s13 copy-paste slips, s14 another company's name).
- **Layered notice:** 2/15 (s02: signs as the first layer for CCTV, QR code and print copies in
  stores; s06: short notice for the signup screen and a spoken notice before call recording).
- **Not sections:** see the note under *Section ids*.

## Facts preview

Facts each id needs, for reuse by `tr-explicit-consent` and the `tr` block of
`data-subject-request` (step 5 comes later; no facts file is edited here). Existing keys are
reused where the fact is the same; `facts.tr.*` is proposed only where the fact is KVKK-specific.

| Id | Facts | Keys |
|---|---|---|
| intro | groups covered; apps, sites and offline channels covered | `facts.data.subject_categories`, `facts.product.services_in_scope`, `facts.product.name` |
| controller | name, address, contacts, registry ids, VERBİS, representative | `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.company.phone`, `facts.tr.seller_registry` (MERSİS, tax, trade registry, KEP: same fact; the name says "seller" but fits), **`facts.tr.verbis`**, **`facts.tr.controller_representative`** |
| controller-role | processor role, joint control, marketplace intermediary | `facts.company.acts_as_processor`, `facts.company.processor_customers`, `facts.company.joint_controllers`, `facts.tr.sales_model` |
| notice-status | which processing rests on separate consent texts | derived from **`facts.tr.legal_bases`**; consent texts' URLs in `facts.company.published_policies` |
| definitions | none | — |
| data-categories | categories, fields, required or optional, not collected | `facts.data.collected` |
| collection-method | sources; online channels; offline and non-automated channels | `facts.data.collected` (source), `facts.data.third_party_sources`, `facts.product.services_in_scope`, **`facts.tr.collection_channels`** |
| special-categories | special data, purpose, Art. 6 condition | `facts.data.sensitive` (with the condition from **`facts.tr.legal_bases`**) |
| purposes | purpose per category; the KVKK condition per purpose; activity flows (call recording, CCTV); commercial messages | `facts.data.purposes`, **`facts.tr.legal_bases`**, `facts.product.features`, `facts.marketing.email`, `facts.marketing.sms`, `facts.marketing.push` |
| user-duties | public or shared content; guardian accounts | `facts.product.public_content`, `facts.product.child_directed` |
| integrations | connected services, platform statements | `facts.product.integrations`, `facts.product.platform_disclosures` |
| cookies-tracking | trackers, consent route, cookie notice URL | `facts.data.tracking`, `facts.data.cookie_controls`, `facts.company.published_policies` |
| recipients | processors, other recipients, group companies, sale, public display | `facts.processors.list`, `facts.data.other_recipients`, `facts.company.group_companies`, `facts.data.sells`, `facts.product.public_content` |
| transfer-abroad | countries; foreign recipients; the Art. 9 tool and notification per transfer | `facts.data.storage_locations`, `facts.processors.list` (location), `facts.company.group_companies` (country), **`facts.tr.transfer_tools`** |
| children | minimum age, child-directed | `facts.product.min_age`, `facts.product.child_directed` |
| consent-withdrawal | where consent and message permissions are withdrawn | `facts.data.cookie_controls`, `facts.users.rights_channels`, `facts.marketing.*` (İYS registration is left to item 52) |
| retention | periods per category, data kept after deletion, destruction policy and cycle | `facts.data.retention`, `facts.data.kept_after_deletion`, **`facts.tr.destruction_policy`** |
| automated-decisions | automated decisions | `facts.data.automated_decisions` |
| security | measures | `facts.data.security_measures` |
| ai-use | AI features | `facts.product.ai_features` |
| rights | none (statutory) | — |
| application | channels, KEP, form URL, in-app routes | `facts.users.rights_channels`, `facts.company.contact_email`, `facts.company.address`, `facts.tr.seller_registry` (KEP), `facts.company.published_policies` (application form) |
| changes | how changes are announced | `facts.company.change_notice` |

Proposed `facts.tr.*` keys (6):

- `facts.tr.legal_bases`: per purpose, the KVKK condition relied on: Art. 5(1) explicit consent,
  Art. 5(2)(a)–(f), or for special-category data Art. 6(3) as amended by Law 7499. The basis enum
  in `facts.data.purposes` is GDPR-shaped and cannot hold these. `tr-explicit-consent` reads the
  consent rows from it.
- `facts.tr.transfer_tools`: per transfer abroad, the recipient, country and Art. 9 tool (adequacy,
  standard contract with the Authority notification date, BCR, written undertaking, occasional
  transfer under Art. 9(6)), or none.
- `facts.tr.verbis`: VERBİS registration status (registered, exempt, not yet registered).
- `facts.tr.controller_representative`: the Turkish data-controller representative of a controller
  not established in Turkey, or none.
- `facts.tr.collection_channels`: offline and non-automated channels (stores, call centre, paper
  forms, CCTV, events), needed for the Art. 10(1)(d) method statement.
- `facts.tr.destruction_policy`: whether a retention and destruction policy exists and the
  periodic destruction interval (Regulation on deletion, destruction or anonymisation).

## Copies (rule 4)

None in s01–s15. Compared on the `raw/` texts with 6-word shingles (share of the smaller text's
shingles): the highest pair is s07/s13 at 0.28, then s13/s15 at 0.12 (the statutory rights wording) and
s09/s11 at 0.11; every other pair is under 0.09. Neither is a copy:

- s07 Starbucks and s13 Mudo share a law-firm block: the VERBİS purpose strings, the Art. 11 rights
  list word for word, and the application paragraphs (Tebliğ contents, proxies, "Yetkisiz üçüncü
  kişilerin…"). Headings, activity blocks, transfers and retention differ. The block adds to
  patterns once.
- s09 Fırsat and s11 Pluxee share a stock frame: the opening sentence ("…veri sorumlusu olarak …
  tarafından aşağıda açıklanan kapsamda işlenebilecektir"), the purposes lead-in and two headings.
  Content (categories, rows, recipients, transfers) differs. The frame adds to patterns once.
  s16 FLO carries the same frame (batch 1; see *Saturation*).

No candidate is a known generator template; s02's unfilled brackets read as a law-firm template
used by one company only.

## First-batch qualification

All 15 valid. Borderline ones:

| Sample | Verdict | Why |
|---|---|---|
| s02 Lufian (mid) | valid, borderline | published with bracket placeholders (address, KEP, retention, transfer status); it is the live text. |
| s04 ING (large) | valid, borderline | the two main tables are published as images (the extraction describes them); kept on `dated` (2024-09-03), though its foreign transfers name no Art. 9 tool (*Avoid*). |
| s06 Cari Plus (small) | valid | only the notice is the sample; Ek 1–6 are outside this document (rule 6). |
| s09 Fırsat (small) | valid; **a short notice, not a thin extraction** | only 6 rows, but the raw text has exactly the intro and five headings (categories, purposes, recipients, method, rights), the stock frame it shares with s11. Retention, security and a controller block are missing from the page, not from the extraction; the extractor's 2,116 words match the raw text's 2,212 less site chrome. The page is short in sections, not in words: its tables are long. |
| s10 Türk Telekom (large) | valid | only the first tab (Türk Telekom customer notice) is the sample; the other tabs are group companies (rule 5). |
| s14 Gedik (mid) | valid, borderline | a prospective-investor notice, the account-opening notice the app links; another group company's name left in its text. |

## Saturation

A sample is new only when it has a section whose content fits no id in *Section ids*; how it
writes a known id never makes it new (`build/build.md` step 3). Stop at 5 non-new in a row. Copies
(rule 4) are not judged. Drafting boilerplate never makes a sample new (decision 44).

Batch 1 in pool order: s16–s20 (candidates 16–20; tags `art9`, `no-transfer`, `dated`,
`dated, art9`, `no-transfer`). All valid: each is the company's live customer notice in Turkish, and
each company is its own group (rule 5: FLO, BKM Kitap/Point İnternet, Güven Eğitim, Getir, Paribu;
none shares an owner with s01–s15). s17 and s18 name an operating company as controller that
differs from the brand or app seller; both are still the brand's own notice. s20's page continues
with a group company's separate notice, not extracted (rule 6). No copies (rule 4, raw texts):
s16 shares the s09/s11 stock frame (0.25 with s11: opening sentence, purposes lead-in, headings)
but its table, recipients and transfers differ; every other pair is under 0.07.

| Sample | Verdict | Why |
|---|---|---|
| s16 FLO (large, `art9`) | not new | context table to `purposes`, `data-categories`, `children` (footnote), `cookies-tracking` (link); recipients with no-sale line; two named foreign providers on standard contract to `transfer-abroad`; form-only application. 1 non-new |
| s17 BKM Kitap (mid, `no-transfer`) | not new | care statement to `security`; per-category paragraphs to `data-categories` and `purposes` (adds to two *Avoid* counts); one-sentence recipients; rights only by reference. No transfer fact, as tagged. 2 |
| s18 Güven Sürücü Kursu (small, `dated`) | not new | the richest of the batch (16 rows), all known ids: per-activity blocks to `data-categories`, `collection-method`, `purposes`; `notice-status`, `user-duties`, `cookies-tracking`, `consent-withdrawal`, `retention`, `changes`; services abroad with no tool chosen to `transfer-abroad`. 3 |
| s19 Getir (large, `dated, art9`) | not new | category table, activity table with bases, recipients table with share-sale paragraph, Art. 9 sentence without a chosen tool, rights, application, `changes`. 4 |
| s20 Paribu (mid, `no-transfer`) | not new | biometric data to `special-categories` (AML-law basis); purposes by basis; one-sentence recipients; no transfer fact, as tagged; `changes` in the closing line. 5 |

**Stop (step-3 rule):** 5 non-new in a row (s16–s20): `saturated: true` at s20 with 20 samples
(7 large, 7 mid, 6 small). No id was added after the first batch: 23 ids throughout.

**Reservation (chief of staff's concern).** Counted over `dated`/`art9` samples only, the run is
3 (s16, s18, s19), not 5: it would not hold. The build order (pool order) includes `no-transfer`
samples by decision 46, so the rule is met as written. The concern is partly right. Short samples
hit fewer ids (s17 9, s20 9, s16 10, against a first-batch median of 14), so they are weak tests
for a new id. But thinness is not a `no-transfer` trait: s16 (`art9`, large) is as thin, and the
richest test in the batch, s18 (16 rows, `dated`, small), brought nothing new and hit four rare
ids. The rare tail is recurring, not growing: one id is still single (`ai-use`), and
`notice-status`, `user-duties`, `consent-withdrawal` and `changes` each gained a sample. My view:
the ids are probably complete, but the evidence for that rests on 3 samples, not 5. One more batch
(s21–s25: pool rows 21 small `dated`, 22 large `art9`, 23 mid `no-transfer`, 24 small `dated`, 25
large `art9`) would make the `dated`/`art9` run 7 if none is new, and would firm up the counts
near tier edges (`retention` 13/20, `controller` 13/20, `transfer-abroad` 18/20). It is cheap, and
I recommend it as a check, not a rule change. The owner decides; until then the rule's
`saturated: true` stands with this reservation.

**Decision (chief of staff, delegated by the owner, 2026-10-27):** follow the rule: saturated at
s20, no extra batch. Grounds: thinness is not a `no-transfer` trait, and s18 brought nothing new.
Pool rows 21–30 are not extracted. `sample_count: 20`.

## Changes

- 2026-10-27 (saturation batch 1): no id added and no meaning changed. Counts moved to s01–s20:
  `retention` core → common, `transfer-abroad` 15/15 → 18/20 (the 2 without it are the 2
  `no-transfer` samples). *Avoid* counts: consent stacked 2 → 3 and basis not named 3 → 4 (both
  s17).
- 2026-10-27 (step 4): `definitions` (5/20) and `notice-status` (3/20) stay ids here but are folded
  into `intro` as patterns in the skeleton (drafting content no fact decides; `skeleton-format.md`
  rare-section rule); `ai-use` (1/20) is folded into `purposes`, with `facts.product.ai_features`
  among its facts. The skeleton has 20 sections: 8 core, 5 common, 7 rare.

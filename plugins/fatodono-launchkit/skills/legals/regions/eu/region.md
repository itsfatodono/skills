---
code: eu
name: European Union
laws:
  - GDPR (Regulation (EU) 2016/679)
  - Consumer Rights Directive (2011/83/EU)
  - Digital Services Act (Regulation (EU) 2022/2065)
  - AI Act (Regulation (EU) 2024/1689), Art. 50
  - European Accessibility Act (Directive (EU) 2019/882)
languages: [en]
storefront: ie
added: 2026-10-26
---

## Sources

Shared routes (R1–R12) and the candidate rules are in `build/sources.md`; only the EU parameters are
here. Item numbers are those of the seed catalog in `PLAN.md` until `helpers/catalog.md`
exists.

Samples are English documents from companies that sell in the EU (`build/sources.md` rule 3). Run
R1 and R3 with an EU storefront in English (`cc=ie`); fetch from an EU location, or take the
EU version from the site's region switcher.

Items 35, 48 and 49 exist only under EU law and will be `eu` catalog items; the rest are `eu`
blocks of root items.

### Documents

| Items | Where | Expected pool |
|---|---|---|
| 1 privacy policy, `eu` block | Reuse the global pool's samples that carry EU content (`research/privacy-policy/merge.md`); add EU-based companies from R1/R3 `cc=ie` for the rest. | ≥30 |
| 13 data subject request, `eu` block | Reuse the global pool's samples that carry EU content (`research/data-subject-request/merge.md` *Regional content*): EU-based companies' own forms and OneTrust webforms behind privacy policies (R4); recipes for hosted portals in `research/data-subject-request/portal-probe.md`. | ~10 |
| 18 RoPA, `eu` block | The global pool's GDPR samples (`research/ropa/merge.md` *Regional content*); R10 Irish universities' data-protection pages ("high-level ROPA") and council FOI releases; R11 regulator models in English (CNIL, Finland's Data Protection Ombudsman, Cyprus's Commissioner, Ireland's DPC guidance layouts; Finland and Cyprus block fetching, use Wayback); association models for members (GAA). EU institutions' registers follow Reg. (EU) 2018/1725, not the GDPR. Companies never publish theirs. | <20 |
| 16 children's notice, `eu` block (GDPR Art. 8) | R1/R3 Kids category charts with `cc=ie`; keep notices that address parental consent under Art. 8. | ≥20 |
| 41 withdrawal notice, `eu` block | Checkout and terms pages of digital-content sellers in the EU. | ≥30 |
| 48 DSA notice-and-action and point of contact | R1–R4 at social and UGC apps. The list of VLOPs/VLOSEs: `digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses`; then smaller platforms' "DSA" pages via R4. | ≥30 |
| 49 DSA transparency report (decision 43) | The VLOPs' transparency reports: `digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency`; then smaller platforms' "DSA" pages via R4. | ≥20 |
| 56 AI disclosure, `eu` block | R4 at AI-feature apps that sell in the EU. Art. 50 applies from 2026-08-02. | ≥20 |
| 57 accessibility statement, `eu` block | R4 `/accessibility` at EU sellers. The EU model accessibility statement, (EU) 2018/1523, is a public-sector model; it counts as a regulator model (`build/sources.md` *Few public samples*). | ≥30 |

### Forms

| # | Form | Answers public per app | Where | source |
|---|---|---|---|---|
| 35 | DSA trader status, Apple | yes | EU storefront listing: "has identified itself as a trader", with address, phone and e-mail | sampled |
| 35 | DSA trader status, Google | no distinct label found; *About the developer* shows contact details | — | official |

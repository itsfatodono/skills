---
code: us
name: United States
laws:
  - California Consumer Privacy Act, as amended by the CPRA
  - the other US state comprehensive privacy laws
  - Children's Online Privacy Protection Act (COPPA) and the FTC COPPA Rule
  - DMCA § 512 (17 U.S.C. § 512)
languages: [en]
storefront: us
added: 2026-10-26
---

## Sources

Shared routes (R1–R12) and the candidate rules are in `build/sources.md`; only the US parameters are
here.

| Items | Where | Expected pool |
|---|---|---|
| 1 privacy policy, `us` block | Reuse the global pool's samples that carry US state content (`research/privacy-policy/merge.md`); add US companies whose footer has "Do Not Sell or Share" or "Your Privacy Choices". | ≥30 |
| 13 data subject request, `us` block | Reuse the global pool's samples that carry US state content (`research/data-subject-request/merge.md` *Regional content*); US companies' "CCPA request", "Your Privacy Choices" and privacy-portal forms linked from their privacy policies (R4), including OneTrust and Transcend portals (`research/data-subject-request/portal-probe.md`). | ≥14 |
| 16 children's notice, `us` block (COPPA) | R1/R3 Kids category charts with `cc=us`; members of the FTC COPPA Safe Harbor programs (`ftc.gov/enforcement/coppa-safe-harbor-program`), such as kidSAFE (`kidsafe.com/members`). | ≥30 |
| 47 copyright policy, `us` block (DMCA) | R1–R4 at social and UGC apps; the US Copyright Office DMCA agent directory (`dmca.copyright.gov/dmca/search.html`) lists services with a designated agent. | ≥30 |
| 56 AI disclosure, `us` block (state AI laws) | R4 at AI-feature apps that sell in the US. Candidate laws: Utah's AI disclosure law, California SB 942; check which are in force at build time. | ≥20 |

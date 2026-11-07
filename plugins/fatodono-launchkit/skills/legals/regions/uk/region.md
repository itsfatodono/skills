---
code: uk
name: United Kingdom
laws:
  - UK GDPR and the Data Protection Act 2018
languages: [en]
storefront: gb
added: 2026-10-26
---

## Sources

Shared routes (R1–R12) and the candidate rules are in `build/sources.md`; only the UK parameters are
here.

Run R1 and R3 with `cc=gb`. Most global samples write the UK together with the EEA; a UK block
counts only rows that name the UK, so add UK-based companies (R1/R3 `cc=gb`) when a block's
counts are too low to show patterns.

| Items | Where | Expected pool |
|---|---|---|
| 1 privacy policy, `uk` block | Reuse the global pool's samples that name the UK (`research/privacy-policy/merge.md`); add UK-based companies for the rest. | ≥30 |
| 13 data subject request, `uk` block | Reuse the global pool's UK samples (`research/data-subject-request/merge.md` *Regional content*); UK companies' "subject access request" pages and PDF forms (banks, telecoms, retailers) via R4. | ~10 |
| 18 RoPA, `uk` block | Reuse the global RoPA pool's UK samples (`research/ropa/merge.md` *Regional content*). R10: `"ROPA" site:ox.ac.uk` (colleges publish one file per area), council `RoPA` spreadsheets, fire and NHS registers (NHS Digital's GDPR register through the Wayback CDX index). R11: the ICO template only. No UK company publishes its record. | ~25 |
| 16 children's notice, `uk` block (Age Appropriate Design Code) | R1/R3 Kids category charts with `cc=gb`; keep notices that name the Children's Code. | ≥20 |
| 41 withdrawal notice, `uk` block (Consumer Contracts Regulations 2013) | Checkout and terms pages of digital-content sellers in the UK. | ≥30 |

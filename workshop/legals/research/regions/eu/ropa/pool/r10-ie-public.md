# ropa / eu / r10-ie-public

Slice: R10 public bodies in Ireland (non-university). Language: English. Collected 2026-10-26.

| Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
|---|---|---|---|---|---|---|

No rows kept. No Irish public body outside the universities and Wexford publishes an actual RoPA that search can reach.

## Searches run

- `"record of processing activities" council site:ie filetype:pdf`: only DPC guidance, UK councils.
- `"ROPA" site:gov.ie record of processing activities`: no gov.ie hits; university guides, EU bodies.
- `FOI disclosure log "record of processing activities" Ireland`: only generic disclosure-log pages (HSA, Tailte, Courts, Fáilte Ireland, FSAI); none mention a RoPA.
- `"Article 30" "record of processing" site:ie filetype:pdf`: DPC guidance only.
- `Wexford County Council record of processing activities FOI`: confirms FOI 16/25 (already in pool).
- `"records of processing" "legal basis" "retention period" ... site:ie`: Wexford FOI 16/25 and EU ELA records only.
- `HSE "record of processing activities" register publication scheme`: no Irish register.
- `"article 30" register of processing activities Tusla OR Revenue OR "Department of" site:ie`: DPC guidance, Tusla pointer.
- `Tusla "Record of Processing Activities" ...`: pages that mention a Tusla ROPA; the ROPA itself is not published.
- `council Ireland FOI response "RoPA" ... disclosure log pdf`: Wexford only; surfaced DFA FOI 19/212.
- `"Record of Processing Activities"` plus Dublin City, Cork, Fingal, Kerry, Galway, Limerick councils: nothing.
- `gov.ie FOI "Record of Processing Activities" department release ROPA spreadsheet`: DFA 19/212 only.
- ROPA + FOI + HSE / Údarás / Sport Ireland: HSE staff guidance pages only.
- ROPA + HSE hospital group / DPC / Central Bank / Revenue / Garda released under FOI: guidance and law-firm notes only.

## Skipped

- Wexford County Council FOI 16/25 (`wexfordcoco.ie/.../FOI 16 25 Combined.pdf`): already in the pool.
- DFA FOI 19/212 (`gov.ie/en/publication/77713-foi-request-19212/`): gov.ie page returns 403. The archived attachment (`assets.gov.ie/131389/2f7e4e13-...pdf`, Wayback 20241027182703) is a 1-page PDF with no text layer, so it is probably the decision letter. I could not confirm it holds record rows. A reviewer could re-check it by OCR. Not kept.
- HSE `healthservice.hse.ie/staff/procedures-guidelines/data-protection/record-of-processing-activities-ropa/` and `.../staff/benefits-services/benefits/record-of-processing-activity-ropa-.html`: guidance and procedure only, no rows. The RoPA template and central repository are not linked.
- Tusla (`register.openathens.net/tusla.ie/register`, gov.ie "Register of Users" page): they say a ROPA exists, but no record is published. The gov.ie page returns 403.
- DPC guidance note and web page (`dataprotection.ie`, April 2023): guidance, not a record.
- Wexford FOI privacy statement, Clare Co. Co. FOI privacy notice: privacy notices.
- UCG, UCD, TCD guides: universities, another collector; also guidance.
- European Labour Authority records (`ela.europa.eu/DPR-ELA-*`), CoR, SRB, EDPS: EU bodies under Reg. 2018/1725.
- UK councils, NHS, ICO, Pensions Regulator, Lincolnshire, Gloucestershire: not Ireland.
- Vendor and law-firm articles (learnsignal, openforest, Arthur Cox, Reed Smith, etc.): not records.

## Note for the build

Irish public bodies rarely publish RoPAs, and the FOI route gives sporadic one-off releases. A targeted request, or a search of individual council FOI response pages (as with Wexford), is the only likely source. A WebSearch tool limited to indexed pages will not reach them.

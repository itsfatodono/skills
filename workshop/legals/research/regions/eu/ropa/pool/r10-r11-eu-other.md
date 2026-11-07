# Pool slice r10-r11-eu-other (ropa, region eu, English)

Columns reused for non-app rows: App = body type, Store id = country code, Genre = format and scope, Ratings or downloads = headcount (blank, none visible).

| Company | App | Store id | Genre | Ratings or downloads | Document URL | Developer site |
|---|---|---|---|---|---|---|
| Office of the Data Protection Ombudsman (Tietosuojavaltuutetun toimisto) | regulator-model | FI | Blank xlsx template, controller's record (Art. 30(1)), English, one sample row (financial administration / payroll); a separate processor template is on the same page | | https://tietosuoja.fi/documents/6927448/8323207/Template+for+controllers+-+record+of+processing+activities.xlsx/696390cb-00ae-4780-884a-668d0f8dd655?t=1654165400828 (blocked) | https://tietosuoja.fi/en/controller-s-record-of-processing-activities (blocked) |
| Office of the Commissioner for Personal Data Protection (Cyprus) | regulator-model | CY | Blank xlsx template "Record of Activities Template ENG" (columns numbered to Art. 30) plus an English PDF guide v1.2; Greek twin exists | | https://www.dataprotection.gov.cy/dataprotection/dataprotection.nsf/ED1AAB60C3F3A93BC22582600037E15D/$file/Record%20of%20Activities%20Template%20ENG.xlsx (blocked) | https://www.dataprotection.gov.cy/dataprotection/dataprotection.nsf/page2d_en/page2d_en?opendocument (blocked) |
| Data Protection Commission (Ireland) | regulator-model | IE | PDF guidance note (Apr 2023) ending in worked layouts: Approach A and B (well-completed spreadsheet RoPA for a fictional "A Company Ltd"), Approach C (insufficient detail), plus a Table A of suggested detail; the layouts are images, text extraction gives only headings | | https://www.dataprotection.ie/sites/default/files/uploads/2023-04/Records%20of%20Processing%20Activities%20(RoPA)%20under%20Article%2030%20GDPR.pdf | https://www.dataprotection.ie/en/dpc-guidance/records-of-processing-article-30-guidance |

## Searches run

R10 (bodies publishing a filled RoPA): `"record of processing activities" university filetype:pdf -site:europa.eu -site:ac.uk` (operators ignored; UK/Irish results); `"register of processing activities" GDPR Article 30 English university`; `"processing register" university English GDPR faculty`; `"register of processing activities" site:nl`; Dutch university names (Wageningen, Utrecht, Leiden, Tilburg, Maastricht, Eindhoven) with `"register of processing activities"`; Nordic/Baltic university and institute queries (FI, SE, DK, EE, LV, LT); Belgium/Austria/Portugal/Poland/Italy university query; German `Verzeichnis von Verarbeitungstätigkeiten` English; company / NGO / foundation `"Article 30 GDPR"` and `"our record of processing activities"` queries; municipality / agency / foundation `"register of processing activities"`.
Result: the web search returned almost only the University of Groningen (already pooled), UK/Irish universities (out of scope), vendor templates and Article 30 text. No filled English record from another EU member state was found; R10 yielded 0 rows.

R11 (regulator models): EDPB SME guide (`/sme/find-practical-info/practical-resources-for-smes/<country>_en`, all 17 country pages fetched and scanned for RoPA links); searches for FI, DK, EE, LV, LT, HR, SI, CY, EL, CZ, HU, LU, MT, IE, SE, NL, AT, DE; domain-restricted searches on the DPA sites.

## Skipped (and why)

- CNIL, Wexford County Council, University of Groningen (and its unit pages, e.g. UCG, FEB, Library): already in pool.
- EU institutions, bodies, agencies (EDPS, FRA, ELA, EISMEA, ECA, EC DPO register): Reg. 2018/1725, excluded by the brief.
- Lithuania VDAI `Rekomend_tvarkymo_veiklos_irasu_2018.docx`: Lithuanian only (EDPB SME page lists it; the English items there are DPA clauses, not a RoPA).
- Croatia AZOP controller xlsx (`ARC-obrazac-Evidencija-aktivnosti-obrade.xlsx`) and processor docx: Croatian; no English version found.
- Denmark Datatilsynet `Eksempel på en fortegnelse ... HR.docx`: Danish; the site's English versions cover only the processor agreement and joint controller templates. Not a RoPA in English.
- Germany (LDI NRW, BayLDA `info_verfahrensverzeichnis.pdf`, DSK hints): German.
- Belgium DPA model: French and Dutch only (the OneTrust English copy is a vendor translation).
- Luxembourg CNPD: its page publishes no model of its own and points to FR, BE and Bavarian ones (a 2019 CNPD Excel model is mentioned by a law firm, not found on the site).
- Sweden IMY: English page holds checklists only, no template or example record.
- Spain AEPD: no RoPA template in the EDPB list (only a DPIA template in English).
- Estonia, Latvia, Slovenia, Czechia, Hungary, Greece, Malta, Netherlands, Austria, Portugal, Poland: no English RoPA model found (Malta and Slovenia not reachable through search; Estonia, Latvia, Czechia, Hungary, Greece, Netherlands, Austria not found).
- Spanish bodies with English wrapper pages and Spanish records: Universidad Complutense de Madrid (38 PDFs, Spanish), Consorci Zona Franca Barcelona (Spanish PDF), INCLIVA (Spanish PDFs), ANECA (Spanish PDF, 28 pp.). Same trap as the earlier Groningen/CJEU case, reversed.
- University of Obuda (HU) `2_2_4_nyilvantartasok_vezetese_engm.pdf`: English rules on the content of the register, not a record.
- TU Delft GDPR register page: describes the register in prose, the register itself is not public. VU Amsterdam: register behind login. HHU Duesseldorf: internal wiki. University of Twente `manual-register-of-processings`: manual, not a record. FU Berlin / HU Berlin / Oldenburg: guidance pages.
- Dutch municipalities' pre-filled register (VNG / IBD via privacy-web.nl): Dutch.
- Bitkom English guide on processing records (45 pp.): industry-association guidance with example records in section 5; guidance, not a record or a regulator model, left to the build branch to reconsider.
- Vendor and consultancy templates (Chino.io, Orbiq, Securityscientist, Advisera, PlanItPrima, ActiveMind, Strac, etc.): never samples.
- Non-EU: Norway (Datatilsynet / Digdir), UK ICO and councils, Jersey OIC, Brazil ANPD.
- Tried but unreachable: Cyprus and Finland pages return a bot wall / 403 to direct fetch; the file URLs above were found and the contents checked through Wayback copies (both English).

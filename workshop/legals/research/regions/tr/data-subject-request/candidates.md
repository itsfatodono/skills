---
doc_id: data-subject-request
region: tr
built: 2026-10-27
routes_run: [KAP/İSO 500/Fortune Türkiye 500 → R4, R1 cc=tr, R2 cc=tr]
raw_rows: ../kvkk-pool/pool/
---

Selected from the shared KVKK pool (`research/regions/tr/kvkk-pool/pool/`, PLAN.md decision 45),
using only the *Başvuru formu URL* column: 41 rows with a URL (`tr-apps` 23, `tr-large` 12,
`tr-tail` 6), 40 distinct companies (ING is in both `tr-apps` and `tr-large`). The Emlaksitem
row in `tr-tail` has an unescaped `|` in its app name, so its columns shift and the
Açık rıza URL appears in the Başvuru formu column. It has no form URL and is not a candidate,
which leaves 40 rows and 39 companies. Decision 46's 7499 cut-off does not apply here (KVKK
Arts. 11 and 13 were not amended), so no date test was run. Dates are recorded where they show.
Size is an estimate per `sources.md`. Rows 1–24 are the pool; rows 25+ are the reserve, used in
order when a candidate is invalid. Rows 1–15 are the first batch, 5 per size.

**First-screen check** (fetched 2026-10-27). Every URL returned 200. Each file was opened to
confirm it is the controller's own Art. 11/13 application form (or, for HTML, a page that is the
form), not a notice or another kind of application. *Format* gives the file type. *Fam* tags
suspected shared templates (rule 4), found by 6-word shingle overlap (containment over the
smaller text) between the kept texts:
- **T1** "GENEL AÇIKLAMALAR … veya bu kişilerin yasal temsilcilerine (“Başvuru Sahibi” veya
  “İlgili Kişi”)": Penti, Midas Kripto, Starbucks (0.56–0.79). Midas's Kognivia form also
  belongs to this family.
- **T2** "1. Başvuru Yöntemi … Tebliğ’in 5. maddesi gereğince, işbu form ile" plus the
  three-column method table: Vestel, evital, Pluxee, Opet, Koton, Fırsat (0.30–0.56).
- **T3** "GENEL AÇIKLAMALAR … (Bundan sonra “Başvuru Sahibi” olarak anılacaktır)":
  Pamukkale, TürkKEP, Multinet (0.35–0.47). Etstur and IKEA open the same way.
- **T4** Macrocenter (DPG) and IKEA (0.63).

No two companies from different groups share the whole text: the highest cross-group overlap is
0.79 (Penti and Midas Kripto). So every row stays a sample, and the merge decides copies. Beymen
and Network (Boyner) share 0.94, but they are one group.

**Shortfall.** Pool: 10 large, 8 mid, 6 small (24). Reserve: 7 large, 0 mid, 0 small.
- **Mid is short by 2.** The pool has only 8 mid companies with a form URL, and all 8 are
  picks. Most mid rows in the shared pool (Lufian, BKM Kitap, arabam.com, Paribu, UPTION and
  others) have no Başvuru formu URL.
- **Small is short by 4.** `tr-apps` gives 4 small rows and `tr-tail` gives 5. Three `tr-tail`
  URLs were not KVKK forms (see the drops), so 6 small rows remain. The tail slice was collected
  for notices, and small developers rarely publish a separate form; the slice header does not
  say whether form links were looked for on every site.
- If a mid or small pick turns out invalid, that third gets shorter.

**Drops at the first screen** (6):
- Not a KVKK application form, only a sign-up form that shares the word *başvuru* (3):
  Kursum (`kursum.app/basvuru/`, course-sales lead form), Kiovita (`/basvuru`, trainer/gym
  account application), Rezzim (`/salonunu-ekle/basvuru`, salon sign-up).
- Not the company's own form (1): Midas, whose URL is the Kognivia Yazılım A.Ş. form. Midas
  Kripto's own form is kept.
- Wrong company (1): Pegasus. `pegasus.com.tr` is Pegasus Denizcilik A.Ş., not the airline;
  the notice run dropped it for the same reason.
- Group rule (1, see below): AgeSA.

**Group rule** (candidate rule 5), left out before the check: Pierre Cardin (Aydınlı, with
U.S. Polo Assn.). Both pages link the same Aydınlı PDF, so the group is one row: U.S. Polo is
the pick and the PDF is the sample. Network (Boyner, with Beymen). Midas and Midas Kripto are
one group; Midas Kripto is kept. AgeSA (Sabancı, with Akbank). ING's two rows are one company.

**Notes.**
- U.S. Polo's URL is a help page whose only content is a download link. The sample is the
  linked Aydınlı PDF
  (`https://25d163.a-cdn.akinoncloud.com/cms/2024/03/22/e817eccc-43ed-4da8-af7c-91c777381c35.pdf`,
  rule 6).
- ING's URL is a page with a rights summary that links the PDF form
  (`https://www.ing.com.tr/F/Documents/pdf/Hakkimizda/Site_Basvuru_Formu_060722_.pdf`).
  Extract the page and the PDF together.
- getirfinans: the form is an HTML help page that follows a cookie banner.
- Honda's PDF (an Illustrator export, file dated 2020, PDF created 2023-10-03) has no usable
  text layer. It was read with OCR (`pdftoppm` and `tesseract -l tur`), and extraction must do
  the same.
- The first scripted download of Honda and Midas Kripto came back truncated. Fetch them again
  in full (744,815 and 235,263 bytes).
- AgeSA's URL redirects to `agesa.com.tr`.
- VakıfBank's URL redirects to `vbassets.vakifbank.com.tr`. Its form keeps a `[•]` placeholder
  ("[•] adresinde yer alan Başvuru formu"), a leftover from a drafting template.
- Campaign's page is a procedure page with a sample request letter ("Örnek başvuru şablonu"),
  not a form with fields. It is kept as the form under rule 6.
- 6 Tekrar (2026-09-27), Ortak Market (2026-09-27) and Campaign (2026-09-05) are recent HTML
  pages by small developers with a similar outline ("Başvuru yolları", fee and complaint-period
  paragraphs). Their shingle overlap is below 0.25, so they are not flagged as copies.
- Dates shown: TürkKEP form FRM-058 Rev. 01.0, 25.12.2020; Multinet 09.06.2026; ING file name
  060722; Fırsat 29 Ağustos 2026.
- Vestel's form is headed "Vestel Grup Şirketleri" and covers the whole group.
- Macrocenter's form is issued by Dijital Platform Gıda Hizmetleri A.Ş. (Migros).

Sector: the App Store primary category of the main app; `e-commerce` for a shop without an app
in the pool. The sector cap of a pre-built run does not apply to a region run.

| # | Company | App (store id) | URL | Sector | Format | Fam | Size | Base | Language | Route |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Flo Mağazacılık ve Pazarlama A.Ş. | FLO AYAKKABI (889027386) | https://floimages.mncdn.com/media/import/pdf/23-10/09/flo_ilgilikisi_basvuruformu_v4.pdf | shopping | pdf | - | large | TR | tr | R1 |
| 2 | Eczacıbaşı Evital Sağlık Hizmetleri ve Tic. A.Ş. | evital (1631884007) | https://img-evital.mncdn.com/evital/assets/files/Evital_Veri_Basvuru_Formu.pdf | health-fitness | pdf | T2 | mid | TR | tr | R1 |
| 3 | Fırsat Yapay Zeka Teknolojileri A.Ş. | Fırsat (6795664118) | https://firsat.com/ilgili-kisi-basvuru-formu | shopping | html | T2 | small | TR | tr | R1 |
| 4 | ING Bank A.Ş. | ING Mobil (395535459) | https://www.ing.com.tr/tr/ing/kisisel-verilerin-korunmasi/ilgili-kisi-basvuru-formu (+ linked pdf) | finance | html + pdf | - | large | TR | tr | KAP/R4 |
| 5 | Multinet Kurumsal Hizmetler A.Ş. | MultiPay (680381668) | https://multinet.com.tr/sites/default/files/static/multinet-kvkk-basvuru-formu_1.pdf | finance | pdf | T3 | mid | TR | tr | R1 |
| 6 | Mahir Baran Aydoğan (6 Tekrar) | 6 Tekrar (6816790796) | https://6tekrar.com/yasal/ilgili-kisi-basvuru-formu | health-fitness | html | - | small | TR | tr | R1 |
| 7 | Shaya Kahve San. ve Tic. A.Ş. (Starbucks Türkiye) | - | https://media.sbuxtr.com/files/g7r5gvep/shaya-kahve-ilgili-kisi-basvuru-formu.pdf | food-drink | pdf | T1 | large | TR | tr | KAP/R4 |
| 8 | Honda Türkiye A.Ş. | Honda Yanımda (6743437540) | https://honda.com.tr/assets/files/HondaBasvuruFormu2020.pdf | lifestyle | pdf (OCR) | - | mid | TR | tr | R1 |
| 9 | This Is A Company Teknoloji Gelişim ve Yatırım A.Ş. | Frink (1538561803) | https://frink.com.tr/tr/kvkk-basvuru-formu | food-drink | html | - | small | TR | tr | R1 |
| 10 | Mars Spor Kulübü ve Tesisleri İşletmeciliği A.Ş. (MACFit) | MAC+ (1573778936) | https://www.macfit.com/wp-content/uploads/2025/04/KVKK-Basvuru-Formu.pdf | health-fitness | pdf | - | large | TR | tr | R1 |
| 11 | TürkKEP Kayıtlı Elektronik Posta Hizmetleri A.Ş. | TÜRKKEP Mobil KEP (6451191619) | https://turkkep.com.tr/wp-content/uploads/2020/12/FRM-058-Veri-Sahibi-Basvuru-Formu.pdf | productivity | pdf | T3 | mid | TR | tr | R1 |
| 12 | Ekin Hazal Altıparmak (Look Bubble Teknoloji) | Look Bubble (6749798052) | https://lookbubble.com/kvkk-basvuru-formu/ | lifestyle | html | - | small | TR | tr | R2 |
| 13 | Ets Ersoy Turistik Servisleri A.Ş. | Etstur (882198456) | https://images.etstur.com/files/images/site/images/politikalar/kvkk-basvuru-formu.pdf | travel | pdf | - | large | TR | tr | R1 |
| 14 | Gedik Yatırım Menkul Değerler A.Ş. | Gedik Trader (1116732065) | https://cdn.gedik.com/media/media/vxahm3i2/kvkk-verisahibibasvuruformu.pdf | finance | pdf | - | mid | TR | tr | R1 |
| 15 | Ortakmarket Reklam Pazarlama ve Tic. Ltd. Şti. | Ortak Market (6739862539) | https://ortakmarket.com/kvkk-basvuru-formu | business | html | - | small | TR | tr | R2 |
| 16 | Aydınlı Hazır Giyim San. ve Tic. A.Ş. (U.S. Polo Assn.) | U.S. Polo Assn. (788605532) | https://tr.uspoloassn.com/ilgili-kisi-basvuru-formu/ (→ linked pdf) | shopping | pdf | - | large | TR | tr | R1 |
| 17 | Pluxee Çalışan Deneyimi Danışmanlık ve Paz. Hiz. A.Ş. | Pluxee Türkiye (1557840411) | https://www.pluxee.com.tr/sites/g/files/jclxxe426/files/2025-08/Pluxee_ilgili_kisi_basvuru_formu.pdf | food-drink | pdf | T2 | mid | TR | tr | R1 |
| 18 | Mehmet Fatih Yaşar (Campaign) | Campaign – Deal Tracker (6811686857) | https://campaignapp.tech/kvkk-basvuru/ | shopping | html | - | small | TR | tr | R1 |
| 19 | Akbank T.A.Ş. | - | https://www.akbank.com/Documents/Sozlesmeler/Akbank_Veri_Sahibi_Basvuru_Formu.pdf | finance | pdf | - | large | TR | tr | KAP/R4 |
| 20 | Midas Kripto Varlık Alım Satım Platformu A.Ş. | Midas Kripto (6505027440) | https://www.midaskripto.com/wp-content/uploads/2025/09/ILGILI-KISI-BASVURU-FORMU.pdf | finance | pdf | T1 | mid | TR | tr | R1 |
| 21 | Opet Petrolcülük A.Ş. | Opet Mobil (390624881) | https://opetwebcdn.azureedge.net/medium/document-file-14.vsf | lifestyle | pdf (.vsf) | T2 | large | TR | tr | R1 |
| 22 | Matriks Finansal Teknolojiler A.Ş. | Matriks Mobil IQ (1446245060) | https://www.matriksdata.com/website/uploads/docs/basvuru-formu.pdf | finance | pdf | - | mid | TR | tr | R1 |
| 23 | Pamukkale Ulaşım Seyahat ve Turizm Hiz. A.Ş. | Pamukkale (1029824276) | https://www.pamukkale.com.tr/uploads/verisahibibasvuruformu.docx | travel | docx | T3 | large | TR | tr | R1 |
| 24 | Getir Teknolojik Hizmetler A.Ş. | getirfinans (6758653941) | https://www.getirfinans.com/yardim/ilgili-kisi-basvuru-formu/ | finance | html | - | large | TR | tr | R1 |
| 25 | Beymen Perakende ve Tekstil Yatırımları A.Ş. | - | https://img-agency-pdf.mncdn.com/pdf/Beymen_Ilgili_Kisi_Basvuru_Formu.pdf | e-commerce | pdf | - | large | TR | tr | KAP/R4 |
| 26 | Vestel (Vestel Grup Şirketleri) | - | https://statik.vestel.com.tr/webfiles/veri-sahibi-basvuru-formu.pdf | e-commerce | pdf | T2 | large | TR | tr | KAP/R4 |
| 27 | MAPA Mobilya ve Aksesuar Paz. A.Ş. (IKEA Türkiye) | - | https://cdn.ikea.com.tr/kvk/IKEA-Veri-Sahibi-Basvuru-Formu.pdf | e-commerce | pdf | T4 | large | TR | tr | KAP/R4 |
| 28 | Koton Mağazacılık Tekstil San. ve Tic. A.Ş. | - | https://koton.mncdn.com/static/KotonVeriSahibiBasvuruFormuCEBTS.pdf | e-commerce | pdf | T2 | large | TR | tr | KAP/R4 |
| 29 | Dijital Platform Gıda Hizmetleri A.Ş. (Macrocenter) | - | https://images.migrosone.com/misc/dpg-kvkk-form.pdf | e-commerce | pdf | T4 | large | TR | tr | KAP/R4 |
| 30 | Penti Giyim Tic. A.Ş. | - | https://file-penti.mncdn.com/pentimedias/ilgilikisi.pdf | e-commerce | pdf | T1 | large | TR | tr | KAP/R4 |
| 31 | Türkiye Vakıflar Bankası T.A.O. | - | https://www.vakifbank.com.tr/documents/bankamiz/kisisel-veri-sahibi-basvuru-formu.pdf | finance | pdf | - | large | TR | tr | KAP/R4 |

# ropa / tr: public bodies and standard forms (pool slice)

Collected 2026-10-26. Every URL below was opened (HTTP 200, file type and fields checked). Nothing judged beyond the keep rule.

## Rows

| Body | Kind (ministry/municipality/hospital/chamber/model...) | Document URL | Format | Rows or activities (approx.) | Notes |
|---|---|---|---|---|---|
| KVKK Kurumu (Kişisel Verileri Koruma Kurumu) | model (regulator; sector `standard-form`) | https://kvkk.gov.tr/SharedFolderServer/CMSFiles/b5fe209d-3c12-4c70-8dac-a2eaa5742ae6.xlsx (sample inventory); guide: https://kvkk.gov.tr/SharedFolderServer/CMSFiles/224af10e-ff71-4cc9-9e18-c6c142f8da05.pdf ; announcement hub: https://www.kvkk.gov.tr/Icerik/5445/Kisisel-Veri-Isleme-Envanteri-Hazirlama-Rehberi-Kurum-Internet-Sayfasinda-Yayinlanmistir | xlsx + pdf (15 pp.) | 46 filled rows (sheet "Envanter örneği", 14 columns) | One row for the regulator. Columns: Departman, Faaliyet, Veri Kategorisi, Kişisel Veri, Özel Nitelikli, İşleme Amacı, Veri Konusu Kişi Grubu, Hukuki Sebebi, Saklama Süresi, Alıcı Grupları, Yabancı Ülkelere Aktarılan Veriler, İdari Tedbirler, Teknik Tedbirler. Guide dated April 2019 (announced 19 June 2019). The VERBİS Kılavuzu (KVKK Yayınları No: 112, Oct 2025) is a screen-by-screen guide, not an inventory; no kvkk.gov.tr PDF link was reachable (the Rehberler page is JS-driven), only a mirror at https://www.alomaliye.com/wp-content/uploads/2026/05/veri-sorumlulari-sicil-bilgi-sistemi-kilavuz.pdf (not the issuer's domain, not opened). |
| Türk Psikiyatri Derneği (member guide, likely derived from the TTB/health-sector VERBİS guidance) | model (professional body; sector `standard-form`) | https://psikiyatri.org.tr/TPDData/Uploads/files/Ek-D-VERBIS_Kayit_Kilavuzu.pdf | pdf (34 pp., 12 MB, screenshot-heavy) | VERBİS registration form walked through screen by screen | "Ek-D VERBİS Kayıt Kılavuzu": model VERBİS entry for practising psychiatrists with suggested purposes ("Diğer: sağlık hizmeti sunulması…"), recipient groups (SGK, özel sigorta, serbest muhasebeci/mali müşavir), 20-year retention for patient health data, subject groups ("Hastalar"), transfer-abroad advice. A guide with recommended entries, not a filled grid. Mostly images, so text extraction is partial. |
| Türk Tabipleri Birliği (TTB) | model (professional body; sector `standard-form`) | https://www.ttb.org.tr/userfiles/files/verbis_son(1).pdf | pdf (17 pp.) | field list only | "VERBİS'e kayıt işlemleri ve süreç basamakları": section I states the 7 minimum inventory items with the VERBİS data-category breakdown, says form is free (table or prose), and points to KVKK's sample. No filled grid. Marginal: keep only if fields-only models are accepted. |
| Lüleburgaz Belediyesi | municipality (sector `public-sector`) | https://luleburgaz.bel.tr/sayfa/kisisel-verielri-koruma-saklama-ve-imha-politikasi | html page (policy with embedded tables) | six tables, 22 to 154 rows each: Tablo-3 subject group x category x personal data; Tablo-4 activity x subject group x category x domestic/foreign recipient groups; Tablo-6 activity x retention x destruction time | Partial inventory inside a Saklama ve İmha Politikası. No legal ground or security-measure columns. This was the only municipal page found whose process-level tables together approach an inventory. Borderline: it is a policy page, not a standalone inventory. |

## Not samples

| URL | Why |
|---|---|
| https://www.turmob.org.tr/Commons/FileContent/5b1f37a5-635f-4b90-bc96-6b3b2bffee66/Icerik and https://turmob.org.tr/ekutuphane/Read/f870d4a7-9ce1-4ee0-9cdc-152c30db696c | TÜRMOB VERBİS information notes (5 and 4 pp.), no inventory or fields grid. |
| https://www.turmob.org.tr/arsiv/kvkk/1_TURMOB_Kisisel_Veri_Saklama_ve_Imha_Politikasi.pdf and the other `arsiv/kvkk/*` files (aydınlatma beyanları, başvuru formu) | TÜRMOB's published KVKK set has no inventory. Policy and notices only. |
| https://www.amasra.bel.tr/download/kvkk/kvkk_politika.pdf | Municipal policy that mentions the inventory (section 5), no inventory table. |
| https://www.sehitkamil.bel.tr/Duyurular/detay/kisisel_veri_saklama_ve_imha_politikasi1650521675, https://kvkk.tavas.bel.tr/index.php?slug=kisisel-veri-saklama-ve-imha-politikasi, https://www.hemsin.bel.tr/sayfa/saklama-ve-imha-politikasi.html, https://www.beylikduzu.istanbul/content/media/Uploads/kvkk/POL-02 (and POL-03) | Municipal retention/destruction or processing policies; the recipient-group and retention words occur only in definitions or a retention table, no activity x subject x recipient grid. |
| https://mapeg.gov.tr/Uploads/KVKK/Ki%C5%9Fisel%20Veri%20Saklama%20ve%20%C4%B0mha%20Politikas%C4%B1.pdf, https://www.tpic.gov.tr/uploads/corporate/p_f5e1b486-389b-4fe8-a620-41a9056362e3.pdf, https://www.toki.gov.tr/AppResources/UserFiles/files/Ki%C5%9Fisel%20Verileri%20Saklama%20ve%20%C4%B0mha%20Politikas%C4%B1.pdf, https://kvkk.ktb.gov.tr/Eklenti/142768,veri-saklama-ve-imha-politikasi-2025pdf.pdf, PTT, KVKK's own https://www.kvkk.gov.tr/SharedFolderServer/CMSFiles/9d528504-e3df-4934-ad7b-bf93fda8ea82.pdf | Public-body Saklama ve İmha Politikası files. MAPEG and TPIC have process x retention tables only (no purposes, legal ground, subjects, recipients). TPIC and MAPEG refer to a separate "KVK Komisyonu ve Envanter Sorumluları" annex that is not published. |
| https://geka.gov.tr/uploads/pages_v/ozelnitverisl.pdf | Güney Ege Kalkınma Ajansı special-category data policy, no inventory. |
| https://www.cankaya.bel.tr/uploads/documents/cankayakvkk2025_1760353634_HqZzOVgB.pdf | Mobile-app privacy policy and contract. |
| https://www.istabip.org.tr/6410-veri-envanteri-neleri-icermelidir.html | Chamber article explaining inventory contents, no sample. |
| https://ismmmo.org.tr/dosya/3008/Egitim-Dosya/kvkksunum.pdf, https://bilgiguvenligi.marmara.edu.tr/dosya/bilgiguvenligi/Duyurular/2023/KisiselVeriEnvanteriHazirlamaSunumu.pdf, https://kvkk.metu.edu.tr/sites/kvkk.metu.edu.tr/files/kvkk_envanter_cozumu_detay_sunum.pdf | Training slide decks (SMMM chamber and universities; universities belong to another slice). |
| https://envanter.kaysis.gov.tr/?Kurum=80228899 (also ?kurum=24308261) | KAYSİS, a different "envanter" (public service inventory). |
| https://www.konya.bel.tr/k/hizmet-envanteri, https://www.mersin.bel.tr/dokumanlar/mbb-hizmet-standardi-ve-envanteri, https://www.kayseri.bel.tr/kamu-hizmet-envanteri-tablolari | Hizmet envanteri (service standards), unrelated to KVKK. |
| https://www.ktun.edu.tr/Dosyalar/1070/files/Bgys/Prosed%C3%BCrler/Kritik%20Veri%20Envanteri%20Y%C3%B6netimi%20Prosed%C3%BCr%C3%BC.pdf | University IT-asset ("kritik veri") inventory procedure, not a KVKK inventory. |
| https://www.verbis.kvkk.gov.tr query-detail links (e.g. verbis.kvkk.gov.tr/Query/Details?q=...) | Public VERBİS query returns an error page without the captcha session; no body summary could be fetched by script. |
| mihci.av.tr, harbiyehukuk.com, ffkpartnerhukuk.com.tr, cottgroup.com, imer.av.tr (verbis-bildirim-taslagi), lawinsider.com/tr, nesilteknoloji.com, verikasifi.com, denetci.org-style consultancy and template pages | Law-firm articles, consultancy blogs, template/tool sellers. |
| https://kvk.barobirlik.org.tr/ (TBB KVK komisyonu), https://www.barobirlik.org.tr/kvkihlalformu | TBB site: commission yönerge and breach form, no inventory. The KVKK-TBB lawyers' guide (Sept 2026, 158 pp.) did not surface as a file and no inventory was reported in its summaries. |

## Searches run

WebSearch (the engine ignores `site:` operators; `allowed_domains` used instead, and returned mostly policies and law-firm pages):
- `"kişisel veri işleme envanteri" site:gov.tr`; same with allowed_domains gov.tr, bel.tr, org.tr
- `"veri envanteri" site:bel.tr` (zero bel.tr hits); `kişisel veri işleme envanteri` with allowed_domains bel.tr (only policies)
- `"azami saklama süresi" "veri kategorisi" "ilgili kişi grubu" envanter pdf`; `"Veri Konusu Kişi Grubu" "Hukuki Sebebi" "Saklama Süresi" "Alıcı Grupları" envanter belediye…`
- `"Kişisel Veri İşleme Envanteri" filetype:xlsx`; `"Kişisel Veri Envanteri" "Yabancı Ülkelere Aktarılan" filetype:pdf`
- `kişisel veri envanteri xlsx belediye kvkk "alıcı grubu"`; `"Aktarımı Yapılan Kişisel Verilerin Süreçler Bazında Alıcı/Alıcı Grupları" belediye`
- `"Süreç Bazında Saklama ve İmha Süreleri" …`; hospital, kalkınma ajansı, ticaret odası/baro, "VERBİS kayıt özeti" variants
- Part B: KVKK Rehberi; VERBİS Kılavuzu; TOBB, TBB, Eczacılar, TTB, Diş Hekimleri, Noterler Birliği, TÜSİAD variants
- Only KVKK Kurumu, Psikiyatri Derneği, TTB and Lüleburgaz produced usable hits.

curl crawls (`curl -sL -A "Mozilla/5.0"`; homepage, KVKK-looking links, then links containing "envanter" or pdf/xlsx with veri/kvkk in the name), none yielded an inventory:
- municipalities: ibb.istanbul, ankara, izmir, bursa (empty response), antalya, konya, kocaeli, bolu, gaziantep, mersin, beylikdüzü, kadıköy, beşiktaş, şişli, üsküdar, maltepe, çankaya, yenimahalle, nilüfer, muratpaşa, karşıyaka, bornova, tepebaşı, kayseri, samsun, trabzon, eskişehir, denizli
- bodies: kvkk.gov.tr (Rehberler and Diğer Dokümanlar pages, 17 PDFs checked for "envanter"), turmob, tobb, barobirlik, ttb, istabip, istanbulbarosu, ankarabarosu, ito, iso, ika, istka, ankaraka, tusiad, kosgeb, saglik.gov.tr, meb.gov.tr, sgk, gib, btk, tcmb, spk, ticaret.gov.tr, csb.gov.tr (eczacilar.org.tr returned empty)
- DuckDuckGo/Bing scraping was blocked.

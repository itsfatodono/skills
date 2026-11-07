# ropa / tr / pool: Turkish universities (*.edu.tr)

Run 2026-10-26. Result: 0 rows. No university published a filled Kişisel Veri İşleme Envanteri or a VERBİS summary on its own domain. VERBİS itself (`verbis.kvkk.gov.tr`) sits behind a captcha and is not an `*.edu.tr` page.

| Institution | Kind (state/foundation university) | Document URL | Format (pdf/xlsx/html/docx) | Rows or activities (approx.) | Notes |
|---|---|---|---|---|---|
| (none) | | | | | |

## Not samples

- Ankara Üniversitesi: `kvkk.ankara.edu.tr/2021/09/17/universitemizin-kisisel-veri-isleme-envanteri-tamamlandi/` and the 2021-12-30 VERBİS post are announcements only; no inventory file or table is linked.
- Bingöl Üniversitesi: `kisiselveri.bingol.edu.tr` is the "Kişisel Veri İşleme Envanteri Uygulaması", behind a corporate e-mail login; the inventory is not public.
- Marmara Üniversitesi: `kvknet.marmara.edu.tr` (Kişisel Veri Envanter Yönetim Sistemi) is an internal system; `bilgiguvenligi.marmara.edu.tr/.../KisiselVeriEnvanteriHazirlamaSunumu.pdf` and the 2021 "KV Envanter Eğitimi" PDF are training decks with a sample inventory.
- Kastamonu Üniversitesi: `kvkk.kastamonu.edu.tr` "Kişisel Veri Envanteri Nedir?" (id=289) explains the inventory headings; `KVKK-CZG-001 Kisisel Verileri Saklama Surelerini Gosteriri Cizelge.pdf` is a retention schedule, and `KVKK-PO-002` a retention and destruction policy.
- Fırat Üniversitesi: `kvkk.firat.edu.tr` news items on "Veri Envanteri Oluşturma" meetings and portal training; no inventory published.
- Bartın Üniversitesi: `kvkk.bartin.edu.tr/rehberler.html` links the KVKK Authority's guide only.
- Hacettepe, Niğde Ömer Halisdemir, Atatürk, Gaziantep İslam Bilim ve Teknoloji, Boğaziçi, Koç, TED, Ağrı, Özyeğin, Malatya Turgut Özal: Saklama ve İmha Politikası or Kişisel Verilerin Korunması Politikası PDFs. They mention the inventory (some with a per-category retention table) but are policies, excluded by the brief.
- ODTÜ (`kvkk.metu.edu.tr`): per-process aydınlatma PDFs (`.../aydinlatma_metinleri/...`) and a FAQ docx; notices, not an inventory.
- Eskişehir Osmangazi, Muğla, Pamukkale, Mersin, Gaziantep/others: `*/kvkk` pages and "Hizmet Envanteri" (Kamu Hizmet Envanteri) pages are service inventories, unrelated to KVKK.
- Bilkent (`w3.bilkent.edu.tr/.../KVKK_Politikasi.pdf`, aydınlatma metni), Yeditepe (gizlilik politikası mentions a "Veri Envanteri"), Medipol, Gedik (aydınlatma metni): policy or notice texts only.
- KVKK Authority "Kişisel Veri İşleme Envanteri Hazırlama Rehberi" (kvkk.gov.tr) and any "örnek envanter" copies: guide, not a university's own.
- Hosts that answered 200 but showed no inventory, VERBİS or document links on the KVKK page or the first 80 same-site links: Akdeniz, Atatürk (`kvkk.atauni.edu.tr`; `veri.atauni.edu.tr` did not resolve), DEÜ, Ege, OMÜ, Sakarya, Muğla, Pamukkale, `subu.edu.tr` (Sakarya Uygulamalı Bilimler), Niğde, Özyeğin, Çankaya, Tokat Gaziosmanpaşa (`gop`), KTÜN, Mersin, Cumhuriyet, Ardahan, Boğaziçi, Kocaeli, İstanbul.

## Searches run

- `"kişisel veri işleme envanteri" site:edu.tr filetype:pdf`
- `"ilgili kişi grubu" "alıcı grubu" "azami saklama süresi" envanter site:edu.tr`
- `üniversitesi "veri envanteri" xlsx "veri kategorisi" "hukuki sebep" kvkk site:edu.tr`
- `üniversitesi "Kişisel Veri İşleme Envanteri" "Veri Kategorisi" "Aktarılan Alıcı Grubu" "Saklama Süresi" birim tablosu`
- `üniversite "VERBİS" kayıt özeti "ilgili kişi grupları" "kişisel veri kategorileri" "veri aktarılan alıcı grupları" edu.tr`
- `"veri işleme envanteri" ... "yurt dışına aktarım" fakültesi dekanlığı pdf`
- `"Kişisel Veri Envanteri" üniversite birim "süreç" "veri sahibi grubu" ... xlsx OR pdf`
- `Bilkent OR Sabancı OR Koç OR Bahçeşehir OR Başkent OR Atılım ... envanteri yayımlandı`
- curl probes of `kvkk.<uni>.edu.tr` and `www.<uni>.edu.tr/kvkk` for about 60 universities (about 45 answered 200), then a same-site crawl (80 links per site) of 28 KVKK sites grepping for "envanter" and "verbis".

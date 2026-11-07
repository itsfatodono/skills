---
doc_id: tr-explicit-consent
region: tr
built: 2026-10-27
routes_run: [KAP/İSO 500/Fortune Türkiye 500 → R4, R1 cc=tr, R2 cc=tr, footer/web search "açık rıza metni" → R4]
raw_rows: ../kvkk-pool/pool/
---

Selected from the shared KVKK pool (`research/regions/tr/kvkk-pool/pool/`, PLAN.md decision 45): the
*Açık rıza URL* column of `tr-apps` (9 companies), `tr-large` (7 more; Rossmann is in both) and
`tr-tail` (12), and every row of `tr-consent` (40), so 68 distinct companies. No other column was
used. Size is an estimate per `sources.md`. Rows 1–28 are the pool; rows 29+ are the reserve, used
in order of size when a candidate is invalid. Rows 1–15 are the first batch, 5 per size. Large runs
short (below), so rows 16–28 hold the last 3 large rows and the other mid and small rows.

**Decision 46 does not apply to this item** (PLAN.md decision 46, revised 2026-10-27): neither the
7499 cut-off nor the Art. 6 check is used, so no text is dropped for its date, its transfer
section or a special-category consent. An earlier selection the same day applied them and dropped
34 texts; all 34 are back in the pool. The first-screen check (fetched 2026-10-27) only confirms
that each page is a consent text for customers or users.

*Tags.*
- `transfer-consent`: the text asks consent for transfer abroad (Art. 9). The tag is set so the
  merge's decision-47 check can find these texts; consent used for regular transfers goes to
  *Avoid* there. A text that only names other Art. 9 tools, or a basis other than consent (Carell,
  Gökova Sigorta, Kullanat), or lists the right to know foreign recipients, is not tagged.
- `etk`: a commercial-message (6563 ticari elektronik ileti) consent text, item 51's subject. The
  pool's `(etk)` rows are tagged, and so are untagged rows whose text is mainly an ETK permission
  (Tekzen, Supplementler, Hemington). At most 3 may be in the pool. Rows 1–27 hold 2 (Tekzen,
  Bauhaus, both large, where the third runs short); mid and small fill with untagged texts. An
  `etk` pick is replaced only by an `etk` reserve, or by an untagged one.
- `inline`: no row in the pool is a signup-form text, so none is tagged.

Quality was not filtered (decision 47 is checked at the merge). For example, RandevuBak's text
calls its processing contractual under a consent title, Butika makes its transfer consent a
condition of service, and the clinic texts ask consent for treatment data. All of them stay.

**Shortfall.** Large: 8 of 10, no reserve. The pool has 10 large companies with an Açık rıza URL.
Karaca's page shows no text (script-rendered; the consent text is not in the HTML). Tuğba (tugba.com, a modest-wear brand) is estimated mid. Mid: 10 of 10,
reserve 7. Small: 10 of 10, reserve 28.

**Drops at the first screen** (5 companies):
- Page shows no text (3): Karaca (script-rendered), Parolapara (empty page, no Wayback capture),
  TAKITAK (empty page, no Wayback capture).
- Not a customer/user consent text (2): Cubicl (a çalışan adayı text at the explicit-consent link),
  Bluemint (an ETK notice with no consent wording).

**Group rule** (candidate rule 5): no two of the 63 texts come from one group. Rule 5 targets
companies whose texts come from one legal team. Ziraat Bankası and VakıfBank are both under the
Türkiye Varlık Fonu but are run separately, so they are not one group (chief-of-staff call,
2026-10-27). VakıfBank was added as row 22 after rows 1–15 went to extraction, and the rows after
it moved down by one. Their 6-word shingle overlap is under 15%.

**Copies** (rule 4, 6-word shingles over the 63 texts): no whole-text copies. Partial overlaps,
which stay separate samples and add their shared wording to patterns once:
- TürkKEP and Tuzcular Sigorta share 53% of Tuzcular's text (one KVKK iletişim consent template).
- Gedik and Emlaksitem share 53% of Gedik's text.
- Tekzen and E-Ticaret360 share 48% of Tekzen's text (one ETK paragraph).
- Adana Diş Hekimi and Uzman Diş Grup share 27% (one clinic template).

**Notes.**
- Emaa Sigorta's URL is a hub of six PDF consent forms, one per policy line. The general *Ürün veya
  Hizmet Alan Kişi Açık Rıza Metni* was taken (rule 6).
- Gedik's host refused connections, so the Wayback capture of 2026-06-18 was used
  (`http://web.archive.org/web/20260618085400/https://sozlesme.gedik.com/doc/acik_riza_beyani.htm`).
  Its text is an investor-prospect marketing consent that cites a "Çalışan Adayı Aydınlatma Metni".
- Turna (reserve) answered 403, so the Wayback capture of 2026-08-24 was used
  (`http://web.archive.org/web/20260824152717/https://www.turna.com/ticari-elektronik-ileti-acik-riza-metni`).
- Paribu's page carries the consent text followed by a long KVK policy of "Paribu Biletleme";
  extract only the consent part.
- Rossmann publishes a separate *Müşteri Yurtdışı Açık Rıza Metni*; the main consent text was taken.
- Pages that hold several texts: Penti (a WhatsApp notice plus a consent), Look Bubble and Lunaar
  (user and business consents), and Seyhan, Adana Diş Hekimi, HEM and TKRCD (a notice plus a
  consent). Extract only the customer/user consent part (rule 6).
- Alan Suites' text is for website visitors, and ITserv's is a combined visitor notice and consent.
- Footer or CMS dates were not recorded as text dates: Dentaforum's "Son Güncelleme: 07.08.2026"
  is site-wide, and Öztekin Oto's "son değiştirilme" is the fetch day.

Sector: the App Store primary category of the main app; `e-commerce` for a shop without an app in
the pool, `b2b-saas` for a B2B software seller, `medical` for a clinic. The sector cap of a pre-built
run does not apply to a region run.

| # | Company | App (store id) | URL | Sector | Tags | Size | Base | Language | Route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dirk Rossmann Mağazacılık Tic. Ltd. Şti. | Rossmann (1636829121) | https://www.rossmann.com.tr/rossmann-politikalari/musteri-acik-riza-metni | shopping | transfer-consent | large | TR | tr | R1 |
| 2 | Paribu Kripto Varlık Alım Satım Platformu A.Ş. | Paribu (1448200352) | https://www.paribu.com/destek/yasal/paribu-kripto-varlik-alim-satim-platformu-as-musterilere-iliskin-acik-riza-metni | finance | transfer-consent | mid | TR | tr | R1 |
| 3 | Harun Yardımcı (EatWell) | EatWell (6797201529) | https://geteatwell.app/legal/tr/saglik-verisi-acik-riza.html | health-fitness | transfer-consent | small | TR | tr | R2 |
| 4 | Emaa Sigorta A.Ş. | - | https://s3.emaasigorta.com.tr/emaasigorta/Ueruen_veya_Hizmet_Alan_Kisi_Acik_Riza_Formu_701b637806.pdf (via hub https://emaasigorta.com.tr/yasal-bilgilendirmeler/acik-riza-metni/) | finance | transfer-consent | large | TR | tr | R4 |
| 5 | Eren Perakende ve Tekstil A.Ş. (FashFed) | FashFed (1584319459) | https://www.fashfed.com/acik-riza-metni | shopping | transfer-consent | mid | TR | tr | R1 |
| 6 | Uzm. Dr. Hande Arda | - | https://www.handearda.com/tr/yasal-uyari-bilgilendirme/hasta-ve-hasta-yakini-kisisel-verilerinin-islenmesine-yonelik-acik-riza-metni | medical | transfer-consent | small | TR | tr | R4 |
| 7 | T.C. Ziraat Bankası A.Ş. | - | https://www.ziraatbank.com.tr/tr/bankamiz/gizlilik-ve-cerez-politikalari/kisisel-verilerin-islenmesine-yonelik-acik-riza-onay-formu | finance | transfer-consent | large | TR | tr | KAP/R4 |
| 8 | Eczacıbaşı Evital Sağlık Hizmetleri ve Tic. A.Ş. | evital (1631884007) | https://evital.com.tr/kisisel-verilerin-islenmesi | health-fitness | | mid | TR | tr | R1 |
| 9 | Selin Çiftçi (Butika) | Butika (6811413788) | https://butika.ai/acik-riza-metni/ | shopping | transfer-consent | small | TR | tr | R2 |
| 10 | Tekzen Taşımacılık Tic. ve San. Yatırım A.Ş. | - | https://www.tekzen.com.tr/acik-riza-metni | e-commerce | etk | large | TR | tr | KAP/R4 |
| 11 | Doğa Sigorta A.Ş. | - | https://www.dogasigorta.com/acik-riza-metni | finance | transfer-consent | mid | TR | tr | R4 |
| 12 | Arifoğulları Otomotiv San. Tic. Ltd. Şti. (Kızılkaya Business Hotel) | - | https://www.kizilkayabusinesshotel.com/acik-riza-metni/ | travel | transfer-consent | small | TR | tr | R4 |
| 13 | İpekyol Giyim San. Paz. ve Tic. A.Ş. | - | https://www.ipekyol.com.tr/pazarlama-verilerinin-kullanimina-iliskin-acik-riza-beyani | e-commerce | transfer-consent | large | TR | tr | KAP/R4 |
| 14 | TÜRKKEP Kayıtlı Elektronik Posta Hizmetleri A.Ş. | TÜRKKEP Mobil KEP (6451191619) | https://turkkep.com.tr/kvkk-iletisim-acik-riza-metni/ | productivity | transfer-consent | mid | TR | tr | R1 |
| 15 | Solviera Teknoloji Yazılım ve Dijital Hiz. Ltd. Şti. (Cari Plus) | Cari Plus Ön Muhasebe (6769539153) | https://cariplus.com.tr/pazarlama-acik-riza-metni | finance | | small | TR | tr | R2 |
| 16 | Penti Giyim Tic. A.Ş. | - | https://www.penti.com/tr/whatsapp-aydinlatma-ve-acik-riza-metni | e-commerce | transfer-consent | large | TR | tr | KAP/R4 |
| 17 | Lufian Pazarlama Hizmetleri A.Ş. (NE-SAÇ Tekstil) | LUFIAN (1549883224) | https://www.lufian.com/acik-riza-metni | shopping | | mid | TR | tr | R1 |
| 18 | Ekin Hazal Altıparmak (Look Bubble) | Look Bubble (6749798052) | https://lookbubble.com/acik-riza-metni/ | lifestyle | transfer-consent | small | TR | tr | R2 |
| 19 | Bauhaus İnşaat Malzemeleri ve Ev Gereçleri Ltd. Şti. | - | https://www.bauhaus.com.tr/aydinlatma-ve-riza-metni.pdf | e-commerce | etk, transfer-consent | large | TR | tr | KAP/R4 |
| 20 | T.O.M. Katılım Bankası A.Ş. | TOM Bank Hadi (1595820974) | https://www.tombank.com.tr/assets/images/doc/tombank-acik-riza-metni.pdf | finance | | mid | TR | tr | R1 |
| 21 | Taiga Teknoloji A.Ş. (Lunaar Vision) | - | https://lunaarvision.com/tr/yasal-merkez/acik-riza-metni | b2b-saas | transfer-consent | small | TR | tr | R4 |
| 22 | Türkiye Vakıflar Bankası T.A.O. (VakıfBank) | - | https://www.vakifbank.com.tr/documents/bankamiz/kvkk-arsiv/kisisel-verilerin-islenmesine-iliskin-izin-formu.pdf (redirects to vbassets.vakifbank.com.tr) | finance | transfer-consent | large | TR | tr | KAP/R4 |
| 23 | Tapucom Teknoloji Pazarlama ve Tic. A.Ş. | tapu.com (1524042636) | https://www.tapu.com/dokumanlar/acik-riza-aydinlatma | shopping | | mid | TR | tr | R2 |
| 24 | PCI Yazılım Danışmanlık ve Org. Ltd. Şti. (Diyetkolik) | Diyetkolik (558076089) | https://www.diyetkolik.com/acik-riza-bilgilendirmesi | health-fitness | transfer-consent | small | TR | tr | R2 |
| 25 | Gedik Yatırım Menkul Değerler A.Ş. | Gedik Trader (1116732065) | https://sozlesme.gedik.com/doc/acik_riza_beyani.htm (Wayback 2026-06-18) | finance | | mid | TR | tr | R1 |
| 26 | Carell Giyim San. ve Tic. Ltd. Şti. | - | https://www.carellofficial.com/acik-riza-metni-kvkk | e-commerce | | small | TR | tr | R4 |
| 27 | Quick Sigorta A.Ş. | - | https://izinyolusigorta.com/yasal-uygulamalar/acik-riza-metni | finance | transfer-consent | mid | TR | tr | R4 |
| 28 | Gökova Sigorta | - | https://www.gokovasigorta.com.tr/yasal-sorumluluklar/acik-riza-metni-saglik | finance | | small | TR | tr | R4 |
| 29 | Koltur Seyahat Acentalığı Turizm Tic. A.Ş. (Kolin Hotel) | - | https://kolinhotel.com/acik-riza-metni/ | travel | | mid | TR | tr | R4 |
| 30 | Yakalahadi Yazılım Hiz. Ltd. Şti. (RandevuBak) | RandevuBak (6762194998) | https://randevubak.com/acik-riza-beyani | business | | small | TR | tr | R2 |
| 31 | Özel Ankara Kadın Sağlığı ve Üreme Merkezi San. Tic. A.Ş. (Centrum Klinik) | - | https://www.centrumtupbebek.com/hasta-acik-riza-metni/ | medical | | mid | TR | tr | R4 |
| 32 | Dentaforum Tedavi Hiz. Turizm Özel Sağlık Hiz. San. ve Tic. A.Ş. | - | https://www.dentaforum.com.tr/acik-riza-metni-hasta/ | medical | | small | TR | tr | R4 |
| 33 | Altın Gök Turistik Tesisleri Tic. ve San. A.Ş. (Armonia Holiday) | - | https://armonia.holiday/acik-riza-metni/ | travel | | mid | TR | tr | R4 |
| 34 | İbrahim Şipal (DietNode) | DietNode (6759876549) | https://www.dietnode.com/legal/acik-riza | health-fitness | | small | TR | tr | R2 |
| 35 | Tuğba | - | https://www.tugba.com/pages/acik-riza-metni | e-commerce | etk, transfer-consent | mid | TR | tr | R4 |
| 36 | Merki International LLC (Emlak Asistan) | Emlak Asistan (6758913072) | https://emlakciasistan.com/kvkk-acik-riza | business | transfer-consent | small | US | tr | R2 |
| 37 | Tripenia Bilişim Turizm Seyahat Acentası ve Tic. A.Ş. (Turna) | - | https://www.turna.com/ticari-elektronik-ileti-acik-riza-metni (Wayback 2026-08-24) | travel | etk | mid | TR | tr | R4 |
| 38 | Tempo Turizm ve Seyahat Acentası Ltd. Şti. | - | https://tempotur.com.tr/acikrizametni | travel | transfer-consent | small | TR | tr | R4 |
| 39 | Dikey Vitamin Kozmetik ve Gıda Takviyeleri Paz. Tic. A.Ş. (Supplementler) | - | https://www.supplementler.com/t/iletisimmetni | e-commerce | etk | mid | TR | tr | R4 |
| 40 | Emir Özçoban (FitJeton) | FitJeton (6795446699) | https://www.fitjeton.com/acik-riza.html | health-fitness | transfer-consent | small | TR | tr | R2 |
| 41 | Kip | - | https://www.kip.com.tr/pages/ticari-elektronik-ileti-onayi | e-commerce | etk | mid | TR | tr | R4 |
| 42 | Dt. Mehmet Mustafa Doğan (Adana Diş Hekimi) | - | https://adanadishekimi.tr/aydinlatma-ve-acik-riza-metni | medical | | small | TR | tr | R4 |
| 43 | Monai Finansal Planlama A.Ş. (Monay) | Monay (1672306126) | https://monay.com.tr/acik-riza-metni | finance | | small | TR | tr | R1 |
| 44 | Tuzcular Sigorta Aracılık Hizmetleri Ltd. Şti. | - | https://tuzcularsigorta.com/bilgi-merkezi/kvkk-aydinlatma-metni/kvkk-acik-riza-metni/ | finance | transfer-consent | small | TR | tr | R4 |
| 45 | Gözalan Özel Eğitim Öğretim Kurumları Öğr. Barınma Hiz. Otelcilik ve Turizm A.Ş. (Alan Suites) | - | https://otel.alansuites.com/acik-riza-metni/ | travel | | small | TR | tr | R4 |
| 46 | Havacılık Eğitim Merkezi (HEM Eğitim) | - | https://hemegitim.com.tr/tr/6698-kvk-kanunu-aydinlatma-metni/ | education | transfer-consent | small | TR | tr | R4 |
| 47 | Prof. Dr. Muammer Seyhan | - | https://www.drmuammerseyhan.com/hasta-aydinlatma-ve-acik-riza-metni,2,285226 | medical | transfer-consent | small | TR | tr | R4 |
| 48 | Dost İnşaat Taahhüt San. ve Tic. A.Ş. (Coliseum) | - | https://www.coliseum.com.tr/kisisel-verilerin-islenmesine-iliskin-acik-riza-metni/ | health-fitness | transfer-consent | small | TR | tr | R4 |
| 49 | Asringrup Bilgi Tekn. Paz. ve Tic. Ltd. Şti. (Emlaksitem) | Emlaksitem (1365504893) | https://emlaksitem.com/icerik/acik-riza-beyani/19 | education | | small | TR | tr | R2 |
| 50 | Prof. Dr. Öztekin Oto | - | https://www.oztekinoto.com/riza-metni | medical | transfer-consent | small | TR | tr | R4 |
| 51 | Uzman Ağız ve Diş Sağlığı Polikliniği Hiz. Ltd. Şti. | - | https://www.uzmandisgrup.com/kvkk/Hasta-Aydinlatma-ve-Acik-Riza-Metni-Form.pdf | medical | | small | TR | tr | R4 |
| 52 | Hotel Konfor | - | https://www.hotelkonfor.com/sayfa/35/kisisel-verilerin-korunmasina-iliskin-bilgilendirme-ve-acik-riza-metni | travel | | small | TR | tr | R4 |
| 53 | Fazla Gıda A.Ş. | - | https://www.fazla.com/musteri-calisani-ve-musteri-yetkilisi-acik-riza-metni/ | b2b-saas | transfer-consent | small | TR | tr | R4 |
| 54 | Türk Kolon ve Rektum Cerrahisi Derneği (TKRCD) | - | https://www.tkrcd.org.tr/gizlilik-ve-kisisel-veri-politikasi | medical | | small | TR | tr | R4 |
| 55 | ITserv Technology | - | https://www.itservtechnology.com/wp-content/uploads/2024/06/Aydinlatma-ve-Acik-Riza-Metni.pdf | b2b-saas | | small | TR | tr | R4 |
| 56 | Hasan Yılmaz (Rezzim) | Rezzim Salon (6766552617) | https://rezzim.com/acik-riza | business | etk, transfer-consent | small | TR | tr | R2 |
| 57 | Kullanat Sipariş | - | https://www.kullanatsiparis.com/pages/acik-riza-ve-ticari-elektronik-ileti-metni | e-commerce | etk | small | TR | tr | R4 |
| 58 | Stargang Store | - | https://stargangstore.com/pages/acik-riza-ve-ticari-ileti-onayi | e-commerce | etk, transfer-consent | small | TR | tr | R4 |
| 59 | FK Bilgi Teknolojileri Ltd. Şti. (Pratik E-Ticaret) | - | https://www.pratiketicaret.com/acik-riza-metni | b2b-saas | etk | small | TR | tr | R4 |
| 60 | E-Ticaret360 | - | https://eticaret360.net/acik-riza-metni | b2b-saas | etk | small | TR | tr | R4 |
| 61 | Voltla | - | https://voltla.com.tr/acik-riza-metni | e-commerce | etk | small | TR | tr | R4 |
| 62 | Impact Hub İstanbul | - | https://istanbul.impacthub.net/hakkimizda/ticari-elektronik-ileti-onay-formu/ | business | etk | small | TR | tr | R4 |
| 63 | Hemington | - | https://www.hemington.com.tr/acik-riza-metni | e-commerce | etk | small | TR | tr | R4 |

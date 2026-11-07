---
doc_id: tr-kvkk-notice
region: tr
built: 2026-10-27
routes_run: [KAP/İSO 500/Fortune Türkiye 500 → R4, R1 cc=tr, R2 cc=tr]
raw_rows: ../kvkk-pool/pool/
---

Selected from the shared KVKK pool (`research/regions/tr/kvkk-pool/pool/`, PLAN.md decision 45):
119 raw rows in 3 slices (`tr-apps` 49, `tr-large` 28, `tr-tail` 42), 106 distinct companies with
an *Aydınlatma URL*; only that column was used. The `tr-consent` slice (written for
`tr-explicit-consent`) has no Aydınlatma URL column and was not read. Six rows had no Aydınlatma URL and were not
candidates (Vestel, Ziraat Bankası, IKEA, Bauhaus, Penti, AgeSA). Size is an estimate per
`sources.md`. Rows 1–30 are the pool; rows 31+ are the reserve, used in order of size when a
candidate is invalid. Rows 1–15 are the first batch and were not reordered when decision 46 was
narrowed; the new mid picks fill rows 16–30 in the size rotation.

**First-screen check** (fetched 2026-10-27). Each page was opened to confirm it is a
customer/user notice, then PLAN.md decision 46 was applied. *Test* records what kept it:
`dated` (shows a date on or after 2024-06-01) or `art9` (its transfer section uses the new Art. 9
tools: yeterlilik kararı, standart sözleşme, bağlayıcı şirket kuralları, arızi aktarım); both are
listed where both were confirmed. For small rows only the date was checked. Under the narrowed
decision 46, an undated notice with no transfer-abroad section is kept as `no-transfer` unless it
bases special-category (özel nitelikli) processing on explicit consent alone (the Art. 6 check).
Of the 20 such rows, 19 passed and 1 was dropped (RE/MAX Türkiye: special-category data collected
"onayınız dahilinde", relying on consent). Paribu's biometric data rests on AML law, Bimasraf and
Planla list several bases, so all three passed.

**Shortfall.** None in the pool: 10 large, 10 mid, 10 small. Mid has no reserve: the 5
`no-transfer` mid rows (BKM Kitap, Paribu, arabam.com, Manulas, Honda) exactly fill the third, and
the other mid rows were notices without the new Art. 9 tools and with no date on or after
2024-06-01 (UPTION, Matriks, Pembe Panjur, Konuşarak Öğren, e-Mükellef), carried a pre-cutoff
date (TürkKEP 2022, FashFed 2024-02-21, tapu.com 2019), failed the Art. 6 check (RE/MAX), or were
not the app's customer notice (Midas: Kognivia general notice). An invalid mid candidate leaves
the third short. Reserve: 6 large, 0 mid, 33 small.

**Drops at the first screen** (29 companies):
- Old-style transfer, explicit consent as the basis for transfer abroad (5): Samsung, Pamukkale,
  Tekzen, enuygun, Emlak Asistan.
- No transfer-abroad section and no date, failing the Art. 6 check (1): RE/MAX Türkiye. The
  other 19 of the original 20 are now kept as `no-transfer` (5 mid picks; 5 large and 9 small
  in the reserve).
- Other (23): transfer section without the new tools and no date: Beymen, Koton, Akbank, Kuveyt
  Türk (hub; banking notice followed), TOM Bank, UPTION, Matriks, Pembe Panjur (footer date is
  the fetch day), Konuşarak Öğren, e-Mükellef, Monay, AdımPara, Arveya; dated before 2024-06-01:
  VakıfBank (2024-01-23), FashFed (2024-02-21), TürkKEP (2022), tapu.com (2019 policy); page
  shows no notice text: Gratis, BİM, Aksa Doğalgaz (hub), Diyetkolik; wrong company: Pegasus
  (pegasus.com.tr is Pegasus Denizcilik); not a customer notice: Midas (Kognivia general notice).

**Group rule** (candidate rule 5), left out before the check: Pierre Cardin (Aydınlı, with U.S.
Polo Assn.; same text); Network (Boyner, with Beymen); idefix (Turkuvaz, with D&R); getirfinans
(Getir); Midas Kripto (Midas); Yapı Kredi and Amerikan Hastanesi (Koç, with Opet); Türkiye
Sigorta (Türkiye Varlık Fonu, with Türk Telekom). No two kept texts match (rule 4, 6-word
shingles); the only near-copies in the pool were within one group (U.S. Polo/Pierre Cardin,
Beymen/Network, ING's two notices).

**Notes.** Karaca's `tr-apps` URL (`/aydinlatma`) is a lighting-products page; the `tr-large` URL
was used. Opet's URL is a hub; its *Müşteri/Kurumsal Müşteri Aydınlatma Metni* link was followed
(rule 6). Türk Telekom's page holds several notices in one page; extract the individual-customer
part. Etstur's page is a combined KVKK and privacy policy that also covers staff, so it is a
reserve, not a pick. ING publishes two near-identical notices; the general one was taken.
Salonia's page calls itself a sample text to be replaced; it is kept as a template (decision 26)
and is last in the small reserve. Macrocenter's page is served in a broken encoding (UTF-8 read as
Windows-1250); decode it as UTF-8 when extracting.

Sector: the App Store primary category of the main app; `e-commerce` for a shop without an app
in the pool. The sector cap of a pre-built run does not apply to a region run.

| # | Company | App (store id) | URL | Sector | Test | Size | Base | Language | Route |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dirk Rossmann Mağazacılık Tic. Ltd. Şti. | Rossmann (1636829121) | https://www.rossmann.com.tr/rossmann-politikalari/musteri-aydinlatma-metni | shopping | art9 | large | TR | tr | R1 |
| 2 | Lufian Pazarlama Hizmetleri A.Ş. (NE-SAÇ Tekstil) | LUFIAN (1549883224) | https://www.lufian.com/kvkk-aydinlatma-metni | shopping | dated, art9 | mid | TR | tr | R1 |
| 3 | Mahir Baran Aydoğan (6 Tekrar) | 6 Tekrar (6816790796) | https://6tekrar.com/yasal/aydinlatma-metni | health-fitness | dated | small | TR | tr | R1 |
| 4 | ING Bank A.Ş. | ING Mobil (395535459) | https://www.ing.com.tr/tr/ing/kisisel-verilerin-korunmasi/kisisel-verilerin-islenmesi-hakkinda-aydinlatma-metni | finance | dated | large | TR | tr | KAP/R4 |
| 5 | Multinet Kurumsal Hizmetler A.Ş. | MultiPay (680381668) | https://multinet.com.tr/sites/default/files/static/kullanici-aydinlatma-metni.pdf | finance | art9 | mid | TR | tr | R1 |
| 6 | Solviera Teknoloji Yazılım ve Dijital Hizmetler Ltd. Şti. | Cari Plus Ön Muhasebe (6769539153) | https://cariplus.com.tr/kvkk-aydinlatma-metni | finance | dated | small | TR | tr | R2 |
| 7 | Shaya Kahve (Starbucks Türkiye) | - | https://www.starbucks.com.tr/kisisel-verileri-aydinlatma-metni | food-drink | art9 | large | TR | tr | KAP/R4 |
| 8 | Eczacıbaşı Evital Sağlık Hizmetleri ve Tic. A.Ş. | evital (1631884007) | https://evital.com.tr/kullanici-aydinlatma-metni | health-fitness | art9 | mid | TR | tr | R1 |
| 9 | Fırsat Yapay Zeka Teknolojileri A.Ş. | Fırsat (6795664118) | https://firsat.com/kvkk-aydinlatma-metni | shopping | dated | small | TR | tr | R1 |
| 10 | Türk Telekomünikasyon A.Ş. | - | https://www.turktelekom.com.tr/destek/kvkk-aydinlatma-metinleri (combined) | utilities | art9 | large | TR | tr | KAP/R4 |
| 11 | Pluxee Çalışan Deneyimi Dan. ve Paz. Hiz. A.Ş. | Pluxee Türkiye (1557840411) | https://www.pluxee.com.tr/kilavuz/kart-kulanicisi-aydinlatma-metni/ | food-drink | art9 | mid | TR | tr | R1 |
| 12 | Gazioğlu Yazılım A.Ş. (Ortak Market) | Ortak Market (6739862539) | https://ortakmarket.com/gizlilik-politikasi | business | dated | small | TR | tr | R2 |
| 13 | Mudo Satış Mağazaları A.Ş. | - | https://www.mudo.com.tr/musteri-aydinlatma-metni | e-commerce | art9 | large | TR | tr | KAP/R4 |
| 14 | Gedik Yatırım Menkul Değerler A.Ş. | Gedik Trader (1116732065) | https://sozlesme.gedik.com/doc/kvkk_aydinlatma_metni.htm | finance | art9 | mid | TR | tr | R1 |
| 15 | Turuncu Deneyim Org. ve Tekn. Ltd. Şti. (Society) | Society (6783267058) | https://societyapp.org/aydinlatma-metni.html | lifestyle | dated | small | TR | tr | R1 |
| 16 | FLO Mağazacılık ve Pazarlama A.Ş. | FLO (889027386) | https://www.flo.com.tr/aydinlatma-metni | shopping | art9 | large | TR | tr | R1 |
| 17 | BKM Kitap Kırtasiye San. ve Tic. Ltd. Şti. | Bkmkitap (1272652000) | https://www.bkmkitap.com/6698-sayili-kisisel-verilerin-korunmasi-kanunu-aydinlatma-ve-bilgilendirme-metni | shopping | no-transfer | mid | TR | tr | R1 |
| 18 | Ali Yılmaz (Güven Sürücü Kursları) | Güven Sürücü Kursları (1494361165) | https://www.guvensurucukursu.com.tr/aydinlatma-metni/ | education | dated | small | TR | tr | R2 |
| 19 | Getir Perakende Lojistik A.Ş. | - | https://www.getir.com/yardim/kvkk/ | food-drink | dated, art9 | large | TR | tr | KAP/R4 |
| 20 | Paribu Kripto Varlık Alım Satım Platformu A.Ş. | Paribu (1448200352) | https://www.paribu.com/destek/yasal/paribu-kripto-varlik-alim-satim-platformu-as-musterilere-iliskin-aydinlatma-metni | finance | no-transfer | mid | TR | tr | R1 |
| 21 | Parpali Yazılım ve Bilişim Hiz. Tic. Ltd. Şti. | HalıSaha+ (6761794919) | https://halisahaplus.com/tr/kvkk | sports | dated | small | TR | tr | R2 |
| 22 | Opet Petrolcülük A.Ş. | Opet Mobil (390624881) | https://opetwebcdn.azureedge.net/medium/document-file-1526.vsf (via hub https://www.opet.com.tr/bilgi-toplulugu-hizmetleri/kisisel-verilerin-korunmasi) | lifestyle | art9 | large | TR | tr | R1 |
| 23 | Arabam.com İnternet ve Bilgi Hizmetleri A.Ş. | arabam.com (369111943) | https://www.arabam.com/kisisel-verilerin-korunmasi | lifestyle | no-transfer | mid | TR | tr | R1 |
| 24 | Burak Ouzhan (Randvy) | Randvy (6792024039) | https://www.randvy.com/legal/privacy | lifestyle | dated | small | TR | tr | R2 |
| 25 | EHM Mağazacılık San. ve Tic. A.Ş. (English Home) | English Home (1190293324) | https://www.englishhome.com/aydinlatma-metni-checkout | shopping | art9 | large | TR | tr | R1 |
| 26 | Manulaş Manisa Ulaşım Hizmetleri Makina San. ve Tic. A.Ş. | Manisa Kart Mobile (6752911560) | https://www.manulas.com.tr/faaliyetler/kisisel-verilerin-korunmasi/aydinlatma-metni | travel | no-transfer | mid | TR | tr | R1 |
| 27 | Osman Ali Elma (FotoButik) | FotoButik (6821299300) | https://fotobutikk.app/gizlilik | photo-video | dated | small | TR | tr | R2 |
| 28 | İpekyol Giyim San. Paz. ve Tic. A.Ş. | - | https://www.ipekyol.com.tr/kvkk-uyarinca-hizmet-alicisi-aydinlatma-metni | e-commerce | art9 | large | TR | tr | KAP/R4 |
| 29 | Honda Türkiye A.Ş. | Honda Yanımda (6743437540) | https://www.honda.com.tr/kisisel-verilerin-korunmasi | lifestyle | no-transfer | mid | TR | tr | R1 |
| 30 | Efe Yağız Subaşı (Kiovita) | Kiovita (6814838025) | https://www.kiovita.com.tr/aydinlatma | health-fitness | dated | small | TR | tr | R2 |
| 31 | Ets Ersoy Turistik Servisleri A.Ş. (Etstur) | Etstur (882198456) | https://www.etstur.com/Gizlilik-Politikasi (combined) | travel | dated, art9 | large | TR | tr | R1 |
| 32 | Mehmet Fatih Yaşar (Campaign) | Campaign – Deal Tracker (6811686857) | https://campaignapp.tech/kvkk/ | shopping | dated | small | TR | tr | R1 |
| 33 | Dijital Platform Gıda Hizmetleri A.Ş. (Macrocenter, Migros) | - | https://www.macrocenter.com.tr/kisisel-verilerin-korunmasi-hakkinda-aydinlatma-yazisi | e-commerce | no-transfer | large | TR | tr | KAP/R4 |
| 34 | Hasan Yılmaz (Rezzim) | Rezzim Salon (6766552617) | https://rezzim.com/salon-aydinlatma-metni | business | dated | small | TR | tr | R2 |
| 35 | Karaca Züccaciye Tic. ve San. A.Ş. | Karaca (1547965580) | https://www.karaca.com/bilgilendirme/musteri-aydinlatma-metni-s2 | shopping | no-transfer | large | TR | tr | KAP/R4 |
| 36 | Ludens İleri Finansal Hiz. ve Dan. Ltd. Şti. | İyi Gelir (6744439314) | https://iyigelir.net/dokumanlar/kvkk-aydinlatma-metni/ | finance | dated | small | TR | tr | R1 |
| 37 | Turkuvaz Müzik Kitap Mağ. Paz. A.Ş. (D&R) | D&R (586922088) | https://www.dr.com.tr/uyelik-aydinlatma-metni | lifestyle | no-transfer | large | TR | tr | R1 |
| 38 | Fırat Yakut (eLLC) | eLLC Kolay Dil Öğren (6761500971) | https://www.ellconline.com/kvkk | education | dated | small | TR | tr | R2 |
| 39 | Aydınlı Hazır Giyim San. ve Tic. A.Ş. (U.S. Polo Assn.) | U.S. Polo Assn. (788605532) | https://tr.uspoloassn.com/kisisel-veri-aydinlatma-metni/ | shopping | no-transfer | large | TR | tr | R1 |
| 40 | Ekin Hazal Altıparmak (Look Bubble) | Look Bubble (6749798052) | https://lookbubble.com/aydinlatma-metni/ | lifestyle | dated | small | TR | tr | R2 |
| 41 | Mars Spor Kulübü ve Tesisleri İşl. A.Ş. (MACFit) | MAC+ (1573778936) | https://www.macfit.com/uyelik-islemleri-aydinlatma-metni | health-fitness | no-transfer | large | TR | tr | R1 |
| 42 | Harun Yardımcı (EatWell) | EatWell (6797201529) | https://geteatwell.app/legal/tr/kvkk-aydinlatma-metni.html | health-fitness | dated | small | TR | tr | R2 |
| 43 | Yakalahadi Yazılım Hiz. Ltd. Şti. (RandevuBak) | RandevuBak (6762194998) | https://randevubak.com/kvkk-aydinlatma-metni | business | dated | small | TR | tr | R2 |
| 44 | Selin Çiftçi (Butika) | Butika (6811413788) | https://butika.ai/aydinlatma-metni/ | shopping | dated | small | TR | tr | R2 |
| 45 | Gökhan Balık (NEFPort) | e-Fatura & e-Arşiv: NEFPort (6766068553) | https://nefport.com/yasal/kvkk-aydinlatma-metni | finance | dated | small | TR | tr | R2 |
| 46 | İhsan Vehbi Yavuz (X3CAD) | Parsel Etüt (6811433435) | https://x3cad.com/aydinlatma | productivity | dated | small | TR | tr | R2 |
| 47 | Moimaere OÜ (Sırada) | Sırada (6762229337) | https://sirada.app/kvkk | business | dated | small | EU (EE) | tr | R2 |
| 48 | İbrahim Şipal (DietNode) | DietNode (6759876549) | https://www.dietnode.com/legal/kvkk-aydinlatma | health-fitness | dated | small | TR | tr | R2 |
| 49 | JASSE Gayrimenkul Dan. Ltd. Şti. | JASSE (6820459416) | https://jasse.com.tr/kvkk | lifestyle | dated | small | TR | tr | R2 |
| 50 | Tekliflee Dijital Hiz. Tic. Ltd. Şti. | Tekliflee (6759823548) | https://tekliflee.com/form-aydinlatma-metni | shopping | dated | small | TR | tr | R1 |
| 51 | İbrahim Kaya (GymKod) | GymKod (6756016320) | https://gymkod.com/privacy-policy (combined) | business | dated | small | TR | tr | R2 |
| 52 | Ali Aktürk (AlhazenPDF) | AlhazenPDF (6771070616) | https://alhazenpdf.com/kvkk.html | utilities | dated | small | TR | tr | R2 |
| 53 | Yasin Akbulut (Diyet Takibim) | Diyet Takibim (6768430807) | https://www.diyettakibim.com/kvkk-aydinlatma-metni | health-fitness | dated | small | TR | tr | R2 |
| 54 | Dijida Teknoloji ve Yazılım Ltd. Şti. (FulSalon) | FulSalon (1449150190) | https://fulsalon.com/yasal/kvkk-aydinlatma-metni | business | dated | small | TR | tr | R2 |
| 55 | FC Yapı İnşaat Oto. San. Tic. Ltd. Şti. (Xtapu) | Xtapu (6791942616) | https://xtapu.com/kvkk | lifestyle | dated | small | TR | tr | R2 |
| 56 | Emir Özçoban (FitJeton) | FitJeton (6795446699) | https://www.fitjeton.com/kvkk.html | health-fitness | dated | small | TR | tr | R2 |
| 57 | Samet Danaç (Resepton) | Resepton (6817353435) | https://resepton.com/kvkk | business | dated | small | TR | tr | R2 |
| 58 | Serdar Ziya Akova (Velora) | Velora Salon Management (6762641928) | https://www.veloraappy.com/legal/kvkk (combined) | business | dated | small | TR | tr | R2 |
| 59 | Beyhan Çolak (Vaktivar) | Vaktivar Partner (6774277819) | https://vaktivar.com/kvkk | business | dated | small | TR | tr | R2 |
| 60 | MKOSoft Yazılım A.Ş. (Önmuhasebeciniz) | Önmuhasebeciniz (6759179047) | https://onmuhasebeciniz.com/kvkk-aydinlatma-metni | business | dated | small | TR | tr | R2 |
| 61 | CG Bilgi Yazılım ve Danışmanlık Ltd. Şti. (Bimasraf) | Bimasraf (1529717141) | https://www.bimasraf.com/aydinlatma-metni | finance | no-transfer | small | TR | tr | R2 |
| 62 | This Is A Company Tekn. Gel. ve Yat. A.Ş. (Frink) | Frink (1538561803) | https://frink.com.tr/tr/aydinlatma-metni | food-drink | no-transfer | small | TR | tr | R1 |
| 63 | Virapp Bilgi Teknolojileri A.Ş. (Kolay Ehliyet) | Kolay Ehliyet (1669463544) | http://kolayehliyet.com/kvkk-aydinlatma-metni | education | no-transfer | small | TR | tr | R1 |
| 64 | Planla Yazılım Tic. Ltd. Şti. | Planla (6758662146) | https://planla.co/kvkk-metni | business | no-transfer | small | TR | tr | R2 |
| 65 | Asringrup Bilgi Tekn. Paz. ve Tic. Ltd. Şti. (Emlaksitem) | Emlaksitem (1365504893) | https://emlaksitem.com/icerik/kvkk-aydinlatma-metni/17 | education | no-transfer | small | TR | tr | R2 |
| 66 | Ayşenur Ülkü Saygı (Notet) | Notet Randevu Programı (6762554656) | https://notet.net/uye-aydinlatma-metni | business | no-transfer | small | TR | tr | R2 |
| 67 | Bakiyem Danışmanlık Arge ve Yazılım Ltd. Şti. (kursum.app) | Aysar Sürücü Kursu (1601513840) | https://kursum.app/kvkk/ | education | no-transfer | small | TR | tr | R2 |
| 68 | Cen Teknoloji Medikal Kozmetik Estetik San. ve Tic. Ltd. Şti. (Salonay) | Salonay (6761684384) | https://salonay.com/kvkk | business | no-transfer | small | TR | tr | R2 |
| 69 | Özsoft Teknoloji Yazılım Eğitim Dan. ve Yay. Tic. Ltd. Şti. (Salonia) | Salonia (6818756452) | https://salonia.io/kvkk | business | no-transfer | small | TR | tr | R2 |

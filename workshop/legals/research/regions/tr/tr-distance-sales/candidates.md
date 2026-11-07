---
doc_id: tr-distance-sales
region: tr
built: 2026-10-26
routes_run: [KAP/İSO 500/Fortune Türkiye 500 → R4, R1 cc=tr, R2 cc=tr, R3 gl=TR, Turkish-keyword web search → R4]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (118 rows, 5 slices: `large-lists` 26, `r1-appstore-tr`
20, `r3-play-tr` 22, `r2-tail-tr` 20, `web-tail-tr` 30). Size is an estimate per `sources.md`.
Rows 1–30 are the pool; rows 31+ are the reserve, used in order of size when a candidate is
invalid. *Goods* marks what the seller sells, because the withdrawal-right exceptions differ for
digital content and services.

Group rule (candidate rule 5): Beymen is left out (Boyner group); Bellona is left out
(İstikbal, Boydak group); Bambu Çiçek is left out (Nota Çiçek, same company); D&R is left out
(idefix, Turkuvaz group).

Sector: the App Store primary category of the main app; `e-commerce` for a shop without an
app; `b2b-saas` for software subscriptions sold online. Shopping dominates because the document
exists only where goods are sold; the sector cap of a pre-built run does not apply to a region
run.

| # | Company | App (store id) | URL | Sector | Goods | Size | Language | Route |
|---|---|---|---|---|---|---|---|---|
| 1 | FLO Mağazacılık ve Pazarlama A.Ş. | FLO (889027386) | https://www.flo.com.tr/mesafeli-satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 2 | BKM Kitap Kırtasiye San. ve Tic. Ltd. Şti. | Bkmkitap (1272652000) | https://www.bkmkitap.com/satis-sozlesmesi | shopping | physical | mid | tr | R1 |
| 3 | TrendTeach Eğitim Danışmanlık Org. Ltd. Şti. | - | https://www.trendteach.com/distance_sales | education | digital (courses) | small | tr | web |
| 4 | Vestel Elektronik San. ve Tic. A.Ş. | Vestel Smart Life (966916050) | https://www.vestel.com.tr/content/satis-sozlesmesi | lifestyle | physical | large | tr | R1 |
| 5 | Cevher Kozmetik ve Sağlık San. Tic. A.Ş. | Kozmela (com.tsoft.kozmela) | https://www.kozmela.com/satis-sozlesmesi | shopping | physical | mid | tr | R3 |
| 6 | Lab Kahve Unlu Mamuller İml. San. ve Tic. Ltd. Şti. | Coffee LAB (6740917575) | https://coffeelab.com.tr/mesafeli-satis-sozlesmesi/ | food-drink | physical | small | tr | R2 |
| 7 | Karaca Züccaciye Tic. ve San. A.Ş. | Karaca (1547965580) | https://www.karaca.com/bilgilendirme/mesafeli-satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 8 | Nota Çiçek Satış ve Tic. A.Ş. | Nota Çiçek (com.notacicek.app) | https://www.notacicek.com/s/mesafeli-satis-sozlesmesi | shopping | physical (perishable) | mid | tr | R3 |
| 9 | Solviera Teknoloji Yazılım ve Dijital Hizmetler Ltd. Şti. | - | https://solviera.com.tr/sayfa/mesafeli-satis-sozlesmesi | b2b-saas | service (software) | small | tr | web |
| 10 | Dirk Rossmann Mağazacılık Tic. Ltd. Şti. | Rossmann (1636829121) | https://www.rossmann.com.tr/musteri-hizmetleri/mesafeli-satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 11 | Gündoğdu Mobilya | Gündoğdu Mobilya (com.gundogdumobilya.mobil) | https://www.gundogdumobilya.com.tr/mesafeli-satis-sozlesmesi (combined) | shopping | physical (bulky) | mid | tr | R3 |
| 12 | Nil Evcil Hayvan Ürünleri Paz. San. ve Tic. Ltd. Şti. | Patime Gelsin (1596258781) | https://patimegelsin.com/mesafeli_satis_sozlesmesi.html | shopping | physical | small | tr | R2 |
| 13 | Mudo | - | https://www.mudo.com.tr/satis-sozlesmesi | e-commerce | physical | large | tr | KAP/R4 |
| 14 | Fernus Bilişim Hizmetleri Eğ. Dan. ve Tic. Ltd. Şti. | Fenomen Video Çözüm (1462253730) | https://www.fernus.com.tr/mesafeli-satis-sozlesmesi/ | education | digital (video lessons) | mid | tr | R1 |
| 15 | Khilios (Nilüfer Demirci) | - | https://www.khilios.com/sayfa/mesafeli-satis-sozlesmesi | e-commerce | physical | small | tr | web |
| 16 | Boyner Büyük Mağazacılık A.Ş. | Boyner (610957461) | https://www.boyner.com.tr/content/mesafeli-satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 17 | Saat ve Saat | Saat&Saat (com.mnm.saatvesaat.mobile) | https://www.saatvesaat.com.tr/mesafeli-satis-sozlesmesi | shopping | physical | mid | tr | R3 |
| 18 | Eduson Yazılım San. ve Tic. Ltd. Şti. | Öğretmen Evrak (1520664624) | https://ogretmenevrak.com/mesafeli-satis-sozlesmesi | education | digital (documents, membership) | small | tr | R1 |
| 19 | Turkuvaz Müzik Kitap Mağ. Paz. A.Ş. (idefix) | idefix (1106420758) | https://www.idefix.com/s/satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 20 | İnt-el International Elektronik | Direnc.net (com.tsoft.direncnet) | https://www.direnc.net/mesafeli-satis-sozlesmesi | shopping | physical | mid | tr | R3 |
| 21 | Yener Zeytin ve Zeytinyağı | - | https://yenerzeytin.com.tr/page/mesafeli-satis-sozlesmesi | e-commerce | physical (food) | small | tr | web |
| 22 | Doğuş Perakende Satış Giyim ve Aks. Tic. A.Ş. (Kiko Milano TR) | Kiko Milano (6451242576) | https://www.kikomilano.com.tr/mesafeli-satis-sozlesmesi/ | shopping | physical | large | tr | R1 |
| 23 | Kahve Diyarı Paz. San. ve Tic. A.Ş. | Kahve Diyarı (com.kaizentech.kahvediyari) | https://kahvediyari.com/pages/mesafeli-satis-sozlesmesi | food-drink | physical (food) | mid | tr | R3 |
| 24 | Ferda Uslu Doğal Kozmetik ve Gıda Ürünleri A.Ş. | Fermente Mutfağım (1493265214) | https://www.fermentemutfagim.com/satis-sozlesmesi (combined) | shopping | physical (food) | small | tr | R2 |
| 25 | Deha Mağazacılık Ev Tekstili Ürünleri A.Ş. (Madame Coco) | Madame Coco (1411335629) | https://www.madamecoco.com/satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 26 | DDY Gıda İnş. Taah. Tur. A.Ş. (Arabica Coffee House) | Arabica Coffee House (6447524981) | https://arabicacoffee.com.tr/sayfalar/mesafeli-satis-sozlesmesi | food-drink | physical (food) | mid | tr | R1 |
| 27 | Doğal Ahşap ve Gıda Ürünleri San. Tic. Ltd. Şti. (Toysishop) | - | https://www.toysishop.com/mesafeli-satis-sozlesmesi | e-commerce | physical | small | tr | web |
| 28 | Tekzen | - | https://www.tekzen.com.tr/mesafeli-satis-sozlesmesi | e-commerce | physical | large | tr | KAP/R4 |
| 29 | Dinçerler Gıda İşletmeleri A.Ş. (Gloria Jean's TR) | Gloria Jean's Coffees Türkiye (6739029923) | https://gloriajeans.com.tr/pages/mesafeli-satis-sozlesmesi | food-drink | physical (food) | mid | tr | R1 |
| 30 | Kontroljet Yazılım A.Ş. (HakedişJet) | - | https://hakedisjet.com/mesafeli-satis/ | b2b-saas | service (software) | small | tr | web |
| 31 | Ay Marka Mağazacılık A.Ş. (Network) | Network (1233028325) | https://www.network.com.tr/content/mesafeli-satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 32 | True Friends Pet Shop | TrueFriends (com.truefriends.app) | https://truefriends.com.tr/mesafeli-satis-sozlesmesi | shopping | physical | mid | tr | R3 |
| 33 | Qapo Coffee | - | https://www.qapocoffee.com/mesafeli-satis-sozlesmesi/ | e-commerce | physical (food) | small | tr | web |
| 34 | Flormar | Flormar (com.flormar.flormar) | https://www.flormar.com.tr/mesafeli-satis-sozlesmesi/ | shopping | physical | large | tr | R3 |
| 35 | ZOO Pet Shop | ZOO Pet Shop (com.ticimax.androidbase.zoo) | https://www.zoo.com.tr/mesafeli-satis-sozlesmesi | shopping | physical | mid | tr | R3 |
| 36 | Erol Akademi Eğitim San. ve Tic. Ltd. Şti. (Online Ders Merkezi) | - | https://www.onlinedersmerkezi.com/mesafeli-satis-sozlesmesi (combined) | education | service (live lessons) | small | tr | web |
| 37 | Ayakkabı Dünyası | - | https://www.ayakkabidunyasi.com.tr/mesafeli-satis-sozlesmesi | e-commerce | physical | large | tr | KAP/R4 |
| 38 | Vatkalı Tekstil Ürünleri Paz. San. Tic. Ltd. Şti. | VATKALI (6446801830) | https://www.vatkali.com/tr/mesafeli-satis-sozlesmesi | shopping | physical | mid | tr | R1 |
| 39 | Misket | - | https://www.misket.com.tr/sayfa/2/mesafeli-satis-sozlesmesi | e-commerce | physical (second-hand) | small | tr | web |
| 40 | Lescon | - | https://www.lescon.com.tr/satis-sozlesmesi/ | e-commerce | physical | large | tr | KAP/R4 |
| 41 | Farktör Yazılım Dan. San. ve Tic. Ltd. Şti. (FullaModa) | FullaModa (1504843422) | https://www.fullamoda.com/mesafeli-satis-sozlesmesi | shopping | physical | mid | tr | R1 |
| 42 | Otelsoft Yazılım Teknolojileri | - | https://otelsoft.com/mesafeli-satis-sozlesmesi | b2b-saas | service (software) | small | tr | web |
| 43 | Evkur | - | https://www.evkur.com.tr/mesafeli-satis-sozlesmesi | e-commerce | physical | large | tr | KAP/R4 |
| 44 | Babymall | - | https://www.babymall.com.tr/mesafeli-satis-sozlesmesi | e-commerce | physical | mid | tr | KAP/R4 |
| 45 | Sidra Gıda (Bitkisel Reyonum) | - | https://bitkiselreyonum.com/mesafeli-satis-sozlesmesi/ | e-commerce | physical | small | tr | web |
| 46 | BR Mağazacılık Tic. A.Ş. (Altınyıldız Classics) | Altınyıldız Classics (1483910505) | https://www.altinyildizclassics.com/satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 47 | Dermoeczanem | - | https://www.dermoeczanem.com/satis-sozlesmesi | e-commerce | physical | mid | tr | KAP/R4 |
| 48 | Siliconmade Arge Yazılım Bilişim A.Ş. (Siliconmade Academy) | - | https://www.siliconmadeacademy.com/mesafeli-satis-sozlesmesi.html (combined) | education | digital (courses) | small | tr | web |
| 49 | Shaya Mağazacılık A.Ş. (Victoria's Secret TR) | Victoria's Secret Türkiye (6443790652) | https://www.victoriassecret.com.tr/mesafeli-satis-sozlesmesi | shopping | physical | large | tr | R1 |
| 50 | Kağan Parfümeri | Kağan Parfümeri (com.tsoft.kaganparfumeri) | https://www.kaganparfumeri.com/satis-sozlesmesi | shopping | physical | mid | tr | R3 |
| 51 | Tolia Zeytinyağı (Pelitköy) | - | https://toliapelitkoy.com/pages/mesafeli-satis-sozlesmesi | e-commerce | physical (food) | small | tr | web |
| 52 | Suwen | - | https://www.suwen.com.tr/mesafeli-satis-sozlesmesi | e-commerce | physical | large | tr | KAP/R4 |
| 53 | Doratek Gıda (Kolaymama) | Kolaymama (1164892235) | https://www.kolaymama.com/satis-sozlesmesi.shtm | shopping | physical | mid | tr | R2 |
| 54 | Pakkod Yazılım (Happinessİst) | Happinessİst (6787659777) | https://happinessistanbul.com/mesafeli-satis-sozlesmesi | shopping | physical | small | tr | R2 |
| 55 | Sportive | Sportive (com.akinon.sportive) | https://www.sportive.com.tr/satis-sozlesmesi/ | shopping | physical | large | tr | R3 |
| 56 | Kitapsec Yayıncılık | Kitap Seç (1445690338) | https://www.kitapsec.com/Konu/Mesafeli-Satis-Sozlesmesi.html | shopping | physical | mid | tr | R2 |
| 57 | Teak Eğitim Yazılım A.Ş. (Türkiye Eğitim Akademisi) | - | https://turkiyeegitimakademisi.com/sozlesme | education | digital (courses) | small | tr | web |
| 58 | İstikbal | - | https://www.istikbal.com.tr/sayfa/mesafeli-satis-sozlesmesi | e-commerce | physical (bulky) | large | tr | KAP/R4 |
| 59 | Sütiş Restoran İşletmeleri A.Ş. | Sütiş Çiftliği (1538793505) | https://shop.sutis.com.tr/pages/mesafeli-satis-sozlesmesi | shopping | physical (food) | mid | tr | R2 |
| 60 | Detay Kahve San. ve Tic. A.Ş. (Bikaldi) | - | https://www.bikaldi.com.tr/mesafeli-satis-sozlesmesi | e-commerce | physical (food) | small | tr | web |

Further raw rows in `pool/` (small IdeaSoft, ikas, WooCommerce and Shopify shops; Damat Tween
and Kelebek with blank checkout templates; Pazarama, JS-only) are the last reserve.

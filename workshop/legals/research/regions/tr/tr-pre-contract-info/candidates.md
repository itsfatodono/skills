---
doc_id: tr-pre-contract-info
region: tr
built: 2026-10-27
routes_run: [tr-distance-sales pool sites → R4, Turkish-keyword web search → R4]
raw_rows: pool/
---

Selected from the raw rows in `pool/` (112 rows, 1 slice: `relocate`, made of 25 sites from the
`tr-distance-sales` pool and 87 found by Turkish-keyword web search). Size is an estimate per
`sources.md`. Rows 1–30 are the pool; rows 31+ are the reserve, used in order of size when a
candidate is invalid. *Goods* marks what the seller sells, because the withdrawal-right
exceptions differ for digital content and services. *Form* is `page` for a stand-alone form and
`embedded` for a form block inside the distance sales contract (PLAN.md decision 45); embedded
rows are neither excluded nor favoured. Every row below was opened on 2026-10-27 and its first
screen shows the form, or for `embedded` rows the form block inside the contract.

Group rule (candidate rule 5): Karaca Home is left out (Karaca group).

Dropped at first screen: Kitap Yayınevi and Delta Kültür Yayınevi (the page holds only a
title, so the text is rendered by script and the fetch got none); Sundex Vitamin (the row says
`in MSS`, but the contract has no form block, only a footer link to the form). Not screened, so
not picked: 10 Shopify shops (Demontha, Troya Case, Serena Uziyel, Toysall, Muyuru, Saja
Mercan, Kanzii, Triathlon.tc, Biocore, Ponet Maison, Yapılır; the shop host answered 429 for
the whole run) and Tebilon (bot wall; a Wayback capture from 2026-01-30 exists). They stay in
the last reserve.

Shared texts (candidate rule 4, kept as samples; the merge decides copies). The *Template*
column names them:

- `T1`: "Satış Sözleşmesi Ön Bilgi Formu … SİPARİŞ VEREN/ALICI" text, often with unfilled
  `{_saticiunvan_}`-style variables (a platform default). Raw rows: Gündoğdu, Bu Yayınevi,
  Little Lamb, Saray Takı, Nom Oto, PlantoHealth, Taşkın; close variants at Williams Roastery,
  Evine Kahve, Doqu Home, Duvar Kağıdı Modelleri, Class One. The same opening starts the forms
  of Shaya (Victoria's Secret), OPPO and Galipoğlu Hidromas. The most copied form in the pool.
- `T2`: Karaca's text. Karaca Home carries it, and Tane Teknoloji copies it word for word with
  the seller details left blank; Tekzen shares its definitions opening.
- `T3`: a "ÖN BİLGİLENDİRME" block inside a "Satış Sözleşmesi" page: Evvahe, Fermente
  Mutfağım, Siveno, Kağan Parfümeri.
- `T4`: platform default with `----` in place of seller data: Kaybio, Dubpa, Oasisbooks.
- `T5`: block inside `/teslimat-ve-iade/mesafeli-satis-sozlesmesi`: BebeGross, Prendi Home
  (with `........` placeholders).
- Pairs: Vatkalı ≈ FullaModa; İş Kültür ≈ Multibem Kitap; Dermoeczanem shares parts with
  KRVN (Kervan); Beyhan Butik ≈ Parça Yıldızı; Zygielle and Revert share an opening.

Sector: the App Store primary category of the main app; `e-commerce` for a shop without an
app; `b2b-saas` for software sold online. Where a reseller runs the brand's TR store, the seller
is named in brackets.

| # | Company | App (store id) | URL | Sector | Goods | Size | Form | Template | Language | Route |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Karaca Züccaciye Tic. ve San. A.Ş. | Karaca (1547965580) | https://www.karaca.com/bilgilendirme/on-bilgilendirme-formu | shopping | physical | large | page | T2 (source) | tr | R1 |
| 2 | Fernus Bilişim Hizmetleri Eğ. Dan. ve Tic. Ltd. Şti. | Fenomen Video Çözüm (1462253730) | https://www.fernus.com.tr/on-bilgilendirme-formu/ | education | digital (video lessons) | mid | page | - | tr | R1 |
| 3 | AVHOS Hukuk Otomasyon Sistemleri | - | https://avhos.com/mesafeli-satis-on-bilgilendirme-formu/ | b2b-saas | service (software licence, optional hardware) | small | page | - | tr | web |
| 4 | Turkuvaz Müzik Kitap Mağ. Paz. A.Ş. (idefix) | idefix (1106420758) | https://www.idefix.com/s/on-bilgilendirme-formu | shopping | physical (marketplace) | large | page | - | tr | R1 |
| 5 | Dermo Grup İnternet Mağazacılık San. ve Tic. A.Ş. (Dermoeczanem) | - | https://www.dermoeczanem.com/on-bilgilendirme-formu | e-commerce | physical | mid | page | shares parts with KRVN | tr | KAP/R4 |
| 6 | Detay Kahve San. ve Tic. A.Ş. (Bikaldi) | - | https://www.bikaldi.com.tr/on-bilgilendirme-formu/ | e-commerce | physical (food) | small | page | - | tr | web |
| 7 | Borusan Oto Online Store | - | https://onlinestore.borusanoto.com/on-bilgilendirme-formu | e-commerce | physical (automotive) | large | page | - | tr | web |
| 8 | Kağan Parfümeri | Kağan Parfümeri (com.tsoft.kaganparfumeri) | https://www.kaganparfumeri.com/satis-sozlesmesi | shopping | physical | mid | embedded | T3 | tr | R3 |
| 9 | Siliconmade Arge Yazılım Bilişim A.Ş. (Siliconmade Academy) | - | https://www.siliconmadeacademy.com/on-bilgilendirme-formu.html | education | digital (courses) | small | page | - | tr | web |
| 10 | Mudo | - | https://www.mudo.com.tr/satis-sozlesmesi | e-commerce | physical | large | embedded | - | tr | KAP/R4 |
| 11 | Boğaziçi İstanbul Reklam ve Org. Ltd. Şti. (İstanbul Çiçekleri) | - | https://www.istanbulcicekleri.com/on-bilgilendirme-formu | e-commerce | physical (perishable) | mid | page | - | tr | web |
| 12 | Terra Point Design Seramik Tasarım San. Tic. Ltd. Şti. (Opal Seramik) | - | https://opalseramik.com/on-bilgilendirme-formu/ | e-commerce | physical | small | page | - | tr | web |
| 13 | ASUS Türkiye (GPN Bilgi Teknolojileri San. ve Tic. A.Ş.) | - | https://www.asus.com/tr/About_ASUS/On-Bilgilendirme-Formu | e-commerce | physical (electronics) | large | page | - | tr | web |
| 14 | True Friends Pet Shop | TrueFriends (com.truefriends.app) | https://truefriends.com.tr/on-bilgilendirme-formu | shopping | physical | mid | page | - | tr | R3 |
| 15 | Bu Yayınevi | - | https://www.buyayinevi.com/sayfa/on-bilgilendirme-formu | e-commerce | physical (books) | small | page | T1 | tr | web |
| 16 | Bizim Toptan Satış Mağazaları A.Ş. | - | https://www.bizimtoptan.com.tr/on-bilgilendirme-formu/ | e-commerce | physical (groceries) | large | page | - | tr | KAP/R4 |
| 17 | Cevher Kozmetik ve Sağlık San. Tic. A.Ş. | Kozmela (com.tsoft.kozmela) | https://www.kozmela.com/on-bilgilendirme-formu | shopping | physical | mid | page | - | tr | R3 |
| 18 | CORVIA Yazılım ve Bilişim Tek. San. Tic. A.Ş. | - | https://corviasoftware.com/PreInformationForm | b2b-saas | service (software) | small | page | - | tr | web |
| 19 | Tekzen | - | https://www.tekzen.com.tr/on-bilgilendirme-formu | e-commerce | physical | large | page | shares T2's opening | tr | KAP/R4 |
| 20 | Kültür Yayınları İş Türk A.Ş. (İş Kültür Yayınları) | - | https://www.iskultur.com.tr/on-bilgilendirme-formu | e-commerce | physical (books) | mid | page | ≈ Multibem Kitap | tr | web |
| 21 | Fermente Mutfağım Yaşayan Gıda Paz. Tic. A.Ş. | Fermente Mutfağım (1493265214) | https://www.fermentemutfagim.com/satis-sozlesmesi | shopping | physical (food) | small | embedded | T3 | tr | R2 |
| 22 | OPPO Türkiye (Mobile Point Bilişim Hizmetleri A.Ş.) | - | https://www.oppo.com/tr/store/events/on-blglendrme-formu | e-commerce | physical (electronics) | large | page | T1 opening | tr | web |
| 23 | Elele Dış Ticaret A.Ş. (Elele Baby) | - | https://www.elelebaby.com/on-bilgilendirme-formu | e-commerce | physical | mid | page | - | tr | web |
| 24 | İmhotep Mobilya | - | https://www.imhotep.com.tr/on-bilgilendirme-formu/ | e-commerce | physical (bulky) | small | page | - | tr | web |
| 25 | BR Mağazacılık Tic. A.Ş. (Altınyıldız Classics) | Altınyıldız Classics (1483910505) | https://www.altinyildizclassics.com/on-bilgilendirme-formu | shopping | physical | large | page | - | tr | R1 |
| 26 | The North Face Türkiye (RND Yazılım ve E-Ticaret A.Ş.) | - | https://www.thenorthface.com.tr/thenorthface-on-bilgilendirme-formu | e-commerce | physical | mid | page | - | tr | web |
| 27 | Vizetek Yayıncılık San. ve Tic. Ltd. Şti. | - | https://vizetek.com.tr/sayfa/Mesafeli-Satis-Sozlesmesi-1 | e-commerce | physical (books) | small | embedded | - | tr | web |
| 28 | Siberian Wellness Türkiye | - | https://tr.siberianhealth.com/tr/shop/page/pre-purchase-form/ | e-commerce | physical (supplements) | large | page | - | tr | web |
| 29 | Vatkalı Tekstil Ürünleri Paz. San. Tic. Ltd. Şti. | VATKALI (6446801830) | https://www.vatkali.com/tr/on-bilgilendirme | shopping | physical | mid | page | ≈ FullaModa | tr | R1 |
| 30 | Zigel Aksesuar Takı Tasarım Ltd. Şti. (Zygielle) | - | https://zygielle.com/on-bilgilendirme-formu/ | e-commerce | physical | small | page | shares opening with Revert | tr | web |
| 31 | Shaya Mağazacılık A.Ş. (Victoria's Secret TR) | Victoria's Secret Türkiye (6443790652) | https://www.victoriassecret.com.tr/on-bilgilendirme-formu | shopping | physical | large | page | T1 opening | tr | R1 |
| 32 | Dikey Vitamin Kozmetik ve Gıda Takviyeleri Paz. Tic. A.Ş. (Supplementler.com) | - | https://m.supplementler.com/t/onbilgilendirmeformu | e-commerce | physical (supplements) | mid | page | - | tr | web |
| 33 | Homm Bitkisel | - | https://www.hommbitkisel.com.tr/sozlesmeler/on_bilgilendirme_formu | e-commerce | physical | small | page | - | tr | web |
| 34 | Doğuş Perakende Satış Giyim ve Aks. Tic. A.Ş. (Maje Türkiye) | - | https://www.maje-paris.com.tr/on-bilgilendirme-formu | e-commerce | physical | large | page | - | tr | web |
| 35 | İstanbul Modern Sanat Müzesi İktisadi İşletmesi (Mağaza) | - | https://www.istanbulmodern.org/magaza/on-bilgilendirme-formu | e-commerce | physical | mid | page | - | tr | web |
| 36 | ElektronikLisans | - | https://www.elektroniklisans.tr/on-bilgilendirme-formu.php | e-commerce | digital (software licences) | small | page | - | tr | web |
| 37 | Bosch Professional e-shop (Fi Commerce Teknoloji Tic. A.Ş.) | - | https://eshop.bosch-professional.com/tr/tr/on-bilgilendirme-metni | e-commerce | physical (tools) | large | page | - | tr | web |
| 38 | SporPark Ayakkabı Teks. ve Spor Malz. Tic. Ltd. Şti. (Slazenger Türkiye) | - | https://www.slazenger.com.tr/on-bilgilendirme-formu | e-commerce | physical | mid | page | - | tr | web |
| 39 | CND Edutech Eğitim Teknolojileri A.Ş. (Bizle Geliş) | - | https://bizlegelis.com/on-bilgilendirme-formu/ | education | digital (courses) | small | page | - | tr | web |
| 40 | Galipoğlu Hidromas (Galipoğlu Form Dış Ticaret A.Ş.) | - | https://store.hidromas.com/on-bilgilendirme-formu | e-commerce | physical (industrial; business buyers) | large | page | T1 opening | tr | web |
| 41 | BebeGross | - | https://www.bebegross.com/teslimat-ve-iade/mesafeli-satis-sozlesmesi | e-commerce | physical | mid | embedded | T5 | tr | web |
| 42 | Athenaum (Pelin Dilara Çolak Güleç, sole trader) | - | https://athenaum.tr/yasal/on-bilgilendirme-formu | e-commerce | service (membership) | small | page | - | tr | web |
| 43 | Kervan Tekstil San. ve Dış Tic. A.Ş. (KRVN) | - | https://www.krvn.com.tr/on-bilgilendirme-formu | e-commerce | physical (bulky) | mid | page | shares parts with Dermoeczanem | tr | web |
| 44 | Eken Mobilya | - | https://ekenmobilya.com.tr/tr/yasal/on-bilgilendirme | e-commerce | physical (bulky) | small | page | - | tr | web |

Further raw rows in `pool/` are the last reserve: the other screened small shops (most of them
`T1`, `T3` or `T4` copies), Gündoğdu Mobilya and FullaModa (mid), the unscreened Shopify
shops and Tebilon. The raw row "Koçtaş / KRVN" is Kervan Tekstil (KRVN), not Koçtaş.

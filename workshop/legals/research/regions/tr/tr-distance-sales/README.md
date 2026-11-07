# tr-distance-sales: build record

Built 2026-10-26 (Phase 2 pilot, region run `tr`, `part: whole`). Skeleton:
`plugins/fatodono-founderkit/skills/legals/regions/tr/tr-distance-sales.md`. Item 39 of the seed catalog
(Mesafeli Satış Sözleşmesi) only; the Ön Bilgilendirme Formu (item 40) was skipped wherever a
page carried both (rule 6).

## Run

- **Routes run:** large companies from the KAP BIST list, İSO 500 and Fortune Türkiye 500, then
  R4 on each site; R1 (`cc=tr`, genres 6024, 6023, 6012, 6013, 6017, free and grossing); R2
  (`country=tr`, 13 Turkish keywords: kahve, butik, çiçek, doğal kozmetik, takı, organik,
  pastane, kitap, evcil hayvan, abonelik, online kurs, spor salonu, ders); R3 (`gl=TR`,
  SHOPPING, FOOD_AND_DRINK, BEAUTY, HOUSE_AND_HOME, SPORTS, BOOKS_AND_REFERENCE, plus about 20
  Play keyword searches); a Turkish-keyword web search for small sellers without an app
  (`"mesafeli satış sözleşmesi"` plus `"SATICI" "ALICI"` plus a product word), then R4.
  Raw rows: `pool/` (118 rows, 5 `pool-collector` slices). Selection: `candidates.md` (30 pool
  rows plus 30 reserve rows).
- **Re-judged 2026-10-27** under decisions 26 (templates are valid samples; whole-text copies
  count once) and 27 (only a new section id makes a sample new). The first run had dropped
  s06, s09, s15, s21, s27, s33, s35 and s39 as template texts; s35 and s39 were extracted now.
  The run below is the re-judged one; the first run's verdicts stay in `merge.md` for the
  record.
- **First batch:** s01–s15 (5 large, 5 mid, 5 small), no replacements.
- **Saturation:** batches s16–s20, s21–s25, then s26 s28 s29 s30 (s27 a copy). New: s19
  (`marketplace`), s24 (`subscription`). Not new: s25, s26, s28, s29, s30 (5 in a row).
  Verdicts per sample in `merge.md`.
- **Past the stop point, kept:** s32, s34, s36, s39, s42.
- **Stop reason:** saturated after s30. `sample_count: 34`.
- **Size mix:** large 11, mid 11, small 12. s32 is recorded as mid but is a sole
  proprietorship and is probably small.
- **Merged section list:** `merge.md` (all 34 samples).

## Scarcity

- **Small sellers:** most small physical-goods sellers publish a template: the widely copied
  contract (the text at `forbes.com.tr/mesafeli-satis-sozlesmesi`, also on Law Insider TR,
  whole or cut down) or an older shop template, on IdeaSoft, Ticimax, WooCommerce, Qukasoft,
  Zükkan and custom sites alike. Under decision 26 they count, but 3 of them (s27, s33, s35)
  publish the same whole text as s15 and count once, so the samples hold fewer distinct small
  physical-goods texts than candidates.
- **Large marketplaces and chains:** Trendyol, Hepsiburada, n11, Çiçeksepeti, Sahibinden, A101,
  Teknosa, DeFacto, Mavi, LC Waikiki, Koton, MediaMarkt, Migros and others answered with 403,
  429 or JS-only pages, or show the contract only at checkout. The Wayback CDX index was
  offline during collection, so no capture URL was found for them. The only marketplace in the
  samples is idefix (s19).
- **Sectors missing:** telecom, airlines, travel and branded grocery published no stable
  contract URL. Health and fitness apps (R1 genre 6013) showed the contract only at checkout.

## Invalid and copies

| Sample | Company | Rule | Reason |
|---|---|---|---|
| s27 | Toysishop | 4, copy of s15 | the s15 text with the shop's details and one toy example added (Qukasoft shop) |
| s31 | Ay Marka (Network) | 5 | Boyner group; the text is the Boyner contract (s16) with small changes |
| s33 | Qapo Coffee | 4, copy of s15 | the s15 text with even the seller fields left blank (WooCommerce shop) |
| s35 | ZOO Pet Shop | 4, copy of s15 | the s15 text with the seller's name and address filled in (Ticimax shop) |

s06, s09, s15, s21 and s39, dropped by the first run as template texts, are valid samples
under decision 26. s21 is the s15 template cut down to 8 articles, so its whole text differs
and it stays a sample for prevalence, but adds no patterns (decision 38).

Builder's calls on borderline samples, kept valid: s02 and s23 rewrite the common template in
their own words (no copied sentence beyond statutory wording); s28 leaves one drafting bracket
naming the company, not a generator placeholder; s13 calls itself the pre-information form in
one article but is the contract page; s02, s04, s14, s24 and s26 name a group company as
seller, on the brand's own domain.

## Samples

| Sample | Company | URL | Sector | Size | Language | Fetched |
|---|---|---|---|---|---|---|
| s01 | FLO Mağazacılık ve Pazarlama A.Ş. | https://www.flo.com.tr/mesafeli-satis-sozlesmesi | shopping | large | tr | 2026-10-26 |
| s02 | BKM Kitap Kırtasiye San. ve Tic. Ltd. Şti. | https://www.bkmkitap.com/satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s03 | TrendTeach Eğitim Danışmanlık Organizasyon Ltd. Şti. | https://www.trendteach.com/distance_sales | education | small | tr | 2026-10-26 |
| s04 | Vestel Elektronik Sanayi ve Ticaret A.Ş. | https://www.vestel.com.tr/content/satis-sozlesmesi | lifestyle | large | tr | 2026-10-26 |
| s05 | Cevher Kozmetik ve Sağlık San. Tic. A.Ş. (Kozmela) | https://www.kozmela.com/satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s06 | Lab Kahve Unlu Mamuller İml. San. ve Tic. Ltd. Şti. (Coffee Lab) | https://coffeelab.com.tr/mesafeli-satis-sozlesmesi/ | food-drink | small | tr | 2026-10-26 |
| s07 | Karaca Züccaciye Ticaret ve Sanayi A.Ş. | https://www.karaca.com/bilgilendirme/mesafeli-satis-sozlesmesi | shopping | large | tr | 2026-10-26 |
| s08 | Nota Çiçek Satış ve Ticaret A.Ş. | https://www.notacicek.com/s/mesafeli-satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s09 | Solviera Teknoloji Yazılım ve Dijital Hizmetler Ltd. Şti. | https://solviera.com.tr/sayfa/mesafeli-satis-sozlesmesi | b2b-saas | small | tr | 2026-10-26 |
| s10 | Dirk Rossmann Mağazacılık Ticaret Ltd. Şti. | https://www.rossmann.com.tr/musteri-hizmetleri/mesafeli-satis-sozlesmesi | shopping | large | tr | 2026-10-26 |
| s11 | Gündoğdu Mobilya San. Tic. Ltd. Şti. | https://www.gundogdumobilya.com.tr/mesafeli-satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s12 | Nil Evcil Hayvan Ürünleri Paz. San. ve Tic. Ltd. Şti. (Patime Gelsin) | https://patimegelsin.com/mesafeli_satis_sozlesmesi.html | shopping | small | tr | 2026-10-26 |
| s13 | Mudo | https://www.mudo.com.tr/satis-sozlesmesi | e-commerce | large | tr | 2026-10-26 |
| s14 | Fernus Bilişim Hizmetleri Eğ. Dan. ve Tic. Ltd. Şti. | https://www.fernus.com.tr/mesafeli-satis-sozlesmesi/ | education | mid | tr | 2026-10-26 |
| s15 | Khilios (Nilüfer Demirci) | https://www.khilios.com/sayfa/mesafeli-satis-sozlesmesi | e-commerce | small | tr | 2026-10-26 |
| s16 | Boyner Büyük Mağazacılık A.Ş. | https://www.boyner.com.tr/content/mesafeli-satis-sozlesmesi | shopping | large | tr | 2026-10-26 |
| s17 | Saat ve Saat Mağazacılık A.Ş. | https://www.saatvesaat.com.tr/mesafeli-satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s18 | Eduson Yazılım San. ve Tic. Ltd. Şti. (Öğretmen Evrak) | https://ogretmenevrak.com/mesafeli-satis-sozlesmesi | education | small | tr | 2026-10-26 |
| s19 | Turkuvaz Müzik Kitap Mağazacılık Pazarlama A.Ş. (idefix) | https://www.idefix.com/s/satis-sozlesmesi | shopping | large | tr | 2026-10-26 |
| s20 | İnt-el International Elektronik (Direnc.net) | https://www.direnc.net/mesafeli-satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s21 | Yener Zeytin ve Zeytinyağı (Ahmet Yener) | https://yenerzeytin.com.tr/page/mesafeli-satis-sozlesmesi | e-commerce | small | tr | 2026-10-26 |
| s22 | Doğuş Perakende Satış Giyim ve Aksesuar Tic. A.Ş. (Kiko Milano Türkiye) | https://www.kikomilano.com.tr/mesafeli-satis-sozlesmesi/ | shopping | large | tr | 2026-10-26 |
| s23 | Kahve Diyarı Pazarlama San. ve Tic. A.Ş. | https://kahvediyari.com/pages/mesafeli-satis-sozlesmesi | food-drink | mid | tr | 2026-10-26 |
| s24 | Ferda Uslu Doğal Kozmetik ve Gıda Ürünleri A.Ş. (Fermente Mutfağım) | https://www.fermentemutfagim.com/satis-sozlesmesi | shopping | small | tr | 2026-10-26 |
| s25 | Deha Mağazacılık Ev Tekstili Ürünleri San. ve Tic. A.Ş. (Madame Coco) | https://www.madamecoco.com/satis-sozlesmesi | shopping | large | tr | 2026-10-26 |
| s26 | DDY Gıda İnşaat Taahhüt Turizm A.Ş. (Arabica Coffee House) | https://arabicacoffee.com.tr/sayfalar/mesafeli-satis-sozlesmesi | food-drink | mid | tr | 2026-10-26 |
| s28 | Tekzen | https://www.tekzen.com.tr/mesafeli-satis-sozlesmesi | e-commerce | large | tr | 2026-10-26 |
| s29 | Dinçerler Gıda İşletmeleri A.Ş. (Gloria Jean's Coffees Türkiye) | https://gloriajeans.com.tr/pages/mesafeli-satis-sozlesmesi | food-drink | mid | tr | 2026-10-26 |
| s30 | Kontroljet Yazılım A.Ş. (HakedişJet) | https://hakedisjet.com/mesafeli-satis/ | b2b-saas | small | tr | 2026-10-26 |
| s32 | TrueFriends Pet Shop (sole proprietorship) | https://truefriends.com.tr/mesafeli-satis-sozlesmesi | shopping | mid | tr | 2026-10-26 |
| s34 | Kosan Kozmetik Pazarlama ve Ticaret A.Ş. (Flormar) | https://www.flormar.com.tr/mesafeli-satis-sozlesmesi/ | shopping | large | tr | 2026-10-26 |
| s36 | Erol Akademi Eğitim San. ve Tic. Ltd. Şti. (Online Ders Merkezi) | https://www.onlinedersmerkezi.com/mesafeli-satis-sozlesmesi | education | small | tr | 2026-10-26 |
| s39 | Misket | https://www.misket.com.tr/sayfa/2/mesafeli-satis-sozlesmesi | e-commerce | small | tr | 2026-10-27 |
| s42 | Otelsoft Yazılım Teknolojileri | https://otelsoft.com/mesafeli-satis-sozlesmesi | b2b-saas | small | tr | 2026-10-26 |

All samples were fetched live; none needed a Wayback capture.

## Method notes

- **Rule 4 check (first run, since replaced):** quoted WebSearch returns summaries and misses
  exact Turkish phrases, so "no hits" proved little. From s15 on, extractors fetched known
  copies of the common templates (Forbes TR page, IdeaSoft example, Law Insider TR copies) and
  compared sentences against their full text; that is what found the template blocks. Under
  decision 26 the re-judge needed none of this: the copies showed in the extraction tables
  (same headings in the same order, same quotes).
- **Template text** (decisions 38 and 39): every sample counts for prevalence; in patterns each
  template's wording counts once and s21 adds none. The 11 earlier samples' template blocks
  were re-read on 2026-10-27; the templates and the sample each counts through are in
  `merge.md`.
- **Extractors past the first batch** were dispatched before the first batch had finished, in
  pool order, to keep the small third filled; batch B was dispatched before batch A was
  judged. Verdicts were still made one at a time in pool order.
- Counts in the skeleton were tallied from the extraction tables (section mapping in
  `merge.md`, plus keyword passes over the tables). Counts of fine-grained patterns can be off
  by one where an extractor's wording was ambiguous.

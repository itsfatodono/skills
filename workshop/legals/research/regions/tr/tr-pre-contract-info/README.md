# tr-pre-contract-info: build record

Built 2026-10-27 (region run `tr`, `part: whole`; PLAN.md decision 45, track B). Skeleton:
`plugins/fatodono-launchkit/skills/legals/regions/tr/tr-pre-contract-info.md`. Item 40 of the seed catalog
(Ön Bilgilendirme Formu). Catalog row added to `regions/tr/catalog.md`.

## Files

- `candidates.md`: the pool of 30 and the reserve (rows 31–44), with shared texts T1–T5.
- `pool/`: raw rows from one slice (`relocate`).
- `samples/sNN.md`: one extraction table per sample, s01–s20.
- `raw/`: stripped texts (git-ignored, never committed or shipped).
- `merge.md`: section ids and meanings, drafting boilerplate (decision 44), section maps, the
  first-batch merged list, patterns, copies and template blocks, document level, saturation log
  and the merged list over all 20 samples.

## Run

- **Routes run:** the `tr-distance-sales` pool sites (25 rows), then R4 on each; a
  Turkish-keyword web search (`"ön bilgilendirme formu"` plus product words) for sellers
  outside that pool (87 rows), then R4. 112 raw rows in one slice.
- **Pool:** 30 candidates, 10 large, 10 mid, 10 small; goods physical 26, digital or service 4;
  form `page` 26, `embedded` 4 (a form block inside the contract page; decision 45, neither
  excluded nor favoured). Group check (rule 5) and first-screen check at selection: Karaca Home
  left out (Karaca group); three rows dropped at first screen (two script-rendered pages, one
  contract with only a footer link to the form).
- **First batch:** s01–s15 (5 per size). All valid; none replaced.
- **Saturation:** batch 1 s16–s20, all valid. Not new: s16, s17, s18, s19, s20. No section id
  was added after the first batch. One id meaning was made explicit while judging s17
  (`card-misuse` covers buyer card default; `merge.md` note 1).
- **Stop reason:** 5 non-new samples in a row, at s20: `saturated: true`. `sample_count: 20`.
  Pool rows 21–30 were not extracted.

## Invalid

None.

## Templates and copies

Rule 4: no copies. Raw texts compared on 6-word shingles; the highest overlap is s19 (Tekzen) at
45% of its text shared with s01 (Karaca, T2). s19 rewrites the exceptions and the data clause
and adds an article, so it stays a sample and is not a cut-down template (decision 38). T1
(s15) and T3 (s08) have one carrier each in the samples; T4 and T5 none. Six template blocks
cross the samples (an older shop template's general provisions, the common contract
provisions, and four single sentences); each counts once in patterns (decision 39). Details in
`merge.md` *Copies* and *Saturation*.

## Size thirds

Valid samples: 7 large, 7 mid, 6 small. No size ran short; the uneven third is only where the
stop fell.

## Samples

All fetched 2026-10-27, language `tr`.

| Sample | Company | URL | Sector | Size |
|---|---|---|---|---|
| s01 | Karaca Züccaciye Tic. ve San. A.Ş. | https://www.karaca.com/bilgilendirme/on-bilgilendirme-formu | shopping | large |
| s02 | Fernus Eğitim Teknolojileri A.Ş. | https://www.fernus.com.tr/on-bilgilendirme-formu/ | education | mid |
| s03 | AVHOS Hukuk Otomasyon Sistemleri | https://avhos.com/mesafeli-satis-on-bilgilendirme-formu/ | b2b-saas | small |
| s04 | Turkuvaz Müzik Kitap Mağ. Paz. A.Ş. (idefix) | https://www.idefix.com/s/on-bilgilendirme-formu | shopping | large |
| s05 | Dermo Grup İnternet Mağazacılık San. ve Tic. A.Ş. (Dermoeczanem) | https://www.dermoeczanem.com/on-bilgilendirme-formu | e-commerce | mid |
| s06 | Detay Kahve San. ve Tic. A.Ş. (Bikaldi) | https://www.bikaldi.com.tr/on-bilgilendirme-formu/ | e-commerce | small |
| s07 | Borusan Oto Servis ve Ticaret A.Ş. (Borusan Oto Online Store) | https://onlinestore.borusanoto.com/on-bilgilendirme-formu | e-commerce | large |
| s08 | Kağan Parfümeri Kozmetik Giyim Turizm Gıda İnşaat San. Tic. Ltd. Şti. | https://www.kaganparfumeri.com/satis-sozlesmesi | shopping | mid |
| s09 | Siliconmade Arge Yazılım Bilişim A.Ş. (Siliconmade Academy) | https://www.siliconmadeacademy.com/on-bilgilendirme-formu.html | education | small |
| s10 | Mudo Satış Mağazaları A.Ş. | https://www.mudo.com.tr/satis-sozlesmesi | e-commerce | large |
| s11 | Boğaziçi İstanbul Reklam ve Org. Ltd. Şti. (İstanbul Çiçekleri) | https://www.istanbulcicekleri.com/on-bilgilendirme-formu | e-commerce | mid |
| s12 | Terra Point Design Seramik Tasarım San. Tic. Ltd. Şti. (Opal Seramik) | https://opalseramik.com/on-bilgilendirme-formu/ | e-commerce | small |
| s13 | GPN Bilgi Teknolojileri San. ve Tic. A.Ş. (ASUS Türkiye online store) | https://www.asus.com/tr/About_ASUS/On-Bilgilendirme-Formu | e-commerce | large |
| s14 | TrueFriends Pet Shop (Şenay Özsoy, sole trader) | https://truefriends.com.tr/on-bilgilendirme-formu | shopping | mid |
| s15 | Bu Yayınevi | https://www.buyayinevi.com/sayfa/on-bilgilendirme-formu | e-commerce | small |
| s16 | Bizim Toptan Satış Mağazaları A.Ş. | https://www.bizimtoptan.com.tr/on-bilgilendirme-formu/ | e-commerce | large |
| s17 | Cevher Kozmetik ve Sağlık San. Tic. A.Ş. (Kozmela) | https://www.kozmela.com/on-bilgilendirme-formu | shopping | mid |
| s18 | CORVIA Yazılım ve Bilişim Teknolojileri San. Tic. A.Ş. | https://corviasoftware.com/PreInformationForm | b2b-saas | small |
| s19 | Tekzen | https://www.tekzen.com.tr/on-bilgilendirme-formu | e-commerce | large |
| s20 | Kültür Yayınları İş Türk A.Ş. (İş Kültür Yayınları) | https://www.iskultur.com.tr/on-bilgilendirme-formu | e-commerce | mid |

Versions and parts taken: s08 only the "ÖN BİLGİLENDİRME" block that opens the "Satış
Sözleşmesi" page (T3); s10 the whole text on a page titled "Satış Sözleşmesi" that calls itself
the form and has no contract after it; s04 the raw order-time template with its per-seller loop
visible; s18 the Turkish version from the language switcher. Seller entity differs from the
candidate row in s02, s13 (authorised reseller, not ASUS) and s14 (sole trader).

## Skeleton

25 sections: 9 core (`subject`, `parties`, `goods-price`, `payment`, `delivery`, `withdrawal`,
`exceptions`, `pre-info-ack`, `disputes`), 9 common (`price-validity`, `inspection`,
`performance`, `card-misuse`, `order-limits`, `personal-data`, `complaints`, `copy`,
`formation`), 7 rare (`marketplace`, `digital-content`, `use-terms`, `after-sales`, `loyalty`,
`subscription`, `withdrawal-form`).

Of the 28 ids in `merge.md`:

- **Folded (3):** `definitions` (5/20) into *Document*, recurring elements; `payment-duty`
  (5/20, the warning that confirming creates a duty to pay) into *goods-price* and
  *pre-info-ack* as a pattern; `misc-rare` (4/20: order-entry error correction into
  *goods-price*, chamber code of conduct and a related-documents list into *Document*, commonly
  omitted). No fact decides any of them (`skeleton-format.md`, rare drafting section).
- **Order:** by median position, except `card-misuse` (0.57) placed before `withdrawal` (0.56)
  so withdrawal and exceptions stay together, and `loyalty` after `exceptions`, as in
  `tr-distance-sales`.
- **Avoid:** `personal-data` carries s01's built-in blanket consent (1/20), against the KVKK
  Board's explicit-consent guidance (decision 47; accepted by the chief of staff 2026-10-27).
- **Drafting boilerplate:** signature and date blocks (7/20) and the "made for commercial
  purposes" line (2/20) are layout under decision 44, not sections (accepted 2026-10-27). The
  skeleton therefore has no `signature` section, unlike `tr-distance-sales`.

## Relation to the distance sales contract

The form and `tr-distance-sales` share most facts (seller, goods and price, delivery,
withdrawal, exceptions, disputes) and reuse the same keys, so a write run fills both from the
same values. The contract's `pre-info-ack` points to this form through `facts.tr.pre_info_form`;
this form's `formation` section makes it part of that contract. 2 of 20 samples publish the form
on the contract page.

## Facts

One key added to `regions/tr/facts.md`: `facts.tr.after_sales` (warranty documents and period,
the seller's own guarantees, after-sales support channels), for the rare `after-sales` section.

Reused from `tr-distance-sales`: `facts.tr.seller_registry`, `facts.tr.sales_model`,
`facts.tr.delivery`, `facts.tr.business_buyers`, `facts.tr.order_limits`,
`facts.tr.loyalty_program`, `facts.tr.acceptance_mechanism`, `facts.tr.contract_copy`,
`facts.tr.pre_info_form`, `facts.tr.kvkk_notice_url`, `facts.tr.withdrawal_period_days`,
`facts.tr.withdrawal_channels`, `facts.tr.return_shipping`, `facts.tr.withdrawal_exceptions`,
`facts.tr.immediate_performance_consent`, `facts.tr.merchant_court`, and the shared
`facts.company.*`, `facts.product.name`, `facts.product.services_in_scope`,
`facts.sales.offer_type`, `facts.sales.payment_methods`, `facts.sales.payment_provider`,
`facts.sales.subscription`, `facts.sales.return_address`, `facts.marketing.email`. New uses of
existing shared keys: `facts.sales.taxes`, `facts.sales.promotions`,
`facts.product.system_requirements`, `facts.product.activation`, `facts.product.support`,
`facts.data.storage_locations`, `facts.company.published_policies`. `tools/check-facts` exits 0.

## Regional content

None: a `whole` skeleton for a region-only item.

## Open for the owner

- **Same pattern in tr-distance-sales.** That skeleton's `personal-data` records "4/18 take
  marketing consent inside the contract" as a plain pattern, with no *Avoid* field (it predates
  the field). Under decision 47 it should probably get the same *Avoid* mark.
- **use-terms gate.** Website-terms clauses (3/5, all physical-goods sellers) are left out by the
  *Applies when* (digital content and services only), and the pattern tells the writer to link
  the terms of service instead. Keep that, or let it follow the samples?
- **Trigger.** The catalog row asks the same question as `tr-distance-sales`, so the two items
  always come together. If the write branch should treat them as one pair, that is a catalog
  convention to decide.

## Lessons

- **The form overlaps the contract more than its law suggests.** 8 of 20 forms carry contract
  clauses (card misuse, seller cancellation, site disclaimers), mostly through two circulated
  templates. Facts they give still count, but the skeleton points site terms to the terms of
  service.
- **The section list was stable from the first batch.** Every saturation sample mapped onto the
  first batch's 28 ids; the only change was making one id's meaning explicit.

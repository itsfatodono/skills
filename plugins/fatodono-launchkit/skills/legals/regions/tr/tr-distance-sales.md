---
doc_id: tr-distance-sales
title: Mesafeli Satış Sözleşmesi (distance sales contract)
kind: document
family: commerce
region: tr
part: whole
sample_languages: [tr]
sample_count: 34
saturated: true
scanned: 2026-10-26
format_version: 2
---

## Document

- **Purpose:** The contract an online seller concludes with a consumer in Turkey for each order:
  who the parties are, what is sold at what price, how it is delivered, how the buyer can
  withdraw, and where disputes go.
- **Shape:**
  - 34/34 one web page, usually under the footer's "Sözleşmeler" menu; median 1,590 words
    (range 390–4,480). 7/34 are under 600 words, 6 of them from sellers of digital content or
    services.
  - 26/34 number their articles "MADDE 1 – TARAFLAR …"; 8/34 use plain numbered headings.
    Decimal sub-clauses (5.1, 5.2) are the norm; a long "Genel Hükümler" article holds the
    delivery, performance and card clauses in 22/34.
  - 23/34 are the order-time template: blank buyer fields, an empty order table, or
    platform tokens (`{{.OrderTotalPrice}}`, `{TotalFee}`, `[Fiyat]`) filled per order. 11/34
    are written as general text with no order fields and point to the order summary instead.
  - 3/34 share the page with the Ön Bilgilendirme Formu (the form first, then the contract);
    30/34 refer to the form as a separate document and an integral part of the contract.
  - 1/34 opens with a table of contents; 3/34 give a "last updated" date.
- **Register:** formal legal Turkish in 29/34: third person, parties as SATICI and ALICI in
  capitals, long sentences ending "kabul, beyan ve taahhüt eder". 5/34 (all digital or small
  sellers) use short modern sentences. 8/34 switch to "siz" in the return, delivery or
  complaint steps.
  Day counts are written as digits plus words ("14 (on dört) gün").
- **Recurring elements:**
  - Law 6502 named: 33/34; the Mesafeli Sözleşmeler Yönetmeliği with its Official Gazette
    date and number: 11/34.
  - A definitions block (site, seller, buyer, product, pre-order): 10/34, at the top.
  - A statement of the article count before the signature ("11 (onbir) maddeden ibaret"):
    6/34.
  - A website-terms block (liability for site failures, IP, third-party links) inside the
    contract: 11/34 (see *use-terms*).
  - 16/34 use a widely circulated template: 5/34 publish one whole (a shop template, a
    generator text, the common contract in full or cut down), 11/34 carry at least one block
    of it inside their own text. 3 more shops published the same whole text as one of the 5 and
    count once (`research/…/README.md`).
  - 11/34 still name a repealed law (4077) or regulation, or a former ministry name; 5/34
    published drafting leftovers (a lawyer's review notes, an editor's comment, unfilled
    "[24/48]" brackets, a generator's "review this template" warning). Recorded as observed,
    not as a legal judgement.
- **Commonly omitted:** a version or date line (31/34); a summary or plain-language overview
  (34/34); named carriers (29/34); fixed refund day counts in some sellers who defer to "the
  law" (2/34); clauses on unilateral changes to the contract (31/34); cash-on-delivery rules
  (33/34).

Counts come from the 34 samples in `research/regions/tr/tr-distance-sales/`. Every sample
counts for prevalence. In patterns, each template's wording counts once however many samples
carry it, and s21, the common template cut down, adds none (`research/…/merge.md`). Patterns record
what sellers write, including where it restates the law; they are not legal advice.

## Sections

### parties: Parties

- **Covers:** the seller's identity, registration numbers and contact channels, and the
  buyer's identity, either as fields filled per order or as a definition.
- **Prevalence:** 34/34 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.company.phone`, `facts.tr.seller_registry`, `facts.sales.return_address`
- **Patterns:**
  - 31/34 give the seller as a label/value block (Unvanı, Adresi, Telefon, E-posta, MERSİS
    No); 1/34 points to the pre-information part; 1/34 names only the brand.
  - Seller identifiers: MERSİS 17/34, tax office and number 10/34, fax 9/34, KEP 4/34.
  - Buyer: 20/34 blank per-order fields (name, address, phone, e-mail); 12/34 one sentence
    saying the buyer's details are those entered at sign-up or checkout; 1/34 points to the
    pre-information part.
  - 9/34 give a complaint channel: a complaint phone line or call-centre hours in the seller
    block (3/9) or a short complaints clause pointing back to it (6/9).
  - 4/34 add a separate return address or warehouse, 2 with the carrier to use.
  - 2/34 add that the stated addresses are the addresses for legal notice.
- **Quote:** "Alıcının adı, soyadı, adresi, telefon numarası ve e-posta adresi sipariş formunda belirtilmektedir." (s32)
- **Commonly omitted:** KEP address (30/34); a seller signature.

### subject: Subject and legal basis

- **Covers:** what the contract governs, the sales channels it covers, and the laws it is made
  under.
- **Prevalence:** 34/34 (100%), core
- **Applies when:** always
- **Facts:** `facts.product.name`, `facts.product.services_in_scope`, `facts.sales.offer_type`
- **Patterns:**
  - 29/34 one long sentence: "İşbu sözleşmenin konusu, ALICI'nın SATICI'ya ait … internet
    sitesinden elektronik ortamda sipariş verdiği …", naming the website and the law.
  - 9/34 extend it to the mobile app or other electronic channels.
  - 4/34 put a one-line legal-basis preamble above the first article.
  - 2/34 say the contract leaves the membership agreement in force alongside it.
  - Digital and service sellers name the kind of content or service sold (7/7).
- **Quote:** "Sözleşme’nin konusu, ALICI’nın SATICI’ya ait fernus.com.tr internet sitesi (“Platform”) üzerinden elektronik ortamda sipariş verdiği, niteliği ve satış bedeli aşağıda belirtilen dijital eğitim hizmeti/içeriği veya abonelik paketinin (“Hizmet”) satışı ve ifasına ilişkin olarak, 6502 sayılı Kanun ve Mesafeli Sözleşmeler Yönetmeliği hükümleri gereğince tarafların hak ve yükümlülüklerinin belirlenmesidir." (s14)
- **Commonly omitted:** the regulation's article numbers; the seller's role when it sells
  through a group company (named by 5/34 only indirectly, by giving a different entity).

### goods-price: Goods, price and order details

- **Covers:** the goods or service ordered, quantities, prices including taxes, shipping and
  other charges, the total, and delivery and invoice addresses.
- **Prevalence:** 32/34 (94%), core
- **Applies when:** always
- **Facts:** `facts.sales.offer_type`, `facts.tr.delivery`, `facts.sales.payment_methods`, `facts.tr.business_buyers`
- **Patterns:**
  - Split: 19/32 an order table or field block filled per order (product, quantity, unit
    price, VAT-inclusive total, shipping fee, payment method, delivery and invoice address);
    11/32 point to the order summary, product page or Ön Bilgilendirme Formu instead; 1/32
    lists the kinds of order data as bullets.
  - 7/32 open the table with a sentence naming the product facts ("Cinsi ve türü, miktarı,
    marka/modeli, rengi, satış bedeli") "as shown below".
  - 6/32 add that listed prices hold until updated and campaign prices until the campaign ends.
  - 6/32 add an invoice block (individual or company invoice, e-invoice by e-mail).
- **Quote:** "Hizmetin türü, miktarı, tüm vergiler dahil satış bedeli ve ödeme bilgileri sipariş onay ekranında ve faturada yer almaktadır." (s36)
- **Commonly omitted:** a worked example of the total; per-line discount detail (3/32 give
  discount or coupon lines).

### marketplace: Marketplace role

- **Covers:** for a platform where third-party sellers sell, the platform's identity, that it
  is not a party to the sale, and how payment, order reassignment and multi-seller carts work.
- **Prevalence:** 1/34 (3%), rare
- **Applies when:** `facts.tr.sales_model == marketplace`
- **Facts:** `facts.tr.sales_model`, `facts.company.legal_name`
- **Patterns:**
  - 1/1 identifies the platform ("Aracı Hizmet Sağlayıcı") in its own block next to a blank
    seller block filled per order.
  - 1/1 has both parties accept that the platform is not a party and bears no liability for
    the sale, and that withdrawal cannot be exercised against it.
  - 1/1 says paying the platform discharges the price owed to the seller, under the platform's
    buyer-protection scheme.
  - 1/1 lets the platform pass an order to another seller with the same goods, and lets one
    cart hold several sellers' items with separate invoices and deliveries.
- **Quote:** "Platform, işbu mesafeli satış sözleşmesinin tarafı olmadığından Platform’a karşı cayma hakkı kullanılamaz veya Platform’dan bedel iadesi talep edilemez." (s19)
- **Commonly omitted:** everything else; the large marketplaces (Trendyol, Hepsiburada, n11)
  blocked fetching and are not in the samples.

### pre-info-ack: Acknowledgement of pre-contract information

- **Covers:** the buyer's statement that it received and read the pre-contract information
  before ordering and confirmed it electronically.
- **Prevalence:** 30/34 (88%), core
- **Applies when:** always
- **Facts:** `facts.tr.pre_info_form`
- **Patterns:**
  - 26/30 one sentence: "ALICI, … ön bilgileri okuyup bilgi sahibi olduğunu ve elektronik
    ortamda gerekli teyidi verdiğini kabul ve beyan eder."
  - 14/30 list the topics confirmed inside that sentence (main features, tax-inclusive price,
    payment, delivery and its cost, seller's trade name and address, withdrawal); 3/30 give
    them as a separate list of 11–16 items.
  - 11/30 name the Ön Bilgilendirme Formu as an integral part of the contract.
  - It usually opens the general provisions; some samples repeat it in the closing
    acceptance (see *formation*).
- **Quote:** "ALICI, … Yönetmeliğin 5. maddesi kapsamındaki tüm ön bilgileri okuyup bilgi sahibi olduğunu ve elektronik ortamda gerekli teyidi verdiğini açıkça beyan eder." (s04)
- **Commonly omitted:** where the form can be found again after the order.

### delivery: Delivery

- **Covers:** where and when goods are delivered or a digital service is activated, carriers,
  shipping costs, failed delivery and delivery to someone other than the buyer.
- **Prevalence:** 33/34 (97%), core
- **Applies when:** always
- **Facts:** `facts.tr.delivery`, `facts.sales.offer_type`
- **Patterns:**
  - 21/33 restate the 30-day maximum delivery period; 6/33 give the usual dispatch time
    (business days to hand to the carrier); 1/33 (an old template) adds that delivery may take
    up to 3 months.
  - Physical goods: 10/33 say the buyer pays shipping unless a free-shipping threshold or
    campaign applies; 8/33 say the seller is not liable if a named third-party recipient
    refuses; 5/33 make the buyer collect from the carrier's nearest branch when there is none
    locally; 5/33 count delivery as performed when nobody is at the address, at the buyer's
    cost; 5/33 name the carrier.
  - Digital content and services: 7/33 say there is no shipping and access is activated on
    payment, immediately or within a stated number of hours.
  - 2/33 cover pre-orders, counting the 30 days from the stated restock date.
- **Avoid:** 1/33 (an old template) says delivery may take up to 3 months. Law 6502 Art. 48(3)
  and Yönetmelik Art. 16(1) cap the delivery of goods at 30 days.
- **Quote:** "Sözleşme konusu ürün ve/veya ürünler, yasal 30 günlük süreyi aşmamak koşulu ile … teslim edilir." (s04)
- **Commonly omitted:** delivery to other countries (2/33); weekend and holiday handling (1/33).

### payment: Payment

- **Covers:** payment methods, how card instalments and bank campaigns work, the payment
  provider, and card-data handling.
- **Prevalence:** 20/34 (59%), common
- **Applies when:** always
- **Facts:** `facts.sales.payment_methods`, `facts.sales.payment_provider`
- **Patterns:**
  - 13/20 list the accepted methods (card, card instalments, bank transfer/EFT, wallets, gift
    card); 4/20 add bank transfer with the seller's bank details.
  - 5/20 name the payment institution and 3D Secure; 4/20 state card data is not stored by the
    seller.
  - 4/20 say bank instalments are the bank's credit, so the sale is a cash sale for the seller.
  - 4/20 explain that card refunds come back in the same instalments, through the bank.
  - 3/20 make extra instalments or deferrals offered by banks the bank's responsibility.
- **Quote:** "Kart bilgileri SATICI'nın sunucularında saklanmaz." (s18)
- **Commonly omitted:** cash on delivery (1/20); instalment fees.

### performance: Seller's performance, impossibility and force majeure

- **Covers:** the seller's duty to deliver as ordered, what happens when it cannot (out of
  stock, impossibility, force majeure), substitute goods, and payment as a precondition.
- **Prevalence:** 31/34 (91%), core
- **Applies when:** always
- **Facts:** `facts.tr.delivery`, `facts.sales.offer_type`
- **Patterns:**
  - 10/31 restate the impossibility rule: notify the buyer within 3 days and refund within 14.
  - 10/31 allow an equal-quality, equal-price substitute only with the buyer's consent; 1/31
    without a consent step.
  - 10/31 give the buyer a choice on force-majeure delay: cancel, take a substitute, or wait;
    6/31 list force-majeure events (weather, transport cuts, epidemics).
  - 12/31 make full payment a precondition of delivery; non-payment or a bank cancellation
    releases the seller.
  - 9/31 say the seller delivers the goods intact, with warranty documents and manuals.
  - 4/31 place the risk of loss on the seller until delivery.
- **Quote:** "ALICI, siparişin iptal edilmesini veya teslimat süresinin engelleyici durumunun ortadan kalkmasına kadar ertelenmesi haklarından birini kullanabilir." (s04)
- **Commonly omitted:** compensation beyond the refund; how the buyer is notified.

### inspection: Inspection on delivery and damaged goods

- **Covers:** the buyer's check of the parcel at handover, refusing damaged parcels, and how
  defective goods are handled.
- **Prevalence:** 19/34 (56%), common
- **Applies when:** `facts.sales.offer_type in [physical, mixed]`
- **Facts:** `facts.sales.offer_type`, `facts.tr.delivery`
- **Patterns:**
  - 12/19 tell the buyer to inspect at handover, refuse a damaged parcel and have the carrier
    write a damage report.
  - 8/19 deem an accepted parcel undamaged; 5/19 disclaim liability for damage once accepted.
  - 5/19 give a separate defect procedure (return form with photos, reply time, free pickup;
    a deadline to report defects, then repair, replacement or rescission) or reserve warranty
    rights, 1 with warranty repairs shipped at the seller's cost.
  - 3/19 write it as a second-person note at the end ("Lütfen dikkat").
- **Avoid:** 8/19 deem an accepted parcel undamaged, and 5/19 disclaim liability for damage once
  it is accepted. Law 6502 gives the buyer the defective-goods rights for two years from
  delivery, with no duty to report at handover (Arts. 8–12), and the seller bears loss and damage
  until delivery (Mesafeli Sözleşmeler Yönetmeliği Art. 17). The writer tells the buyer how to
  refuse a damaged parcel and leaves the defect rights whole.
- **Quote:** "Ürün kutusunun açık olması, hasarlı olması veya üzerinde sıvı lekesi bulunması, ürünlerde (eksik veya kırık/hasarlı ürün olması) olağan dışı durum olması veya yanlış ürün gelmiş olması durumlarında Alıcı veya siparişi teslim alan üçüncü kişi, kargoyu teslim almayarak, kargo görevlisine tutanak tutturma ve kargoyu reddetme hakkına sahiptir." (s10)
- **Commonly omitted:** the warranty period; who pays shipping for warranty repairs (stated
  by 1/19).

### order-limits: Consumer-only scope and order limits

- **Covers:** sales only to end consumers, business buyers, quantity caps, a minimum age, and
  the seller's right to cancel orders (bulk, obvious price errors, fraud suspicion).
- **Prevalence:** 15/34 (44%), common
- **Applies when:** `facts.tr.order_limits != []` or `facts.tr.business_buyers == true`
- **Facts:** `facts.tr.order_limits`, `facts.tr.business_buyers`
- **Patterns:**
  - 7/15 cap quantities per product or treat 3+ units as wholesale, with cancellation and
    refund.
  - 6/15 state the goods are sold only at retail to end consumers.
  - 6/15 cancel orders placed at a wrong price or disclaim price errors; 3/15 cancel on fraud
    suspicion.
  - 4/15 say a business buyer (tacir, company invoice) gets no consumer-specific rights.
  - 2/15 bar buyers under 18.
  - 5/15 phrase the seller's rights as "… hakkını saklı tutar".
- **Quote:** "Ürün fiyatlarının açık bir hata olduğu ortalama bir kişi tarafından anlaşılacak seviyede piyasa fiyatının çok altında yazılması durumunda, işbu hatalı fiyata göre verilen tüm siparişlerin SATICI tarafından iptal edilme hakkı vardır." (s13)
- **Commonly omitted:** how the buyer is told of a cancellation; the refund time for cancelled
  orders (2/15).

### subscription: Recurring orders and subscriptions

- **Covers:** recurring deliveries or subscriptions: billing per period, renewal, price
  changes, failed payments, and cancellation by either side.
- **Prevalence:** 2/34 (6%), rare
- **Applies when:** `facts.sales.subscription != none`
- **Facts:** `facts.sales.subscription`, `facts.sales.payment_provider`
- **Patterns:**
  - 2/2 bill at the start of each chosen period by card.
  - 1/2 announces the renewal date and amount in advance and lets the buyer stop renewal at
    any time; 1/2 cancels from the account page, irreversibly.
  - 1/2 treats each delivery as a separate distance sale with its own withdrawal period.
  - 2/2 handle failed payment: a warning, then termination or suspension (3 days; 30 days with
    data kept).
  - 1/2 charges later deliveries at the current site price; 1/2 lets the seller end the
    subscription without reason, refunding prepaid undelivered shipments.
- **Quote:** "Otomatik yenilemeli aboneliklerde yenileme tarihi ve tutarı önceden bildirilir; Müşteri yenilemeyi dilediği zaman durdurabilir." (s30)
- **Commonly omitted:** trial periods (offered elsewhere on the site by 2 more digital
  sellers).

### card-misuse: Unauthorised card use and chargebacks

- **Covers:** what happens when the bank does not pay because the card was used without
  authorisation, and chargebacks after delivery.
- **Prevalence:** 22/34 (65%), common
- **Applies when:** `facts.sales.payment_methods contains card` or `facts.sales.payment_methods contains card-instalments`
- **Facts:** `facts.sales.payment_methods`
- **Patterns:**
  - 13/22 require the buyer to return the goods within 3 days when the bank does not pay for
    unauthorised use not caused by the buyer; most put the shipping on the buyer, the common
    template on the seller.
  - 3/22 treat a chargeback after delivery as grounds to terminate, charge default interest
    and recover the goods.
  - 1/22 bars "bad-faith" chargebacks for a digital service and passes chargeback costs to the
    buyer; 1/22 leaves the case to the law and the payment institution.
  - 1/22 lets the seller ask for ID or a card statement when the cardholder is not the buyer,
    freezing the order and cancelling it after 24 hours.
  - 4/22 have this clause only in the common template's wording, inside otherwise own text.
- **Quote:** "…ALICI’nın kendisine teslim edilmiş olması kaydıyla ilgili ürünü 3(üç) gün içinde SATICI'ya iade etmesi zorunludur." (s17)
- **Commonly omitted:** what the seller refunds in that case.

### use-terms: Use of the site and the purchased service

- **Covers:** website-terms material inside the contract (liability for site failures, site
  changes, third-party links, IP) and rules on using a purchased digital service.
- **Prevalence:** 18/34 (53%), common
- **Applies when:** always
- **Facts:** `facts.product.has_accounts`, `facts.sales.offer_type`
- **Patterns:**
  - 11/18 carry website-terms clauses: exclusion of liability for site or app failures, the
    right to change the site without notice, third-party links, and IP in site content.
  - 6/18 (digital sellers) set service rules: use tied to the buying account, extra users,
    no resale of the output, buyer's own device and connection, suspension for abuse; 1 frames
    the sale as a software licence and bans copying and reverse engineering.
  - 3/18 add account and password security.
  - 1/18 adds an app chapter (device data processed, coupon terms).
- **Quote:** "Üretilen dokümanlar ALICI'nın mesleki kullanımı içindir; toplu olarak çoğaltılıp satılamaz." (s18)
- **Commonly omitted:** acceptable-use lists for user content (1/18).

### withdrawal: Right of withdrawal

- **Covers:** the withdrawal period and when it starts, how to give notice, returning the
  goods, return costs, refunds, and the buyer's liability for loss of value.
- **Prevalence:** 34/34 (100%), core
- **Applies when:** always
- **Facts:** `facts.tr.withdrawal_period_days`, `facts.tr.withdrawal_channels`, `facts.tr.return_shipping`, `facts.sales.return_address`, `facts.tr.immediate_performance_consent`, `facts.tr.business_buyers`, `facts.sales.offer_type`
- **Patterns:**
  - Period: 25/34 state 14 days from delivery (from contract formation for services); 2/34
    grant 30 days; 4/34 state no period and rely on an exception or a separate page; 2/34
    have only the common template's wording here.
  - 7/34 restate the start-day rules for split, multi-part and recurring deliveries; 4/34 say
    withdrawal is possible before delivery.
  - Notice channels: e-mail 15/34, account or order-page return button 8/34, phone or call
    centre 9/34, fax 6/34, registered post 4/34; 3/34 annex the model form.
  - Return shipping: 13/34 free through the seller's contracted carrier, at the buyer's cost
    through any other; 3/34 put all withdrawal costs on the seller with no carrier named; 2/34
    at the buyer's cost; the rest leave it unstated or to "the law".
  - Send-back deadline: 10 days after notice 9/34, 14 days 3/34; 1/34 instead has the seller
    take the goods back within 20 days (the pre-2014 rule).
  - Refund: within 14 days 15/34, within 10 days 4/34; 2/34 defer to "the statutory period".
  - 15/34 list return conditions (invoice, original box, accessories, resaleable); 7/34
    require a return invoice from company buyers.
  - 9/34 restate the buyer's liability for loss of value from use beyond inspection.
  - 5/34 cancel a campaign or free-shipping discount when a return drops the order below the
    threshold.
  - Digital and service sellers (7): all rely on the exception for performance started with
    consent; 4/7 never state the 14-day right; 2/7 offer a free trial or demo instead; 1/7
    refunds live classes pro rata, with the formula written out.
  - 2/34 read as a returns policy (seller approval, unopened box) rather than a withdrawal
    clause.
- **Avoid:** making withdrawal depend on unopened packaging, the original box or a resaleable
  condition: part of the 15/34 that list return conditions, and the 2/34 that read as a returns
  policy. Yönetmelik Art. 9 gives the right without reasons, and Art. 13(2) leaves the buyer
  liable only for loss of value beyond normal use. Only goods under Art. 15(1)(ç) and (e) lose the
  right once their packaging is opened (see *exceptions*). Asking for the accessories and the
  invoice with the return stays a pattern.
- **Quote:** "Alıcı, on dört gün içinde herhangi bir gerekçe göstermeksizin ve cezai şart ödemeksizin sözleşmeden cayma hakkına sahiptir." (s05)
- **Commonly omitted:** the one-year extension when the buyer was not informed (1/34); customs
  costs for foreign returns (2/34).

### personal-data: Personal data

- **Covers:** processing of the buyer's personal data for the order, data-subject rights, and
  consent to commercial electronic messages.
- **Prevalence:** 18/34 (53%), common
- **Applies when:** always
- **Facts:** `facts.tr.kvkk_notice_url`, `facts.marketing.email`
- **Patterns:**
  - Split: 7/18 one sentence or a link to the separate privacy policy and KVKK notice; 7/18 a
    full clause (purposes, recipient categories, rights under KVKK Art. 11); 2/18 one sentence
    allowing disclosure to authorities on a lawful request; 2/18 a confidentiality paragraph or
    a marketing-contact clause with no KVKK reference.
  - 9/18 cover commercial electronic messages; 2/18 say that consent is given separately from
    the contract and can be withdrawn at any time.
- **Avoid:** 4/18 (s07 s16 s19 s23) take marketing consent inside the contract, 2 of them (s07
  s16) for sharing data with group companies. The KVKK Board's explicit-consent guidance ("Açık
  Rıza Alırken Dikkat Edilecek Hususlar") holds that consent not limited to a specific subject is
  a blanket consent and invalid, and the Board's decision on making a service conditional on
  consent ("Hizmetin Açık Rıza Şartına Bağlanması") holds that consent tied to the contract is not
  freely given (PLAN.md decision 47). Law 6563 (Art. 6, 8) and the Ticari İletişim ve Ticari
  Elektronik İletiler Hakkında Yönetmelik require prior consent to commercial electronic messages,
  which the buyer can refuse at any time. The writer never builds consent into this contract;
  marketing consent goes to `tr-explicit-consent` (item 12) or a separate checkbox.
- **Quote:** "6.2. Ticari elektronik iletiler (SMS/E-posta) ALICI'nın sözleşmeden bağımsız vereceği açık rıza onayına (opt-in) tabidir." (s36)
- **Commonly omitted:** retention periods; data transfers abroad.

### exceptions: Withdrawal exceptions

- **Covers:** the goods and services for which the buyer has no right of withdrawal, and
  conditions such as unopened hygiene packaging.
- **Prevalence:** 34/34 (100%), core
- **Applies when:** always
- **Facts:** `facts.tr.withdrawal_exceptions`, `facts.sales.offer_type`, `facts.tr.immediate_performance_consent`
- **Patterns:**
  - Split: 15/34 copy the regulation's list (8 or more items) as a lettered or bulleted list;
    1/34 runs it into one paragraph with its own additions; 8/34 pick 2–6 items that fit their
    goods; 7/34 name a single exception (6 digital or service sellers: performance started
    with consent or instant digital delivery; 1 cosmetics seller: opened hygiene packaging);
    1/34 points to a separate page; 1/34 mentions only the hygiene rule inside another article.
  - 4/34 include the items added to the list from 2024 (phones, smartwatches, tablets,
    computers, drones, installed goods, live auctions).
  - 14/34 add examples or house rules for their own goods: cosmetics, underwear and swimwear;
    assembled flat-pack furniture; flowers and bundles; opened pet food; custom-cut DIY
    materials; electronic codes.
  - 4/34 add that unopened cosmetics, underwear or software remain returnable.
  - 1/34 declares special-day and campaign goods non-returnable.
- **Avoid:** excluding goods that the closed list in Yönetmelik Art. 15(1) does not name: 1/34
  declares special-day and campaign goods non-returnable, and a house rule among the 14/34 counts
  when it goes beyond the list. So does a listed category written without its condition:
  software, media and cosmetics are excepted only once their protective packaging is opened
  (Art. 15(1)(ç), (e)).
- **Quote:** "Cayma hakkı aşağıdaki hallerde kullanılamaz:" (s08)
- **Commonly omitted:** how the buyer is told at checkout that an item is excepted (2/34).

### loyalty: Loyalty points on returns

- **Covers:** loyalty points, coupons or gift cards earned or spent on an order, and what
  happens to them on return or cancellation.
- **Prevalence:** 4/34 (12%), rare
- **Applies when:** `facts.tr.loyalty_program != none`
- **Facts:** `facts.tr.loyalty_program`
- **Patterns:**
  - 3/4 claw back points earned on a returned order, first from other points and then from the
    refund.
  - 3/4 let the seller charge the buyer for points gained or used wrongly.
  - 2/4 re-credit points spent on a returned order as points, not cash; 2/4 say the scheme's
    own terms prevail.
- **Quote:** "Tüketici tarafından herhangi bir surette haksız ödül puanı kazanımı veya kullanımının tespit edildiği durumlarda, söz konusu ödül puanlarının parasal değeri SATICI tarafından tahsil edilebilir." (s28)
- **Commonly omitted:** expiry of points.

### default: Default

- **Covers:** the consequences when the buyer does not pay, including card default and
  suspension of a digital service.
- **Prevalence:** 15/34 (44%), common
- **Applies when:** always
- **Facts:** `facts.sales.payment_methods`, `facts.sales.subscription`
- **Patterns:**
  - 8/15 say a buyer in card default owes the bank interest under the card agreement and
    compensates the seller for late payment; 3/15 have only the common template's wording here.
  - 3/15 (digital sellers) suspend or end the service on non-payment, 1 keeping the data.
  - 1/15 sets a 7-day cure period for either party before termination.
- **Quote:** "ALICI’nın, kredi kartı ile yapmış olduğu işlemlerde temerrüde düşmesi halinde kart sahibi bankanın kendisi ile yapmış olduğu kredi kartı sözleşmesi çerçevesinde faiz ödeyecek ve bankaya karşı sorumlu olacaktır." (s19)
- **Commonly omitted:** the seller's own default (2/15).

### disputes: Disputes, evidence and governing law

- **Covers:** where consumer disputes go, the forum for business buyers, evidence rules, and
  the governing law.
- **Prevalence:** 34/34 (100%), core
- **Applies when:** always
- **Facts:** `facts.tr.merchant_court`, `facts.tr.business_buyers`, `facts.company.address`
- **Patterns:**
  - 30/34 name the provincial or district Tüketici Hakem Heyeti up to the monetary limit the
    Ministry sets each year, and the Tüketici Mahkemesi above it; 1/34 names only a city's
    courts; 2/34 have only the common template's wording here.
  - Place: 16/34 the buyer's residence or the place of purchase; 12/34 add the seller's
    domicile, 1 of them making it the only forum.
  - 7/34 add a named city's courts, mostly for business buyers.
  - 4/34 mention mediation before suing in the consumer court.
  - 10/34 add an evidence clause making the seller's books and electronic records (logs, IP,
    voice recordings) conclusive evidence; 7 of them cite HMK Art. 193.
  - 5/34 state that Turkish law applies.
- **Avoid:**
  - One court as the only forum for consumer disputes: 1/34 the seller's domicile, 1/34 a named
    city's courts. Law 6502 Art. 73(5) lets the consumer sue where they live, and HMK Art. 18(2)
    allows forum agreements only between merchants or public bodies. A named city for business
    buyers stays a pattern.
  - Monetary limits as figures from a past year (the common template gives those of 2014). The
    Ministry sets the limits each year; the writer refers to them, or gives the current year's.
- **Quote:** "İşbu Sözleşme’den kaynaklanan uyuşmazlıklarda, Ticaret Bakanlığı’nca her yıl ilan edilen parasal sınırlar dâhilinde tüketici hakem heyetleri ile ALICI’nın veya SATICI’nın yerleşim yerindeki Tüketici Mahkemeleri yetkilidir." (s14)
- **Commonly omitted:** the current monetary limits as figures (only the common template gives
  figures, those of 2014).

### formation: Formation and entry into force

- **Covers:** how and when the contract is concluded, the acceptance act, where the buyer gets
  a copy, and notices.
- **Prevalence:** 32/34 (94%), core
- **Applies when:** always
- **Facts:** `facts.tr.acceptance_mechanism`, `facts.tr.contract_copy`, `facts.tr.pre_info_form`
- **Patterns:**
  - 22/32 make the contract effective when the buyer approves it electronically; 4/32 at
    payment approval; 2/32 on sign-up as a member; 1/32 (an old template) when the buyer posts
    or faxes a signed copy.
  - 9/32 name the act: ticking a checkbox at checkout, or clicking the order or payment button.
  - 9/32 say the contract is e-mailed with the order confirmation or kept in the account; 3
    of them give a retention period (3 years).
  - 7/32 end with "the buyer is deemed to accept by ordering".
  - 6/32 state the number of articles; 4/32 name e-mail and SMS as the channel for notices.
  - 1/32 says mandatory law and the term more favourable to the consumer prevail over the
    contract.
- **Quote:** "Sipariş özeti ve sözleşme metni ALICI'nın e-posta adresine iletilir; ayrıca bu sayfadan her zaman erişilebilir." (s18)
- **Commonly omitted:** the language of the contract; how the buyer can correct input errors
  before ordering (1/32).

### signature: Signature block

- **Covers:** the closing lines naming the parties and the date.
- **Prevalence:** 16/34 (47%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`
- **Patterns:**
  - 12/16 end with "SATICI / ALICI / Tarih" lines, the seller filled and the buyer and date
    filled per order.
  - 3/16 repeat the seller's contact block after the last article instead.
- **Quote:** "Tarih: Sipariş tarihi itibarıyla geçerlidir." (s32)
- **Commonly omitted:** any signature for the buyer beyond the electronic acceptance.

### withdrawal-form: Model withdrawal form

- **Covers:** an annexed withdrawal form the buyer can fill in and send.
- **Prevalence:** 3/34 (9%), rare
- **Applies when:** `facts.tr.withdrawal_channels contains form`
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`
- **Patterns:**
  - 3/3 reproduce the regulation's model form: addressee, a one-line declaration, then order
    and delivery date, goods, price, buyer's name and address, signature (paper only), date.
  - 1/3 adds the seller's KEP address to the addressee block.
- **Quote:** "Bu formla aşağıdaki malların satışına ilişkin sözleşmeden cayma hakkımı kullandığımı beyan ederim." (s28)
- **Commonly omitted:** instructions on where to send the form beyond the addressee block.

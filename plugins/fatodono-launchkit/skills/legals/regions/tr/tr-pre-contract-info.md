---
doc_id: tr-pre-contract-info
title: Ön Bilgilendirme Formu (pre-contract information form)
kind: document
family: commerce
region: tr
part: whole
sample_languages: [tr]
sample_count: 20
saturated: true
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** The form an online seller shows a consumer in Turkey before the distance sales
  contract is made: who the seller is, what is sold at what total price, how it is paid for and
  delivered, whether and how the buyer can withdraw, and where complaints and disputes go.
- **Shape:**
  - 18/20 a stand-alone page (footer or checkout link "Ön Bilgilendirme Formu"); 2/20 a block
    or the whole text on a page titled "Satış Sözleşmesi". Median about 1,430 words (range
    180–4,200); 4/20 are under 500 words, 2 of them from sellers of digital services.
  - 9/20 number their articles "MADDE 1 – …"; 11/20 use plain numbered headings. Decimal
    sub-clauses are the norm.
  - 16/20 are the order-time template: blank buyer and order fields or checkout tokens
    (`{_saticiunvan_}`, `%FATURA_AD_SOYAD%`, `{{ vendor.title }}`, `[Fiyat]`) filled per
    order; 4/20 are general text with no order fields and point to the order screen.
  - 6/20 append the model withdrawal form (see *withdrawal-form*).
  - 1/20 (a marketplace) repeats the form once per seller in the cart, then one order summary.
- **Register:** formal legal Turkish in 17/20: third person, SATICI and ALICI (or Tüketici) in
  capitals, long clauses, many ending "kabul, beyan ve taahhüt eder". 3/20 (short digital,
  pet-shop and perishable-goods forms) use brief plain lines. 6/20 slip into "siz" in a delivery, return or
  data clause. Day counts are written as digits plus words ("14 (on dört) gün").
- **Recurring elements:**
  - Law 6502 named: 17/20; the Mesafeli Sözleşmeler Yönetmeliği by name: 18/20, with its
    Official Gazette date and number 5/20.
  - A definitions block (site, seller, consumer, product, contract, pre-order) at the top: 5/20.
  - Seller contact details repeated in the withdrawal, complaints or model-form part: 7/20.
  - A signature and date block (SATICI / ALICI / TARİH, or consumer name and date fields):
    7/20. It gives the buyer no fact, so it is layout, not a section (`research/…/merge.md`,
    accepted 2026-10-27); the writer adds one only when the checkout records it.
  - An update or effective date: 4/20.
  - Contract-style general provisions (card misuse, seller cancellation, site disclaimers)
    inside the form: 8/20, mostly in the wording of two widely circulated templates.
  - 5/20 still name a repealed law (4077), its 2012–2014 monetary limits or a former ministry
    name; 7/20 published drafting errors (duplicated articles, a wrong article number, "SATICI"
    where the buyer is meant). Recorded as observed, not as a legal judgement.
- **Commonly omitted:** a version or date line (16/20); the current consumer-arbitration limit as
  a figure (18/20); the model withdrawal form (14/20); personal-data content (12/20); how to
  correct input errors before ordering (17/20; 3/20 give a phone or e-mail for it); the
  seller's chamber membership and code of conduct (19/20); a list of related documents (19/20).

Counts come from the 20 samples in `research/regions/tr/tr-pre-contract-info/`. Every sample
counts for prevalence; in patterns, each template's wording counts once however many samples
carry it (`research/…/merge.md`, *Copies*). Patterns record what sellers write, including where
it restates the law; they are not legal advice. The form and the distance sales contract
(`regions/tr/tr-distance-sales.md`) cover many of the same facts; the writer fills both from the
same fact values so they never disagree.

## Sections

### subject: Subject and legal basis

- **Covers:** what the form is for (informing the consumer before the distance contract), what
  is sold through which site or app, and the law it is issued under.
- **Prevalence:** 18/20 (90%), core
- **Applies when:** always
- **Facts:** `facts.product.name`, `facts.product.services_in_scope`, `facts.sales.offer_type`
- **Patterns:**
  - Most write one sentence: "İşbu Ön Bilgilendirme Formu'nun konusu, ALICI'nın …
    bilgilendirilmesidir", naming the site and the law; 2 share one template sentence.
  - 4/18 put it as an untitled preamble above the first article; 1/18 only as a subtitle naming
    the regulation article.
  - 2/18 state here that the form is an integral part of the distance sales contract (see
    *formation*).
  - 2/18 add the pre-order case: shipping starts from the restock date on the product page.
  - 1/18 (an authorised reseller) opens by saying it sells only as the brand's reseller (see
    *marketplace*).
- **Quote:** "İşbu Ön Bilgilendirme Formu; 6502 sayılı Tüketicinin Korunması Hakkında Kanun, Mesafeli Sözleşmeler Yönetmeliği ve yürürlükte bulunan ilgili mevzuat kapsamında Tüketici'nin sözleşme kurulmadan önce bilgilendirilmesi amacıyla hazırlanmıştır." (s12)
- **Commonly omitted:** the regulation's article numbers (cited by 4/18); the app as a sales
  channel (named by 2/18).

### parties: Seller and buyer details

- **Covers:** the seller's trade name, address, contact channels and registration numbers, and
  the buyer's, recipient's and invoice details as fields filled per order.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.company.phone`, `facts.tr.seller_registry`, `facts.sales.return_address`
- **Patterns:**
  - 19/20 a label/value block (Unvanı, Adresi, Telefon, E-posta, MERSİS No); 16/20 fill it,
    4/20 leave it blank or as tokens for the checkout.
  - Seller identifiers: MERSİS 13/20, tax office and number 6/20, fax 8/20, KEP 6/20.
  - Buyer: 12/20 blank per-order fields (name, address, phone, e-mail, delivery and invoice
    address); 1/20 one sentence saying the buyer is the registered member; 7/20 no buyer block.
  - 3/20 call the seller "hizmet sağlayıcı" or "aracı hizmet sağlayıcı" instead of SATICI,
    without a marketplace role.
  - 3/20 add a separate return, notice or showroom address; 1/20 adds that the given addresses
    are those for legal notices.
- **Quote:** "Müşteri olarak kaganparfumeri.com alışveriş sitesine üye olan kişi, üye olurken kullanılan adres ve iletişim bilgileri esas alınır." (s08)
- **Commonly omitted:** KEP address (14/20); trade registry number (19/20).

### marketplace: Platform or reseller role

- **Covers:** when the site is a marketplace, the intermediary platform's identity next to the
  seller's and how payment to the platform works; when the seller is a brand's reseller, that
  role.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.tr.sales_model == marketplace`
- **Facts:** `facts.tr.sales_model`, `facts.company.legal_name`
- **Patterns:**
  - 1/2 (a marketplace) gives an "Aracı Hizmet Sağlayıcı" block next to each seller's block and
    says paying the platform discharges the price owed to the seller.
  - 1/2 (a brand's authorised reseller on the brand's own site) states that role in the opening
    sentence.
- **Quote:** "Alıcı Malın Bedelini Idefıx'e Ödemekle, Ürün Bedelini Satıcı’ya Ödemiş Sayılacak Ve Bir Daha Ödeme Yükümlülüğü Altına Girmeyecektir." (s04)
- **Commonly omitted:** how withdrawal works against the platform (stated by neither).

### goods-price: Goods, total price and order details

- **Covers:** the main characteristics of the goods or service, the total price including taxes,
  shipping and other charges, and the order's delivery and invoice details.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.sales.offer_type`, `facts.sales.taxes`, `facts.tr.delivery`, `facts.sales.payment_methods`
- **Patterns:**
  - Split: 13/20 an order table or field block filled per order (product, quantity,
    VAT-inclusive unit price, shipping fee, total, payment method, delivery and invoice
    address); 7/20 point to the product page or the order screen the buyer confirms instead
    (1 of them circularly, to the form itself).
  - 8/20 open with a sentence naming the product facts ("türü, miktarı, marka/modeli, rengi,
    adedi, tüm vergiler dahil satış bedeli") "as shown below" or "on the order page".
  - 6/20 state outright that the total includes all taxes and costs and nothing more is charged.
  - Digital and service sellers (4) describe what is sold: package, scope, duration, modules
    and their limits.
  - 3/20 give the channel for correcting order-entry errors here (phone or e-mail).
  - Warning that confirming the order creates a duty to pay the price, shipping and taxes: 5/20,
    as its own short article (2), in the subject (1) or in the acknowledgement (2); the writer
    adds it to *pre-info-ack* (`research/…/merge.md`, `payment-duty`).
- **Quote:** "Tüketici tarafından ödenecek ürün bedeli, kargo / teslimat bedeli ve varsa diğer yasal masraflar, sipariş onaylanmadan önce açıkça gösterilir." (s12)
- **Commonly omitted:** discount and coupon lines (3/20); a worked example of the total.

### payment: Payment

- **Covers:** payment methods, card instalments and bank campaigns, transfer deadlines and bank
  details, the payment provider, and invoicing.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.sales.payment_methods`, `facts.sales.payment_provider`, `facts.tr.business_buyers`
- **Patterns:**
  - 18/20 list the accepted methods (card, instalments, bank transfer/EFT, wallets, cash on
    delivery); 2/20 only say the method chosen at checkout applies.
  - 4/20 give the seller's bank and IBAN for transfers or refunds; 2/20 cancel an order whose
    transfer has not arrived within a set number of business days.
  - 3/20 say instalments, deferrals and their costs are the bank's or the wallet's matter.
  - 3/20 name the payment provider; 1/20 says card data is not stored by the seller.
  - 5/20 cover the invoice: sent with the parcel or by e-mail, individual or company invoice.
  - 1/20 bans instalments for one product category, citing the banking rule.
- **Quote:** "Kart bilgileri sistemimizde saklanmaz." (s14)
- **Commonly omitted:** instalment fees as figures; cash-on-delivery fees.

### price-validity: Validity of prices and offers

- **Covers:** how long the listed prices, campaign prices and the pre-contract information stay
  valid.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** always
- **Facts:** `facts.sales.promotions`
- **Patterns:**
  - 6/9 carry one template sentence: listed prices hold until updated, time-limited prices
    until the stated end (counted once in wording); 1 of them repeats it in a second article.
  - 1/9 says the information holds until the order is confirmed and then becomes part of the
    contract; 1/9 gives the validity of written offers.
  - 1/9 adds what happens to an order placed at a mispriced item (see *order-limits*).
- **Quote:** "Süreli olarak ilan edilen fiyatlar ise belirtilen süre sonuna kadar geçerlidir." (s07)
- **Commonly omitted:** a fixed validity period in days (0/9).

### delivery: Delivery or performance

- **Covers:** where and when goods are delivered or a digital service is activated, the legal
  maximum, carriers, shipping cost, store pickup and pre-orders.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.tr.delivery`, `facts.sales.offer_type`
- **Patterns:**
  - 13/20 restate the 30-day maximum (1/20 promises 14 days); 3/20 give a shop-wide dispatch
    window in business days; the digital sellers instead say access is activated on payment
    (4/4).
  - 10/20 say who pays shipping: the buyer unless a free-shipping threshold or campaign applies
    (most), or the fee per named carrier (2).
  - 6/20 name the carrier.
  - 6/20 say the seller is not liable if a named third-party recipient is absent or refuses,
    and deem the order delivered then.
  - 3/20 cover pre-orders (30 days from the restock date); 1/20 click-and-collect with a code
    and automatic cancellation if uncollected; 1/20 extra cost for several addresses.
- **Quote:** "Hizmet, dijital nitelikte olduğundan kargo ile teslim edilmez; ödemenin onaylanmasının ardından ALICI’nın Platform üzerindeki hesabına elektronik ortamda anında veya makul süre içinde tanımlanarak ifa edilir." (s02)
- **Commonly omitted:** delivery abroad (2/20); weekend and holiday handling.

### digital-content: Using digital content and software

- **Covers:** what the buyer needs to use the product: functionality and technical requirements
  of digital content or software, technical protection measures, where its data is kept, and
  usage instructions.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.sales.offer_type in [digital-content, service, mixed]`
- **Facts:** `facts.product.system_requirements`, `facts.product.activation`, `facts.data.storage_locations`
- **Patterns:**
  - 3/4 name the connection or device the buyer must supply and put connectivity on the buyer.
  - 1/4 (on-premise software) says where customer data lives, what is sent to the vendor, the
    licence check and technical protection measures, and that backups are the buyer's duty.
  - 1/4 echoes the regulation's headings (functionality, technical protection measures) but
    fills them with equipment advice and disclaimers.
  - 1/4 (physical goods) points to the manual and labels for usage instructions.
- **Quote:** "Söz konusu internet bağlantısının sağlanması, kalitesi ve güvenliği KULLANICI sorumluluğundadır." (s09)
- **Commonly omitted:** interoperability with other hardware or software (0/4).

### use-terms: Use of purchased content

- **Covers:** rules on using what is bought (no copying or downloading course material, IP in
  the content) and website-terms material placed in the form.
- **Prevalence:** 5/20 (25%), rare
- **Applies when:** `facts.sales.offer_type in [digital-content, service, mixed]`
- **Facts:** `facts.sales.offer_type`, `facts.company.published_policies`
- **Patterns:**
  - 3/5 carry website-terms clauses (liability for site failures, site changes, third-party
    links, IP in site content) that belong in the terms of service; the writer links the terms
    instead.
  - 2/5 bar copying or downloading purchased works or course documents; 1/5 points to a licence
    agreement for the usage right.
- **Commonly omitted:** everything for physical goods.

### after-sales: Warranty and after-sales support

- **Covers:** warranty documents and periods, the seller's own guarantees, and the after-sales
  support channel.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.tr.after_sales != none`
- **Facts:** `facts.tr.after_sales`, `facts.product.support`
- **Patterns:**
  - 2/4 give warranty periods or point to the statutory warranty (1 with separate periods for
    new and used hardware).
  - 1/4 gives a freshness or expiry-date guarantee and points to the terms of use for it.
  - 2/4 name a technical-support or after-sales channel; 1/4 handles printing defects by
    replacement at the seller's choice.
- **Commonly omitted:** who pays shipping for warranty repairs.

### inspection: Inspection on delivery and damaged goods

- **Covers:** the buyer's check of the parcel at handover, refusing damaged parcels, and how to
  report wrong, damaged or missing items.
- **Prevalence:** 10/20 (50%), common
- **Applies when:** `facts.sales.offer_type in [physical, mixed]`
- **Facts:** `facts.sales.offer_type`, `facts.tr.delivery`
- **Patterns:**
  - 7/10 tell the buyer to inspect at handover, refuse a damaged parcel and have the carrier
    write a damage report; 4/10 deem an accepted parcel undamaged.
  - 1/10 addresses the buyer directly with advice ("kargo tutanağını imzalamadan önce …").
  - 1/10 (perishable goods) sets a notice window in hours for wrong or damaged items and deems
    silence acceptance.
  - 1/10 reminds the buyer that the seller delivers with warranty papers and manuals.
- **Avoid:** 4/10 deem an accepted parcel undamaged, and 1/10 (perishable goods) deems silence
  after a few hours acceptance. Law 6502 gives the buyer the defective-goods rights for two years
  from delivery, with no duty to report at handover (Arts. 8–12), and the seller bears loss and
  damage until delivery (Mesafeli Sözleşmeler Yönetmeliği Art. 17). The writer tells the buyer
  how to refuse a damaged parcel and leaves the defect rights whole.
- **Quote:** "ALICI, Ürün'ü teslim aldığı anda kontrol etmekle ve üründe kargodan kaynaklanan bir sorun gördüğünde, ürünü kabul etmemekle ve kargo firması yetkilisine tutanak tutturmakla sorumludur." (s07)
- **Commonly omitted:** the deadline for reporting hidden defects.

### performance: Seller's performance, impossibility and force majeure

- **Covers:** what happens when the seller cannot deliver on time or at all: notice, substitute
  goods, force-majeure delay, the buyer's right to cancel, and the refund.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** always
- **Facts:** `facts.tr.delivery`, `facts.sales.offer_type`
- **Patterns:**
  - 6/13 restate the impossibility rule: tell the buyer within 3 days and refund within 14.
  - 6/13 allow an equal-quality, equal-price substitute only with the buyer's consent.
  - 4/13 give the buyer a choice on force-majeure delay (cancel, substitute or wait); 3/13 just
    exclude the seller's liability.
  - 4/13 let the buyer cancel when the seller fails to deliver in time.
  - 5/13 add how long a card refund takes to reach the account and disclaim bank delays.
- **Quote:** "SATICI'nın haklı bir sebep olmaksızın teslim yükümlülüğünü yerine getirmemesi durumunda, ALICI siparişini iptal etmek suretiyle sözleşmeyi feshedebilir." (s07)
- **Commonly omitted:** compensation beyond the refund.

### card-misuse: Unpaid card payments and chargebacks

- **Covers:** what happens when the bank does not pay over the price because the card was used
  without authorisation, a chargeback after delivery, or card or instalment default.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** `facts.sales.payment_methods contains card` or `facts.sales.payment_methods contains card-instalments`
- **Facts:** `facts.sales.payment_methods`
- **Patterns:**
  - 6/8 require the buyer to return the goods within 3 days when the bank does not pay (one
    template's wording, counted once, plus own variants).
  - 4/8 make full payment a condition of delivery; non-payment or a bank cancellation frees the
    seller.
  - 2/8 say card default is between the buyer and the bank and the buyer answers for the
    seller's loss from late payment.
- **Quote:** "Ürün teslimatı sonrasında herhangi bir sebepten dolayı, işlem yapılan kredi kartının ait olduğu banka/finans kuruluşunun Ürün bedelini SATICI'ya ödememesi halinde, Ürün en geç 3 gün içinde ALICI tarafından tüm giderleri ALICI’ya ait olmak üzere SATICI'ya iade edilir." (s04)
- **Commonly omitted:** what the seller refunds in that case.

### order-limits: Consumer-only scope and order cancellation

- **Covers:** that consumer rights apply only to consumers, rules for business buyers, minimum
  age, delivery area, and the seller's right to cancel orders (fraud, resale, price errors).
- **Prevalence:** 9/20 (45%), common
- **Applies when:** `facts.tr.order_limits != []` or `facts.tr.business_buyers == true`
- **Facts:** `facts.tr.order_limits`, `facts.tr.business_buyers`
- **Patterns:**
  - 4/9 limit the consumer-protection clauses to buyers who are consumers (2 in one template
    sentence).
  - 3/9 cancel orders placed at an obvious price error, 1 of them limiting the seller: stock-out
    or internal reasons are no ground and the buyer may keep the order at the right price.
  - 3/9 cancel on fraud or resale suspicion, with a refund.
  - 2/9 exclude delivery abroad; 1/9 bars buyers under 18.
- **Quote:** "İşbu madde, Satıcı'ya keyfi veya gerekçesiz sipariş iptal hakkı vermez …" (s12)
- **Commonly omitted:** how the buyer is told of a cancellation.

### withdrawal: Right of withdrawal

- **Covers:** the withdrawal period and when it starts, how to give notice, returning the goods,
  return costs, refunds, and the buyer's liability for loss of value.
- **Prevalence:** 17/20 (85%), core
- **Applies when:** always
- **Facts:** `facts.tr.withdrawal_period_days`, `facts.tr.withdrawal_channels`, `facts.tr.return_shipping`, `facts.sales.return_address`, `facts.tr.immediate_performance_consent`, `facts.sales.offer_type`
- **Patterns:**
  - 14/17 state 14 days from delivery (from contract formation for services); 3/17 (digital or
    service sellers) state the right and then the exception for performance started with
    consent.
  - 8/17 restate the start-day rules for split, multi-part and regular deliveries; 3/17 say
    withdrawal is possible before delivery.
  - Notice channels: e-mail most often, then phone or call centre, the account's return flow,
    registered post or fax; 6/17 point to the annexed model form; 1/17 offers an online form.
  - Return shipping: 5/17 on the seller (through its contracted carrier, or all costs); 1/17 on
    the buyer except short-dated or faulty goods; 1/17 states both.
  - 4/17 add return conditions stricter than the law (unopened, original box, invoice
    original); 1/17 a shorter seller window for wrong-order returns beside the statutory right;
    1/17 says opening the box alone does not lose the right.
  - 2/17 offer goodwill refunds beyond the law (24 hours; partial for courses).
  - 1/17 repeats the whole withdrawal block later in the form, with small differences.
  - 3/20 have no withdrawal section: a block that leaves it to the contract below, a perishable
    seller and a digital seller that state only the exception (see *exceptions*).
- **Avoid:** making withdrawal depend on unopened packaging or the original box: part of the
  4/17 (s05 s06 s07 s13) with conditions stricter than the law. Yönetmelik Art. 9 gives the right
  without reasons, and Art. 13(2) leaves the buyer liable only for loss of value beyond normal
  use. Only goods under Art. 15(1)(ç) and (e) lose the right once their packaging is opened (see
  *exceptions*). Asking for the invoice with the return stays a pattern.
- **Quote:** "Tüketici, ürün kendisine teslim edilmeden önce de cayma hakkını kullanabilir." (s12)
- **Commonly omitted:** the one-year extension when the buyer was not informed (1/17).

### exceptions: Withdrawal exceptions

- **Covers:** the goods and services with no right of withdrawal, or a statement that the right
  does not apply to what is sold.
- **Prevalence:** 19/20 (95%), core
- **Applies when:** always
- **Facts:** `facts.tr.withdrawal_exceptions`, `facts.sales.offer_type`, `facts.tr.immediate_performance_consent`
- **Patterns:**
  - Split: 10/19 copy the regulation's full list (a–h, or a–k with the newer items); 9/19 pick
    the items that fit their goods, 5 of them a single exception (perishables, instant digital
    content or a service started with consent, opened protective packaging).
  - 2/19 include the items added from 2024 (phones, smartwatches, tablets, computers, vehicles,
    installed goods).
  - 3/19 add examples from their own range in brackets (jewellery, pet food, custom-cut
    worktops, paint mixes); 2/19 add own categories (custom-made goods; an older list of
    software, media and cosmetics).
  - Digital and service sellers (4/4) rely on the exception for instant digital delivery or a
    service started with consent; 1/4 says the buyer gives that consent separately at checkout,
    1/4 states the exclusion flatly without the consent condition. Only a service started before
    the period ends needs that consent (Art. 15(1)(h)); instant digital delivery does not (ğ).
- **Avoid:** listing a category the closed list of Yönetmelik Art. 15(1) does not name, or a
  listed one without its condition: 1/19 (s05) gives an older list that excludes software, media
  and consumables outright, which Art. 15(1)(e) excepts only once their protective packaging is
  opened.
- **Quote:** "Mesafeli Sözleşmeler Yönetmeliği'nin 15. maddesi uyarınca aşağıdaki ürünlerde cayma hakkı kullanılamaz:" (s14)
- **Commonly omitted:** how the buyer is told at checkout that an item is excepted.

### loyalty: Loyalty points on returns

- **Covers:** loyalty points, gift vouchers and campaign benefits on withdrawal or cancellation.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** `facts.tr.loyalty_program != none`
- **Facts:** `facts.tr.loyalty_program`
- **Patterns:**
  - 1/1 claws back points earned on a returned order, re-credits points spent as points, and
    refuses cash for points.
  - Campaign discount clawback when a return drops the order below a threshold sits in
    *withdrawal* in 3 more samples.
- **Quote:** "Satıcı'dan kazanılan veya Satıcı nezdinde kullanılan ödül puanları, hediye çekleri gibi mukabili nakdi para talepleri, hiçbir durumda ve surette kabul edilmez." (s07)
- **Commonly omitted:** expiry of points.

### personal-data: Personal data

- **Covers:** how the buyer's personal data is processed for the order, or a pointer to the KVKK
  notice, and how marketing consent is handled.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** always
- **Facts:** `facts.tr.kvkk_notice_url`, `facts.marketing.email`
- **Patterns:**
  - Split: 4/8 one sentence pointing to the separate KVKK Aydınlatma Metni (1 adding a data
    annex); 3/8 a short inline notice (controller, data categories, purposes, recipients such as
    carriers), 1 of them pointing to a fuller notice at checkout; 1/8 only a clause on
    disclosure to authorities on lawful request.
  - 1/8 says accepting the form or the contract is not consent to marketing or commercial
    messages, which are asked for separately.
  - 1/8 adds the statutory retention period for transaction records.
- **Avoid:** 1/20 (s01) builds a deemed, blanket consent to data use and commercial messages
  (covering group companies and third parties) into the form. The KVKK Board's explicit-consent
  guidance ("Açık Rıza Alırken Dikkat Edilecek Hususlar") holds that consent not limited to a
  specific subject is a blanket consent and invalid, and the Board's decision on making a service
  conditional on consent ("Hizmetin Açık Rıza Şartına Bağlanması") holds that asking for consent
  to processing that rests on another legal basis (performing the contract) misleads the person,
  and that consent tied to the contract is not freely given (PLAN.md decision 47). The writer
  never builds consent into this form; marketing consent goes to `tr-explicit-consent` (item 12) or a
  separate checkbox.
- **Quote:** "Tüketici'nin Ön Bilgilendirme Formu'nu veya Mesafeli Satış Sözleşmesi'ni kabul etmesi, tek başına pazarlama amaçlı kişisel veri işlemeye veya ticari elektronik ileti almaya açık rıza verdiği anlamına gelmez." (s12)
- **Commonly omitted:** data transfers abroad; data-subject rights (listed by 1/8, s01).

### complaints: Complaints channel

- **Covers:** how and where the buyer sends complaints and requests to the seller.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** always
- **Facts:** `facts.company.contact_email`, `facts.company.phone`, `facts.company.address`
- **Patterns:**
  - 4/13 a section of its own; 6/13 a clause opening the disputes article ("first to the
    seller, then …"); 2/13 a clause in the delivery or general provisions; 1/13 only complaint
    fields in the seller block.
- **Quote:** "Alıcı, verilen hizmetler ile ilgili talep ve şikâyetlerini, Satıcı'nın yukarıda belirtilen posta veya elektronik posta adresine yapabilir." (s06)
- **Commonly omitted:** a reply time.

### subscription: Duration and renewal

- **Covers:** how long the contract runs (one-off or recurring), renewal, and what cancelling
  does.
- **Prevalence:** 3/20 (15%), rare
- **Applies when:** `facts.sales.subscription != none`
- **Facts:** `facts.sales.subscription`, `facts.sales.payment_provider`
- **Patterns:**
  - 1/3 states the sale is one-off with no term (the regulation's duration item).
  - 1/3 (a software licence) gives the support period, how renewal is priced and requested, and
    that nothing renews automatically.
  - 1/3 (a subscription) says the service runs to the end of the paid term after cancelling,
    with no refund.
- **Quote:** "İptal edildiğinde kalan süre boyunca hizmet devam eder, ücret iadesi yapılmaz." (s18)
- **Commonly omitted:** the minimum term and price changes on renewal.

### pre-info-ack: Acknowledgement of pre-contract information

- **Covers:** the buyer's statement that it read the pre-contract information and confirmed it
  electronically, and that ordering creates a duty to pay.
- **Prevalence:** 16/20 (80%), core
- **Applies when:** always
- **Facts:** `facts.tr.acceptance_mechanism`
- **Patterns:**
  - 10/16 near the end; 3/16 inside the general provisions; 3/16 at the top, 2 of them
    repeating it at the end.
  - Many list the topics confirmed (main features, tax-inclusive price, payment, delivery,
    seller's name and address, withdrawal) inside the sentence; 1/16 as a bulleted checklist.
  - 2/16 cite Law 6502 Art. 48(2) and regulation Arts. 5–7 in one template sentence.
  - 5/20 add the payment-duty warning here or next to it (see *goods-price*).
- **Quote:** "Tüketici, işbu ön bilgilendirme formunu elektronik ortamda okuyup bilgi sahibi olduğunu kabul ve beyan eder." (s14)
- **Commonly omitted:** the date and time of confirmation.

### copy: Copy of the form and contract

- **Covers:** how the buyer receives and can later reach the form and contract, and how long the
  seller keeps them.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** always
- **Facts:** `facts.tr.contract_copy`
- **Patterns:**
  - 4/8 keep them in the buyer's account ("Hesabım") or on the site; 2/8 e-mail them with the
    order confirmation; 1/8 sends them on a durable medium after the order.
  - 3/8 say the seller keeps the records, 1 for 3 years.
- **Quote:** "İşbu Form ve Mesafeli Satış Sözleşmesi’nin bir örneği, sipariş onayı ile birlikte ALICI’nın bildirdiği e-posta adresine gönderilir ve ALICI hesabı üzerinden erişilebilir hâlde tutulur." (s02)
- **Commonly omitted:** the format of the copy (PDF, e-mail body).

### disputes: Disputes

- **Covers:** where consumer disputes go (consumer arbitration committee, consumer court),
  monetary limits, mediation, the forum for business buyers, and the fallback law.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.tr.merchant_court`, `facts.tr.business_buyers`, `facts.company.address`
- **Patterns:**
  - 14/20 refer to the limits the Ministry sets each year without figures; 2/20 give the current
    limit in TL; 2/20 give dated limits under old law; 2/20 name no limit.
  - Place: the buyer's residence or place of purchase in most; a few add the seller's domicile.
  - 3/20 say mediation comes before the consumer court.
  - 3/20 name a city's courts for business buyers; 1/20 names one for all disputes.
  - 2/20 add that Law 6502 governs anything the form does not cover.
- **Avoid:**
  - One city's courts for all disputes: 1/20. Law 6502 Art. 73(5) lets the consumer sue where
    they live, and HMK Art. 18(2) allows forum agreements only between merchants or public
    bodies. A named city for business buyers stays a pattern.
  - Monetary limits from repealed law or a past year: 2/20 (s08 s15). The Ministry sets the
    limits each year; the writer refers to them, or gives the current year's.
- **Quote:** "Tüketici mahkemelerine başvurmadan önce arabuluculuk kurumuna başvurulması kanunen zorunludur." (s13)
- **Commonly omitted:** the current limit as a figure (18/20).

### formation: Relation to the contract

- **Covers:** that the form is accepted electronically before the contract step, becomes part of
  the distance sales contract, and when the contract forms.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** always
- **Facts:** `facts.tr.acceptance_mechanism`, `facts.tr.pre_info_form`
- **Patterns:**
  - 4/13 one template sentence: the contract step follows only after the form is read and
    accepted electronically.
  - 4/13 make the form an annex and integral part of the contract.
  - 2/13 deem every buyer who orders to accept the contract; 1/13 accepts form and contract in
    one sentence.
  - 1/13 says the contract forms when card details are entered and the order is placed.
  - 1/13 ends with one line that the form was read and confirmed electronically.
- **Quote:** "İşbu Ön Bilgilendirme Formu, taraflar arasında elektronik ortamda kurulacak Mesafeli Satış Sözleşmesi'nin eki ve ayrılmaz bir parçasıdır." (s12)
- **Commonly omitted:** where the contract itself is shown.

### withdrawal-form: Model withdrawal form

- **Covers:** an annexed withdrawal form the buyer can fill in and send.
- **Prevalence:** 6/20 (30%), rare
- **Applies when:** `facts.tr.withdrawal_channels contains form`
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.tr.seller_registry`
- **Patterns:**
  - 6/6 reproduce the regulation's model form: addressee, a one-line declaration, then order or
    delivery date, goods, price, buyer's name and address, signature (paper only), date.
  - 5/6 fill the seller's details in the addressee block; 1/6 adds the KEP address; 1/6 gives an
    after-sales address that differs from the seller block.
- **Quote:** "Bu formla aşağıdaki malların satışına veya hizmetlerin sunulmasına ilişkin sözleşmeden cayma hakkımı kullandığımı beyan ederim." (s01)
- **Commonly omitted:** where to send the form beyond the addressee block.

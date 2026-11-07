---
doc_id: tr-kvkk-notice
title: KVKK Aydınlatma Metni (privacy notice under KVKK Art. 10)
kind: document
family: privacy-notices
region: tr
part: whole
sample_languages: [tr]
sample_count: 20
saturated: true
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** The notice a controller gives customers and users in Turkey when it collects their
  personal data (KVKK Art. 10 and the Aydınlatma Yükümlülüğü Tebliğ): who the controller is, what
  data it processes, how and why, on which legal condition, who receives it at home and abroad,
  and how people use their Art. 11 rights.
- **Shape:**
  - 18/20 a web page (footer label "Aydınlatma Metni", "KVKK" or "Kişisel Verilerin Korunması";
    2 inside a help centre); 1/20 a PDF, 1/20 a Word file saved as HTML. 1/20 is one tab of a page
    holding several group companies' notices; 1/20 is followed on the same page by a group
    company's notice. Median about 2,050 words (range 1,440–6,080); small companies write the
    longest texts.
  - 15/20 number their sections (1 letters them A–E); 7/20 use question headings; 2/20 add a
    table of contents.
  - The core is a purposes block: 11/20 a table (purpose, data, legal basis), 7/20 a list, 2/20
    prose. 5/20 are built around processing activities (sales, membership, call centre, CCTV),
    each block repeating data, purpose and basis.
  - 2/20 are layered: signs or a short signup-screen notice as the first layer, the full text as
    the second.
- **Register:** formal legal Turkish in 15/20: "biz/siz" ("Şirketimiz", "kişisel verileriniz"),
  long nominal sentences, statutory wording copied for the legal bases and the rights; 4/20 plainer
  and product-specific; 1/20 informal "sen". Defined short names in quotes ("Kanun", "Şirket",
  "Platform") in nearly all; they are drafting, not content.
- **Recurring elements:**
  - The audience in the title ("Müşteri", "Kullanıcı", "Yatırımcı Adayı" … Aydınlatma Metni):
    12/20.
  - A date in the text: 9/20 (a version label 4/20); 1/20 only the help centre's page date.
  - Pointers: to the application form 12/20, to the company's KVKK or retention policy 4/20; to a
    separate cookie notice and to separate consent texts in several.
  - KVKK articles cited inline (5/2-c, 9, 11) in most; the VERBİS purpose and category names in
    many.
  - Published placeholders or leftovers from another text: 4/20 ("[ADRES]", "[●]", another
    company's name). Recorded as observed.
- **Commonly omitted:** a controller block beyond the name (7/20 name the controller only in the
  intro); retention (7/20); security (12/20); the countries data goes to (15/18 that cover
  transfers abroad); the complaint to the Board (16/20); a date or version (11/20).

Counts come from the 20 samples in `research/regions/tr/tr-kvkk-notice/`. Every sample counts for
prevalence; shared wording (a law-firm block in two samples, a stock frame in three) counts once in
patterns (`merge.md`, *Copies*). Patterns record what companies write, including where it restates
the law; they are not legal advice. Every Art. 10(1) item (controller, purposes, recipients and
transfer purpose, collection method and legal basis, rights) is written in every notice: those
sections apply always, whatever their tier. A notice informs only: the writer never asks the
reader to accept it and never puts a consent text inside it (Tebliğ Art. 5(1)(f); consent texts are
`tr-explicit-consent`).

## Sections

### intro: Opening and scope

- **Covers:** the law the notice is given under (KVKK Art. 10, the Tebliğ), the controller named
  in passing, whom it addresses (customers, users, visitors; groups excluded), which apps, sites
  and channels it covers, and what it explains.
- **Prevalence:** 19/20 (95%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.product.services_in_scope`, `facts.data.subject_categories`, `facts.tr.collection_channels`
- **Patterns:**
  - 3/19 one stock sentence: "Kanun uyarınca, kişisel verileriniz; veri sorumlusu olarak …
    tarafından aşağıda açıklanan kapsamda işlenebilecektir"; the rest one or two own paragraphs.
  - 8/19 cite Art. 10 or the Tebliğ by name; 6/19 list the data-subject groups covered or
    excluded (1 sends its mobile apps to their own notices); 4/19 open with a care statement
    ("kişisel verilerinizin güvenliği önceliğimizdir"); 4/19 restate the Art. 4 principles.
  - Folded here (`merge.md`): 5/20 add KVKK definitions (a glossary, or "what is personal
    data?"); write at most one sentence, only when a term is used that a reader would not know.
    3/20 say the notice is information only, needs no acceptance and is not a consent text, with
    consent texts presented separately; write this sentence whenever `facts.tr.legal_bases` has a
    `5/1` or `6/3-a` row.
- **Quote:** "Bu aydınlatma metni (“Aydınlatma Metni”), Getir mobil uygulaması (“Uygulama”) aracılığıyla, kişisel verilerinizi veri sorumlusu sıfatıyla nasıl işlediğimize dair sizleri bilgilendirmek amacıyla hazırlanmıştır." (s19)
- **Commonly omitted:** the channels covered beyond "the website and app"; groups excluded.

### controller: Controller identity and contact

- **Covers:** the controller identified as such ("Veri Sorumlusu"), with its trade name, address,
  registry numbers, KEP, e-mail and phone, VERBİS status, and its representative in Turkey if it
  is established abroad.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.company.phone`, `facts.tr.seller_registry`, `facts.registrations.privacy_regulator`, `facts.tr.representative`
- **Patterns:**
  - 6/13 a full label/value block with registry identifiers (MERSİS, trade registry, tax office);
    the rest a labelled line or short section with name and address, some with e-mail.
  - 10/13 put it first; 2/13 last, as a contact block; 1 repeats it in a footer.
  - 7/20 have no such block: the controller is named only in the intro, and address and KEP
    appear only as application channels. Art. 10(1)(a) is met by the name, but write the block.
  - 1/13 states its VERBİS registration; 1/13 states it is Turkey-based and needs no
    representative.
- **Quote:** "Kişisel verileriniz, aşağıda bilgileri yer alan Şirketimiz tarafından veri sorumlusu sıfatıyla işlenmektedir:" (s02)
- **Commonly omitted:** KEP address and VERBİS status; a phone line.

### controller-role: Where the company is not the controller

- **Covers:** processing where the company acts for others or alongside them: processor for
  business customers' own records, another firm the controller for a product the company sells as
  agent, a marketplace or listing platform that is not party to users' dealings.
- **Prevalence:** 5/20 (25%), rare
- **Applies when:** `facts.company.acts_as_processor == true` or `facts.company.joint_controllers != []` or `facts.tr.sales_model == marketplace`
- **Facts:** `facts.company.acts_as_processor`, `facts.company.processor_customers`, `facts.company.joint_controllers`, `facts.tr.sales_model`
- **Patterns:**
  - 2/5 limit the notice to controller-role processing and send readers to the business
    customer's or health provider's own notice for the rest; 1/5 adds that a separate processor
    agreement governs it.
  - 1/5 names the insurers as controllers for underwriting and points to their notices.
  - 1/5 (a listing platform) says it is not party to the sale and users answer for the data they
    exchange; 1/5 says a content provider has no access to users' data.
- **Quote:** "İşbu Aydınlatma Metni, yalnızca Şirketimizin veri sorumlusu hukuki statüsü ile gerçekleştirdiği kişisel veri işleme faaliyetleri ile sınırlı şekilde hazırlanmıştır." (s08)
- **Commonly omitted:** how a reader tells which role applies to their data.

### data-categories: Personal data processed

- **Covers:** the personal data processed, by category, with example fields; limits on what is
  collected or stored.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.collected`
- **Patterns:**
  - 13/20 a separate inventory (7 a table, 5 a list, 1 inside a combined table); 7/20 name
    categories only inside activity blocks or purpose rows. Write the inventory.
  - Most use the VERBİS category names (Kimlik, İletişim, Müşteri İşlem, İşlem Güvenliği,
    Pazarlama, Görsel ve İşitsel Kayıtlar, Lokasyon) with "örn." examples.
  - 5/20 say what is not collected or not stored (card numbers kept by the payment provider, no
    ID number or contacts).
  - 2/20 note that the set varies by product or service used.
- **Quote:** "Her müşterimizin tüm veri kategorileri işlenmemekte; yalnızca gerçekleştirilen işlemin gerektirdiği veriler, amaçla sınırlı ve ölçülü olarak işlenmektedir." (s02)
- **Commonly omitted:** whether each item is required or optional (few mark it).

### collection-method: How data is collected

- **Covers:** the channels and sources data comes from (the person, third parties, public
  sources) and whether collection is fully or partly automated or non-automated (Art. 10(1)(d)).
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.data.third_party_sources`, `facts.product.services_in_scope`, `facts.tr.collection_channels`
- **Patterns:**
  - 14/20 a section of its own; 6/20 per activity or as a source column in the data table.
  - Most use the statutory formula ("tamamen veya kısmen otomatik ya da veri kayıt sisteminin
    parçası olmak kaydıyla otomatik olmayan yollarla"; or "sözlü, yazılı veya elektronik
    ortamda"), then list the channels (app, website, call centre, stores, forms, e-mail, social
    media).
  - 8/20 name third-party sources (carriers, payment institutions, official identity databases,
    social sign-in, colleagues who invite the user).
  - 3/20 put method and legal basis under one heading, as Art. 10(1)(d) words it, and restate the
    Art. 5 list there.
- **Avoid:** 2/20 (s08, s09) end the channel list open-ended ("ileride eklenebilecek sair
  yöntemler"). The Tebliğ (Art. 5(1)(g)) bars general and vague wording in the notice, and
  Art. 5(1)(i) requires the method to be stated clearly. The writer names the channels in use and
  nothing beyond them.
- **Quote:** "Kişisel verileriniz elektronik ortamda, kısmen veya tamamen otomatik yollarla şu kanallardan toplanır:" (s12)
- **Commonly omitted:** which channel collects which data (a channel/data table in 2/20).

### special-categories: Special-category data

- **Covers:** whether special-category (özel nitelikli) data is processed, which, why, and on
  which Art. 6(3) condition.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** `facts.data.sensitive` is not empty
- **Facts:** `facts.data.sensitive`, `facts.tr.legal_bases`
- **Patterns:**
  - 4/8 name the data and its condition: health data for a telehealth service, biometric face
    matching under anti-money-laundering law, disability data for accessibility, criminal
    records for cheque accounts.
  - 3/8 say none is sought and incidental data is deleted or redacted; when
    `facts.data.sensitive` is empty, the writer may add that one sentence to `data-categories`.
  - 1/8 only warns users not to share it (see `user-duties`).
- **Quote:** "Özel nitelikli kişisel veri (sağlık, din, biyometrik veri vb.) işlemeyi amaçlamıyoruz." (s12)
- **Commonly omitted:** the Art. 6(3) letter as amended by Law 7499 (cited by 2/8).

### purposes: Purposes and legal bases

- **Covers:** why each kind of data is processed and the KVKK condition each purpose rests on
  (Art. 5(1) explicit consent, Art. 5(2)(a)–(f), Art. 6(3) for special data), with the statute
  where the condition is a law or legal obligation; activity-specific flows (call recording,
  CCTV, AI features).
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.purposes`, `facts.tr.legal_bases`, `facts.product.features`, `facts.product.ai_features`, `facts.marketing.email`, `facts.marketing.sms`, `facts.marketing.push`
- **Patterns:**
  - Format: 11/20 a table, 7/20 a list, 2/20 prose. Cut: 6/20 one row per purpose, 5/20 by
    activity, 4/20 by legal basis, 3/20 by data category, 2/20 an unmapped list. Write one row per
    purpose with its data and condition.
  - Conditions: 7/20 cite the Art. 5 letter ("md. 5/2-c"); 11/20 the statute's wording or a
    paraphrase; 2/20 name none per purpose. 5/20 use the VERBİS purpose names.
  - 19/20 use explicit consent somewhere, mostly for marketing, profiling and commercial
    e-messages; 8/20 tie commercial e-messages to the separate ETK/İYS permission as well.
  - 2/20 give an activity its own block with notice, condition, retention and access (call
    recording; CCTV with excluded areas); 1/20 gives AI features a block (data sent and withheld,
    provider terms, AI output labelled).
- **Avoid:**
  - 3/20 (s04, s07, s17) rest a purpose on explicit consent next to, or instead of, a condition
    that already covers it (consent stacked with contract and legal obligation for a credit
    limit; consent plus legitimate interest for events; consent listed beside every Art. 5(2)
    basis per category). The Board's guidance on the processing conditions ("Kişisel Verilerin
    İşlenme Şartları") holds that where a condition other than consent applies, consent must not
    also be asked for, and its explicit-consent guidance ("Açık Rıza Alırken Dikkat Edilecek
    Hususlar") requires consent to be specific (PLAN.md decision 47). The writer gives each
    purpose one condition from `facts.tr.legal_bases`; consent only where no other applies.
  - 4/20 (s09, s10, s14, s17) do not say which condition each purpose rests on (no basis, blank
    rows, a list of bases apart from the purposes, or "one or more of" the whole Art. 5 list).
    Tebliğ Art. 5(1)(h) requires the condition relied on to be stated clearly. The writer names a
    condition for every purpose.
- **Quote:** "Meşru menfaat, her türlü veri işlemenin genel gerekçesi olarak kullanılmaz; gereklilik, daha az müdahaleci seçenekler ve ilgili kişinin hakları birlikte değerlendirilir." (s06)
- **Commonly omitted:** what happens if consent is refused (stated by 4/20: the service stays
  available).

### user-duties: What the reader is asked to do

- **Covers:** the reader's own part: informing people whose data they share, not posting
  special-category or others' data, registering only people they represent, keeping data
  accurate.
- **Prevalence:** 5/20 (25%), rare
- **Applies when:** `facts.product.public_content != none` or `facts.product.business_use != none` or `facts.product.account_roles != []`
- **Facts:** `facts.product.public_content`, `facts.product.business_use`, `facts.product.account_roles`
- **Patterns:**
  - 3/5 ask users not to post or type special-category, ID, card or third-party data into
    messages, listings or forms.
  - 1/5 lets a guardian register only the minors or wards they represent; 1/5 puts the duty to
    inform third parties on the user who shares their data, and asks users to keep their data
    accurate.
- **Quote:** "Kullanıcıların, zorunlu olmadıkça özel nitelikli kişisel verilerini ve üçüncü kişilere ait kişisel verileri paylaşmamaları gerekmektedir." (s15)
- **Commonly omitted:** what the company does with data posted against the request.

### integrations: Connected services

- **Covers:** third-party services the user connects, the data that moves each way, and
  platform statements (Google API Limited Use; Apple Health / Health Connect).
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.product.integrations != []`
- **Facts:** `facts.product.integrations`, `facts.product.platform_disclosures`
- **Patterns:**
  - 1/2 per connection: scope of data read, no ad use or sale of Google API data, and that
    revoking access stops future access but keeps existing records.
  - 1/2 a write-only health integration: what is written, nothing read, data stays on the device.
- **Quote:** "Google API verileri, Kullanıcı'nın gördüğü ve talep ettiği ilgili işlevleri sunmak için kullanılır; reklam hedefleme için kullanılmaz ve satılmaz." (s06)
- **Commonly omitted:** the legal condition for each connection (given by neither).

### children: Children's data

- **Covers:** minors' data: the age limit, when it is processed, guardian consent or
  guardian-registered accounts, limits on its use.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.product.min_age < 18` or `facts.product.child_directed == true`
- **Facts:** `facts.product.min_age`, `facts.product.child_directed`, `facts.product.account_roles`
- **Patterns:**
  - 1/4 sets 18 as the membership age and deletes data received from minors; 1/4 processes it
    only when the child holds a product, with guardian consent where law requires.
  - 1/4 gives minors registered by guardians their own purposes table; 1/4 limits children's
    size data to the service, with no marketing or profiling.
- **Quote:** "Şirketimiz, on sekiz yaşından küçük kişilerden bilinçli olarak kişisel veri toplamamaktadır." (s02)
- **Commonly omitted:** how a guardian exercises the child's rights.

### recipients: Who receives the data

- **Covers:** recipient groups in Turkey and in general (Art. 8, 10(1)(c)): who they are, the
  purpose and condition of each transfer, the data shared, what other users or the public see,
  and that data is not sold.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.processors.list`, `facts.data.other_recipients`, `facts.company.group_companies`, `facts.data.sells`, `facts.product.public_content`
- **Patterns:**
  - 7/20 a table of groups, 7/20 a list, 6/20 prose. Groups by type (suppliers, business
    partners, group companies, authorities and courts, lawyers and auditors), as the Tebliğ's
    "alıcı grubu" asks; 6/20 also name vendors.
  - 8/20 give the condition per group; 7/20 the purpose only; 3/20 one sentence of groups with
    neither. Write group, purpose and condition.
  - 4/20 add that data is not sold; 4/20 treat other users or the public as recipients (public
    listings, posted reviews, event photos); 2/20 cover an acquirer in a merger or share sale.
  - 1/20 justifies naming groups only, calling recipients' identities a trade secret.
- **Quote:** "Kişisel verileriniz, yukarıda sayılan amaçlar dışında üçüncü kişilere satılmaz, kiralanmaz veya pazarlama amacıyla devredilmez." (s02)
- **Commonly omitted:** the data each group receives (given by 7/20).

### cookies-tracking: Cookies, SDKs and ad measurement

- **Covers:** cookies, SDKs and ad measurement as the notice describes them: their use, condition
  and consent route, or a pointer to the separate cookie notice.
- **Prevalence:** 10/20 (50%), common
- **Applies when:** `facts.data.tracking != []`
- **Facts:** `facts.data.tracking`, `facts.data.cookie_controls`, `facts.company.published_policies`
- **Patterns:**
  - 4/10 a pointer to the cookie notice only; 4/10 describe cookie consent (essential cookies on
    contract or legitimate interest, others on unticked per-category consent, how to change);
    2/10 cover app ad measurement and its consent route (cookie settings, the OS tracking prompt).
  - 1/10 says that visiting, scrolling or an OS permission prompt is not consent; 1/10 that no
    optional service loads before consent.
- **Quote:** "Zorunlu olmayan çerezler yalnızca açık rızanız bulunması hâlinde çalıştırılır; çerez tercihlerinizi internet sitemizdeki çerez yönetim panelinden veya tarayıcı ayarlarınızdan dilediğiniz zaman değiştirebilirsiniz." (s02)
- **Commonly omitted:** which trackers send data abroad (2/10 say).

### transfer-abroad: Transfers abroad

- **Covers:** whether data goes abroad, to which recipients and countries, why, and under which
  Art. 9 tool (adequacy decision, standard contract notified to the Authority, binding corporate
  rules, undertaking, occasional transfer), or that none is made.
- **Prevalence:** 18/20 (90%), core
- **Applies when:** always
- **Facts:** `facts.tr.transfer_tools`, `facts.data.storage_locations`, `facts.processors.list`, `facts.company.group_companies`
- **Patterns:**
  - The 2/20 without it are the two undated samples kept because they have no transfer section
    (`merge.md`, decision 46). When `facts.tr.transfer_tools` is none, write one sentence that no
    data is transferred abroad (as 1/18 does "as a rule").
  - 8/18 a section of its own; 10/18 fold it into recipient rows, activity blocks or one
    sentence. Write a section.
  - Tool: 12/18 the standard contract (4 add the five-business-day notification to the
    Authority); 4/18 restate the Art. 9 ladder without saying which tool applies; 2/18 keep
    occasional transfer with consent as a fallback only. Write the tool per transfer.
  - 3/18 name countries; 5/18 name the foreign recipients (cloud and CRM hosts, an ad SDK's
    operator, a parent company). 2/18 say remote access from abroad is a transfer, and that
    consent or accepting terms does not replace an Art. 9 tool.
- **Avoid:**
  - 1/20 (s15) rests a regular transfer (an ad SDK sending identifiers to its foreign operator) on
    explicit consent. KVKK Art. 9(6)(a), as amended by Law 7499, allows consent only for
    occasional, non-repeating transfers. The writer uses an Art. 9(1)–(4) tool from
    `facts.tr.transfer_tools` for every regular transfer.
  - 1/20 (s04) lists foreign recipients on Art. 5 or sector-law bases alone, with no Art. 9 tool.
    KVKK Art. 9 requires an adequacy decision, an appropriate safeguard or an occasional-transfer
    case for any transfer abroad. The writer never leaves a foreign recipient without its tool.
- **Quote:** "Ana sunucunun Türkiye'de olması, yabancı bir sağlayıcıya erişim verilmesi nedeniyle doğan aktarımı ortadan kaldırmaz." (s06)
- **Commonly omitted:** the countries (15/18); the Authority notification of the standard
  contract (14/18).

### consent-withdrawal: Withdrawing consent and message permissions

- **Covers:** how to withdraw explicit consent and opt out of commercial messages, and the effect
  (future only; the service is not blocked).
- **Prevalence:** 6/20 (30%), rare
- **Applies when:** `facts.tr.legal_bases` has a `5/1` or `6/3-a` row, or `facts.marketing.email == true` or `facts.marketing.sms != none` or `facts.marketing.push != none`
- **Facts:** `facts.tr.legal_bases`, `facts.data.cookie_controls`, `facts.users.rights_channels`, `facts.marketing.email`, `facts.marketing.sms`, `facts.marketing.push`
- **Patterns:**
  - 3/6 give in-product paths (settings, cookie icon, device tracking setting); 1/6 a channel
    table for message opt-out (İYS, the link in each message, a direct request) with the
    three-business-day deadline.
  - 3/6 say withdrawal works only for the future and refusing does not block the service; 1/6
    adds that withdrawal does not move marketing to legitimate interest.
- **Quote:** "Ret talepleriniz, ilgili mevzuatta öngörülen süre içinde (talebin ulaşmasını takip eden üç iş günü içinde) yerine getirilir ve bu tarihten sonra tarafınıza ticari elektronik ileti gönderilmez." (s02)
- **Commonly omitted:** that each consent is withdrawn separately.

### automated-decisions: Automated decisions and profiling

- **Covers:** automated decisions and profiling the company runs, their effect, and how to object
  (Art. 11(1)(g)).
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.data.automated_decisions == true`
- **Facts:** `facts.data.automated_decisions`, `facts.data.purposes`, `facts.users.rights_channels`
- **Patterns:**
  - 2/4 list the automated decisions (credit and risk checks, fraud and sanctions screening,
    listing moderation); 1/4 says results are only suggestions the user can override; 1/4 says no
    solely automated adverse decision is made and profiling runs on consent.
  - 2/4 say how to object, 1 with review by a person.
- **Quote:** "Bu kararlara itiraz etmek için destek@ortakmarket.com adresine yazabilirsiniz; talebiniz bir görevli tarafından incelenir (KVKK md. 11/1-g)." (s12)
- **Commonly omitted:** the logic or criteria used.

### security: Security measures

- **Covers:** technical and administrative measures, staff confidentiality, breach notification.
- **Prevalence:** 8/20 (40%), common
- **Applies when:** always
- **Facts:** `facts.data.security_measures`
- **Patterns:**
  - 5/8 one general paragraph (technical and administrative measures, policies, access control);
    3/8 concrete measures (encryption, signed links, EXIF stripping, role-based access, a table of
    administrative and technical measures).
  - 2/8 cover breach notification to the Board and to the people affected; 1/8 staff
    confidentiality.
- **Quote:** "Bu kapsamda Kişisel Verileri yetkisiz erişim, zarar, kayıp veya ifşaya karşı korumak için gerekli teknik ve idari güvenlik önlemleri alınır." (s01)
- **Commonly omitted:** the 72-hour breach notice period (given by 1/8).

### retention: Retention and destruction

- **Covers:** how long data is kept (periods or a rule), the retention and destruction policy,
  periodic destruction, and how data is deleted, destroyed or anonymised.
- **Prevalence:** 13/20 (65%), common
- **Applies when:** always
- **Facts:** `facts.data.retention`, `facts.data.kept_after_deletion`, `facts.tr.destruction_policy`
- **Patterns:**
  - 4/13 a table of periods per data set with its statute (VUK, TTK, TBK, e-commerce rules);
    5/13 a rule with at most one example; 4/13 one period or one data type. Write the table.
  - 3/13 name the retention and destruction policy; 3/13 the periodic destruction cycle (six
    months); 2/13 the longest-period rule where laws overlap.
- **Quote:** "Birden fazla mevzuatın öngördüğü sürelerin çakışması hâlinde, süreler bakımından en uzun olanı esas alınır." (s02)
- **Commonly omitted:** backups (covered by 3/13).

### rights: Data-subject rights

- **Covers:** the rights of KVKK Art. 11.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** none (statutory)
- **Patterns:**
  - 17/20 list the rights, mostly in the statute's order and wording in the second person (19 a
    list, 1 a table with the article letter); 3/20 only refer to Art. 11. Write the list.
  - 1/20 omits the first right (to learn whether data is processed); write all of them.
- **Quote:** "KVKK'nın 11. maddesi uyarınca aşağıdaki haklara sahipsiniz:" (s19)
- **Commonly omitted:** a plain explanation of each right (few give one).

### application: How to apply

- **Covers:** how to exercise the rights: channels (written application to the address, notary,
  KEP, e-mail from a registered address or with e-signature, the application form), required
  contents, identity checks and proxies, the 30-day reply and fee, reasoned refusal, the
  complaint to the Board, and in-app self-service.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.contact_email`, `facts.company.address`, `facts.tr.seller_registry`, `facts.company.published_policies`
- **Patterns:**
  - Channels per the Başvuru Tebliği: written application to the address, KEP, and e-mail from
    an address on file or signed electronically, in most; 12/20 link an application form (2 as the
    only route). 1/20 says the form and a notary are not required.
  - Most state the 30-day free reply with the Board's fee tariff when costly; 3/20 give no fee
    rule, 1/20 no deadline.
  - At least 6/20 add the required request contents under the Başvuru Tebliğ, some with proxy
    rules; 4/20 the complaint to the Board (with its 30/60-day windows in 2); 4/20 in-app
    self-service for correction and deletion.
- **Quote:** "Başvuru formu kullanmanız yardımcı olabilir, fakat form kullanmak veya noter aracılığıyla başvurmak zorunlu tutulmaz." (s06)
- **Commonly omitted:** the complaint to the Board (16/20).

### changes: Changes to the notice

- **Covers:** how the notice is updated, how readers are told, when a change takes effect.
- **Prevalence:** 7/20 (35%), rare
- **Applies when:** `facts.company.change_notice` has an entry for `documents`
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - 3/7 announce updates (in the app, to customers); 3/7 publish the new version with its date,
    effective on publication; 1/7 keeps a version history table.
  - 2/7 say new consent-based processing gets its own notice and choice, and continued use is not
    consent.
- **Quote:** "Siteyi kullanmaya devam etmeniz kendiliğinden yeni bir açık rıza oluşturmaz." (s18)
- **Commonly omitted:** advance notice of material changes (1/7).

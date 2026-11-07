---
doc_id: tr-explicit-consent
title: KVKK Açık Rıza Metni (explicit consent text under KVKK Art. 5(1), 6(3)(a), 9(6)(a))
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

- **Purpose:** The text by which a customer or user in Turkey gives explicit consent (açık rıza)
  to processing that no other KVKK condition covers: marketing, profiling, ad tracking,
  special-category data without another Art. 6(3) condition, or an occasional transfer abroad. It
  says to whom consent is given, for which data, purposes and recipients, and how it is given and
  withdrawn.
- **Shape:**
  - 16/20 a web page (footer label "Açık Rıza Metni"), 3/20 a PDF, 1/20 a paper form published as a
    page. 2/20 share their page with another text (a notice, a business-user tab). Median about
    280 words (range 100–1,260); small companies write the longest texts, banks the shortest.
  - 12/20 one to three unheaded paragraphs, usually one long first-person sentence ending in the
    consent verb; 5/20 numbered items or bullets, one per consent; 2/20 paragraphs with a bulleted
    data list; 1/20 headed sections.
  - 4/20 give one choice per consent; 16/20 one acceptance for everything.
- **Register:** formal legal Turkish; 19/20 in the data subject's first person ("açık rıza
  veriyorum", "onay veriyorum"), often after a company-voice opening. 2/20 plain, short sentences.
  Defined short names ("Şirket", "Kanun") and strings of processing verbs are drafting, not
  content.
- **Recurring elements:**
  - A title "Açık Rıza Metni / Beyanı / Onay Formu" 20/20; the subject in the title 8/20 (marketing,
    health data, a transfer abroad), the audience 4/20.
  - An acknowledgment of the separate Aydınlatma Metni 14/20.
  - A free-will formula ("özgür irademle", "hiçbir baskı altında kalmadan") 10/20.
  - Address, e-mail or phone 9/20; a date or version 5/20; a signature or name-and-date block
    3/20.
  - Leftovers or broken clauses 5/20 (an editor's comment mark, contact details "stated below"
    that are absent). Recorded as observed.
- **Commonly omitted:** withdrawal (11/20); what refusing costs (15/20); the possible risks of a
  transfer abroad (15/15 that cover one); the countries data goes to (13/15); how consent is
  logged (18/20); a date or version (15/20).

Counts come from the 20 samples in `research/regions/tr/tr-explicit-consent/`. Every sample counts
for prevalence; shared wording (one marketing-purposes string in s13 and s17) counts once in
patterns (`merge.md`, *Copies*). Patterns record what companies write; they are not legal advice.
Three rules hold for every text, whatever the counts. The text covers only purposes that rest on
consent in `facts.tr.legal_bases` (`5/1`, `6/3-a`) and transfers with tool `occasional` in
`facts.tr.transfer_tools`; nothing another condition covers. It is a text of its own, separate from
the KVKK notice (`tr-kvkk-notice`) and from the contract, terms and ETK permission. No service or
feature is made conditional on a consent, except the feature that cannot run without the
processing itself.

## Sections

### controller: Controller and opening

- **Covers:** the controller consent is given to (trade name, brand, address, registry numbers,
  e-mail, phone), and any company-voice opening: the law consent is asked under, why consent is
  the condition, and the request itself.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.company.legal_name`, `facts.product.name`, `facts.company.address`, `facts.company.contact_email`, `facts.company.phone`, `facts.tr.seller_registry`, `facts.product.services_in_scope`, `facts.data.subject_categories`
- **Patterns:**
  - 15/20 name the controller only in passing (title, opening or acknowledgment sentence); 5/20
    give an address or a block (1 a letterhead footer with registry, MERSİS, KEP and phone; 1 a
    chamber registry number). 4/20 give an e-mail only as the withdrawal or complaint channel.
    Write the name and address, and the e-mail.
  - 1/20 names only the brand, never the legal person; 1/20 groups five brands as one controller.
  - Folded here (`merge.md`, `intro`): 5/20 open in the company's voice before the first-person
    declaration, with the law and the request ("açık rızanızı talep ediyoruz"); 2/20 say why consent
    is asked (servers or a vendor abroad, no adequacy decision). Write one opening sentence naming
    the controller and what the text asks for.
- **Quote:** "…kişisel verilerinizin işlenmesi kapsamında aşağıdaki hususlara ilişkin açık rızanızı talep ediyoruz;" (s01)
- **Commonly omitted:** registry numbers and KEP; a phone line.

### notice-link: Link to the KVKK notice

- **Covers:** the separate Aydınlatma Metni: an acknowledgment that it was given and read (named,
  linked or summarised), or a statement that this text is separate from it.
- **Prevalence:** 17/20 (85%), core
- **Applies when:** always
- **Facts:** `facts.tr.kvkk_notice_url`, `facts.company.published_policies`
- **Patterns:**
  - 14/20 a first-person acknowledgment of the notice, named by title ("… Aydınlatma Metni'ni
    okudum"); 2/20 take the data scope from it by reference. 1/20 in the company's voice ("the
    notice we gave you before"). 2/20 say this text is separate from the notice. Write the notice's
    title and link, and that it was given before this text.
  - 3/20 restate the Art. 10 topics as received; 1/20 says its notice explained the risks of
    occasional transfers abroad.
  - 1/20 only implies a notice; 1/20 has none.
- **Avoid:** 1/20 (s19) is one text titled "Aydınlatma ve Rıza Metni", with controller,
  purposes, recipients and opt-out folded into the consent sentence and no separate notice. The
  Aydınlatma Yükümlülüğü Tebliğ (Art. 5(1)(f)) requires informing and taking consent to be done
  separately where processing rests on explicit consent. The writer points to the notice and never
  makes this text the notice.
- **Quote:** "Şirket tarafından KVKK ve ilgili mevzuatlar uyarınca “Kızılkaya Business Otel Aydınlatma Metni” ile bilgilendirildim." (s12)
- **Commonly omitted:** a link (most name the notice without one).

### purposes: Purposes consented to

- **Covers:** the purposes the consent covers, listed or by reference to the notice.
- **Prevalence:** 19/20 (95%), core
- **Applies when:** always
- **Facts:** `facts.tr.legal_bases`, `facts.data.purposes`, `facts.product.features`, `facts.product.ai_features`, `facts.tr.consent_capture`
- **Patterns:**
  - Format: 10/20 inline in one sentence, 6/20 a list, 3/20 one purpose per consent item; 2/20 only
    by reference to the notice. Write each purpose named, one per consent item.
  - Scope: 7/20 mix service and marketing purposes, 6/20 marketing only (offers, campaigns,
    segmentation, profiling, ads on third-party media), 4/20 health or special-category data, 2/20
    a single transfer.
  - 1/20 gives no purpose at all (see *Avoid*).
- **Avoid:**
  - 6/20 (s01, s02, s06, s07, s12, s19) ask consent for processing another condition covers
    (account, invoicing and delivery; identity checks and contract performance; diagnosis,
    treatment and insurer billing of health data; bank risk reporting; reservations; information
    on purchases and legal matters). The Board's decision "Hizmetin Açık Rıza Şartına Bağlanması"
    holds that asking consent where another condition exists misleads the person and abuses the
    right (KVKK Art. 4); Tebliğ Art. 5(1)(j) bars misleading information. The writer lists only
    purposes with a `5/1` or `6/3-a` row in `facts.tr.legal_bases`.
  - 4/20 (s01, s04, s06, s18) give blanket consent: data and purposes "not limited to" those
    listed, all processing "within the notice", an advance permission to every processing, or no
    purpose at all. The Board's guide "Açık Rıza Alırken Dikkat Edilecek Hususlar" calls consent
    not tied to a specific subject a blanket consent ("battaniye rıza") and invalid. The writer
    names every purpose and never adds open-ended wording.
- **Quote:** "Sağlık verilerimin yukarıda açıklanan amaç ve sınırlarla işlenmesine açıkça rıza gösteriyorum." (s03)
- **Commonly omitted:** which purpose belongs to which consent item, where items are bundled.

### data-categories: Data covered

- **Covers:** the personal data the consent covers, by category or field, and whether
  special-category data is covered.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.data.collected`, `facts.data.sensitive`, `facts.tr.legal_bases`
- **Patterns:**
  - 13/20 name categories or fields (VERBİS names such as Kimlik, İletişim, Lokasyon, with
    examples); 2/20 name data only inside purposes; 5/20 only generically or by reference to the
    notice ("kişisel verilerim", "current or future data"). Write the categories per consent item.
  - 6/20 cover special-category data (health 5, biometric 1); each names it separately.
- **Quote:** "Lokasyon Verisi: Konum Bilgisi" (s18)
- **Commonly omitted:** which data goes with which purpose.

### scope-limits: What the consent does not cover

- **Covers:** what the consent does not cover: data processed on other conditions, purposes that
  need their own consent, permissions taken elsewhere (ETK approval, cookie banner), data held as
  processor.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.data.tracking != []` or `facts.company.acts_as_processor == true` or `facts.marketing.email == true` or `facts.marketing.sms == service-and-marketing` or `facts.marketing.push == service-and-marketing`
- **Facts:** `facts.data.tracking`, `facts.data.cookie_controls`, `facts.company.acts_as_processor`, `facts.marketing.email`, `facts.marketing.sms`, `facts.marketing.push`, `facts.company.published_policies`
- **Patterns:**
  - 2/4 say the ETK message approval or the cookie consent is taken separately and this consent
    does not replace it.
  - 1/4 says other data is processed on Art. 5 and 6 conditions without consent, and consent is
    asked only for the rest; 1/4 says separable purposes (sharing with a dietitian, model
    improvement) need their own consent.
- **Quote:** "Bu rıza, ticari elektronik ileti gönderilmesine ilişkin ayrıca alınacak kanal bazlı onayın yerine geçmez;" (s15)
- **Commonly omitted:** data held as processor for business customers.

### consent-records: How consent is recorded

- **Covers:** how a given or refused consent is logged and proved (date, text version, source),
  and the copy the person can read before consenting.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.tr.consent_capture` has a row with `logged == true`
- **Facts:** `facts.tr.consent_capture`
- **Patterns:**
  - 1/2 logs every consent and refusal with date, text version and source; 1/2 keeps a
    server-side record and shows the text before the unticked box.
- **Quote:** "…verdiğiniz veya reddettiğiniz her onay tarih, metin sürümü ve kaynağıyla birlikte kayıt altına alınır." (s09)
- **Commonly omitted:** how long the record is kept.

### voluntariness: Refusing a consent

- **Covers:** whether each consent is optional, and what refusing costs: nothing, an alternative
  channel, or only the feature that needs the processing.
- **Prevalence:** 5/20 (25%), rare
- **Applies when:** `facts.tr.consent_capture` has a row whose `refusal_effect` or `alternative` is not none
- **Facts:** `facts.tr.consent_capture`
- **Patterns:**
  - 4/5 say refusing costs nothing or only the feature, and the legal relationship does not depend
    on consent; 1/5 offers the call centre instead and an e-mail to report pressure.
  - 1/5 labels each item optional or required.
  - When no refusal turns anything off, the writer adds one sentence to `consent-statement` that
    refusing or withdrawing does not affect the service (as 4/20 do).
- **Avoid:** 1/20 (s09) makes two consents a condition of the account ("uygulama için
  gereklidir"), and withdrawing one closes it. The Board's decision "Hizmetin Açık Rıza Şartına
  Bağlanması" holds that consent made a condition of a service is not freely given, and its guide
  requires consent "özgür iradeyle açıklanan". The writer names only the feature the processing
  itself serves as what refusing turns off.
- **Quote:** "Bu rızanın isteğe bağlı olduğunu, rıza vermememin veya rızamı geri almamın Cari Plus hizmetinden yararlanmamı engellemeyeceğini biliyorum." (s15)
- **Commonly omitted:** the alternative for a refused feature.

### retention: How long consented data is kept

- **Covers:** how long data under the consent is kept, where it is stored, and when it is deleted.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.data.retention` has an entry for a category processed only on a `5/1` or `6/3-a` row of `facts.tr.legal_bases`
- **Facts:** `facts.data.retention`, `facts.tr.legal_bases`
- **Patterns:**
  - 1/2 says feature inputs are discarded after use and consent records kept on the server; 1/2 a
    period "within the legal maximum".
  - Write the period, and that the data is deleted when consent is withdrawn unless another
    condition then applies.
- **Commonly omitted:** a period in days or months.

### recipients: Recipients in Turkey

- **Covers:** recipients inside Turkey that consented data goes to, by name or category, and
  their purpose; transfers the person is told of that do not rest on the consent.
- **Prevalence:** 14/20 (70%), common
- **Applies when:** `facts.processors.list`, `facts.data.other_recipients` or `facts.company.group_companies` has a recipient in Turkey for data under a `5/1` or `6/3-a` row of `facts.tr.legal_bases`
- **Facts:** `facts.processors.list`, `facts.data.other_recipients`, `facts.company.group_companies`, `facts.tr.legal_bases`
- **Patterns:**
  - 12/14 by category (suppliers, business partners, shareholders, group companies, call-centre and
    e-mail vendors); 2/14 name one (an AI provider; a dietitian the user picks). Write the
    category with its purpose, and name a recipient the person chooses.
  - 1/14 adds a separate consent for named family members, with blank fields for each; 1/14
    states legally required transfers as "I know", not as consent.
  - 1/14 names group companies and partners with no word on whether they are in Turkey.
- **Quote:** "…aydınlatma metninde belirtilen barındırma, müşteri ilişkileri yönetimi ve ileti gönderimi hizmeti sağlayıcılarıyla paylaşılmasına özgür irademle açık rıza veriyorum." (s15)
- **Commonly omitted:** the data each recipient gets.

### transfer-abroad: Occasional transfer abroad

- **Covers:** an occasional transfer abroad on consent (KVKK Art. 9(6)(a)): the foreign recipient,
  the country, why data goes abroad, the data sent, the one case it is for, and the possible
  risks.
- **Prevalence:** 15/20 (75%), common
- **Applies when:** `facts.tr.transfer_tools` has a row with tool `occasional`
- **Facts:** `facts.tr.transfer_tools`, `facts.data.storage_locations`, `facts.tr.consent_capture`
- **Patterns:**
  - Default (s06 items 3 and 7, the only occasional transfers in the samples): one approve /
    do-not-approve item per case, naming the purpose ("limited to the consultation, test or
    analysis"), the recipients abroad and the data. Write one item per row with tool `occasional`.
  - 11/15 put the transfer in the same consent as processing; 4/15 give it a choice or text of
    its own. Give it its own.
  - 4/15 name the foreign recipient, 2/15 the countries, 4/15 cite Art. 9, 3/15 say why data goes
    abroad. 0/15 state the possible risks, which Art. 9(6)(a) requires the person to be told:
    write the risks (no adequacy decision for the country, no Art. 9(4) safeguard in place).
- **Avoid:** 15/20 (s01, s02, s03, s04, s05, s06 item 2, s07, s09, s11, s12, s13, s14, s16, s18,
  s19) rest a regular transfer on consent: group companies, suppliers, hosting and cloud providers,
  a messaging platform, AI and support vendors, ad networks. KVKK Art. 9(6)(a), as amended by Law
  7499 (in force 2024-06-01), allows consent only for occasional transfers, where no adequacy
  decision or Art. 9(4) safeguard can be used, and only after the person is told the risks. The
  writer never puts a regular transfer in this text; those go under their tool in the notice
  (`tr-kvkk-notice`).
- **Quote:** "…yurt dışında yerleşik sağlık kuruluşlarına, doktorlara ve sağlık personellerine ... tıbbi konsültasyonun/tetkikin/testin temini ile sınırlı olarak aktarılmasına onay" (s06)
- **Commonly omitted:** the risks (15/15); the countries (13/15).

### withdrawal: Withdrawing consent

- **Covers:** that consent can be withdrawn at any time, the channel, and the effect (forward
  only; which feature stops); where the other Art. 11 rights are used.
- **Prevalence:** 9/20 (45%), common
- **Applies when:** always
- **Facts:** `facts.tr.consent_capture`, `facts.users.rights_channels`, `facts.data.cookie_controls`, `facts.company.contact_email`
- **Patterns:**
  - 11/20 are silent. Of the 9: 5 name a channel (in-app settings, e-mail, İYS or the link in each
    message, the website), 1 points to the notice's channels, 3 state the right only or a vague channel ("electronic channels"). Write the
    in-product path and the e-mail.
  - 2/9 say withdrawal works only for the future; 1/9 that it does not require deleting the
    account; 1/9 that legally required communications continue.
  - Written always, against the count (11/20 silent). The Board's guide "Açık Rıza Alırken Dikkat
    Edilecek Hususlar" (Icerik/2037) and its "Doğru Bilinen Yanlışlar -II-" (questions 6–7) hold
    that consent can be withdrawn at any time, effective from when the withdrawal reaches the
    controller, and that withdrawing must be as easy as consenting; its guide "Açık Rıza" (p. 11)
    requires the person to know the consequences of consenting, not only its subject. No source
    says in terms that the text must state the right; the rule rests on these two points.
  - Folded here (`merge.md`, `rights`): 4/20 refer to the Art. 11 rights (reserved, explained,
    or where to use them; 1 the right to compensation). Write one sentence pointing to the notice
    for the other rights.
- **Quote:** "Geri alma ileriye etkili olarak rızaya dayalı işlemleri durdurur." (s03)
- **Commonly omitted:** that each consent is withdrawn separately.

### commercial-messages: Commercial electronic messages

- **Covers:** permission to send commercial electronic messages (Law 6563) given inside the text:
  channels, message types, İYS. Processing for sending messages, without permission wording, is
  `purposes`.
- **Prevalence:** 4/20 (20%), rare
- **Applies when:** `facts.marketing.email == true` or `facts.marketing.sms == service-and-marketing` or `facts.marketing.push == service-and-marketing`
- **Facts:** `facts.marketing.email`, `facts.marketing.sms`, `facts.marketing.push`, `facts.tr.consent_capture`
- **Patterns:**
  - 1/4 gives the permission its own box, with İYS and the link in each message as the way out;
    1/4 joins it with appointment reminders in one item; 2/4 put it in the same sentence as the
    marketing consent (1 makes the whole text an ETK permission).
  - Channels named: e-mail, SMS, calls, social media, push. Give it its own choice, apart from the
    KVKK items.
- **Quote:** "Bu onayı İYS (İleti Yönetim Sistemi) üzerinden veya iletideki bağlantıdan dilediğim zaman geri alabilirim." (s09)
- **Commonly omitted:** the message types per channel.

### security: Security undertaking

- **Covers:** the controller's undertaking to keep the consented data secure.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** `facts.data.sensitive` is not empty
- **Facts:** `facts.data.security_measures`, `facts.data.sensitive`
- **Patterns:**
  - 1/1 (a bank) one sentence that the data is protected, beside a reserved right to
    compensation. For special-category data, write one sentence on the measures, since KVKK Art. 6
    requires adequate measures set by the Board.
- **Commonly omitted:** the measures themselves.

### user-duties: What the person warrants

- **Covers:** what the person warrants: that third parties' data they share was shared lawfully,
  with those persons informed.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** `facts.product.public_content != none` or `facts.product.business_use != none` or `facts.product.account_roles != []`
- **Facts:** `facts.product.public_content`, `facts.product.business_use`, `facts.product.account_roles`
- **Patterns:**
  - 1/1 (a clinic form) a warranty that third parties' data given was shared lawfully, they were
    informed and their consent taken where needed.
- **Commonly omitted:** what the company does with data shared against the warranty.

### consent-statement: The declaration

- **Covers:** the affirmative declaration and how it is given: the consent wording the person
  adopts, a checkbox, an approve / do-not-approve choice per item, a signature or name-and-date
  block.
- **Prevalence:** 20/20 (100%), core
- **Applies when:** always
- **Facts:** `facts.tr.consent_capture`
- **Patterns:**
  - 19/20 a first-person declaration ("açık rıza veriyorum", "onay veriyorum", "muvafakat ederim");
    1/20 says what ticking the box means. 10/20 add a free-will formula; 2/20 the triple "kabul,
    beyan ve taahhüt".
  - Mechanism: 4/20 a checkbox (3 unticked, 1 next to the send button), 3/20 a paper approve /
    do-not-approve choice with name, date or signature, 13/20 none on the page.
  - Granularity: 4/20 one choice per item, 16/20 one acceptance for everything. Write one unticked
    choice per consent, matching `facts.tr.consent_capture`. Why, against the count: the Board's
    guide "Açık Rıza" (KVKK Yayınları No: 98, June 2025, p. 10) requires consent per purpose ("her
    amaç için ayrı bir açık rıza alınması gerekir"), and separately for a secondary operation such
    as a transfer abroad; its "Doğru Bilinen Yanlışlar -II-" (No: 66, March 2026, question 8,
    citing Board decision 2020/173) holds that only an opt-in box, not pre-ticked, gives valid
    consent.
  - 4/20 add that refusing or withdrawing does not affect the service (see `voluntariness`).
- **Avoid:** 13/20 (s01, s02, s07, s08, s10, s11, s12, s13, s14, s15, s17, s19, s20) cover more
  than one purpose (or processing plus sharing or transfer abroad) with a single acceptance. The
  Board's guide "Açık Rıza" (KVKK Yayınları No: 98, June 2025, p. 10) requires consent to be given
  for each purpose ("her amaç için ayrı bir açık rıza alınması gerekir"), and separately for a
  secondary operation such as a transfer abroad. The writer gives each consent in
  `facts.tr.consent_capture` its own unticked choice.
- **Quote:** "6698 sayılı KVKK kapsamında, işaretlediğim ölçüde aşağıdaki hususlara özgür irademle açık rıza veriyorum." (s09)
- **Commonly omitted:** where the choice is made (13/20 show no mechanism).

### guardian: Consent for a minor or ward

- **Covers:** consent given by a parent, guardian or legal representative for a minor or a person
  under guardianship.
- **Prevalence:** 2/20 (10%), rare
- **Applies when:** `facts.product.min_age < 18` or `facts.product.child_directed == true`
- **Facts:** `facts.product.min_age`, `facts.product.child_directed`, `facts.product.account_roles`
- **Patterns:**
  - 1/2 a second declaration in the representative's capacity; 1/2 a signature block naming the
    parent of a child patient, a guardian or a legal representative.
- **Quote:** "…veli / vasi / yasal temsilci sıfatıyla açık rıza veriyorum." (s08)
- **Commonly omitted:** how the representative's authority is checked.

### changes: Changes to the text

- **Covers:** how the text is updated and when a change takes effect.
- **Prevalence:** 1/20 (5%), rare
- **Applies when:** `facts.company.change_notice` has an entry for `documents`
- **Facts:** `facts.company.change_notice`
- **Patterns:**
  - 1/1 takes effect when the person approves it and reserves a right to update the text. Write
    that a new purpose, data set or recipient needs a new consent, and continued use is not
    consent.
- **Quote:** "İşbu metin veri konusu kişi onayladığı anda yürürlüğe girer." (s12)
- **Commonly omitted:** how people are told of a new version.

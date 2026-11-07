---
doc_id: data-subject-request
title: Data Subject Request Form, Turkey part (İlgili Kişi Başvuru Formu)
kind: document
family: privacy-notices
region: tr
part: block
sample_languages: [tr]
sample_count: 15
saturated: false                # first batch only: the owner closed the pool before any saturation batch, so the 5-in-a-row stop was never tested
scanned: 2026-10-27
format_version: 2
---

## Document

- **Purpose:** What KVKK Arts. 11, 13 and 14 and the Veri Sorumlusuna Başvuru Usul ve Esasları
  Hakkında Tebliğ ("Başvuru Tebliği") add to the request form for a company whose users include
  people in Turkey: the channels an application may use, what it must contain, the Art. 11
  rights, the 30-day free reply and its fee, the written or electronic answer, the complaint to
  the KVK Board, and the notice for the form's own data.
- **Shape:** Turkish practice is a form the person prints, fills in, signs and sends: 10/15 PDFs,
  4/15 HTML pages to print, 1/15 an online form. Median 547 words (189–1,040). Most open with
  the legal basis and the channels, then lettered or numbered field blocks (identity,
  relationship, request, reply channel), a declaration and a signature block. The root sections
  already cover the relationship field (15/15), identity checks (12/15), the declaration (10/15)
  and representatives (6/15); this block holds the parts Turkish law decides.
- **Register:** formal legal Turkish ("Şirketimiz", "siz") in 13/15; the applicant speaks in the
  first person in options and the declaration ("…öğrenmek istiyorum", "beyan ve taahhüt ederim")
  in 10/15. Law 6698 is cited by article in 13/15, the Başvuru Tebliği by name in 7/15.
- **Recurring elements:** the subject line "Kişisel Verilerin Korunması Kanunu Kapsamında Bilgi
  Talebi" for the envelope or e-mail (7/15); a date or version (6/15); an office-use receipt box
  (2/15).
- **Commonly omitted:** an application tool as a channel (0/15 name one); that applications are
  made in Turkish (Tebliğ Art. 4(2); 0/15); the complaint to the Board (2/15 give it); refusal
  with reasons (2/15).

Counts come from 15 Turkish forms (`research/regions/tr/data-subject-request/`), mapped against the
root ids. No two are copies; shared template wording counts once in *Patterns*. The pool was closed
after the first batch, so the block is `saturated: false`. In the regional part, write this block
in Turkish.

## Sections

### tr-channels: How to send the application

- **Covers:** the channels of Başvuru Tebliği Art. 5(1) the company accepts, each with its
  address: a signed written application (in person, by notary, by post), KEP, e-mail with a
  secure electronic or mobile signature, e-mail from an address the person gave the company
  before, and an application tool (the form itself, when it submits online); how to fill in, sign
  and mark the application.
- **Prevalence:** 14/15 (93%), core
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.company.legal_name`, `facts.company.address`, `facts.company.contact_email`, `facts.tr.seller_registry`
- **Patterns:**
  - In person 13/14, notary 9/14, post 8/14; KEP 9/14; e-mail from the address on file 8/14;
    e-signed or mobile-signed e-mail 7/14; an application tool 0/14. Write every channel the
    company can receive, the online form among them when it has one.
  - 5/14 give a grid of channel, address and the text to write on the envelope or in the subject
    line (two template texts); 7/14 give the subject line "Kişisel Verilerin Korunması Kanunu
    Kapsamında Bilgi Talebi".
  - 4/14 say to fill in and sign (or print) the form first; 5/14 ask for ID when applying in
    person; 2/14 add "other methods the law allows".
  - 1/14 leaves every address blank and never names the company.
- **Avoid:** naming only paper routes (in person, notary, registered post) as the way to apply:
  3/15 (s09, s10, s13; s13 also requires this form). The Board held that telling people they may
  apply only through a notary or by e-signature puts a burden on them that neither KVKK nor the
  Tebliğ provides, against the lawfulness and good-faith rule of Başvuru Tebliği Art. 6(1)
  (decision 2019/296, 1 October 2019); Art. 5(1) lets the person choose among its channels.
- **Quote:** "Bu formu doldurup aşağıdaki yollardan biriyle gönderebilirsiniz (sayfayı tarayıcınızdan yazdırabilirsiniz):" (s15)
- **Commonly omitted:** an online form or app as a channel (0/14); that the application is made
  in Turkish (Tebliğ Art. 4(2); 0/15).

### tr-timeline: Reply time and fees

- **Covers:** the answer as soon as possible and within 30 days of receipt, free of charge; the
  fee when the answer has a cost (Başvuru Tebliği Art. 7: free up to 10 pages, 1 TL per page
  above, the cost of a CD or flash drive); refusal with reasons; the refund when the application
  was caused by the company's error (KVKK Art. 13(2)–(3), Tebliğ Art. 6(5)).
- **Prevalence:** 14/15 (93%), core
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - 13/15 give 30 days; 4/13 add "as soon as possible"; 5/13 count from receipt.
  - 10/15 point to "the Board's tariff" with no amounts; 2/15 give the Tebliğ amounts; 1/15 says
    it will ask before going ahead with extra cost. Write the amounts.
  - 6/15 say the answer is free; 3/15 make the applicant acknowledge a possible fee in the
    declaration (one template text).
  - 2/15 say a refusal comes with reasons; 1/15 gives the refund.
  - No sample asks for a fee up front; every fee line matches Art. 13(2) and Tebliğ Art. 7.
- **Quote:** "Niteliğine göre talebiniz; en kısa sürede ve en geç otuz gün içinde ücretsiz olarak sonuçlandırılacaktır." (s07)
- **Commonly omitted:** the refund (14/15); refusal with reasons (13/15).

### tr-application-content: What the application must contain

- **Covers:** the contents of Başvuru Tebliği Art. 5(2)–(3) as fields: name and surname, and a
  signature if written; T.C. kimlik no., or for foreigners nationality and passport or ID number;
  the address for notices (home or work); e-mail, phone and fax if the person has them; the
  subject of the request in free text; supporting documents.
- **Prevalence:** 15/15 (100%), core
- **Applies when:** always
- **Facts:** `facts.users.request_handling`, `facts.product.has_accounts`
- **Patterns:**
  - T.C. kimlik no. 15/15 (1 only on written applications); the foreigners' alternative 9/15; an
    address 15/15, mostly in the Tebliğ's words "tebligata esas yerleşim yeri veya iş yeri adresi".
  - A signature and date block 14/15, often with a note that e-signature serves for KEP.
  - 3/15 cite the Tebliğ on the fields; 1/15 says the ID number and address are used only to
    answer and verify.
  - The request in free text 15/15; 6/15 ask for supporting documents; 1/15 asks not to send
    originals; 1/15 asks not to include special-category data.
  - 2/15 add an account identifier (username, the account's e-mail or phone).
- **Avoid:** making phone, mobile, fax or e-mail required, or saying the Tebliğ requires them:
  3/15 (s01 asterisks every field, fax included, citing the Tebliğ; s12 and s13 require mobile
  and e-mail). Başvuru Tebliği Art. 5(2)(ç) asks for them only "varsa" (if the person has them),
  and KVKK Art. 4(2)(ç) limits data to what the purpose needs.
- **Quote:** "T.C. kimlik numarası ve adres bilgisi Tebliğ md. 5 gereği istenir ve yalnızca başvurunuzu sonuçlandırmak ve kimliğinizi doğrulamak için kullanılır." (s15)
- **Commonly omitted:** that e-mail, phone and fax are optional (1/15 says so); the foreigners'
  alternative (6/15).

### tr-rights: KVKK Art. 11 rights in the request menu

- **Covers:** the nine rights of KVKK Art. 11(1) as the form's request options: (a) learn whether
  data is processed, (b) ask for information about it, (c) learn the purpose and whether data is
  used for it, (ç) know the recipients in Turkey and abroad, (d) correction, (e) erasure or
  destruction under Art. 7, (f) notice of (d) and (e) to recipients, (g) objection to an adverse
  result of solely automated analysis, (ğ) compensation for unlawful processing; with the Art. 11
  and 13 citation that frames the form.
- **Prevalence:** 10/15 (67%), common
- **Applies when:** always
- **Facts:** `facts.users.rights_channels`, `facts.data.automated_decisions`
- **Patterns:**
  - 7/10 list all nine (2 fold (f) into (d) and (e), 1 splits it in two); 3/10 list four, five or
    seven. Write all nine.
  - 6/10 a tick-list; 3/10 a list above the fields only; 1/10 a fixed petition that asserts every
    listed right at once.
  - 7/10 phrase options in the first person ("Kişisel verilerimin silinmesini istiyorum"); 3/10
    tag each with its article letter; 3/10 ask for details after correction or compensation.
  - 2/10 add consent withdrawal as an option; 1/10 splits (b) into information and an electronic
    copy.
  - 5/15 have only a free-text box and no list.
- **Quote:** "Kişisel verilerimin işlenip işlenmediğini öğrenmek istiyorum." (s14)
- **Commonly omitted:** what each right means for the company's product (2/10 give examples).

### tr-complaint: Complaint to the KVK Board

- **Covers:** that if the request is refused, the answer is inadequate or no answer comes in time,
  the person may complain to the KVK Board within 30 days of learning the answer and in any case
  within 60 days of the application (KVKK Art. 14(1)), after applying to the company first
  (Art. 14(2)).
- **Prevalence:** 2/15 (13%), rare
- **Applies when:** always
- **Facts:** none (statutory)
- **Patterns:**
  - 1/2 one sentence with the three triggers; 1/2 the triggers and the 30/60-day windows. Write
    the windows.
  - Both sit next to the deadline and fee lines.
- **Quote:** "Başvurun reddedilirse, cevabı yetersiz bulursan ya da süresinde cevap verilmezse Kurul'a şikâyette bulunabilirsin." (s06)
- **Commonly omitted:** where to complain (the Board's online complaint form).

### tr-reply: How you want the answer

- **Covers:** the applicant's choice of reply channel, the answer always given in writing or
  electronically (KVKK Art. 13(3), Başvuru Tebliği Art. 6(3)), and how copies of data are
  delivered safely.
- **Prevalence:** 14/15 (93%), core
- **Applies when:** always
- **Facts:** `facts.users.request_handling`
- **Patterns:**
  - Post 12/14, e-mail 13/14, collection in person 4/14 (a proxy only with a notarised power of
    attorney, one template text), fax 2/14, KEP 1/14; 1/14 only "in writing or electronically".
  - 3/14 say e-mail is faster; 1/14 replies by the channel used to apply when none is ticked.
  - 1/14 sends data copies through an expiring link or an encrypted file, the password by another
    channel.
  - 2/15 add an office-use box (reference, receipt date and channel, identity check, reply date,
    outcome with reasons, notice to recipients under Art. 11(1)(f)).
- **Avoid:** offering a phone call as the answer: 2/15 (s09, s10). KVKK Art. 13(3) and Tebliğ
  Art. 6(3) require the answer in writing or electronically, and the Board's announcement of
  1 October 2026 says phone, face-to-face or other oral replies are not that answer. A call may
  still be used to ask for more information.
- **Quote:** "(Herhangi bir cevap yöntemi tercih edilmemesi halinde başvuru iletildiği usul ile cevaplandırılacaktır.)" (s07)
- **Commonly omitted:** a default channel when none is ticked (13/14).

### tr-request-notice: Notice for the data in this form

- **Covers:** the KVKK Art. 10 notice for the data the form collects: the controller, the
  purposes (handling and answering the request, keeping it as evidence), the legal condition
  (Art. 5(2)(ç) legal obligation, Art. 5(2)(e) establishing or defending a right), recipients,
  transfers abroad, collection method and retention; or a link to the main notice when it covers
  requests.
- **Prevalence:** 3/15 (20%), rare
- **Applies when:** always
- **Facts:** `facts.tr.kvkk_notice_url`, `facts.tr.legal_bases`, `facts.tr.transfer_tools`, `facts.data.retention`
- **Patterns:**
  - 1/3 a separate, titled Aydınlatma Metni on its own page, purposes grouped by legal condition;
    1/3 one paragraph with purposes, conditions, recipients, server abroad and retention; 1/3 a
    link in a checkbox.
  - 3/15 also put a purpose-limit line by the identity fields (one template text).
- **Avoid:** asking consent ("rıza" or "izin") to process the application's data, or bundling it
  with the notice: 3/15 (s09, s12, s13; s12 in one required box "Aydınlatma Metni'ni okudum ve …
  rıza gösteriyorum"). Answering is a legal duty under KVKK Art. 13, so the processing rests on
  Art. 5(2)(ç); the Board's decision "Hizmetin Açık Rıza Şartına Bağlanması" holds that asking
  consent where another condition exists misleads the person and abuses the right (Art. 4), and
  the Aydınlatma Yükümlülüğü Tebliğ Art. 5(1)(f) keeps informing and consent apart.
- **Quote:** "… KVKK md. 5/2-ç (hukuki yükümlülük) ve md. 5/2-e (hakların korunması) hukuki sebeplerine dayanılarak işlenir." (s15)
- **Commonly omitted:** any notice for the form's data (12/15 give none).

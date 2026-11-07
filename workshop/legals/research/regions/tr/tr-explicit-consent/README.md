# tr-explicit-consent: build record

Built 2026-10-27 (region run `tr`, `part: whole`; PLAN.md item 12, decisions 25, 27, 45–47, 50).
Skeleton: `plugins/fatodono-founderkit/skills/legals/regions/tr/tr-explicit-consent.md`. Catalog row added to
`regions/tr/catalog.md`.

## Files

- `candidates.md`: 28 pool rows and the reserve (rows 29–63), from the shared KVKK pool, with the
  `transfer-consent` and `etk` tags and the first-screen drops.
- `../kvkk-pool/pool/`: the shared KVKK pool's raw rows (decision 45).
- `samples/sNN.md`: one extraction table per sample, s01–s20.
- `raw/`: stripped texts (git-ignored, never committed or shipped).
- `merge.md`: section ids and meanings, drafting boilerplate (decision 44), mapping notes, section
  map, merged list over s01–s20, patterns (first batch and saturation batch), *Avoid* candidates,
  document level, facts preview, copies, first-batch qualification, saturation log, changes.

## Run

- **Routes run:** the *Açık rıza URL* column of the shared pool's `tr-apps`, `tr-large` and
  `tr-tail` slices, and every row of `tr-consent` (KAP, İSO 500 and Fortune Türkiye 500 → R4; R1
  and R2 with `cc=tr`; footer and web search "açık rıza metni" → R4). 68 distinct companies.
- **Pool:** 28 candidates (8 large, 10 mid, 10 small); large ran short (10 large companies with a
  consent URL, one script-rendered, one re-sized mid; no large reserve). Decision 46 (cut-off and
  Art. 6 check) does not apply to this item: no text was dropped for its date or its transfer
  section. 5 dropped at the first screen (3 empty pages, 2 not customer consent texts).
- **First batch:** s01–s15 (candidates 1–15, 5 per size). All valid; none replaced.
- **Saturation:** batch 1 s16–s20 (candidates 16–20), all valid. Not new: s16, s17, s18, s19,
  s20. No id was added after the first batch: 19 ids throughout.
- **Stop reason:** 5 non-new samples in a row, at s20: `saturated: true`. `sample_count: 20`.
  Pool rows 21–28 were not extracted. Reservation in `merge.md` *Saturation*: three of the five
  are under 140 words, but short single-sentence texts are this document's typical shape, so no
  extra batch is proposed.

## Invalid

None. Borderline but valid (`merge.md` *First-batch qualification*): s04 one form from a hub of
six PDFs; s06 a paper patient form on a web page; s07, s10, s11, s12, s14, s15 short on the page,
not thin extractions. In the saturation batch, s16 and s18 are one part of a page that holds
another text (rule 6).

## Templates and copies

Rule 4: no copies. Raw texts compared on 6-word shingles. The highest pair is s13/s17 at 0.33 of
s17's text, one fashion-retail marketing-purposes string; their tables differ, so both are
samples and the string counts once in patterns. Every other pair is under 0.05. The pool's listed
overlaps (TürkKEP/Tuzcular, Tekzen/E-Ticaret360, Gedik/Emlaksitem, the two clinics) each have one
member that was not extracted.

## Size thirds

Valid samples: 7 large, 7 mid, 6 small. Large ran short in the pool (8 of 10); the first 20 did
not reach the shortfall.

## Samples

All fetched 2026-10-27, language `tr`.

| Sample | Company | URL | Sector | Size | Tags |
|---|---|---|---|---|---|
| s01 | Dirk Rossmann Mağazacılık Tic. Ltd. Şti. | https://www.rossmann.com.tr/rossmann-politikalari/musteri-acik-riza-metni | shopping | large | transfer-consent |
| s02 | Paribu Kripto Varlık Alım Satım Platformu A.Ş. | https://www.paribu.com/destek/yasal/paribu-kripto-varlik-alim-satim-platformu-as-musterilere-iliskin-acik-riza-metni | finance | mid | transfer-consent |
| s03 | Harun Yardımcı (EatWell) | https://geteatwell.app/legal/tr/saglik-verisi-acik-riza.html | health-fitness | small | transfer-consent |
| s04 | Emaa Sigorta A.Ş. | https://s3.emaasigorta.com.tr/emaasigorta/Ueruen_veya_Hizmet_Alan_Kisi_Acik_Riza_Formu_701b637806.pdf | finance | large | transfer-consent |
| s05 | Eren Perakende ve Tekstil A.Ş. (FashFed) | https://www.fashfed.com/acik-riza-metni | shopping | mid | transfer-consent |
| s06 | Uzm. Dr. Hande Arda | https://www.handearda.com/tr/yasal-uyari-bilgilendirme/hasta-ve-hasta-yakini-kisisel-verilerinin-islenmesine-yonelik-acik-riza-metni | medical | small | transfer-consent |
| s07 | T.C. Ziraat Bankası A.Ş. | https://www.ziraatbank.com.tr/tr/bankamiz/gizlilik-ve-cerez-politikalari/kisisel-verilerin-islenmesine-yonelik-acik-riza-onay-formu | finance | large | transfer-consent |
| s08 | Eczacıbaşı Evital Sağlık Hizmetleri ve Tic. A.Ş. | https://evital.com.tr/kisisel-verilerin-islenmesi | health-fitness | mid | |
| s09 | Selin Çiftçi (Butika) | https://butika.ai/acik-riza-metni/ | shopping | small | transfer-consent |
| s10 | Tekzen Taşımacılık Tic. ve San. Yatırım A.Ş. | https://www.tekzen.com.tr/acik-riza-metni | e-commerce | large | etk |
| s11 | Doğa Sigorta A.Ş. | https://www.dogasigorta.com/acik-riza-metni | finance | mid | transfer-consent |
| s12 | Arifoğulları Otomotiv San. Tic. Ltd. Şti. (Kızılkaya Business Hotel) | https://www.kizilkayabusinesshotel.com/acik-riza-metni/ | travel | small | transfer-consent |
| s13 | İpekyol Giyim San. Paz. ve Tic. A.Ş. | https://www.ipekyol.com.tr/pazarlama-verilerinin-kullanimina-iliskin-acik-riza-beyani | e-commerce | large | transfer-consent |
| s14 | TÜRKKEP Kayıtlı Elektronik Posta Hizmetleri A.Ş. | https://turkkep.com.tr/kvkk-iletisim-acik-riza-metni/ | productivity | mid | transfer-consent |
| s15 | Solviera Teknoloji Yazılım ve Dijital Hiz. Ltd. Şti. (Cari Plus) | https://cariplus.com.tr/pazarlama-acik-riza-metni | finance | small | |
| s16 | Penti Giyim Tic. A.Ş. | https://www.penti.com/tr/whatsapp-aydinlatma-ve-acik-riza-metni | e-commerce | large | transfer-consent |
| s17 | Lufian Pazarlama Hizmetleri A.Ş. (NE-SAÇ Tekstil) | https://www.lufian.com/acik-riza-metni | shopping | mid | |
| s18 | Ekin Hazal Altıparmak (Look Bubble) | https://lookbubble.com/acik-riza-metni/ | lifestyle | small | transfer-consent |
| s19 | Bauhaus İnşaat Malzemeleri ve Ev Gereçleri Ltd. Şti. | https://www.bauhaus.com.tr/aydinlatma-ve-riza-metni.pdf | e-commerce | large | etk, transfer-consent |
| s20 | T.O.M. Katılım Bankası A.Ş. | https://www.tombank.com.tr/assets/images/doc/tombank-acik-riza-metni.pdf | finance | mid | |

Versions and parts taken: s04 the general form from a hub of six (rule 6); s16 the consent part
only, not the WhatsApp notice above it; s18 the user tab, not the business tab; s17 names an
operating company (NE-SAÇ Tekstil) that differs from the candidate row.

## Skeleton

17 sections: 5 core (`controller`, `notice-link`, `purposes`, `data-categories`,
`consent-statement`), 3 common (`recipients`, `transfer-abroad`, `withdrawal`), 9 rare
(`scope-limits`, `consent-records`, `voluntariness`, `retention`, `commercial-messages`,
`security`, `user-duties`, `guardian`, `changes`).

Of the 19 ids in `merge.md`, 2 are folded: `intro` (5/20) into `controller` and `rights` (4/20)
into `withdrawal`, as drafting content no fact decides (`skeleton-format.md` rare-section rule).
The header note limits the text to purposes with a `5/1` or `6/3-a` condition and transfers with
tool `occasional`, keeps it separate from the notice, and bars conditioning a service on consent.

`transfer-abroad` (fixed by the first merge): 15/20, but every sample with it rests a regular
transfer on consent, so that pattern is *Avoid*. Its *Applies when* is limited to rows of
`facts.tr.transfer_tools` with tool `occasional`, and its Default is s06's per-case wording. Its
tier moved from core (12/15) to common (15/20) with the saturation batch; the *Applies when* makes
the tier irrelevant to what the writer does.

**Avoid** fields (decisions 47, 50): `notice-link` 1 (bundled with the notice 1/20), `purposes` 2
(consent for processing another condition covers 6/20; blanket consent 4/20), `voluntariness` 1
(consent a condition of the account 1/20), `transfer-abroad` 1 (regular transfer on consent
15/20), `consent-statement` 1 (one acceptance for several purposes 13/20). Guidance cited: KVKK Art. 9 as amended by Law 7499; the Aydınlatma Yükümlülüğü Tebliğ
Art. 5(1)(f), (j); the Board's guides "Açık Rıza Alırken Dikkat Edilecek Hususlar" and "Açık Rıza"
(2025), and its decision
"Hizmetin Açık Rıza Şartına Bağlanması".

## Facts

One key added to `regions/tr/facts.md`: `facts.tr.consent_capture` (per consent: purposes, where
it is asked, own choice, what refusing turns off, the alternative, withdrawal path, whether it is
logged), with *Proposed shared key* `facts.data.consent_capture`. Nothing existing fits:
`facts.tr.acceptance_mechanism` is the contract's acceptance, and `facts.data.cookie_controls` and
`facts.data.telemetry_controls` cover only cookies and telemetry.

Reused from `tr-kvkk-notice` and `tr-distance-sales`: `facts.tr.legal_bases`,
`facts.tr.transfer_tools`, `facts.tr.kvkk_notice_url`, `facts.tr.seller_registry`. Shared:
`facts.company.*` (legal name, address, contact email, phone, acts as processor, group companies,
published policies, change notice), `facts.product.*` (name, services in scope, features, AI
features, public content, business use, account roles, min age, child directed), `facts.data.*`
(subject categories, collected, sensitive, purposes, tracking, cookie controls, other recipients,
storage locations, retention, security measures), `facts.processors.list`,
`facts.users.rights_channels`, `facts.marketing.*`. `tools/check-facts` exits 0.

## Regional content

None: a `whole` skeleton for a region-only item.

## Decisions (chief of staff, 2026-10-27)

- `transfer-abroad` goes to common by count; its fixed *Applies when* and Default stay.
- No extra batch: saturated at s20.
- Both writer choices stay, each with a sourced reason in the skeleton (`merge.md` *Changes*):
  one unticked choice per consent rests directly on the Board's guide "Açık Rıza" (2025, p. 10:
  a separate consent per purpose) and "Doğru Bilinen Yanlışlar -II-" (2026, question 8: opt-in
  only, decision 2020/173). `withdrawal` *Applies when: always* rests on Icerik/2037 and
  "Doğru Bilinen Yanlışlar -II-" questions 6–7 (withdrawal at any time, as easy as consenting) and
  "Açık Rıza" p. 11 (the person must know the consequences of consenting); no source requires the
  text to state the right in terms.
- One acceptance for several purposes is an *Avoid* on `consent-statement` (decisions 47/50):
  13/20, counting only texts that cover more than one purpose with a single acceptance; cited to
  the Board's guide "Açık Rıza" (2025, p. 10). `withdrawal` stays always, with the inference
  stated.

## Open for the owner

- **ETK permission.** 4/20 put the commercial-message permission inside the KVKK consent. The
  skeleton keeps it as a rare section with its own choice; whether it should instead only point
  to item 51's separate ETK text is item 51's call.

## Lessons

- **The law changed faster than the texts.** 15/20 still rest regular transfers abroad on
  consent, two years after Law 7499; prevalence here measures stale practice, which is why
  decision 47's check matters most for this item.
- **The typical text is one sentence.** 12/20 are one to three unheaded paragraphs ending in the
  consent verb; small companies write the longest and most structured texts (s03, s06, s18).

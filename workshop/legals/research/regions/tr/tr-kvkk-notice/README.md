# tr-kvkk-notice: build record

Built 2026-10-27 (region run `tr`, `part: whole`; PLAN.md decision 45, track A). Skeleton:
`plugins/fatodono-founderkit/skills/legals/regions/tr/tr-kvkk-notice.md`. Item 11 of the seed catalog (KVKK
Aydınlatma Metni for customers and users). Catalog row added to `regions/tr/catalog.md`.

## Files

- `candidates.md`: the pool of 30 and the reserve (rows 31–69), with each candidate's decision-46
  test tag (`dated`, `art9`, `no-transfer`) and the first-screen drops.
- `../kvkk-pool/pool/`: the shared KVKK pool's raw rows (decision 45), also used by
  `tr-explicit-consent` and the `tr` block of `data-subject-request`.
- `samples/sNN.md`: one extraction table per sample, s01–s20.
- `raw/`: stripped texts (git-ignored, never committed or shipped).
- `merge.md`: section ids and meanings, drafting boilerplate (decision 44), mapping notes, section
  map, merged list over s01–s20, patterns, *Avoid* candidates, document level, facts preview,
  copies, first-batch qualification, saturation log and decision, changes.

## Run

- **Routes run:** KAP BIST list, İSO 500 and Fortune Türkiye 500 → R4 (`tr-large`, 28 rows); R1
  with `cc=tr` (`tr-apps`, 49 rows); R2 with Turkish keywords (`tr-tail`, 42 rows). 119 raw rows,
  106 distinct companies with an Aydınlatma URL.
- **Pool:** 30 candidates, 10 large, 10 mid, 10 small. Group check (rule 5) before the
  first-screen check; 29 companies dropped at the first screen, most under the decision-46 cut-off
  (old-style transfer on consent, no new Art. 9 tools and no date on or after 2024-06-01, or a
  pre-cut-off date). Under the narrowed decision 46, undated notices with no transfer section
  were kept as `no-transfer` unless they rest special-category data on consent alone (1 dropped).
  The mid third has no reserve: the five `no-transfer` mid rows exactly fill it.
- **First batch:** s01–s15 (candidates 1–15, 5 per size). All valid; none replaced. None is
  `no-transfer`.
- **Saturation:** batch 1 s16–s20 (candidates 16–20), all valid. Not new: s16, s17, s18, s19,
  s20. No section id was added after the first batch: 23 ids throughout.
- **Stop reason:** 5 non-new samples in a row, at s20: `saturated: true`. `sample_count: 20`.
  Pool rows 21–30 were not extracted. The chief of staff noted that two of the five (s17, s20)
  are short `no-transfer` notices; counted over `dated`/`art9` samples only the run is 3. Decision
  (chief of staff, delegated by the owner, 2026-10-27): follow the rule, no extra batch, since
  thinness is not a `no-transfer` trait (s16, `art9`, is as thin) and the richest sample, s18,
  brought nothing new (`merge.md` *Saturation*).

## Invalid

None. Borderline but valid (details in `merge.md` *First-batch qualification*): s02 published with
bracket placeholders; s04 publishes its main tables as images and names no Art. 9 tool for its
foreign recipients; s09 is a short notice (6 rows), checked against its raw text, not a thin
extraction; s14 is a prospective-investor notice with another company's name left in it.

## Templates and copies

Rule 4: no copies. Raw texts compared on 6-word shingles; the highest overlap is s07/s13 at 0.28
(a law-firm block: VERBİS purpose strings, the rights list and the application paragraphs).
s09, s11 and s16 share a stock opening frame (0.11–0.25). Each shared block counts once in
patterns (decision 39). No generator template was found.

## Size thirds

Valid samples: 7 large, 7 mid, 6 small. No size ran short; the uneven third is only where the
stop fell (s16–s20 were large, mid, small, large, mid).

## Samples

All fetched 2026-10-27, language `tr`.

| Sample | Company | URL | Sector | Size | Test |
|---|---|---|---|---|---|
| s01 | Dirk Rossmann Mağazacılık Tic. Ltd. Şti. | https://www.rossmann.com.tr/rossmann-politikalari/musteri-aydinlatma-metni | shopping | large | art9 |
| s02 | Lufian Pazarlama Hizmetleri A.Ş. | https://www.lufian.com/kvkk-aydinlatma-metni | shopping | mid | dated, art9 |
| s03 | Mahir Baran Aydoğan (6 Tekrar) | https://6tekrar.com/yasal/aydinlatma-metni | health-fitness | small | dated |
| s04 | ING Bank A.Ş. | https://www.ing.com.tr/tr/ing/kisisel-verilerin-korunmasi/kisisel-verilerin-islenmesi-hakkinda-aydinlatma-metni | finance | large | dated |
| s05 | Multinet Kurumsal Hizmetler A.Ş. | https://multinet.com.tr/sites/default/files/static/kullanici-aydinlatma-metni.pdf | finance | mid | art9 |
| s06 | Solviera Teknoloji Yazılım ve Dijital Hizmetler Ltd. Şti. (Cari Plus) | https://cariplus.com.tr/kvkk-aydinlatma-metni | finance | small | dated |
| s07 | Shaya Kahve (Starbucks Türkiye) | https://www.starbucks.com.tr/kisisel-verileri-aydinlatma-metni | food-drink | large | art9 |
| s08 | Eczacıbaşı Evital Sağlık Hizmetleri ve Tic. A.Ş. | https://evital.com.tr/kullanici-aydinlatma-metni | health-fitness | mid | art9 |
| s09 | Fırsat Yapay Zeka Teknolojileri A.Ş. | https://firsat.com/kvkk-aydinlatma-metni | shopping | small | dated |
| s10 | Türk Telekomünikasyon A.Ş. | https://www.turktelekom.com.tr/destek/kvkk-aydinlatma-metinleri | utilities | large | art9 |
| s11 | Pluxee Çalışan Deneyimi Dan. ve Paz. Hiz. A.Ş. | https://www.pluxee.com.tr/kilavuz/kart-kulanicisi-aydinlatma-metni/ | food-drink | mid | art9 |
| s12 | Gazioğlu Yazılım A.Ş. (Ortak Market) | https://ortakmarket.com/gizlilik-politikasi | business | small | dated |
| s13 | Mudo Satış Mağazaları A.Ş. | https://www.mudo.com.tr/musteri-aydinlatma-metni | e-commerce | large | art9 |
| s14 | Gedik Yatırım Menkul Değerler A.Ş. | https://sozlesme.gedik.com/doc/kvkk_aydinlatma_metni.htm | finance | mid | art9 |
| s15 | Turuncu Deneyim Org. ve Tekn. Ltd. Şti. (Society) | https://societyapp.org/aydinlatma-metni.html | lifestyle | small | dated |
| s16 | FLO Mağazacılık ve Pazarlama A.Ş. | https://www.flo.com.tr/aydinlatma-metni | shopping | large | art9 |
| s17 | BKM Kitap Kırtasiye San. ve Tic. Ltd. Şti. | https://www.bkmkitap.com/6698-sayili-kisisel-verilerin-korunmasi-kanunu-aydinlatma-ve-bilgilendirme-metni | shopping | mid | no-transfer |
| s18 | Ali Yılmaz (Güven Sürücü Kursları) | https://www.guvensurucukursu.com.tr/aydinlatma-metni/ | education | small | dated |
| s19 | Getir Perakende Lojistik A.Ş. | https://www.getir.com/yardim/kvkk/ | food-drink | large | dated, art9 |
| s20 | Paribu Kripto Varlık Alım Satım Platformu A.Ş. | https://www.paribu.com/destek/yasal/paribu-kripto-varlik-alim-satim-platformu-as-musterilere-iliskin-aydinlatma-metni | finance | mid | no-transfer |

Versions and parts taken: s10 the first tab (Türk Telekom customer notice) of a page holding four
group companies' notices; s20 the Paribu A.Ş. customer notice only, not the group company's notice
that follows on the same page; s06 the notice only, not its annexed consent texts and request
guidance (rule 6); s17 and s18 name an operating company as controller that differs from the
app seller.

## Skeleton

20 sections: 8 core (`intro`, `data-categories`, `collection-method`, `purposes`, `recipients`,
`transfer-abroad`, `rights`, `application`), 5 common (`controller`, `special-categories`,
`cookies-tracking`, `security`, `retention`), 7 rare (`controller-role`, `user-duties`,
`integrations`, `children`, `consent-withdrawal`, `automated-decisions`, `changes`).

Of the 23 ids in `merge.md`, 3 are folded: `definitions` (5/20) and `notice-status` (3/20) into
`intro`, as drafting content no fact decides (`skeleton-format.md` rare-section rule); `ai-use`
(1/20) into `purposes`. The header note makes every Art. 10(1) item apply always, so `controller`
is written in every notice although it is common by count (7/20 name the controller only in the
intro).

**Avoid** fields (decision 50, owner-approved): `purposes` 2 (consent stacked on another condition
3/20; condition not named per purpose 4/20), `collection-method` 1 (open-ended catch-alls 2/20),
`transfer-abroad` 2 (regular transfer on consent 1/20; no Art. 9 tool 1/20). Guidance cited: KVKK
Art. 9 as amended by Law 7499, the Aydınlatma Yükümlülüğü Tebliğ Art. 5(1), and the Board's
guidance "Kişisel Verilerin İşlenme Şartları" and "Açık Rıza Alırken Dikkat Edilecek Hususlar".

## Facts

Six keys added to `regions/tr/facts.md` (owner-approved): `facts.tr.legal_bases`,
`facts.tr.transfer_tools`, `facts.tr.verbis`, `facts.tr.representative`,
`facts.tr.collection_channels`, `facts.tr.destruction_policy`.

- **`legal_bases` stays in `tr`** (decision 29 checked). `eu` has no legal-basis key: its
  privacy-policy block and RoPA read the GDPR basis from the shared `facts.data.purposes`. KVKK's
  conditions are not GDPR Art. 6 relabelled (law, made-public and legal-claims conditions stand on
  their own; no public task; Art. 6(3) differs from GDPR Art. 9(2)), and one purpose can rest on a
  different condition under each law, so a shared field cannot hold both. This follows
  `facts.uk.special_conditions`, which keeps the UK's own conditions.
- **`representative`** is named after `facts.eu.representative` and `facts.uk.representative`
  (the proposed `controller_representative` was renamed).
- **`verbis`** carries a *Proposed shared key* line, `facts.registrations.privacy_regulator`, the
  name `facts.uk.ico_registration` already announces for the same kind of fact. It is not
  promoted here.
- **`transfer_tools`** keeps its name. `facts.eu.transfer_mechanisms` and
  `facts.uk.transfer_mechanisms` list tools only; the KVKK key is per transfer (recipient,
  country, tool, notification date), because the standard contract is notified per transfer.

Reused: `facts.company.*` (legal name, address, contact email, phone, acts as processor,
processor customers, joint controllers, group companies, published policies, change notice),
`facts.product.*` (name, services in scope, public content, business use, account roles,
integrations, platform disclosures, min age, child directed, features, AI features),
`facts.data.*` (subject categories, collected, third-party sources, sensitive, purposes,
tracking, cookie controls, other recipients, sells, storage locations, retention, kept after
deletion, automated decisions, security measures), `facts.processors.list`,
`facts.users.rights_channels`, `facts.marketing.*`, and `facts.tr.seller_registry` and
`facts.tr.sales_model` from `tr-distance-sales`. `tools/check-facts` exits 0.

## Regional content

None: a `whole` skeleton for a region-only item.

## Open for the owner

- **VERBİS promotion.** `facts.uk.ico_registration` and `facts.tr.verbis` are the same kind of
  fact in two regions, which meets decision 29's condition. Promoting means a shared key in
  `helpers/facts-schema.md` and renaming the `uk` references; left for the maintainer.
- **`transfer_tools` name.** Keep it, or rename it `facts.tr.transfer_mechanisms` to match the
  `eu`/`uk` names despite the different shape?
- **Allowlist.** `tools/check-facts` still allowlists `facts.tr.verbis` in `build-task.md` as an
  undefined example; the key now exists, so the entry can go.
- **Privacy policy and notice.** A product with users in Turkey gets both the privacy policy and
  this notice. The writer should fill both from the same facts; whether the privacy policy's `tr`
  block should then only point here is not settled.

## Lessons

- **The cut-off shapes prevalence.** Decision 46's tests favour notices with a transfer section,
  so `transfer-abroad` reads 18/20; the two samples without it are the two `no-transfer` ones.
- **Small companies write the longest notices.** Several 2026-dated small notices (s03, s06,
  s12, s18) are detailed, plain and product-specific; large companies' texts are mostly
  law-firm frames with VERBİS purpose strings.
- **The section list was stable from the first batch.** Every saturation sample mapped onto the
  first batch's 23 ids.

# ropa, `tr` block: extraction notes

Given to every `sample-extractor` in this run, on top of the global run's notes
(`research/ropa/extract-notes.md`, which still apply: what one sample is, the extra *Document*
lines, one row per field or column, the `table` / `list` / `prose` / `embedded` / `pointer`
formats, the `[law: ...]` mark).

## What the sample is

The KVKK "kişisel veri işleme envanteri" (also "kişisel veri envanteri", "KVK envanteri") or
a published VERBİS registration summary. Read only content that applies under Turkish law;
an English or GDPR column in a bilingual file is noted in *Document* and not extracted.

- A VERBİS summary lists categories, not processes. Record that under *Status* and extract
  its fields as they are.
- A model inventory (`size: none`): read the blank grid, its worked example rows and the
  guide's instructions for each column.

## Extra Document lines

- **Status:** filled inventory, VERBİS summary, inventory annex inside another document, or
  model.
- **VERBİS:** whether the sample names VERBİS, a sicil number or the registration duty, and
  where.
- **Retention policy link:** whether it points to a Saklama ve İmha Politikası, and how
  (column, footnote, intro sentence).

## Fields to watch

Write these exactly as the sample does; they are what the `tr` block is built from.

- **Legal ground.** Which KVKK articles and points are cited (Art. 5(1) explicit consent,
  5(2)(a)–(ç)…(f), 6(2)/(3) for special categories, the 2024 wording of Art. 6), as article
  numbers, letters, the law's own phrases, or short labels.
- **Special categories ("özel nitelikli kişisel veri").** How they are flagged, and which
  condition is cited.
- **Data categories.** Whether the vocabulary is VERBİS's fixed list (Kimlik, İletişim,
  Lokasyon, Özlük, Hukuki İşlem, Müşteri İşlem, Fiziksel Mekan Güvenliği, İşlem Güvenliği,
  Risk Yönetimi, Finans, Mesleki Deneyim, Pazarlama, Görsel ve İşitsel Kayıtlar, ...) or the
  sample's own.
- **Subject and recipient groups.** Fixed VERBİS-style labels or own words.
- **Retention.** "Azami saklama süresi": a period per row, per category, or a pointer; the
  statute behind it; the link to the retention and destruction policy and periodic destruction.
- **Transfer abroad.** Yes/no, destination, and the mechanism named (adequacy decision,
  standard contract, BCR, undertaking, Art. 9(6) incidental transfer, explicit consent under
  the pre-2024 Art. 9).
- **Security measures.** VERBİS's fixed idari / teknik tedbirler list or own words; once for
  the whole inventory or per row.
- **Process / department.** The "iş süreci", "süreç", "faaliyet" and "birim / departman"
  columns and how they group the rows.
- **Anything else** a Turkish inventory has that a GDPR RoPA lacks (data source, collection
  method "toplama yöntemi", medium "ortam" physical/electronic, "aydınlatma" or "açık rıza"
  status columns, "irtibat kişisi" contact, sicil number).

Mark every such cell `[law: KVKK Art. N]` or `[law: Veri Sorumluları Sicili Yönetmeliği]` as
the global notes say.

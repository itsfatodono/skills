---
code: tr
name: Turkey
laws:
  - KVKK (6698 sayılı Kişisel Verilerin Korunması Kanunu)
  - 6502 sayılı Tüketicinin Korunması Hakkında Kanun
  - Mesafeli Sözleşmeler Yönetmeliği (2014)
  - 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun
languages: [tr]
storefront: tr
added: 2026-10-26
---

## Sources

Where samples for this region are found. Shared routes (R1–R12) and the candidate rules are in
`build/sources.md`; only the Turkey-specific parameters are here. Item numbers are those of the seed
catalog in `PLAN.md` until `helpers/catalog.md` exists. Routes were checked on 2026-10-26.

### Pool

Build the pool with R1 and R3 using `cc=tr`, `hl=tr`, `gl=TR`, plus R2 with Turkish keywords
for small companies. Add large companies from KAP's BIST list
(`kap.org.tr/tr/bist-sirketler`), İSO 500 and Fortune Türkiye 500. Then read each site's
footer and checkout, per item below.

Small sellers without an app are reached by Turkish-keyword web search ("mesafeli satış
sözleşmesi" plus a product word: `kahve`, `seramik`, `online eğitim`) and then R4 on the
seller's own site.

### Documents

| Items | Where | Expected pool |
|---|---|---|
| 10 Künye | The homepage "İletişim" block required by Art. 5(1) of the 2022 Elektronik Ticaret Aracı Hizmet Sağlayıcı ve Elektronik Ticaret Hizmet Sağlayıcılar Hakkında Yönetmelik (unvan, MERSİS, address, KEP, e-mail, phone). | ≥30 |
| 11 Aydınlatma Metni, 12 Açık Rıza Metni, 51 ETK consent | Footer labels "Kişisel Verilerin Korunması", "KVKK", "… Aydınlatma Metni", "Açık Rıza Metni", "İlgili Kişi / Veri Sahibi Başvuru Formu" (often a PDF), "Ticari Elektronik İleti Aydınlatma / Açık Rıza Metni". Signup forms link the same texts. | ≥30; 51 ≥20 |
| 13 data subject request, `tr` block | The shared KVKK pool's *Başvuru formu URL* column (`research/regions/tr/kvkk-pool/`): forms linked from the KVKK page or footer ("İlgili Kişi / Veri Sahibi Başvuru Formu"), mostly PDFs on the company's CDN; KAP, İSO 500 and Fortune Türkiye 500 → R4 for large companies, R1/R2 `cc=tr` for apps. Small developers rarely publish one, and mid and small ran short on 2026-10-27 (`research/regions/tr/data-subject-request/candidates.md`). | ~25 (24 found) |
| 18 VERBİS inventory | VERBİS public query at `verbis.kvkk.gov.tr/sicil-sorgula`. It takes one controller name per query behind a captcha, so search for the pool's companies by name. VERBİS summaries are samples of item 18; they cover the inventory's categories, not its full layout. On 2026-10-26 no company (44 sites) or public university (about 45 KVKK sites) published a filled inventory, so the block was not built (`research/regions/tr/ropa/README.md`). | 0 found |
| 19 Saklama ve İmha Politikası | Web-search `"saklama ve imha politikası" filetype:pdf`; finance firms publish the most. These texts are rarely in footers. | ≥20 |
| 39 Mesafeli Satış Sözleşmesi (`tr-distance-sales`), 40 Ön Bilgilendirme Formu, 41 withdrawal notice | Footer "Satış Sözleşmesi", "Mesafeli Satış Sözleşmesi" or "İşlem Rehberi", and the checkout checkbox "Ön Bilgilendirme Formu ve Mesafeli Satış Sözleşmesi". Many sites show these only after a product is in the cart. | ≥30 |
| 72 employee notice | "çalışan adayı aydınlatma metni" on career pages; process-level personnel notices on public universities' `kvkk.<university>.edu.tr` sites. | ≥20 |

### Template texts

E-commerce platforms ship ready contract texts: IdeaSoft ships ready drafts, and Shopify TR
shops use contract apps.

The most copied text is not a platform default: a full distance sales contract published at
`forbes.com.tr/mesafeli-satis-sozlesmesi` (also on Law Insider TR) appears word for word on
ikas, Ticimax, WooCommerce, IdeaSoft and custom shops, and in parts of large retailers'
contracts. An older pre-2014 shop template circulates too. In the 2026-10-26 run, 7 of 13
small candidates used the forbes.com.tr text; under candidate rule 4 they count as one
sample. Sellers of digital content and services write their own texts far more often.

### Blocked sites

Trendyol, Hepsiburada, n11 and Sahibinden answered scripted fetches with 403: use rule 2's
Wayback fallback. In the 2026-10-26 run, Çiçeksepeti, A101, Teknosa, DeFacto, Mavi, Watsons and
Koçtaş also blocked scripts, and LC Waikiki, Koton, MediaMarkt, Migros and others showed the
contract only at checkout; the Wayback CDX index was offline, so none of them was sampled.

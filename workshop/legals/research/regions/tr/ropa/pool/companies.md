# ropa / tr pool slice: companies, foundations, associations, private schools, private hospitals

Run 2026-10-26. Result: 0 qualifying rows. No company, foundation, association, private school or private hospital was found publishing its own filled Kişisel Veri İşleme Envanteri or a VERBİS registration summary.

| Company | Sector guess | Size guess | Document URL | Format | Rows (approx.) | Notes |
|---|---|---|---|---|---|---|
| (none) | | | | | | |

## Not samples

Retention and destruction policies (item 19, not ropa). Each was downloaded and grepped for "envanter", "alıcı grubu", "hukuki sebep", "azami". None has a process x category x purpose x legal ground x subject group x recipient x retention grid; they only define the inventory in the definitions section and carry a per-category retention table.

| URL | Why not a sample |
|---|---|
| https://bereket.com.tr/StaticFiles/pdf/Bereket_Emeklilik_Veri_Saklama_ve_Imha_Politikasi.pdf | Saklama ve İmha Politikası (item 19); inventory only defined |
| https://www.odeabank.com.tr/medium/document-file-1217.vsf | Same; retention table only |
| https://www.bimar.com.tr/files/Bimar_tr/docs/kisisel_verileri_saklama_ve_imha_politikasi.pdf | Same; EK-A is a retention/destruction period table, EK-B is a roles table |
| https://www.radtek.com.tr/kvkk/K3.pdf | Same |
| https://www.turmob.org.tr/arsiv/kvkk/1_TURMOB_Kisisel_Veri_Saklama_ve_Imha_Politikasi.pdf | Same (professional body, not in slice) |
| https://www.halkbank.com.tr/content/dam/halkbank/tr/dokumanlar/genel/kvkk-formlari/10112021-KisiselVerileriSaklamaveimhaPolitikasi.pdf | Same; Ek-1 is a list of subject groups |
| https://www.kfw-ipex-bank.de/PDF/Über-die-KfW-IPEX-Bank/Standorte/Istanbul/TOCC-2058-KfW-IPEX-Bank_Personal-Data-Storage-and-Destruction-Policy_-(TR).pdf | Same; foreign bank branch |
| https://denizyatirim.com.tr/asset/FooterPdf/1719388736.pdf | Fetch returned 244 bytes (not a document); search snippet showed a policy referring to third parties in Ek-1 |
| https://www.gsdbank.com.tr/assets/kvkk/Kişisel Veri Saklama ve İmha Politikası.pdf | Failed to load (curl 000, non-ASCII path); policy anyway |
| https://www.amerikanhastanesi.org/getmedia/deec475d-a4da-4bdf-a625-d30c6e223dd5/KISISEL-VERILERIN-KORUNMASI-POLITIKASI.pdf.aspx | Private hospital data protection policy; no inventory (0 hits for "envanter") |
| https://www.kuh.ku.edu.tr/getmedia/23b489bd-2ba0-45b7-be11-f49a0c03c88d/kocKvkk.pdf.aspx | Koç University Hospital patient notice (aydinlatma); not an inventory |
| https://www.yyd.org.tr/documents/KVKK%20Dosyalar/yeyuzu-doktorlari-kisisel-veri-koruma-politikasi.pdf | Association (Yeryüzü Doktorları) data protection policy; loaded but pdftotext produced no text (scanned or protected), unchecked beyond title; policy type, not inventory |
| https://www.sp.k12.tr/wp-content/uploads/2026/05/KVKK-Belgesi-2026.pdf | Private school KVKK document; notice-style, no inventory grid |
| https://www.isov.org.tr/Pdf/bursiyerAydınlatmaMetni.pdf, https://basvuru.anadoluvakfi.org.tr/download/anadolu_vakfi_bursiyer_adayi_kisisel_verilerin_islenmesi_aydinlatma_metni.pdf | Foundation aydinlatma metni (item 11), seen via search snippet only |
| https://taskolej.k12.tr/index.php/en/corporate/personal-data-protection-law | Private school aydinlatma notice, snippet only |

Other non-samples: the Akbank `/kvkk` page mentions "Kişisel Veri Envanteri ... VERBİS" in two bullets only; the 40+ BIST/e-commerce homepages and `/kvkk`, `/kisisel-verilerin-korunmasi`, `/kisisel-veriler` paths on 16 of them had no link or text with "envanter" or "VERBİS" beyond that. Law-firm and consultancy pages (mihci.av.tr, harbiyehukuk.com, hukukcularevi.com, ffkpartnerhukuk.com.tr, cottgroup), template sellers (mustafabaysal.com, kvkk.biz, verikasifi.com) and official guides/samples (kvkk.gov.tr Envanter Hazırlama Rehberi, Sorularla VERBİS, psikiyatri.org.tr Ek-D VERBİS Kayıt Kılavuzu) are excluded by rule. University decks (Marmara, METU) are public bodies, outside this slice.

Candidates noted: none. No retention policy was found containing the full inventory as an annex ("annex in retention policy").

## Searches run

WebSearch (standard unless noted):
1. `"kişisel veri işleme envanteri" filetype:pdf -rehber`
2. `"veri envanterimiz" "azami saklama süresi" "ilgili kişi grubu"`
3. `"VERBİS'e kayıtlı" "veri kategorileri" "azami saklama süresi" şirket`
4. `"kişisel veri envanteri" dernek OR vakıf pdf "alıcı grubu"`
5. `"kişisel veri envanteri" özel hastane OR "özel okul" "hukuki sebep" "saklama süresi"`
6. (extended) `"kişisel veri işleme envanteri" "veri kategorisi" "işleme amacı" "hukuki sebep" "saklama süresi" A.Ş. kvkk sayfası`
7. `"VERBİS" "kayıtlı bilgilerimiz" veri sorumluları sicili özet tablo ...`
8. `kvkk "envanter" .xlsx "ilgili kişi grubu" site:.com.tr`
9. `"Kişisel Veri Saklama ve İmha Politikası" ekler "Kişisel Veri İşleme Envanteri" "Ek" ...`
10. `"Veri Kategorisi" "Aktarılan Alıcı Grubu" "Azami Saklama Süresi" "Veri Konusu Kişi Grubu" tablo ...`
11. `"VERBİS kayıt bilgileri" şirketimiz ...`
12. dernek `"kişisel veri işleme envanteri"` ... tablo
13. vakıf kvkk `"veri işleme envanteri"` öğrenci bağışçı burs ...
14. özel okul kolejleri `"kişisel veri envanteri"` veli öğrenci ...
15. hastanesi `"kişisel veri işleme envanteri"` hasta ...
16. (extended) `"Veri Sorumluları Sicil" şirketimiz "kayıtlı" ...`
17. `"envanter" "kişisel veri" "süreç" ... xlsx OR docx OR pdf indir şirket`
18. `"Kişisel Veri İşleme Envanteri" "EK-1" ... vakıf OR dernek OR hastane OR okul`

Not run: `site:` operator variants, "KVK Envanteri"/"Veri Envanteri" title variants, per-company name searches, VERBİS sicil-sorgula (captcha, one controller per query).

curl (`-A "Mozilla/5.0"`): homepages of 44 companies (Turkcell, Türk Telekom, Garanti BBVA, Akbank, Yapı Kredi, Koç, Sabancı, Arçelik, Pegasus, Migros, BİM, Şişecam, Ford Otosan, Tofaş, Enerjisa, Aksa, Doğuş, Eczacıbaşı, Getir, Trendyol, Hepsiburada, Papara, Insider, Tüpraş, Kordsa, Vestel, Aselsan, Sahibinden, n11, Çiçeksepeti, Yemeksepeti, Boyner, LCW, Mavi, Koton, DeFacto, Teknosa, Vakıfbank, İş Bankası, Ziraat, Halkbank, QNB, Denizbank, ING) grepped for `envanter|verbis` in hrefs. Zero hits (Enerjisa matched an unrelated sentence). Blocked or tiny responses: Arçelik, DeFacto, Getir, Hepsiburada, Pegasus, Mavi, n11, Sahibinden, Şişecam, Teknosa, Çiçeksepeti, Aselsan; Trendyol returned an empty body. `/kvkk`, `/kisisel-verilerin-korunmasi`, `/kisisel-veriler` tried on 16 of them (Turkcell, TT, Garanti, Akbank, YKB, Koç, Sabancı, Tofaş, Ford Otosan, Migros, BİM, Enerjisa, Eczacıbaşı, Doğuş, Papara, Tüpraş): only akbank.com/kvkk matched, with the two sentences above.

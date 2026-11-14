with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix unescaped single quotes in DEFAULT_AUDIT_ITEMS
# Let's replace the DEFAULT_AUDIT_ITEMS block cleanly with backticks or escaped strings
old_block = """    const DEFAULT_AUDIT_ITEMS = [
      {
        id: 'item_1',
        title: 'TikTok Handle Standardizasyonu',
        desc: '@heritage.cafe.bake olan TikTok adını mümkünse @heritagecafeandbakery olarak eşitleyin.',
        category: 'TikTok',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_2',
        title: 'Biyografi ve Biolink / Linktree Kurulumu',
        desc: 'Bioya: Ankara/Çankaya Reşit Galip No:18, Kapanış 18:00, Harita, Menü ve Trendyol Go linki ekleyin.',
        category: 'Tüm Kanallar',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_3',
        title: 'YouTube Shorts Kapak Resmi (Thumbnail) Seçimi',
        desc: 'Shorts yüklerken kalem simgesiyle dumanın tüttüğü veya sosun aktığı en iştah kabartan kareyi kapak seçin.',
        category: 'YouTube',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_4',
        title: 'Tıklatan Başlık Formülü (CTR Optimizasyonu)',
        desc: '"Focaccia yaptık" yerine "Ankara\\'da Böyle Uzayan Bir Peynir Görmediniz! 🧀" tarzı merak kancaları kullanın.',
        category: 'YouTube & TikTok',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_5',
        title: 'İlk 3 Saniye Kancası (Hook) Kuralı',
        desc: 'Videoya sessiz başlamayın; ilk 1 saniyede duman, çatal batırma veya çıtır ses + iddialı ekran yazısı girsin.',
        category: 'Video Üretimi',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_6',
        title: '3 Adet Sabitlenmiş Video (Pinned Posts)',
        desc: 'Profilin tepesine: 1) Biz Kimiz, 2) İmza Lezzetler (Cinnabon/Samsa), 3) Reşit Galip Yol Tarifi videolarını sabitleyin.',
        category: 'Instagram & TikTok',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_7',
        title: 'LinkedIn Şirket & Kurucu Sayfası Açılışı',
        desc: 'LinkedIn\\'de profesyonel şirket sayfası açıp Çankaya B2B ofis ikramlarını ve kurucu hikayelerini paylaşın.',
        category: 'LinkedIn B2B',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_8',
        title: 'Yorum & Lead Döngüsü (Katalog Kampanyası)',
        desc: '"Yorumlara KATALOG yazan Çankaya ofislerine ücretsiz deneme kutusu" kampanyasını LinkedIn ve IG\\'de yayınlayın.',
        category: 'B2B Satış',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_9',
        title: 'Haftalık 3 Günlük Paylaşım Rutinine Geçiş',
        desc: 'Salı B2B, Perşembe Cinnabon/Focaccia ASMR, Pazar zanaat fırıncılık hikayesi takvimini uygulayın.',
        category: 'İçerik Takvimi',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_10',
        title: 'Masa Üstü QR Kodlu UGC Madeleine Kampanyası',
        desc: 'Masalara QR kodlu akrilik çadır koyun: "Bizi hikayende etiketle, sıcak Belçika çikolatalı Madeleine ikramımız olsun!"',
        category: 'Dükkan İçi Viral',
        weight: 10,
        done: false,
        note: ''
      }
    ];"""

# In python triple-quoted string, \' needs to be \\' so it appears as \' in JS
# Or even better, use double quotes for string properties or backticks!
new_block = """    const DEFAULT_AUDIT_ITEMS = [
      {
        id: "item_1",
        title: "TikTok Handle Standardizasyonu",
        desc: "@heritage.cafe.bake olan TikTok adını mümkünse @heritagecafeandbakery olarak eşitleyin.",
        category: "TikTok",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_2",
        title: "Biyografi ve Biolink / Linktree Kurulumu",
        desc: "Bioya: Ankara/Çankaya Reşit Galip No:18, Kapanış 18:00, Harita, Menü ve Trendyol Go linki ekleyin.",
        category: "Tüm Kanallar",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_3",
        title: "YouTube Shorts Kapak Resmi (Thumbnail) Seçimi",
        desc: "Shorts yüklerken kalem simgesiyle dumanın tüttüğü veya sosun aktığı en iştah kabartan kareyi kapak seçin.",
        category: "YouTube",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_4",
        title: "Tıklatan Başlık Formülü (CTR Optimizasyonu)",
        desc: "Focaccia yaptık yerine Ankara'da Böyle Uzayan Bir Peynir Görmediniz! tarzı merak kancaları kullanın.",
        category: "YouTube & TikTok",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_5",
        title: "İlk 3 Saniye Kancası (Hook) Kuralı",
        desc: "Videoya sessiz başlamayın; ilk 1 saniyede duman, çatal batırma veya çıtır ses + iddialı ekran yazısı girsin.",
        category: "Video Üretimi",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_6",
        title: "3 Adet Sabitlenmiş Video (Pinned Posts)",
        desc: "Profilin tepesine: 1) Biz Kimiz, 2) İmza Lezzetler (Cinnabon/Samsa), 3) Reşit Galip Yol Tarifi videolarını sabitleyin.",
        category: "Instagram & TikTok",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_7",
        title: "LinkedIn Şirket & Kurucu Sayfası Açılışı",
        desc: "LinkedIn'de profesyonel şirket sayfası açıp Çankaya B2B ofis ikramlarını ve kurucu hikayelerini paylaşın.",
        category: "LinkedIn B2B",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_8",
        title: "Yorum & Lead Döngüsü (Katalog Kampanyası)",
        desc: "Yorumlara KATALOG yazan Çankaya ofislerine ücretsiz deneme kutusu kampanyasını LinkedIn ve IG'de yayınlayın.",
        category: "B2B Satış",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_9",
        title: "Haftalık 3 Günlük Paylaşım Rutinine Geçiş",
        desc: "Salı B2B, Perşembe Cinnabon/Focaccia ASMR, Pazar zanaat fırıncılık hikayesi takvimini uygulayın.",
        category: "İçerik Takvimi",
        weight: 10,
        done: false,
        note: ""
      },
      {
        id: "item_10",
        title: "Masa Üstü QR Kodlu UGC Madeleine Kampanyası",
        desc: "Masalara QR kodlu akrilik çadır koyun: Bizi hikayende etiketle, sıcak Belçika çikolatalı Madeleine ikramımız olsun!",
        category: "Dükkan İçi Viral",
        weight: 10,
        done: false,
        note: ""
      }
    ];"""

pos = text.find('const DEFAULT_AUDIT_ITEMS = [')
end_pos = text.find('let auditItems = [];', pos)

if pos != -1 and end_pos != -1:
    text = text[:pos] + new_block + '\n\n    ' + text[end_pos:]
    with open('build_portal.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Replaced DEFAULT_AUDIT_ITEMS with safe double-quoted block!")
else:
    print("Could not find DEFAULT_AUDIT_ITEMS block!")

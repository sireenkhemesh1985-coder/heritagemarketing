# 🥐 Heritage Cafe & Bakery — Finansal Yönetim, Pazarlama & B2B Portalı

> **"El Emeğiyle Yaşatılan Lezzetler · Save the Heritage"**  
> 📍 **Konum:** 100. Yıl, Reşit Galip Cd. No:18, Çankaya / Ankara  
> 🌐 **Resmi Web Sitesi:** [heritagecafe.com.tr](https://heritagecafe.com.tr)  
> ⏰ **Çalışma Saatleri:** Pazartesi – Cuma: 08:00 – 18:00 | Cumartesi: 08:00 – 15:00 | Pazar: Kapalı  

---

## 📌 Proje Genel Bakış
Bu proje, Ankara Çankaya'da (IVF Merkezi içinde) faaliyet gösteren butik artisan fırın ve kafe **Heritage Cafe & Bakery**'nin 4 aylık fiili muhasebe verilerini (Temmuz – Ekim 2026), 326+ online siparişini, dükkan kasası gelirlerini, tedarik faturalarını ve personel maliyetlerini interaktif olarak analiz eden, büyüme ve B2B kurumsal satış stratejileri sunan kapsamlı bir yönetim portalıdır.

---

## 🚀 Öne Çıkan Özellikler

1. **Finansal Genel Bakış & Günlük Özet:**
   * 804.075 ₺ brüt ciro, 629.127 ₺ kasa geliri, kanal dağılımı (Kasa %78.2, Trendyol %18.4, Yemeksepeti %3.3).
   * %38.8 platform komisyon erozyon analizi ve net hakediş takibi.
2. **Sipariş Listesi (326+ Online Sipariş):**
   * Detaylı filtreleme, arama, komisyon/kesinti hesabı ve tek tıkla CSV dışa aktarma.
3. **Pazarlama & Menü Analitiği:**
   * Ciro liderleri, fırsat ürünleri, Boston Consulting Group (BCG) menü mühendisliği matrisi.
   * New York Cookie, Focaccia, Cinnabon (Artisan Tarçınlı Rulo) video ve Reels/TikTok kurguları.
4. **Satış & Büyüme Stratejisi:**
   * Komisyon kurtarma planı, akıllı dönemsel indirimler, sepet büyütme (AOV) combo'ları.
   * Gıda maliyeti (Food Cost) optimizasyonu: CNR Gıda ve Manav yerine Ankara GİMAT & Hal toptancı rehberi.
5. **12 Aylık Finansal Tahminleme & Mevsimsel Risk Analizi:**
   * Ankara okul takvimi, ara tatiller, Ramazan ve yaz rehavetine göre 3 senaryolu (Gerçekçi, İyimser, Kriz) kâr projeksiyonu.
6. **Maaşlar & Dinamik Net Kâr Simülatörü:**
   * Personel ekleme/çıkarma, net maaş, SGK/stopaj ve yemek desteğiyle anlık net kâr simülasyonu.
7. **Sosyal Medya Denetimi & LinkedIn B2B Lead Motoru:**
   * YouTube (@HeritageCafeBakery), TikTok (@heritage.cafe.bake) ve Instagram (@heritagecafeandbakery) denetimi.
   * İnteraktif checklist, canlı sağlık skoru, kalıcı yorum/not kaydetme ve otomatik "Eksiklik Raporu (Gap Analysis)" motoru.
   * LinkedIn kurumsal toplantı ve coffee-break kutuları için "Yorum & Lead Döngüsü" B2B satış sistemi.
8. **Güvenli Yönetici Girişi (Login):**
   * Luxury dark glassmorphism arayüz, Beni Hatırla desteği ve demo tek tıkla doldurma.

---

## 🔑 Yönetici Giriş Bilgileri
* **Kullanıcı Adı:** `heritage` | **Şifre:** `heritage2026`
* **Admin:** `admin` | **Şifre:** `admin2026`

---

## 💻 Çalıştırma ve Yayınlama

### 1. Yerel Çalıştırma (Local Server)
```bash
python run_portal.py
# veya Windows'ta çift tıklayın:
HERITAGE_PORTAL_BASLAT.bat
```
Tarayıcınızda açın: **http://localhost:8080**

### 2. Streamlit Cloud Üzerinde Yayınlama
* **Main file path:** `streamlit_app.py`
* **Gerekli dosyalar:** `streamlit_app.py`, `index.html`, `portal_data.js`, `requirements.txt`
```bash
streamlit run streamlit_app.py
```

---

## 🛠️ Teknolojiler
* **Frontend:** Tailwind CSS, Chart.js, Lucide Icons, Vanilla ES6+
* **Backend / Runner:** Python 3 (HTTP Server / Streamlit), openpyxl, pandas
* **Veri:** `portal_data.json` / `portal_data.js` (Heritage_Cafe_Muhasebe.xlsx kaynağından derlenmiş)

---

## 🏛️ Proje Künyesi & Telif Hakkı

> **Conceived & Directed by Sireen Khemesh**  
> *© 2026 ZEUS Bioscience. All rights reserved*

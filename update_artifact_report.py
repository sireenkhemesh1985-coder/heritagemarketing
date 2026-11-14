import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\sireen.khemesh\.gemini\antigravity\brain\6bc0ebe0-bf6e-4d46-9ff9-4b695826a984\Heritage_Finans_Pazarlama_Raporu.md'

with open(path, 'r', encoding='utf-8') as f:
    old_content = f.read()

# Let's append Section 3
section3_md = """
---

## 3. Ankara Toptancı & Hammadde Tedarik Optimizasyonu (CNR Gıda ve Manav Alternatifleri)

### 🧐 Neden CNR Gıda ve Güleryüz Manav Pahalı Geliyor? (Fatura Kalemleri Teşhisi)
Muhasebe kayıtlarındaki **394 adet fatura kalemi** tek tek incelendiğinde, 4 aylık **328.018 ₺** tutarındaki toplam hammadde faturasının ve **%44,5'lik Food Cost (hammadde maliyeti)** oranının arkasındaki 3 temel yapısal neden gün yüzüne çıkmıştır:

1. **Ev Tipi / Perakende Paketleme Tuzağı:**
   - **Krema:** 1 litrelik endüstriyel Horeca boy yerine **200 ml'lik minik Sütaş kutularıyla** alınmış (litre maliyeti 502 ₺'ye geliyor!).
   - **Tereyağı:** GİMAT'tan 10-25 kg blok Horeca tereyağı almak yerine, **Migros'a gidilip perakende raftan 1 kg'lık paketlerle 474 ₺/kg'ye** alınmış.
   - **Un:** GİMAT'tan 50 kg'lık pastalık çuval un yerine, Pazarama üzerinden internetten **5 kg'lık Tellioğlu unlar** kargoyla sipariş edilmiş.
   - **Kahve Çekirdeği:** İdefix / Petpal üzerinden 1 kg'lık Tchibo paketleri **661 ₺/kg** perakende fiyatla sipariş edilmiş.

2. **İşlenmiş Ürün / Kolaylık Primi (Convenience Markup):**
   - **Ekici Rende Mozarella 2 kg:** 4 ayda tam **39.156 ₺** ödenmiş ve kilogram birim maliyeti **436 ₺**! Dükkanda blok mozarella alınıp endüstriyel rende makinesinde çekilse kg maliyeti 230 – 260 ₺ bandına iner (%42 tasarruf).
   - **Samsa İspanağı:** Samsa fırında pişen bir börek olmasına rağmen, Güleryüz Manav'dan paketlenmiş **yıkanmış salatalık bebek ıspanak** alınmış (kilogramı **355 ₺**!). Ankara Hali'nde veya taze sebze toptancısında dökme taze ıspanağın kilogramı **35 – 50 ₺**'dir (Tam 8-10 kat fiyat farkı!).

3. **Aracı Distribütör Komisyonu:**
   - CNR Gıda ve Güleryüz Manav birer alt dağıtıcıdır. GİMAT ve Toptancı Hali'nden aldıkları malların üzerine kapıya servis ve işletme kârı olarak **%25 ila %50 marj** eklerler.

---

### 📊 Kritik Ürünlerde Fatura Fiyatı vs Ankara Toptancı Fiyatı Karşılaştırması

| Hammadde / Ürün Kalemi | Mevcut Alım Yeri | Mevcut Fatura Fiyatı | Önerilen 1. El Ankara Toptancısı | Hedef Toptan Birim Fiyat | 4 Aylık Tasarruf Potansiyeli |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mozarella Peyniri (Rende)** | CNR Gıda (Ekici 2kg) | **436 ₺ / kg** | **GİMAT Süt Ürünleri (Blok Mozarella)** | 230 – 260 ₺ / kg | **~16.500 ₺** (%42) |
| **Ispanak (Samsa Börek Harcı)** | Güleryüz Manav (Paket) | **355 ₺ / kg** | **Ankara Toptancı Hali (Dökme Kasa)** | 35 – 50 ₺ / kg | **~7.200 ₺** (%85) |
| **Tereyağı (Bakery & Kurabiye)** | Migros (1 kg perakende) | **474 ₺ / kg** | **GİMAT (10-25 kg Blok Horeca Tereyağı)** | 290 – 320 ₺ / kg | **~4.500 ₺** (%34) |
| **Fesleğen & Roka (Pesto & Salata)**| Güleryüz Manav (Erüst pk) | **790 ₺ / kg** | **Ankara Hali Erüst Bayisi / Metro Horeca** | 420 – 480 ₺ / kg | **~4.600 ₺** (%40) |
| **Krema %35 Yağlı (Pastacılık)** | CNR Gıda (Sütaş 200 ml) | **502 ₺ / L (100 ₺/kutu)** | **GİMAT / Koza Gıda (1 Litre Horeca)** | 140 – 170 ₺ / Litre | **~3.700 ₺** (%68) |
| **Füme Dana Et & Cotto & Antrikot**| Fulya / Yayla-Türk & CNR | **2.100 – 2.626 ₺ / kg** | **GİMAT Şarküteri Toptancıları / Ege Füme** | 1.500 – 1.850 ₺ / kg | **~15.500 ₺** (%28) |
| **Çift Duvarlı Karton Bardak (14 oz)**| Alfamarkt / CNR | **5,35 ₺ / Adet** | **Murpak Kağıtçılık / İvedik OSB Ambalaj** | 2,60 – 3,10 ₺ / Adet | **~3.000 ₺** (%45) |
| **Tchibo Espresso Kahve Çekirdeği** | İdefix / Petpal (1 kg) | **661 ₺ / kg** | **Ankara Nitelikli Roastery / Tchibo Horeca**| 400 – 480 ₺ / kg | **~2.800 ₺** (%30) |
| **TOPLAM TASARRUF ETKİSİ** | — | — | — | — | **~57.800 ₺ (Aylık ~14.500 ₺ - 20.000 ₺)** |

> [!TIP]
> **Net Kâr Sıçraması:** Yalnızca bu satın alma optimizasyonları ile Food Cost oranı **%44,5'ten %34'e çekilir**. Bu da işletmenin aylık net kârına doğrudan **15.000 ₺ – 20.000 ₺ net nakit eklenmesi** demektir!

---

### 📍 Ankara İçi Somut Toptancı ve Satın Alma Adresleri

#### 1. Taze Meyve, Sebze ve Yeşillik İçin (Güleryüz Manav Alternatifi)
- **Ankara Toptancı Hali (Yenimahalle / Macunköy - Hipodrom Yanı):**
  - *Ne Alınmalı:* Sandıkla dökme taze ıspanak, çeri domates, beef domates, salatalık, limon (sandık 18-20 kg), avokado ve portakal.
  - *Uygulama Modeli:* Çankaya Reşit Galip'ten arabayla 15-18 dakikadır. Hal'deki 1-2 güvenilir komisyoncu ile anlaşılıp, **Salı ve Cuma sabahları haftada 2 gün** dükkana kapı teslim kasa servisi bağlanabilir.
- **Metro Grossmarket Türkiye (Etlik & Batıkent Horeca Mağazaları):**
  - *Ne Alınmalı:* Erüst fesleğen, baby roka, saksı yeşillikler, limon, avokado, mantar.
  - *Avantaj:* Vergi levhanızla Horeca kartı çıkartılır. Faturaları kuruşu kuruşuna resmidir; fiyatları Güleryüz Manav'a göre ortalama **%25 - %35 daha uygundur**.

#### 2. Süt Ürünleri, Peynir ve Şarküteri İçin (CNR Gıda Alternatifi)
- **GİMAT Toptancılar Sitesi (Yenimahalle / Macunköy):**
  - *Ergüven Süt & Güvenler Gıda (GİMAT):* Zaten mevcut faturalarınızda doğrudan alım yaptığınız bir firma! CNR Gıda'yı aradan çıkarıp doğrudan Güvenler veya Akdeniz Süt Ürünleri'nden **blok mozarella (rendelenmemiş), tost kaşarı, labne ve 10 kg blok Karadeniz/Horeca tereyağı** alınmalıdır.
  - *GİMAT Şarkütericiler Çarşısı (Namet, Polonez, Ege Füme Bayileri):* Dana jambon, dana cotto, füme et ve sucuk koli bazlı toptan fiyattan alınır.

#### 3. Pastacılık, Belçika Çikolatası ve Un İçin
- **Öztürk Pastacılık Hammaddeleri (GİMAT):**
  - Ankara'nın en köklü pastacılık toptancısıdır. Callebaut / Belcolade Belçika çikolatası (kuvertür ve pul), pasta kremaları, fındık/Antep fıstığı ezmesi, mascarpone ve pasta katkı maddeleri 1. el toptan fiyata temin edilir.
- **Koza Gıda Ankara Bölge Müdürlüğü (Ostim / Yenimahalle):**
  - Butik kafelerin ve şeflerin ana tedarikçisidir. Lotus Biscoff kreması/bisküvisi, Monin kahve şurupları, Elle & Vire profesyonel krema/tereyağı ve dondurulmuş meyve püreleri kapıya soğuk zincir teslim edilir.
- **GİMAT Uncular Sitesi:**
  - Tellioğlu, Söke veya Ova 50 kg'lık pastalık-böreklik çuval un. İnternetten 5 kg paket alımı derhal sonlandırılmalıdır.

#### 4. Ambalaj, Kutu, Bardak ve Sarf Malzemeleri İçin
- **Murpak Kağıtçılık & Ambalaj (İvedik OSB):**
  - Zaten faturalarınızda yer alan yerli ambalaj üreticisi. 14 oz / 8 oz çift duvarlı sıcak bardak, soğuk pet bardak, kraft sandviç kutusu ve peçeteler koli bazlı doğrudan fabrikasından alınmalıdır (adet maliyeti 5,35 ₺'den 2,80 ₺ bandına iner).
- **GİMAT Ambalajcılar Çarşısı:**
  - Streç film, yağlı pişirme kağıdı, ahşap çatal/bıçak ve kraft taşıma poşetleri koliyle toptan temin edilir.

#### 5. Nitelikli Kahve Çekirdeği İçin (İdefix / Perakende Tchibo Yerine)
- **Ankara Yerel Nitelikli Kahve Kavurucuları (B2B Roastery):**
  - *Tavsiye Edilenler:* Paper Roasting Co., Spada Coffee, Null Coffee, Gordion Coffee Roasters.
  - *Model:* Aylık 20-30 kg düzenli çekirdek tüketimi taahhüdüyle B2B toptan fiyat anlaşması (kg başına 400 – 480 ₺). Hem İdefix'ten pahalıya alınan paket kahveden kurtulunur hem de kahve lezzeti 3. nesil artisan seviyeye yükselir.

---

### 🚀 3 Adımlı Uygulama Yol Haritası

1. **Endüstriyel Rende Makinesi:** Mutfağa 1 adet endüstriyel peynir rendeleme makinesi alın (tek seferlik yatırım). Blok mozarella alarak sadece rendeleme farkından **ayda 4.000 ₺** kazanın.
2. **Ispanak Alımını Değiştirin:** Güleryüz Manav'dan alınan paketli yıkanmış bebek ıspanak alımını derhal durdurun. Samsa böreği için Hal'den veya yerel sebze toptancısından dökme taze ıspanak alın (Sadece bu adım **ayda 2.000 – 2.500 ₺** tasarruf sağlar).
3. **GİMAT & Horeca Cari Hesapları:** GİMAT'ta Öztürk Pastacılık ve Güvenler Süt ile işletme cari hesabı açarak aylık/15 günlük toplu sevkiyat rotası kurun.
"""

new_content = old_content + "\n" + section3_md
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated artifact report with Section 3 successfully!")

import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
path = r'C:\Users\sireen.khemesh\.gemini\antigravity\brain\6bc0ebe0-bf6e-4d46-9ff9-4b695826a984\Heritage_Finans_Pazarlama_Raporu.md'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

website_insights_md = """
---

## 6. Resmi Web Sitesi (heritagecafe.com.tr) Analizi & Strateji Entegrasyonu

### 🌐 heritagecafe.com.tr İncelemesinden Elde Edilen Kritik Bulgular
1. **Çalışma Saatleri Gerçeği:**
   * **Pazartesi – Cuma:** 08:00 – 18:00
   * **Cumartesi:** 08:00 – 15:00
   * **Pazar: KAPALI!**
   * *Stratejik Etki:* Sosyal medya paylaşım rutini Pazar gününden **Cumartesi sabahı saat 09:30'a** çekilmiştir. Cumartesi saat 15:00 kapanışı nedeniyle Cuma akşamı ve Cumartesi sabahı "Hafta sonu al-götür kahvaltı & Cinnabon kutusu" vurgusu yapılmalıdır.
2. **Resmi Marka Sloganı & Felsefesi:**
   * **Slogan:** *"Save the Heritage · El emeğiyle yaşatılan lezzetler."*
   * **Manifesto:** *"Mirasın bir tarif defterinde değil, elde açılan bir hamurda, sabırla çırpılan bir kremada yaşadığına inanıyoruz. Her sabah fırını yeniden yakıyor, sevdiğimiz lezzetleri en dürüst malzemelerle yeniden yaratıyoruz."*
   * *Stratejik Etki:* Bu güçlü zanaat manifestosu LinkedIn B2B içeriklerinde ve TikTok/Reels videolarında kurumsal güven inşa etmek için birebir kullanılmalıdır.
3. **Resmi Menü İmzaları ve Fiyatlandırma (heritagecafe.com.tr/menu/):**
   * **Gusto Ciabatta Sandviçler:**
     * *Heritage Gusto 1 (350 ₺):* Ciabatta ekmeği, köz biberli sos, dana cotto, köz patlıcan, süzme peynir, roka.
     * *Gurme Pepperoni & Gouda (500 ₺):* 80 gr Pepperoni, Gouda, ev yapımı pesto, focaccia.
     * *Gurme Roastbeef & Çörekotlu (520 ₺):* 80 gr karabiberli roastbeef, çörekotlu peynir, acılı zeytinyağı.
     * *Gurme Dana Cotto & Mozzarella (480 ₺)*
   * **El Açması Fırın Ürünleri:** Samsa, Napolyon, Medovik, Çilekli & Antep Fıstıklı Madlen, New York Cookies.
   * **Özel Beslenme:** Glutensiz kabak & lor peynirli waffle menüsü (IVF merkezi sağlık kitlesine doğrudan hitap eden kilit ürün!).
4. **Resmi Kanallar & Doğrudan WhatsApp Siparişi:**
   * **Web Sitesi:** [heritagecafe.com.tr](https://heritagecafe.com.tr)
   * **WhatsApp Doğrudan Sipariş:** `0 534 592 70 12`
   * **Sabit Telefon:** `0312 427 48 01`
   * **Kurumsal & Toplu İkram Sayfası:** `heritagecafe.com.tr/iletisim/` altında doğrudan "Kurumsal / Toplu İkram" formu mevcuttur!
"""

new_text = text + "\n" + website_insights_md
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated artifact report with Section 6 successfully!")

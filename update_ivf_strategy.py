# -*- coding: utf-8 -*-
"""
Replaces Strateji 6 in build_portal.py with tailored IVF (In Vitro Fertilization / Tüp Bebek) Clinic strategies.
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    text = f.read()

idx_start = text.find('<!-- Strateji 6: Hastane İçi Kafe')
idx_end = text.find('<!-- Strateji 7: Trendyol Go vs Yemeksepeti')

if idx_start == -1 or idx_end == -1:
    print(f"Error finding markers: start={idx_start}, end={idx_end}")
    exit(1)

new_ivf_html = """<!-- Strateji 6: IVF (Tüp Bebek) Merkezi İçi Kafe Özel Büyüme Stratejisi -->
      <div class="glass-card rounded-2xl p-6 border border-pink-500/30 bg-gradient-to-r from-slate-900 via-pink-950/20 to-slate-900 space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-pink-500/20 border border-pink-500/30 flex items-center justify-center">
              <i data-lucide="heart-pulse" class="w-5 h-5 text-pink-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">IVF (Tüp Bebek) Merkezi Kafe Stratejisi (Çiftler, Bekleme Süreleri & 18:00 Kapanış)</h3>
              <p class="text-xs text-slate-400 mt-0.5">Yatan hasta olmayan, çiftlerin uzun süre beklediği ve hassas beslendiği merkeze özel 4 gelir motoru</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-pink-500/10 text-pink-400 font-bold border border-pink-500/20 self-start sm:self-auto">IVF Konsepti</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <!-- 1. Kafeinsiz (Decaf) Kahve -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-pink-500/40 transition">
            <div class="flex items-center gap-1.5 text-pink-400 font-bold text-sm">
              <i data-lucide="coffee" class="w-4 h-4"></i>
              1. Kafeinsiz (Decaf) Kahve (1 Numaralı Fırsat!)
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Kitle:</strong> Tedavi ve transfer sürecindeki anne adayları.<br>
              <strong>Fırsat:</strong> Doktorlar kafeini yasaklar veya günde 1 fincanla sınırlar. Kadınlar kahve içmek ister ama içemez!<br>
              <strong class="text-pink-300">Aksiyon:</strong> Menüye <em>"Doğal Swiss Water Yöntemiyle Kafeinsizleştirilmiş Decaf Americano & Decaf Latte"</em> ekleyin. Merkezdeki kadın hastaların tartışmasız 1 numaralı tercihi olur.
            </p>
          </div>

          <!-- 2. İki Kişilik Çift Menüleri -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-pink-500/40 transition">
            <div class="flex items-center gap-1.5 text-amber-400 font-bold text-sm">
              <i data-lucide="users" class="w-4 h-4"></i>
              2. İki Kişilik Çift Menüleri (Uzun Bekleme & Moral)
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Kitle:</strong> Tahlil ve randevu aralarında 1-2 saat salonda birlikte bekleyen çiftler.<br>
              <strong>Fırsat:</strong> Stresli ve duygusal bir bekleme sürecidir; baş başa kahvaltı ve sıcak içecek tüketirler.<br>
              <strong class="text-amber-300">Aksiyon:</strong> "İki Kişilik Çift Kahvaltısı (2 Tost + 2 İçecek)" veya "Moral Molası (Paylaşımlı Tiramisu / Cookie + 2 İçecek)" paketleri sunun.
            </p>
          </div>

          <!-- 3. Tahlil ve OPU Sonrası Hafif Kahvaltı -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-pink-500/40 transition">
            <div class="flex items-center gap-1.5 text-emerald-400 font-bold text-sm">
              <i data-lucide="sparkles" class="w-4 h-4"></i>
              3. Tahlil & İşlem Sonrası "Mide Dostu" Kahvaltı
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Kitle:</strong> Sabah 08:00 – 10:30 arası aç karnına kan veren veya işlemden çıkan hastalar.<br>
              <strong>Fırsat:</strong> Mideyi bulandırmayan, gaz yapmayan, sindirimi çok kolay besinler aranır.<br>
              <strong class="text-emerald-300">Aksiyon:</strong> Ekşi mayalı sıcak focaccia kaşarlı tost, ceviz, taze ıspanaklı Samsa ve rahatlatıcı taze ıhlamur/nane çayı kombinasyonu.
            </p>
          </div>

          <!-- 4. Glutensiz & Antioksidan Clean Eating -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-pink-500/40 transition">
            <div class="flex items-center gap-1.5 text-blue-400 font-bold text-sm">
              <i data-lucide="apple" class="w-4 h-4"></i>
              4. Glutensiz & Antioksidan "Clean Eating" Menüsü
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Kitle:</strong> IVF sürecinde Akdeniz tipi / glutensiz beslenen bilinçli kitle.<br>
              <strong>Fırsat:</strong> Menünüzdeki <strong>Glutensiz Bagel'ın 135 adet satması</strong> bu kitlenin kanıtıdır!<br>
              <strong class="text-blue-300">Aksiyon:</strong> Avokadolu sandviç (Heritage Gusto 2), cevizli kek ve yeşil detox içeceğini menüde <em>"IVF & Doğal Beslenme Dostu"</em> simgeleriyle öne çıkarın.
            </p>
          </div>
        </div>
      </div>
"""

updated_text = text[:idx_start] + new_ivf_html + "\n      " + text[idx_end:]

with open("build_portal.py", "w", encoding="utf-8") as f:
    f.write(updated_text)

print("Updated build_portal.py with IVF specific strategies successfully!")

# -*- coding: utf-8 -*-
"""
Adds Section 5: Detailed Advertising Budget by Platform into Tab 3 (Pazarlama & Menü Analitiği) in build_portal.py
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    content = f.read()

# Find the end of tab-marketing
idx_marketing = content.find('id="tab-marketing"')
if idx_marketing == -1:
    print("Could not find tab-marketing")
    exit(1)

idx_close = content.find('</section>', idx_marketing)
if idx_close == -1:
    print("Could not find </section> of tab-marketing")
    exit(1)

ad_budget_html = """
      <!-- Section 5: Platform Bazlı Detaylı Reklam Bütçesi & Dağılım Rehberi -->
      <div class="glass-card rounded-2xl p-6 border border-emerald-500/30 bg-gradient-to-b from-slate-900 via-slate-900 to-emerald-950/20 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center">
              <i data-lucide="coins" class="w-5 h-5 text-emerald-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Platform Bazlı Detaylı Reklam Bütçesi & Harcama Kılavuzu</h3>
              <p class="text-xs text-slate-400 mt-0.5">Aylık ~184.000 ₺ net cironun %6,5'i (12.000 ₺) ile maksimum müşteri ve ROAS üretecek dağılım</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/20 self-start sm:self-auto">Bütçe Matrisi</span>
        </div>

        <!-- 3 Tier Budget Overview -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400">1. Başlangıç / Test Planı</span>
              <span class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded font-bold">Minimum</span>
            </div>
            <div class="text-xl font-black text-white">7.500 ₺ <span class="text-xs text-slate-400 font-normal">/ ay (250 ₺ / gün)</span></div>
            <p class="text-[11px] text-slate-400 leading-relaxed">
              Sadece Instagram Reels ve Google Haritalar. Yeni menü lezzetlerini Çankaya'ya duyurmak için giriş seviyesi.
            </p>
          </div>

          <div class="p-4 rounded-xl bg-emerald-950/30 border-2 border-emerald-500/50 space-y-1.5 relative overflow-hidden">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-400">2. İdeal Büyüme Planı (ÖNERİLEN)</span>
              <span class="text-[11px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded font-extrabold">En Çok Tavsiye Edilen</span>
            </div>
            <div class="text-2xl font-black text-emerald-400">12.000 ₺ <span class="text-xs text-emerald-300/80 font-normal">/ ay (400 ₺ / gün)</span></div>
            <p class="text-[11px] text-slate-300 leading-relaxed">
              Instagram (%50) + Google Maps (%21) + TikTok (%17) + Trendyol İçi (%12). Hem salona çift çeker hem paket satışı katlar.
            </p>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400">3. Agresif Bölge Lideri Planı</span>
              <span class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded font-bold">Maksimum</span>
            </div>
            <div class="text-xl font-black text-white">18.000 ₺ <span class="text-xs text-slate-400 font-normal">/ ay (600 ₺ / gün)</span></div>
            <p class="text-[11px] text-slate-400 leading-relaxed">
              Tüm Çankaya, GOP, Tunalı ve Ayrancı bölgesinde artisan fırın & kahve pazarında mutlak bilinirlik ve yüksek Trendyol hacmi.
            </p>
          </div>
        </div>

        <!-- Detailed Platform Breakdown Cards (Based on 12.000 TL Recommended Budget) -->
        <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider pt-2 flex items-center gap-2">
          <i data-lucide="pie-chart" class="w-4 h-4 text-amber-400"></i>
          Önerilen 12.000 ₺ / Ay Bütçenin Platform Bazında Ayrıntılı Dökümü
        </h4>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          
          <!-- Platform 1: Instagram (Meta Ads) -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-pink-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-pink-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="instagram" class="w-4 h-4"></i>
                1. Instagram (Meta)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-pink-500/20 text-pink-300 font-bold">%50 Pay</span>
            </div>
            <div class="space-y-1">
              <div class="text-lg font-black text-white">6.000 ₺ / Ay</div>
              <span class="text-[11px] text-slate-400">Günlük 200 ₺ (2 Ayrı Kampanya)</span>
            </div>
            <div class="space-y-2 text-slate-300 pt-1 leading-relaxed">
              <p>• <strong>Reels Trafik & Video İzleme (130 ₺/gün):</strong> Çikolata şelalesi, New York Cookie akışı ve Pesto Focaccia tost videoları (Profil Ziyareti hedefi).</p>
              <p>• <strong>Yerel Story & Yol Tarifi (70 ₺/gün):</strong> Çankaya + 3 km yarıçaptaki 24-45 yaş hedef kitleye "Yol Tarifi Al / Konumu Aç" çağrılı Story reklamları.</p>
              <p class="text-[11px] text-emerald-400 font-semibold pt-1">Beklenen Sonuç: 90.000+ gösterim, 1.400+ profil ziyareti, ~1,40 ₺ tıklama maliyeti (CPC).</p>
            </div>
          </div>

          <!-- Platform 2: Google Ads & Haritalar -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-blue-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-blue-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="map-pin" class="w-4 h-4"></i>
                2. Google Haritalar
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-blue-500/20 text-blue-300 font-bold">%21 Pay</span>
            </div>
            <div class="space-y-1">
              <div class="text-lg font-black text-white">2.500 ₺ / Ay</div>
              <span class="text-[11px] text-slate-400">Günlük ~83 ₺ (Yerel Arama)</span>
            </div>
            <div class="space-y-2 text-slate-300 pt-1 leading-relaxed">
              <p>• <strong>Google Maps Promoted Pins:</strong> Çankaya'da haritayı açan veya "yakınımdaki kafe", "Çankaya kahvaltı", "Reşit Galip fırın" arayanların haritasında mor/kare kare parlayan iğne.</p>
              <p>• <strong>Önem:</strong> IVF merkezine gelen hastalar, tahlil sonrası Google'a "yakında kahvaltı nerede yapılır" diye arattığında 1. sırada çıkarsınız.</p>
              <p class="text-[11px] text-emerald-400 font-semibold pt-1">Beklenen Sonuç: Ayda 350+ doğrudan harita yol tarifi ve telefon araması (En yüksek dönüşüm!).</p>
            </div>
          </div>

          <!-- Platform 3: TikTok Ads -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-purple-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="music" class="w-4 h-4"></i>
                3. TikTok Ads
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-purple-500/20 text-purple-300 font-bold">%17 Pay</span>
            </div>
            <div class="space-y-1">
              <div class="text-lg font-black text-white">2.000 ₺ / Ay</div>
              <span class="text-[11px] text-slate-400">Günlük ~67 ₺ (In-Feed Video)</span>
            </div>
            <div class="space-y-2 text-slate-300 pt-1 leading-relaxed">
              <p>• <strong>ASMR & Foodporn Kurguları:</strong> 60 ₺'lik çıtır Samsa ısırığı, uzayan peynirli tost ve New York cookie kırılma anı (10-12 saniyelik videolar).</p>
              <p>• <strong>Önem:</strong> Ankara genelinde TikTok'ta bin gösterim maliyeti (CPM) sadece 15 – 22 ₺'dir (Instagram'dan 3 kat daha ucuz kitle erişimi!).</p>
              <p class="text-[11px] text-emerald-400 font-semibold pt-1">Beklenen Sonuç: 75.000+ tam video izlenmesi, viral marka bilinirliği.</p>
            </div>
          </div>

          <!-- Platform 4: Trendyol Go & Yemeksepeti -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-orange-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-orange-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="shopping-bag" class="w-4 h-4"></i>
                4. Trendyol İçi Reklam
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-orange-500/20 text-orange-300 font-bold">%12 Pay</span>
            </div>
            <div class="space-y-1">
              <div class="text-lg font-black text-white">1.500 ₺ / Ay</div>
              <span class="text-[11px] text-slate-400">Günlük 50 ₺ (Öğle Saatleri)</span>
            </div>
            <div class="space-y-2 text-slate-300 pt-1 leading-relaxed">
              <p>• <strong>Arama & Kategori Sponsorluğu:</strong> Hafta içi saat 11:30 – 14:00 arasında Trendyol Go uygulamasında "Tost & Sandviç" ve "Tatlı" kategorisinde en üst sırada görünme.</p>
              <p>• <strong>Kurgu:</strong> Dışarıdaki ofis çalışanları tam acıktığı anda 1. sırada Heritage'ı görür.</p>
              <p class="text-[11px] text-emerald-400 font-semibold pt-1">Beklenen Sonuç: Ayda +40 - 50 ekstra online sipariş (~25.000 ₺ ek ciro!).</p>
            </div>
          </div>

        </div>

        <!-- ROAS & Targeting Specs Summary -->
        <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800 space-y-3 text-xs">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <span class="font-bold text-amber-400 flex items-center gap-2">
              <i data-lucide="target" class="w-4 h-4"></i>
              Nokta Atışı Reklam Hedefleme Parametreleri (Meta & Google):
            </span>
            <span class="px-2.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-bold">Beklenen ROAS: 4,8x – 6,2x</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-slate-300">
            <div class="p-2.5 bg-slate-800/40 rounded-lg">
              <span class="text-slate-400 block font-semibold">📍 Coğrafi Konum:</span>
              Ankara / Çankaya (Reşit Galip Cd. merkezli 3 km yarıçap + Gaziosmanpaşa, Tunalı, Ayrancı, ODTÜ/Bilkent aksı).
            </div>
            <div class="p-2.5 bg-slate-800/40 rounded-lg">
              <span class="text-slate-400 block font-semibold">👥 Demografi & Yaş:</span>
              24 – 48 yaş arası kadın & erkek (Çiftler, sağlık çalışanları, elçilik personeli, kurumsal çalışanlar).
            </div>
            <div class="p-2.5 bg-slate-800/40 rounded-lg">
              <span class="text-slate-400 block font-semibold">🎯 İlgi Alanı Etiketleri:</span>
              Nitelikli Kahve, Artisan Fırın, Akdeniz Diyeti, Glutensiz Beslenme, Butik Pastane, Kadın Sağlığı & İyi Yaşam.
            </div>
          </div>
        </div>
      </div>
"""

updated_content = content[:idx_close] + ad_budget_html + "\n    " + content[idx_close:]

with open("build_portal.py", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Added Section 5: Detailed Ad Budget into build_portal.py successfully!")

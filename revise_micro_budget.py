# -*- coding: utf-8 -*-
"""
Revises Section 5 in build_portal.py to Lean Micro-Budgets (1.500 TL - 3.000 TL / month)
and adds Zero-Cost In-Clinic Growth tactics.
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    text = f.read()

idx_start = text.find('<!-- Section 5: Platform Bazlı Detaylı Reklam Bütçesi')
idx_end = text.find('</section>', idx_start)

if idx_start == -1 or idx_end == -1:
    print("Could not find markers for Section 5")
    exit(1)

new_micro_budget_html = """<!-- Section 5: Yalın & Düşük Riskli Mikro Reklam Bütçesi (Gözden Geçirilmiş Model) -->
      <div class="glass-card rounded-2xl p-6 border border-emerald-500/30 bg-gradient-to-b from-slate-900 via-slate-900 to-emerald-950/20 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center">
              <i data-lucide="piggy-bank" class="w-5 h-5 text-emerald-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Gözden Geçirilmiş Yalın & Düşük Riskli Mikro Reklam Bütçesi</h3>
              <p class="text-xs text-slate-400 mt-0.5">Kasanızı asla yormayacak, aylık sadece 1.500 ₺ – 3.000 ₺ (günlük 50-100 ₺) ile hedefe kilitlenen model</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/20 self-start sm:self-auto">Düşük Risk / Mikro Bütçe</span>
        </div>

        <!-- Finansal Gerçeklik Notu -->
        <div class="p-3.5 bg-amber-500/10 border border-amber-500/20 rounded-xl text-xs text-amber-300 leading-relaxed">
          <strong>Neden Bütçeyi Düşürdük?</strong> Maaşlar ödendikten sonra aylık net kârınız ~37.000 ₺ seviyesindedir. Ayrıca cironuzun <strong>%78'i zaten IVF merkezi içindeki hastalar ve personelden</strong> gelmektedir. Bu kitle zaten binanın içindedir; onlara reklam harcanmaz! Reklam sadece Çankaya çevresindeki dış müşteriler ve Trendyol için yapılmalıdır. Bu yüzden bütçeyi <strong>günde sadece 1 kahve parasına (50 – 100 ₺)</strong> indirdik.
        </div>

        <!-- 3 Tier Micro Budget Overview -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400">1. Ultra Düşük Test Modeli</span>
              <span class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded font-bold">Günde 1 Kahve Parası</span>
            </div>
            <div class="text-xl font-black text-white">1.500 ₺ <span class="text-xs text-slate-400 font-normal">/ ay (50 ₺ / gün)</span></div>
            <p class="text-[11px] text-slate-400 leading-relaxed">
              Haftada sadece 3 gün (Cuma, Cumartesi, Pazar) Instagram'da en çok izlenen 1 videoyu Reşit Galip çevresine öne çıkarma.
            </p>
          </div>

          <div class="p-4 rounded-xl bg-emerald-950/30 border-2 border-emerald-500/50 space-y-1.5 relative overflow-hidden">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-400">2. İdeal Mikro Bütçe (EN TAVSİYE EDİLEN)</span>
              <span class="text-[11px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded font-extrabold">Önerilen</span>
            </div>
            <div class="text-2xl font-black text-emerald-400">3.000 ₺ <span class="text-xs text-emerald-300/80 font-normal">/ ay (100 ₺ / gün)</span></div>
            <p class="text-[11px] text-slate-300 leading-relaxed">
              Instagram Reels (60 ₺/gün) + Google Haritalar (40 ₺/gün). Aylık net kârınızın sadece %8'i. Tamamen risksiz ve verimli.
            </p>
          </div>

          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400">3. Genişletilmiş Bütçe</span>
              <span class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded font-bold">Maksimum Tavan</span>
            </div>
            <div class="text-xl font-black text-white">5.000 ₺ <span class="text-xs text-slate-400 font-normal">/ ay (~165 ₺ / gün)</span></div>
            <p class="text-[11px] text-slate-400 leading-relaxed">
              İşler büyüdükçe ve kâr arttıkça Trendyol ve TikTok'a küçük bütçeler eklenerek çıkılacak tavan nokta.
            </p>
          </div>
        </div>

        <!-- Önerilen 3.000 TL Bütçenin Akıllı Dağılımı -->
        <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider pt-2 flex items-center gap-2">
          <i data-lucide="layers" class="w-4 h-4 text-emerald-400"></i>
          Önerilen 3.000 ₺ / Ay Mikro Bütçenin Akıllı Dağılımı (Sadece 2 Kanala Odak)
        </h4>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          
          <!-- Kanal 1: Instagram Reels Boost -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-2.5 hover:border-pink-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-pink-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="instagram" class="w-4 h-4"></i>
                1. Instagram Reels Öne Çıkarma
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-pink-500/20 text-pink-300 font-bold">1.800 ₺ / Ay (60 ₺ / Gün)</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p>• <strong>Nasıl Uygulanır?</strong> Sıfırdan karmaşık reklam panelleriyle uğraşmayın. Telefonunuzdan çektiğiniz en iştah kabartan 2 videonun (New York Cookie kırılma anı ve Pesto Soslu Tost) altına girip <strong>"Gönderiyi Öne Çıkar"</strong> deyin.</p>
              <p>• <strong>Hedef:</strong> Çankaya + 2 km yarıçap, 24-45 yaş. Günde sadece 60 ₺ ile haftada 4 gün yayınlayın.</p>
              <p class="text-[11px] text-emerald-400 font-semibold">Beklenen Etki: Ayda 35.000+ yerel gösterim, 500+ yeni yerel takipçi ve profil ziyareti.</p>
            </div>
          </div>

          <!-- Kanal 2: Google Haritalar -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-2.5 hover:border-blue-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-blue-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="map-pin" class="w-4 h-4"></i>
                2. Google Haritalar Yerel Arama
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-blue-500/20 text-blue-300 font-bold">1.200 ₺ / Ay (40 ₺ / Gün)</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p>• <strong>Nasıl Uygulanır?</strong> Google Haritalar'da Akıllı Yerel Kampanya (Smart Campaign) açın. Bütçeyi günde 40 ₺ ile sınırlandırın.</p>
              <p>• <strong>Önem:</strong> Biri Reşit Galip'te "kafe", "kahvaltı", "tost" yazdığında haritada en üstte çıkarsınız. Sadece haritayı tıklayan olursa para kesilir, tıklanmazsa para kasada kalır.</p>
              <p class="text-[11px] text-emerald-400 font-semibold">Beklenen Etki: Ayda 180+ doğrudan dükkana yol tarifi alma (En temiz dönüşüm!).</p>
            </div>
          </div>

        </div>

        <!-- SIFIR MALİYETLİ (0 TL) HASTANE İÇİ GERİLLA PAZARLAMA MOTORU -->
        <div class="p-5 rounded-xl bg-slate-900/90 border border-amber-500/30 space-y-3 text-xs">
          <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="font-bold text-amber-400 flex items-center gap-2 text-sm">
              <i data-lucide="sparkles" class="w-4 h-4"></i>
              Asıl Ciro Motoru: SIFIR MALİYETLİ (0 ₺) Hastane İçi Büyüme Taktikleri
            </span>
            <span class="px-2.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold">Maliyetsiz Ciro</span>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-slate-300">
            <div class="p-3 bg-slate-800/40 rounded-lg space-y-1">
              <span class="font-bold text-white block">1. Tahlil Çıkışı Ağızdan Pazarlama:</span>
              Kan alma odasındaki hemşire/personelle iyi iletişim kurularak, kan veren hastalara: <em>"Geçmiş olsun, alt kattaki fırında sıcacık tost ve ıhlamur var, kan şekeriniz düşmeden bir şeyler atıştırın"</em> yönlendirmesi. (Maliyet: 0 ₺, Etki: Anında sabah cirosu).
            </div>
            <div class="p-3 bg-slate-800/40 rounded-lg space-y-1">
              <span class="font-bold text-white block">2. Bekleme Salonuna Şık Pleksi Menü:</span>
              Çiftlerin oturduğu bekleme koltuklarının yanındaki sehpalara şık ahşap/pleksi içinde QR kodlu menü ve <em>"İki Kişilik Çift Kahvaltısı & Decaf Kahve"</em> görseli koymak. (Maliyet: Tek seferlik 150 ₺ baskı).
            </div>
            <div class="p-3 bg-slate-800/40 rounded-lg space-y-1">
              <span class="font-bold text-white block">3. Saatli Koku Pazarlaması (Scent):</span>
              Saat 10:00 ve 14:00'te fırında kurabiye ve vanilyalı ürünler pişirerek havalandırmadan salona taze fırın kokusu yaymak. Aç olan çiftleri doğrudan kokuyla kafeye çekmek. (Maliyet: 0 ₺).
            </div>
          </div>
        </div>

      </div>
"""

updated_text = text[:idx_start] + new_micro_budget_html + "\n    " + text[idx_end:]

with open("build_portal.py", "w", encoding="utf-8") as f:
    f.write(updated_text)

print("Updated build_portal.py with Lean Micro-Budget framework successfully!")

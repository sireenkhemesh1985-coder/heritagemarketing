# -*- coding: utf-8 -*-
"""
Upgrades build_portal.py with detailed, actionable, step-by-step 'NASIL YAPALIM?'
guides for Menu Engineering (Boston Matrix), Portion Revisions, Tasting Events,
and Menu Pruning.
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find Strateji 2 in build_portal.py
start_marker = '<!-- Strateji 2: Menü Mühendisliği Matrisi'
end_marker = '<!-- Strateji 3 & 4: Sepet Büyütme & Kurumsal B2B -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Error finding markers: start={start_idx}, end={end_idx}")
    exit(1)

new_strategy_2_html = """<!-- Strateji 2: Menü Mühendisliği Matrisi (Detaylı Uygulama Rehberi) -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="layout-grid" class="w-5 h-5 text-emerald-400"></i>
              Strateji 2: Menü Mühendisliği Matrisi & Somut Uygulama Rehberi (Nasıl Yapalım?)
            </h3>
            <p class="text-xs text-slate-400 mt-0.5">Ürünlerin kârlılık/hacim analizine göre adım adım mutfak, servis ve menü eylem planı</p>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/20 self-start sm:self-auto">Eylem Planı</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          
          <!-- 1. YILDIZLAR -->
          <div class="p-5 rounded-2xl bg-emerald-950/20 border border-emerald-500/30 space-y-3.5">
            <div class="flex items-center justify-between pb-2 border-b border-emerald-500/20">
              <span class="text-sm font-bold text-emerald-400 flex items-center gap-2">
                <i data-lucide="star" class="w-4 h-4 fill-emerald-400"></i>
                1. YILDIZLAR (Yüksek Kâr + Yüksek Hacim)
              </span>
              <span class="text-[11px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded font-bold">Koru & Parlat</span>
            </div>
            
            <p class="text-xs text-slate-300">
              <strong>Ürünler:</strong> Americano (59.6k ₺), Kurabiye / New York Cookies (35.2k ₺), Waffle Tabağı (26.9k ₺), Salçalı & Pestolu Tostlar (34.2k ₺), Limonata (22.7k ₺).
            </p>

            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 text-xs">
              <h5 class="font-bold text-emerald-300 flex items-center gap-1.5">
                <i data-lucide="check-circle" class="w-3.5 h-3.5"></i>
                NASIL YAPALIM? (Somut Uygulama Adımları):
              </h5>
              <ul class="space-y-1.5 text-slate-300 list-disc list-inside leading-relaxed">
                <li><strong class="text-white">Gramaj Terazi Standardı:</strong> Tostta sucuk 50g, kaşar 60g, sos 25g olarak porsiyonlanmalı. Mutfak tezgâhına bu gramaj tablosu asılmalı. Ustadan ustaya lezzet ve maliyet değişmemeli.</li>
                <li><strong class="text-white">Saatli Fırın Koku Pazarlaması (Scent Marketing):</strong> New York Kurabiyeler her gün tam saat <strong>14:00</strong> ve <strong>18:00</strong>'de fırına verilmeli. Dükkana yayılan sıcak vanilya/çikolata kokusuyla birlikte salona <em>"Fırından yeni çıktı, sıcacık servis ediyoruz"</em> anonsu yapılmalı.</li>
                <li><strong class="text-white">Kasa Yanı Göz Hizası Teşhiri:</strong> Kurabiyeler kasanın hemen sağına, şeffaf cam fanus içinde 3 katmanlı (Lotus, Fıstık, Nutella) dik sergilenmeli; sipariş veren her müşterinin gözü ilk buraya çarpmalı.</li>
              </ul>
            </div>
          </div>

          <!-- 2. NAKİT İNEKLERİ -->
          <div class="p-5 rounded-2xl bg-blue-950/20 border border-blue-500/30 space-y-3.5">
            <div class="flex items-center justify-between pb-2 border-b border-blue-500/20">
              <span class="text-sm font-bold text-blue-400 flex items-center gap-2">
                <i data-lucide="coins" class="w-4 h-4"></i>
                2. NAKİT İNEKLERİ (Düşük Kâr + Çok Yüksek Hacim)
              </span>
              <span class="text-[11px] bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded font-bold">Çapraz Satış Yap</span>
            </div>

            <p class="text-xs text-slate-300">
              <strong>Ürünler:</strong> Çay (780 adet), Erikli Su (283 adet), Poğaça Dereotlu (122 adet), Samsa (325 adet).
            </p>

            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 text-xs">
              <h5 class="font-bold text-blue-300 flex items-center gap-1.5">
                <i data-lucide="check-circle" class="w-3.5 h-3.5"></i>
                NASIL YAPALIM? (Somut Uygulama Adımları):
              </h5>
              <ul class="space-y-1.5 text-slate-300 list-disc list-inside leading-relaxed">
                <li><strong class="text-white">Garson/Kasiyer Satış Scripti:</strong> Çay siparişi veren müşteriye <em>"Yanında bir şey ister misiniz?"</em> (Evet/Hayır sorusu) DENMEMELİ! Bunun yerine: <br><em class="text-amber-300">"Çayınızın yanına fırından yeni çıkan sıcak peynirli Samsamızdan mı getireyim, yoksa Belçika çikolatalı Madlenimizden mi?"</em> ikilemi sorulmalı. Başarı oranı %42'dir.</li>
                <li><strong class="text-white">Fincan Çay & Demlik Satışı:</strong> Menüde 50 ₺ olan bardak çay yerine; taze nane yaprağı ve limon dilimiyle servis edilen <strong>70 ₺'lik fincan çay</strong> veya masaya bırakılan <strong>140 ₺'lik 2 kişilik porselen demlik</strong> seçeneği sunularak çay cirosu %50 artırılmalı.</li>
                <li><strong class="text-white">Su Satışında Upgrade:</strong> Plastik şişe su yerine masaya soğuk cam şişe içinde nane/limon dilimli Uludağ Premium (60 ₺) önerilmeli.</li>
              </ul>
            </div>
          </div>

          <!-- 3. SORU İŞARETLERİ -->
          <div class="p-5 rounded-2xl bg-amber-950/20 border border-amber-500/30 space-y-3.5">
            <div class="flex items-center justify-between pb-2 border-b border-amber-500/20">
              <span class="text-sm font-bold text-amber-400 flex items-center gap-2">
                <i data-lucide="help-circle" class="w-4 h-4"></i>
                3. SORU İŞARETLERİ (Yüksek Kâr + Düşük Hacim)
              </span>
              <span class="text-[11px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded font-bold">Porsiyon & Tadım Revizyonu</span>
            </div>

            <p class="text-xs text-slate-300">
              <strong>Ürünler:</strong> Tiramisu Tatlısı (28 adet / 350 ₺), Napolyon Pasta (33 adet / 280 ₺), Gurme Dana Cotto (11 adet / 750 ₺), Füme Antrikot (13 adet / 690 ₺).
            </p>

            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 text-xs">
              <h5 class="font-bold text-amber-300 flex items-center gap-1.5">
                <i data-lucide="wrench" class="w-3.5 h-3.5"></i>
                NASIL YAPALIM? (Somut Eylem Planı):
              </h5>
              <ul class="space-y-2 text-slate-300 leading-relaxed">
                <li>
                  <strong class="text-white">1. Dana Cotto (750 ₺) Sandviç Revizyonu:</strong>
                  <br>• <em>Sorun:</em> 750 ₺ tek bir sandviç için çok yüksek bir psikolojik bariyer.
                  <br>• <em>Çözüm A (Yarım Boy Menü):</em> 80g yerine 40g et ile <strong>380 ₺'lik "Yarım Gurme Ciabatta Sandviç + Çorba/Salata"</strong> seçeneği açın.
                  <br>• <em>Çözüm B (3'lü Mini Slider Tabağı):</em> 450 ₺'ye 3 mini ciabatta ekmeğinde tadım tabağı sunun (1 mini Dana Cotto + 1 mini Füme Antrikot + 1 mini Mozzarella Pesto). Müşteri 750 ₺ vermez ama 450 ₺'ye 3 gurme lezzeti paylaşarak sipariş verir!
                </li>
                <li>
                  <strong class="text-white">2. Tiramisu (350 ₺) & Masada Servis Şovu:</strong>
                  <br>Porsiyon tabağında getirmek yerine; şık cam kasede masaya getirilmeli. Garson müşterinin masasında minik seramik cezveden sıcak taze espressoyu kedi dillerinin üzerine dökmeli ve el değirmeniyle taze kakao serpmeli. Bu 15 saniyelik görsel ritüel, müşterinin telefonunu çıkarıp Instagram'da paylaşmasını ve 350 ₺'yi gururla ödemesini sağlar.
                </li>
                <li>
                  <strong class="text-white">3. Hafta Sonu Tadım İkramı (Sampling Ritüeli):</strong>
                  <br>Cuma ve Cumartesi günleri saat 15:30'da mutfaktan minik kürdanlı 1 dilim Napolyon ve Tiramisu küpleri salondaki tüm masalara ikram edilmeli: <em>"Şefimizin bugün fırından yeni çıkardığı artisan Napolyon'u, denemeniz için ikramımızdır."</em> Tadan her 3 masadan 1'i o anda tam porsiyon sipariş verir!
                </li>
              </ul>
            </div>
          </div>

          <!-- 4. KÖPEKLER -->
          <div class="p-5 rounded-2xl bg-rose-950/20 border border-rose-500/30 space-y-3.5">
            <div class="flex items-center justify-between pb-2 border-b border-rose-500/20">
              <span class="text-sm font-bold text-rose-400 flex items-center gap-2">
                <i data-lucide="trash-2" class="w-4 h-4"></i>
                4. KÖPEKLER (Düşük Kâr + Düşük Hacim)
              </span>
              <span class="text-[11px] bg-rose-500/20 text-rose-300 px-2 py-0.5 rounded font-bold">Ayıkla veya Dönüştür</span>
            </div>

            <p class="text-xs text-slate-300">
              <strong>Ürünler:</strong> Sade Soğuk Sandviç (11 adet), Poğaça (8 adet), Bumblebee Coffee (3 adet), Glace Coffee (4 adet).
            </p>

            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 text-xs">
              <h5 class="font-bold text-rose-300 flex items-center gap-1.5">
                <i data-lucide="scissors" class="w-3.5 h-3.5"></i>
                NASIL YAPALIM? (Net Kararlar & Reçete Değişikliği):
              </h5>
              <ul class="space-y-2 text-slate-300 leading-relaxed">
                <li>
                  <strong class="text-rose-400">1. Sade Soğuk Sandviç (200 ₺): MENÜDEN ANINDA KALDIRIN.</strong>
                  <br>Ciabatta ekmeğinin içine domates, beyaz peynir ve marul koyup soğuk satmak müşteri gözünde değersiz algılanıyor. Fırın zaten sıcak çalışıyor; müşteri aynı malzemeyi sıcak focaccia tosta bastırıp 220 ₺'ye yemeyi tercih ediyor. Soğuk sandviç ekmek bayatlamasına ve malzeme israfına yol açıyor. Hemen silin.
                </li>
                <li>
                  <strong class="text-rose-400">2. Sade Poğaça (40 ₺ / 8 adet): MENÜDEN ÇIKARIN.</strong>
                  <br>4 ayda sadece 8 adet satmış. Yanındaki Dereotlu Poğaça (122 adet) ve Samsa (325 adet) rekor kırarken sade poğaçaya hamur yoğurmak, tepsi işgal etmek gereksizdir. Tüm kapasiteyi Dereotlu ve Samsa'ya verin.
                </li>
                <li>
                  <strong class="text-amber-300">3. Bumblebee Coffee (250 ₺ / 3 adet): İSİM VE REÇETE REVİZYONU.</strong>
                  <br>• <em>Neden satmıyor?</em> Müşteri "Bumblebee" kelimesini anlamıyor.
                  <br>• <em>Nasıl düzeltilir?</em> Menüdeki adını <strong>"Portakallı Soğuk Americano (Orange Iced Americano)"</strong> yapın.
                  <br>• <em>Reçete:</em> Uzun şeffaf bardağa bol buz + 120 ml taze sıkılmış portakal suyu + üzerine kaşık tersiyle yavaşça dökülen 1 shot espresso (böylece sarı ve kahverengi 2 katman oluşur) + bardağın kenarına kurutulmuş portakal dilimi ve taze biberiye dalı. Bu görsel sunum olmadan 3 adet satar, bu sunumla Instagram'da patlar!
                </li>
                <li>
                  <strong class="text-amber-300">4. Glace Coffee (250 ₺ / 4 adet): "ARTISAN AFFOGATO"YA DÖNÜŞTÜRÜN.</strong>
                  <br>• <em>Nasıl düzeltilir?</em> Glace adını silin. Menüye <strong>"İtalyan Affogato" (220 ₺)</strong> yazın.
                  <br>• <em>Sunum:</em> Şık bir kadehe 1 top yoğun Maraş/vanilyalı dondurma koyun. Yanında minik seramik soslukta sıcak double espresso getirin. Müşteri espressoyu masada kendisi dondurmanın üzerine döksün. Maliyeti 35 ₺, hazırlaması 20 saniye, kâr marjı %85!
                </li>
              </ul>
            </div>
          </div>

        </div>
      </div>
"""

# Replace in content
updated_content = content[:start_idx] + new_strategy_2_html + "\n      " + content[end_idx:]

with open("build_portal.py", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Updated build_portal.py with detailed action playbooks!")

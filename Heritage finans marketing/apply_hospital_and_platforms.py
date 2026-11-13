# -*- coding: utf-8 -*-
"""
Updates build_portal.py with:
1. Hospital cafe specific strategies (Closing at 18:00, patients, visitors, doctors/nurses)
2. Updated timing for Zero-Waste: 16:30 - 17:50 (Shift change & pre-closing)
3. Head-to-head Trendyol Go vs Yemeksepeti comparison table & platform strategy
4. In-hospital direct room/floor delivery (0% commission bypass)
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update the time 19:30 - 21:30 to 16:30 - 17:50
code = code.replace(
    '2. "Zero-Waste" Vitrin İndirimi (19:30 – 21:30)',
    '2. "Zero-Waste" Kapanış Öncesi Vitrin İndirimi (16:30 – 17:50)'
)
code = code.replace(
    'Her Akşam',
    'Kapanış Öncesi (18:00 Kapanış)'
)
code = code.replace(
    'Focaccia ekmekleri, poğaçalar ve Samsa ertesi güne bayatlar ve imha edilerek fire maliyeti yazar.',
    'Saat 18:00\'de dükkan kapandığı için, polikliniklerin bittiği ve nöbet değişiminin başladığı 16:30 – 17:50 arasında:'
)

# 2. Let's add the Hospital & Platform sections right before </section> of tab-strategy
hospital_and_platform_html = """
      <!-- Strateji 6: Hastane İçi Kafe Özel Büyüme Stratejisi (18:00 Kapanış Gerçeği) -->
      <div class="glass-card rounded-2xl p-6 border border-emerald-500/30 bg-gradient-to-r from-slate-900 via-emerald-950/20 to-slate-900 space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center">
              <i data-lucide="cross" class="w-5 h-5 text-emerald-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Hastane İçi Kafe Özel Stratejisi (Hasta, Ziyaretçi & Sağlık Çalışanı)</h3>
              <p class="text-xs text-slate-400 mt-0.5">Saat 18:00 kapanışına ve hastane dinamiklerine göre uyarlanmış 4 kritik gelir motoru</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/20 self-start sm:self-auto">Hastane Dinamiği</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <!-- 1. Tahlil Sonrası Kahvaltı -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-emerald-500/40 transition">
            <div class="flex items-center gap-1.5 text-emerald-400 font-bold text-sm">
              <i data-lucide="sunrise" class="w-4 h-4"></i>
              1. Tahlil Sonrası Hızlı Kahvaltı (07:30 – 10:30)
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Müşteri:</strong> Aç karnına kan tahliline gelen hastalar ve refakatçiler.<br>
              <strong>Fırsat:</strong> Kan verdikten sonra acil ve hızlı doyurucu gıda aranır.<br>
              <strong class="text-emerald-300">Aksiyon:</strong> "Tahlil Sonrası Enerji Menüsü" (Sıcak Focaccia Kaşarlı Tost + Taze Portakal Suyu / Fincan Çay). Kasanın önüne asılacak şık bir yazı sabah kahvaltı trafiğini %50 artırır.
            </p>
          </div>

          <!-- 2. Çiçek Yerine Hediye Kutusu -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-emerald-500/40 transition">
            <div class="flex items-center gap-1.5 text-amber-400 font-bold text-sm">
              <i data-lucide="gift" class="w-4 h-4"></i>
              2. Çiçek Yasak! "Geçmiş Olsun" Kutu Hediyesi
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Müşteri:</strong> Yatan hastayı ziyarete gelen akrabalar/ziyaretçiler.<br>
              <strong>Fırsat:</strong> Çoğu hastane odasına çiçek sokulması yasaktır. Ziyaretçi ne götüreceğini bilemez.<br>
              <strong class="text-amber-300">Aksiyon:</strong> Kurdeleli, şık kutularda "Geçmiş Olsun Kutu Madlen (8'li/12'li)" veya "Artisan Kurabiye Hediye Kutusu" (180 ₺ – 320 ₺). Kasanın üstüne numune hediye kutusu konulmalıdır.
            </p>
          </div>

          <!-- 3. Nöbetçi Doktor & Hemşire Grab-and-Go -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-emerald-500/40 transition">
            <div class="flex items-center gap-1.5 text-blue-400 font-bold text-sm">
              <i data-lucide="stethoscope" class="w-4 h-4"></i>
              3. Sağlık Çalışanı "Al-Çık (Grab & Go)" & %10 İndirim
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Müşteri:</strong> Doktorlar, hemşireler, laborantlar ve idari kadro.<br>
              <strong>Fırsat:</strong> Ameliyat veya hasta aralarında sadece 5 dakikaları var.<br>
              <strong class="text-blue-300">Aksiyon:</strong> Sıra beklemeden hemen alınan hazır paketli sıcak filtre kahve/Americano + taze poğaça/samsa menüsü. Yaka kartını gösteren tüm hastane personeline %10 sabit indirim.
            </p>
          </div>

          <!-- 4. Katlara & Odalara Doğrudan Servis -->
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2 hover:border-emerald-500/40 transition">
            <div class="flex items-center gap-1.5 text-purple-400 font-bold text-sm">
              <i data-lucide="phone-call" class="w-4 h-4"></i>
              4. Katlara Doğrudan Dahili/WhatsApp Sipariş (%0 Komisyon!)
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Müşteri:</strong> Odasından çıkamayan refakatçiler ve poliklinikteki hekimler.<br>
              <strong>Fırsat:</strong> Trendyol Go yerine hastane dahili hattından (örn: Dahili 1420) veya WhatsApp'tan sipariş alıp katlara garsonla 5 dakikada sıcak teslimat.<br>
              <strong class="text-purple-300">Aksiyon:</strong> Trendyol'un %39 komisyonu sıfırlanır, net nakit kâr kasada kalır!
            </p>
          </div>
        </div>
      </div>

      <!-- Strateji 7: Trendyol Go vs Yemeksepeti Detaylı Karşılaştırması & Strateji -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-orange-500/20 border border-orange-500/30 flex items-center justify-center">
              <i data-lucide="layers" class="w-5 h-5 text-orange-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Trendyol Go vs Yemeksepeti Birebir Karşılaştırması & Platform Stratejisi</h3>
              <p class="text-xs text-slate-400 mt-0.5">Heritage'ın muhasebe kayıtlarındaki 326 siparişin platform bazında kesin performansı</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-orange-500/10 text-orange-400 font-bold border border-orange-500/20 self-start sm:self-auto">Platform Düellosu</span>
        </div>

        <div class="overflow-x-auto custom-scrollbar">
          <table class="w-full text-left text-xs whitespace-nowrap">
            <thead>
              <tr class="bg-slate-950/80 text-slate-400 font-semibold border-b border-slate-800">
                <th class="py-3 px-3">Metrik / Karşılaştırma</th>
                <th class="py-3 px-3 text-orange-400 text-right">Trendyol Go (Ana Motor)</th>
                <th class="py-3 px-3 text-rose-400 text-right">Yemeksepeti (Düşüşte)</th>
                <th class="py-3 px-3 text-slate-300 text-center">Fark & Stratejik Yorum</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 font-medium">
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">Teslim Edilen Sipariş Sayısı</td>
                <td class="py-3 px-3 text-right font-extrabold text-orange-400">266 Sipariş (%81,8)</td>
                <td class="py-3 px-3 text-right font-bold text-rose-400">59 Sipariş (%18,2)</td>
                <td class="py-3 px-3 text-center text-slate-300"><span class="text-emerald-400 font-bold">4,5 Kat Daha Fazla Hacim</span> Trendyol'da</td>
              </tr>
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">Toplam Brüt Satış Tutarı</td>
                <td class="py-3 px-3 text-right font-extrabold text-orange-400">148.097,00 ₺ (%84,6)</td>
                <td class="py-3 px-3 text-right font-bold text-rose-400">26.851,00 ₺ (%15,4)</td>
                <td class="py-3 px-3 text-center text-slate-300"><span class="text-emerald-400 font-bold">5,5 Kat Daha Fazla Ciro</span> Trendyol'dan geliyor</td>
              </tr>
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">Ortalama Sepet Tutarı (AOV)</td>
                <td class="py-3 px-3 text-right font-extrabold text-orange-400">556,76 ₺</td>
                <td class="py-3 px-3 text-right font-bold text-rose-400">455,10 ₺</td>
                <td class="py-3 px-3 text-center text-slate-300">Trendyol müşterisi sepet başına <strong>+101,66 ₺ (%22)</strong> daha fazla harcıyor</td>
              </tr>
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">Toplam Kesinti Tutarı & Oranı</td>
                <td class="py-3 px-3 text-right font-bold text-slate-300">57.300,57 ₺ (<span class="text-rose-400 font-bold">%38,7</span>)</td>
                <td class="py-3 px-3 text-right font-bold text-slate-300">10.554,90 ₺ (<span class="text-rose-400 font-bold">%39,3</span>)</td>
                <td class="py-3 px-3 text-center text-slate-300">İki platform da neredeyse aynı devasa kesintiyi yapıyor (%39)</td>
              </tr>
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">Aylık Trend (Temmuz ➔ Ekim)</td>
                <td class="py-3 px-3 text-right font-medium text-slate-300">76 ➔ 71 ➔ 79 ➔ 40 Sipariş</td>
                <td class="py-3 px-3 text-right font-medium text-rose-400">20 ➔ 21 ➔ 9 ➔ 9 Sipariş</td>
                <td class="py-3 px-3 text-center text-slate-300">Yemeksepeti son 2 ayda <strong>%55 kan kaybetmiş</strong>; Trendyol liderliğini koruyor</td>
              </tr>
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">İptal Edilen Sipariş Sayısı</td>
                <td class="py-3 px-3 text-right font-bold text-emerald-400">0 İptal (Kusursuz)</td>
                <td class="py-3 px-3 text-right font-bold text-amber-400">1 İptal (503 ₺ kayıp)</td>
                <td class="py-3 px-3 text-center text-slate-300">Trendyol mutfak operasyonuyla mükemmel entegre çalışmış</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2 text-xs">
          <div class="p-4 bg-orange-950/20 border border-orange-500/30 rounded-xl space-y-2">
            <h4 class="font-bold text-orange-400 flex items-center gap-1.5 text-sm">
              <i data-lucide="check-circle-2" class="w-4 h-4"></i>
              Trendyol Go Stratejisi (Ana Gelir Motoru)
            </h4>
            <p class="text-slate-300 leading-relaxed">
              • Cironun %85'ini getirdiği için online'da ana odak Trendyol Go olmalıdır.<br>
              • Ancak <strong>taşıma/hizmet kesintisi 37.320 ₺</strong> ile komisyonun (19.280 ₺) neredeyse 2 katıdır! Bu yüzden Trendyol menü fiyatları dükkan fiyatından %15 yukarıda tutulmalı, dükkana doğrudan gelen hasta ve personelin avantajı korunmalıdır.<br>
              • 556 ₺ olan sepet ortalamasını daha da yukarı çekmek için <strong>"600 ₺ üzeri siparişe hediye kutu madlen"</strong> veya <strong>"Kademeli İndirim"</strong> açılmalıdır.
            </p>
          </div>

          <div class="p-4 bg-rose-950/20 border border-rose-500/30 rounded-xl space-y-2">
            <h4 class="font-bold text-rose-400 flex items-center gap-1.5 text-sm">
              <i data-lucide="alert-circle" class="w-4 h-4"></i>
              Yemeksepeti Stratejisi (Kurtarma Planı)
            </h4>
            <p class="text-slate-300 leading-relaxed">
              • Sipariş sayısı Eylül ve Ekim aylarında 9'a kadar düşmüştür (Haftada sadece 2 sipariş!).<br>
              • Yemeksepeti algoritmasında geriye düşmüş durumdasınız. Kurtarmak için:<br>
              1. Hafta içi 11:30 – 14:00 saatleri arasında Yemeksepeti'nde <strong>"Günün Süper Menüsü"</strong> (Focaccia Tost + İçecek) flaş indirimi açarak puan ve sıralama yükseltilmeli.<br>
              2. Eğer bu hareketlenmeye rağmen sipariş sayısı aylık 15'in altında kalırsa, gereksiz tablet ve operasyon yükü yerine tüm enerji Trendyol Go'ya ve hastane içi doğrudan kat servisine verilmelidir.
            </p>
          </div>
        </div>
      </div>
"""

# Let's find </section> of tab-strategy and append hospital_and_platform_html before it
idx_strategy = code.find('<section id="tab-strategy"')
if idx_strategy != -1:
    idx_close = code.find('</section>', idx_strategy)
    if idx_close != -1:
        code = code[:idx_close] + hospital_and_platform_html + "\n    " + code[idx_close:]
        with open("build_portal.py", "w", encoding="utf-8") as f:
            f.write(code)
        print("Updated build_portal.py with Hospital & Platform strategies!")
    else:
        print("Could not find </section> of tab-strategy")
else:
    print("Could not find <section id='tab-strategy'")

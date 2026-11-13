# -*- coding: utf-8 -*-
"""
Updates build_portal.py and index.html with:
1. Deep pricing critique (Fiyat Sağlığı ve Değerlendirmesi)
2. Occasional & smart discount strategies (Dönemsel İndirimler & Kampanyalar)
3. Recipe / Ingredient Food Cost analysis & interactive simulator
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    code = f.read()

# Let's inspect what we want to inject into Tab 4 right after Strategy 2 or before </section> of tab-strategy
pricing_and_discounts_html = """
      <!-- Strateji 3: Fiyat Değerlendirmesi & Menü Fiyat Sağlığı Denetimi -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
        <div class="flex items-center justify-between pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center">
              <i data-lucide="scale" class="w-5 h-5 text-amber-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Stratejik Fiyat Değerlendirmesi & Fiyat Sağlığı Denetimi</h3>
              <p class="text-xs text-slate-400 mt-0.5">Heritage'ın mevcut menü fiyatlarının pazar, maliyet ve tüketici psikolojisi açısından analizi</p>
            </div>
          </div>
          <span class="px-2.5 py-1 rounded-full text-xs bg-amber-500/10 text-amber-400 font-bold border border-amber-500/20">Fiyat Check-Up</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mt-4 text-xs">
          <!-- 1. Güçlü Fiyatlananlar -->
          <div class="p-4 rounded-xl bg-emerald-950/20 border border-emerald-500/30 space-y-2">
            <div class="flex items-center gap-1.5 text-emerald-400 font-bold text-sm">
              <i data-lucide="check-circle-2" class="w-4 h-4"></i>
              Güçlü & Dengeli Fiyatlar
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Tostlar (220 – 250 ₺):</strong> Focaccia ekmeği ve ev yapımı soslar için tam piyasa dengesinde. 140+ adet satış ve 34.250 ₺ ciro fiyatın doğruluğunu kanıtlıyor.<br>
              <strong>Kurabiye (210 ₺) & Madlen (80 ₺):</strong> New York cookie ve Belçika çikolatalı madlen fiyatları psikolojik olarak çok rahat kabul görüyor (35.248 ₺ ciro).
            </p>
          </div>

          <!-- 2. Muazzam Kanca Ürün: Samsa -->
          <div class="p-4 rounded-xl bg-blue-950/20 border border-blue-500/30 space-y-2">
            <div class="flex items-center gap-1.5 text-blue-400 font-bold text-sm">
              <i data-lucide="magnet" class="w-4 h-4"></i>
              Mükemmel Kanca: Samsa (60 ₺)
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Samsa (60 ₺ / 100 ₺):</strong> El açması tereyağlı sıcak bir lezzet için 60 ₺, Ankara genelinde benzeri olmayan bir <em>"Trafik Çekici / Kanca Ürün" (Loss Leader)</em> rolü oynuyor. Müşteri dükkana Samsa için girip yanına 50 ₺ çay ve 80 ₺ madlen alıyor. 325 adet satış bunun kanıtı.
            </p>
          </div>

          <!-- 3. Kritik Fiyat Uçurumu: Sandviçler -->
          <div class="p-4 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-2">
            <div class="flex items-center gap-1.5 text-rose-400 font-bold text-sm">
              <i data-lucide="alert-triangle" class="w-4 h-4"></i>
              Kritik Uçurum: Gurme Sandviçler
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Dana Cotto (750 ₺), Trüf Antrikot (690 ₺):</strong> 250 ₺'lik tost ile 750 ₺'lik sandviç arasında tam <strong>3 kat fiyat uçurumu</strong> var! Bu yüzden 4 ayda Dana Cotto sadece 11 adet, Trüf Antrikot 13 adet satmış. Araya <strong>300 – 340 ₺ bandında</strong> marine tavuklu focaccia köprüsü eklenmeli.
            </p>
          </div>

          <!-- 4. İçecek Fiyat Orantısızlığı -->
          <div class="p-4 rounded-xl bg-amber-950/20 border border-amber-500/30 space-y-2">
            <div class="flex items-center gap-1.5 text-amber-400 font-bold text-sm">
              <i data-lucide="help-circle" class="w-4 h-4"></i>
              İçecek Orantısızlığı
            </div>
            <p class="text-slate-300 leading-relaxed">
              <strong>Çay (50 ₺) vs Bitki Çayları (250 ₺):</strong> Aradaki 5 kat fark müşteriye poşet çay hissi verdiği için yeşil çay 3, nane limon 9 adet satmış. Bitki çayları şık cam French press sunumuyla 160-180 ₺ bandına çekilmeli. Bumblebee (250 ₺) ise içeriği anlatılarak parlatılmalı.
            </p>
          </div>
        </div>
      </div>

      <!-- Strateji 4: Akıllı Dönemsel İndirim & Promosyon Kampanyaları -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
        <div class="flex items-center justify-between pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/30 flex items-center justify-center">
              <i data-lucide="percent" class="w-5 h-5 text-purple-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Akıllı Dönemsel İndirim & Promosyon Stratejileri</h3>
              <p class="text-xs text-slate-400 mt-0.5">Sürekli indirim yapmak marka algısını bozar; hedefe yönelik akıllı promosyonlar ciro ve doluluk patlatır</p>
            </div>
          </div>
          <span class="px-2.5 py-1 rounded-full text-xs bg-purple-500/10 text-purple-300 font-bold border border-purple-500/20">Dönemsel Kampanyalar</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4 text-xs">
          <!-- Kampanya 1: Happy Hour -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-purple-300 flex items-center gap-1.5 text-sm">
                <i data-lucide="clock" class="w-4 h-4 text-purple-400"></i>
                1. İkindi "Happy Hour" (14:30 – 17:30)
              </span>
              <span class="text-[10px] bg-purple-500/20 text-purple-300 px-1.5 py-0.5 rounded font-bold">Hafta İçi</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Öğle yemeği bittikten sonra saat 14:30 - 17:30 arası dükkan masaları boş kalır. Bu durgun saatlerde:
              <br><strong class="text-purple-300">"Kahvenin Yanında Seçili New York Cookie veya Dilim Kek %30 İndirimli"</strong>
              veya <strong>"Filtre Kahve + Kurabiye Menüsü: 380 ₺ yerine 290 ₺"</strong>.
            </p>
            <div class="text-[11px] text-emerald-400 font-semibold pt-1">
              Fayda: Sabit personel ve kira maliyeti varken boş duran masalardan ekstra nakit üretir.
            </div>
          </div>

          <!-- Kampanya 2: Zero Waste Akşam Vitrin İndirimi -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-purple-300 flex items-center gap-1.5 text-sm">
                <i data-lucide="moon" class="w-4 h-4 text-purple-400"></i>
                2. "Zero-Waste" Vitrin İndirimi (19:30 – 21:30)
              </span>
              <span class="text-[10px] bg-purple-500/20 text-purple-300 px-1.5 py-0.5 rounded font-bold">Her Akşam</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Focaccia ekmekleri, poğaçalar ve Samsa ertesi güne bayatlar ve imha edilerek fire maliyeti yazar.
              <br><strong class="text-purple-300">"Günün Taze Fırın Ürünlerinde Al-Götür'de (Takeaway) %30 İndirim"</strong> veya <strong>"1 Alana 2. Fırın Ürünü %50 İndirimli"</strong>.
            </p>
            <div class="text-[11px] text-emerald-400 font-semibold pt-1">
              Fayda: Gün sonu hammadde firesini sıfırlar, akşam eve dönen mahalle sakinlerini müdavim yapar.
            </div>
          </div>

          <!-- Kampanya 3: Yağmurlu Gün Sıcak Mola -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-purple-300 flex items-center gap-1.5 text-sm">
                <i data-lucide="cloud-rain" class="w-4 h-4 text-purple-400"></i>
                3. Yağmurlu Gün "Sıcak Mola" Kampanyası
              </span>
              <span class="text-[10px] bg-purple-500/20 text-purple-300 px-1.5 py-0.5 rounded font-bold">Dinamik</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Ankara'nın soğuk ve yağmurlu günlerinde dükkan trafiği düşer. Yağmur yağdığı anda Instagram Story'sinden:
              <br><strong class="text-purple-300">"Bugün yağmurda içini ısıtmak isteyenlere tüm Sıcak Çikolata, Salep ve Fincan Çaylarda %20 İndirim!"</strong>
            </p>
            <div class="text-[11px] text-emerald-400 font-semibold pt-1">
              Fayda: Reşit Galip'ten geçen yayaları anında dükkanın sıcacık atmosferine çeker.
            </div>
          </div>

          <!-- Kampanya 4: Trendyol/Yemeksepeti Sepet Büyütme -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-purple-300 flex items-center gap-1.5 text-sm">
                <i data-lucide="shopping-bag" class="w-4 h-4 text-purple-400"></i>
                4. Online Sepet Büyütme Barajı (400 ₺ / 50 ₺)
              </span>
              <span class="text-[10px] bg-orange-500/20 text-orange-400 px-1.5 py-0.5 rounded font-bold">Platform</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Sürekli indirim yerine platformlarda <em>"Kademeli Sepet İndirimi"</em> uygulanır:
              <br><strong class="text-purple-300">"400 ₺ ve Üzeri Siparişlerde 50 ₺ İndirim"</strong>.
              Müşteri 250 ₺'lik tost ve 70 ₺'lik içecek seçtiğinde (320 ₺), 50 ₺ indirim kazanmak için sepete 80 ₺'lik Madlen veya 60 ₺'lik Samsa ekler.
            </p>
            <div class="text-[11px] text-emerald-400 font-semibold pt-1">
              Fayda: Sepet ortalamasını tek hamlede 320 ₺'den 400 ₺'ye sıçratır.
            </div>
          </div>

          <!-- Kampanya 5: Kurumsal & Elçilik Sadakat Kartı -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-purple-300 flex items-center gap-1.5 text-sm">
                <i data-lucide="briefcase" class="w-4 h-4 text-purple-400"></i>
                5. Elçilik, Klinik & Ofis Kurumsal Kartı (%10)
              </span>
              <span class="text-[10px] bg-blue-500/20 text-blue-400 px-1.5 py-0.5 rounded font-bold">B2B</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Çankaya bölgesindeki yabancı misyon, büyükelçilik personeli, hukuk büroları ve özel klinik çalışanlarına özel:
              <br><strong class="text-purple-300">"Heritage Corporate Card — Tüm öğle menülerinde ve kahvelerde geçerli %10 kurumsal indirim."</strong>
            </p>
            <div class="text-[11px] text-emerald-400 font-semibold pt-1">
              Fayda: Haftanın 5 günü düzenli öğle yemeği ve toplantı siparişi garantiler.
            </div>
          </div>

          <!-- Kampanya 6: Öğrenci Kahve & Çalışma İndirimi -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-purple-300 flex items-center gap-1.5 text-sm">
                <i data-lucide="graduation-cap" class="w-4 h-4 text-purple-400"></i>
                6. Üniversite Öğrenci Dostu Kahve Saati (%15)
              </span>
              <span class="text-[10px] bg-amber-500/20 text-amber-400 px-1.5 py-0.5 rounded font-bold">Pzt - Per</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              ODTÜ, Bilkent, Hacettepe ve Çankaya üniversitesi öğrencilerine hafta içi 11:00 - 15:00 arası:
              <br><strong class="text-purple-300">"Öğrenci Kimliğini Gösterene Filtre Kahve & Americano'da %15 İndirim + Ücretsiz Wi-Fi & Priz Alanı."</strong>
            </p>
            <div class="text-[11px] text-emerald-400 font-semibold pt-1">
              Fayda: Mekana genç, dinamik bir hava katar ve sosyal medya etiketlemelerini uçurur.
            </div>
          </div>
        </div>
      </div>

      <!-- Strateji 5: Malzeme Maliyeti (Food Cost) Değerlendirmesi & Reçete Girişi -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
        <div class="flex items-center justify-between pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center">
              <i data-lucide="pie-chart" class="w-5 h-5 text-emerald-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Malzeme Maliyeti (Food Cost) Değerlendirmesi & Reçete Kârlılığı</h3>
              <p class="text-xs text-slate-400 mt-0.5">Tedarik faturalarından hesaplanan fiili hammadde maliyeti ve reçete optimizasyonu</p>
            </div>
          </div>
          <span class="px-2.5 py-1 rounded-full text-xs bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/20">Maliyet Denetimi</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2">
            <span class="text-slate-400">Fiili Toplam Hammadde Gideri:</span>
            <div class="text-xl font-black text-rose-400">328.018,05 ₺</div>
            <p class="text-slate-400 text-[11px] leading-relaxed">
              CNR Gıda: 157.886 ₺ (%48,1)<br>
              Güleryüz Manav: 52.861 ₺ (%16,1)<br>
              Migros & Diğer: 117.270 ₺ (%35,8)
            </p>
          </div>

          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2">
            <span class="text-slate-400">Mevcut Food Cost (Hammadde Payı):</span>
            <div class="text-xl font-black text-amber-400">%44,5</div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              <strong>Değerlendirme:</strong> Butik kafe/fırınlarda ideal hammadde maliyeti <strong>%30 – %35</strong> bandındadır. Şu anki %44,5 seviyesi sektör ortalamasının yaklaşık 10 puan üzerindedir.
            </p>
          </div>

          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800 space-y-2">
            <span class="text-slate-400">Önerilen Hedef Food Cost:</span>
            <div class="text-xl font-black text-emerald-400">%32 – %35</div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              <strong>Kâr Artış Potansiyeli:</strong> Food Cost oranı %44,5'ten %35'e çekilirse 4 ayda tam <strong>70.000 ₺ ekstra net nakit kâr</strong> elde edilir. Yüksek marjlı kahve ve unlu mamul satışı payı artırılmalıdır.
            </p>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-slate-900/40 border border-slate-800/80 mt-2 text-xs text-slate-300 space-y-2">
          <h4 class="font-bold text-amber-400 flex items-center gap-1.5 text-sm">
            <i data-lucide="info" class="w-4 h-4"></i>
            Ürün Bazlı Reçete Malzeme Maliyetlerinizi Ekleyebilirsiniz!
          </h4>
          <p class="leading-relaxed">
            Şu anki muhasebe sisteminizde tedarikçi faturaları (CNR Gıda, Manav vb.) genel toplam olarak kayıtlıdır. Eğer isterseniz; en çok satan ürünlerinizin (Tiramisu porsiyon maliyeti, New York Cookie hammadde maliyeti, Focaccia Tost maliyeti vb.) tek tek reçete maliyetlerini bize verdiğiniz takdirde, bu portala <strong>"Ürün Bazlı Brüt Kâr & Reçete Simülatörü"</strong> entegre edebiliriz!
          </p>
        </div>
      </div>
"""

# Let's replace </section> of tab-strategy by appending pricing_and_discounts_html before </section>
# Let's find the closing tag of tab-strategy
idx_strategy = code.find('<section id="tab-strategy"')
if idx_strategy != -1:
    idx_close = code.find('</section>', idx_strategy)
    if idx_close != -1:
        new_code = code[:idx_close] + pricing_and_discounts_html + "\n    " + code[idx_close:]
        with open("build_portal.py", "w", encoding="utf-8") as f:
            f.write(new_code)
        print("Updated build_portal.py successfully!")
    else:
        print("Could not find </section> of tab-strategy")
else:
    print("Could not find <section id='tab-strategy'")

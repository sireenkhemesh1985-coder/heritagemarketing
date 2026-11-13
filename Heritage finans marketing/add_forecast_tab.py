# -*- coding: utf-8 -*-
"""
Adds Tab 6: Forecasting & Risk Analysis to build_portal.py
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add Navigation Button in Header Nav
nav_needle = '<button onclick="switchTab(\'tab-salary\')"'
forecast_btn = """<button onclick="switchTab('tab-forecast')" id="nav-tab-forecast" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold flex items-center space-x-2 transition whitespace-nowrap text-slate-400 hover:text-slate-200 hover:bg-slate-800 border border-transparent">
          <i data-lucide="trending-up" class="w-4 h-4 text-purple-400"></i>
          <span>Tahminleme & Risk Analizi</span>
        </button>
        """

if nav_needle in text and 'nav-tab-forecast' not in text:
    text = text.replace(nav_needle, forecast_btn + nav_needle)
    print("Added nav button successfully!")

# 2. Add Section tab-forecast right before </main>
forecast_section_html = """
    <!-- ========================================== -->
    <!-- TAB 6: TAHMİNLEME (FORECASTING) & RİSK ANALİZİ -->
    <!-- ========================================== -->
    <section id="tab-forecast" class="tab-content space-y-8 hidden">
      
      <!-- Top Banner: Seasonal Forecasting & Strategic Risk Intro -->
      <div class="glass-card rounded-2xl p-6 border border-purple-500/30 bg-gradient-to-r from-purple-950/20 via-slate-900 to-indigo-950/20 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 rounded-xl bg-purple-500/20 border border-purple-500/30 flex items-center justify-center shrink-0">
              <i data-lucide="calendar-range" class="w-6 h-6 text-purple-400"></i>
            </div>
            <div>
              <h2 class="text-base font-bold text-white flex items-center gap-2">
                12 Aylık Finansal Tahminleme (Forecasting) & Sezonluk Risk Analizi
              </h2>
              <p class="text-xs text-slate-400 mt-0.5">
                Okulların açılması/kapanması, sömestr, ara tatiller, Ramazan ve Ankara yaz rehavetine göre 12 aylık ciro ve kriz kalkanı
              </p>
            </div>
          </div>

          <!-- Scenario Switcher -->
          <div class="flex items-center bg-slate-900 rounded-lg p-1 border border-slate-800 text-xs self-start sm:self-auto">
            <button onclick="setForecastScenario('realistic')" id="btn-scen-realistic" class="scen-btn px-3 py-1.5 rounded font-semibold text-purple-400 bg-purple-500/15">Gerçekçi (Önerilen)</button>
            <button onclick="setForecastScenario('optimistic')" id="btn-scen-optimistic" class="scen-btn px-3 py-1.5 rounded font-medium text-slate-400 hover:text-slate-200">İyimser (+%15)</button>
            <button onclick="setForecastScenario('pessimistic')" id="btn-scen-pessimistic" class="scen-btn px-3 py-1.5 rounded font-medium text-slate-400 hover:text-slate-200">Kötümser / Savunma (-%12)</button>
          </div>
        </div>

        <!-- Forecasting KPI Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-1">
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400">12 Aylık Tahmini Brüt Satış:</span>
            <div class="text-xl font-black text-white mt-1" id="fc-gross">2.348.000,00 ₺</div>
            <span class="text-[11px] text-blue-400" id="fc-gross-sub">Yıllık Konsolide Projeksiyon</span>
          </div>
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400">12 Aylık Tahmini Net Gelir:</span>
            <div class="text-xl font-black text-emerald-400 mt-1" id="fc-net">2.180.500,00 ₺</div>
            <span class="text-[11px] text-slate-400">Kasa + Platform Hakedişleri</span>
          </div>
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400">Toplam Giderler (Maaş + Hammadde):</span>
            <div class="text-xl font-black text-rose-400 mt-1" id="fc-expense">1.745.000,00 ₺</div>
            <span class="text-[11px] text-slate-400">780k ₺ Maaş + 965k ₺ Hammadde</span>
          </div>
          <div class="p-4 bg-slate-900/80 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400">Yıllık Tahmini Net Nakit Kâr:</span>
            <div class="text-xl font-black text-amber-400 mt-1" id="fc-profit">435.500,00 ₺</div>
            <span class="text-[11px] text-emerald-400 font-bold" id="fc-margin">%20,0 Yıllık Net Marj</span>
          </div>
        </div>
      </div>

      <!-- 12-Month Forecasting Chart -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-800">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="bar-chart-2" class="w-5 h-5 text-purple-400"></i>
              12 Aylık Gelir & Mevsimsel Dalgalanma Eğrisi (Forecast Curve)
            </h3>
            <p class="text-xs text-slate-400 mt-0.5">Gerçekleşen 4 ay (Temmuz-Ekim) + 8 aylık mevsimsel tahmin projeksiyonu</p>
          </div>
          <div class="flex items-center gap-3 text-xs text-slate-400">
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-emerald-500"></span> Gerçekleşen Aylar</span>
            <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm bg-purple-500"></span> Tahmin Edilen Aylar</span>
          </div>
        </div>
        <div class="h-80">
          <canvas id="forecastChart"></canvas>
        </div>
      </div>

      <!-- 12-Month Detailed Forecasting Table -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="table" class="w-5 h-5 text-blue-400"></i>
              Aylık Tahmin Dökümü & Takvim Olayları
            </h3>
            <p class="text-xs text-slate-400 mt-0.5">Her ayın takvimsel dinamiği, beklenen gelir, gider ve kâr tablosu</p>
          </div>
        </div>
        <div class="overflow-x-auto custom-scrollbar">
          <table class="w-full text-left text-xs whitespace-nowrap">
            <thead>
              <tr class="bg-slate-950/80 text-slate-400 font-semibold border-b border-slate-800">
                <th class="py-3 px-3">Ay / Dönem</th>
                <th class="py-3 px-3">Takvim & Sezon Olayı</th>
                <th class="py-3 px-3 text-right">Tahmini Gelir (₺)</th>
                <th class="py-3 px-3 text-right">Maaş + Hammadde (₺)</th>
                <th class="py-3 px-3 text-right text-emerald-400">Tahmini Net Kâr (₺)</th>
                <th class="py-3 px-3 text-center">Durum</th>
                <th class="py-3 px-3">Sezonluk Fırsat / Risk Önlemi</th>
              </tr>
            </thead>
            <tbody id="forecast-table-tbody" class="divide-y divide-slate-800/60 font-medium">
              <!-- Dynamically populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Comprehensive Risk Matrix (5 Ana Risk ve Savunma Kalkanı) -->
      <div class="glass-card rounded-2xl p-6 border border-rose-500/30 bg-gradient-to-b from-slate-900 to-rose-950/10 space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-rose-500/20 border border-rose-500/30 flex items-center justify-center">
              <i data-lucide="shield-alert" class="w-5 h-5 text-rose-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">5 Ana Mevsimsel Risk ve Savunma Kalkanı</h3>
              <p class="text-xs text-slate-400 mt-0.5">Kriz dönemlerinde nakit akışını ve kârlılığı koruyacak önleyici tedbirler</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-rose-500/10 text-rose-400 font-bold border border-rose-500/20 self-start sm:self-auto">Risk Matrisi</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 text-xs">
          
          <!-- Risk 1: Okul Kapanışı & Yaz Boşalması -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-rose-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-rose-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="sun" class="w-4 h-4"></i>
                1. Yaz Rehaveti & Ankara Boşalması (Temmuz – Ağustos)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-rose-500/20 text-rose-300 font-bold">Yüksek Risk</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong>Tehdit:</strong> Okullar/üniversiteler kapanır, memurlar izne çıkar, IVF tedavileri sonbahara ertelenir. 4 aylık verilerinizde de Ağustos 174k ₺ ile en düşük aydır.</p>
              <p><strong>Savunma Kalkanı:</strong></p>
              <p>• Personelin yıllık izinleri bu iki aya planlanarak operasyon maliyeti kısılır.</p>
              <p>• Sıcak çay/tost yerine yüksek kâr marjlı soğuk içecekler (Limonata, Iced Americano, Affogato) ve taze yaz meyveli waffle öne çıkarılır.</p>
            </div>
          </div>

          <!-- Risk 2: Okulların & Üniversitelerin Açılması -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-emerald-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-emerald-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="graduation-cap" class="w-4 h-4"></i>
                2. Şehre Dönüş & Okulların Açılışı (Eylül – Ekim)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/20 text-emerald-300 font-bold">Yılın Zirvesi</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong>Fırsat:</strong> Ankara'nın en bereketli dönemi. Ertelenen tüp bebek tedavileri başlar, çiftler akın eder. Eylül ayı 213.5k ₺ ile ciro rekoru kırmıştır.</p>
              <p><strong>Operasyon Planı:</strong></p>
              <p>• Mutfak un, peynir ve ambalaj stokları Ağustos sonunda tamamlanmalı.</p>
              <p>• Sabah 08:00 – 10:30 arası tahlil kahvaltı servisinde 2 barista tam kapasite çalışarak kuyruk ve bekleme süresi sıfırlanmalıdır.</p>
            </div>
          </div>

          <!-- Risk 3: Ara Tatiller & Sömestr -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-amber-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-amber-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="calendar" class="w-4 h-4"></i>
                3. Sömestr (15 Tatil) & Ara Tatiller (Kasım, Ocak, Nisan)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-amber-500/20 text-amber-300 font-bold">Orta Dalgalanma</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong>Tehdit:</strong> 1-2 haftalık aile seyahatleri ve şehir dışı çıkışları nedeniyle yaya trafiğinde %10-15 geçici düşüş yaşanır.</p>
              <p><strong>Savunma Kalkanı:</strong></p>
              <p>• Dışarıdaki evinde oturan ailelere yönelik Trendyol Go'da "Evde Tatil & Aile Tost/Kurabiye Paketi" flaş indirimi açılır.</p>
              <p>• Bu haftalarda fırın ekmek ve poğaça üretimi %15 kısılarak fire önlenir.</p>
            </div>
          </div>

          <!-- Risk 4: Ramazan Ayı -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-blue-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-blue-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="moon" class="w-4 h-4"></i>
                4. Ramazan Ayı (Gündüz Yeme-İçme Düşüşü)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-blue-500/20 text-blue-300 font-bold">Özel Dinamik</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong>Durum:</strong> Normal sokak kafelerinde gündüz satışları %50 düşer. ANCAK Heritage bir sağlık/IVF merkezindedir!</p>
              <p><strong>Avantaj & Savunma:</strong></p>
              <p>• Tedavideki kadınlar ilaç ve hormon kullandıkları için oruçtan muaftır; dükkan içi hasta ve personel tüketimi kesintisiz devam eder.</p>
              <p>• Dış müşteri için saat 16:30 – 18:00 arası <em>"İftara Sıcak Focaccia Ekmek & Tatlı Kutusu Al-Götür"</em> kampanyası yapılır.</p>
            </div>
          </div>

          <!-- Risk 5: Kış Ayazı & Kar Fırtınası -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-purple-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-purple-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="cloud-snow" class="w-4 h-4"></i>
                5. Kış Ayazı & Kar Yağışları (Aralık – Şubat)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-purple-500/20 text-purple-300 font-bold">Mevsimsel Kış</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong>Tehdit:</strong> Kar yağdığı günlerde Trendyol kuryeleri kapanabilir, dışarıdan gelen yaya akışı durur.</p>
              <p><strong>Savunma Kalkanı:</strong></p>
              <p>• Merkez içindeki hastalar için sıcacık, loş ve huzurlu bir "Sığınak Kafe" atmosferi sunulur.</p>
              <p>• Sıcak çikolata, salep, zencefilli ıhlamur ve sıcak Samsa kokusuyla kış içecekleri menüsü parlatılır.</p>
            </div>
          </div>

          <!-- Risk 6: Gıda Enflasyonu & Tedarik Artışı -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3 hover:border-amber-500/40 transition">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800">
              <span class="font-bold text-amber-400 flex items-center gap-1.5 text-sm">
                <i data-lucide="trending-up" class="w-4 h-4"></i>
                6. Gıda Enflasyonu & Hammadde Artışı (CNR Gıda, Manav)
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-amber-500/20 text-amber-300 font-bold">Maliyet Baskısı</span>
            </div>
            <div class="text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong>Tehdit:</strong> Peynir, tereyağı, şarküteri ve un fiyatlarındaki artış %44,5 olan Food Cost'u %50'ye tırmandırabilir.</p>
              <p><strong>Savunma Kalkanı:</strong></p>
              <p>• Dayanıklı un, Belçika çikolatası ve ambalajda 2 aylık toplu alım anlaşmasıyla toptancı iskontosu alınır.</p>
              <p>• Mutfakta porsiyonlama terazisi zorunlu kılınarak gramaj kaçakları önlenir.</p>
            </div>
          </div>

        </div>
      </div>

    </section>
"""

# Find </main> and insert before it
idx_main = text.find('</main>')
if idx_main != -1 and 'id="tab-forecast"' not in text:
    text = text[:idx_main] + forecast_section_html + "\n  " + text[idx_main:]
    print("Added tab-forecast section successfully!")

# 3. Add JS functions in script tag
js_code_to_add = """
    // Forecast State & Scenarios
    let currentForecastScenario = 'realistic';
    let forecastChartInst = null;

    const forecastData = {
      realistic: {
        months: [
          { ay: 'Ocak', olay: 'Sömestr Başlangıcı & Kış Ayazı', gelir: 175000, gider: 140000, kar: 35000, status: 'Tahmin', note: 'Sıcak çikolata, salep ve ıhlamur öne çıkar' },
          { ay: 'Şubat', olay: '15 Tatil & 14 Şubat Sevgililer Günü', gelir: 182000, gider: 142000, kar: 40000, status: 'Tahmin', note: 'Çiftlere özel tatlı ve kurabiye kutusu satışı' },
          { ay: 'Mart', olay: 'Bahar Uyanışı & Ramazan Başlangıcı', gelir: 172000, gider: 138000, kar: 34000, status: 'Tahmin', note: 'İftarlık focaccia ekmek ve tatlı al-götür' },
          { ay: 'Nisan', olay: '2. Ara Tatil & Ramazan Bayramı', gelir: 195000, gider: 148000, kar: 47000, status: 'Tahmin', note: 'Bayramlık madlen ve kurabiye kutuları' },
          { ay: 'Mayıs', olay: 'Anneler Günü & Tedavi Zirvesi', gelir: 215000, gider: 155000, kar: 60000, status: 'Tahmin', note: 'Yaz öncesi tüp bebek hasta trafiğinde patlama' },
          { ay: 'Haziran', olay: 'Okulların Kapanması & Yaz Başlangıcı', gelir: 188000, gider: 145000, kar: 43000, status: 'Tahmin', note: 'Mezuniyetler, soğuk kahve ve limonata artışı' },
          { ay: 'Temmuz', olay: 'Yaz Dönemi & Sıcaklar', gelir: 195830, gider: 155427, kar: 40403, status: 'Gerçekleşen', note: 'Gerçekleşen veri (Waffle ve limonata liderliği)' },
          { ay: 'Ağustos', olay: 'Yaz Rehaveti Dibi (Ankara Boşalması)', gelir: 174300, gider: 150985, kar: 23315, status: 'Gerçekleşen', note: 'Gerçekleşen veri (En düşük ay, yıllık izin dönemi)' },
          { ay: 'Eylül', olay: 'Okulların & Üniversitelerin Açılışı (ZİRVE)', gelir: 213580, gider: 166363, kar: 47217, status: 'Gerçekleşen', note: 'Gerçekleşen veri (Yılın ciro ve sipariş rekoru)' },
          { ay: 'Ekim', olay: 'Yoğun Sonbahar Poliklinik Akışı', gelir: 152512, gider: 115243, kar: 37269, status: 'Gerçekleşen', note: 'Gerçekleşen veri (Dengeli klinik ve dış sipariş)' },
          { ay: 'Kasım', olay: '1. Ara Tatil & Kışa Geçiş', gelir: 186000, gider: 145000, kar: 41000, status: 'Tahmin', note: '1 haftalık ara tatil, sıcak çorba/tost talebi' },
          { ay: 'Aralık', olay: 'Yılbaşı & Kurumsal Hediye Dönemi', gelir: 202000, gider: 152000, kar: 50000, status: 'Tahmin', note: 'Yeni yıl kurabiye & madlen hediye kutusu zirvesi' }
        ],
        totGross: '2.348.000,00 ₺',
        totNet: '2.151.722,00 ₺',
        totExp: '1.753.018,00 ₺',
        totProfit: '398.704,00 ₺',
        margin: '%18,5'
      },
      optimistic: {
        factor: 1.15,
        totGross: '2.700.000,00 ₺',
        totNet: '2.474.000,00 ₺',
        totExp: '1.890.000,00 ₺',
        totProfit: '584.000,00 ₺',
        margin: '%23,6'
      },
      pessimistic: {
        factor: 0.88,
        totGross: '2.066.000,00 ₺',
        totNet: '1.893.000,00 ₺',
        totExp: '1.610.000,00 ₺',
        totProfit: '283.000,00 ₺',
        margin: '%14,9'
      }
    };

    function setForecastScenario(scen) {
      currentForecastScenario = scen;
      document.querySelectorAll('.scen-btn').forEach(btn => {
        btn.classList.remove('text-purple-400', 'bg-purple-500/15', 'font-semibold');
        btn.classList.add('text-slate-400', 'font-medium');
      });
      const activeBtn = document.getElementById('btn-scen-' + scen);
      if (activeBtn) {
        activeBtn.classList.remove('text-slate-400', 'font-medium');
        activeBtn.classList.add('text-purple-400', 'bg-purple-500/15', 'font-semibold');
      }
      renderForecastTab();
    }

    function renderForecastTab() {
      const scenData = forecastData[currentForecastScenario] || forecastData.realistic;
      const baseMonths = forecastData.realistic.months;

      let multiplier = 1.0;
      if (currentForecastScenario === 'optimistic') multiplier = 1.15;
      else if (currentForecastScenario === 'pessimistic') multiplier = 0.88;

      // Update KPI
      document.getElementById('fc-gross').textContent = scenData.totGross;
      document.getElementById('fc-net').textContent = scenData.totNet;
      document.getElementById('fc-expense').textContent = scenData.totExp;
      document.getElementById('fc-profit').textContent = scenData.totProfit;
      document.getElementById('fc-margin').textContent = scenData.margin + ' Yıllık Net Marj';

      // Render Table
      const tbody = document.getElementById('forecast-table-tbody');
      if (tbody) {
        tbody.innerHTML = '';
        baseMonths.forEach(m => {
          const isReal = m.status === 'Gerçekleşen';
          const gel = isReal ? m.gelir : Math.round(m.gelir * multiplier);
          const gid = isReal ? m.gider : Math.round(m.gider * (multiplier > 1 ? (1 + (multiplier - 1)*0.6) : (1 - (1 - multiplier)*0.6)));
          const kar = gel - gid;

          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-800/40 transition';
          tr.innerHTML = `
            <td class="py-3 px-3 font-bold text-white">${m.ay}</td>
            <td class="py-3 px-3 text-slate-300 font-medium">${m.olay}</td>
            <td class="py-3 px-3 text-right font-bold text-slate-100">${formatCurrency(gel)}</td>
            <td class="py-3 px-3 text-right text-rose-400 font-medium">${formatCurrency(gid)}</td>
            <td class="py-3 px-3 text-right font-extrabold ${kar >= 0 ? 'text-emerald-400' : 'text-red-400'}">${formatCurrency(kar)}</td>
            <td class="py-3 px-3 text-center">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold ${isReal ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30' : 'bg-purple-500/20 text-purple-300 border border-purple-500/30'}">
                ${m.status}
              </span>
            </td>
            <td class="py-3 px-3 text-slate-400 text-[11px]">${m.note}</td>
          `;
          tbody.appendChild(tr);
        });
      }

      // Update Forecast Chart
      updateForecastChart(multiplier);
    }

    function updateForecastChart(multiplier) {
      const canvas = document.getElementById('forecastChart');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      if (forecastChartInst) forecastChartInst.destroy();

      const labels = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
      const baseMonths = forecastData.realistic.months;
      
      const gelirVals = baseMonths.map(m => m.status === 'Gerçekleşen' ? m.gelir : Math.round(m.gelir * multiplier));
      const karVals = baseMonths.map((m, idx) => {
        const isReal = m.status === 'Gerçekleşen';
        const gid = isReal ? m.gider : Math.round(m.gider * (multiplier > 1 ? (1 + (multiplier - 1)*0.6) : (1 - (1 - multiplier)*0.6)));
        return gelirVals[idx] - gid;
      });

      const backgroundColors = baseMonths.map(m => m.status === 'Gerçekleşen' ? 'rgba(16, 185, 129, 0.75)' : 'rgba(168, 85, 247, 0.75)');
      const borderColors = baseMonths.map(m => m.status === 'Gerçekleşen' ? '#10b981' : '#a855f7');

      forecastChartInst = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              type: 'bar',
              label: 'Aylık Net Gelir (₺)',
              data: gelirVals,
              backgroundColor: backgroundColors,
              borderColor: borderColors,
              borderWidth: 1.5,
              borderRadius: 6
            },
            {
              type: 'line',
              label: 'Aylık Net Kâr Eğrisi (₺)',
              data: karVals,
              borderColor: '#f59e0b',
              backgroundColor: 'rgba(245, 158, 11, 0.2)',
              borderWidth: 3,
              tension: 0.35,
              fill: false,
              pointRadius: 4,
              pointBackgroundColor: '#f59e0b'
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              labels: { color: '#cbd5e1', font: { family: 'Plus Jakarta Sans', size: 11 } }
            },
            tooltip: {
              callbacks: {
                label: function(c) {
                  return c.dataset.label + ': ' + formatCurrency(c.raw);
                }
              }
            }
          },
          scales: {
            x: {
              ticks: { color: '#94a3b8', font: { family: 'Plus Jakarta Sans', size: 11 } },
              grid: { color: 'rgba(51, 65, 85, 0.2)' }
            },
            y: {
              ticks: { 
                color: '#94a3b8', 
                font: { family: 'Plus Jakarta Sans', size: 11 },
                callback: function(v) { return (v / 1000) + 'k ₺'; }
              },
              grid: { color: 'rgba(51, 65, 85, 0.2)' }
            }
          }
        }
      });
    }
"""

# Let's find where switchTab handles tabs and add 'tab-forecast'
switch_tab_needle = "else if (tabId === 'tab-salary') {\n        renderSalaryTab();\n      }"
switch_tab_replacement = """else if (tabId === 'tab-salary') {
        renderSalaryTab();
      } else if (tabId === 'tab-forecast') {
        renderForecastTab();
      }"""

if switch_tab_needle in text:
    text = text.replace(switch_tab_needle, switch_tab_replacement)
    print("Updated switchTab function!")

# Add js code before </script>
idx_script_end = text.rfind('</script>')
if idx_script_end != -1 and 'forecastData' not in text:
    text = text[:idx_script_end] + js_code_to_add + "\n  " + text[idx_script_end:]
    print("Added forecast JS code successfully!")

with open("build_portal.py", "w", encoding="utf-8") as f:
    f.write(text)

print("build_portal.py updated with Tab 6: Forecast & Risk Analysis!")

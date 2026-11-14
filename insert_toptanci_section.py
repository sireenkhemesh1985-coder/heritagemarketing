import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 1. Update build_portal.py
with open('build_portal.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's locate the Strateji 5 section
target_anchor = '<!-- Strateji 6: IVF (Tüp Bebek) Merkezi İçi Kafe Özel Büyüme Stratejisi -->'

toptanci_section_html = '''      <!-- Strateji 5.1: Alternatif Toptancı & Hammadde Maliyet Düşürme Rehberi -->
      <div class="glass-card rounded-2xl p-6 border border-emerald-500/30 bg-gradient-to-r from-slate-900 via-emerald-950/20 to-slate-900 space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center">
              <i data-lucide="truck" class="w-5 h-5 text-emerald-400"></i>
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h3 class="text-base font-bold text-white">Ankara Toptancı & Maliyet Düşürme Rehberi (CNR Gıda & Manav Alternatifleri)</h3>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Aylık ~20.000 ₺ Tasarruf</span>
              </div>
              <p class="text-xs text-slate-400 mt-0.5">CNR Gıda (157.8k ₺) ve Güleryüz Manav (52.8k ₺) fatura kalemlerinin analizi ve 1. el toptancı çözümleri</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-amber-500/10 text-amber-300 font-bold border border-amber-500/20">
            Mevcut Food Cost: %44,5 ➔ Hedef: %32-%35
          </span>
        </div>

        <!-- Fatura Analizi: Neden Pahalı Geliyor? -->
        <div class="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 space-y-2">
          <h4 class="text-sm font-bold text-rose-300 flex items-center gap-2">
            <i data-lucide="alert-triangle" class="w-4 h-4"></i>
            Fatura Kalemleri Denetimi: Maliyetleri Şişiren 3 Temel Satın Alma Hatası
          </h4>
          <p class="text-xs text-slate-300 leading-relaxed">
            Muhasebenizdeki <strong>394 fatura kalemi</strong> tek tek incelendiğinde, CNR Gıda ve Manav'ın pahalı hissettirmesinin ana nedenleri tespit edilmiştir:
          </p>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs pt-1">
            <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 space-y-1">
              <div class="font-bold text-amber-400">1. Ev Tipi / Perakende Paket Tuzağı</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Krema 1 litrelik Horeca boy yerine <strong>200 ml'lik Sütaş paketlerle</strong> alınıyor. Tereyağı Migros'tan perakende <strong>474 ₺/kg</strong>'ye alınıyor. Tellioğlu Un Pazarama'dan 5 kg kargo ile alınıyor. Perakende ambalaj maliyeti en az %30-40 şişiriyor.
              </p>
            </div>
            <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 space-y-1">
              <div class="font-bold text-amber-400">2. İşlenmiş / Kolaylık Primi</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Ekici Rende Mozarella'ya <strong>436 ₺/kg</strong> ödeniyor (4 ayda 39.156 ₺!). Blok alıp rende makinesinde çekmek yerine hazır rende alındığı için büyük kâr kaybı var. Samsa için taze ıspanak yerine manavdan <strong>355 ₺/kg bebek ıspanak</strong> alınıyor (Hal'de taze ıspanak 35-40 ₺!).
              </p>
            </div>
            <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 space-y-1">
              <div class="font-bold text-amber-400">3. Aracı Distribütör Marjı</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                CNR Gıda ve Güleryüz Manav son dağıtıcıdır; GİMAT toptancılarından ve Toptancı Hali'nden aldıkları ürünlerin üzerine kapıya getirme, lojistik ve kâr marjı olarak <strong>%25 ila %50</strong> koyarlar.
              </p>
            </div>
          </div>
        </div>

        <!-- Ürün Bazlı Karşılaştırma & Tasarruf Tablosu -->
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <h4 class="text-sm font-bold text-white flex items-center gap-2">
              <i data-lucide="scale" class="w-4 h-4 text-emerald-400"></i>
              Kritik Ürünlerde Fiyat Karşılaştırması & Tasarruf Potansiyeli
            </h4>
            <span class="text-xs text-slate-400">Gerçek Fatura vs Ankara Toptancı Fiyatları</span>
          </div>

          <div class="overflow-x-auto rounded-xl border border-slate-800">
            <table class="w-full text-left text-xs border-collapse">
              <thead>
                <tr class="bg-slate-900/90 text-slate-300 border-b border-slate-800 text-[11px]">
                  <th class="py-2.5 px-3">Hammadde / Ürün</th>
                  <th class="py-2.5 px-3">Mevcut Alım Yeri</th>
                  <th class="py-2.5 px-3">Ödenen Birim Fiyat</th>
                  <th class="py-2.5 px-3 text-emerald-400">Önerilen 1. El Toptancı</th>
                  <th class="py-2.5 px-3 text-emerald-400">Hedef Toptan Fiyat</th>
                  <th class="py-2.5 px-3 text-right">Tahmini Tasarruf</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-800/60 font-mono text-[11px]">
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Mozarella Peyniri (4 ayda 39k ₺)</td>
                  <td class="py-2.5 px-3 text-slate-400">CNR Gıda (Ekici Rende 2kg)</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">436 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">GİMAT Süt Ürünleri (Blok Mozarella)</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">230 – 260 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%42 (16.500 ₺)</td>
                </tr>
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Ispanak (Samsa harcı için)</td>
                  <td class="py-2.5 px-3 text-slate-400">Güleryüz Manav (Paket 500g)</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">355 ₺ / kg (177 ₺/pk)</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">Ankara Hali / Metro Horeca (Dökme Kasa)</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">35 – 50 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%85 (7.200 ₺)</td>
                </tr>
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Tereyağı (Bakery & Kurabiye)</td>
                  <td class="py-2.5 px-3 text-slate-400">Migros (1 kg perakende)</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">474 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">GİMAT (10-25 kg Blok Horeca Tereyağı)</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">290 – 320 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%34 (4.500 ₺)</td>
                </tr>
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Fesleğen & Yeşillik (Pesto için)</td>
                  <td class="py-2.5 px-3 text-slate-400">Güleryüz Manav (Erüst paket)</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">790 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">Ankara Hali Erüst Bayisi / Metro Horeca</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">420 – 480 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%40 (4.600 ₺)</td>
                </tr>
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Krema %35 Yağlı (Pastacılık)</td>
                  <td class="py-2.5 px-3 text-slate-400">CNR Gıda (Sütaş 200 ml)</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">502 ₺ / Litre (100 ₺/kutu)</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">GİMAT / Koza Gıda (1 Litrelik Horeca)</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">140 – 170 ₺ / Litre</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%68 (3.700 ₺)</td>
                </tr>
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Füme Dana Et & Antrikot & Cotto</td>
                  <td class="py-2.5 px-3 text-slate-400">Fulya / Yayla-Türk & CNR</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">2.100 – 2.626 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">GİMAT Şarküteri Toptancıları / Ege Füme</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">1.500 – 1.850 ₺ / kg</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%28 (15.500 ₺)</td>
                </tr>
                <tr class="hover:bg-slate-800/30">
                  <td class="py-2.5 px-3 font-sans font-medium text-white">Çift Duvarlı Karton Bardak (14 oz)</td>
                  <td class="py-2.5 px-3 text-slate-400">Alfamarkt / CNR</td>
                  <td class="py-2.5 px-3 text-rose-400 font-bold">5,35 ₺ / Adet</td>
                  <td class="py-2.5 px-3 text-emerald-300 font-sans">Murpak Kağıtçılık / İvedik OSB Ambalaj</td>
                  <td class="py-2.5 px-3 text-emerald-400 font-bold">2,60 – 3,10 ₺ / Adet</td>
                  <td class="py-2.5 px-3 text-right text-emerald-400 font-bold font-sans">%45 (3.000 ₺)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Ankara İçi Somut Toptancı ve Tedarikçi Önerileri -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <!-- 1. Taze Sebze & Meyve -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2.5">
            <div class="flex items-center space-x-2 text-emerald-400 font-bold">
              <i data-lucide="carrot" class="w-4 h-4"></i>
              <span>1. Taze Sebze & Yeşillik</span>
            </div>
            <div class="text-[11px] text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong class="text-white">Ankara Toptancı Hali (Yenimahalle):</strong> Çankaya'ya 18 dk mesafede. Güleryüz Manav'a kıyasla <strong>%40-50 daha ucuzdur</strong>. Erüst yeşillik, çeri domates, avokado ve limon sandık bazında doğrudan hal komisyoncusundan alınmalıdır.</p>
              <p><strong class="text-white">Metro Grossmarket Horeca (Etlik / Batıkent):</strong> Vergi levhanızla işletme kartı çıkartın. Haftalık toplu sebze/yeşillik alımlarında hem fatura %100 nizami hem manavdan %30 daha uygundur.</p>
              <div class="pt-1 text-[10px] text-emerald-400 font-medium">💡 İpucu: Haldeki bir komisyoncuyla anlaşıp Salı ve Cuma sabahı dükkana teslim kasa servisi bağlayabilirsiniz.</div>
            </div>
          </div>

          <!-- 2. Süt & Peynir & Şarküteri -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2.5">
            <div class="flex items-center space-x-2 text-amber-400 font-bold">
              <i data-lucide="milk" class="w-4 h-4"></i>
              <span>2. Süt, Peynir & Şarküteri</span>
            </div>
            <div class="text-[11px] text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong class="text-white">GİMAT Toptancılar Sitesi (Macunköy):</strong> Türkiye'nin en büyük gıda toptancı üssü.</p>
              <p><strong class="text-white">Ergüven Süt / Güvenler Gıda (GİMAT):</strong> Faturalarınızda zaten adı geçiyor! CNR aradan çıkarılıp doğrudan Güvenler veya Akdeniz Süt Ürünleri'nden <strong>blok mozarella (rendelenmemiş), tost kaşarı ve 10 kg blok tereyağı</strong> toptan alınmalıdır.</p>
              <p><strong class="text-white">GİMAT Şarkütericiler Çarşısı:</strong> Namet, Polonez, Ege Füme yetkili toptancıları buradadır. Dana cotto ve sucuk %25 indirimli toptan koliyle alınır.</p>
            </div>
          </div>

          <!-- 3. Pastacılık & Çikolata -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2.5">
            <div class="flex items-center space-x-2 text-purple-400 font-bold">
              <i data-lucide="cake" class="w-4 h-4"></i>
              <span>3. Pastacılık & Belçika Çikolatası</span>
            </div>
            <div class="text-[11px] text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong class="text-white">Öztürk Pastacılık (GİMAT):</strong> Ankara'daki butik fırınların ve pastanelerin ana tedarikçisi. Callebaut / Belcolade Belçika kuvertür çikolatası, fındık/fıstık ezmesi, mascarpone, jöle ve pasta unları 1. el fiyattır.</p>
              <p><strong class="text-white">Koza Gıda Ankara (Ostim):</strong> Türkiye'nin en kaliteli Horeca gurme distribütörü. Lotus Biscoff ezmesi, Fransız tereyağı, Monin şuruplar ve profesyonel pastacılık kreması doğrudan teslim edilir.</p>
              <p><strong class="text-white">GİMAT Uncular Sitesi:</strong> Tellioğlu 50 kg pastalık çuval un (kg'ı 15 ₺'ye gelir, Pazarama'da 30 ₺ ödeniyor!).</p>
            </div>
          </div>

          <!-- 4. Ambalaj & Kahve Çekirdeği -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2.5">
            <div class="flex items-center space-x-2 text-blue-400 font-bold">
              <i data-lucide="coffee" class="w-4 h-4"></i>
              <span>4. Ambalaj & Nitelikli Kahve</span>
            </div>
            <div class="text-[11px] text-slate-300 space-y-1.5 leading-relaxed">
              <p><strong class="text-white">Murpak Kağıtçılık & İvedik Ambalaj:</strong> Çift duvarlı karton bardak, sızdırmaz kase ve kraft kutular koli bazlı alımda 5,35 ₺ yerine 2,80 ₺ bandına iner.</p>
              <p><strong class="text-white">Ankara Nitelikli Kahve Roastery'leri:</strong> Tchibo'yu İdefix'ten 661 ₺'ye tek paket almak yerine, Ankara yerel kavurucuları (Paper Roasting, Spada, Null, Gordion) veya Tchibo Horeca Bölge Müdürlüğü ile <strong>aylık 20-30 kg toptan çekirdek anlaşması</strong> yapılmalıdır. Kg maliyeti 400-450 ₺'ye düşerken kahve kalitesi ikiye katlanır.</p>
            </div>
          </div>
        </div>

        <!-- 3 Adımlı Uygulama Eylem Planı -->
        <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div class="flex items-center justify-between">
            <h4 class="text-xs font-bold text-white uppercase tracking-wider flex items-center gap-2">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400"></i>
              3 Adımlı Maliyet Düşürme Eylem Planı (Hemen Başlanabilir)
            </h4>
            <span class="text-[11px] text-emerald-400 font-bold">Hedef: Ayda ~20.000 ₺ Ekstra Kâr</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
            <div class="p-3 bg-slate-950/60 rounded-lg border border-slate-800/80 space-y-1">
              <div class="font-bold text-blue-300">Adım 1: Dükkana Endüstriyel Peynir Rendeleme Makinesi Alın (1 Kez)</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                CNR'dan hazır rendelenmiş mozarella almak yerine GİMAT'tan blok mozarella alın. Dükkanda kendiniz rendeleyerek sadece bu kalemde <strong>ayda 4.000 ₺</strong> net kârı kasada tutun.
              </p>
            </div>
            <div class="p-3 bg-slate-950/60 rounded-lg border border-slate-800/80 space-y-1">
              <div class="font-bold text-blue-300">Adım 2: Ankara Hali / Erüst ile Haftalık 2 Gün Sabit Dağıtım Bağlayın</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Güleryüz Manav'a günlük sipariş vermek yerine, haftada 2 gün (Salı - Cuma) Hal'den sandıkla dökme yeşillik ve sebze getirtin. Samsa için taze dökme ıspanak kullanarak <strong>ayda 5.000 ₺</strong> tasarruf edin.
              </p>
            </div>
            <div class="p-3 bg-slate-950/60 rounded-lg border border-slate-800/80 space-y-1">
              <div class="font-bold text-blue-300">Adım 3: GİMAT'ta Öztürk & Güvenler ile Aylık Cari Hesap Açın</div>
              <p class="text-slate-400 text-[11px] leading-relaxed">
                Migros ve internet pazar yerlerinden (Pazarama/Amazon) küçük küçük almak yerine, ayda 1 kez 50 kg un, 20 kg tereyağı ve pastacılık çikolatası koli bazlı kapıya sevkiyat anlaşması yapın.
              </p>
            </div>
          </div>
        </div>
      </div>

'''

if target_anchor in content:
    # insert before target_anchor
    new_content = content.replace(target_anchor, toptanci_section_html + '\n      ' + target_anchor)
    with open('build_portal.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("build_portal.py updated successfully with Toptancı Rehberi!")
else:
    print("target_anchor not found in build_portal.py!")

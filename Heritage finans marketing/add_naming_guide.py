# -*- coding: utf-8 -*-
"""
Adds the Product Naming Audit & Recommendations Table into Tab 3 (Pazarlama & Menü Analitiği)
"""

with open("build_portal.py", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find </section> of tab-marketing
idx_marketing = content.find('id="tab-marketing"')
if idx_marketing == -1:
    print("Could not find tab-marketing")
    exit(1)

idx_close = content.find('</section>', idx_marketing)
if idx_close == -1:
    print("Could not find </section> of tab-marketing")
    exit(1)

naming_guide_html = """
      <!-- Section 4: Ürün İsimlendirme & Menü Terminolojisi Denetimi -->
      <div class="glass-card rounded-2xl p-6 border border-amber-500/30 bg-slate-900/90 space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center">
              <i data-lucide="tag" class="w-5 h-5 text-amber-400"></i>
            </div>
            <div>
              <h3 class="text-base font-bold text-white">Ürün İsimlendirme & Menü Terminolojisi Denetimi (Önerilen İsim Değişiklikleri)</h3>
              <p class="text-xs text-slate-400 mt-0.5">Bazı ürünlerinizin az satmasının sebebi ürün değil, isminin ne sunduğunu anlatamamasıdır</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs bg-amber-500/10 text-amber-400 font-bold border border-amber-500/20 self-start sm:self-auto">İsim Reformu</span>
        </div>

        <div class="overflow-x-auto custom-scrollbar">
          <table class="w-full text-left text-xs whitespace-nowrap">
            <thead>
              <tr class="bg-slate-950/80 text-slate-400 font-semibold border-b border-slate-800">
                <th class="py-3 px-3">Mevcut İsim (Menü/Sistem)</th>
                <th class="py-3 px-3 text-rose-400">Neden Sorunlu? (Müşteri Algısı)</th>
                <th class="py-3 px-3 text-emerald-400">Önerilen Yeni & İştah Kabartan İsim</th>
                <th class="py-3 px-3 text-amber-400">Beklenen Etki & Satış Artışı</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 font-medium">
              <!-- Item 1: Bumble Bee -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Bumble Bee (₺250)
                  <span class="block text-[10px] text-rose-400 font-normal">4 ayda sadece 3 adet!</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Müşteri ne olduğunu anlamıyor. Sinemadaki 'Transformers' arısını çağrıştırıyor; portakal suyu ve espresso olduğu menüde yazmıyor.">
                  Ne olduğu meçhul. Portakal suyu + espresso olduğu anlaşılmıyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Orange Iced Americano (Portakallı Soğuk Kahve)
                </td>
                <td class="py-3 px-3 text-slate-300">
                  <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 font-semibold">Satışta 10x Artış</span> (Instagram trendi)
                </td>
              </tr>

              <!-- Item 2: Coffee Glacé -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Coffee Glacé (₺250)
                  <span class="block text-[10px] text-rose-400 font-normal">4 ayda sadece 4 adet!</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Fransızca 'Glacé' buzlu demek. Müşteri buzlu filtre kahve mi yoksa dondurma mı anlamıyor.">
                  Fransızca terim kafa karıştırıyor; buzlu kahve sanılıyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  İtalyan Artisan Affogato (Dondurmalı Sıcak Espresso)
                </td>
                <td class="py-3 px-3 text-slate-300">
                  <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-300 font-semibold">%85 Kâr Marjı</span> ile tatlı/kahve eşlikçisi
                </td>
              </tr>

              <!-- Item 3: Gusto 1, 2, 3 -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Heritage Gusto 1, 2, 3 (₺350 – ₺370)
                  <span class="block text-[10px] text-slate-400 font-normal">Sandviç Çeşitleri</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Numara vermek müşteride kafa karışıklığı yaratır. Müşteri 'Gusto 1 neydi, 2 neydi?' diye garsona sormak zorunda kalıyor.">
                  Numara sistemi müşteriye lezzeti hissettirmiyor, siparişi yavaşlatıyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Gusto 1 ➔ Köz Patlıcan & Dana Cotto Ciabatta<br>
                  Gusto 2 ➔ Avokado & Mozzarella Gusto Ciabatta<br>
                  Gusto 3 ➔ Şefin İmzası Gurme Ciabatta
                </td>
                <td class="py-3 px-3 text-slate-300">
                  "Avokado" ve "Dana Cotto" kelimeleri doğrudan siparişi tetikler.
                </td>
              </tr>

              <!-- Item 4: Tart -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Tart (₺290)
                  <span class="block text-[10px] text-slate-400 font-normal">Tatlılar</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Sadece 'Tart' yazılmış. Oysa içinde zengin ekşi vişne dolgusu ve tereyağlı altın crumble var.">
                  Sadece "Tart" yazmak ürünü pastane bisküvisi gibi sıradanlaştırıyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Vişneli Crumble Tart (Belçika Kremalı)
                </td>
                <td class="py-3 px-3 text-slate-300">
                  "Vişne" ve "Crumble" iştah açar, kadın kitlede siparişi ikiye katlar.
                </td>
              </tr>

              <!-- Item 5: Cheesecake -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Cheesecake (₺290)
                  <span class="block text-[10px] text-rose-400 font-normal">4 ayda sadece 6 adet!</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Başlıkta sadece Cheesecake yazıyor, Lotus Biscoff bisküvi tabanı alttaki küçük yazıda gizli kalıyor.">
                  Başlık çok sönük. Lotus Biscoff'un gücü başlıkta görünmüyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Karamelli Lotus Biscoff Cheesecake
                </td>
                <td class="py-3 px-3 text-slate-300">
                  Lotus Biscoff ismi tek başına sipariş mıknatısıdır.
                </td>
              </tr>

              <!-- Item 6: Dilim Kek -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Dilim Kek (₺100)
                  <span class="block text-[10px] text-slate-400 font-normal">Muhasebedeki İsim</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="İngilizce menüde Carrot Cake yazıyor ama Türkçe listede 'Dilim Kek' geçiyor. Bakkal keki hissi veriyor.">
                  "Dilim kek" ambalajlı fabrika keki hissi yaratıyor; fırın artisanlığı yok.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Cevizli & Tarçınlı Havuçlu Fırın Keki (Carrot Cake)
                </td>
                <td class="py-3 px-3 text-slate-300">
                  Çay ve filtre kahve yanına en hızlı çapraz satılan ürün olur.
                </td>
              </tr>

              <!-- Item 7: Shu Tatlısı -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Choux Pastry / Shu Tatlısı (₺200)
                  <span class="block text-[10px] text-slate-400 font-normal">Fransız Şu</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Müşterilerin bir kısmı 'Şu tatlısı' nedir bilmiyor; Profiterol veya ekler zannediyor.">
                  "Şu tatlısı" ismi müşteride soru işareti yaratıyor, profiterolden farkı bilinmiyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Kıtır Craquelin Choux (Belçika Çikolatalı Fransız Şu)
                </td>
                <td class="py-3 px-3 text-slate-300">
                  Fransız patisserie prestiji kazandırır, 200 ₺'yi çok uygun hissettirir.
                </td>
              </tr>

              <!-- Item 8: Sade Soğuk Sandviç -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Simple Cold Sandwich / Sade Soğuk (₺200)
                  <span class="block text-[10px] text-rose-400 font-normal">11 adet</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="'Sade Soğuk' kelimesi iştah kapatıcı ve ucuz büfe sandviçi hissi veriyor.">
                  "Sade soğuk" kelimesi iştah kaçırıyor, kuru ekmek algısı yaratıyor.
                </td>
                <td class="py-3 px-3 font-bold text-rose-400">
                  MENÜDEN KALDIRIN (veya İtalyan Gouda & Pesto Ciabatta)
                </td>
                <td class="py-3 px-3 text-slate-300">
                  Bayatlama ve hammadde israfını sıfırlar.
                </td>
              </tr>

              <!-- Item 9: Tost İsimleri -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Kashar Toast / Kaşarlı Tost (₺220)
                  <span class="block text-[10px] text-slate-400 font-normal">Tostlar</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="Sıradan tost ekmeğine kaşar konmuş gibi duruyor. Oysa el yapımı focaccia ekmeğiniz ve özel sosunuz var!">
                  Ev yapımı fırın focaccia ekmeğiniz ve özel sosunuz isimde gizli kalıyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Özel Salça Soslu Focaccia Kaşarlı Tost
                </td>
                <td class="py-3 px-3 text-slate-300">
                  Sıradan büfe tostu algısından çıkarıp 220 ₺'yi gurme değere taşır.
                </td>
              </tr>

              <!-- Item 10: Yumurta Tabakları -->
              <tr class="hover:bg-slate-800/30 transition">
                <td class="py-3 px-3 font-bold text-slate-200">
                  Haşlama Yumurta (₺70) / Omletli Tabak (₺80)
                  <span class="block text-[10px] text-slate-400 font-normal">Kahvaltı</span>
                </td>
                <td class="py-3 px-3 text-slate-300 max-w-[240px] truncate" title="'Haşlama yumurta' kafe menüsü için çok zayıf bir tabir.">
                  "Haşlama yumurta" tabiri kafe menüsü için zayıf ve kuru duruyor.
                </td>
                <td class="py-3 px-3 font-bold text-emerald-400">
                  Heritage Fırın Focaccia & Haşlanmış Yumurta Tabağı
                </td>
                <td class="py-3 px-3 text-slate-300">
                  Yanına zeytin ve yeşillik eklenerek tek yumurtadan gurme tabak üretir.
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="p-3 bg-amber-500/10 border border-amber-500/20 rounded-xl text-xs text-amber-300 leading-relaxed">
          <strong>Altın Kural:</strong> Menünüzdeki ürünün adı sadece bir etiket değildir; müşterinin o ürünü ağzında hayal etmesini sağlayan ilk lokmadır. İsimde <em>"Focaccia", "Belçika Çikolatası", "Lotus Biscoff", "Köz Patlıcan", "Dana Cotto"</em> gibi duyusal ve iştah kabartan malzeme isimleri mutlaka yer almalıdır.
        </div>
      </div>
"""

# Insert before </section> of tab-marketing
updated_content = content[:idx_close] + naming_guide_html + "\n    " + content[idx_close:]

with open("build_portal.py", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("Updated build_portal.py with Naming Guide!")

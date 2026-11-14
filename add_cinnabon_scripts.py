import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. HTML Card Section for Cinnabon
cinnabon_html = '''
      <!-- Cinnabon (Tarçınlı Rulo) Özel Sosyal Medya & Reklam Senaryoları -->
      <div class="glass-card rounded-2xl p-6 border border-amber-500/30 bg-gradient-to-r from-slate-900 via-amber-950/20 to-slate-900 space-y-5">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center shrink-0">
              <i data-lucide="flame" class="w-5 h-5 text-amber-400"></i>
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h3 class="text-base font-bold text-white">Cinnabon (Artisan Tarçınlı Rulo) Özel Video & Reklam Senaryoları</h3>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Trend Lideri</span>
              </div>
              <p class="text-xs text-slate-400 mt-0.5">Ankara Çankaya'da Cinnabon fırtınası estirecek, Meta & TikTok Ads hazır 5 çekim kurgusu</p>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-emerald-300 bg-emerald-500/10 px-3 py-1 rounded-lg border border-emerald-500/20 font-medium">
              Yüksek Dönüşümlü Reels & TikTok
            </span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          
          <!-- Cinnabon 1: ASMR Glaze -->
          <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-500/15 text-amber-400 border border-amber-500/30">Cinnabon 1 · Viral Glaze ASMR</span>
                <span class="text-[11px] text-slate-400">11 sn</span>
              </div>
              <h4 class="text-sm font-bold text-white">"Dumanı Üstünde Glaze Şelalesi"</h4>
              <div class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                <p><span class="text-amber-400 font-semibold">Hook (0-3 sn):</span> Fırından yeni çıkmış, dumanı tüten sıcacık Cinnabon'un üzerine fırıncı kepçesiyle bembeyaz, kıvamlı vanilyalı cream cheese glaze dökülür; krema kıvrımlara eriyerek sızar.</p>
                <p><span class="text-blue-400 font-semibold">Görsel & ASMR:</span> Çatal tam orta göbeğe batırılır, en yumuşak spiral katman sıcacık dumanla ayrılır. Net fırın & krema ASMR sesleri.</p>
                <p><span class="text-rose-400 font-semibold">Ekran Metni:</span> "Ankara'da bu kokuya hayır diyebilecek biri var mı? 🤤"</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Kaydet, ilk Cinnabon borcu olan arkadaşına gönder!"</p>
              </div>
            </div>
            <button onclick="copyScript('cinnabon_1')" class="mt-4 w-full py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center gap-1.5 cursor-pointer">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
              <span>Senaryoyu Kopyala</span>
            </button>
          </div>

          <!-- Cinnabon 2: POV Şehir Rehberi -->
          <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/15 text-blue-400 border border-blue-500/30">Cinnabon 2 · POV Şehir Rehberi</span>
                <span class="text-[11px] text-slate-400">16 sn</span>
              </div>
              <h4 class="text-sm font-bold text-white">"Ankara'da Gerçek Cinnabon Nerede Yenir?"</h4>
              <div class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                <p><span class="text-amber-400 font-semibold">Hook (0-3 sn):</span> "Ankara'da canınız deli gibi sıcacık Cinnabon çektiğinde zincir mağazalardaki donuk ürünler yerine nereye gideceksiniz?"</p>
                <p><span class="text-blue-400 font-semibold">Görsel:</span> Reşit Galip'ten kafeye giriş, taş fırından tepsisi yeni çıkan Cinnabon, yanına taze Flat White kahve sunumu.</p>
                <p><span class="text-rose-400 font-semibold">Seslendirme:</span> "Fabrikasyon değil, her sabah el açması tereyağlı mayalı hamurla sıfırdan sarılıyor!"</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Bugün 18:00'e kadar bekliyoruz veya Trendyol Go'dan kapına söyle! 📍 Çankaya No:18"</p>
              </div>
            </div>
            <button onclick="copyScript('cinnabon_2')" class="mt-4 w-full py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center gap-1.5 cursor-pointer">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
              <span>Senaryoyu Kopyala</span>
            </button>
          </div>

          <!-- Cinnabon 3: Mutfak Sırrı BTS -->
          <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-purple-500/15 text-purple-400 border border-purple-500/30">Cinnabon 3 · Mutfak Sırrı BTS</span>
                <span class="text-[11px] text-slate-400">18 sn</span>
              </div>
              <h4 class="text-sm font-bold text-white">"1 Ruloda Neler Var? (Tatmin Edici Kesim)"</h4>
              <div class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                <p><span class="text-amber-400 font-semibold">Hook (0-3 sn):</span> Mayalanmış puf hamurun tezgaha vuruluşu ve un bulutu. Merdaneyle tül gibi açılış.</p>
                <p><span class="text-blue-400 font-semibold">Adımlar:</span> Spatulayla bol gerçek tereyağı, esmer şeker ve Seylan tarçını yağmuru, dikiş ipiyle pürüzsüz kesim anı!</p>
                <p><span class="text-rose-400 font-semibold">Ekran Metni:</span> "Margarin yok ❌ Donuk hazır hamur yok ❌ Sadece tereyağı, Seylan tarçını ve aşk. ❤️"</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Bu tepsiyi kiminle bitirirsin? Etiketle!"</p>
              </div>
            </div>
            <button onclick="copyScript('cinnabon_3')" class="mt-4 w-full py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center gap-1.5 cursor-pointer">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
              <span>Senaryoyu Kopyala</span>
            </button>
          </div>

          <!-- Cinnabon 4: Duygusal Stres Savar -->
          <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-pink-500/15 text-pink-400 border border-pink-500/30">Cinnabon 4 · Duygusal Stres Savar</span>
                <span class="text-[11px] text-slate-400">14 sn</span>
              </div>
              <h4 class="text-sm font-bold text-white">"Günün Stresini Unutturan İlk Çatal"</h4>
              <div class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                <p><span class="text-amber-400 font-semibold">Hook (0-3 sn):</span> Yağmurlu/soğuk Ankara sokak görüntüsü, ardından dükkanın sıcak atmosferine ve dumanı tüten Cinnabon'a geçiş.</p>
                <p><span class="text-blue-400 font-semibold">Görsel:</span> Masada iki fincan kahve; ortadaki sıcacık Cinnabon'un en yumuşak kremalı orta göbeğinden büyük bir parça koparılıp sevdiğine uzatılır.</p>
                <p><span class="text-rose-400 font-semibold">Seslendirme:</span> "Bazen ihtiyacın olan tek şey, sıcacık bir fincan kahve ve tarçın kokusunun getirdiği o küçük huzur anıdır."</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Kendine bugün küçük bir ödül ver. Saat 18:00'e kadar bekliyoruz."</p>
              </div>
            </div>
            <button onclick="copyScript('cinnabon_4')" class="mt-4 w-full py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center gap-1.5 cursor-pointer">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
              <span>Senaryoyu Kopyala</span>
            </button>
          </div>

          <!-- Cinnabon 5: FOMO & Al-Götür -->
          <div class="bg-slate-900/90 rounded-xl p-4 border border-slate-800 flex flex-col justify-between hover:border-amber-500/40 transition">
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-red-500/15 text-red-400 border border-red-500/30">Cinnabon 5 · FOMO & Al-Götür</span>
                <span class="text-[11px] text-slate-400">12 sn</span>
              </div>
              <h4 class="text-sm font-bold text-white">"Günde Sadece 3 Tepsi Çıkıyor!"</h4>
              <div class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
                <p><span class="text-amber-400 font-semibold">Hook (0-3 sn):</span> Fırın saati 11:30'u gösterir. Fırın kapağı açılır, dumanlar yükselir. Ekran yazısı: "DİKKAT: Günde sadece 3 tepsi çıkıyor ve 1 saatte tükeniyor!"</p>
                <p><span class="text-blue-400 font-semibold">Görsel:</span> Sıcacık rulolar şık Heritage paket kutusuna yerleştirilir. "Mikrodalgada 15 saniye ısıt, kreması fırından yeni çıkmış gibi erisin!"</p>
                <p><span class="text-rose-400 font-semibold">Hedef Kitle:</span> Çankaya ofisleri, büyükelçilikler ve evde çalışanlar.</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Tükenmeden Şimdi Sipariş Ver! (Trendyol Go & Al-Götür) / Kapanış: 18:00"</p>
              </div>
            </div>
            <button onclick="copyScript('cinnabon_5')" class="mt-4 w-full py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center gap-1.5 cursor-pointer">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
              <span>Senaryoyu Kopyala</span>
            </button>
          </div>

        </div>
      </div>
'''

# We insert this after the Video 5 card closing tag
# Let's find copyScript(5) button container
target_str = 'onclick="copyScript(5)" class="mt-4 w-full py-2 text-xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center gap-1.5">\n              <i data-lucide="copy" class="w-3.5 h-3.5"></i>\n              <span>Senaryoyu Kopyala</span>\n            </button>\n          </div>\n\n        </div>\n      </div>'

if target_str in code:
    code = code.replace(target_str, target_str + '\n\n' + cinnabon_html, 1)
    print("Inserted Cinnabon HTML cards successfully!")
else:
    # Try finding with flexible whitespace
    pos = code.find('copyScript(5)')
    if pos != -1:
        end_pos = code.find('</div>\n      </div>', pos) + 18
        code = code[:end_pos] + '\n\n' + cinnabon_html + code[end_pos:]
        print("Inserted Cinnabon HTML cards via offset!")
    else:
        print("Could not find insertion position for Cinnabon HTML!")

# 2. Update copyScript in JavaScript to support cinnabon_1 to cinnabon_5
old_copy_fn = '''    function copyScript(id) {
      const scripts = {
        1: `Video 1: Çikolata Şelalesi & New York Cookie\\nHook: Ankara'da gerçek Belçika çikolatasıyla yapılan kurabiyeyi gördünüz mü?\\nGörsel: Kurabiye ikiye ayrılır, içinden akışkan sıcak fıstık/Lotus kreması süzülür.\\nCTA: Tatlı krizine gireceğin arkadaşına gönder! 📍 Reşit Galip No:18 Çankaya`,
        2: `Video 2: Sabah 07:00'de Çankaya Fırını\\nHook: Güne bu kokuyla başlamak isteyenler Ankara'da toplanıyor...\\nGörsel: Focaccia hamuruna zeytinyağı ve biberiye basılışı, taş fırından çıkışı.\\nCTA: Taze fırından çıktığında yakalamak için hemen uğra!`,
        3: `Video 3: Pesto Soslu Çıtır Focaccia Tost\\nHook: Böyle uzayan bir peyniri daha önce Ankara'da görmediniz!\\nGörsel: Çıtır kızarmış focaccia tost ikiye kesilir ve uzatılır.\\nCTA: Tost sevdalısı arkadaşını etiketle!`,
        4: `Video 4: 60 TL'ye El Açması Çıtır Samsa!\\nHook: Ankara'da 60 TL'ye böyle bir çıtırlık kaldı mı?\\nGörsel: Samsa tül gibi açılır, tereyağı sürülür, fırından çıkar.\\nCTA: Hemen kaydet, çayın yanında mutlaka dene!`,
        5: `Video 5: Çankaya'nın Saklı Çalışma Cenneti\\nHook: Ankara'da laptopunu kapıp saatlerce çalışabileceğin o mekan...\\nGörsel: Laptop, sıcak Americano, dilimlenmiş Tiramisu ve sakin müzik.\\nCTA: Kaydet, bir gün mutlaka lazım olacak!`
      };
      navigator.clipboard.writeText(scripts[id]).then(() => {
        alert('Senaryo panoya kopyalandı!');
      });
    }'''

new_copy_fn = '''    function copyScript(id) {
      const scripts = {
        1: `Video 1: Çikolata Şelalesi & New York Cookie\\nHook: Ankara'da gerçek Belçika çikolatasıyla yapılan kurabiyeyi gördünüz mü?\\nGörsel: Kurabiye ikiye ayrılır, içinden akışkan sıcak fıstık/Lotus kreması süzülür.\\nCTA: Tatlı krizine gireceğin arkadaşına gönder! 📍 Reşit Galip No:18 Çankaya`,
        2: `Video 2: Sabah 07:00'de Çankaya Fırını\\nHook: Güne bu kokuyla başlamak isteyenler Ankara'da toplanıyor...\\nGörsel: Focaccia hamuruna zeytinyağı ve biberiye basılışı, taş fırından çıkışı.\\nCTA: Taze fırından çıktığında yakalamak için hemen uğra!`,
        3: `Video 3: Pesto Soslu Çıtır Focaccia Tost\\nHook: Böyle uzayan bir peyniri daha önce Ankara'da görmediniz!\\nGörsel: Çıtır kızarmış focaccia tost ikiye kesilir ve uzatılır.\\nCTA: Tost sevdalısı arkadaşını etiketle!`,
        4: `Video 4: 60 TL'ye El Açması Çıtır Samsa!\\nHook: Ankara'da 60 TL'ye böyle bir çıtırlık kaldı mı?\\nGörsel: Samsa tül gibi açılır, tereyağı sürülür, fırından çıkar.\\nCTA: Hemen kaydet, çayın yanında mutlaka dene!`,
        5: `Video 5: Çankaya'nın Saklı Çalışma Cenneti\\nHook: Ankara'da laptopunu kapıp saatlerce çalışabileceğin o mekan...\\nGörsel: Laptop, sıcak Americano, dilimlenmiş Tiramisu ve sakin müzik.\\nCTA: Kaydet, bir gün mutlaka lazım olacak!`,
        'cinnabon_1': `Cinnabon Video 1: Dumanı Üstünde Glaze Şelalesi (ASMR)\\nHook: Ankara'da bu kokuya hayır diyebilecek biri var mı? 🤤\\nGörsel: Fırından yeni çıkmış sıcak Cinnabon tepsisine bol labneli vanilyalı glaze sos dökülür, kıvrımlarına sızar. Çatal orta göbeğe batırılır.\\nCTA: Kaydet, ilk Cinnabon borcu olan arkadaşına gönder! 📍 Reşit Galip No:18 Çankaya`,
        'cinnabon_2': `Cinnabon Video 2: Ankara'da Gerçek Cinnabon Nerede Yenir? (POV)\\nHook: Ankara'da canınız deli gibi sıcacık Cinnabon çektiğinde zincir mağazalardaki donuk ürünler yerine nereye gideceksiniz?\\nGörsel: Çankaya sokaklarından Heritage vitrinine giriş. Taş fırından taze çıkan Cinnabon ve taze çekilmiş kahve.\\nCTA: Bugün 18:00'e kadar bekliyoruz veya Trendyol Go'dan kapına söyle! 📍 Heritage Cafe`,
        'cinnabon_3': `Cinnabon Video 3: 1 Ruloda Neler Var? (Behind The Scenes)\\nHook: Donuk hamur yok, margarin yok! Sadece saf tereyağı ve Seylan tarçını.\\nGörsel: Mayalı hamurun açılışı, tereyağı sürülüşü, tarçın serpiştirilmesi, dikiş ipiyle pürüzsüz kesim anı ve fırından çıktığı gibi glaze dökülüşü.\\nCTA: Bu tepsiyi kiminle bitirirsin? Etiketle!`,
        'cinnabon_4': `Cinnabon Video 4: Günün Stresini Unutturan İlk Çatal (Duygusal)\\nHook: Bugün günün biraz stresli mi geçti?...\\nGörsel: Masada iki kahve; ortadaki ılık Cinnabon'un en yumuşak, kremalı göbeğinden çatal darbesiyle büyük bir lokma alınıp uzatılır.\\nCTA: Kendine bugün küçük bir ödül ver. Saat 18:00'e kadar bekliyoruz. ☕✨`,
        'cinnabon_5': `Cinnabon Video 5: Günde Sadece 3 Tepsi Çıkıyor! (FOMO / Paket Servis)\\nHook: DİKKAT: Günde sadece 3 tepsi çıkıyor ve 1 saatte tükeniyor!\\nGörsel: 11:30 fırın dumanı, paket kutusuna yerleştirilen sıcacık Cinnabon. "Mikrodalgada 15 sn ısıt, ilk anki gibi erisin!"\\nCTA: Tükenmeden Şimdi Sipariş Ver! (Trendyol Go & Al-Götür) / Kapanış: 18:00`
      };
      if (scripts[id]) {
        navigator.clipboard.writeText(scripts[id]).then(() => {
          alert('Cinnabon senaryosu panoya kopyalandı!');
        });
      }
    }'''

if old_copy_fn in code:
    code = code.replace(old_copy_fn, new_copy_fn, 1)
    print("Updated copyScript function with Cinnabon scripts!")
else:
    print("old_copy_fn not matched directly, checking regex...")
    pos = code.find('function copyScript')
    end_pos = code.find('navigator.clipboard.writeText', pos)
    end_pos2 = code.find('}', end_pos) + 9
    code = code[:pos] + new_copy_fn + code[end_pos2:]
    print("Replaced copyScript via offset!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_portal.py written successfully!")

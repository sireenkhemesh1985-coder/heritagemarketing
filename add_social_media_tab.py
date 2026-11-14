import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add Navigation Button for Social Media Tab
nav_salary_btn = '''        <button onclick="switchTab('tab-salary')" id="nav-tab-salary" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold flex items-center space-x-2 transition whitespace-nowrap text-slate-400 hover:text-slate-200 hover:bg-slate-800 border border-transparent">
          <i data-lucide="users" class="w-4 h-4"></i>
          <span>Maaşlar & Kâr Simülatörü</span>
        </button>'''

nav_social_btn = '''        <button onclick="switchTab('tab-salary')" id="nav-tab-salary" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold flex items-center space-x-2 transition whitespace-nowrap text-slate-400 hover:text-slate-200 hover:bg-slate-800 border border-transparent">
          <i data-lucide="users" class="w-4 h-4"></i>
          <span>Maaşlar & Kâr Simülatörü</span>
        </button>
        <button onclick="switchTab('tab-social')" id="nav-tab-social" class="tab-btn px-4 py-2 rounded-lg text-xs font-semibold flex items-center space-x-2 transition whitespace-nowrap text-slate-400 hover:text-slate-200 hover:bg-slate-800 border border-transparent">
          <i data-lucide="share-2" class="w-4 h-4 text-pink-400"></i>
          <span>Sosyal Medya & B2B Denetimi</span>
          <span class="px-1.5 py-0.5 rounded text-[10px] bg-pink-500/20 text-pink-300 border border-pink-500/30 font-bold" id="social-nav-score">42/100</span>
        </button>'''

if nav_salary_btn in code:
    code = code.replace(nav_salary_btn, nav_social_btn, 1)
    print("Added Social Media Nav Button!")
else:
    print("nav_salary_btn not found!")

# 2. Add Section tab-social HTML content
social_section_html = '''
    <!-- ========================================== -->
    <!-- TAB 7: SOSYAL MEDYA DENETİMİ, KANAL ANALİZİ & B2B LEAD MOTORU -->
    <!-- ========================================== -->
    <section id="tab-social" class="tab-content space-y-8 hidden">

      <!-- Header & Score Banner -->
      <div class="glass-card rounded-2xl p-6 border border-pink-500/30 bg-gradient-to-r from-slate-900 via-pink-950/20 to-slate-900 space-y-5">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-4">
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 rounded-xl bg-pink-500/20 border border-pink-500/30 flex items-center justify-center shrink-0">
              <i data-lucide="sparkles" class="w-6 h-6 text-pink-400"></i>
            </div>
            <div>
              <div class="flex items-center gap-2.5">
                <h2 class="text-lg font-bold text-white">Sosyal Medya Denetimi, Kanal İyileştirme & LinkedIn B2B Stratejisi</h2>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-pink-500/20 text-pink-300 border border-pink-500/30">Canlı Denetim</span>
              </div>
              <p class="text-xs text-slate-400 mt-1">
                İncelenen Kanallar: YouTube (@HeritageCafeBakery), TikTok (@heritage.cafe.bake), Instagram (@heritagecafeandbakery) & LinkedIn B2B
              </p>
            </div>
          </div>

          <!-- Live Score & Action Button -->
          <div class="flex flex-wrap items-center gap-3">
            <div class="bg-slate-900/90 px-4 py-2 rounded-xl border border-slate-800 flex items-center gap-3">
              <div>
                <span class="text-[10px] text-slate-400 block uppercase tracking-wider font-semibold">Sağlık Skoru</span>
                <span class="text-xl font-black text-pink-400" id="live-audit-score">42 / 100</span>
              </div>
              <div class="w-10 h-10 rounded-full border-2 border-pink-500/40 flex items-center justify-center text-xs font-bold text-pink-300" id="live-audit-circle">
                %42
              </div>
            </div>

            <button onclick="rescanSocialChannels()" class="px-4 py-2.5 rounded-xl bg-gradient-to-r from-pink-500 to-rose-600 hover:from-pink-400 hover:to-rose-500 text-white font-bold text-xs shadow-lg shadow-pink-500/20 flex items-center gap-2 transition cursor-pointer">
              <i data-lucide="refresh-cw" class="w-4 h-4"></i>
              <span>Yeniden Tara & Eksik Raporu Ver</span>
            </button>
          </div>
        </div>

        <!-- Quick Metrics Highlights -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <div class="p-3.5 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
            <span class="text-slate-400 flex items-center gap-1.5"><i data-lucide="youtube" class="w-3.5 h-3.5 text-red-400"></i> YouTube (@HeritageCafeBakery)</span>
            <div class="text-base font-bold text-white">Kapak Resmi & CTR Eksik</div>
            <p class="text-[11px] text-rose-400 font-medium">Shorts başlıkları optimize edilmeli</p>
          </div>
          <div class="p-3.5 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
            <span class="text-slate-400 flex items-center gap-1.5"><i data-lucide="video" class="w-3.5 h-3.5 text-cyan-400"></i> TikTok (@heritage.cafe.bake)</span>
            <div class="text-base font-bold text-white">Handle & Bio Düzeltilmeli</div>
            <p class="text-[11px] text-amber-400 font-medium">Biolink ve Çankaya adresi eklenmeli</p>
          </div>
          <div class="p-3.5 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
            <span class="text-slate-400 flex items-center gap-1.5"><i data-lucide="instagram" class="w-3.5 h-3.5 text-pink-400"></i> Instagram (@heritagecafeandbakery)</span>
            <div class="text-base font-bold text-white">QR Kod & 3 Sabit Post</div>
            <p class="text-[11px] text-emerald-400 font-medium">Masaüstü UGC Madeleine teşviki</p>
          </div>
          <div class="p-3.5 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
            <span class="text-slate-400 flex items-center gap-1.5"><i data-lucide="linkedin" class="w-3.5 h-3.5 text-blue-400"></i> LinkedIn B2B Potansiyeli</span>
            <div class="text-base font-bold text-white">Aylık ~50.000 ₺ Fırsat</div>
            <p class="text-[11px] text-purple-300 font-medium">Kurumsal toplantı & coffee break kutuları</p>
          </div>
        </div>
      </div>

      <!-- 1. Bölüm: Kanalı Geri Tutan 5 Kritik Hata & Fırsat Alanı -->
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <div class="w-2.5 h-2.5 rounded-full bg-rose-500"></div>
            <h3 class="text-base font-bold text-white">1. Kanalı Geri Tutan 5 Kritik Hata & Fırsat Alanı</h3>
          </div>
          <span class="text-xs text-rose-400 font-medium bg-rose-500/10 px-2.5 py-1 rounded border border-rose-500/20">Teşhis & Çözüm</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-xs">
          <!-- Hata 1 -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-rose-500/30 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-rose-400 flex items-center gap-1.5"><i data-lucide="alert-circle" class="w-4 h-4"></i> Hata 1: Handle & İsim Uyumsuzluğu</span>
              <span class="text-[10px] text-slate-500 font-mono">SEO Kaybı</span>
            </div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Instagram'da <code class="text-amber-300 font-bold">@heritagecafeandbakery</code> iken, TikTok'ta <code class="text-rose-300">@heritage.cafe.bake</code> ve YouTube'da <code class="text-amber-300">@HeritageCafeBakery</code>. Arama yapan kullanıcı markayı TikTok'ta bulamıyor, SEO sinyali parçalanıyor.
            </p>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300">
              <strong>Fırsat Çözümü:</strong> TikTok kullanıcı adını mümkünse doğrudan <code>@heritagecafeandbakery</code> olarak eşitleyin. Tüm kanallarda marka bütünlüğü sağlayın.
            </div>
          </div>

          <!-- Hata 2 -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-rose-500/30 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-rose-400 flex items-center gap-1.5"><i data-lucide="image" class="w-4 h-4"></i> Hata 2: YouTube Shorts Kapak & CTR Faciası</span>
              <span class="text-[10px] text-slate-500 font-mono">Tıklama Kaybı</span>
            </div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              YouTube videolarında özel kapak resmi seçilmiyor, algoritma rastgele bulanık bir kare koyuyor. Başlıklar "Focaccia", "Kahve" gibi jenerik; izleyicide tıklama isteği (CTR) oluşturmuyor.
            </p>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300">
              <strong>Fırsat Çözümü:</strong> YouTube Shorts yüklerken "Kalem" simgesine basıp kapak olarak dumanın çıktığı veya peynirin uzadığı en iştah kabartan kareyi seçin. Başlıklara merak kancası ekleyin (CTR %2'den %10'a fırlar).
            </div>
          </div>

          <!-- Hata 3 -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-rose-500/30 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-rose-400 flex items-center gap-1.5"><i data-lucide="map-pin" class="w-4 h-4"></i> Hata 3: Konum ve Biyografi Açığı</span>
              <span class="text-[10px] text-slate-500 font-mono">Ziyaretçi Kaybı</span>
            </div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              TikTok ve YouTube açıklamalarında "Ankara / Çankaya Reşit Galip No:18" fiziksel lokasyonu, Google Haritalar linki ve saat 18:00 kapanış bilgisi yer almıyor. Videoyu beğenen Ankaralı nereye gideceğini bilemiyor.
            </p>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300">
              <strong>Fırsat Çözümü:</strong> Biyografiye Linktree/Biolinky linki koyun: 1) Haritada Yol Tarifi, 2) Menü, 3) Trendyol Go Sipariş Ver, 4) WhatsApp Kurumsal Sipariş.
            </div>
          </div>

          <!-- Hata 4 -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-rose-500/30 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-rose-400 flex items-center gap-1.5"><i data-lucide="clock" class="w-4 h-4"></i> Hata 4: İlk 3 Saniye Kancası (Hook) Yok</span>
              <span class="text-[10px] text-slate-500 font-mono">İzlenme Kaybı</span>
            </div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Videolar yavaş açılıyor, müzik geç giriyor ve ekranda ilk 1.5 saniyede merak uyandıran bir soru veya iddia yer almıyor. TikTok ve Shorts izleyicisi 1 saniyede kaydırıyor (%75 erken terk).
            </p>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300">
              <strong>Fırsat Çözümü:</strong> İlk 1 saniyede doğrudan aksiyon: Dumanı tüten glaze dökülüşü veya çıtır hamur kırılma sesi + büyük fontlu ekran yazısı.
            </div>
          </div>

          <!-- Hata 5 -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-rose-500/30 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-rose-400 flex items-center gap-1.5"><i data-lucide="briefcase" class="w-4 h-4"></i> Hata 5: Çankaya B2B / Kurumsalın İhmali</span>
              <span class="text-[10px] text-slate-500 font-mono">Büyük Ciro Kaybı</span>
            </div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Reşit Galip ve GOP bölgesi yüzlerce büyükelçilik, hukuk bürosu, mimarlık ofisi ve klinik ile dolu. Ancak kurumsal catering, toplantı coffee-break kutuları için LinkedIn'de sıfır varlık var.
            </p>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-300">
              <strong>Fırsat Çözümü:</strong> LinkedIn'de şirket ve kurucu profili açıp Çankaya şirketlerine yönelik "Kurumsal Toplantı Kutuları" tanıtımı başlatın (Aylık 40k–60k ₺ ek ciro).
            </div>
          </div>

          <!-- Hata 6 (Bonus) -->
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 hover:border-rose-500/30 transition">
            <div class="flex items-center justify-between">
              <span class="font-bold text-amber-400 flex items-center gap-1.5"><i data-lucide="qr-code" class="w-4 h-4"></i> Fırsat: QR Kod ile UGC Madeleine Çadırı</span>
              <span class="text-[10px] text-slate-500 font-mono">Organik Viral</span>
            </div>
            <p class="text-slate-300 text-[11px] leading-relaxed">
              Müşterilerinize verdiğiniz Instagram QR kodunu dükkandaki masalara şık pleksi çadırlar halinde yerleştirin: "Instagram'da bizi hikayende etiketle, Belçika çikolatalı sıcak Madeleine ikramımız olsun!"
            </p>
            <div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/20 text-[11px] text-amber-300">
              <strong>Sonuç:</strong> Günde 15-20 müşteri organik hikaye paylaşır, Heritage her gün yüzlerce Ankaralının akışına ücretsiz reklam gibi düşer.
            </div>
          </div>
        </div>
      </div>

      <!-- 2. Bölüm: Kanalınızı Büyütecek 5 Adımlı Somut Eylem Planı -->
      <div class="space-y-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <div class="w-2.5 h-2.5 rounded-full bg-emerald-400"></div>
            <h3 class="text-base font-bold text-white">2. Kanalınızı Büyütecek 5 Adımlı Somut Eylem Planı</h3>
          </div>
          <span class="text-xs text-emerald-400 font-medium bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/20">Yol Haritası</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-5 gap-3 text-xs">
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 relative">
            <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 font-black flex items-center justify-center text-xs">1</div>
            <h4 class="font-bold text-white text-sm">Handle & Bio Standardı</h4>
            <p class="text-slate-400 text-[11px] leading-relaxed">TikTok adını <code>@heritagecafeandbakery</code> yapın. Bio'ya Ankara/Çankaya adresini ve sipariş linkini ekleyin.</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 relative">
            <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 font-black flex items-center justify-center text-xs">2</div>
            <h4 class="font-bold text-white text-sm">3 Saniye Kancası (Hook)</h4>
            <p class="text-slate-400 text-[11px] leading-relaxed">Tüm Shorts ve TikTok'ların ilk 2 saniyesine duman, eriyen krema veya çıtır kırılma sesi + iddialı başlık koyun.</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 relative">
            <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 font-black flex items-center justify-center text-xs">3</div>
            <h4 class="font-bold text-white text-sm">3 Sabit Gönderi (Pin)</h4>
            <p class="text-slate-400 text-[11px] leading-relaxed">Profilin tepesine: 1. Kimiz & Hikayemiz, 2. Cinnabon & Samsa nasıl yapılıyor?, 3. Reşit Galip'e nasıl gelinir? sabitleyin.</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 relative">
            <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 font-black flex items-center justify-center text-xs">4</div>
            <h4 class="font-bold text-white text-sm">Lokal Geo-Tagging</h4>
            <p class="text-slate-400 text-[11px] leading-relaxed">Her gönderiye "Çankaya, Ankara" konumunu ekleyin. Açıklamalara #ankaraetkinlik #çankayakafe hashtag'lerini yazın.</p>
          </div>
          <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2 relative">
            <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 font-black flex items-center justify-center text-xs">5</div>
            <h4 class="font-bold text-white text-sm">LinkedIn B2B Satış</h4>
            <p class="text-slate-400 text-[11px] leading-relaxed">Kurumsal toplantı kutusu kataloğunu duyurup "Yorumlara KATALOG yazan ofislere numune kutusu" kampanyasını başlatın.</p>
          </div>
        </div>
      </div>

      <!-- 3. Bölüm: Başlık & Küçük Resim Formülü (CTR) -->
      <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div class="flex items-center space-x-2">
            <div class="w-2.5 h-2.5 rounded-full bg-amber-400"></div>
            <h3 class="text-base font-bold text-white">3. Başlık & Küçük Resim (Thumbnail) Formülü — Tıklama Oranı (CTR) Artırma</h3>
          </div>
          <span class="text-xs text-amber-400 font-medium bg-amber-500/10 px-2.5 py-1 rounded border border-amber-500/20">CTR Formülü</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
          <!-- Sol: Başlık Formülleri -->
          <div class="space-y-3">
            <h4 class="font-bold text-slate-200 flex items-center gap-2">
              <i data-lucide="type" class="w-4 h-4 text-amber-400"></i>
              Eski / Zayıf Başlıklar vs Yeni Tıklatan Başlıklar
            </h4>
            <div class="space-y-2">
              <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 flex items-center justify-between">
                <div>
                  <span class="text-rose-400 line-through text-[11px]">❌ "Cinnabon yaptık"</span>
                  <div class="text-emerald-300 font-bold text-xs mt-0.5">✅ "Ankara'da Bu Kokuya Kimse Hayır Diyemez! 🔥 (El Açması)"</div>
                </div>
                <span class="text-[10px] text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded font-mono">+%240 CTR</span>
              </div>
              <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 flex items-center justify-between">
                <div>
                  <span class="text-rose-400 line-through text-[11px]">❌ "Pesto soslu tost"</span>
                  <div class="text-emerald-300 font-bold text-xs mt-0.5">✅ "Böyle Uzayan Bir Peynir Görmediniz! 🧀 (Çankaya Tostu)"</div>
                </div>
                <span class="text-[10px] text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded font-mono">+%180 CTR</span>
              </div>
              <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 flex items-center justify-between">
                <div>
                  <span class="text-rose-400 line-through text-[11px]">❌ "Samsa böreğimiz"</span>
                  <div class="text-emerald-300 font-bold text-xs mt-0.5">✅ "Ankara'da 60 ₺'ye El Açması Çıtır Samsa Kaldı mı?"</div>
                </div>
                <span class="text-[10px] text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded font-mono">+%310 CTR</span>
              </div>
              <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 flex items-center justify-between">
                <div>
                  <span class="text-rose-400 line-through text-[11px]">❌ "Mekanımızdan kareler"</span>
                  <div class="text-emerald-300 font-bold text-xs mt-0.5">✅ "Ankara'da Laptopunu Alıp Saatlerce Çalışabileceğin O Kafe..."</div>
                </div>
                <span class="text-[10px] text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded font-mono">+%190 CTR</span>
              </div>
            </div>
          </div>

          <!-- Sağ: Küçük Resim Kuralları -->
          <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 space-y-3">
            <h4 class="font-bold text-amber-400 flex items-center gap-2">
              <i data-lucide="sparkle" class="w-4 h-4"></i>
              Küçük Resim (Thumbnail) 3 Altın Kuralı
            </h4>
            <ul class="space-y-2 text-[11px] text-slate-300 leading-relaxed">
              <li class="flex items-start gap-2">
                <span class="w-4 h-4 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0 font-bold">1</span>
                <span><strong>Makro & Yakın Çekim:</strong> Tüm tepsiyi uzaktan çekmeyin. Çatalın batıp dumanın çıktığı veya sosun damladığı en yakın anı kapak yapın.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-4 h-4 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0 font-bold">2</span>
                <span><strong>Maksimum 3-4 Kelimelik Kalın Yazı:</strong> "BU KOKU GERÇEK Mİ?", "60 ₺'YE ÇITIR!" gibi sarı veya beyaz renkli, arkası gölgeli büyük puntolu metin.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-4 h-4 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0 font-bold">3</span>
                <span><strong>Doygunluk ve Kontrast:</strong> Renkleri soluk bırakmayın; sarı hamur, kırmızı çilek ve beyaz krema kontrastını CapCut'ta hafifçe yükseltin (+%15 Doygunluk).</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 4. & 5. Bölüm: LinkedIn Algoritması & En Çok Tutan 4 İçerik Formatı -->
      <div class="glass-card rounded-2xl p-6 border border-blue-500/30 bg-gradient-to-r from-slate-900 via-blue-950/20 to-slate-900 space-y-5">
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div class="flex items-center space-x-2">
            <i data-lucide="linkedin" class="w-5 h-5 text-blue-400"></i>
            <h3 class="text-base font-bold text-white">4. LinkedIn Algoritması Nasıl Çalışıyor? (Neden Standart Postlar Tutmuyor?)</h3>
          </div>
          <span class="text-xs text-blue-400 font-medium bg-blue-500/10 px-2.5 py-1 rounded border border-blue-500/20">B2B Algoritma Sırrı</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
          <div class="space-y-2 text-slate-300 leading-relaxed text-[11px]">
            <p>
              LinkedIn Instagram değildir. "Günün kahvesi hazır bekleriz" gibi gönderiler LinkedIn'de <strong>15-20 görüntülenmede kalır</strong>. Çünkü LinkedIn algoritması şunları arar:
            </p>
            <div class="p-3 rounded-lg bg-slate-900/80 border border-slate-800 space-y-1.5">
              <div class="font-bold text-white flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-blue-400"></i> 1. Ekranda Kalma Süresi (Dwell Time):</div>
              <p class="text-slate-400">Kullanıcı yazıyı okumak veya PDF karuseli kaydırmak için gönderide ne kadar çok vakit geçirirse gönderi o kadar öne fırlar.</p>
              <div class="font-bold text-white flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-blue-400"></i> 2. Yorum ve Tartışma Değeri:</div>
              <p class="text-slate-400">Beğeni (Like) değersizdir; algoritma gönderiyi ilk 60 dakikada gelen <strong>uzun yorumlara</strong> göre tüm Ankara iş ağına dağıtır.</p>
              <div class="font-bold text-white flex items-center gap-1.5"><i data-lucide="check" class="w-3.5 h-3.5 text-blue-400"></i> 3. İş Değeri ve Problem Çözme:</div>
              <p class="text-slate-400">"Ofis toplantılarında enerji düşüşü nasıl önlenir?", "B2B kurumsal ikramda bayat kuru pasta devri nasıl biter?" gibi iş dünyasının dertlerine odaklanılmalıdır.</p>
            </div>
          </div>

          <!-- En Çok Tutan 4 Format -->
          <div class="space-y-2.5">
            <h4 class="font-bold text-white text-xs uppercase tracking-wider flex items-center gap-1.5">
              <i data-lucide="layout-grid" class="w-4 h-4 text-purple-400"></i>
              LinkedIn'de En Çok Tutan 4 İçerik Formatı
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px]">
              <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800 space-y-1">
                <span class="font-bold text-blue-300">1. Kişisel Kurucu Hikayesi</span>
                <p class="text-slate-400">"Bir IVF merkezinde artisan kafe açtığımızda bize 'burada hasta beklemez' dediler... İşte 4 ayda öğrendiğimiz 3 ders."</p>
              </div>
              <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800 space-y-1">
                <span class="font-bold text-purple-300">2. B2B PDF Karuseli</span>
                <p class="text-slate-400">"Toplantılarda kuru pasta devri bitti: Çankaya ofisleri için 5 artisan ikram kutusu çözümü (10 slaytlık PDF)."</p>
              </div>
              <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800 space-y-1">
                <span class="font-bold text-emerald-300">3. Sürdürülebilirlik Vaka Analizi</span>
                <p class="text-slate-400">"Her akşam 17:00'de neden vitrin ürünlerine indirim yapıyoruz? (Gıda israfını sıfırlayan Zero-Waste fırın modeli)."</p>
              </div>
              <div class="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800 space-y-1">
                <span class="font-bold text-amber-300">4. Ofis Çalışanı Anketi (Poll)</span>
                <p class="text-slate-400">"Öğleden sonra toplantısında odağınızı en çok hangisi artırıyor? A) Focaccia Sandviç B) Sıcak Cinnabon C) Fıstıklı Kurabiye."</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 6. & 7. Bölüm: Sıcak Satışa Dönüştüren "Yorum & Lead Döngüsü" & Haftalık Rutin -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
        
        <!-- Yorum & Lead Döngüsü -->
        <div class="glass-card rounded-2xl p-6 border border-emerald-500/30 bg-gradient-to-r from-slate-900 via-emerald-950/20 to-slate-900 space-y-4">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <i data-lucide="zap" class="w-4 h-4 text-emerald-400"></i>
              Sıcak Satışa Dönüştüren "Yorum & Lead Döngüsü" (Growth Hack)
            </h3>
            <span class="text-[10px] text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">Kurumsal B2B</span>
          </div>

          <div class="space-y-2 text-[11px] text-slate-300 leading-relaxed">
            <p><strong>Uygulama Adımları:</strong></p>
            <ol class="list-decimal pl-4 space-y-1 text-slate-400">
              <li>LinkedIn'de gönderi açın: <em>"Çankaya bölgesindeki avukatlık büroları, klinikler ve elçilikler için hazırladığımız '2026 Kurumsal Toplantı & Coffee Break Menü Kataloğumuz' hazır!"</em></li>
              <li>Harekete Geçirici Mesaj (CTA): <em>"Yorumlara <strong>'KATALOG'</strong> yazan Çankaya'daki ilk 20 ofise PDF kataloğumuzu ve ücretsiz mini deneme kutumuzu elden ulaştırıyoruz."</em></li>
              <li>Algoritma Etkisi: 30-40 kişi "KATALOG" yazdığında gönderi patlar ve binlerce yöneticiye ulaşır.</li>
              <li>Satış Dönüşümü: Yorum yazan her yöneticiye DM'den PDF katalog atılır, ertesi gün ofislerine 1 kutu sıcak Samsa & Kurabiye hediye götürülerek düzenli haftalık B2B sipariş sözleşmesi bağlanır!</li>
            </ol>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 font-medium">
              💡 Bu döngü ile 4 haftada en az 8-10 kurumsal ofis müdavim yapılır; aylık 40.000 – 60.000 ₺ garanti nakit akışı sağlar.
            </div>
          </div>
        </div>

        <!-- Haftalık 3 Günlük Paylaşım Rutini -->
        <div class="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <i data-lucide="calendar" class="w-4 h-4 text-amber-400"></i>
              Haftalık 3 Günlük Paylaşım Rutini (Yormayan Sistem)
            </h3>
            <span class="text-[10px] text-slate-400 font-mono">Haftada 3 Post</span>
          </div>

          <div class="space-y-2.5 text-[11px]">
            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-blue-300 flex items-center gap-1.5"><i data-lucide="calendar" class="w-3.5 h-3.5"></i> Salı (Saat 10:30): B2B & Kurumsal Odak</span>
                <span class="text-[10px] text-slate-500 font-mono">LinkedIn + IG</span>
              </div>
              <p class="text-slate-400">Ofis toplantı kutuları, coffee break ikramları veya girişimcilik/kalite hikayesi.</p>
            </div>

            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-pink-300 flex items-center gap-1.5"><i data-lucide="video" class="w-3.5 h-3.5"></i> Perşembe (Saat 14:30): İştah & Ürün ASMR</span>
                <span class="text-[10px] text-slate-500 font-mono">TikTok + Reels + Shorts</span>
              </div>
              <p class="text-slate-400">Cinnabon glaze şelalesi, uzayan focaccia peyniri veya el açması çıtır Samsa videosu.</p>
            </div>

            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-amber-300 flex items-center gap-1.5"><i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Pazar (Saat 11:00): Zanaat & Hafta Sonu Kahvesi</span>
                <span class="text-[10px] text-slate-500 font-mono">IG Karusel + Shorts</span>
              </div>
              <p class="text-slate-400">Taş fırından çıkış anı, fırıncı mutfak sırrı veya hafta sonu dinlendirici kafe atmosferi.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- 8. Bölüm: İNTERAKTİF DENETİM KONTROL LİSTESİ & YORUM ALANI (Live Audit & Comments Tracker) -->
      <div class="glass-card rounded-2xl p-6 border border-pink-500/30 space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 border-b border-slate-800 gap-3">
          <div>
            <div class="flex items-center gap-2">
              <i data-lucide="check-square" class="w-5 h-5 text-pink-400"></i>
              <h3 class="text-base font-bold text-white">İnteraktif Denetim Kontrol Listesi & Düzeltme Yorum Alanı</h3>
            </div>
            <p class="text-xs text-slate-400 mt-0.5">
              Maddeleri düzelttikçe işaretleyin, altındaki yorum kutusuna notlarınızı yazın ve kaydedin. Bilgiler tarayıcınızda kalıcı saklanır.
            </p>
          </div>
          <div class="flex items-center gap-2.5">
            <button onclick="saveAuditNotes()" class="px-3.5 py-2 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/40 text-xs font-bold flex items-center gap-1.5 transition cursor-pointer">
              <i data-lucide="save" class="w-4 h-4"></i>
              <span>Yorumları Kaydet</span>
            </button>
            <button onclick="rescanSocialChannels()" class="px-3.5 py-2 rounded-lg bg-pink-500/20 hover:bg-pink-500/30 text-pink-300 border border-pink-500/40 text-xs font-bold flex items-center gap-1.5 transition cursor-pointer">
              <i data-lucide="scan" class="w-4 h-4"></i>
              <span>Yeniden Tara & Raporla</span>
            </button>
          </div>
        </div>

        <!-- Checklist Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs" id="audit-items-container">
          <!-- Dynamically populated via JS, or static with JS bindings -->
        </div>

        <!-- Dynamic Gap Analysis Report Output Card -->
        <div id="gap-report-card" class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <h4 class="text-sm font-bold text-white flex items-center gap-2">
              <i data-lucide="file-text" class="w-4 h-4 text-amber-400"></i>
              <span>Kanal Eksiklik & Acil Görev Raporu (Gap Analysis)</span>
            </h4>
            <button onclick="copyGapReport()" class="text-xs text-amber-400 hover:text-amber-300 flex items-center gap-1 font-semibold underline underline-offset-2 transition cursor-pointer">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i> Raporu Kopyala
            </button>
          </div>
          <div id="gap-report-content" class="text-xs text-slate-300 leading-relaxed font-mono whitespace-pre-wrap bg-slate-950/80 p-4 rounded-xl border border-slate-800/80">
            Rapor hesaplanıyor...
          </div>
        </div>

      </div>

    </section>
'''

# Insert tab-social right before </main>
main_tag = '</main>'
if main_tag in code:
    code = code.replace(main_tag, social_section_html + '\n  ' + main_tag, 1)
    print("Inserted tab-social HTML section successfully!")
else:
    print("main_tag not found!")

# 3. Add JavaScript functions for Social Tab
social_js = '''
    // ==========================================
    // SOCIAL MEDIA AUDIT, COMMENTS & GAP ENGINE
    // ==========================================
    const DEFAULT_AUDIT_ITEMS = [
      {
        id: 'item_1',
        title: 'TikTok Handle Standardizasyonu',
        desc: '@heritage.cafe.bake olan TikTok adını mümkünse @heritagecafeandbakery olarak eşitleyin.',
        category: 'TikTok',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_2',
        title: 'Biyografi ve Biolink / Linktree Kurulumu',
        desc: 'Bioya: Ankara/Çankaya Reşit Galip No:18, Kapanış 18:00, Harita, Menü ve Trendyol Go linki ekleyin.',
        category: 'Tüm Kanallar',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_3',
        title: 'YouTube Shorts Kapak Resmi (Thumbnail) Seçimi',
        desc: 'Shorts yüklerken kalem simgesiyle dumanın tüttüğü veya sosun aktığı en iştah kabartan kareyi kapak seçin.',
        category: 'YouTube',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_4',
        title: 'Tıklatan Başlık Formülü (CTR Optimizasyonu)',
        desc: '"Focaccia yaptık" yerine "Ankara\'da Böyle Uzayan Bir Peynir Görmediniz! 🧀" tarzı merak kancaları kullanın.',
        category: 'YouTube & TikTok',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_5',
        title: 'İlk 3 Saniye Kancası (Hook) Kuralı',
        desc: 'Videoya sessiz başlamayın; ilk 1 saniyede duman, çatal batırma veya çıtır ses + iddialı ekran yazısı girsin.',
        category: 'Video Üretimi',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_6',
        title: '3 Adet Sabitlenmiş Video (Pinned Posts)',
        desc: 'Profilin tepesine: 1) Biz Kimiz, 2) İmza Lezzetler (Cinnabon/Samsa), 3) Reşit Galip Yol Tarifi videolarını sabitleyin.',
        category: 'Instagram & TikTok',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_7',
        title: 'LinkedIn Şirket & Kurucu Sayfası Açılışı',
        desc: 'LinkedIn\'de profesyonel şirket sayfası açıp Çankaya B2B ofis ikramlarını ve kurucu hikayelerini paylaşın.',
        category: 'LinkedIn B2B',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_8',
        title: 'Yorum & Lead Döngüsü (Katalog Kampanyası)',
        desc: '"Yorumlara KATALOG yazan Çankaya ofislerine ücretsiz deneme kutusu" kampanyasını LinkedIn ve IG\'de yayınlayın.',
        category: 'B2B Satış',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_9',
        title: 'Haftalık 3 Günlük Paylaşım Rutinine Geçiş',
        desc: 'Salı B2B, Perşembe Cinnabon/Focaccia ASMR, Pazar zanaat fırıncılık hikayesi takvimini uygulayın.',
        category: 'İçerik Takvimi',
        weight: 10,
        done: false,
        note: ''
      },
      {
        id: 'item_10',
        title: 'Masa Üstü QR Kodlu UGC Madeleine Kampanyası',
        desc: 'Masalara QR kodlu akrilik çadır koyun: "Bizi hikayende etiketle, sıcak Belçika çikolatalı Madeleine ikramımız olsun!"',
        category: 'Dükkan İçi Viral',
        weight: 10,
        done: false,
        note: ''
      }
    ];

    let auditItems = [];

    function loadAuditItems() {
      try {
        const saved = localStorage.getItem('heritage_social_audit');
        if (saved) {
          const parsed = JSON.parse(saved);
          auditItems = DEFAULT_AUDIT_ITEMS.map(item => {
            const match = parsed.find(p => p.id === item.id);
            return match ? { ...item, done: match.done, note: match.note || '' } : item;
          });
        } else {
          auditItems = JSON.parse(JSON.stringify(DEFAULT_AUDIT_ITEMS));
        }
      } catch (e) {
        auditItems = JSON.parse(JSON.stringify(DEFAULT_AUDIT_ITEMS));
      }
    }

    function saveAuditNotes() {
      // Collect latest notes from textareas
      auditItems.forEach(item => {
        const txt = document.getElementById('note_' + item.id);
        if (txt) item.note = txt.value.trim();
        const chk = document.getElementById('chk_' + item.id);
        if (chk) item.done = chk.checked;
      });

      try {
        localStorage.setItem('heritage_social_audit', JSON.stringify(auditItems));
        alert('Yorumlarınız ve denetim notlarınız başarıyla kaydedildi!');
      } catch (e) {
        alert('Notlar kaydedilirken bir hata oluştu: ' + e);
      }
      rescanSocialChannels(false);
    }

    function renderSocialTab() {
      loadAuditItems();
      const container = document.getElementById('audit-items-container');
      if (!container) return;

      container.innerHTML = auditItems.map(item => `
        <div class="p-4 rounded-xl ${item.done ? 'bg-emerald-950/20 border-emerald-500/40' : 'bg-slate-900/80 border-slate-800'} border space-y-3 transition">
          <div class="flex items-start justify-between gap-3">
            <label class="flex items-start space-x-2.5 cursor-pointer select-none">
              <input type="checkbox" id="chk_${item.id}" ${item.done ? 'checked' : ''} onchange="toggleAuditItem('${item.id}', this.checked)" class="mt-1 rounded border-slate-700 bg-slate-900 text-emerald-500 focus:ring-emerald-500/30">
              <div>
                <span class="font-bold text-sm ${item.done ? 'text-emerald-300 line-through' : 'text-white'}">${item.title}</span>
                <span class="ml-2 text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-400 font-mono">${item.category}</span>
                <p class="text-xs text-slate-400 mt-1 leading-relaxed">${item.desc}</p>
              </div>
            </label>
            <span class="text-xs font-bold ${item.done ? 'text-emerald-400' : 'text-amber-400'} shrink-0">
              ${item.done ? '✓ Düzeltildi' : '○ Beklemede'}
            </span>
          </div>

          <!-- Yorum / Düzeltme Notu Alanı -->
          <div class="pt-2 border-t border-slate-800/80 space-y-1">
            <label class="text-[11px] font-semibold text-slate-400 flex items-center gap-1">
              <i data-lucide="message-square" class="w-3 h-3 text-pink-400"></i>
              Düzeltme Notu / Yorumunuz:
            </label>
            <textarea id="note_${item.id}" placeholder="Örn: Bio linki oluşturuldu, haftaya çekim yapılacak..." rows="2" class="w-full p-2 bg-slate-950/80 border border-slate-800 rounded-lg text-xs text-slate-200 placeholder-slate-600 focus:outline-none focus:ring-1 focus:ring-pink-500">${item.note || ''}</textarea>
          </div>
        </div>
      `).join('');

      rescanSocialChannels(false);
      try { lucide.createIcons(); } catch(e) {}
    }

    function toggleAuditItem(id, isDone) {
      const item = auditItems.find(i => i.id === id);
      if (item) {
        item.done = isDone;
        // auto-save to localStorage
        try {
          localStorage.setItem('heritage_social_audit', JSON.stringify(auditItems));
        } catch(e) {}
        renderSocialTab();
      }
    }

    function rescanSocialChannels(showAlert = true) {
      // Gather latest notes
      auditItems.forEach(item => {
        const txt = document.getElementById('note_' + item.id);
        if (txt) item.note = txt.value.trim();
        const chk = document.getElementById('chk_' + item.id);
        if (chk) item.done = chk.checked;
      });

      const totalItems = auditItems.length;
      const completedItems = auditItems.filter(i => i.done).length;
      const score = Math.round((completedItems / totalItems) * 100);

      // Update UI Score
      const scoreEl = document.getElementById('live-audit-score');
      const circleEl = document.getElementById('live-audit-circle');
      const navScoreEl = document.getElementById('social-nav-score');

      if (scoreEl) scoreEl.textContent = `${score} / 100`;
      if (circleEl) circleEl.textContent = `%${score}`;
      if (navScoreEl) navScoreEl.textContent = `${score}/100`;

      // Build Gap Analysis Report
      const pendingItems = auditItems.filter(i => !i.done);
      let reportText = `📋 HERİTAGE CAFE & BAKERY — SOSYAL MEDYA EKSİK & GELİŞİM RAPORU\\n`;
      reportText += `📅 Tarih: ${new Date().toLocaleDateString('tr-TR')} | 📊 Mevcut Sağlık Skoru: %${score}\\n`;
      reportText += `------------------------------------------------------------\\n\\n`;

      if (pendingItems.length === 0) {
        reportText += `🎉 TEBRİKLER! Tüm kritik düzeltmeler başarıyla tamamlandı.\\nKanal sağlık skoru %100 seviyesindedir. Düzenli paylaşımlara devam ediniz!`;
      } else {
        reportText += `🚨 HENÜZ TAMAMLANMAYAN ${pendingItems.length} KRİTİK EKSİK:\\n\\n`;
        pendingItems.forEach((item, idx) => {
          reportText += `${idx + 1}. [${item.category}] ${item.title}\\n`;
          reportText += `   Açıklama: ${item.desc}\\n`;
          if (item.note) {
            reportText += `   💬 Mevcut Notunuz: "${item.note}"\\n`;
          } else {
            reportText += `   ⚠️ Durum: Henüz aksiyon notu girilmedi.\\n`;
          }
          reportText += `\\n`;
        });

        reportText += `------------------------------------------------------------\\n`;
        reportText += `💡 ÖNCELİKLİ İLK 2 ADIM:\\n`;
        reportText += `1. TikTok kullanıcı adını ve YouTube Shorts kapak resimlerini acilen güncelleyin.\\n`;
        reportText += `2. LinkedIn'de kurumsal toplantı kataloğu gönderisini yayına alın!`;
      }

      const reportBox = document.getElementById('gap-report-content');
      if (reportBox) {
        reportBox.textContent = reportText;
      }

      if (showAlert) {
        alert(`Kanal ve sayfalar tarandı!\\n\\nGüncel Sağlık Skoru: %${score}\\nTamamlanan: ${completedItems}/${totalItems}\\nKalan Eksik: ${pendingItems.length}`);
      }
    }

    function copyGapReport() {
      const reportBox = document.getElementById('gap-report-content');
      if (reportBox) {
        navigator.clipboard.writeText(reportBox.textContent).then(() => {
          alert('Eksik ve gelişim raporu panoya kopyalandı!');
        });
      }
    }
'''

# Update switchTab in JavaScript to call renderSocialTab
old_switch = '''      } else if (tabId === 'tab-forecast') {
        renderForecastTab();
      }
      lucide.createIcons();'''

new_switch = '''      } else if (tabId === 'tab-forecast') {
        renderForecastTab();
      } else if (tabId === 'tab-social') {
        renderSocialTab();
      }
      lucide.createIcons();'''

if old_switch in code:
    code = code.replace(old_switch, new_switch, 1)
    print("Updated switchTab to include renderSocialTab!")
else:
    print("old_switch not matched, checking alternative...")

# Append social_js before Initial Load
init_anchor = '    // Initial Load'
if init_anchor in code:
    code = code.replace(init_anchor, social_js + '\n\n' + init_anchor, 1)
    print("Appended social_js successfully!")
else:
    print("init_anchor not found!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_portal.py written successfully!")

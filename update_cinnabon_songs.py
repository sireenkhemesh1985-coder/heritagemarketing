import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's update each Cinnabon card with 🎵 Müzik / Trend Ses line

# Card 1
old_c1 = '''                <p><span class="text-rose-400 font-semibold">Ekran Metni:</span> "Ankara'da bu kokuya hayır diyebilecek biri var mı? 🤤"</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Kaydet, ilk Cinnabon borcu olan arkadaşına gönder!"</p>'''

new_c1 = '''                <p><span class="text-rose-400 font-semibold">Ekran Metni:</span> "Ankara'da bu kokuya hayır diyebilecek biri var mı? 🤤"</p>
                <p><span class="text-purple-400 font-semibold">🎵 Önerilen Ses:</span> <strong>Laufey - "From the Start" (Lo-Fi Jazz Beat)</strong> veya <em>HM Surf - "Tupac"</em> (Müzik sesi %20'ye kısılmalı, ASMR fırın/krema sesi %100 kalmalı).</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Kaydet, ilk Cinnabon borcu olan arkadaşına gönder!"</p>'''

# Card 2
old_c2 = '''                <p><span class="text-rose-400 font-semibold">Seslendirme:</span> "Fabrikasyon değil, her sabah el açması tereyağlı mayalı hamurla sıfırdan sarılıyor!"</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Bugün 18:00'e kadar bekliyoruz veya Trendyol Go'dan kapına söyle! 📍 Çankaya No:18"</p>'''

new_c2 = '''                <p><span class="text-rose-400 font-semibold">Seslendirme:</span> "Fabrikasyon değil, her sabah el açması tereyağlı mayalı hamurla sıfırdan sarılıyor!"</p>
                <p><span class="text-purple-400 font-semibold">🎵 Önerilen Ses:</span> <strong>Surfaces - "Sunday Best"</strong> veya <strong>Bakar - "Hell N Back (Instrumental)"</strong> (Dinamik, pozitif, şehirli kafe yürüyüş ritmi).</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Bugün 18:00'e kadar bekliyoruz veya Trendyol Go'dan kapına söyle! 📍 Çankaya No:18"</p>'''

# Card 3
old_c3 = '''                <p><span class="text-rose-400 font-semibold">Ekran Metni:</span> "Margarin yok ❌ Donuk hazır hamur yok ❌ Sadece tereyağı, Seylan tarçını ve aşk. ❤️"</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Bu tepsiyi kiminle bitirirsin? Etiketle!"</p>'''

new_c3 = '''                <p><span class="text-rose-400 font-semibold">Ekran Metni:</span> "Margarin yok ❌ Donuk hazır hamur yok ❌ Sadece tereyağı, Seylan tarçını ve aşk. ❤️"</p>
                <p><span class="text-purple-400 font-semibold">🎵 Önerilen Ses:</span> <strong>Tom Misch - "Disco Yes"</strong> veya <strong>Khruangbin - "Texas Sun"</strong> (Mutfak kesitlerine, hamur vurma ve ip kesim anına oturan tatmin edici ritim).</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Bu tepsiyi kiminle bitirirsin? Etiketle!"</p>'''

# Card 4
old_c4 = '''                <p><span class="text-rose-400 font-semibold">Seslendirme:</span> "Bazen ihtiyacın olan tek şey, sıcacık bir fincan kahve ve tarçın kokusunun getirdiği o küçük huzur anıdır."</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Kendine bugün küçük bir ödül ver. Saat 18:00'e kadar bekliyoruz."</p>'''

new_c4 = '''                <p><span class="text-rose-400 font-semibold">Seslendirme:</span> "Bazen ihtiyacın olan tek şey, sıcacık bir fincan kahve ve tarçın kokusunun getirdiği o küçük huzur anıdır."</p>
                <p><span class="text-purple-400 font-semibold">🎵 Önerilen Ses:</span> <strong>Laufey - "Promise (Acoustic)"</strong> veya <strong>Norah Jones - "Don't Know Why"</strong> (Sıcak, dinlendirici, sonbahar/kış kafe atmosferi).</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Kendine bugün küçük bir ödül ver. Saat 18:00'e kadar bekliyoruz."</p>'''

# Card 5
old_c5 = '''                <p><span class="text-rose-400 font-semibold">Hedef Kitle:</span> Çankaya ofisleri, büyükelçilikler ve evde çalışanlar.</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Tükenmeden Şimdi Sipariş Ver! (Trendyol Go & Al-Götür) / Kapanış: 18:00"</p>'''

new_c5 = '''                <p><span class="text-rose-400 font-semibold">Hedef Kitle:</span> Çankaya ofisleri, büyükelçilikler ve evde çalışanlar.</p>
                <p><span class="text-purple-400 font-semibold">🎵 Önerilen Ses:</span> <strong>Dua Lipa - "Levitating (Instrumental Club Beat)"</strong> veya Meta Ads Telifsiz Kütüphanesinden <em>"Upbeat Bright Morning Funk"</em> (Hızlı, scroll durdurucu ritim).</p>
                <p><span class="text-emerald-400 font-semibold">CTA:</span> "Tükenmeden Şimdi Sipariş Ver! (Trendyol Go & Al-Götür) / Kapanış: 18:00"</p>'''

for old_s, new_s in [(old_c1, new_c1), (old_c2, new_c2), (old_c3, new_c3), (old_c4, new_c4), (old_c5, new_c5)]:
    if old_s in code:
        code = code.replace(old_s, new_s, 1)
        print("Updated card with song recommendation!")
    else:
        print("Could not match old card string, checking...")

# Update copyScript text for Cinnabon
old_js_c1 = "'cinnabon_1': `Cinnabon Video 1: Dumanı Üstünde Glaze Şelalesi (ASMR)\\nHook: Ankara'da bu kokuya hayır diyebilecek biri var mı? 🤤\\nGörsel: Fırından yeni çıkmış sıcak Cinnabon tepsisine bol labneli vanilyalı glaze sos dökülür, kıvrımlarına sızar. Çatal orta göbeğe batırılır.\\nCTA: Kaydet, ilk Cinnabon borcu olan arkadaşına gönder! 📍 Reşit Galip No:18 Çankaya`"
new_js_c1 = "'cinnabon_1': `Cinnabon Video 1: Dumanı Üstünde Glaze Şelalesi (ASMR)\\nHook: Ankara'da bu kokuya hayır diyebilecek biri var mı? 🤤\\nGörsel: Fırından yeni çıkmış sıcak Cinnabon tepsisine bol labneli vanilyalı glaze dökülür.\\n🎵 Önerilen Şarkı: Laufey - From the Start (Lo-Fi Jazz) veya HM Surf - Tupac (Müzik: %20, ASMR ses: %100)\\nCTA: Kaydet, ilk Cinnabon borcu olan arkadaşına gönder! 📍 Reşit Galip No:18 Çankaya`"

if old_js_c1 in code:
    code = code.replace(old_js_c1, new_js_c1, 1)
    print("Updated copyScript cinnabon_1 with song!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_portal.py updated successfully!")

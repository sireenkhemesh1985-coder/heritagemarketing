import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
path = r'C:\Users\sireen.khemesh\.gemini\antigravity\brain\6bc0ebe0-bf6e-4d46-9ff9-4b695826a984\Heritage_Finans_Pazarlama_Raporu.md'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Update slides with song recommendations
text = text.replace(
    '- **Caption & CTA:** *"Fırından yeni çıktı, kreması üzerinde eriyor... 🥐🔥 Ankara Çankaya\'da canınız gerçek el açması Cinnabon çektiğinde adres belli. Kaydet, ilk Cinnabon borcu olan arkadaşına gönder! 📍 Reşit Galip Cd. No:18 Çankaya*"',
    '- **🎵 Önerilen Müzik / Trend Ses:** **Laufey - "From the Start" (Lo-Fi Jazz Beat)** veya **HM Surf - "Tupac"** (Müzik sesi %20\'ye kısılmalı, ASMR fırın ve krema sesi %100 orijinal kalmalı!)\n- **Caption & CTA:** *"Fırından yeni çıktı, kreması üzerinde eriyor... 🥐🔥 Ankara Çankaya\'da canınız gerçek el açması Cinnabon çektiğinde adres belli. Kaydet, ilk Cinnabon borcu olan arkadaşına gönder! 📍 Reşit Galip Cd. No:18 Çankaya*"'
)

text = text.replace(
    '- **CTA (12-16 sn):** *"Bugün saat 18:00\'e kadar dükkandayız; ya da Trendyol Go\'dan kapına söyle! 🛵*"',
    '- **🎵 Önerilen Müzik:** **Surfaces - "Sunday Best"** veya **Bakar - "Hell N Back (Instrumental)"** (Pozitif, enerjik şehirli kafe yürüyüş ritmi)\n- **CTA (12-16 sn):** *"Bugün saat 18:00\'e kadar dükkandayız; ya da Trendyol Go\'dan kapına söyle! 🛵*"'
)

text = text.replace(
    '- **CTA:** *"Bu tepsiyi kiminle bitirirsin? Etiketle!"*',
    '- **🎵 Önerilen Müzik:** **Tom Misch - "Disco Yes"** veya **Khruangbin - "Texas Sun"** (Gitar ve bas groove\'u; hamur açma, tereyağı sürme ve dikiş ipi kesim anına oturtulmalı)\n- **CTA:** *"Bu tepsiyi kiminle bitirirsin? Etiketle!"*'
)

text = text.replace(
    '- **Süre:** 14 saniye | **Müzik:** Sıcak nostaljik lo-fi veya akustik gitar',
    '- **Süre:** 14 saniye | **🎵 Önerilen Müzik:** **Laufey - "Promise (Acoustic)"** veya **Norah Jones - "Don\'t Know Why"** (Huzur veren, sarıp sarmalayan kafe melodisi)'
)

text = text.replace(
    '- **CTA (Reklam Butonu):** *"Tükenmeden Şimdi Sipariş Ver! (Trendyol Go & Al-Götür) / Kapanış: 18:00*"',
    '- **🎵 Önerilen Müzik:** **Dua Lipa - "Levitating (Instrumental)"** veya Meta Ads Sound Collection\'dan *Upbeat Bright Funk* (Scroll durdurucu, dinamik satış ritmi)\n- **CTA (Reklam Butonu):** *"Tükenmeden Şimdi Sipariş Ver! (Trendyol Go & Al-Götür) / Kapanış: 18:00*"'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated artifact report with song recommendations successfully!")

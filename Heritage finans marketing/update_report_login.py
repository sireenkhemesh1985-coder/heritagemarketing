import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
path = r'C:\Users\sireen.khemesh\.gemini\antigravity\brain\6bc0ebe0-bf6e-4d46-9ff9-4b695826a984\Heritage_Finans_Pazarlama_Raporu.md'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '## Executive Summary (Yönetici Özeti)'

auth_box = """> [!IMPORTANT]
> **🔐 Portal Güvenlik & Giriş Bilgileri (Login Credentials):**
> Canlı interaktif yönetim portalına ([http://localhost:8080](http://localhost:8080)) güvenli erişim için oluşturulan kullanıcı hesapları:
> * **Yönetici Hesabı:** Kullanıcı Adı: `heritage` | Şifre: `heritage2026`
> * **Sistem Admin:** Kullanıcı Adı: `admin` | Şifre: `admin2026`
> * **İşletme Sahibi:** Kullanıcı Adı: `patron` | Şifre: `123456`
> * **Kişisel Giriş:** Kullanıcı Adı: `sireen` | Şifre: `heritage2026`
> *(Giriş ekranında "Beni Hatırla" seçeneği aktiftir; ayrıca "Tek Tıkla Doldur" butonuyla şifre yazmadan doğrudan giriş yapılabilir. Dashboard sağ üst köşesinde "Çıkış Yap" butonu yer almaktadır.)*

"""

if target in text:
    new_text = text.replace(target, auth_box + target, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Report updated with login credentials!")
else:
    print("target not found in report!")

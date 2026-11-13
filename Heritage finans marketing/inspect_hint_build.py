with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix showPasswordHint
old_hint = """    function showPasswordHint() {
      alert('Tanımlı Giriş Bilgileri:

Kullanıcı Adı: heritage (veya admin)
Şifre: heritage2026 (veya admin2026)');
    }"""

# In build_portal.py, let's see how showPasswordHint is written
import re
print("Matches in build_portal.py:", len(re.findall(r'function showPasswordHint', text)))

# Let's inspect showPasswordHint in build_portal.py
pos = text.find('function showPasswordHint')
if pos != -1:
    print(text[pos:pos+250])

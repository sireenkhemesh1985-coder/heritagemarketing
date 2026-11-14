import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Fix form tag and submit button
old_form = '<form id="login-form" onsubmit="handleLoginSubmit(event)" class="space-y-4">'
new_form = '<form id="login-form" action="javascript:void(0);" onsubmit="handleLoginSubmit(event); return false;" class="space-y-4">'

if old_form in code:
    code = code.replace(old_form, new_form, 1)
    print("Updated form tag!")
else:
    print("old_form not found!")

old_btn = '<button type="submit" id="login-submit-btn"'
new_btn = '<button type="button" onclick="handleLoginSubmit(event)" id="login-submit-btn"'

if old_btn in code:
    code = code.replace(old_btn, new_btn, 1)
    print("Updated submit button to type='button'!")
else:
    print("old_btn not found!")

# 2. Fix showPasswordHint and alert
old_hint = """    function showPasswordHint() {
      alert('Tanımlı Giriş Bilgileri:\\n\\nKullanıcı Adı: heritage (veya admin)\\nŞifre: heritage2026 (veya admin2026)');
    }"""

# Let's use regex or search to replace the entire showPasswordHint and auth functions
old_auth_section_pattern = r'// ==========================================\s+// AUTHENTICATION & LOGIN MANAGEMENT[\s\S]*?// Initial Load\s+window\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s+checkAuth\(\);\s+\}\);'

new_auth_section = '''// ==========================================
    // AUTHENTICATION & LOGIN MANAGEMENT
    // ==========================================
    const VALID_USERS = [
      { username: 'heritage', password: 'heritage2026', name: 'Heritage Yönetici', role: 'Yönetici' },
      { username: 'admin', password: 'admin2026', name: 'Sistem Yöneticisi', role: 'Süper Admin' },
      { username: 'patron', password: '123456', name: 'İşletme Sahibi', role: 'Yönetici' },
      { username: 'sireen', password: 'heritage2026', name: 'Sireen', role: 'Yönetici' }
    ];

    function checkAuth() {
      try {
        const authData = localStorage.getItem('heritage_auth') || sessionStorage.getItem('heritage_auth');
        if (authData) {
          const parsed = JSON.parse(authData);
          if (parsed && parsed.username) {
            showApp(parsed.username, parsed.name || parsed.username);
            return true;
          }
        }
      } catch (e) {
        console.warn('Auth check parse warning:', e);
        clearAuth();
      }
      showLogin();
      return false;
    }

    function showLogin() {
      const loginContainer = document.getElementById('login-container');
      const appContainer = document.getElementById('app-container');
      if (loginContainer) loginContainer.classList.remove('hidden');
      if (appContainer) appContainer.classList.add('hidden');
      try { lucide.createIcons(); } catch(e) {}
    }

    function showApp(username, displayName) {
      try {
        const loginContainer = document.getElementById('login-container');
        const appContainer = document.getElementById('app-container');
        if (loginContainer) loginContainer.classList.add('hidden');
        if (appContainer) appContainer.classList.remove('hidden');

        const userDisplay = document.getElementById('current-user-display');
        if (userDisplay) {
          userDisplay.textContent = displayName || username;
        }

        // Render dashboard tabs safely
        try { renderFinanceTab(); } catch(e) { console.error('Finance tab error:', e); }
        try { renderOrdersTab(); } catch(e) { console.error('Orders tab error:', e); }
        try { renderSalaryTab(); } catch(e) { console.error('Salary tab error:', e); }
        try { lucide.createIcons(); } catch(e) {}
      } catch (err) {
        console.error('showApp error:', err);
      }
    }

    function handleLoginSubmit(e) {
      if (e && e.preventDefault) e.preventDefault();
      
      const uInputEl = document.getElementById('login-username');
      const pInputEl = document.getElementById('login-password');
      if (!uInputEl || !pInputEl) return false;

      const uInput = uInputEl.value.trim().toLowerCase();
      const pInput = pInputEl.value;
      const remember = document.getElementById('login-remember') ? document.getElementById('login-remember').checked : true;
      const errBox = document.getElementById('login-error');
      const errMsg = document.getElementById('login-error-msg');

      const matchedUser = VALID_USERS.find(u => u.username.toLowerCase() === uInput && u.password === pInput);

      if (matchedUser) {
        if (errBox) errBox.classList.add('hidden');
        const authObj = {
          username: matchedUser.username,
          name: matchedUser.name,
          role: matchedUser.role,
          loginAt: new Date().toISOString()
        };

        try {
          if (remember) {
            localStorage.setItem('heritage_auth', JSON.stringify(authObj));
          } else {
            sessionStorage.setItem('heritage_auth', JSON.stringify(authObj));
          }
        } catch (storageErr) {
          console.warn('Storage unavailable:', storageErr);
        }

        showApp(matchedUser.username, matchedUser.name);
      } else {
        if (errBox) errBox.classList.remove('hidden');
        if (errMsg) errMsg.textContent = 'Kullanıcı adı veya şifre hatalı! Lütfen bilgilerinizi kontrol edin.';
        try { lucide.createIcons(); } catch(e) {}

        // Shake animation
        const card = document.querySelector('#login-container .glass-card');
        if (card) {
          card.classList.add('translate-x-2');
          setTimeout(() => card.classList.remove('translate-x-2'), 100);
          setTimeout(() => card.classList.add('-translate-x-2'), 200);
          setTimeout(() => card.classList.remove('-translate-x-2'), 300);
        }
      }
      return false;
    }

    function handleLogout() {
      if (confirm('Heritage Yönetim Portalından çıkış yapmak istediğinize emin misiniz?')) {
        clearAuth();
        showLogin();
        const uInput = document.getElementById('login-username');
        const pInput = document.getElementById('login-password');
        if (uInput) uInput.value = '';
        if (pInput) pInput.value = '';
      }
    }

    function clearAuth() {
      try {
        localStorage.removeItem('heritage_auth');
        sessionStorage.removeItem('heritage_auth');
      } catch (e) {}
    }

    function togglePasswordVisibility() {
      const pInput = document.getElementById('login-password');
      const icon = document.getElementById('password-toggle-icon');
      if (!pInput) return;
      if (pInput.type === 'password') {
        pInput.type = 'text';
        if (icon) icon.setAttribute('data-lucide', 'eye-off');
      } else {
        pInput.type = 'password';
        if (icon) icon.setAttribute('data-lucide', 'eye');
      }
      try { lucide.createIcons(); } catch(e) {}
    }

    function fillDemoCredentials(u, p) {
      const uInput = document.getElementById('login-username');
      const pInput = document.getElementById('login-password');
      if (uInput) uInput.value = u;
      if (pInput) pInput.value = p;
      const errBox = document.getElementById('login-error');
      if (errBox) errBox.classList.add('hidden');
      // Otomatik giriş yap
      handleLoginSubmit();
    }

    function showPasswordHint() {
      alert(`Tanımlı Giriş Bilgileri:\\n\\nKullanıcı Adı: heritage (veya admin)\\nŞifre: heritage2026 (veya admin2026)`);
    }

    // Initial Load
    window.addEventListener('DOMContentLoaded', () => {
      checkAuth();
    });'''

if re.search(old_auth_section_pattern, code):
    code = re.sub(old_auth_section_pattern, new_auth_section, code, count=1)
    print("Replaced auth section successfully with regex!")
else:
    print("old_auth_section_pattern not matched via regex, searching alternative...")
    # fallback search
    pos1 = code.find('// AUTHENTICATION & LOGIN MANAGEMENT')
    pos2 = code.find('checkAuth();', pos1)
    if pos1 != -1 and pos2 != -1:
        end_pos = code.find('});', pos2) + 3
        code = code[:pos1-42] + new_auth_section + code[end_pos:]
        print("Replaced auth section via fallback offset!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_portal.py written successfully!")

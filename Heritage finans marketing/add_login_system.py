import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add Login Container right after <body> tag
body_target = '<body class="min-h-screen text-slate-100 antialiased selection:bg-brand-500 selection:text-white">'

login_html = '''<body class="min-h-screen text-slate-100 antialiased selection:bg-brand-500 selection:text-white">

  <!-- ========================================== -->
  <!-- LOGIN SCREEN (YÖNETİCİ GİRİŞ EKRANI) -->
  <!-- ========================================== -->
  <div id="login-container" class="min-h-screen flex items-center justify-center p-4 relative overflow-hidden bg-[#0a0d14] z-50">
    <!-- Ambient Glow Background Blobs -->
    <div class="absolute -top-32 -left-32 w-96 h-96 bg-amber-500/15 rounded-full blur-[100px] pointer-events-none"></div>
    <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-emerald-500/15 rounded-full blur-[100px] pointer-events-none"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[550px] h-[550px] bg-slate-900/60 rounded-full blur-[120px] pointer-events-none"></div>

    <!-- Login Glass Card -->
    <div class="max-w-md w-full glass-card rounded-3xl p-8 border border-amber-500/30 shadow-2xl relative z-10 space-y-6 transition-all duration-300">
      
      <!-- Brand Logo & Header -->
      <div class="text-center space-y-3">
        <div class="inline-flex w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-500 to-amber-700 p-0.5 shadow-xl shadow-amber-900/40 items-center justify-center">
          <div class="w-full h-full bg-[#12161f] rounded-[14px] flex items-center justify-center">
            <span class="text-amber-400 font-black text-3xl tracking-tighter">H</span>
          </div>
        </div>
        <div>
          <h2 class="text-2xl font-black text-white tracking-tight flex items-center justify-center gap-2">
            Heritage Cafe & Bakery
          </h2>
          <div class="flex items-center justify-center gap-2 mt-1.5">
            <span class="text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-amber-500/15 text-amber-300 border border-amber-500/30">
              Ankara / Çankaya
            </span>
            <span class="text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
              Yönetici Portalı
            </span>
          </div>
        </div>
        <p class="text-xs text-slate-400 pt-0.5">
          Finansal Yönetim, Sipariş Analitiği & Büyüme Sistemi
        </p>
      </div>

      <!-- Error Alert Box -->
      <div id="login-error" class="hidden p-3 rounded-xl bg-rose-500/15 border border-rose-500/30 text-rose-300 text-xs flex items-center gap-2.5 transition">
        <i data-lucide="alert-triangle" class="w-4 h-4 shrink-0 text-rose-400"></i>
        <span id="login-error-msg" class="leading-tight">Kullanıcı adı veya şifre hatalı!</span>
      </div>

      <!-- Login Form -->
      <form id="login-form" onsubmit="handleLoginSubmit(event)" class="space-y-4">
        <!-- Username Input -->
        <div class="space-y-1.5">
          <label class="text-xs font-semibold text-slate-300 block">Kullanıcı Adı</label>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
              <i data-lucide="user" class="w-4 h-4"></i>
            </div>
            <input type="text" id="login-username" required autocomplete="username" placeholder="heritage" class="w-full pl-10 pr-4 py-2.5 bg-slate-900/90 border border-slate-700 rounded-xl text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition">
          </div>
        </div>

        <!-- Password Input -->
        <div class="space-y-1.5">
          <div class="flex items-center justify-between">
            <label class="text-xs font-semibold text-slate-300 block">Şifre</label>
            <button type="button" onclick="showPasswordHint()" class="text-[11px] text-slate-400 hover:text-amber-300 transition">Şifremi unuttum?</button>
          </div>
          <div class="relative">
            <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
              <i data-lucide="lock" class="w-4 h-4"></i>
            </div>
            <input type="password" id="login-password" required autocomplete="current-password" placeholder="••••••••" class="w-full pl-10 pr-10 py-2.5 bg-slate-900/90 border border-slate-700 rounded-xl text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:border-amber-500 transition">
            <button type="button" onclick="togglePasswordVisibility()" class="absolute inset-y-0 right-0 pr-3.5 flex items-center text-slate-400 hover:text-slate-200 transition focus:outline-none">
              <i data-lucide="eye" id="password-toggle-icon" class="w-4 h-4"></i>
            </button>
          </div>
        </div>

        <!-- Remember Me & Security Badge -->
        <div class="flex items-center justify-between text-xs text-slate-400 pt-1">
          <label class="flex items-center space-x-2 cursor-pointer select-none">
            <input type="checkbox" id="login-remember" checked class="rounded border-slate-700 bg-slate-900 text-amber-500 focus:ring-amber-500/30">
            <span>Beni Hatırla</span>
          </label>
          <span class="text-[11px] text-emerald-400 font-medium flex items-center gap-1">
            <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> 256-bit Güvenli
          </span>
        </div>

        <!-- Submit Button -->
        <button type="submit" id="login-submit-btn" class="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-bold text-sm shadow-lg shadow-amber-500/25 flex items-center justify-center gap-2 transition duration-200 transform hover:-translate-y-0.5 cursor-pointer">
          <span>Giriş Yap</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </button>
      </form>

      <!-- Demo / Otomatik Doldurma Kutusu -->
      <div class="pt-4 border-t border-slate-800/80 space-y-2.5">
        <div class="flex items-center justify-between text-xs">
          <span class="text-slate-400 font-medium flex items-center gap-1.5">
            <i data-lucide="key-round" class="w-3.5 h-3.5 text-amber-400"></i>
            Tanımlı Giriş Bilgileri:
          </span>
          <button type="button" onclick="fillDemoCredentials('heritage', 'heritage2026')" class="text-[11px] text-amber-400 hover:text-amber-300 font-bold underline underline-offset-2 transition cursor-pointer">
            Tek Tıkla Doldur &rarr;
          </button>
        </div>
        <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 text-[11px] text-slate-300 space-y-1.5 font-mono">
          <div class="flex items-center justify-between">
            <span class="text-slate-400 font-sans">Kullanıcı Adı:</span>
            <span class="text-amber-300 font-bold">heritage</span>
            <span class="text-slate-400 font-sans text-[10px]">veya</span>
            <span class="text-amber-300 font-bold">admin</span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400 font-sans">Şifre:</span>
            <span class="text-emerald-300 font-bold">heritage2026</span>
            <span class="text-slate-400 font-sans text-[10px]">veya</span>
            <span class="text-emerald-300 font-bold">admin2026</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MAIN APP CONTAINER (GİRİŞ YAPILINCA GÖRÜNÜR) -->
  <!-- ========================================== -->
  <div id="app-container" class="hidden">'''

# Replace body tag with login container + opening app-container
if body_target in code:
    code = code.replace(body_target, login_html, 1)
    print("Added login container and app-container opening successfully!")
else:
    print("body_target not found!")

# 2. Add User Badge & Logout button into header action buttons
header_btn_target = '''          <button onclick="window.print()" class="flex items-center space-x-1.5 px-3 py-1.5 text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg border border-slate-700 transition shadow-sm">
            <i data-lucide="printer" class="w-3.5 h-3.5 text-blue-400"></i>
            <span>Yazdır</span>
          </button>'''

header_btn_replacement = '''          <button onclick="window.print()" class="flex items-center space-x-1.5 px-3 py-1.5 text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg border border-slate-700 transition shadow-sm">
            <i data-lucide="printer" class="w-3.5 h-3.5 text-blue-400"></i>
            <span>Yazdır</span>
          </button>

          <!-- Logged in User & Logout Button -->
          <div class="flex items-center space-x-2 pl-2 border-l border-slate-800">
            <div class="hidden sm:flex items-center space-x-1.5 px-2.5 py-1.5 text-xs bg-slate-900/90 border border-slate-800 rounded-lg text-slate-300">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <i data-lucide="user-check" class="w-3.5 h-3.5 text-emerald-400"></i>
              <span id="current-user-display" class="font-semibold text-white">heritage</span>
            </div>

            <button onclick="handleLogout()" class="flex items-center space-x-1.5 px-3 py-1.5 text-xs font-semibold bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 rounded-lg border border-rose-500/30 transition shadow-sm cursor-pointer" title="Güvenli Çıkış">
              <i data-lucide="log-out" class="w-3.5 h-3.5"></i>
              <span>Çıkış</span>
            </button>
          </div>'''

if header_btn_target in code:
    code = code.replace(header_btn_target, header_btn_replacement, 1)
    print("Added user display & logout button to header!")
else:
    print("header_btn_target not found!")

# 3. Close #app-container before </body>
footer_target = '''  <!-- Footer -->
  <footer class="border-t border-slate-800 py-6 text-center text-xs text-slate-500 bg-[#0d1117]">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div>
        <span class="font-bold text-slate-400">Heritage Cafe & Bakery</span> &copy; 2026. Tüm hakları saklıdır.
      </div>
      <div class="flex items-center space-x-4">
        <span>Ankara / Çankaya</span>
        <span>•</span>
        <span>Reşit Galip Cd. No:18</span>
        <span>•</span>
        <span class="text-amber-400 font-medium">Büyüme & Kârlılık Sistemi</span>
      </div>
    </div>
  </footer>'''

if footer_target in code:
    code = code.replace(footer_target, footer_target + '\n  </div><!-- End #app-container -->', 1)
    print("Closed #app-container before footer/scripts!")
else:
    print("footer_target not found!")

# 4. Add Authentication Logic to JavaScript
auth_js = '''
    // ==========================================
    // AUTHENTICATION & LOGIN MANAGEMENT
    // ==========================================
    const VALID_USERS = [
      { username: 'heritage', password: 'heritage2026', name: 'Heritage Yönetici', role: 'Yönetici' },
      { username: 'admin', password: 'admin2026', name: 'Sistem Yöneticisi', role: 'Süper Admin' },
      { username: 'patron', password: '123456', name: 'İşletme Sahibi', role: 'Yönetici' },
      { username: 'sireen', password: 'heritage2026', name: 'Sireen', role: 'Yönetici' }
    ];

    function checkAuth() {
      const authData = localStorage.getItem('heritage_auth') || sessionStorage.getItem('heritage_auth');
      if (authData) {
        try {
          const parsed = JSON.parse(authData);
          showApp(parsed.username, parsed.name || parsed.username);
          return true;
        } catch (e) {
          clearAuth();
        }
      }
      showLogin();
      return false;
    }

    function showLogin() {
      const loginContainer = document.getElementById('login-container');
      const appContainer = document.getElementById('app-container');
      if (loginContainer) loginContainer.classList.remove('hidden');
      if (appContainer) appContainer.classList.add('hidden');
      lucide.createIcons();
    }

    function showApp(username, displayName) {
      const loginContainer = document.getElementById('login-container');
      const appContainer = document.getElementById('app-container');
      if (loginContainer) loginContainer.classList.add('hidden');
      if (appContainer) appContainer.classList.remove('hidden');

      const userDisplay = document.getElementById('current-user-display');
      if (userDisplay) {
        userDisplay.textContent = displayName || username;
      }

      // Render dashboard tabs
      renderFinanceTab();
      renderOrdersTab();
      renderSalaryTab();
      lucide.createIcons();
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      const uInput = document.getElementById('login-username').value.trim().toLowerCase();
      const pInput = document.getElementById('login-password').value;
      const remember = document.getElementById('login-remember').checked;
      const errBox = document.getElementById('login-error');
      const errMsg = document.getElementById('login-error-msg');

      const matchedUser = VALID_USERS.find(u => u.username.toLowerCase() === uInput && u.password === pInput);

      if (matchedUser) {
        errBox.classList.add('hidden');
        const authObj = {
          username: matchedUser.username,
          name: matchedUser.name,
          role: matchedUser.role,
          loginAt: new Date().toISOString()
        };

        if (remember) {
          localStorage.setItem('heritage_auth', JSON.stringify(authObj));
        } else {
          sessionStorage.setItem('heritage_auth', JSON.stringify(authObj));
        }

        showApp(matchedUser.username, matchedUser.name);
      } else {
        errBox.classList.remove('hidden');
        errMsg.textContent = 'Kullanıcı adı veya şifre hatalı! Lütfen tekrar kontrol edin.';
        lucide.createIcons();

        // Shake animation
        const card = document.querySelector('#login-container .glass-card');
        if (card) {
          card.classList.add('translate-x-2');
          setTimeout(() => card.classList.remove('translate-x-2'), 100);
          setTimeout(() => card.classList.add('-translate-x-2'), 200);
          setTimeout(() => card.classList.remove('-translate-x-2'), 300);
        }
      }
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
      localStorage.removeItem('heritage_auth');
      sessionStorage.removeItem('heritage_auth');
    }

    function togglePasswordVisibility() {
      const pInput = document.getElementById('login-password');
      const icon = document.getElementById('password-toggle-icon');
      if (pInput.type === 'password') {
        pInput.type = 'text';
        icon.setAttribute('data-lucide', 'eye-off');
      } else {
        pInput.type = 'password';
        icon.setAttribute('data-lucide', 'eye');
      }
      lucide.createIcons();
    }

    function fillDemoCredentials(u, p) {
      const uInput = document.getElementById('login-username');
      const pInput = document.getElementById('login-password');
      if (uInput) uInput.value = u;
      if (pInput) pInput.value = p;
      const errBox = document.getElementById('login-error');
      if (errBox) errBox.classList.add('hidden');
      const submitBtn = document.getElementById('login-submit-btn');
      if (submitBtn) submitBtn.focus();
    }

    function showPasswordHint() {
      alert('Tanımlı Giriş Bilgileri:\\n\\nKullanıcı Adı: heritage (veya admin)\\nŞifre: heritage2026 (veya admin2026)');
    }
'''

# Replace DOMContentLoaded handler with checkAuth
init_target = '''    // Initial Load
    window.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      renderFinanceTab();
      renderOrdersTab();
      renderSalaryTab();
    });'''

init_replacement = auth_js + '''
    // Initial Load
    window.addEventListener('DOMContentLoaded', () => {
      checkAuth();
    });'''

if init_target in code:
    code = code.replace(init_target, init_replacement, 1)
    print("Replaced initial load with checkAuth() and auth logic!")
else:
    print("init_target not found!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_portal.py updated successfully!")

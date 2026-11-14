import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Header with Official Website Link & Slogan
old_header_sub = '<p class="text-xs text-slate-400">Finansal Yönetim, Sipariş Analitiği & Büyüme Portalı (Temmuz – Ekim 2026)</p>'
new_header_sub = '''<p class="text-xs text-slate-400 flex items-center gap-2">
              <span>Finansal Yönetim & Büyüme Portalı</span>
              <span>•</span>
              <a href="https://heritagecafe.com.tr" target="_blank" class="text-amber-400 hover:text-amber-300 font-medium flex items-center gap-1 underline underline-offset-2">
                heritagecafe.com.tr <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
              <span>•</span>
              <span class="text-slate-500 italic">"Save the Heritage"</span>
            </p>'''

if old_header_sub in code:
    code = code.replace(old_header_sub, new_header_sub, 1)
    print("Updated header subtitle with website link!")

# 2. Update Footer with hours and official site
old_footer = '''      <p>Heritage Cafe & Bakery · 100. Yıl, Reşit Galip St. No:18, Çankaya/ANKARA · Tel: 0 534 592 70 12</p>
      <p class="text-slate-400 font-medium">Finansal Raporlama & Pazarlama Portalı 2026</p>'''

new_footer = '''      <div>
        <p class="font-semibold text-slate-300">Heritage Cafe & Bakery · 100. Yıl, Reşit Galip Cd. No:18, Çankaya/ANKARA</p>
        <p class="text-slate-500 text-[11px] mt-0.5">
          Çalışma Saatleri: H.içi 08:00 – 18:00 | Cmt 08:00 – 15:00 | Pazar Kapalı · Tel: 0 534 592 70 12 · 
          <a href="https://heritagecafe.com.tr" target="_blank" class="text-amber-400 underline">heritagecafe.com.tr</a>
        </p>
      </div>
      <p class="text-slate-400 font-medium">"El Emeğiyle Yaşatılan Lezzetler · Save the Heritage"</p>'''

if old_footer in code:
    code = code.replace(old_footer, new_footer, 1)
    print("Updated footer with official hours & website!")

# 3. Update Pazar to Cumartesi in 3-day posting routine
old_routine_sun = '''            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-amber-300 flex items-center gap-1.5"><i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Pazar (Saat 11:00): Zanaat & Hafta Sonu Kahvesi</span>
                <span class="text-[10px] text-slate-500 font-mono">IG Karusel + Shorts</span>
              </div>
              <p class="text-slate-400">Taş fırından çıkış anı, fırıncı mutfak sırrı veya hafta sonu dinlendirici kafe atmosferi.</p>
            </div>'''

new_routine_sat = '''            <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-amber-300 flex items-center gap-1.5"><i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Cumartesi (Saat 09:30): Hafta Sonu Taze Fırın Kahvaltısı</span>
                <span class="text-[10px] text-slate-500 font-mono">IG Karusel + Shorts</span>
              </div>
              <p class="text-slate-400">Taş fırından taze ciabatta/focaccia sandviçler ve sıcak Cinnabon. "Pazar kapalıyız, Cumartesi saat 15:00'e kadar bekliyoruz!" vurgusu.</p>
            </div>'''

if old_routine_sun in code:
    code = code.replace(old_routine_sun, new_routine_sat, 1)
    print("Updated Sunday routine to Saturday 09:30 breakfast!")

# 4. Update Audit Item 2 to explicitly mention heritagecafe.com.tr
old_item_2 = 'desc: "Bioya: Ankara/Çankaya Reşit Galip No:18, Kapanış 18:00, Harita, Menü ve Trendyol Go linki ekleyin.",'
new_item_2 = 'desc: "Bioya: heritagecafe.com.tr web sitesi, Ankara/Çankaya Reşit Galip No:18, Çalışma saatleri ve WhatsApp sipariş linkini ekleyin.",'

if old_item_2 in code:
    code = code.replace(old_item_2, new_item_2, 1)
    print("Updated audit item 2 with official site!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_portal.py updated successfully!")

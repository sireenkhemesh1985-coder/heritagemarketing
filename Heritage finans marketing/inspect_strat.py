with open('build_portal.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1330, 2120):
    l = lines[i]
    if '<h3' in l or '<h2' in l or 'Strateji' in l or 'IVF' in l or 'class="card' in l or 'border-slate-800' in l:
        if any(keyword in l for keyword in ['Strateji', 'Hammadde', 'Tedarik', 'Hastane', 'IVF', 'Bütçe', 'Maliyet']):
            print(f"Line {i+1}: {l.strip()[:100]}")

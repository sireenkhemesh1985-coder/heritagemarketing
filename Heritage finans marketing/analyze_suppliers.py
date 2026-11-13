import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('portal_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Toplam Gider Faturası: {len(d.get('giderler', []))}")

cnr_items = []
manav_items = []
migros_items = []
other_items = []

for g in d.get('giderler', []):
    t = g.get('tedarikci', '')
    cat = g.get('kategori', '')
    val = float(g.get('excel_tutar', 0))
    if 'CNR' in cat or 'CNR' in t:
        cnr_items.append((g.get('tarih'), t, val))
    elif 'Manav' in cat or 'Güleryüz' in t or 'Gler' in t:
        manav_items.append((g.get('tarih'), t, val))
    elif 'Migros' in cat or 'Migros' in t:
        migros_items.append((g.get('tarih'), t, val))
    else:
        other_items.append((g.get('tarih'), t, val))

print(f"\n--- CNR GIDA ({len(cnr_items)} fatura, Toplam: {sum(x[2] for x in cnr_items):,.2f} TL) ---")
for x in cnr_items[:10]:
    print(f"  {x[0]} | {x[1]} | {x[2]:,.2f} TL")

print(f"\n--- MANAV ({len(manav_items)} fatura, Toplam: {sum(x[2] for x in manav_items):,.2f} TL) ---")
for x in manav_items[:10]:
    print(f"  {x[0]} | {x[1]} | {x[2]:,.2f} TL")

print(f"\n--- MIGROS ({len(migros_items)} fatura, Toplam: {sum(x[2] for x in migros_items):,.2f} TL) ---")
for x in migros_items:
    print(f"  {x[0]} | {x[1]} | {x[2]:,.2f} TL")

print(f"\n--- DİĞER ({len(other_items)} fatura, Toplam: {sum(x[2] for x in other_items):,.2f} TL) ---")
for x in other_items[:15]:
    print(f"  {x[0]} | {x[1]} | {x[2]:,.2f} TL")

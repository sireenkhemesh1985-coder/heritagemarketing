import openpyxl
import sys
from collections import defaultdict

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Heritage_Cafe_Muhasebe.xlsx', data_only=True)
ws = wb['Fatura kalemleri']

items = []
by_product = defaultdict(lambda: {'count': 0, 'qty_list': [], 'total_tl': 0.0, 'unit_prices': []})

for row in ws.iter_rows(min_row=2, values_only=True):
    if not any(row):
        continue
    fatura_no, f_date, idx, prod, qty, unit_price, kdv, total_no_kdv, src = row[:9]
    if prod:
        prod_clean = str(prod).strip()
        u_p = float(unit_price or 0)
        tot = float(total_no_kdv or 0)
        if tot == 0 and u_p > 0:
            # estimate
            tot = u_p
        by_product[prod_clean]['count'] += 1
        by_product[prod_clean]['qty_list'].append(str(qty))
        by_product[prod_clean]['total_tl'] += tot
        by_product[prod_clean]['unit_prices'].append(u_p)

sorted_prods = sorted(by_product.items(), key=lambda x: x[1]['total_tl'], reverse=True)

print(f"Toplam Tekil Ürün Kalemi: {len(sorted_prods)}")
print("\n--- EN ÇOK HARCAMA YAPILAN İLK 30 ÜRÜN KALEMİ ---")
for p, d in sorted_prods[:30]:
    avg_price = sum(d['unit_prices']) / len(d['unit_prices']) if d['unit_prices'] else 0
    print(f"{p:<45} | Toplam: {d['total_tl']:>9.2f} TL | Alım Sayısı: {d['count']:>2} | Birim Fiyat Ort: {avg_price:>7.2f} TL | Örnek Miktar: {d['qty_list'][0]}")

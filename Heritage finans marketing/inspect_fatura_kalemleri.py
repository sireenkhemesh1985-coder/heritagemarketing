import openpyxl
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Heritage_Cafe_Muhasebe.xlsx', data_only=True)
ws = wb['Fatura kalemleri']

headers = [cell.value for cell in ws[1]]
print("Headers:", headers)

rows = []
for row in ws.iter_rows(min_row=2, values_only=True):
    if any(row):
        rows.append(row)

print(f"Toplam Fatura Kalemi: {len(rows)}")
for r in rows[:20]:
    print(r[:7])

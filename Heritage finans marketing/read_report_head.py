import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
path = r'C:\Users\sireen.khemesh\.gemini\antigravity\brain\6bc0ebe0-bf6e-4d46-9ff9-4b695826a984\Heritage_Finans_Pazarlama_Raporu.md'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(10, 30):
    print(f"{i+1}: {lines[i]}", end='')

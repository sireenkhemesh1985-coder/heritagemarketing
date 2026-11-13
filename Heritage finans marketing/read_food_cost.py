import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1793, 1850):
    print(lines[i], end='')

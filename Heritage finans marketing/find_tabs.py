import sys

with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("build_portal length:", len(text))
lines = text.split('\n')
for i, l in enumerate(lines):
    if 'tab-strategy' in l or 'tab-forecast' in l:
        print(f"Line {i}: {l[:80]}")

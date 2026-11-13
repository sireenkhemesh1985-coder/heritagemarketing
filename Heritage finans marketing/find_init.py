with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'lucide\.createIcons', text)]
print("lucide.createIcons matches count:", len(matches))
for pos in matches:
    start = max(0, pos - 150)
    end = min(len(text), pos + 150)
    print("--- MATCH ---")
    print(text[start:end])

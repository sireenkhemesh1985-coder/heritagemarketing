with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'alert\(', text)]
for pos in matches:
    print(text[pos-20:pos+100])

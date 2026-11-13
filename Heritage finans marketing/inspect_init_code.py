import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("window.addEventListener('DOMContentLoaded'")
if pos != -1:
    print(text[pos-200:pos+350])

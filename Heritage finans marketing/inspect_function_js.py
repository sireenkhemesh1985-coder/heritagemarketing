import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function handleLoginSubmit')
print('function handleLoginSubmit pos:', pos)
if pos != -1:
    print(text[pos-50:pos+800])

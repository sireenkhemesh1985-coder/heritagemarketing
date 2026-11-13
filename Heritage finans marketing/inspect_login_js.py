import sys
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('handleLoginSubmit')
print('handleLoginSubmit pos:', pos)
if pos != -1:
    print(text[pos-100:pos+800])

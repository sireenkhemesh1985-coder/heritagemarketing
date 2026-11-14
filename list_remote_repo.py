import urllib.request
import json

req = urllib.request.Request(
    'https://api.github.com/repos/sireenkhemesh1985-coder/heritagemarketing/contents', 
    headers={'User-Agent': 'Mozilla/5.0'}
)

try:
    with urllib.request.urlopen(req) as resp:
        contents = json.loads(resp.read().decode())
        print('Files on remote repo:')
        for item in contents:
            print(f" - {item['name']} ({item['size']} bytes)")
except Exception as e:
    print("Error:", e)

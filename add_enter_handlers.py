with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Add onkeydown to inputs
old_u = 'id="login-username" required autocomplete="username" placeholder="heritage" class="'
new_u = 'id="login-username" onkeydown="if(event.key===\'Enter\') handleLoginSubmit(event)" required autocomplete="username" placeholder="heritage" class="'

old_p = 'id="login-password" required autocomplete="current-password" placeholder="••••••••" class="'
new_p = 'id="login-password" onkeydown="if(event.key===\'Enter\') handleLoginSubmit(event)" required autocomplete="current-password" placeholder="••••••••" class="'

if old_u in text:
    text = text.replace(old_u, new_u, 1)
    print("Added enter handler to username input!")
if old_p in text:
    text = text.replace(old_p, new_p, 1)
    print("Added enter handler to password input!")

with open('build_portal.py', 'w', encoding='utf-8') as f:
    f.write(text)

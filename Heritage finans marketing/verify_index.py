with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'id="login-container"' in text, 'login-container missing!'
assert 'id="app-container" class="hidden"' in text, 'app-container missing!'
assert 'function checkAuth()' in text, 'checkAuth missing!'
assert 'handleLoginSubmit' in text, 'handleLoginSubmit missing!'
assert 'handleLogout' in text, 'handleLogout missing!'
assert 'current-user-display' in text, 'current-user-display missing!'
print('All integrity assertions passed successfully!')

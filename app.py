import os
import sys

# Streamlit varsayılan ana dosya yönlendirmesi
# streamlit_app.py dosyasını çalıştırır
current_dir = os.path.dirname(os.path.abspath(__file__))
streamlit_app_path = os.path.join(current_dir, "streamlit_app.py")

with open(streamlit_app_path, "r", encoding="utf-8") as f:
    code = f.read()

exec(code)

import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit sayfa yapılandırması
st.set_page_config(
    page_title="Heritage Cafe & Bakery — Yönetim Portalı",
    page_icon="🥐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit arayüzünü tam ekran ve kusursuz yapmak için CSS
st.markdown("""
<style>
    /* Streamlit varsayılan başlık ve altbilgilerini gizle */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stDecoration"] {visibility: hidden;}
    
    /* Sayfa boşluklarını sıfırla */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* Iframe'i tam ekran yap */
    iframe {
        width: 100% !important;
        min-height: 100vh !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Ana dizin ve dosya yolları
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # portal_data.js dosyasını doğrudan HTML içine göm (Cloud uyumluluğu için)
    js_path = os.path.join(current_dir, "portal_data.js")
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f_js:
            js_code = f_js.read()
        html_content = html_content.replace(
            '<script src="portal_data.js"></script>',
            f'<script>\n{js_code}\n</script>'
        )
    
    # HTML portalını Streamlit componenti olarak yayınla
    components.html(html_content, height=1600, scrolling=True)
else:
    st.error("index.html dosyası bulunamadı! Lütfen build_portal.py dosyasını çalıştırınız.")

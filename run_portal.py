# -*- coding: utf-8 -*-
"""
Local server runner for Heritage Cafe & Bakery Portal
Starts a local HTTP server and opens index.html in the default web browser.
"""
import http.server
import socketserver
import webbrowser
import threading
import time
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    time.sleep(1.0)
    url = f"http://localhost:{PORT}/index.html"
    print(f"Tarayıcı açılıyor: {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Tarayıcı açma hatası: {e}")

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    print("=" * 60)
    print(" Heritage Cafe & Bakery — Finans & Satış Portalı")
    print(f" Yerel Sunucu Portu: {PORT}")
    print(f" Web Portalı: http://localhost:{PORT}/index.html")
    print("=" * 60)
    
    # Sadece parametre ile veya doğrudan çalıştırıldığında tarayıcı aç
    if "--no-browser" not in sys.argv:
        threading.Thread(target=open_browser, daemon=True).start()
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        while True:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nSunucu kullanıcı tarafından kapatıldı.")
                break
            except Exception as e:
                # Bağlantı sıfırlanması veya sekme kapanması durumunda sunucunun çökmesini engelle
                time.sleep(0.5)

import time

from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)
CORS(app)

def get_page_text(url):

    options = Options()
    options.add_argument("--headless")  # Ativa o modo headless
    options.add_argument("--no-sandbox")  # Para evitar problemas de sandbox no ambiente headless
    options.add_argument("--disable-dev-shm-usage")  # Reduz problemas com a memória compartilhada]
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36")

    navegador = webdriver.Chrome(options=options)

    navegador.get(url)
    time.sleep(2)
    page_html = navegador.page_source
    navegador.quit()

    soup = BeautifulSoup(page_html, "html.parser")
    page_text = soup.get_text(separator="\n", strip=True)
    
    return page_text

@app.route('/extract', methods=['POST'])
def extract_text():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    print(f"📌 URL recebida: {url}")  # <-- Adiciona log

    text = get_page_text(url)
    return jsonify({"text": text})


if __name__ == '__main__':
    app.run(debug=True)

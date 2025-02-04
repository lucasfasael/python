from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def accept_cookies(navegador):
    try:
        
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'aceitar') or contains(text(), 'OK') or contains(text(), 'accept')]"))
        )
        
        # Tenta clicar no botão de aceitação
        buttons = navegador.find_elements(By.XPATH, "//button[contains(text(), 'aceitar') or contains(text(), 'OK') or contains(text(), 'accept')]")
        if buttons:
            buttons[0].click()
            print("Cookies aceitos com sucesso!")
            return True
        
        # Caso não encontre, tenta verificar se está dentro de um iframe
        iframe = navegador.find_elements(By.TAG_NAME, "iframe")
        if iframe:
            navegador.switch_to.frame(iframe[0])  # Acessa o iframe
            buttons = navegador.find_elements(By.XPATH, "//button[contains(text(), 'aceitar') or contains(text(), 'OK') or contains(text(), 'accept')]")
            if buttons:
                buttons[0].click()
                print("Cookies aceitos com sucesso dentro de iframe!")
                navegador.switch_to.default_content()
                return True
        print("Botão de aceitar cookies não encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao tentar aceitar cookies: {e}")
        return False

def get_page_text(url):

    options = Options()
    options.add_argument("--headless")
    navegador = webdriver.Chrome(options=options)

    navegador.get(url)
    accept_cookies(navegador)

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
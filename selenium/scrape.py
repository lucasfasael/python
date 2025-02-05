import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Função para download 
def download():
    pdfs = driver.find_elements(By.CLASS_NAME, 'mat-mdc-button-touch-target')

    # Localiza o elemento usando o XPath fornecido
    element = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/header/div[2]/mat-paginator/div/div/div[2]/div')

    texto = element.text  

    numeros = texto.split(" - ")

    numero_inicio = int(numeros[0].strip())
    numero_fim = int(numeros[1].strip().split(" ")[0])

    resultado = numero_fim - numero_inicio + 1

    for index, pdf in enumerate(pdfs):
        
        if index == resultado:
            break
        time.sleep(1)

        # Muda para o próximo baseado no index
        pdf_xpath = f'//*[@id="lista-resultado__itens"]/ul/li[{index+1}]/div/div/div[2]/button[2]/span[4]'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pdf_xpath)))
        
        # Tenta baixar o mesmo arquivo novamente em caso de falha
        download_successful = False
        while not download_successful:
            try:
                # Clica no botão para abrir o menu de download
                pdf = driver.find_element(By.XPATH, pdf_xpath)
                pdf.click()

                # Espera até que o botão real de download esteja disponível
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mat-mdc-menu-item')))

                # Clica no botão real para iniciar o download
                pdf_real = driver.find_element(By.CLASS_NAME, 'mat-mdc-menu-item')
                pdf_real.click()

                # Espera até o ícone de carregamento desaparecer (indicando que o download foi iniciado)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.invisibility_of_element((By.CLASS_NAME, "tcu-spinner")))

                # Dá uma pequena pausa para garantir que o download foi iniciado
                time.sleep(1)

                # Se não houve exceção até aqui, o download foi bem-sucedido
                download_successful = True

            except Exception as e:
                print(f"Erro ao tentar baixar o arquivo no índice {index+1}: {e}")
                print("Tentando novamente...")
            
                time.sleep(3)

#Função para avançar para a próxima página
def nextPage():
    nextPage = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/footer/mat-paginator/div/div/div[2]/button[2]/span[4]')
    nextPage.click()
    time.sleep(2)

#Espera e fecha o modal
def fecharModal():
    modal_xpath = '//*[@id="cdk-overlay-0"]/app-aviso-tags-anotacoes-favoritos/div/div/div[1]/button/span[5]'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, modal_xpath)))
    modal = driver.find_element(By.XPATH, modal_xpath)
    modal.click()

time.sleep(3)

#Configuração do Selenium WebDriver
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)

#Acessa a página
url = 'https://pesquisa.apps.tcu.gov.br/pesquisa/acordao-completo'
driver.get(url)

time.sleep(3)

fecharModal()

#Data de ínicio e fim da pesquisa
input_date1 = driver.find_element(By.ID, 'datainiciosessao') 
input_date2 = driver.find_element(By.ID, 'datafimsessao') 

# Pergunta ao usuário qual a data inicial e final
print("Qual a data inicial da pesquisa ?")
date1 = input("Digite a data inicial (formato dd/mm/aaaa): ")

print("Qual a data final da pesquisa ?")
date2 = input("Digite a data final (formato dd/mm/aaaa): ")

# Agora, você envia essas datas para os campos de entrada
input_date1.send_keys(date1)
input_date2.send_keys(date2)

print(f"Data inicial: {date1}")
print(f"Data final: {date2}")

#Executar a pesquisa
pesquisar = driver.find_element(By.CLASS_NAME, 'barra-botoes__pesquisar')
pesquisar.click()

time.sleep(3)

# Encontrando o botão "Próxima Página"
nextPageButton = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/footer/mat-paginator/div/div/div[2]/button[2]')

# Verificando o atributo 'disabled'
disabled_attribute = nextPageButton.get_attribute('disabled')

# Lógica de loop para navegar até a última página
while True:
    
    # Encontrando o botão "Próxima Página"
    nextPageButton = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/footer/mat-paginator/div/div/div[2]/button[2]')
    
    # Verificando o atributo 'disabled' do botão
    disabled_attribute = nextPageButton.get_attribute('disabled')
    
    # Se o botão estiver desabilitado, significa que você chegou à última página
    if disabled_attribute:
        print("Botão 'Próxima Página' está desabilitado, você está na última página.")
        download()
        break  # Sai do loop, pois chegou à última página
    else:
        print("Botão 'Próxima Página' está habilitado, há mais páginas.")
        download()
        time.sleep(2)
        nextPage()


driver.quit()
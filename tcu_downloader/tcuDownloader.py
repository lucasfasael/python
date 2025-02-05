import os
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def download():
    pdfs = driver.find_elements(By.CLASS_NAME, 'mat-mdc-button-touch-target')

    for index, pdf in enumerate(pdfs):
        if index == 20:
            break
        time.sleep(1)
        pdf_xpath = f'//*[@id="lista-resultado__itens"]/ul/li[{index+1}]/div/div/div[2]/button[2]/span[4]'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pdf_xpath)))
        
        download_successful = False
        while not download_successful:
            try:
                pdf = driver.find_element(By.XPATH, pdf_xpath)
                pdf.click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mat-mdc-menu-item')))
                pdf_real = driver.find_element(By.CLASS_NAME, 'mat-mdc-menu-item')
                pdf_real.click()
                wait = WebDriverWait(driver, 10)
                wait.until(EC.invisibility_of_element((By.CLASS_NAME, "tcu-spinner")))
                time.sleep(1)
                download_successful = True
            except Exception as e:
                print(f"Erro ao tentar baixar o arquivo no índice {index+1}: {e}")
                print("Tentando novamente...")
                time.sleep(3)

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)

url = 'https://pesquisa.apps.tcu.gov.br/pesquisa/acordao-completo'
driver.get(url)

time.sleep(3)

modal_xpath = '//*[@id="cdk-overlay-0"]/app-aviso-tags-anotacoes-favoritos/div/div/div[1]/button/span[5]'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, modal_xpath)))
modal = driver.find_element(By.XPATH, modal_xpath)
modal.click()

time.sleep(3)

input_date1 = driver.find_element(By.ID, 'datainiciosessao') 
input_date2 = driver.find_element(By.ID, 'datafimsessao') 

print("Qual a data inicial da pesquisa ?")
date1 = input("Digite a data inicial (formato dd/mm/aaaa): ")

print("Qual a data final da pesquisa ?")
date2 = input("Digite a data final (formato dd/mm/aaaa): ")

input_date1.send_keys(date1)
input_date2.send_keys(date2)

print(f"Data inicial: {date1}")
print(f"Data final: {date2}")

pesquisar = driver.find_element(By.CLASS_NAME, 'barra-botoes__pesquisar')
pesquisar.click()

time.sleep(3)

nextPageButton = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/footer/mat-paginator/div/div/div[2]/button[2]')

disabled_attribute = nextPageButton.get_attribute('disabled')

while True:
    print('Entrou 1')
    nextPageButton = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/footer/mat-paginator/div/div/div[2]/button[2]')
    disabled_attribute = nextPageButton.get_attribute('disabled')
    
    if disabled_attribute:
        print("Botão 'Próxima Página' está desabilitado, você está na última página.")
        break
    else:
        print("Botão 'Próxima Página' está habilitado, há mais páginas.")
        download()
        time.sleep(2)
        nextPage = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/footer/mat-paginator/div/div/div[2]/button[2]/span[4]')
        nextPage.click()
        time.sleep(2)

driver.quit()

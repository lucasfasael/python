#import matplotlib
from io import StringIO
from time import sleep

import cv2
import pandas as pd
import requests
from pyzbar import pyzbar

chave = 'Q19ZZQITJ9S2OG5M'


estoque = {}
contatos = [
    {"nome": "Pedro Augusto", "empresa": "Brasilia Distribuidora de alimentos",
        "telefone": "61-991209984"},
    {"nome": "Marques Diniz", "empresa": "Marques Distribuidora de bebidas",
        "telefone": "61-998541200"},
    {"nome": "Sergio Amorin", "empresa": "Rac Distribuidora de alimentos",
        "telefone": "61-3475-7972"},
    {"nome": "Lucas Andrade", "empresa": "DF Distribuidora",
        "telefone": "61-3037-73332"},
    {"nome": "Marcos Silva", "empresa": "Distribuidora de bebidas fale baixo ",
        "telefone": "61-30458920"},
    {"nome": "Swift", "empresa": "Swift", "telefone": "08004002892"},
    {"nome": "Israel Gonçalves  ", "empresa": "Meats distribuidora ",
        "telefone": "61-3042-0340"},
    {"nome": "AMBEV", "empresa": "AMBEV", "telefone": "(61)999351306"}
]


def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = {"nome": nome, "descricao": descricao,
               "preco": preco, "quantidade": quantidade}
    estoque[nome] = produto
    print("Produto adicionado ao estoque com sucesso!")
    if quantidade <= 6:
        print("Alerta de estoque! Recomendamos entrar em contato com um distribuidor")


def remover_produto():
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto removido do estoque com sucesso!")
    else:
        print("Produto não encontrado no estoque")


def fazer_pedido():
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        quantidade = int(input("Digite a quantidade do produto: "))
        if estoque[nome]["quantidade"] >= quantidade:
            estoque[nome]["quantidade"] -= quantidade
            print(f"Pedido de {quantidade} {nome}(s) realizado com sucesso!")
            if estoque[nome]["quantidade"] <= 6:
                opcao = input(
                    "Alerta de estoque! Deseja exibir a lista de contatos para contato? (s/n) ")
                if opcao.lower() == "s":
                    for i, contato in enumerate(contatos):
                        display(
                            f"{i+1}. {contato['nome']} da empresa {contato['empresa']}. Telefone: {contato['telefone']}")
                    escolha = int(
                        input("Digite o número do distribuidor que deseja usar: "))
                    distribuidor = contatos[escolha-1]
                    print(
                        f"Você escolheu o distribuidor {distribuidor['nome']} da empresa {distribuidor['empresa']}.")
                    # faça algo com as informações do distribuidor, como enviar um e-mail ou mensagem de texto
        else:
            print("Não há produtos suficientes em estoque")
    else:
        print("Produto não encontrado no estoque")


def digitalizar_produto():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            print("Código de barras detectado")
            print("Tipo de código: ", obj.type)
            print("Código: ", obj.data)
            nome = obj.data.decode('utf-8')
            if nome in estoque:
                print(
                    f"O produto {nome} está em estoque com quantidade de {estoque[nome]['quantidade']}")
                opcao = input(
                    "Deseja remover o produto digitalmente ou manualmente? (d/m) ")
                if opcao.lower() == "d":
                    del estoque[nome]
                    print(f"Produto {nome} removido do estoque digitalmente.")
                elif opcao.lower() == "m":
                    remover_produto(nome)
                else:
                    print("Opção inválida. Tente novamente.")
            else:
                print("Produto não encontrado no estoque")
                adicionar = input(
                    "Deseja adicionar este produto ao estoque? (s/n) ")
                if adicionar.lower() == "s":
                    descricao = input("Digite a descrição do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    quantidade = int(input("Digite a quantidade do produto: "))
                    produto = {"nome": nome, "descricao": descricao,
                               "preco": preco, "quantidade": quantidade}
                    estoque[nome] = produto
                    print("Produto adicionado ao estoque com sucesso!")
                    if quantidade <= 6:
                        opcao = input(
                            "Alerta de estoque! Deseja exibir a lista de contatos para contato? (s/n) ")
                        if opcao.lower() == "s":
                            for contato in contatos:
                                print(
                                    f"{contato['nome']} da empresa {contato['empresa']}. Telefone: {contato['telefone']}")
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def exibir_estoque():
    for nome, produto in estoque.items():
        print(
            f"Nome: {nome}, Descrição: {produto['descricao']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")


def exibir_acoes():
    # TODAS AS INFORMAÇOES ESTAO SENDO PEGAS DIRETO DO BANCO DE DADOS AO VIVO DO BANCO CENTRAL PELA API
    print("deseja ver as açoes de quais produtos ?")
    sleep(0.3)
    display("[com o valor das açoes e ativos dos produtos pode ajudar voce a fazer um preço que nao lhe prejudique no mercado")
    sleep(0.5)
    print("JBSS3 ==> CARNE BOVINA /DERIVADOS DE FRANGO E PORCO/ DIGITE: [0] ")
    print("CAMIL3==> ARROZ /ALIMENTOS PROCESSADOS NO GERAL/ DIGITE: [1]")
    print("MDIA3==>DERIVADOS DO AGRONEGOCIO/TRIGO/ DIGITE: [2]")
    print("AMBEV3==> BEBIDAS GERAL/ DIGITE: [3]")
    print(
        "deseja consultar alguma empresa gringa ou brasileira para saber o valor de mercado ?[4]")
    escolhas = int(input("quais açoes deseja ver: "))
    if escolhas == 0:
        # INICIO DO SEMANAL
        print("resultados do mercado semanal")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=JBSS3.SA&apikey={chave}&datatype=csv'
        r = requests.get(url)
        tabela = pd.read_csv(StringIO(r.text))
        display(tabela.head(4))
        # FIM DO SEMANAL
        # AQUI VOCE VAI PODER VER A ALTERAÇAO O PREÇO NOS PRODUTOS NO CASO AQUI E DO JBSS3 RESPONSALVE PELA CARNE BRASIL
        acoes = ['JBSS3']
        compilada = pd.DataFrame()
        print("alteraçao de valor e preço baseado no mercado")
        sleep(0.6)
        for acao in acoes:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SA&apikey={chave}&datatype=csv'
            r = requests.get(url)
            tabela = pd.read_csv(StringIO(r.text))
            lista_tabelas = [compilada, tabela]
            compilada = pd.concat(lista_tabelas)
            display(compilada)
    if escolhas == 1:
        # INICIO DO SEMANAL
        display("resultados do mercado semanal")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=CAML3.SA&apikey={chave}&datatype=csv'
        r = requests.get(url)
        tabela = pd.read_csv(StringIO(r.text))
        display(tabela.head(4))
        # FIM DO SEMANAL
        # AQUI VOCE VAI PODER VER A ALTERAÇAO O PREÇO NOS PRODUTOS NO CASO AQUI E DO CAML3.SA ARROZ  E DERIVADOS DO DRIGO RESPONSALVE PELA CARNE BRASIL
        acoes = ['CAML3.SA']
        compilada = pd.DataFrame()
        display("alteraçao de valor e preço baseado no mercado")
        sleep(0.6)
        for acao in acoes:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SA&apikey={chave}&datatype=csv'
            r = requests.get(url)
            tabela = pd.read_csv(StringIO(r.text))
            lista_tabelas = [compilada, tabela]
            compilada = pd.concat(lista_tabelas)
            display(compilada)

    if escolhas == 2:
        display("resultados do mercado semanal")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=MDIA3.SA&apikey={chave}&datatype=csv'
        r = requests.get(url)
        tabela = pd.read_csv(StringIO(r.text))
        display(tabela.head(4))
        # FIM DO SEMANAL
        # AQUI VOCE VAI PODER VER A ALTERAÇAO O PREÇO NOS PRODUTOS NO CASO AQUI E DO DERIVADO DO AGRO RESPONSALVE PELA CARNE BRASIL
        acoes = ['MDIA3.SA']
        compilada = pd.DataFrame()
        display("alteraçao de valor e preço baseado no mercado")
        sleep(0.6)
        for acao in acoes:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SA&apikey={chave}&datatype=csv'
            r = requests.get(url)
            tabela = pd.read_csv(StringIO(r.text))
            lista_tabelas = [compilada, tabela]
            compilada = pd.concat(lista_tabelas)
            display(compilada)
    if escolhas == 3:
        display("resultados do mercado semanal")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=AMBEV3.SA&apikey={chave}&datatype=csv'
        r = requests.get(url)
        tabela = pd.read_csv(StringIO(r.text))
        display(tabela.head(4))
        # FIM DO SEMANAL
        # AQUI VOCE VAI PODER VER A ALTERAÇAO O PREÇO NOS PRODUTOS NO CASO AQUI E DO JBSS3 RESPONSALVE PELA AMBEV BRASIL
        acoes = ['AMBEV3.SA']
        compilada = pd.DataFrame()
        display("alteraçao de valor e preço baseado no mercado")
        sleep(0.6)
        for acao in acoes:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SA&apikey={chave}&datatype=csv'
            r = requests.get(url)
            tabela = pd.read_csv(StringIO(r.text))
            lista_tabelas = [compilada, tabela]
            compilada = pd.concat(lista_tabelas)
            display(compilada)


def exibir_menu():
    print("Bem-vindo ao sistema de gerenciamento de estoque")
    sleep(0.4)
    print("Selecione uma opção:")
    sleep(0.4)
    print("1 - Adicionar produto")
    sleep(0.4)
    print("2 - Remover produto")
    sleep(0.4)
    print("3 - Fazer pedido")
    sleep(0.4)
    print("4 - Digitalizar produto")
    sleep(0.4)
    print("5 - Exibir estoque")
    sleep(0.4)
    print("6- Exibir informações de açoes ")
    sleep(0.4)
    print("7 - Sair")
    sleep(0.4)
    opcao = int(input("Opção: "))
    return opcao


def main():
    while True:
        opcao = exibir_menu()
        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            remover_produto()
        elif opcao == 3:
            fazer_pedido()
        elif opcao == 4:
            digitalizar_produto()
        elif opcao == 5:
            exibir_estoque()
        elif opcao == 6:
            exibir_acoes()
        elif opcao == 7:
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()

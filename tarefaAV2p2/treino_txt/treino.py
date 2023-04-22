nome = "tarefaAV2p2\\treino_txt\\tabela.csv"
tabela = []
media = 0
idade_total = 0
with open(nome, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    
    for linha in linhas:
        conteudo_linha = linha.split(";")
        if(conteudo_linha[1]=="idade"):
            continue
        nome_pessoa, idade, uf = conteudo_linha[0], int(conteudo_linha[1]), conteudo_linha[2]
        tabela.append( (nome_pessoa, idade, uf) )
        arquivo.close()

for registro in tabela:
    idade_total = idade_total + registro[1]
media = idade_total / len(tabela)
    
with open("saida.txt", "w", encoding="utf-8") as arquivo_saida:
    arquivo_saida.write("quantidade;media_idade\n")
    arquivo_saida.write(f"{len(tabela)};{media}")
    arquivo_saida.close()

with open("saida.txt", "r", encoding="utf-8") as teste:
    rows = teste.readlines()
    for row in rows:
        print(row.split(";"))
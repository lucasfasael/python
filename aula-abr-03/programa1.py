path = 'aula-abr-03'

nome = f'{path}\\dados.csv'


dataHead = []
tabela = []
tratandoLinha = []

with open(nome, 'r', encoding='utf-8') as arquivo:

    linhas = arquivo.readlines()
    dataHead = linhas[0].split(',')

    for linha in linhas:

        conteudo_linha = linha.split(",")
        if (conteudo_linha[0] == "DOI"):
            continue

        doi, pmid, arXiv, title = conteudo_linha[0],  conteudo_linha[1], conteudo_linha[2], conteudo_linha[3]
        conteudo_linha.pop(0)
        conteudo_linha.pop(0)
        conteudo_linha.pop(0)
        conteudo_linha.pop(0)

        year = conteudo_linha[len(conteudo_linha) - 1]
        journal = conteudo_linha[len(conteudo_linha) - 2]
        conteudo_linha.pop()
        conteudo_linha.pop()

        conteudo_linha = ','.join(conteudo_linha).split('"')

        conteudo_linha.reverse()

        authors = conteudo_linha[1]
        conteudo_linha.pop(1)

        abstract = ','.join(conteudo_linha).strip(',')

        tabela.append((doi, pmid, arXiv, title,
                      abstract, authors, journal, year))

    arquivo.close()


with open(f'{path}/saida.html', 'w', encoding='utf-8') as arq_saida:

    arq_saida.write('''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Artigos selecionados</title>
    <style>
    table{
    text-align: center;
    border-collapse: collapse;
    width: 95%;
    border-radius: 8px;
    font-weight: 400;
    letter-spacing: 3px;
    color: #000000;
    background: rgb(126, 251, 255);
    box-shadow: 0px 10px 40px -12px rgb(10, 65, 67);
}
body{
    background: rgb(92, 135, 208);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
h1{
    text-align: center;
    font-size: 50px;
    color: yellow;
}
td{
    border: 3px solid black;
}
.dado{
    border: 3px solid black;
    background-color: rgb(7, 217, 14);
    font-size: 40px;
}
</style>
</head>
<body>
    ''')

    arq_saida.write('<h1>Artigos selecionados</h1>')

    # LOGICA
    arq_saida.write('<table>')

    arq_saida.write('<tr>')

    for index, elemento in enumerate(dataHead):
        if (index == 1 or index == 2 or index == 4):
            continue

        arq_saida.write(f'<th class="dado"> {elemento} </th>')

    arq_saida.write('</tr>')
    for linha in tabela:
        arq_saida.write('<tr>')

        for index, elemento in enumerate(linha):
            if (index == 1 or index == 2 or index == 4):
                continue

            arq_saida.write(f'<td> {elemento} </td>')

    arq_saida.write('</tr>')
    arq_saida.write('''
</body>
</html>
    ''')
    arq_saida.close()

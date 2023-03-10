idades = [15, 18, 12]
aprovados = []

def permissao(idades, aprovados):
    for idade in idades:
        if idade >= 18:
            aprovados.append(True)
        else:
            aprovados.append(False)

permissao(idades, aprovados)
for aprovado in aprovados:
    if aprovado == True:
        print("Tem permissão")
    else:
        print("Não tem permissão")


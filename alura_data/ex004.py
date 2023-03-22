idades = []
aprovados = []
x = 0


def isAble(idades, aprovados):
    condicao = 1
    while condicao == 1:
        idade = int(input("Qual a idade ? : "))
        idades.append(idade)
        condicao = int(
            input("Você quer inserir outra idade ? (0 = não, 1 = sim) : "))
    for idade in idades:
        if idade >= 18:
            aprovados.append(True)
        else:
            aprovados.append(False)


isAble(idades, aprovados)

for aprovado in aprovados:
    if aprovado == True:
        print(f"A idade : {idades[x]}, é apta")
    else:
        print(f"A idade : {idades[x]}, NÃO é apta")
    x = x + 1

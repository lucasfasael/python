comidas = ["Maça", "Batata", "Cenoura", "Arroz"]

precos = [2.13, 4.5, 3.2, 2.73]


total = 0

resposta = input("Você quer Maça, Batata, Cenoura ou Arroz ? : ")
lista = resposta.split(", ")


for item in lista:

    cont = 0
    contem = 0

    for comida in comidas:

        if(item.upper() == comida.upper()):

            total = total + precos[cont]
            contem = contem + 1

        cont = cont + 1

    if(contem == 0):

        print(f"O produto {item} não é uma opção valida ! ")


variavelTratada = str(round(total, 2)).replace(".", ",")


print(f"O total das compras foi: R$ {variavelTratada} ")

lista = []
x = 0
for x in range(5):
    lista.append(float(input("Qual a nota do {}° aluno ?: ".format(x+1))))

soma = (sum(lista))
media = soma / len(lista)

print("A média das notas é {}".format(media))




# lista = []

# x = 0;
# y = 0;
# soma = 0;
# cont = 0;
# media = 0;
# for x in range(4):
#     lista.append (float(input("Qual a venda do funcionario ? : ")))
#     print(lista)
#     soma = lista[x] + soma

# media = soma / len(lista)
# print("A média é {}".format(media))


# for element in lista:
#     if(element < media):
#         print(f"O funcinário de valor {element)} está abaixo da média.")

"""
 for y in range(4):
     if(lista[y] < media):
         print("O funcionário {} está abaixo da média com o valor de: {}".format(y, lista[y]))
lista.append(45)

 print(len(lista)

 for element in lista

sum(lista)

lista.remove() = remover especifico
lista.pop() = remover o ultimo
lista.push() = adicionar

matriz = [[]]
"""
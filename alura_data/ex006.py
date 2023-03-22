from random import randrange, seed

lista = []
randrange(0, 11)
seed(11)

for notas in range(5):
    lista.append(randrange(0, 11))

print(lista)

lista = []
listaPAR = []
listaIMPAR = []

for x in range(20):
    n = int(input("Qual o {}º número? : ".format(x+1)))
    lista.append(n)
    if(lista[x] % 2 == 0):
        listaPAR.append(lista[x])
    else:
        listaIMPAR.append(lista[x])

print("A lista é: {}".format(lista))
print("Os pares dela são: {}".format(listaPAR))

print("Os impares dela são: {}".format(listaIMPAR))
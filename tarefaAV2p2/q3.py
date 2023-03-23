lista = []
multi = 0

for x in range(5):
    n = int(input("Qual o {}º número da lista ? : ".format(x+1)))
    lista.append(n)
    if(len(lista) == 1 ):
        multi = n
    else:
        multi = multi * n
print("A soma da lista é = {}".format(sum(lista)))
print("A multiplicação da lista é = {}".format(multi))
print("Os números digitados foram: {}".format(lista))

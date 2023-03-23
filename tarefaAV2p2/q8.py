lista = []
x = 50

while(x < 100):
    if(x % 6 == 0):
        lista.append(x)
    x = x + 1

print("Os multiplos de 6 no intervalo são: {}".format(lista))

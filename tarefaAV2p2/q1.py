lista = []
dobrolista = []
pergunta = ''
x = 0
condicao = True

while(condicao):
    n = float(input("Qual o {}º número? : ".format(x+1)))
    lista.append(n)
    dobrolista.append(lista[x] * 2)
    x = x + 1
    pergunta = input("Gostaria de adicionar mais elementos a lista ? Digite 's' ou 'n' : ")
    if(pergunta == 'n' or len(lista) >= 20):
        condicao = False

print("A primeira lista é: {}".format(lista))
print("E o dobro dela é: {}".format(dobrolista))
cont = 0
listaA = []
listaI = []
for x in range(5):
    altura = float(input("Qual a altura do {}º aluno ? : ".format(x+1)))
    listaA.append(altura)
    idade = int(input("Qual a idade do {}º aluno ? : ".format(x+1)))
    listaI.append(idade)

media = sum(listaA) / len(listaA)

for y in range(5):
    if(listaA[y] < media and listaI[y] > 13):
        cont = cont + 1

print("Existem {} alunos com mais de 13 anos e abaixo da média de altura dos alunos.".format(cont))
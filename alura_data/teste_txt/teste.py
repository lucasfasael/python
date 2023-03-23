notas = [9.8, 8.3, 7.9, 8, 9.7]
alunos = ['Adriana', 'Caio', 'Livia', 'Solano', 'Tais']

with open('banco.txt','w') as arquivo:
    for x in range(5):
        arquivo.write(alunos[x] + ' ; ' + str(notas[x]) + '\n')

with open('binario.bi','wb') as barquivo:
    for x in range(5):
        barquivo.write(alunos[x] + ' ; ' + notas[x] + '\n')
        
# with open('banco.txt','r+') as arquivo:
#     for aluno in arquivo:
#         print(aluno)
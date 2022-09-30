print("Seja bem vindo ao registro acadêmico da turma !!")
condicao = 1;
x = 0;
y = 0;
mm = 0;

while(condicao):
    matricula = int(input("Qual a matrícula do aluno ? : "))
    if(matricula == -1):
        condicao = 0;
        print("Tem {} alunos com 21 anos ou mais" .format(y))
    elif(matricula != -1):
      nome = input("Qual o nome do {} aluno ? : ".format(x+1))
      n1 = float(input("Quanto o aluno tirou na primeira nota ? : "))
      n2 = float(input("Quanto o aluno tirou na segunda nota ? : "))
      f = int(input("Quantas faltas o aluno possui ? : "))
      ano = int(input("Em que ano o aluno nasceu ? : "))
      media = (n1 + n2) / 2;
      if(ano > 2001):
          y = y + 1;
      if(media > mm):
          mm = media;
          mnome = nome;
          mmatricula = matricula;
          print("A maior média agora é {}".format(mm))
          
    
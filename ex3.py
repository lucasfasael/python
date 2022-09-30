print("Seja bem vindo ao registro acadêmico da turma !!")
condicao = 1;
x = 0;
y = 0;
mm = 0;
nm = 10;
ap = 0;
rp = 0;
rpp = 0;

while(condicao):
    matricula = int(input("Qual a matrícula do {}º aluno ? : ".format(x+1)))
    if(matricula == -1):
        condicao = 0;
        print("O aluno {}, da matrícula: {}, é o aluno com a maior média, atingindo uma média incrível de {}".format(mnome, mmatricula, mm))
        print("O aluno {}, da matrícula: {}, é o aluno com a menor média, atingindo uma média de {}, que decepção ...".format(nnome, nmatricula, nm))
        print("Tem {} alunos com mais de 21 anos." .format(y))
        print("A quantidade de alunos aprovados foi de: {} alunos, sendo que a turma é de {} alunos".format(ap, x))
        print("A quantidade de alunos reprovados foi de: {} alunos, sendo que a turma é de {} alunos".format(rp, x))
        print("Dos alunos reprovados {} tiraram 0 em pelo menos uma das notas.".format(rpp))

    elif(matricula != -1):
      nome = input("Qual o nome do {}º aluno ? : ".format(x+1))
      n1 = float(input("Quanto o aluno tirou na primeira nota ? : "))
      n2 = float(input("Quanto o aluno tirou na segunda nota ? : "))
      f = int(input("Quantas faltas o aluno possui ? : "))
      ano = int(input("Em que ano o aluno nasceu ? : "))
      media = (n1 + n2) / 2;
      x = x+1;
      if(ano < 2001):
          y = y + 1;
      if(media > mm):
          mm = media;
          mnome = nome;
          mmatricula = matricula;
      if(media < nm):
          nm = media;
          nnome = nome;
          nmatricula = matricula;
      if(media >= 7 and f < 22.5):
        ap = ap + 1;
      if(media < 7 or f >= 22.5):
        rp = rp + 1;
      if(n1 == 0 or n2 == 00):
        rpp = rpp + 1;
          
    
nm = 0;
print("Irei informar se o seu número é primo !!!")
for y in range(0, 5):
  n1 = int(input("Qual o seu número ? : "))
  cont = 0;
  for x in range(1, n1 + 1):
      if(n1 % x == 0):
          cont += 1;
  if(cont == 2):
      print("O número {}, é um número primo".format(n1))
      if(n1 > nm):
        nm = n1;
  else:
    print("O número {}, não é um número primo".format(n1))

print("Entre os números primos citados o maior deles é : {}".format(nm))

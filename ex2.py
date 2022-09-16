print("Cardápio: 1 - Cachorro Quente, 2 - X-Salada, 3 - X-Bacon, 4 - Torrada simples, 5 - Refrigerante.")
c = int(input("Qual o código da comida que você gostaria ? : "))
q = int(input("Quantos vão ser ? : "))
valor1 = 4 * q
valor2 = 4.5 * q
valor3 = 5 * q
valor4 = 2 * q
valor5 = 1.5 * q

if(c==1):
    print(valor1)
if(c==2):
    print(valor2)
if(c==3):
    print(valor3)
if(c==4):
    print(valor4)
if(c==5):
    print(valor5)
else:
    print("Escolha um código compatível.")
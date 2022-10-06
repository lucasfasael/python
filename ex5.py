print("Olá, estou aqui para informar se suas medidadas podem formar um triângulo e qual tipo de triângulo ele é !!!")

n1 = float(input("Qual a medida do primeiro lado ? : "))
n2 = float(input("Qual a medida do segundo lado ? : "))
n3 = float(input("Qual a medida do terceiro lado ? : "))

if(n1+n2 > n3 and n2+n3 > n1 and n1+n3 > n2):
    print("Parabéns, suas medidas formam um triângulo !!!")
    if(n1 == n2 == n3):
        print("Seu triângulo é do tipo equilátero !!!")
    elif(n1 == n2 or n2 == n3 or n3 == n1):
        print("Seu triângulo é do tipo isósceles !!!")
    elif(n1 != n2 and n2 != n3 and n3 != n1):
        print("Seu triângulo é do tipo escaleno !!!")

else:
    print("As medidas utilizadas não podem formar um triângulo.")
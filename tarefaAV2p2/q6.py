def soma(n1, n2, n3):
    n4 = n1 + n2 + n3
    if(n1 > n2 and n1 > n3):
        maior = n1
    elif(n2 > n1 and n2 > n3):
        maior = n2
    elif(n3 > n1 and n3 > n2):
        maior = n3
    return ("A soma é igual a : {} e o maior é: {}".format(n4, maior))

n1 = int(input("Qual o primeiro número ? : "))
n2 = int(input("Qual o segundo número ? : "))
n3 = int(input("Qual o terceiro número ? : "))

print(soma(n1,n2,n3))

n1 = int(input("Digite um número"))
n2 = int(input("Digite o segundo número"))

if(n1==n2):
    print("O número %d é igual a %d"%(n1, n2))
elif(n1!=n2):
    print("O número %d é diferente do %d"%(n1, n2))
elif(n1>n2):
    print("O número %d é maior do %d"%(n1, n2))
elif(n1<n2):
    print("O número %d é menor do %d"%(n1, n2))
elif(n1<0):
    print("Tá de palhaçada?")

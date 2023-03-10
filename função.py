def soma(n1, n2):
    n3 = n1 + n2
    return n3

def altera():
    global n1
    n1 = 200
    
n1 = int(input("Qual o primeiro número ? : "))
n2 = int(input("Qual o segundo número ? : "))

altera()
print(soma(n1, n2))
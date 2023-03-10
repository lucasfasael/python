idade = int(input("Qual é a sua idade ? "))

def verificacao(idade):
    if idade >= 18:
        print("Você pode dirigir !")
    else:
        print("Você não pode dirigir !")
        
verificacao(idade)
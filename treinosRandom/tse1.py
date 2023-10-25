lista = []
cont = 0
palavra1 = input("Qual a primeira ? : ")

palavra2 = input("Qual a segunda ? : ")

if(len(palavra1) == len(palavra2)):
    cont = 0
    for letra in palavra1:
        for letra2 in palavra2:
            if(letra == letra2):
                cont = cont + 1
                break
    if (len(palavra1) == cont):
        print("Suas palavras são anagramas")
    else:
        print("Suas palavras não são anagramas!")

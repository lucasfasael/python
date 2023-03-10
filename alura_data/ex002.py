idades = [12, 15, 18, 20, 17]

def verificacao(idades):
    for idade in idades:
        if(idade >= 18):
            print(f'A idade {idade} TEM permissão para dirigir')
        else:
            print(f'A idade {idade} NÃO tem permissão para dirigir')

verificacao(idades)
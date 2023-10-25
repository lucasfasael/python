import requests


class filme:

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def apresenta(self):
        print(f"O nome do filme é {self.nome} e o ano de lançamento é {self.ano}")

filmes = []


movie = input("Qual o filme ? : ")


r = requests.get(f'https://www.omdbapi.com/?t={movie}&apikey=e131c7a5')


splited = r.text.split(':"')


splited2 = splited[1].split('"')


splited3 = splited[2].split('"')

name = splited2[0]
year = splited3[0]

filmes.append(filme(name, year))

print(filmes[0].apresenta())

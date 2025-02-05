class Estagiario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def apresenta(self):
        print(f"O meu nome é {self.nome} e o meu salário é R${self.salario}")


lista = []

for x in range(2):
    name = input("Qual o seu nome novo estagiário ? : ")
    wage = input("Quanto vai ganhar ? : ")
    estagiario = Estagiario(name, wage)
    lista.append(estagiario)

for estagiario in lista:
    estagiario.apresenta()

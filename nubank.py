from array import array
from json.encoder import ESCAPE_ASCII
from multiprocessing.dummy import Array


class Pessoa:
    def __init__(self, nome, credito, debito):
        self.nome = nome
        self.credito = credito
        self.debito = debito

todasPessoas = []
def smallestNegativeBalance(todasPessoas: list):
        pessoasEndividadas = list (filter(filtrarPessoas, todasPessoas))
        print(pessoasEndividadas)

def filtrarPessoas(pessoa: Pessoa):
  if pessoa.debito > pessoa.credito:
    return True
  else:
    return False

adicionarNovasPessoas = True
pessoas = []
while(adicionarNovasPessoas):
    nome = input("Qual o nome ? : ")
    credito = float(input("Qual o cred ? : "))
    debito = float(input("Qual o deb ? : "))
    pessoas.append(Pessoa(nome, credito, debito))
    smallestNegativeBalance(pessoas)


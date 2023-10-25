class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produtos = [produto("Maça", 22), produto("Cenoura", 15)]

total = 0
for produto in produtos:
    total = total + produto.preco

print(f"O seu total foi de: {total}")

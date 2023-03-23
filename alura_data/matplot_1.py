from random import randrange, seed

import matplotlib.pyplot as plt

randrange(0, 11)
seed(11)

x = list(range(1, 9))
y = []


for nota in range(8):
    y.append(randrange(0, 11))

plt.plot(x, y, marker="o")
plt.title("Notas de Matemática")
plt.xlabel("Provas")
plt.ylabel("Notas")
plt.show()

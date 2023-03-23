from random import randrange, seed
import matplotlib.pyplot as plt

x = list(range(0, 9))
y = []
randrange(0, 11)
seed(11)

for nota in range(8):
    y.append(randrange(0, 11))
    
plt.plot(x, y)
plt.title("Notas de Matemática")
plt.xlabel("Prova")
plt.ylabel("Nota")
plt.show()
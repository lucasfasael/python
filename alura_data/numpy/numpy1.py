import numpy as np

km = np.loadtxt("carros-km.txt")
anos = np.loadtxt('carros-anos.txt', dtype=int)
km_media = km / (2023 - anos)
print(km_media)

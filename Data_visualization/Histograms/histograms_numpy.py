import numpy as np

np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=500)

#print(d[:5])
hist, bin_edges = np.histogram(d)

print(hist)
print()
print(bin_edges)
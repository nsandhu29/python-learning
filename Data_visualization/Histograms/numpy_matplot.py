import numpy as np
import matplotlib.pyplot as plt
np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=500)

n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My very own Histogram')
plt.text(23, 24, r'$\mu=15, b=3$')
max_freq = n.max()
plt.ylim(top=np.ceil(max_freq/10) * 10 if max_freq % 10 else max_freq + 10)

plt.show()



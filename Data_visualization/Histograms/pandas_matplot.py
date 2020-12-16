import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

size, scale = 1000, 10

commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)
commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')

plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Commute Time')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)

plt.show()
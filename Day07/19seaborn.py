import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

flights = sns.load_dataset('flights')
# print(flights)
data = flights.pivot('month', 'year', 'passengers')
# print(data)

# plt.pcolor(data)
# plt.xticks(np.arange(0.5, len(data.columns), 1), data.columns)
# plt.yticks(np.arange(0.5, len(data.index), 1), data.index)
# plt.colorbar()


sns.heatmap(data, annot=True, fmt='d', cmap='RdYlGn_r')

plt.show()
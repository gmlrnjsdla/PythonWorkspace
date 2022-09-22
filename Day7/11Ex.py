import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5, 3, 1000)
y = np.random.normal(3, 2, 1000)

fig, ax = plt.subplots()

ax.scatter(x, y, color='pink', label='math score', alpha=0.5)
ax.set_title('2021 Math Score Distribution', fontdict={'fontweight':'bold'})
ax.set_xlabel('score')
ax.set_ylabel('student')
ax.set_xticks([-5, 0, 5, 10, 15])
ax.legend(loc='upper right')
plt.show()
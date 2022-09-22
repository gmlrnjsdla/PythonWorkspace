import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.size'] = 12

fig, ax = plt.subplots()

ax.set_title('Mean Squared Error', pad=20)

ax.set_xlim(-3, 3)
ax.set_ylim(0, 3)
ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax.set_yticks([1, 2, 3])

x = np.linspace(-3, 3, 100)
ax.set_xlabel('score')
ax.set_ylabel('y1 score')
graph1 = ax.plot(x, x**2, color='red', label='kor')
# ax.legend()

ax2 = ax.twinx()
ax2.set_ylabel('y2 score')
graph2 = ax2.plot([1,2,3,4,5],[1,2,3,3,4], label='eng')
# ax2.legend(loc='upper left')

graph3 = graph1 + graph2
labels = [la.get_label() for la in graph3]
ax.legend(graph3, labels, loc='upper right')
plt.show()

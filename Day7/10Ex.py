import matplotlib.pyplot as plt
import numpy as np

y1 = [500, 450, 520, 610]
y2 = [690, 700, 820, 900]
y3 = [1100, 1030, 1200, 1300]
y4 = [1500, 1650, 1700, 1850]
y5 = [1990, 2020, 2300, 2420]
y6 = [1020, 1600, 2200, 2550]
x = ['first', 'second', 'third', 'fourth']


fig, ax1 = plt.subplots()
graph1 = ax1.plot(x, y1, label='2015', linewidth=3)
graph2 = ax1.plot(x, y2, label='2016', linewidth=3)
graph3 = ax1.plot(x, y3, label='2017', linewidth=3)
graph4 = ax1.plot(x, y4, label='2018', linewidth=3)
graph5 = ax1.plot(x, y5, label='2019', linewidth=3)
graph6 = ax1.plot(x, y6, label='2020', linewidth=3)
ax1.set_title('2015~2020 Quarterly sales', fontdict={'fontweight':'bold'})
ax1.set_xlabel('Quarters')
ax1.set_ylabel('sales')


graph7 = graph1 + graph2 + graph3 + graph4 + graph5 + graph6
labels = [la.get_label() for la in graph7]
ax1.legend(graph7, labels, loc='upper left')

plt.show()
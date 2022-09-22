import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.size'] = 12

x = [2020, 2021, 2022, 2023, 2024, 2025, 2026]
y1 = np.array([1, 3, 7, 5, 9, 7, 14])
y2 = np.array([1, 3, 5, 7, 9, 11, 13])

fig, ax1 = plt.subplots()

ax1.plot(x, y1, color='green')

ax2 = ax1.twinx()
ax2.bar(x, y2, color='pink', alpha=0.6)

ax1.set_zorder(ax2.get_zorder()+10)
ax1.patch.set_visible(False)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = np.arange(3)
year = ['2019', '2020', '2021']
values = [300, 800, 100]

plt.bar(x, values, color="pink", width=0.4, edgecolor='black', linewidth=3,
        hatch='\\')    # width default 0.8
plt.xticks(x, year)
plt.show()
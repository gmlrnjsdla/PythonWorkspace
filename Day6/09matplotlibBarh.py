import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

y = np.arange(3)
year = ['2019', '2020', '2021']
values = [300, 800, 100]

plt.barh(y, values, color="pink", height=0.4, edgecolor='black', linewidth=3,
        hatch='\\', tick_label=year)    # width default 0.8

plt.show()
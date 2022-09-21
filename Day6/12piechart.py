import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

ratio = [50,5,30,15]

labels = ['축구', '배구', '야구', '농구']
exp = [0,0,0.1,0]
colors = ['gold', 'purple', 'olive', 'silver']
pieEdge = {'width': 0.7, 'edgecolor': 'black', 'linewidth': 2}

plt.pie(ratio, labels=labels, autopct='%.0f%%', startangle=45,
        explode=exp, shadow=True, colors=colors, wedgeprops=pieEdge)
plt.show()
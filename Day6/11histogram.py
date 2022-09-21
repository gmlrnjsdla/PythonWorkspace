import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# weight = [68, 68, 68, 70, 71, 71, 83, 83, 83, 83, 65, 66, 70, 70, 70, 70, 77, 78, 81, 64, 65, 80]
# plt.hist(weight, edgecolor='black')

a = np.random.rand(10000)
plt.hist(a, bins=100, histtype='step')
plt.show()
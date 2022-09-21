import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

np.random.seed(12312421)

x = np.random.rand(50)  # 0~1사이의 랜덤수를 50개 추출
y = np.random.rand(50)
colors = np.random.rand(50)
area = ((np.random.rand(50) * 30)**2)

plt.scatter(x, y, c=colors, s=area, alpha=0.5)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

arr = np.random.standard_normal((30, 40))     # 표준정규분포 2차원 배열 랜덤생성
plt.matshow(arr)
plt.colorbar(shrink=0.8, aspect=10)

plt.show()

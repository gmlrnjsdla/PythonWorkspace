import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.rc('axes', unicode_minus=False)

# plt.style.use('ggplot')
# plt.style.use('classic')
# plt.style.use('bmh')
plt.rcParams['figure.figsize'] = (10, 5)    # 그래프 이미지 크기
plt.rcParams['font.size'] = 15              # 폰트 크기
plt.plot([1, 2, 3, 4], [5, 6, 7, 8])
plt.show()
# plt.savefig('testGraph.png', dpi=200, facecolor='pink')
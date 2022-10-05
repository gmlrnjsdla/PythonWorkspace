import matplotlib.pyplot as plt
import numpy as np

# 한글폰트 불러오기
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)



a = np.arange(0, 2, 0.2)
plt.plot(a, a, color="gold", marker='*')
plt.plot(a, a**2, color='deeppink', marker='o')
plt.plot(a, a**3, color='olive', marker='^')
xlist = ['공책', '연필', '지우개', '볼펜']
plt.xticks(np.arange(0, 2, 0.5), labels=xlist)
plt.yticks(np.arange(1, 6), ('one', 'two', 'three', 'four', 'five'))

plt.tick_params(axis='x', direction='inout', length=10, pad=20, labelsize=15,
                labelcolor='red', color='blue', width=5)

title_font ={'fontsize':20, 'fontweight':'bold', 'color':'springgreen'}
# plt.title('Test Graph',fontdict={'fontsize':20, 'fontweight':'bold'})
plt.title('그래프 연습',fontdict=title_font, loc='right', pad=0)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)    # 2줄 1칸 표 1번째 위치
plt.plot(x1, y1)
plt.title('첫번째 그래프')

plt.subplot(2, 1, 2)    # 2줄 1칸 표 2번째 위치
plt.plot(x2, y2)
plt.title('두번째 그래프')

plt.tight_layout()  # 그래프 겹침 방지
plt.show()
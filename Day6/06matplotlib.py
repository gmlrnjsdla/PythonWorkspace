import matplotlib.pyplot as plt
import numpy as np

x = [2,4,6,8]
y = [10,20,30,40]
a = np.arange(0,20,0.2)

plt.plot(x, y, color='deeppink', marker='x', linestyle=':', linewidth=10, markersize=10)
plt.plot(a, a, color='olive', marker="+")
plt.xlabel('x-label')   # x축 레이블
plt.ylabel('y-label')   # y축 레이블
plt.axis([0, 20, 0, 60])   # 축 범위 지정
plt.fill_between(x[1:3], y[1:3], color='gold', alpha=0.5)  # 지정범위 채우기(막대)
plt.grid(True, axis='both', color='purple', alpha=0.3, linestyle=':')  # 격자
plt.show()
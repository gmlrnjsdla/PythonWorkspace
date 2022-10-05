import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 12

a1 = np.random.normal(0, 2.0, 1000)
# 평균이 0고 표준편차가 2.0 정규분포를 랜덤으로 1000개 추출
a2 = np.random.normal(-3.0, 1.5, 500)
# 평균이 -3고 표준편차가 1.5 정규분포를 랜덤으로 500개 추출
a3 = np.random.normal(1.2, 1.5, 1500)
# 평균이 1.2고 표준편차가 1.5 정규분포를 랜덤으로 1000개 추출

fig, ax = plt.subplots()

ax.boxplot([a1, a2, a3], notch=True, vert=False)
ax.set_ylim(-10.0, 10.0)

plt.show()

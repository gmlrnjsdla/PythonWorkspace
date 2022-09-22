import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.rc('axes', unicode_minus=False)

a = np.random.randn((10000)) *2 +1
b = np.random.standard_normal(10000)
c = np.random.rand(5000) * 20.0 -10.0
fontStyle1 = {'color': 'blue', 'size': 15, 'weight': 'bold', 'alpha': 0.5}
fontStyle2 = {'color': 'orange', 'size': 15, 'weight': 'bold', 'alpha': 0.5}
fontStyle3 = {'color': 'green', 'size': 15, 'weight': 'bold', 'alpha': 0.5}

plt.hist(a, bins=100, histtype='step')
plt.text(2.5, 300, '정규분포 그래프', fontdict=fontStyle1, rotation=30)
plt.text(0.7, 400, r'$\alpha^2 >\beta_3 +\frac{1}{2} +\sqrt{10} - \sin(a) '
                 r'+\sum_a^b{x} $', fontdict=fontStyle1, rotation=30)
plt.hist(b, bins=50, histtype='stepfilled', )
plt.text(1.6, 500, '표준정규분포 그래프', fontdict=fontStyle2, rotation=30)
plt.hist(c, bins=100, histtype='step')
plt.text(6.0, 90, '랜덤분포 그래프', fontdict=fontStyle3)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_path = 'c:/Windows/Fonts/malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
plt.rc('axes', unicode_minus=False)

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

ax[0][0].plot([1,2,3,4],[5,6,7,8], 'red', label='JAN Score')
ax[0][0].set_title('Graph One')
ax[0][0].legend(loc='best')

ax[0][1].plot([2,5,1,3],[5,6,7,8])
ax[0][1].set_title('Graph Two')

ax[1][0].plot([3,7,1,2],[5,6,7,8])
ax[1][0].set_title('Graph Three')

ax[1][1].plot([11,2,13,14],[5,6,7,8])
ax[1][1].set_title('Graph Four')

plt.show()
import matplotlib.pyplot as plt
import numpy as np
import squarify

size = [40, 30, 5, 25]
label = ['one', 'two', 'three', 'four']

squarify.plot(size, 10, 10, label=label, color=['pink', 'olive', 'gray', 'gold'],
              bar_kwargs=dict(linewidth=3, edgecolor='red'))
plt.axis('off')
plt.show()
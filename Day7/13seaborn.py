import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

fig, ax = plt.subplots(2, 2, figsize=(15, 10))

ax[0][0].hist(iris['sepal_length'], color='blue', alpha=0.5)
ax[0][0].set_title('sepal_length')
ax[0][1].hist(iris['sepal_width'], color='red', alpha=0.5)
ax[0][1].set_title('sepal_width')
ax[1][0].hist(iris['petal_length'], color='green', alpha=0.5)
ax[1][0].set_title('petal_length')
ax[1][1].hist(iris['petal_width'], color='pink', alpha=0.5)
ax[1][1].set_title('petal_width')


plt.show()
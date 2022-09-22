import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

# sns.histplot(iris['sepal_width'])
hist1 = sns.distplot(iris['sepal_width'], bins=10, color='pink',
             kde_kws={'linewidth':4})

hist1.set_title('iris sepal width')
hist1.set_xlabel('sepal width')
hist1.set_ylabel('iris count')
plt.show()

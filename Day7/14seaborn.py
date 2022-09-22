import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

# sns.histplot(iris['sepal_width'])
sns.distplot(iris['sepal_width'], bins=10, color='pink', hist=False,
             kde_kws={'linewidth':4})
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

# sns.regplot(x=iris['petal_length'], y=iris['petal_width'])
# sns.scatterplot(x=iris['petal_length'], y=iris['petal_width'], hue=iris['species']
#                 ,style=iris['species'])

sns.pairplot(iris, diag_kind='kde', palette='bright',hue='species')

plt.show()

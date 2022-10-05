import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

sns.distplot(iris[iris.species=='setosa']['petal_length'], label='setosa')
sns.distplot(iris[iris.species=='versicolor']['petal_length'], label='versicolor')
sns.distplot(iris[iris.species=='virginica']['petal_length'], label='virginica')

plt.legend(title='Species')
plt.show()

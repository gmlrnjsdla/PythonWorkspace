import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

# print(iris.shape)
# print(iris.head())
# print(iris.tail())
# print(iris.describe())

plt.hist(iris[iris.species=='setosa'] ['petal_length'], bins=10, alpha=0.5, label='setosa')
plt.hist(iris[iris.species=='versicolor'] ['petal_length'], bins=10, alpha=0.5, label='versicolor')
plt.hist(iris[iris.species=='virginica'] ['petal_length'], bins=10, alpha=0.5, label='virginica')

plt.legend(title='Species')

plt.show()


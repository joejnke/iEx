import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# print(iris.head())
nunet_stat = pd.read_csv('sample_cpu_mem_usage.csv', names=['mem_usage', 'cpu_usage'])


# iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')
# iris.plot.hist(subplots=True, layout=(4,1), figsize=(10, 10), bins=20)
# iris.drop(['class'], axis=1).plot.line(subplots=True, layout=(4, 1), figsize=(10, 10))
# plt.show()

# sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='class')
# sns.lineplot(data=iris.drop(['class'], axis=1))
# sns.lineplot(data=nunet_stat.drop('mem_usage', axis=1))
nunet_stat.plot.line(subplots=True, layout=(2, 1), figsize=(10, 10))
plt.show()

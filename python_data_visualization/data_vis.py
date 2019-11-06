import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
# print(iris.head())


# iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')
# iris.plot.hist(subplots=True, layout=(4,1), figsize=(10, 10), bins=20)
iris.drop(['class'], axis=1).plot.line(subplots=True, layout=(4,1), figsize=(10, 10))
plt.show()


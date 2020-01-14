import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepal_length = np.array([float(row[0]) for row in iris])
sepal_width = np.array([float(row[1]) for row in iris])
petal_length = np.array([float(row[2]) for row in iris])
petal_width = np.array([float(row[3]) for row in iris])
flower = [{b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}[row[4]] for row in iris]

maxsepwid=sepal_width.argmax()
print('the flower with the widest sepal is flower number',maxsepwid+1,'with sepal width',iris[maxsepwid][1],".It's species is",iris[maxsepwid][4])
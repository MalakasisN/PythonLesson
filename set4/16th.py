import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepal_length = np.array([float(row[0]) for row in iris])
sepal_width = np.array([float(row[1]) for row in iris])
petal_length = np.array([float(row[2]) for row in iris])
petal_width = np.array([float(row[3]) for row in iris])
flower = [{b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}[row[4]] for row in iris]

from collections import Counter
setosanum=Counter(flower)[0]
versicolornum=Counter(flower)[1]
virginicanum=Counter(flower)[2]
setosamean=sum(petal_width[0:setosanum])/setosanum
versicolormean=sum(petal_width[setosanum:setosanum+versicolornum])/versicolornum
virginicamean=sum(petal_width[setosanum+versicolornum:setosanum+versicolornum+virginicanum])/virginicanum
print('The petal width mean is for Iris setosa',setosamean,'for Iris versicolor',versicolormean,'and for Iris virginica',virginicamean)
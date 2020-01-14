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
diff=petal_length-sepal_width
setosadiff=diff[:setosanum]
versicolordiff=diff[setosanum:setosanum+versicolornum]
virginicadiff=diff[setosanum+versicolornum:setosanum+versicolornum+virginicanum]
print(len(setosadiff[setosadiff>0]),'Iris setosa have bigger petal lenght than sepal width.\n',len(versicolordiff[versicolordiff>0]),'Iris versicolor have bigger petal lenght than sepal width.\n',len(virginicadiff[virginicadiff>0]),'Iris virginica have bigger petal lenght than sepal width.\n')
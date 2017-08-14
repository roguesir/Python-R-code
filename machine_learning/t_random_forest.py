from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
print(iris.data)
print(iris.target)
test = np.array([3.2,3.2,1.,0.9]).reshape(1,-1)
model = RandomForestClassifier() 
model = model.fit(iris.data,iris.target)
predicted = model.predict(test)
print(predicted)
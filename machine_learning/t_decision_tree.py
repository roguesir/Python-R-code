# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

from sklearn import tree
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
print(iris.data)
print(iris.target)
test = np.array([3.2,3.2,1.,0.9]).reshape(1,-1)
model = tree.DecisionTreeClassifier(criterion='gini') 
model = model.fit(iris.data,iris.target)
predicted = model.predict(test)
print(predicted)
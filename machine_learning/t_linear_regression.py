'''
Author:roguesir
Github:https://github.com/roguesir/Python-practice/tree/master/machine_learning
'''
import numpy as np
from sklearn import linear_model



x_train = np.array([2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
y_train = np.array([202,244,305,382,484,591,712,853,894,1013])

x_test = np.array([2011])

linear = linear_model.LinearRegression()
linear.fit(x_train,y_train)
linear.score(x_train,y_train)

print('Coefficient: ',linear.coef_)
print('Intercept: ',linear.intercept_)

predicted = linear.predict(x_test)
print(predicted)

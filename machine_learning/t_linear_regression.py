# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""
import numpy as np  
from sklearn import linear_model  
import matplotlib.pyplot as plt  
  
x_train = [[2001],[2002],[2003],[2004],[2005],[2006],[2007],[2008],[2009],[2010]]  
y_train = [[202],[244],[305],[382],[484],[591],[712],[853],[894],[1013]]  
  
x_test = [[2011]]  
  
linear = linear_model.LinearRegression()  
linear.fit(x_train,y_train)  
linear.score(x_train,y_train)  
  
print('Coefficient: ',linear.coef_)  
print('Intercept: ',linear.intercept_)  
  
predicted = linear.predict(x_test)  
print(predicted)  
  
plt.figure()  
plt.scatter(x_train,y_train)  
plt.plot(x_train,linear.coef_*x_train+linear.intercept_,'r')  
plt.show()

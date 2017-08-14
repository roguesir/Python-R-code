'''
Author:roguesir
Github:https://github.com/roguesir/Python-practice/tree/master/machine_learning
'''

from sklearn import linear_model

x_train = input_variables_value
y_train = 
x_test = 

linear = linear_model.LinearRegression()
linear.fit(x_train,y_train)
linear.score(x_train,y_train)

print('Coefficient: ',linear.coef_)
print('Intercept: ',linear.intercept_)

predicted = linear.predict(x_test)
print(predicted)
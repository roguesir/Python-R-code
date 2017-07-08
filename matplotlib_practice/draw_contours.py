import numpy as np
import matplotlib as plt

# draw contours
def f(x,y):
	# the hight function
	return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y =np.meshgrid(x,y)

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
plt.contour(X,Y,f(X,Y),10,alpha = 0.75,cmap = plt.cm.hot)

# use plt.contour to add contourline
C = plt.contour(X,Y,f(X,Y),10,colors = 'black',linewidth = .5)
# adding label
plt.clabel(C,inline = True,fontsize = 10)

plt.xticks(())
plt.yticks(())
plt.show()
import numpy as np 
import matplotlib as plt

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4,4,.25)
Y = np.arange(-4,4,.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstide = 1,cstride = )
plt.show()
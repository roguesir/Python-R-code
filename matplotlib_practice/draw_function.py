# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

import numpy as np
import matplotlib.pyplot as plt

h0 = [0.4,.6,.8]
lambda0 = [0.03,0.05,0.07]
plt.figure(figsize=(6,4))
x = np.linspace(0, 50, 50)

for i in lambda0:
	for h in h0:
		plt.plot(x, 11+(20*np.exp(-i*x)-h*x)/2,label='lambda='+str(i)+' h='+str(h))

plt.legend()
plt.show()
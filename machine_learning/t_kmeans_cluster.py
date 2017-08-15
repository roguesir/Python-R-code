import numpy as np 
 
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 9])  
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 3])  
x = np.array(list(zip(x1, x2))).reshape(len(x1), 2)  
print(x)

from sklearn.cluster import KMeans  
kmeans=KMeans(n_clusters=3)
kmeans.fit(x)  
print(kmeans.labels_)

import matplotlib.pyplot as plt  
plt.figure(figsize=(8,10))  
colors = ['b', 'g', 'r']  
markers = ['o', 's', 'D']  
for i,l in enumerate(kmeans.labels_):  
     plt.plot(x1[i],x2[i],color=colors[l],marker=markers[l],ls='None')  
plt.show()  
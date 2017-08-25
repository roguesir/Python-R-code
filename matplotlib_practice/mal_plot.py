import numpy as np
import matplotlib.pyplot as plt

x1=[20,33,51,79,101,121,132,145,162,182,203,219,232,243,256,270,287,310,325]
y1=[49,48,48,48,48,87,106,123,155,191,233,261,278,284,297,307,341,319,341]
x2=[31,52,73,92,101,112,126,140,153,175,186,196,215,230,240,270,288,300]
y2=[48,48,48,48,49,89,162,237,302,378,443,472,522,597,628,661,690,702]
x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
y3=[48,48,48,48,66,173,351,472,586,712,804,899,994,1094,1198,1360,1458,1578,1734,1797,1892]


plt.figure(figsize=(6, 4))

plt.subplot(121)
# figure splits into 2 rows, 3 col, plot to the 6th sub-fig

#p1=np.poly1d(np.polyfit(x1[5:],y1[5:],1))
#p2=np.poly1d(np.polyfit(x2[5:],y2[5:],1))
#p3=np.poly1d(np.polyfit(x3[5:],y3[5:],1))
x=np.arange(20,350)
#l1=plt.plot(x,p1(x),'r--',label='type1')
#l2=plt.plot(x,p2(x),'g--',label='type2')
#l3=plt.plot(x,p3(x),'b--',label='type3')
l1=plt.plot(x1,y1,'r--',label='type1')
l2=plt.plot(x2,y2,'g--',label='type2')
l3=plt.plot(x3,y3,'b--',label='type3')
plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
plt.title('block1')
plt.xlabel('row')
plt.ylabel('column')
plt.legend()

# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(1, 2, 2)
# figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.plot([0, 1], [0, 1])
plt.title('block2')
plt.yticks([0, 0.25, 0.5, 0.75, 1],
           [' ', ' ', ' ', ' ', ' '])






#plt.tight_layout()
plt.show()
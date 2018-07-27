# encoding:utf-8
import os
import sys
import pandas as pd

# read csv file
header = ["Name", "Area", "Population", "Administrative_level", "Have 985"]
index = ['a', 'b', 'c', 'd', 'e']
data = pd.read_csv(path+filename, sep='\t', header=header, index=index)
'''
      Name   Area  Population Administrative_level Have 985
a  Beijing   1.68        2300                 city      Yes
b  Tianjin   1.13        1293                 city      Yes
c  Shaanxi  20.56        3732             Province      Yes
d    Hebei  18.77        7185             Province       No
e  Qinghai  72.00         560             Province       No
'''

# read dict
my_dict = {'a':[1,2,3], 'b':[2,3,4], 'c':[3,4,5]}
pd.Series(my_dict) # 字典的值变成一列
'''
a       [1, 2, 3]
b       [2, 3, 4]
c       [3, 4, 5]
dtype: object
'''
pd.DataFrame(my_dict.values(), index= my_dict.keys())
'''
      0  1  2
a     1  2  3
b     2  3  4
c     3  4  5
'''

# read list
a = [[1,2,3],[4,5,6],[7,8,9]]
pd.DataFrame(a)
'''
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9
'''

# save file 
a.to_csv(path + filename, sep='\t', header=False, index=False)




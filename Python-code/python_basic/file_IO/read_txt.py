# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://m.blog.csdn.net/roguesir
"""

import numpy as np


# Method 1
file1 = open("TXT.txt")
while True:
	line = file1.readline()
	print(line)
	if not line:
		break
file1.close()

# Method 2
for line in open("TXT.txt"):
	print(line)

# Method 3
with open("TXT.txt",'r') as f:
	data = f.read()
	print(data)

'''
读取文件的3种方法：
	read()将文本中所有行读到一个字符串中去
	readline()一行一行读，在读行过程中可以跳过特定行
	readlines()将文本中所有行读到一个list中，文本文件每一行是list的一个元素
'''
# Read 
a = np.loadtxt('TXT.txt')
b = a.reshape(3,3)
c = a.reshape(-1,1,3)
print(b,c)

with open('TXT.txt','r') as f:
	data = f.readlines()
	for line in data:
		item = line.split()
		#item = map(float, item)
		print(float(item[1])+1)




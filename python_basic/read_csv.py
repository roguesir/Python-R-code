# -*- coding: utf-8 -*-

"""
Author: roguesir
Date: 2017/08/30
Github: https://roguesir.github.com
Blog: http://m.blog.csdn.net/roguesir
"""

import csv

csvFile = open("CSV.csv", "r")
reader = csv.reader(csvFile)
data = []
for item in reader:
	if reader.line_num == 1:
		continue
	data.extend(item)
csvFile.close()
print(data)



csvFile = open("CSV.csv", "r")
reader = csv.reader(csvFile)
# 建立空字典
result = {}
for item in reader:
    if reader.line_num == 1:
        continue
    result[item[1]] = item[2]

csvFile.close()
print(result)
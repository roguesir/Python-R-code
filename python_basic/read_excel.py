# -*- coding:utf-8 -*-

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://m.blog.csdn.net/roguesir
"""

import os       
import xlrd

data = xlrd.open_workbook('EXCEL.xlsx')
data = data.sheet_by_index(0)
nrows=data.nrows
ncols=data.ncols
print(nrows,ncols) 
col_score = data.col_values(1)
row_values = data.row_values(0)
print(col_score,row_values)


data=xlrd.open_workbook('EXCEL.xlsx')     
table=data.sheets()[0] 
data_list=[]    
for i in range(4):
	data_list.extend(table.row_values(i))
print(data_list)

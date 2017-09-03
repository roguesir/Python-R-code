# coding:utf-8

"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""

import json
JSON = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

#dumps到字符串
json_str = json.dumps(JSON)
#loads回来
data2 = json.loads(json_str)

## 针对文件
# Writing JSON data
with open('JSON.json', 'w') as f:
    a = json.dump(JSON, f)

# Reading data back
with open('JSON.json', 'r') as f:
    data = json.load(f)
print(data)
# coding:utf-8

'''
    Description: 计算文件内不同feature的推荐列表的重复度
    Usage: python2.7 compute_repeat.py path1 feature1 path2 feature2 times
    Params:
        path1: 输入文件，格式：key \t 推荐列表（","分隔）
        path2: 输入文件，格式：key \t 推荐列表（","分隔）
        feature1: 特征名
        feature2: 特征名
        times: 取前times个结果计算重复数量
    Note: 如果path1和path2相同，则计算同一文件内两个不同feature的列表相似度，
          如果feature1个feature2相同，则计算不同文件内相同feature的相似度
'''

import sys

path1 = sys.argv[1]
path2 = sys.argv[2]
feature1 = sys.argv[3]
feature2 = sys.argv[4]
times = int(sys.argv[5])

feature1_set, feature2_set = set(), set()
for line in open(path1):
    line = line.strip().split("\t")
    feature, feed = line[0], line[1].split(",")
    if feature == feature1:
        for item in feed[:times]:
            feature1_set.add(item)

for line in open(path2):
    line = line.strip().split("\t")
    feature, feed = line[0], line[1].split(",")
    if feature == feature2:
        for item in feed[:times]:
            feature2_set.add(item)
print "times: " + str(times)
print "the same item: " + str(len(feature1_set & feature2_set))


# -*- coding:utf-8 -*-
"""
在这里我们写一些辅助方法
首先写一个，一次读取一个txt文件
然后再写一个读取多个txt文件
作者：
日期：2022年01月02日
"""
import os

def readAFile(route):
    with open(route, 'r',encoding='utf-8') as file:
        data = file.read()
        return data


def readFiles(dir):
    files = os.listdir(dir)
    data = []
    for file in files:
        data.append(readAFile(dir + '/' + file))
    return data

if __name__=="__main__":
    print(readFiles('alldocuments'))


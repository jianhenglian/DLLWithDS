# -*- coding:utf-8 -*-
"""
在这里我们写一些辅助方法
首先写一个，一次读取一个txt文件
然后再写一个读取多个txt文件
作者：
日期：2022年01月02日
"""
import os, json, re
import jieba
import jieba.analyse


def readAFile(route):
    try:
        with open(route, 'r', encoding='utf-8') as file:
            data = file.read()
    except UnicodeDecodeError:
        with open(route, 'r', encoding='gbk') as file:
            data = file.read()
    return data

def readFiles(dir):
    files = os.listdir(dir)
    data = []
    for file in files:
        data.append(readAFile(dir + '\\' + file))
    return data

def readJsons(dir):
    files = os.listdir(dir)
    data = []
    for file in files:
        data.append(readJsonFile(dir + '\\' + file))
    return data

def readJsonFile(route):
    try:
        with open(route, encoding='utf-8') as f:
            return json.load(f)
    except UnicodeError:
        with open(route, encoding="gbk") as f:
            return json.load(f)


def pickUpDate(text):
    dateRE = re.compile("(?<=于)\d{4}年\d{1,2}月\d{1,2}日(?=受理)|(?<=于)\d{4}年\d{1,2}月\d{1,2}日(?=立案)")
    date1=dateRE.findall(text)
    date=[]
    for item in date1:
        temp=re.findall(r'\d+',item)
        single=temp[0]+"."+temp[1]+"."+temp[2]
        date.append(single)
    if len(date) == 0:
        pat = re.compile('\\d+[年]\\d+[月]\\d+[日]')
        return list(set(pat.findall(text)))
    return date

def pickUpCause(text, name):
    causeRE = re.compile("(?<=因).{1,20}(?=一案)|(?<="+ name+ "犯).{1,20}(?=罪)|(?<="+ name+ ").{1,20}(?=一案)|(?<=）).{1,20}(?=一案)")
    cause=causeRE.findall(text)
    return cause

def pickUpNation(text):
    nationRE = re.compile("(?<=，).{1,2}族")
    nation1=nationRE.findall(text)
    nation2=jieba.analyse.extract_tags(text,allowPOS=('nz',))
    nation=[]
    for item in nation2:
        if item in nation1:
            nation.append(item)
    nation.append('无')
    return nation

def pickUpAdd(text):
    addRe = re.compile('\\w{2}[省市]\\w+[，。]')
    addAll = addRe.findall(text)
    add = []
    for item in addAll:
        add.append(item)
    return list(set(add))

def divideText(text):
    data = {"姓名":[],"性别":[],"民族": [],"出生地":[],"案由": [], "案件日期": []}
    data["姓名"] = jieba.analyse.extract_tags(text,allowPOS=('nr',),topK=5)
    data["民族"] = pickUpNation(text)
    if len(data["民族"]) == 1:
        data["性别"] = ['无', '男', '女']
    else:
        data["性别"] = ['男', '女', '无']
    data["出生地"] = pickUpAdd(text)
    data["案由"] = []
    for name in data["姓名"]:
        for inter in pickUpCause(text, name):
            data["案由"].append(inter)
    data["案由"] = list(set(data["案由"]))
    data["案件日期"] = pickUpDate(text)
    data["相关法院"] = jieba.analyse.extract_tags(text, allowPOS=('nt',))
    return data


"""Here we need to replace Chinese with '.', in order to adjust to json
We decide to use regular to take place of Chinese"""
def findDate(str):
    pat = re.compile('\\d+[年]\\d+[月]\\d+[日]')
    return list(set(pat.findall(str)))



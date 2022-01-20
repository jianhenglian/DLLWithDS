# -*- coding:utf-8 -*-
"""
作者：
日期：2022年01月02日
"""
from text2vec import SBert, semantic_search
from .Util import readFiles, readJsons, divideText, findDate
embedder = SBert()

"""改一下这个方法就行了，让他返回两个东西，一个json对象，一个字符串"""
"""如果我们想要改成用json匹配的话，我们只需更改allDocuments即可"""
def findMostSimilarText(targetText):
    allDocuments = readFiles('D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments')
    allFolders = readJsons('D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\docuWithJson')
    corpus_embeddings = embedder.encode(allDocuments)

    query_embedding = embedder.encode(targetText)
    hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
    hits = hits[0]
    jsonFile = allFolders[hits[0]['corpus_id']]
    result = {}
    result["文本"] = allDocuments[hits[0]['corpus_id']]
    result["json"] = jsonFile
    return result

"""
首先，我们读取所有的json对象，放到列表里
然后，我们根据传入的参数“asda”类似的，决定采用哪几个json元素
然后，我们从json对象中提取出想要的东西，组成字符串，放列表里，存成allDocuments
然后，我们提取目标对象的对应属性，作为targetText
也就是说，我们需要的参数是文本，和一个决定用那几个json元素的字符串
r：相关法院
c: 当事人
s: 性别
t: 案件日期/日期
e: 案由
b: 出生地
n: 民族

"""
def useJsonFind(targetText, pattern):
    mainAll = readFiles('D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments')
    allFolders = readJsons(
        'D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\docuWithJson')
    allDocuments = []
    for eachJson in allFolders:
        thisDocu = ""
        for arg in pattern:
            if arg == 'r':
                thisDocu += eachJson["相关法院"]
            if arg == 'c':
                thisDocu += eachJson["当事人"]
            if arg == 's':
                thisDocu += eachJson["性别"]
            if arg == 't':
                try:
                    thisDocu += eachJson["案件日期"]
                except KeyError:
                    thisDocu += eachJson["日期"]
            if arg == 'e':
                thisDocu += eachJson["案由"]
            if arg == 'b':
                thisDocu += eachJson["出生地"]
            if arg == 'n':
                thisDocu += eachJson["民族"]
        allDocuments.append(thisDocu)
    divideTextNow = divideText(targetText)
    display = ""
    realTarText = ""
    for arg in pattern:
        if arg == 'r':
            display += "\n相关法院："
            for a in divideTextNow["相关法院"]:
                display += a + ","
                realTarText += a
        if arg == 'c':
            display += "\n姓名："
            for a in divideTextNow["姓名"]:
                realTarText += a
                display += a + ","
        if arg == 's':
            display += "\n性别："
            for a in divideTextNow["性别"]:
                display += a + ","
                realTarText += a
        if arg == 'n':
            display += "\n民族："
            for a in divideTextNow["民族"]:
                display += a + ","
                realTarText += a
        if arg == 'b':
            display += "\n出生地："
            for a in divideTextNow["出生地"]:
                display += a + ","
                realTarText += a
        if arg == 'e':
            display += "\n案由："
            for a in divideTextNow["案由"]:
                display += a + ","
                realTarText += a
        if arg == 't':
            display += "\n案件日期："
            for a in divideTextNow["案件日期"]:
                display += a + ","
                realTarText += a
    corpus_embeddings = embedder.encode(allDocuments)

    query_embedding = embedder.encode(realTarText)
    hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
    hits = hits[0]
    jsonFile = allFolders[hits[0]['corpus_id']]
    result = {}
    result["文本"] = mainAll[hits[0]['corpus_id']]
    result["json"] = jsonFile
    result["guess"] = display
    return result
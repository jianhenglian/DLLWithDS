from re import I
import jieba
import jieba.posseg as pseg
import jieba.analyse

#自定义词典，以便包含jieba库里没有的新词
jieba.load_userdict("user.txt")

with open("case3.txt",'r',encoding='utf-8') as f:
    text=f.read()

#默认精确模式
#print(jieba.lcut(text))

#失去识别新词能力
#print(jieba.lcut(text,HMM=False))

#分词时有的词语因为新词识别能力被错误地合在了一起 可以将其强制分开 元组形式
#jieba.suggest_freq(('特此','通知'),True)
#print(jieba.lcut(text))

#分词时有的词语被错误地分开
#法一
#jieba.add_word('重新审判条件')
#法二
#jieba.suggest_freq('重新审判条件',True)
#print(jieba.lcut(text))

#搜索引擎模式 对精确模式的长词进行再切分
#print(jieba.lcut_for_search(text)))

#词性标注，返回pair
words=pseg.lcut(text)
for word,flag in words:
    print(word,flag)

#关键词提取
#基于TF-IDF算法
#print(jieba.analyse.extract_tags(text,topK=30))

#同时显示权重
#keywords=jieba.analyse.extract_tags(text,topK=10,withWeight=True)
#for item in keywords:
#   print(item[0],item[1])

#仅包括指定词性的词 元组形式 如果仅一个词性的话要加个逗号！
#当事人(人名)
#print("当事人姓名筛选项：")
#print(jieba.analyse.extract_tags(text,allowPOS=('nr',)))
#print('\n')
#民族(其他专名)
#print('民族筛选项：')
#print(jieba.analyse.extract_tags(text,allowPOS=('nz',)))
#print('\n')
#出生地(地名)
#print('出生地筛选项：')
#print(jieba.analyse.extract_tags(text,allowPOS=('ns',)))
#print('\n')
#案由(刑事案件)?
#print('案由筛选项：')
#print(jieba.analyse.extract_tags(text,allowPOS=('i',)))
#print('\n')
#相关法院(机构名) 有时可以将整个法院名称识别出来，若不行再用ns过滤
#print('相关法院筛选项：')
#print(jieba.analyse.extract_tags(text,allowPOS=('nt',)))
#print('\n')

#基于TextRank算法
#print(jieba.analyse.textrank(text,topK=10))
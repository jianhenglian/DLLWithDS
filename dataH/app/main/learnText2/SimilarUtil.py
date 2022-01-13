# -*- coding:utf-8 -*-
"""
作者：
日期：2022年01月02日
"""
from text2vec import SBert, semantic_search
from .Util import readFiles

embedder = SBert()


def findMostSimilarText(targetText):
    allDocuments = readFiles('D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments')
    corpus_embeddings = embedder.encode(allDocuments)

    query_embedding = embedder.encode(targetText)
    hits = semantic_search(query_embedding, corpus_embeddings, top_k=1)
    hits = hits[0]
    return allDocuments[hits[0]['corpus_id']]
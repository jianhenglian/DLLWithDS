# -*- coding:utf-8 -*-
"""
作者：
日期：2022年01月07日
"""
import unittest
from app.main.learnText2.SimilarUtil import findMostSimilarText

class SimilarTest(unittest.TestCase):
    def test_similar(self):
        self.assertIsNotNone(findMostSimilarText("ljh lyt djf"))

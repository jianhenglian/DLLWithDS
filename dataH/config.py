# -*- coding:utf-8 -*-
"""
作者：
日期：2022年01月07日
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'lyt ljh djf'
    # WTF_CSRF_ENABLED = False

    @staticmethod
    def init__app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'default': DevelopmentConfig
}
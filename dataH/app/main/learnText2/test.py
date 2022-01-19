# -*- coding:utf-8 -*-
"""
作者：
日期：2022年01月11日
"""
from werkzeug.utils import send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:\\self_learning\\flask\\dataH\\app\\main\\learnText2\\alldocuments'
def mkFileUseString():
    name = 'example.txt'
    str = send_from_directory(UPLOAD_FOLDER, name, "WSGIEnvironment")
    with open("test.txt", 'w') as f:
        f.write(str)

def go():
    print(secure_filename("案例文本12.txt"))

if __name__ =="__main__":
    go()
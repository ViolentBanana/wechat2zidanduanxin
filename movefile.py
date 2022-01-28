# coding= utf-8

import shutil
import os



#企微裂变
def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print path + ' 目录已存在'
        return False

def move(dirname, oldfile,newfilename):

    dirname = "userEmoji/"+dirname

    print dirname
    print oldfile
    print newfilename


    mkdir(dirname)
    try:

        os.rename(oldfile,newfilename)

        print dirname + "/" + newfilename

        shutil.move(newfilename, dirname + "/" + newfilename)
        print '移动' + oldfile + "成功"
    except IOError:
        print "目录不存在"

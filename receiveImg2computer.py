# coding=utf8
import itchat, time
from itchat.content import *
import movefile

import re
import os

# 自己的另一个微信，负责接收消息
userkey = "@acd233d325ba803dc97911705948d79fbb18d4a877d87db7d16b00878ed293c0"


# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        global userkey

        print (msg)
        # name = itchat.search_friends(name=u'CHEN')
        # chen = name[0]["UserName"]
        print (msg['FromUserName'])
        print (userkey)
        if msg['FromUserName'] == userkey:
            print ("")

            # 转发给好友
            strcontent = msg['Text']

            try:
                username = re.search("@(.*?)@", strcontent, re.S).group(1)

                print "username:" + username

                contentkey = "@" + username + "@"

                print contentkey

                content = strcontent.replace(contentkey, "")

                print content

                author = itchat.search_friends(name=username)[0]
                author.send(content)
            except:
                print "转发失败"

        else:

            author = itchat.search_friends(name='CHEN')[0]
            author.send(u"[%s]收到好友@%s 的信息：%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']))

            # itchat.send_msg(u"[%s]2收到好友@%s 的信息：%s\n" %
            #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
            #                  msg['User']['NickName'],
            #                  msg['Text']), author)
            # 回复给好友
            return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])


# @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
# def atta_reply(msg):
#     msg['Text'](msg['FileName'])
#     return ({ 'Picture': u'图片', 'Recording': u'录音',
#         'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
#         u'已下载到本地') # download function is: msg['Text'](msg['FileName'])




@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    if not msg['FromUserName'] == myUserName:

        print str(msg)

        username = re.search("u'PYInitial': u'(.*?)',", str(msg), re.S).group(1)
        print "dirname:" + username

        filename = re.search('cdnurl = "(.*?)" designerid', str(msg), re.S).group(1)
        filename = filename.replace("/", "").replace(':', "").replace(".", "") + ".gif"
        print "filename:" + filename

        isExists = os.path.exists(username + "/" + filename)

        if (isExists):
            print "已存在不保存文件"
        else:
            msg.download(msg.fileName)
            movefile.move(username, msg.fileName, filename)

    # typeSymbol = {
    #     PICTURE: 'img',
    #     VIDEO: 'vid', }.get(msg.type, 'fil')
    # return '@%s@%s' % (typeSymbol, msg.fileName)

    return ({'Picture': u'图片', 'Recording': u'录音',
             'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
            u'已下载到本地')


if __name__ == '__main__':
    # itchat.auto_login()
    # 命令行显示二维码
    # itchat.auto_login(enableCmdQR=True)
    # 如部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2
    # itchat.auto_login(enableCmdQR=2)
    itchat.auto_login(hotReload=True)
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]

    # itchat.logout()
    itchat.run()

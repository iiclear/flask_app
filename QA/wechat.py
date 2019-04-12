#coding:utf8
import itchat
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from service import api
@itchat.msg_register(itchat.content.TEXT)
def question(msg):
    que =str(msg['Text']).decode(encoding='UTF-8')
    print que
    ans = api(msg['Text'])
    print ans
    # return ans


if __name__ == '__main__':

    itchat.auto_login()
    time.sleep(2)
    itchat.run()

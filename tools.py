#coding:utf8
import requests
from bs4 import BeautifulSoup
import itchat


def getreplay(question):
    url = 'http://47.101.221.48:5000/api/'+question
    response = requests.get(url)
    web_data = BeautifulSoup(response.text,"lxml")
    ans = web_data.select('body')
    return str(ans[0].get_text()).replace('回答：','').replace('\n','').strip()

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    if msg['Content'] == u'你好':
        itchat.send_msg(msg['User']['NickName'] + "你好啊！我是百科机器人", msg['FromUserName'])

    answer = getreplay(msg['Content'])
    itchat.send_msg('@'+msg['User']['NickName'] +' '+ str(answer), msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()
#coding:utf-8
from flask import Flask,render_template,request
from QA.MainProgram import run
import time
import socket
from QA.Tools.tuling import geta
from flask_bootstrap import Bootstrap
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from tools import getreplay,web_bot
import json


app = Flask(__name__)
#bootstrap = Bootstrap(app)


@app.route('/api/<question>')
def hello_world(question):
    answers=" "
    s = '展开全部'
    answer = run(str(question).encode('utf-8'))
    if(type(answer).__name__=='list')or'唔... 怎么回答...' in answer or '天气' in question:
        answers = geta(question)
        return render_template('index.html',answers=answers)
    else:
        print answer
        if s in str(answer):
            print answer
            answer = str(answer).replace('\n', '').replace('展开全部',"").split('已赞过')[0]
            print answer+'666'
        return render_template('index.html',answer=answer)


@app.route("/test")
def ws():

    user_socket = request.environ.get('wsgi.websocket')#type:WebSocket
    #print(len(user_socket))
    #user_socket_list.append(user_socket)
   # print(len(user_socket_list),user_socket_list)
    while 1:
        msg = user_socket.receive()
        print(msg)
        print(type(msg),msg)
        #user_socket.send(json.loads({"id": "1"}))
        question = json.loads(msg)
        print(type(question))
        q = question['data']['mine']['content']
        print(q)
        res = web_bot(q)
        print(res,"test")
        a = {
  "username": "客服姐姐",
  "avatar": "https://robot.rszhang.top/images/icon/nv/0.jpg" ,
  "id": "-2", #//消息的来源ID（如果是私聊，则是用户id，如果是群聊，则是群组id）
  "type": "friend" ,#//聊天窗口来源类型，从发送消息传递的to里面获取
  "content": res,# //消息内容
  "cid": 0 ,#//消息id，可不传。除非你要对消息进行一些操作（如撤回）
  "mine": True,#//是否我发送的消息，如果为true，则会显示在右方
  "fromid": "100000" ,#/消息的发送者id（比如群组中的某个消息发送者），可用于自动解决浏览器多窗口时的一些问题
  "timestamp": 1467475443306 ,#//服务端时间戳毫秒数。注意：如果你返回的是标准的 unix 时间戳，记得要 *1000
}


        user_socket.send(json.dumps(a))
        print(type(a))



@app.route('/chat/')
def chat():
    return render_template('test.html')


if __name__ == '__main__':

    http_serv = WSGIServer(("0.0.0.0",5000),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()
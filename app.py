#coding:utf-8
from flask import Flask,render_template
from QA.MainProgram import run
import time
from QA.Tools.tuling import geta
app = Flask(__name__)


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



if __name__ == '__main__':
    app.run(host='0.0.0.0',port =5000)

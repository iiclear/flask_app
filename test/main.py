#coding:utf-8
import aiml
import os, sys
import jieba
def wordSegment(text):
    text = text.strip()
    seg_list = jieba.cut(text)
    result = " ".join(seg_list)
    return result

mybot_path = './'
os.chdir(mybot_path)

mybot = aiml.Kernel()
mybot.learn('study.aiml')
while True:
    input_message = raw_input(">>: ")
    message = wordSegment(input_message)
    print message
    res = mybot.respond(message)
    print res


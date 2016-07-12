# -*- encoding: utf-8 -*-

# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，用*号替换
__author__ = 'Administrator'

import re;
import os;

def initWords():
    words= list()
    with open("filtered_words.txt","r") as f:
        for line in f:
            aline=re.findall(r'\w+',line)
            for senceWords in aline:
                wList=senceWords.strip().split()
                for _w in wList:
                        words.insert(len(words),_w)
    return words

if __name__=="__main__":
    text=input("请输入语句:")
    words=initWords()
    flag=1
    for word in words:
        if(word in text):
            print("有敏感哦！")
            text=text.replace(word,(len(word)*"*"))
            flag=0
    if(flag):
        print("没有敏感词！")
    else:
        print("处理后的语句："+text)


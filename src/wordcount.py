# 任一个英文的纯文本文件，统计其中的单词出现的个数
__author__ = 'Administrator'

import os
import re

if __name__ == "__main__":
    dict={}
    with open("G:/a.txt","r") as f:
        for line in f:
            aline=re.findall(r'\w+',line.lower())
            for words in aline:
                wList=words.strip().split()
                for _w in wList:
                    if _w in dict:
                        wordcount=dict[_w]
                        wordcount+=1;
                        dict[_w]=wordcount
                    else:
                        dict[_w]=1


    for k,v in dict.items():
        print(k+"---"+str(v))
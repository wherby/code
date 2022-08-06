import json
import os
from collections import defaultdict,deque

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
def readFile():
    file = "data.json"
    f = open(file)
    lss = json.load(f)
    #print(lss)
    dic = defaultdict(list)
    for ls in lss:
        for items in ls.values():
            for item in items:
                #print(item)
                name = item['name']
                start = item['start']
                end= item['end']
                dic[name].append((start,end))
    #print(dic)
    return dic

def timeToSecond(str1):
    ls = str1.split("T")
    ls = ls[1].split(".")
    ls = ls[0].split(":")
    ls = map(lambda x: int(x),ls)
    acc =0
    for a in ls:
        acc =acc*60 + a 
    return acc
#re = timeToSecond('2022-07-28T07:32:07.817Z')
#print(re)

def caculateDict(dic):
    dic2 = defaultdict(int)
    for k,values in dic.items():
        for start,end in values:
            dur = timeToSecond(end) - timeToSecond(start)
            dic2[k] += dur
    print(dic2)
dic = readFile()
caculateDict(dic)

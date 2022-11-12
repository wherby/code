import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#filename ="t1.txt.cfg"
filename = "t2.txt.cfg"
#filename = "t3.txt.cfg"
#filename = "t6.txt.cfg"
f=open(filename,'r')

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


def getContent(ins):
    pages = []
    tmp =[]
    for line in ins:
        if line.find("PAGE: ") >=0 :
            if len(tmp) >0:
                pages.append(list(tmp))
            tmp=[]
            tmp.append(line)
        else:
            tmp.append(line)
    if len(tmp) >0:
        pages.append(tmp)
    return pages

def removeEmptyLine(ins):
    tmp = []
    for a in ins:
        if  len(a.strip()) != 0:
            tmp.append(a)
    return tmp

def removeHeader(pages):
    ret = []
    for page in pages:
        startLine = 0
        for i,line in  enumerate(page):
            if line.find("***") >=0:
                startLine = i
        ret.append(page[startLine+1:])
    return ret

def fsmForPages(pageLine):
    state = 0
    tmp = []
    ret = []
    #print(pageLine[-10:])
    for a in pageLine:
        #print(len(a.strip()))
        tmp.append(a)
        if len(a.strip()) > 130:
            if state == 0:
                state = 1
            elif state ==1 or state ==2:
                state =2 
                ret.extend(list(tmp))
                tmp = [] 
        else:
            if state ==1:
                tmp =[]
                tmp.append(a)
            state = 0 
    return ret

def toRecord(lines):
    ret = []
    state = 0
    lastHeader = ""
    tmp = []
    header =""
    for a in lines:
        
        if len(a.strip()) > 130:
            tmp.append(a)
            if state ==0:
                state =1
            elif state ==1:
                ret.append([header,tmp[0],tmp[1]])
                tmp = []
                state =0
        else:
            b = a[:60]
            if len(b.strip())>3:
                header = a
                lastHeader = a
            else:
                #print(lastHeader,a)
                #header =a
                header =str(lastHeader[:62] +a[62:])
    return ret
            

def readFileAndExtract(ins):
    ins = removeEmptyLine(ins)
    pages =  getContent(ins)
    #print(pages[-1])
    pages = removeHeader(pages)
    #print(pages[0])
    
    page = [line for page in pages for line in page ]
    print(len(page))
    page = fsmForPages(page)
    print(page[-3:])
    print(len(page))
    record= toRecord(page)
    #print(record[-4:])
    print(len(record))
    print(record[-1])
    print("("*100)
    print(record[:10])
    # for i,re in enumerate(record):
    #     for li in re:
    #         print(i)
    #         print(li)
    pass


readFileAndExtract(ins)
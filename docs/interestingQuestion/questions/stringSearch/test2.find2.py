from typing import List, Tuple, Optional
from random import randint
from collections import defaultdict,deque


def findpat(text,pattern):
    ps = pattern.split("*")
    n =len(text)
    m = len(pattern)
    ps = list(filter(lambda x: len(x)>0, ps))
    if len(ps) ==0:
        return -1 if len(text) ==0 else 0 
    if len(ps) ==1:
        if text.find(ps[0]) ==-1:
            return -1
        if pattern[0] =="*":
            isFind = text.find(ps[0],1)
            if isFind ==-1:
                return -1 
            else:
                return isFind-1 
        elif pattern[-1] =="*":
            isFind = text.find(ps[0])
            if isFind + m == n :
                return -1
            return isFind
        return text.find(ps[0])
    else:
        onels = []
        start = 0
        while text.find(ps[0],start) != -1:
            onels.append(text.find(ps[0],start))
            start +=1
        #print(onels)
        for s1 in onels:
            #b = text.find(ps[1],s1+len(ps[0]) +1)
            if text[s1+1:s1+1+len(ps[1])] == ps[1]:
                return s1 
        return -1

# text ="abcduuiabce"
# pat = ["*abc","a*d","abc","abced"]

# for p in pat:
#     print(findpat(text,p),p)

text = "a"*100000+"b"
pat = "a"*500 + "*" +"a"*500+"b"
import time

start = time.time()
print(findpat(text,pat))
end = time.time()
print(end - start)

from typing import List, Tuple, Optional


def findpat(text,pattern):
    ret  = 10**10
    aToZ = 'abcdefghijklmnopqrstuvwxyz'
    for a in aToZ:
        np = pattern.replace("*",a)
        #print(pattern,np)
        b = text.find(np)
        if b !=-1:
            ret = min(ret,b)
    return ret if ret != 10**10 else -1 

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
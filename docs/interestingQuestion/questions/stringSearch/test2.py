from typing import List, Tuple, Optional
from random import randint
from collections import defaultdict,deque
MOD = randint(8 * 10 ** 8, 9 * 10 ** 8)
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%MOD
            self.pls[i+1] = (self.pls[i]*131)%MOD
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % MOD) % MOD

def findpat(text,pattern):
    ret  = 10**10
    hs = StringHash(text)
    m = len(pattern)
    n = len(text)
    dic = {}
    for i in range(m,n+1):
        t = hs.query(i-m,i)
        if t not in dic:
            dic[t]= i 
    aToZ = 'abcdefghijklmnopqrstuvwxyz'
    for a in aToZ:
        np = pattern.replace("*",a)
        #print(pattern,np)
        hs2 = StringHash(np)
        if hs2.query(0,m) in dic:
            ret = min(ret, dic[hs2.query(0,m)])
    return ret-m if ret != 10**10 else -1 

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
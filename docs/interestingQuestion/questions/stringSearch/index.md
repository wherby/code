# String search

## Question

Search a pattern contains a "*" which could be any charactor, which is different from https://leetcode.cn/problems/substring-matching-pattern/description/

```python
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
            b = text.find(ps[1],s1+len(ps[0]) +1)
            if b == s1 +len(ps[0]) +1:
                return s1 
        return -1
```

which will cost 17 s 

```python
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
```
which cost 0.6972048282623291
``` python
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
```
which will take 0.03990292549133301 


``` python 
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
```
which will take 0.009321212768554688 s 
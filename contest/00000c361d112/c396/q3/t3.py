from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

from collections import Counter
def getAllDiv(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    def getAllComb(pls,n):
        ret =[]
        for p in pls:
            while n%p ==0:
                ret.append(p)
                n = n//p 
        return ret
    allC = getAllComb(res,n)
    ret =set([])
    for i in range(2<<len(allC)):
        acc =1
        for j in range(len(allC)):
            if (1<<j) &i :
                acc *= allC[j]
        ret.add(acc)
    return ret
class Solution:
    def minAnagramLength(self, s: str) -> int:
        c = Counter(s)
        ABC = 'abcdefghijklmnopqrstuvwxyz'
        cand = []
        for a in ABC:
            if c[a] >0:
                cand.append(c[a])
        n = len(s)
        #print(c,cand)
        g = max( list(cand))
        for a in cand:
            g = math.gcd(g,a)
        allD = getAllDiv(g)
        keys= sorted( list(allD), reverse= True)
        for m in keys:
            k = n //m
            dic = defaultdict(int)
            for i in range(0,n,k):
                s1 = s[i:i+k]
                ct =Counter(s1)
                tl = []
                for a in ABC:
                    tl.append(ct[a])
                dic[tuple(tl)] +=1
            
            if len(dic)==1:
                return k




re =Solution().minAnagramLength( "abba")
print(re)
# StringHash search
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod
    
    
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        sh = StringHash(s)
        aidx =[]
        bidx =[]
        ahs = StringHash(a)
        bsh = StringHash(b)
        ak = ahs.query(0,len(a))
        bk = bsh.query(0,len(b))
        for i in range(n -len(a)+1):
            if sh.query(i,i+len(a)) == ak:
                aidx.append(i)
        for i in range(n -len(b)+1):
            if sh.query(i,i+len(b)) == bk:
                bidx.append(i)
        #aidx = [i for i in range(n) if s.startswith(a,i) ]
        #bidx = [i for i in range(n) if s.startswith(b,i)]
        bidx = [-10**10] +bidx + [10**10]
        m = len(bidx)
        l = 0 
        ret =[]
        
        for ai in aidx:
            while l< m and bidx[l+1]<=ai:
                l +=1
            #print(ai,l,bidx)
            if abs(ai - bidx[l]) <= k or abs(bidx[l+1] -ai) <=k:
                ret.append(ai)
        return ret



re =Solution().beautifulIndices(s = "a"*100000, a = "a"*20000, b = "a"*30000, k = 20000)
print(re)





# re =Solution()
# print(re)
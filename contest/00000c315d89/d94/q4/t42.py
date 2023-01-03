from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import Counter

mod  = 10**9+7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret
@cache
def inv(x):
    return quickPow(x,mod-2)

class Solution:
    def countAnagrams(self, s: str) -> int:
        mod  = 10**9+7
        ls = s.split(" ")
        acc =1 

        def comb2(n,m):
            if m==n:
                return 1
            cnt = 1
            acc =1
            for i in range(m):
                cnt *=(n-i) %mod
            for i in range(m):
                acc *= (i+1)%mod
            cnt *= inv(acc)
                #cnt =cnt%mod
            return cnt
        #print(len(ls))
        for a in ls:
            n = len(a)
            c = Counter(a)
            for i,n1 in c.items():
                acc = acc* comb2(n,n1) %mod
                n = n-n1
        return acc


re =Solution().countAnagrams( "a"*50000+"b"*20000+"c"*20000+"d"*20000)
print(re)
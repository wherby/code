from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 10**9+7
        c = [-1]*n
        als,bls ='{:050b}'.format(a)[-n:],'{:050b}'.format(b)[-n:]
        #print(als,bls)
        als=[int(i) for i in als]
        bls=[int(i) for i in bls]
        #print(als,bls)
        # a1,b1= a,b
        # for i in range(n-1,-1,-1):
        #     at,bt = a1//(1<<i),b1//(1<<i)
        #     a1 -= at*(1<<i)
        #     b1 -= bt*(1<<i)
        #     als.append(at)
        #     bls.append(bt)
        #print(als,bls)
        for i in range(n):
            if als[i] == bls[i]:
                c[i] = 1-als[i]
        #print(c,i,als,bls)
        at,bt =a //(1<<(n)),b//(1<<(n)) 
        for i in range(n):
            at,bt = at*2,bt*2
            if c[i] != -1:
                at += (als[i] ^ c[i]) 
                bt += (bls[i]^c[i])
            elif at >=bt:
                c[i] = 1-bls[i]
                at += (als[i] ^ c[i]) 
                bt += (bls[i]^c[i])
            else:
                c[i] = 1-als[i]
                at += (als[i] ^ c[i]) 
                bt += (bls[i]^c[i])
        #print(c)
        cc = 0
        for i in c:
            cc= cc*2 +i
        #print(cc,a,b,c)
        return (a^cc)*(b^cc)%mod



re =Solution().maximumXorProduct(a = 12, b = 5, n = 4)
print(re)
# 1100,0101
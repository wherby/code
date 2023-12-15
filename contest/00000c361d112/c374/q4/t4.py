from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
mod = 10**9 +7



class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        def quickPow(x,y):
            ret =1
            cur = x 
            while y >0:
                if y & 1:
                    ret = ret * cur % mod
                cur = cur *cur % mod
                y = y //2
            return ret

        def inv(x):
            return quickPow(x,mod-2)
        def comb2(n,m, mod= 10**9+7):
            cnt = 1
            acc =1
            for i in range(m):
                cnt *=(n-i) %mod
                acc *= (i+1)%mod
            cnt = cnt* inv(acc)%mod
            return cnt
        mod = 10**9+7
        sick.sort()
        d,s = [],[]
        m = len(sick)
        for i in range(1,m):
            d.append(sick[i]-sick[i-1]-1)
        if sick[0] != 0:
            s.append(sick[0])
        if sick[-1] != n-1:
            s.append(n-1- sick[-1])
        ret = 1
        for a in d:
            ret = ret * quickPow(2,a-1) %mod
        cnt1 = sum(d) + sum(s)
        ads = d+s
        for a in ads:
            ret = ret* comb2(cnt1,a,mod) %mod
            cnt1 -=a
        return ret %mod
        
        





re =Solution().numberOfSequence(100000,[2510,3199,3918,4487,8785,9266,14154,15449,22538,28707,32831,33117,37673,38416,44485,47577,49248,50147,60773,66823,80580,82775,84330,87851,87953,89189,91514,92517,97026])
print(re)
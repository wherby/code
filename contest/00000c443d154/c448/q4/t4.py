from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

import itertools

mod = 10**9+7
MX=31
fac = [1]*MX
for i in range(1,MX):
    fac[i] = fac[i-1]*i%mod
inv_f =[1]*MX
inv_f[MX-1] = pow(fac[MX-1],mod-2,mod)
for i in range(MX-2,-1,-1):
    inv_f[i] = inv_f[i+1]*(i+1)%mod

class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        
        @cache
        def dfs(idx,leftM, leftK,acc):
            if idx ==n:
                return 1 if leftM ==0 and acc.bit_count() ==leftK else 0 
            ret =0
            for j in range(leftM+1):
                bitSet = (acc+j)%2 
                newAcc =acc + j
                ret += dfs(idx+1,leftM -j , leftK -bitSet,newAcc >>1) * pow(nums[idx],j,mod)*inv_f[j]
                ret %=mod 
            return ret
        return dfs(0,M,K,0) * fac[M]%mod
re =Solution().magicalSum(M = 5, K = 5, nums = [1,10,100,10000,1000000])
print(re)
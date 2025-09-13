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


mod = 10**9+7
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        
        @cache
        def dp(res,r):

            if r < 0:
                return 1 
            if 1<<(r+1)<=res:
                return 1<<(r//2+1)%mod
            ret = dp(res//2,r-2)
            cmp = 1<<r 
            if r != 0:
                cmp +=1
            if cmp <= res:
                ret += dp((res-cmp)//2,r-2)
            return ret%mod
            
        m = n.bit_length()
        cnt = 0 
        for i in range(m,0,-1):
            if n - (1<<i) -1 >=0:
                cnt += dp((n -(1<<i) -1)//2 ,i -2)
                #print(i,cnt)
        dp.cache_clear()
        if n >0:
            cnt +=1
        return (cnt+1)%mod





re =Solution().countBinaryPalindromes(1374389534700000000000 *(10**199))
print(re)
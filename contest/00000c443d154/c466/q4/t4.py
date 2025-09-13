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

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        
        @cache
        def dp(res,r,l):
            if res >= 1<<(r+1):
                return 2**((r-l)//2 +1)
            if r <l:
                return 1 
            ret = dp(res,r-1,l+1)
            cmp = 1<<r 
            if r != l :
                cmp += 1<<l
            if res >= cmp:
                ret +=dp(res-cmp,r-1,l+1)
            return ret
        m = n.bit_length()
        cnt = 0 
        for i in range(m,0,-1):
            if n - (1<<i) -1 >=0:
                cnt += dp(n -(1<<i) -1 ,i -1,1)
                #print(i,cnt)
        dp.cache_clear()
        if n >0:
            cnt +=1
        return cnt+1





re =Solution().countBinaryPalindromes(137438953470)
print(re)
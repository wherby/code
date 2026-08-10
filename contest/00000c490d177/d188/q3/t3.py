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
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        
        dp =[0]*(n+1)
        for l,r,v in boosts:
            dp[l] +=v
            dp[r+1] -=v 
        pls = [0]*n 
        cur = 0 
        for i in range(n):
            cur += dp[i]
            pls[i] = cur 
        l,r = 0,sum(monsters)
        def verify(mid):
            cur =mid 
            for i in range(n):
                if cur + pls[i] < monsters[i]:
                    return False
                cur = max(0,cur -monsters[i])
            return True
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r =mid
            else:
                l= mid +1
        return l



re =Solution().minInitialStrength(monsters = [5,10,15], boosts = [[1,2,10],[1,2,5]]
)
print(re)
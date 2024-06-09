from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        l,r = 0, 10**20
        coins.sort()
        n = len(coins)
        def getls():
            ret =[]
            for i in range(1,1<<n):
                lcm =1
                acc = -1
                for j in range(n):
                    if (1<<j)&i:
                        acc*=-1
                        lcm = math.lcm(coins[j],lcm)
                ret.append((lcm,acc))
            return ret
        ls = getls()
        #print(ls)
        def verify(mid):
            return sum([mid//a*acc for a,acc in ls]) >=k
        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r = mid 
            else:
                l = mid+1
            #print(mid)
        return l





re =Solution().findKthSmallest([3,6,9],3)
print(re)
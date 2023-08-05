from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList



class Solution:
    def maxIncreasingGroups(self, us2: List[int]) -> int:
        def verify(mid):
            us=list(us2)
            us.sort(reverse=True)
            acc=0
            for i in range(mid,n):
                acc += us.pop()
            for i in range(1,mid+1):
                acc += us.pop()
                acc -= i 
                if acc<0:
                    return False
            return True
            
        n = len(us2)
        l,r = 1,n 
        while l<r:
            mid = (l+r+1)>>1
            #print(mid)
            #print(mid,verify(mid))
            if verify(mid):
                l =mid
            else:
                r=mid-1
            #print(l,r)
        return l
            
            





re =Solution().maxIncreasingGroups([2,2,2])
print(re)
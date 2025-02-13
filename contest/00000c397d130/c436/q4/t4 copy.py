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
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)
        l,r = 0,10**17
        if len(points) == 2:
            return min(points[0]*(m-m//2)  ,points[1]*(m//2))
        #print("a")
        def verify(mid):
            ls=[(mid + p -1)//p for p in points]
            print(ls,mid)
            lft = ls[0]
            for i in range(1,n):
                if ls[i] <  lft:
                    ls[i] = lft - (i==n-1)
                    lft = 0
                else:
                    lft = ls[i]- lft
            lft =0
            for i in range(n-2,-1,-1):
                if ls[i] < lft:
                    ls[i] = lft 
                    lft =0
                else:
                    lft = ls[i]- lft
            print(ls)
            return sum(ls) <=m

                    

        while l < r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid -1 
        return l





#re =Solution().maxScore(points = [2,4], m = 3)
#re =Solution().maxScore(points = [4,2], m = 9)
re = Solution().maxScore([23,10,7],25)
print(re)
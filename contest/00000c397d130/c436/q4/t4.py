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
            lft = 0
            cnt =0
            for i,a in enumerate(points):
                t = (mid +a -1) // a
                if t <lft :
                    t  = lft-(i == n-1)
                    lft =0 
                else:
                    lft = max(0, t- lft-1)
                cnt += t    
            return cnt <=m

        while l < r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid -1 
        return l





#re =Solution().maxScore(points = [2,4], m = 3)
re =Solution().maxScore(points = [4,2], m = 9)
print(re)
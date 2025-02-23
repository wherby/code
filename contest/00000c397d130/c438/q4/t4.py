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
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        ls = [[] for _ in range(4)]
        for x,y in points:
            if y ==0 and x != side:
                ls[0].append((x,y))
            if x == side and y != side:
                ls[1].append((x,y))
            if y ==side and x != 0:
                ls[2].append((x,y))
            if x == 0 and y !=0:
                ls[3].append((x,y))
        lss = []
        for i,a in enumerate(ls):
            if i <=1:
                a.sort()
                for x,y in a:
                    lss.append(x+y)
            else:
                a.sort(reverse= True)
                for x,y in a:
                    lss.append(4*side - x-y)
        n = len(lss)
        #print(lss)
        lss.extend([4*side +a for a in lss])
        #print(lss)
        def verify2(mid,start):
            cur = start
            for _ in range(k):
                t = bisect_left(lss,lss[cur]+mid)
                if t-start >n or lss[t]-lss[cur] <mid:
                    return False
                #print(mid,lss[start],lss[t])
                cur= t 
            return True
             
        def verify(mid):
            for i in range(n):
                if verify2(mid,i):
                    return True
            return False

        l,r = 1, side
        while l<r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid -1
        return l
            





re =Solution().maxDistance(side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4)
print(re)
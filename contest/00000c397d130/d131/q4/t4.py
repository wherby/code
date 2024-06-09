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
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = 0 
        for q in queries:
            mx = max(mx,q[1])
        st =[(-mx,0,mx)]
        sl=SortedList([(0,mx+1),(mx+1,mx+1)])
        rmd = {}
        ret = []
        for q in queries:
            if q[0] ==1:
                x = q[1]
                k = sl.bisect_left((x,x))
                rm1 = sl[k-1]
                left,right =rm1
                sl.remove(rm1)
                sl.add((left,x))
                sl.add((x,right))
                rmd[(left-right,left,right)] =1
                heappush(st,(left-x,left,x))
                heappush(st,(x-right,x,right))
                #print(left,right,st,q)
            else:
                x,d = q[1],q[2]
                while st[0]  in rmd:
                    heappop(st)
                #print(q,x,d,st)
                if -st[0][0] >= d:
                    ret.append(True)
                else:
                    ret.append(False)
        return ret
                




re =Solution().getResults(queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]])
print(re)
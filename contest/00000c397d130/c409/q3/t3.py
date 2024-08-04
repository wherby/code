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
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ls = [i for i in range(n-1)]
        ret =[]
        sl = SortedList(ls)
        for a,b in queries:
            l = sl.bisect_left(a+1)
            r = sl.bisect_left(b)
            rm = []
            #print(l,r,sl)
            for i in range(l,r):
                rm.append(sl[i])
            for a in rm:
                sl.remove(a)
            ret.append(len(sl))
        return ret


re =Solution().shortestDistanceAfterQueries( n = 5, queries = [[1,3],[2,4]])
print(re)
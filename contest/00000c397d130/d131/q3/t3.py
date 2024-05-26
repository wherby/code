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
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        rdic = {}
        ret = []
        for a,b in queries:
            if a not in rdic:
                rdic[a] = b
            else:
                t = rdic[a]
                dic[t].remove(a)
                if len(dic[t]) ==0:
                    del dic[t]
                rdic[a] = b
            dic[b].add(a)
            ret.append(len(dic))
        return ret





re =Solution().queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]])
print(re)
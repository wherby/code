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
from itertools import pairwise
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        ret = -1 
        dic = defaultdict(list)
        for a,b in points:
            dic[a].append(b)
        keys = list(dic.keys())
        keys.sort()
        n = len(keys)
        for i in range(1,n):
            ord={}
            k0 = dic[keys[i-1]]
            k0.sort()
            for j,a in enumerate(k0):
                ord[a] =j 
            k1 = dic[keys[i]]
            k1.sort()
            for a,b in pairwise(k1):
                if a in ord and b in ord and ord[b] -ord[a] ==1:
                    ret =max(ret,(b-a) * (keys[i] -keys[i-1]))
        return ret





re =Solution().maxRectangleArea( points = [[100,80],[67,79],[100,79],[67,80],[80,47]])
print(re)
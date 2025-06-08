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
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        if len(set(x)) <3:
            return -1 
        dic = defaultdict(int)
        for i,a in enumerate(x):
            dic[a] = max(dic[a],y[i])
        vs = list(dic.values())
        vs.sort(reverse=True)
        return sum(vs[:3])




re =Solution().maxSumDistinctTriplet(x = [1,2,1,3,2], y = [5,3,4,6,2])
print(re)
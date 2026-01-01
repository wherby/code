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
    def minCost(self, s: str, cost: List[int]) -> int:
        dic = defaultdict(int)
        for i,c in enumerate(cost):
            dic[s[i]] +=c 
        return sum(dic.values()) - max(dic.values())





re =Solution()
print(re)
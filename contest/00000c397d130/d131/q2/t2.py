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
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        ret =[]
        ls = dic[x]
        for q in queries:
            if len(ls) >= q:
                ret.append(ls[q-1])
            else:
                ret.append(-1)
        return ret 





re =Solution()
print(re)
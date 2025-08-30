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
from collections import defaultdict,deque
from itertools import pairwise

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0]*n
        sl = SortedList()
        sl2 = SortedList()
        for i,a in enumerate(nums):
            sl.add((a,i))
            sl2.add(i)
        while sl:
            a,i = sl.pop()
            a = max(a,ret[i])
            rm = []
            kidx = sl2.bisect_left(i)
            for j in range(kidx,len(sl2)):
                rm.append(sl2[j])
                ret[j] =a
            for j in rm:
                sl2.remove(j)
            if len(rm):
                sl.add((a,rm[-1]))
            print(sl)
        return ret



re =Solution().maxValue([30,21,5,35,24])
print(re)
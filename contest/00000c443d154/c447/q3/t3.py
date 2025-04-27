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
import itertools
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        lss= itertools.permutations(nums)
        ret = []
        for ls in lss:
            ls1 = [str(a) for a in ls]
            t = "".join(ls1)
            if int(t)%k ==0:
                ret.append(ls)
        ret.sort()
        if len(ret) ==0:
            return []
        return [a for a in ret[0]]





re =Solution().concatenatedDivisibility(nums = [3,12,45], k = 5)
print(re)
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
from collections import Counter
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        c =Counter(nums)
        m = n //k
        if n%k !=0:
            return False
        for k,v in c.items():
            if v>m:
                return False
        return True





re =Solution()
print(re)
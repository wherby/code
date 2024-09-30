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
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [k for k,v in c.items() if v >1]





re =Solution()
print(re)
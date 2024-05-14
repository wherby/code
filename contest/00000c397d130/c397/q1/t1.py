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
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum([abs(s.find(a) -t.find(a)) for a in s])





re =Solution().findPermutationDifference("rwohu","rwuoh")
print(re)
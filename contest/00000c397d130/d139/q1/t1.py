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
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i,a in enumerate(height) if i > 0 and height[i-1]>threshold]





re =Solution()
print(re)
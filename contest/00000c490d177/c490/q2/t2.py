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
    def isDigitorialPermutation(self, n: int) -> bool:
        ls = list(str(n))
        acc = 0
        for a in ls:
            acc += math.factorial(int(a))
        ls.sort()
        ls2 = list(str(acc))
        ls2.sort()
        return ls == ls2





re =Solution()
print(re)
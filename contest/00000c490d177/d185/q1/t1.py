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
    def createGrid(self, m: int, n: int) -> list[str]:
        ret  = [["#"]*n for _ in range(m)]
        for i in range(m):
            ret[i][0] = "."
        for j in range(n):
            ret[m-1][j] = "."
        ret = ["".join(arr) for arr in ret]
        return ret





re =Solution()
print(re)
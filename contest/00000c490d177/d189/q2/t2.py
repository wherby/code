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
    def minOperations(self, s: str) -> int:
        n = len(s)
        ls = [ord(a) - ord('a') for a in s]
        mx = n*26
        for i in range(n):
            nls = ls[i:] + ls[:i]
            acc = 0 
            for j in range(n//2):
                acc += min(26-abs(nls[j] - nls[n-1-j]),abs(nls[j] - nls[n-1-j]))
            mx = min(mx,acc+i)
        return mx





re =Solution().minOperations("abc")
print(re)
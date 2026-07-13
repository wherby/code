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
    def maxDigitRange(self, nums: list[int]) -> int:
        ls =[[] for _ in range(10)]
        for num in nums:
            tl = [int(a) for a in str(num)]
            k = max(tl) - min(tl)
            ls[k].append(num)
        while ls:
            t1 = ls.pop()
            if len(t1):
                return sum(t1) 






re =Solution()
print(re)
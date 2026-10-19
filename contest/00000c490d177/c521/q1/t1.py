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
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ls = [0]*101
        ans = []
        for a in nums:
            ls[a] +=1
        for _ in range(100):
            for j in range(1,101):
                if ls[j] !=0:
                    ans.append(j)
                    ls[j] -=1
        return ans




re =Solution()
print(re)
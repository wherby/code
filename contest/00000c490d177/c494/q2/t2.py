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
    def uniformArray(self, nums1: list[int]) -> bool:
        ls =[[] for _ in range(2)]
        for a in nums1:
            ls[a%2].append(a)
        if len(ls[0]) == 0 or len(ls[1]) ==0:
            return True 
        mn =min(nums1)
        if mn%2 == 0:
            return False 
        return True
        




re =Solution()
print(re)
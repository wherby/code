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
    def longestSubarray(self, nums: list[int], k: int) -> int:
        ndic = {}
        ndic[0] = -1
        dic ={}
        dic[0] = -1
        mx = 0
        acc =0 
        for i,a in enumerate(nums):
            acc =(acc+a)%k 
            target =(acc-2*a)%k 
            if target in ndic:
                start = ndic[target]
                mx = max(mx, i - start)
            if target not in dic:
                dic[target] = i
            if acc in ndic:
                mx = max(mx,i- ndic[acc])
            if acc in dic:
                mx = max(mx,i-dic[acc])
            if acc not in ndic:
                ndic[acc] = i 
        return mx 





re =Solution().longestSubarray([13,14,-7],8)
print(re)
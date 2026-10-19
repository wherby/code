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
        lst =[-1]*k
        fst = [-1]*k 
        dic =[deque() for _ in range(k)]
        acc = 0
        for i,a in enumerate(nums):
            acc = (acc+a)%k
            dic[a%k].append(i)
            lst[acc%k] = i 
        acc =0
        mx = 0
        for i,a in enumerate(nums):
            acc = (acc+a)%k 
            if fst[acc] ==-1:
                mx = max(mx,lst[acc] - i )
                fst[acc] = i 
                for j,b in enumerate(lst):
                    if b > i 




re =Solution().longestSubarray([13,14,-7],8)
print(re)
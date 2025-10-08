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
    def longestSubsequence(self, nums: List[int]) -> int:
        acc = 0 
        mx =0
        for i,a in enumerate(nums):
            acc= acc ^a 
            if acc !=0:
                mx = max(mx,i+1)
        n = len(nums)
        if acc ==0:
            if mx==0:
                return 0 
            return n-1
        return n 





re =Solution()
print(re)
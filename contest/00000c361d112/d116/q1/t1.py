from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        acc =0
        for i in range(n):
            for j in range(i+1,n+1):
                ls = set(nums[i:j])
                #print(ls)
                acc += len(ls)**2
        return acc %mod





re =Solution().sumCounts( [1,2,1])
print(re)
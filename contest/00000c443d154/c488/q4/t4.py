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
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m,n = len(nums1),len(nums2)
        @cache
        def dfs(i,j,k):
            if k == 0:
                return 0 
            if i == m or j == n:
                return - math.inf
            return max(nums1[i]*nums2[j]+dfs(i+1,j+1,k-1),dfs(i+1,j,k),dfs(i,j+1,k))
        ret =  dfs(0,0,k)
        dfs.cache_clear()
        return ret





re =Solution()
print(re)
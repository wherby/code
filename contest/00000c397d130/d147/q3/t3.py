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
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        n = len(nums)
        curDic = defaultdict(int)
        mn,mx = min(nums),max(nums)

        def dfs(idx,sp):
            if idx ==n-1:
                return 1
            a =nums[idx]
            for i in range(min)
            





re =Solution()
print(re)
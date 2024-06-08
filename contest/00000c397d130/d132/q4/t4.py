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
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        
        @cache
        def dfs(lstv,idx,cnt):
            if cnt ==0:
                return len(dic[lstv]) - bisect_left(dic[lstv], idx)
            if idx ==n:
                return 0
            if nums[idx] == lstv:
                return dfs(lstv,idx+1,cnt)+1
            return max(dfs(nums[idx],idx+1,cnt-1)+1,dfs(lstv,idx+1,cnt))
        return dfs(-1,0,k+1)
        





re =Solution().maximumLength([30,30],0)
print(re)
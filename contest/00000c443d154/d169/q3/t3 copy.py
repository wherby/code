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


from math import ceil, log2
 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0 

        @cache
        def dfs(idx,last,used,mcur):
            nonlocal mx
            mx = max(mx,mcur)
            if idx == n :
                return 0
            if nums[idx] >= last:
                dfs(idx+1,nums[idx],used,mcur +1)
                if used == False:
                    dfs(idx+1,last,True,mcur+1)
            else:
                if used == False:
                    if mcur >1 and   nums[idx] >= nums[idx-2]:
                        dfs(idx+1,nums[idx],True,mcur+1)
                    dfs(idx+1,last,True,mcur +1)

                dfs(idx+1,nums[idx],used,1) 
        dfs(0,-10**10,False,0)
        return mx



re =Solution().longestSubarray( nums =[1,2,3,1,2])
print(re)
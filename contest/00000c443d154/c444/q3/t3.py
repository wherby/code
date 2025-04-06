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
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        ret = -1

        @cache
        def dfs(idx,acc,mn,s,isG):
            nonlocal ret
            #print(acc,mn,idx)
            if acc == k and mn <=limit and isG:
                #print(acc,ret)
                ret = max(ret,mn)
            if idx ==n:
                return -1
            dfs(idx+1,acc,mn,s,isG)
            dfs(idx+1,acc+s*nums[idx],min(mn*nums[idx] ,limit +1),s*-1,True)
        dfs(0,0,1,1,False)
        dfs.cache_clear()
        return ret




re =Solution().maxProduct(nums = [0,8], k = -8, limit = 10)
print(re)
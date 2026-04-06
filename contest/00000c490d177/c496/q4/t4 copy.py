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
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if n //2 < k:
            return -1

        
        
        def min_cost(ls,k):

            @cache
            def dfs(res,idx):
                if res == 0:
                    return 0
                if res >(idx+1)//2:
                    return 10**30
                return min(dfs(res,idx-1),dfs(res-1,idx-2)+max(0,max(ls[idx-1], ls[idx+1] )- ls[idx]+1))
            ret = dfs(k,len(ls)-2)
            dfs.cache_clear()
            return ret 
        ls1 = nums + [nums[0]]
        ls2 = [nums[-1]]+nums
        return min(min_cost(ls1,k),min_cost(ls2,k))
        
        







re =Solution()
print(re)
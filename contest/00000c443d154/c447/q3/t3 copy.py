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
import itertools
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans =[]
        ls =[]
        nums.sort()
        @cache
        def dfs(state,res):
            if state == 0 and res ==0:
                ans.append(list(ls))
                return True
            if state ==0:
                return False
            for i in range(n):
                if (1<<i)&state:
                    ls.append(nums[i])
                    m = len(str(nums[i] ))
                    t1  = res * (10**m) + nums[i]
                    t1 = t1%k
                    if dfs(state - (1<<i),t1):
                        return True
                    ls.pop()
            return False
        dfs((1<<n)-1,0)
        return ans[0] if len(ans) >0 else []
                    
            
            





re =Solution().concatenatedDivisibility(nums = [3,12,45], k = 5)
print(re)
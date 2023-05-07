from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList



class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        cost = [0]+cost
        ret =0
        n = n+1

        def dfs(i):
            nonlocal ret
            if i >= n:
                return 0 
            left = dfs(i*2)
            right = dfs(i*2+1)
            mx = max(left,right)
            ret += mx*2-left-right
            return cost[i] +mx
        dfs(1)
        return ret
                





re =Solution().minIncrements(n = 7, cost = [1,5,2,2,3,3,1])
print(re)
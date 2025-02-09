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
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:

        n = len(target)
        @cache
        def cost(state):
            lcm = 1
            for i in range(n):
                if state &(1<<i):
                    lcm = math.lcm(lcm,target[i])
            mx  = lcm
            for a in nums:
                mx = min(mx, (lcm - a %lcm)%lcm)
            return mx

        @cache
        def dfs(state):
            if state ==(1<<n)-1:
                return 0
            ret = 10**10
            for i in range(1,2<<(n-1)):
                if i&state ==0 :
                    ret = min(ret, dfs(i|state) + cost(i))
            print(ret,state)
            return ret
        return dfs(0)




re =Solution().minimumIncrements(nums = [8,10,9], target = [10,6,6])
print(re)
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
        def get_cost(i):
            l = nums[(i - 1) % n]
            r = nums[(i + 1) % n]
            return max(0, max(l, r) + 1 - nums[i])
        

        costs = [get_cost(i) for i in range(n)]
        if n  == k*2:
            return min(sum(costs[1::2]),sum(costs[0::2]))
        
        def get_min(costls):
            length = len(costls)
            m = length // 2
            pre = [0] * (m + 1)
            suf = [0] * (m + 1)
            
            for i in range(m):
                pre[i+1] = pre[i] + costls[2*i]
            for i in range(m-1, -1, -1):
                suf[i] = suf[i+1] + costls[2*i+1]
                
            res = 10**30
            for i in range(m + 1):
                res = min(res, pre[i] + suf[i])
            return res


        return get_min(costs[:-1])







re =Solution()
print(re)
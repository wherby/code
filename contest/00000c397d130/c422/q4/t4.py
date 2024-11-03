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
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 +7
        n = len(num)
        ls = [0]*10
        for a in num:
            ls[int(a)]+=1
        @cache
        def dfs(state,idx,acc):
            if idx == n:
                if acc ==0:
                    return 1
                return 0
            
            ret =0
            for i in range(10):
                if state[i]< ls[i]:
                    ns = list(state)
                    ns[i] +=1
                    ns = tuple(ns)
                    ret += dfs(ns,idx+1, acc +(-1)**idx *i)
            return ret
        return dfs(tuple([0]*10),0,0)%mod





re =Solution().countBalancedPermutations("1234"*20)
print(re)
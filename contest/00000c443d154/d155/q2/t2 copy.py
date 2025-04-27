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

from input import nums
import sys
sys.setrecursionlimit(1500000)

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 10**9+7
        n = len(conversions)+1
        ret = [-1]*n 
        g = [[] for _ in range(n)] 
        for a,b,c in conversions:
            g[a].append((b,c))
        
        def dfs(idx,acc):
            if ret[idx] != -1:
                return
            ret[idx] = acc%mod 
            for b,c in g[idx]:
                if ret[b] ==-1:
                    dfs(b,c*acc)
        dfs(0,1)
        return ret
        





re =Solution().baseUnitConversions(nums)
print(re)
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
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i,a in enumerate(parent):
            if a >=0:
                g[a].append(i)
        
        def dfs(a):
            ret = 1 
            for b in g[a]:
                ret = max(ret,dfs(b)+1)
            return ret 
        h = dfs(0)
        
        def dfs2(a,d):
            ret = nums[a] * (h-d +1)
            for b in g[a]:
                ret += dfs2(b,d+1)
            return ret 
        return dfs2(0,1)




re =Solution().weightedSum( parent = [-1,0,0,0,2,2], nums = [5,2,3,1,4,6])
print(re)
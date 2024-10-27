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
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        @cache
        def dfs(i,j):
            if i ==k:
                return 0
            ret =0
            ret = max(ret,stayScore[i][j] + dfs(i+1,j))
            for k1 in range(n):
                if k1 == j: continue
                ret = max(ret,travelScore[j][k1] + dfs(i+1,k1))
            return ret 
        return max([dfs(0,j) for j in range(n) ])

        





re =Solution().maxScore(n = 3, k = 2, stayScore = [[3,4,2],[2,1,2]], travelScore = [[0,2,1],[2,0,4],[3,2,0]])
print(re)
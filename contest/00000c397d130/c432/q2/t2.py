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
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m,n = len(coins),len(coins[0])

        @cache
        def dfs(i,j,k):
            if i >= m or j >=n:
                return -10**10
            if i == m-1 and j ==n-1:
                if coins[i][j] >=0 or k==0:
                    return coins[i][j]
                return 0
            ret = -10**10
            if coins[i][j]<0 and k >0:
                ret = max(ret,dfs(i+1,j,k-1))
                ret = max(ret,dfs(i,j+1,k-1))
            ret = max(ret,dfs(i+1,j,k) + coins[i][j])
            ret = max(ret,dfs(i,j+1,k) + coins[i][j])
            return ret
        return dfs(0,0,2)





re =Solution().maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]])
print(re)
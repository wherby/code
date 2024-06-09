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
    def maxScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        mx =  grid[0][1]-grid[0][0] 
        dp = [[-10**10] *(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mx = max(mx,max(dp[i+1][j], dp[i][j+1])-grid[i][j])
                #print(mx,i,j,grid[i][j], min(dp[i+1][j], dp[i][j+1]))
                dp[i][j]=max(grid[i][j],dp[i+1][j], dp[i][j+1] )
    
        #print(dp)
        
        return mx





re =Solution().maxScore( [[10,5],[5,1]])
print(re)
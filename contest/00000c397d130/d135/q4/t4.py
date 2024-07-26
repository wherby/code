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
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ng = [[0]*(n+2) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ng[i][j+1] =grid[i][j]
        dp=[]
        for i in range(2):
            dp.append([[0]*(n+2) for _ in range(n)])
        for i in range(n):
            dp[1][i][0] = -10**10
        cur =0
        for j in range(n):
            last =0
            for i in range(n):
                last = max(last,dp[0][i][j],dp[1][i][j])
            acc=0
            reverse = [0]
            for i in range(n-1,-1,-1):
                reverse.append(max(reverse[-1],dp[0][i][j]))
            for i in range(n):
                cur += grid[i][j]
                acc += grid[i][j]
                cur -= ng[i][j]
                dp[0][i][j+1]=max(last,dp[1][i][j] + cur,reverse[-(i+1)] +acc)
                dp[1][i][j+1]=last
        mx = 0
        for i in range(2):
            mx = max([max(a) for a in dp[i]])
        return mx




re =Solution().maximumScore(grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]])
print(re,94)
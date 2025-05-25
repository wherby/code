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
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g= [[] for _ in range(n)]
        p = [-1]*n
        for a,b in hierarchy:
            g[a-1].append(b-1)
            p[b-1]=a-1
        dp =[[0]*(budget+1) for _ in range(2*n+1)]
        for i in range(2*n+1):
            dp[i][0] = 0
        for i in range(n):
            for j in range(budget+1):
                dp[i+n][j] = -10**10
        
        ord=[]
        def dfs(a):
            ord.append(a)
            for b in g[a]:
                dfs(b)
        dfs(0)
        #print(p,ord)
        for i,a in enumerate(ord):
            pres = ord[i-1]
            pa = p[a]
            if i !=0:
                for b in range(budget+1):
                    dp[a][b] =max(dp[a][b],dp[pres][b],dp[pres+n][b],0)
                
            for b in range(budget,present[a]//2 -1,-1):
                if b >=present[a]:
                    dp[a +n][b] = max(dp[pres][b-present[a]] +future[a]-present[a] ,dp[pres+n][b-present[a]] +future[a]-present[a] )
                if pa != -1:
                    dp[a+n][b] = max(dp[a+n][b], dp[pa+n][b - present[a]//2] +future[a]-present[a]//2 )
                    #print(b, dp[pres+n][b - present[a]//2],pres+n,dp[a+n][b])
            if pa != -1:
                for b in range(budget,-1,-1):
                    dp[pa][b] = max(dp[pa][b],dp[a][b],dp[a+n][b])
                    dp[a][b] = max(dp[a][b],dp[pa][b])
            #print(dp,i,a)
        return max([max(a) for a in dp])



#re =Solution().maxProfit(n = 3, present = [49,10,27], future = [18,44,38], hierarchy = [[1,3],[1,2]], budget = 141)
re =Solution().maxProfit(n = 3, present = [6,4,23], future =[50,48,17], hierarchy =[[1,3],[1,2]], budget = 28)
print(re)
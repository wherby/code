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
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        g = [[] for _ in range(n)]
        ind = [0]*n 
        for a,b,c in edges:
            g[a].append((b,c))
            ind[b]+=1
        dp =[[-1]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = [0]
        queue= deque()
        for i in range(n):
            if ind[i] == 0:
                queue.append(i)
        while queue:
            a = queue.popleft()
            for b,c in g[a]:
                for i in range(k):
                    if dp[a][i] != -1:
                        dp[b][i+1] = set([d +c for d in dp[a][i] if d+c < t] + (list(dp[b][i+1]) if dp[b][i+1] != -1 else[])) 
                ind[b] -=1
                if ind[b] ==0:
                    queue.append(b)
        ret = -1
        #print(dp)
        for a in range(n):
            if dp[a][k] != -1  and len(dp[a][k])>0:
                ret = max(ret, max( dp[a][k]))
        return ret  





# re =Solution().maxWeight( n = 3, edges = [[0,1,6],[1,2,8]], k = 1, t = 6)
# re =Solution().maxWeight(  n = 3, edges = [[0,1,1],[1,2,2]], k = 2, t = 4)
re = Solution().maxWeight(4,[[0,2,6],[2,3,2],[0,3,7]],1,588)
print(re)
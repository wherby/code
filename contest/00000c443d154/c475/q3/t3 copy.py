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
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid),len(grid[0])
        
        dic ={}
        start = [-1]*(k+1)
        start[0] = 0
        dic[(0,0)] = start
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j== 0:
                    continue 
                if j != 0:
                    pre =dic[(i,j-1)]
                    b = grid[i][j]
                    if b ==0:
                        dic[(i,j)] = pre 
                    else:
                        nstat = [-1]*(k+1)
                        for kt in range(k):
                            if pre[kt]>=0:
                                nstat[kt+1] = pre[kt]+b 
                        dic[(i,j)] = nstat
                if i!= 0 :
                    pre =dic[(i-1,j)]
                    b = grid[i][j]

                    if b ==0:
                        if (i,j) not in dic: 
                            dic[(i,j)] = [-1]*(k+1) 

                        state1 = dic[(i,j)]
                        state1 = [max(a1,b1)  for a1,b1 in zip(state1,pre)]
                        dic[(i,j)] = state1
                    else:
                        if (i,j) not in dic:
                            dic[(i,j)] = [-1]*(k+1)

                        state1 = dic[(i,j)]
                        nstat = [-1]*(k+1)
                        #print(pre,b)
                        for kt in range(k):
                            if pre[kt]>=0:
                                nstat[kt+1] = pre[kt]+b 
                        #print(nstat)
                        state1 = [max(a1,b1) for a1,b1 in zip(state1,nstat)]
                        #print(state1,(i,j))
                        dic[(i,j)] = state1
                    #print(dic)
        state = dic[(m-1,n-1)]
        #print(dic)
        return max(state)
            





re =Solution().maxPathScore([[0, 1],[1, 2]], k = 1)
print(re)
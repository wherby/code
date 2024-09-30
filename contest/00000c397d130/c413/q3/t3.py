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
        c = defaultdict(int)
        for a1 in grid:
            for b1 in a1:
                c[b1] +=1
        dicc = {}
        idx = 0 
        for k,v in c.items():
            if v ==1:continue
            dicc[k] = idx 
            idx +=1
        #print(dicc)
        @cache
        def dfs(idx,visit):
            #print(idx,visit,"a")
            visit2 = visit
            if idx == m:
                return 0 
            ret = 0 
            dic = {}
            ls= list(grid[idx])
            ls.sort(reverse= True)
            for a in ls:
                if a in dicc and ((visit &(1<<dicc[a])) ==0) :
                    visit += 1<<dicc[a]
                    ret = max(ret,a + dfs(idx+1,visit))
                    #print(visit,ret,"b",idx,visit2)
                    visit -= 1<<dicc[a]
                elif a not in dicc:
                    ret = max(ret, a + dfs(idx+1,visit))
                    break
            ret = max(ret,dfs(idx+1,visit))
            #print(idx,ret,visit)
            return ret
        return dfs(0,0)





re =Solution().maxScore([[5,5],[5,5],[11,5]])
print(re)
print(10*9*8*7*6*120)
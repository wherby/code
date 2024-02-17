from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ret = [0]*n 
        g=[[] for _ in range(n)]
        for i in range(n-1):
            g[i].append(i+1)
            g[i+1].append(i)
        if x != y and  abs(x-y) != 1:
            g[x-1].append(y-1)
            g[y-1].append(x-1)
        visit ={}
        def bfs(i):
            seed =[i]
            cnt =0
            while seed:
                tmp = []
                for a in seed:
                    if a in visit:continue
                    visit[a] =1
                    if cnt != 0:
                        ret[cnt-1] +=1
                    for b in g[a]:
                        tmp.append(b)
                cnt +=1
                seed = tmp
        for i in range(n):
            visit={}
            bfs(i)
        return ret




re =Solution().countOfPairs(n = 5, x = 2, y = 4)
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf


class Solution:
    def numberOfSets(self, n: int, maxv: int, roads: List[List[int]]) -> int:
        
        
        ans = 1
        for stat in range(1, 1<<n):
            edges = []
            for u, v, w in roads:
                if stat >> u & 1 == 0 or stat >> v & 1 == 0: continue
                if w > maxv: continue
                edges.append((u, v, w))
            
            d = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j: d[i][j] = 0
                    else: d[i][j] = math.inf
            
            for u, v, w in edges:
                d[u][v] = d[v][u] = min(d[u][v], w)
            if stat ==15:
                print(d)

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if stat ==15:
                print(d)
            
            flag = True
            for i in range(n):
                if stat >> i & 1:
                    for j in range(n):
                        if stat >> j & 1:
                            if d[i][j] > maxv: 
                                flag = False
                                break
                if not flag: break
            if flag:
                #print(stat) 
                ans += 1
        return ans
        



re =Solution().numberOfSets(10,430,[[3,2,237],[3,1,79],[6,1,84],[6,1,103],[9,6,453],[3,1,342],[3,1,201],[8,0,439],[7,5,467],[4,3,99],[8,7,146],[8,7,335],[6,1,512],[1,0,498],[5,3,241],[5,2,202],[4,1,443],[2,0,69],[2,1,450],[6,3,352],[2,0,438],[4,0,95],[6,1,257],[5,1,271],[8,1,80],[9,1,452],[3,1,57],[9,7,361],[8,4,105]])
print(re)
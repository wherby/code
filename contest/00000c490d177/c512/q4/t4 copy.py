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
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        INF = float('inf')

        dist = [[[INF] * 2 for _ in range(n)] for _ in range(m)]
        
        pq = []

        dist[0][0][1] = 1
        heapq.heappush(pq, (1, 0, 0, 1))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            d, r, c, p = heapq.heappop(pq)
            
            if d > dist[r][c][p]:
                continue
            if r == m - 1 and c == n - 1:
                return d
            next_d = d + penalty[r][c]
            next_p = 1 - p
            if next_d < dist[r][c][next_p]:
                dist[r][c][next_p] = next_d
                heapq.heappush(pq, (next_d, r, c, next_p))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    entry = (nr + 1) * (nc + 1)
                    is_legal = False
                    if p == 1 and (dr == 1 or dc == 1):
                        is_legal = True
                    elif p == 0 and (dr == -1 or dc == -1):
                        is_legal = True
                    cost = entry if is_legal else entry + penalty[r][c]
                    
                    if d + cost < dist[nr][nc][1 - p]:
                        dist[nr][nc][1 - p] = d + cost
                        heapq.heappush(pq, (d + cost, nr, nc, 1 - p))
            print(dist)





re =Solution().minCost(  m = 2, n = 5, penalty = [[602,754,766,5,98],[2,493,534,5,2]])
print(re)
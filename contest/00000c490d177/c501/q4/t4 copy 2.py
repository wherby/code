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
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for a,b,c,t in roads:
            g[a].append((b,c))
            g[b].append((a,c))
            rg[a].append((b,c*t))
            rg[b].append((a,c*t))
        def get_dist(start, g):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: continue
                for v, w in g[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))
            return dist

        ret = []
        for i in range(n):
            d1 = get_dist(i, g) 
            d2 = get_dist(i, rg) 
            res = prices[i]
            for j in range(n):
                res = min(res, d1[j] + prices[j] + d2[j])
            ret.append(res)
        return ret

prices = [81,59,57,74,69,45,81,10,77]
roads = [[2,4,65,7],[8,7,31,9],[6,3,12,1],[7,1,64,9],[2,1,24,8],[5,1,76,8],[7,5,12,7],[8,4,51,4],[7,3,73,6],[2,7,40,6],[3,5,11,4],[3,4,17,4],[1,3,17,1],[4,5,1,1],[1,0,4,7],[3,8,79,6],[6,4,1,2],[2,0,6,7],[0,7,61,6],[4,7,64,5],[3,0,61,4],[0,4,62,3],[1,8,35,4],[8,5,70,5],[2,5,53,8],[5,0,31,9],[6,8,27,9],[2,8,75,5],[6,5,78,6],[1,6,29,2]]


re =Solution().minCost(9,prices,roads)
print(re)
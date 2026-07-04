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
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
        
        dpt = [10**10]* n 
        dpc = [-1]* n 
        q  =deque([(source,0,power)])
        while q:
            a,ct,cp = q.popleft()
            if dpt[a] >ct or dpc[a] <cp:
                if dpt[a]>ct:
                    dpt[a] = ct 
                if dpc[a] < cp:
                    dpc[a] = cp 
                if cp >=cost[a]:
                    for b,c in g[a]:
                        q.append((b,ct+c,cp- cost[a]))
        ct = dpt[target] if dpt[target]<10**10 else -1 
        return [ct,dpc[target]]



edgs = [[8,1,27],[1,0,10],[9,2,22],[0,8,28],[6,7,97],[9,3,36],[3,7,33],[8,7,35],[5,3,79],[9,7,62],[1,2,17],[6,4,48],[4,1,32],[1,2,73],[2,4,12],[6,1,41],[6,0,92],[0,1,48],[5,2,39],[5,9,47],[2,6,26],[6,7,100],[8,3,63],[9,5,43],[1,7,34],[4,0,61],[2,9,36],[4,4,57],[6,1,49],[2,6,79],[1,2,100],[1,1,18],[9,4,67],[9,5,54],[4,1,98],[7,5,23],[9,5,12],[5,5,13],[6,9,48],[8,7,29],[9,4,61],[7,4,80],[4,2,37],[7,8,70],[7,2,95],[0,1,11],[0,9,74],[3,0,16],[4,3,22],[1,0,97],[5,5,98],[6,9,24],[6,4,79],[2,2,72],[0,8,43],[2,5,57],[8,7,69],[3,1,29],[8,2,97],[0,9,97],[3,7,38],[6,8,50],[7,4,75],[6,9,13],[1,1,51],[1,6,29],[0,9,67],[3,2,76],[1,9,32],[2,3,85],[6,4,45],[8,6,44],[9,4,70]]
cost = [3,6,66,2,9,6,20,6,15,9]
re =Solution().minTimeMaxPower(10,edgs,58,cost,8,0)
print(re)
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
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        g = [[] for _ in range(n)]
        mx = 0
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
            mx = max(mx,c)
        def check(mid):
            dist = [10**10]*n 
            dist[source] = 0 
            dq = deque([source])

            while dq:
                a = dq.popleft()

                if a == target:
                    return dist[a] <= k 
                for b,c in g[a]:
                    cost = 1 if c >mid else 0 
                    if dist[a] + cost < dist[b]:
                        dist[b] = dist[a] + cost 
                        if cost ==0:
                            dq.appendleft(b)
                        else:
                            dq.append(b)
            return dist[target] <= k 
        ans =-1 
        l,r = 0,mx
        if not check(mx):
            return -1 
        while l <=r:
            mid = (l+r)>>1
            if check(mid):
                ans = mid
                r = mid -1
            else:
                l = mid +1
        return ans




re =Solution()
print(re)
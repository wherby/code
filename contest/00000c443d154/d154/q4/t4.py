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
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n+1)]
        dic = defaultdict(int)
        for a,b,c in edges:
            g[a].append(b)
            g[b].append(a)
            dic[(a,b)] =c 
            dic[(b,a)] =c 
        n1 = n+1
        up = [[0]*n1 for _ in range(20)]
        sum_up = [[0]*n1 for _ in range(20)]
        depth = [0]*n1 
        parent = [0]*n1 
        dist = [0]*n1 
        q = deque([1])
        parent[1] = 1 
        while q :
            a = q.popleft()
            for b in g[a]:
                if b != parent[a]:
                    parent[b] =a 
                    dist[b] = dist[a] + dic[(a,b)]
                    depth[b] = depth[a] +1
                    q.append(b) 
        
        for b in range(1,n1):
            up[0][b] = parent[b]
            sum_up[0][b] =  dic[(parent[b],b)]
        
        for k in range(1,20):
            for b in range(1,n1):
                up[k][b] = up[k-1][up[k-1][b]]
                sum_up[k][b] = sum_up[k-1][b] + sum_up[k-1][up[k-1][b]]
        ans = [] 
        #print(depth)
        for query in queries:
            if query[0] ==1:
                _,a,b, c = query
                delta = c - dic[(a,b)]
                if b == parent[a]:
                    a,b = b,a 
                dic[(a,b)] = dic[(b,a)] =c
                #print(depth[b],b)
                sum_up[0][b] = c  
                for k in range(1,20):
                    sum_up[k][b] =sum_up[k-1][b] + sum_up[k-1][up[k-1][b]]
            else:
                _,a = query
                res = 0
                for k in range(19,-1,-1):
                    if depth[a] -depth[1] >= (1<<k):
                        res += sum_up[k][a]
                        a = up[k][a] 
                ans.append(res)
            print(sum_up,query)

        return ans



re =Solution().treeQueries( n = 5, edges = [[1,2,1],[2,3,2],[3,4,3],[4,5,4]], queries = [[2,5],[1,3,4,10],[2,5],[1,4,5,1],[2,5]])
print(re)
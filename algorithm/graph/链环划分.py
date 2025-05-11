
# https://leetcode.cn/contest/weekly-contest-449/problems/maximum-sum-of-edge-values-in-a-graph/description/
# 每个节点最多两条边的链环划分
from typing import List, Tuple, Optional

from collections import defaultdict,deque

import math
INF  = math.inf



class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        visited = [False] * n
        cycles = []
        paths = []

        for node in range(n):
            if not visited[node]:
                queue = [node]
                visited[node] = True
                component = []
                while queue:
                    u = queue.pop(0)
                    component.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)
                is_cycle = all(degree[u] == 2 for u in component)
                if is_cycle:
                    cycles.append(component)
                else:
                    paths.append(component)
        
        x = [0] * n
        current_value = n
        cycles = sorted(cycles, key= lambda a: len(a))
        for cycle in cycles:
            for node in cycle:
                x[node] = current_value
                current_value -= 1
        paths = sorted(paths,key = lambda a :len(a))
        start = 1 
        for path in paths:
            vist ={}
            path_sorted = sorted(path, key=lambda u: degree[u])
            #print(path_sorted,degree,path)
            seed = deque([path_sorted[0]])
            if len(path_sorted) >1:
                seed.append(path_sorted[1])
            #print(path_sorted,seed,degree,path)
            while seed:
                a = seed.popleft()
                if a not in vist:
                    x[a] =start
                    start +=1
                    vist[a] =1 
                    for b in adj[a]:
                        if b not in vist:
                            seed.append(b)
        #print(x)
        total = 0
        for u, v in edges:
            total += x[u] * x[v]
        
        return total




re =Solution().maxScore( n = 8, edges = [[4,7],[2,1]])
print(re)
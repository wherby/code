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
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
    # 构建邻接表
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # 计算度数
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        
        # 标记访问过的节点
        visited = [False] * n
        # 存储环和链
        cycles = []
        paths = []
        
        # 识别连通分量
        for node in range(n):
            if not visited[node]:
                # BFS或DFS遍历连通分量
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
                # 判断是环还是链
                is_cycle = all(degree[u] == 2 for u in component)
                if is_cycle:
                    cycles.append(component)
                else:
                    paths.append(component)
        
        # 分配数值
        x = [0] * n
        current_value = n
        # 优先分配环
        for cycle in cycles:
            for node in cycle:
                x[node] = current_value
                current_value -= 1
        # 然后分配链
        for path in paths:
            # 找到链的中心
            # 可以从度数最高的节点开始分配
            # 或者找到链的中间节点
            # 简单起见，按度数排序
            path_sorted = sorted(path, key=lambda u: -degree[u])
            for node in path_sorted:
                x[node] = current_value
                current_value -= 1
        print(x)
        # 计算边的总和
        total = 0
        for u, v in edges:
            total += x[u] * x[v]
        
        return total




re =Solution().maxScore( n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6]])
print(re)
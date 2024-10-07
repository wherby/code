# https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/solutions/2940537/fen-lei-tao-lun-zhu-xing-gou-zao-by-endl-v3x0/
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
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        g = [[] for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)

        # 每种度数选一个点
        edge_to_node = [-1]*5
        for x,e in enumerate(g):
            edge_to_node[len(e)] = x 
        
        if edge_to_node[1] != -1: ## 答案只有一列
            row = [edge_to_node[1]]
        elif edge_to_node[4] == -1: # 答案只有两列
            x = edge_to_node[2]
            for y in g[x]:
                if len(g[y]) ==2:
                    row = [x,y]
                    break
        else:
            # 答案至少有三列
            # 寻找度数为 2333...32 的序列作为第一排
            x = edge_to_node[2]
            row = [x]
            pre = x 
            x = g[x][0]
            while len(g[x]) ==3:
                row.append(x)
                for y in g[x]:
                    if y != pre and len(g[y]) <4:
                        pre = x 
                        x = y 
                        break
            row.append(x) # x 的度数是 2
        
        ans = [[] for _ in range(n//len(row))]
        ans[0] = row 
        visit = [False] *n 
        for x in row:
            visit[x] = True 
        for i in range(1,len(ans)):
            for x in ans[i-1]:
                for y in g[x]:
                    if not visit[y]:
                        visit[y] = True
                        ans[i].append(y)
                        break
        return ans


re =Solution().constructGridLayout(n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]])
print(re)
        

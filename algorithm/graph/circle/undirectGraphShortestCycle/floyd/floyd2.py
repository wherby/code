from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

            
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        maxn= n
        val = [[10**10 for i in range(maxn + 1)] for j in range(maxn + 1)] # 原图的邻接矩阵

        for i in range(n):
            val[i][i] =0
        for a,b in edges:
            val[a][b] =1
            val[b][a] =1

        
        def floyd(n):
            dis = [[10**10]*(n+1) for _ in range(n+1)]
            for i in range(n):
                for j in range(n):
                    dis[i][j] = val[i][j]
            print(dis)
            ans = 10**10
            for k in range(n ):
                for i in range( k):
                    for j in range(i):
                        ans = min(ans, dis[i][j] + val[i][k] + val[k][j]) # 更新答案
                        
                for i in range(n): 
                    for j in range(n):
                        dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]) # 正常的 floyd 更新最短路矩阵
            return ans
        floyd(n)
        ans = floyd(n) if floyd(n)<=n else -1
        return ans
        
        





#re =Solution().findShortestCycle(n = 4, edges = [[0,1],[0,2]])
#re =Solution().findShortestCycle(3,[[0,1],[2,0],[1,2]])
#re =Solution().findShortestCycle(6,[[4,1],[5,1],[3,2],[5,0],[4,0],[3,0],[2,1]])
re =Solution().findShortestCycle(5,[[2,4],[0,1],[3,2],[4,0],[1,3]])
print(re)
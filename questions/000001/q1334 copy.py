from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[10**19]*n for _ in range(n)]
        for a,b,c in edges:
            d[a][b] = c 
            d[b][a] = c
        for i in range(n):
            d[i][i] =0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        ret = -1
        mx = n+2 
        for i in range(n):
            acc = 0
            for j in range(n):
                if d[i][j] <= distanceThreshold:
                    acc +=1
            if acc <= mx:
                mx = acc 
                ret = i 
        return ret 

re =Solution().findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]],20)
print(re)
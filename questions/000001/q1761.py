# OT
from typing import List, Tuple, Optional

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n+1)]
        dic = {}
        for a,b in edges:
            if a > b:
                a,b = b,a 
            g[a].append(b)
            g[b].append(a)
            dic[(a,b)] = 1
        mx = 10**9 
        for a in range(1,n+1):
            if len(g[a])>=2:
                m = len(g[a])
                for i in range(m):
                    for j in range(i):
                        b,c = g[a][i],g[a][j]
                        if b >c:
                            b,c = c,b 
                        if (b,c) in dic:
                            d = len(g[a]) + len(g[b]) + len(g[c]) -6
                            mx = min(mx,d)
        return mx if mx != 10**9 else -1

re = Solution().minTrioDegree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]])
print(re)

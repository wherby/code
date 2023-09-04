from typing import List, Tuple, Optional

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = [set() for _ in range(n+1)]
        ind= [0]*(n+1)
        for a,b in edges:
            if a > b:
                a,b = b,a 
            g[a].add(b)
            g[b].add(a)
            ind[a] +=1
            ind[b] +=1
        mx = 10**9 
        for a,b in edges:
            cs = g[a] & g[b]
            for c in cs:
                d =ind[a] + ind[b] +ind[c] -6
                mx = min(mx,d) 

        return mx if mx != 10**9 else -1

re = Solution().minTrioDegree(n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]])
print(re)

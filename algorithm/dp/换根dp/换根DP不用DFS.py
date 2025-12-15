# https://leetcode.com/contest/weekly-contest-479/ranking/1/?region=global_v2
# im0505
from typing import List, Tuple, Optional


class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        dp = [1 if x else -1 for x in good]
        par = [-1] * n
        order = [0]
        
        idx = 0
        while idx < len(order):
            u = order[idx]
            idx += 1
            for v in adj[u]:
                if v != par[u]:
                    par[v] = u
                    order.append(v)
                    
        for i in range(n - 1, 0, -1):
            u = order[i]
            if dp[u] > 0:
                dp[par[u]] += dp[u]
                
        res = [0] * n
        res[0] = dp[0]
        
        for i in range(1, n):
            u = order[i]
            up = res[par[u]]
            if dp[u] > 0:
                up -= dp[u]
            res[u] = dp[u] + (up if up > 0 else 0)
            
        return res

re =Solution().maxSubgraphScore(n = 5, edges = [[1,0],[1,2],[1,3],[3,4]], good = [0,1,0,1,1])
print(re)
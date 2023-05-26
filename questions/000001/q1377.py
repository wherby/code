# https://leetcode.cn/problems/frog-position-after-t-seconds/
from typing import List, Tuple, Optional

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n+1)]
        g[1] = [0]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ans =0
        def dfs(node,par,left,prod):
            nonlocal ans
            if (node == target and left ==0) or (node == target and len(g[node]) ==1):
                ans =  1 /prod
                return True
            if left == 0 :
                return False
            for a in g[node]:
                if a == par:continue
                dfs(a,node,left-1,prod*(len(g[node])-1))
        dfs(1,0,t,1)
        return ans
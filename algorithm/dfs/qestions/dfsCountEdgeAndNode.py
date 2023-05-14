# https://leetcode.cn/problems/count-the-number-of-complete-components/submissions/

from typing import List, Tuple, Optional



class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visit={}
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(a):
            nonlocal e,v
            if a not in visit:
                visit[a] =1
                v +=1
                e += len(g[a])
            for b in g[a]:
                if b not in visit:
                    dfs(b)
        cnt = 0
        for i in range(n):
            e,v =0,0
            if i not in visit:
                dfs(i)
                if v*(v-1)//2 == e//2:
                    cnt +=1
        return cnt 
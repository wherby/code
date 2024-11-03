# https://leetcode.cn/problems/redundant-connection-ii/?envType=daily-question&envId=2024-10-28
# https://leetcode.cn/problems/redundant-connection-ii/solutions/2967953/fen-liang-chong-qing-kuang-tao-lun-by-lu-pstm/?envType=daily-question&envId=2024-10-28
from typing import List, Tuple, Optional

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        g = [[] for _ in range(n)]
        ind = [0]*n
        for a,b in edges:
            g[a-1].append(b-1)
            ind[b-1] +=1
        rt = -1 
        rt2 = -1
        for i in range(n):
            if ind[i] ==2:
                rt = i
            if ind[i] ==0:
                rt2 = i 
        if rt != -1:
            cands = []
            
            for a,b in edges:
                if b-1 == rt:
                    cands.append((a-1,b-1))
            x2,y2 = cands[1]
            g[x2].remove(y2)
            
            def dfs(i):
                ret = 1
                for a in g[i]:
                    ret += dfs(a)
                return ret
            if dfs(rt2) == n :
                return [x2+1,y2+1]
            else:
                x1,y1 = cands[0]
                return [x1+1,y1+1]


        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        p = list(range(len(edges)))

        for a,b in edges:
            pa,pb =find(a-1),find(b-1)
            if pa == pb:
                return [a,b]
            p[pa] = pb


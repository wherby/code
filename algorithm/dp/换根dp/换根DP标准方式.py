# Down: 记录第一次遍历的时候，该点的子树值，和children值
# Up： 计算当前点和它子节点换根的时候，从 当前点 到子节点 b 的这部分数能给b带来的上部分价值  up[a] + good[a] + (children[a] - max(0,down[b]))

from typing import List, Tuple, Optional

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g= [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        res = [-1]*n
        good = [1 if a >0 else -1 for a in good]
        down = [0]*n 
        up = [0]*n
        children= [0]*n
        def dfs(a,p):
            cur =0
            for b in g[a]:
                if b ==p:continue
                dfs(b,a)
                if down[b] > 0:
                    cur += down[b]
            children[a] = cur 
            down[a] = cur+good[a]
            
        
        dfs(0,-1)
        def dfs2(a,p):
            res[a] = down[a] + max(0,up[a])

            for b in g[a]:
                if b == p : continue
                FromUp = up[a] + good[a] + (children[a] - max(0,down[b]))
                up[b] = max(0,FromUp)
                dfs2(b,a)
        dfs2(0,-1)
        return res
re =Solution().maxSubgraphScore(n = 5, edges = [[1,0],[1,2],[1,3],[3,4]], good = [0,1,0,1,1])
print(re)
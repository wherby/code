# https://leetcode.cn/problems/time-taken-to-mark-all-nodes/solutions/2868276/di-er-lei-huan-gen-dppythonjavacgo-by-en-411w/
from typing import List, Tuple, Optional


class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(len(edges) + 1)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        
        node=[None] * len(g)
        # 计算 最大值max_d 和对于的节点和 第二大值
        def dfs(x, fa):
            max_d=max_d2=my = 0 
            for y in g[x]:
                if y ==fa:continue
                depth = dfs(y,x) + 2 - y %2 
                if depth > max_d:
                    max_d2 = max_d
                    max_d = depth
                    my = y 
                elif depth > max_d2:
                    max_d2 = depth
            node[x] = (max_d,max_d2,my)
            return max_d
        dfs(0,-1)
        ans = [0]* len(g)
        

        # 换根
        def reroot(x,fa, from_up):
            max_d,max_d2,my = node[x]
            ans[x] = max(from_up,max_d)
            w = 2 - x%2 
            for y in g[x]:
                if y ==fa: continue
                reroot(y,x, max(from_up, max_d2 if y == my else max_d) + w)
        reroot(0,-1,0)
        return ans

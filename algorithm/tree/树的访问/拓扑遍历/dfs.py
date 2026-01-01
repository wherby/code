# https://leetcode.cn/problems/total-sum-of-interaction-cost-in-tree-groups/description/
#  使用dfs,计算路径贡献，累积子节点的值
from typing import List, Tuple, Optional

from collections import defaultdict,deque




class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        g =[[] for _ in range(n)]
        ind = [0]*n
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            ind[a] += 1
            ind[b] +=1
        gp = defaultdict(int)
        for i,a in enumerate(group):
            gp[a]+=1
        ret = 0
        def dfs(a,pa):
            nonlocal ret 
            dic1 = defaultdict(int)
            dic1[group[a]] +=1
            for b in g[a]:
                if b ==pa:continue
                dic2 =dfs(b,a)
                for i,c in dic2.items():
                    ret += c*(gp[i]-c )
                    dic1[i] +=c 
            return dic1 
        dfs(0,-1)
        return ret 
        
            





re =Solution().interactionCosts(n = 4, edges = [[0,3],[1,2],[0,1]], group = [1,4,4,4])
print(re)
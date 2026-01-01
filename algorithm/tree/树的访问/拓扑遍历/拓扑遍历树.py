# https://leetcode.cn/problems/total-sum-of-interaction-cost-in-tree-groups/description/
# 也可以使用dfs,计算路径贡献，累积子节点的值 algorithm/tree/树的访问/拓扑遍历/dfs.py
# 其实DFS遍历也是树的拓扑排序
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
        gp = defaultdict(list)
        for i,a in enumerate(group):
            gp[a].append(i)

        def visitTree(ind,k):
            c1 = len(gp[k])
            vs = [int(a ==k) for a in group]
            cand = [] 
            visit = {}
            acc = 0
            for i in range(n):
                if ind[i] ==1:
                    cand.append(i)
                    
            for a in cand:
                visit[a] =1
                for b in g[a]:
                    if b not in visit:
                        ind[b] -=1 
                        if ind[b] ==1:
                            cand.append(b)
                        vs[b] += vs[a]
                        if vs[a]:
                            #print(c1,vs[a])
                            acc += (c1 - vs[a])*vs[a]
            return acc 
        ret = 0
        for k in gp.keys():
            ret += visitTree(list(ind),k)
        return ret 
        
            





re =Solution().interactionCosts(n = 4, edges = [[0,3],[1,2],[0,1]], group = [1,4,4,4])
print(re)
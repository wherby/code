# https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/submissions/632449142/?envType=daily-question&envId=2025-05-26

#TIPS# 有向图用拓扑遍历， 计算最大值则用枚举降维计算，这样可以用一个一维数组计算各个路径可能形成的最大值
from typing import List, Tuple, Optional

from collections import defaultdict,deque
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def verify(color):
            n = len(colors)
            ind = [0]*n 
            g = [[] for _ in range(n)]
            for a,b in edges:
                g[a].append(b)
                if a == b:
                    return [-1]*n
                # if a == b :
                #     return -1
                ind[b] +=1
            seed = deque([i for i in range(n) if ind[i] ==0])
            ls = [-1]*n 
            for i in seed:
                ls[i] = int(color ==colors[i])
            while seed:
                a = seed.popleft()
                for b in g[a]:
                    ind[b] -= 1
                    if ind[b] == 0:
                        seed.append(b)
                    t = ls[a] + int(color == colors[b])
                    if t > ls[b]:
                        ls[b] = t 
            return ls 
        cs = set(colors)
        mx = 0
        for a in cs:
            ls = verify(a)
            mx = max(mx,max(ls))
            #print(ls,a)
            if min(ls) ==-1:
                return -1
        return mx
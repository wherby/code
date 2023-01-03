# https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/
from typing import List, Tuple, Optional

from sortedcontainers import SortedDict,SortedList
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [sorted(c) for c in cuboids]
        n = len(cuboids)
        g =[[] for _ in range(n)]
        ind = [0]*n
        cuboids.sort()
        for i in range(n):
            a= cuboids[i]
            for j in range(i+1,n):
                b = cuboids[j]
                if i == j : continue
                if a[0] <= b[0] and a[1]<= b[1] and a[2]<=b[2]:
                    g[i].append(j)
                    ind[j] +=1
        start =[i for i in range(n) if ind[i]==0]

        record=[0]*n
        def dfs(a,t):
            k = t + cuboids[a][2]
            if k <= record[a]:return
            record[a] = k 
            for b in g[a]:
                dfs(b,k)
        for a in start:
            dfs(a,0)
        return max(record)
            
        
re = Solution().maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])
print(re)
            
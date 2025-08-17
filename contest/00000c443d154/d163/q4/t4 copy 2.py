from typing import List, Tuple, Optional

from collections import defaultdict,deque

import math
INF  = math.inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        dp = defaultdict(lambda : 10**40)
        dic = defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[grid[i][j]].append((i,j))
        keys= list(dic.keys())
        
        keys.sort(reverse= True)
        #print(keys)
        dp[(0,0,0)] = 0
        for k1 in range(k+1):
            for i in range(m):
                for j in range(n):
                    dp[(i,j,k1)] = min(dp[(i,j,k1)],dp[(i-1,j,k1)] + grid[i][j], dp[(i,j-1,k1)] + grid[i][j])
            if k1 > 0:
                mn = 10**30
                for ka in keys:
                    mn = min(mn, min(dp[(i,j,k1-1)] for i,j in dic[ka]))
                    for i,j in dic[ka]:
                        dp[(i,j,k1)] = mn 
                    #print(ka,mn,k1)
            for i in range(m):
                for j in range(n):
                    dp[(i,j,k1)] = min(dp[(i,j,k1)],dp[(i-1,j,k1)] + grid[i][j], dp[(i,j-1,k1)] + grid[i][j])
            #print(dp)
        return dp[(m-1,n-1,k)]



re =Solution().minCost(grid = [[3,1],[10,4]], k = 2)
print(re)
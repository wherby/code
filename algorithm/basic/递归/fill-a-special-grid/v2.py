# https://leetcode.cn/problems/fill-a-special-grid/description/
from typing import List, Tuple, Optional
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        N1= 1<<N
        cur = 0
        ret = [[-1]*N1 for _ in range(N1)]
        def dfs(n,x,y):

            if n ==0:
                nonlocal cur
                ret[x][y] = cur
                cur +=1
                return 

            t1 = 1<<(n-1)
            dfs(n-1,x,y+t1)
            dfs(n-1,x+t1,y+t1)
            dfs(n-1,x+t1,y)
            dfs(n-1,x,y)

        dfs(N,0,0)
        return ret
re =Solution().specialGrid(3)
print(re)

# https://leetcode.cn/problems/fill-a-special-grid/description/
from typing import List, Tuple, Optional
class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        N1= 1<<N
        ret = [[-1]*N1 for _ in range(N1)]
        NN = N1*N1

        def dfs(n,ls,x,y):

            if n ==0:
                ret[x][y] = ls[0]
                return 
            if n ==1:
                ret[x][y+1] = ls[0]
                ret[x+1][y+1] = ls[1]
                ret[x+1][y] =ls[2]
                ret[x][y] = ls[3]
                return
            k  = 1<<(n*2-2)
            t1 = 1<<(n-1)
            dfs(n-1,ls[:k],x,y+t1)
            dfs(n-1,ls[k:2*k],x+t1,y+t1)
            dfs(n-1,ls[k*2:k*3],x+t1,y)
            dfs(n-1,ls[k*3:k*4],x,y)
        ls= [i for i in range(NN)]
        dfs(N,ls,0,0)
        return ret
re =Solution().specialGrid(3)
print(re)

# 因为切分方向，可以不同，所以 ret =min(ret, dfs(xs,i,ys,ye,res -1) + dfs(i,xe,ys,ye,1)) 不能包含所有情况，后面的部分还有可能被切分
from typing import List, Tuple, Optional
from functools import cache

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def dfs2(x1,x2,y1,y2):
            lmn,lmx = x2,x1-1
            rmn,rmx = y2,y1-1
            for i in range(x1,x2):
                for j in range(y1,y2):
                    if grid[i][j]:
                        lmn = min(lmn, i)
                        lmx=max(lmx, i)
                        rmn = min(rmn, j)
                        rmx= max(rmx, j)
            if lmn > lmx :
                return 0 
            return (lmx-lmn+1) * (rmx-rmn +1)
        @cache
        def dfs(xs,xe,ys,ye,res):
            if res ==1:
                return dfs2(xs,xe,ys,ye)
            ret = 10**20
            for i in range(xs+1,xe):
                ret =min(ret, dfs(xs,i,ys,ye,res -1) + dfs(i,xe,ys,ye,1))
                ret =min(ret, dfs(xs,i,ys,ye,1) + dfs(i,xe,ys,ye,res-1))
                #print((xs,xe),i,xe,ys,ye,dfs(i,xe,ys,ye,1))
            for i in range(ys+1,ye):
                ret = min(ret,dfs(xs,xe,ys,i,res-1) + dfs(xs,xe,i,ye,1))
                ret = min(ret,dfs(xs,xe,ys,i,1) + dfs(xs,xe,i,ye,res-1))
                #print(xs,xe,i,ye,i,dfs(xs,xe,i,ye,1),ys,ye)
            return ret 
        m,n = len(grid),len(grid[0])
        return dfs(0,m,0,n,3)


re = Solution().minimumSum([[0,0,0],[0,0,1],[0,0,0],[1,0,1]])
print(re)
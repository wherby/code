from functools import cache
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])

        @cache
        def dfs(state,x,y):
            #print(state,x,y)
            if state == (1<<(m*n)) -1 and abs(x-endx) + abs(y-endy) ==1:
                return 1 
            ret = 0 
            for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0<=a<m and 0<=b<n and state&(1<<(a*n+b))==0:
                    ret += dfs(state + (1<<(a*n+b)),a,b)
            return ret
        sx,sy = 0 ,0,
        edx,endy =0,0
        state = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx,sy = i,j 
                if grid[i][j] !=0:
                    state += 1<<(i*n+j)
                if grid[i][j] ==2:
                    endx,endy = i,j
        return dfs(state,sx,sy)

re = Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
print(re)
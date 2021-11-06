class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m = len(grid)
        n = len(grid[0])
        trans =[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if j ==0:
                    if grid[i][j] == 1  and grid[i][j+1] ==1:
                        trans[i][j] =1
                elif j == n-1:
                    if grid[i][j] ==-1  and grid[i][j-1] ==-1:
                        trans[i][j] =-1
                else:
                    if grid[i][j] == 1 and grid[i][j+1] ==1:
                        trans[i][j] =1
                    if grid[i][j] == -1 and grid[i][j-1] ==-1:
                        trans[i][j] =-1
        res = [-1] *n
        for i in range(n):
            next =i
            lev = 0
            while lev<m and trans[lev][next] != 0 :
                next += trans[lev][next]
                lev +=1
            if lev  == m:
                res[i] = next
        return res

re= Solution().findBall(grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])
print(re)
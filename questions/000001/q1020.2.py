class Solution:
    def numEnclaves(self, grid) -> int:
        m,n = len(grid),len(grid[0])
        newG = [[1]*(n+2) for _ in range(m+2)]
        for i in range(m):
            for j in range(n):
                newG[i+1][j+1] = grid[i][j]
        visited = [[0]*(n+2) for _ in range(m+2)]
        def dfs(x,y):
            if x >=0 and x<m+2 and y >=0 and y <n+2 and visited[x][y] ==0 and newG[x][y] ==1:
                newG[x][y] =0
                for d in dirs:
                    dfs(x + d[0],y + d[1])
        dirs=[[-1,0],[1,0],[0,-1],[0,1]]
        dfs(0,0)
        cnt = sum([sum(i) for i in newG])
        return cnt 
re  = Solution().numEnclaves(grid =  [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print(re)        
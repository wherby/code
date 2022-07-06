from collections import defaultdict,deque
class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        g = [[] for _ in range(m*n)]
        dirs =[[0,1],[1,0], [0,-1],[-1,0]]
        ind =[0]*(m*n)
        dp = [1]*(m*n)
        mod = 10**9+7
        for i in range(m):
            for j in range(n):
                for dx,dy in dirs:
                    nx,ny = i+dx,j+dy
                    #print(0,0,i,j,nx,ny)
                    if 0<=dx+i < m and 0<= dy+j <n and grid[nx][ny] > grid[i][j]:
                       # print(i,j,nx,ny)
                        g[i*n +j].append(nx*n+ny)
                        ind[nx*n+ny] +=1
        dq = deque([])
        for i in range(m*n):
            if ind[i] == 0:
                dq.append(i)
        while dq:
            k = dq.popleft()
            for x in g[k]:
                dp[x] += dp[k]
                dp[x] %= mod
                ind[x] -=1
                if ind[x] ==0:
                    dq.append(x)

        return sum(dp) % mod
re =Solution().countPaths(grid = [[1,1],[3,4]])
print(re)
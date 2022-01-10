class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        m,n = len(grid),len(grid[0])
        left,right,up,down = [[0]*n for _ in range(m)],[[0]*n for _ in range(m)],[[0]*n for _ in range(m)],[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j>0 and grid[i][j] ==0 and grid[i][j-1]==0:
                    left[i][j] = left[i][j-1]+1
                if i>0 and grid[i][j] ==0 and grid[i-1][j] ==0:
                    up[i][j] = up[i-1][j] +1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if j < n-1 and grid[i][j] ==0 and grid[i][j+1] ==0:
                    right[i][j] = right[i][j+1] +1
                if i < m-1 and grid[i][j] ==0 and grid[i+1][j] ==0:
                    down[i][j] = down[i+1][j]+1
        #print(left,right,up,down)
        pls =[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    if left[i][j] + right[i][j] < stampWidth-1 or up[i][j] + down[i][j] < stampHeight-1:
                        return False
                if  (i ==0 or up[i][j]==0) and grid[i][j] ==0 and down[i][j] < stampHeight-1:
                    return False
                if (j ==0 or left[i][j] ==0) and grid[i][j] ==0 and right[i][j] < stampWidth-1:
                    return False
                if (i==m-1 or down[i][j] ==0) and grid[i][j] ==0 and up[i][j] < stampHeight -1:
                    return False
                if (j == n-1 or right[i][j]==0) and grid[i][j]==0 and left[i][j] < stampWidth-1:
                    return False
                if i>0 and left[i][j] ==0 and down[i][j] ==0 and grid[i][j] ==0:
                    if up[i][j]<stampHeight -1 or right[i][j] < stampWidth -1 or i- stampHeight+1 <0 or j+stampWidth-1 >=n or down[i-stampHeight+1][j+stampWidth-1] < stampHeight-1 or left[i-stampHeight+1][j+stampWidth-1] <stampWidth-1:
                        return False 
                if i<m-1 and right[i][j] ==0 and up[i][j] ==0 and grid[i][j] ==0:
                    if down[i][j]<stampHeight -1 or left[i][j] < stampWidth -1 or i+ stampHeight-1 >m-1 or j-stampWidth+1 >=n or up[i+ stampHeight-1][j-stampWidth+1] < stampHeight-1 or right[i+ stampHeight-1][j-stampWidth+1] <stampWidth-1:
                        return False 
        return True

re = Solution().possibleToStamp(grid = [[0,0,0,1,1,1],[0,0,0,1,1,1],[0,0,0,1,1,1],[1,0,0,0,1,1],[1,1,0,0,0,1],[1,1,1,0,0,0],[1,1,1,0,0,0],[1,1,1,0,0,0]], stampHeight = 3, stampWidth = 3 )
print(re)

re = Solution().possibleToStamp(grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3 )
print(re)
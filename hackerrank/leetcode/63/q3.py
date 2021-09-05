class Solution(object):
    def countCornerRectangles(self, grid):
        def isRec(x,y,r,k,n,m,grid):
            if x + r < n and y + k <m:
                if grid[x][y] ==1 and grid[x][y+k] ==1 and grid[x+r][y] ==1 and grid[x+r][y+k] ==1:
                    return True
                else:
                    return False
            else:
                return False
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        num = 0
        for i in range(n-1):
            tp = grid[i]
            yCandi = []
            for x1 in range(len(tp)):
                if tp[x1] == 1:
                    yCandi.append(x1)
            for j in yCandi:
                for k in range(1,m):
                    for r in range(1,n):
                        if isRec(i,j,r,k,n,m,grid):
                            num = num +1
        return num




grid = [[0,1,0],[1,0,1],[1,0,1],[0,1,0]]

s=Solution()
print s.countCornerRectangles(grid)
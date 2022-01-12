class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c


class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        m,n = len(grid),len(grid[0])
        presum = Presum2d(grid)
        matrix2 = [[0]*(n+2) for _ in range(m+2)]
        for i in range(m):
            for j in range(n):
                x1 = i + stampHeight -1
                y1 = j +stampWidth -1
                if x1 < m and y1 <n:
                    if presum.query(i,j,x1,y1) ==0:
                        matrix2[i][j]  +=1
        presum2 = Presum2d(matrix2)
        #print(matrix2)
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    x1 = i - stampHeight +1
                    y1 = j -stampWidth+1
                    x1 = x1 if x1 >0 else 0
                    y1 = y1 if y1 >0 else 0
                    if presum2.query(x1,y1, i,j) ==0:
                        #@print(x1,y1,i,j)
                        return False
        return True


re = Solution().possibleToStamp(grid =[[0,0,0,0],[0,0,0,0],[0,0,0,1]], stampHeight = 3, stampWidth = 3)
print(re)

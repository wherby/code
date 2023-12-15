from typing import List, Tuple, Optional

class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c
    
class Solution:
    def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
        m,n = len(grid),len(grid[0])
        presum  =Presum2d(grid)
        visit = {}
        def isGood(x,y,x2,y2):
            if x <0 or y < 0 or x >= m or y >=n:
                return False
            if x2 <0 or y2<0 or x2 >= m or y2 >=n:
                return False
            return presum.query(x,y,x2,y2) ==0
        matrix2 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isGood(i,j,i+h-1,j+w-1):
                    matrix2[i][j] = 1 
        presum2 = Presum2d(matrix2)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if presum2.query(max(0,i-h+1),max(0,j-w+1),i,j) ==0:
                        return False
        #print(visit,presum.pre)
        return True



re = Solution().possibleToStamp([[0,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0]], 2,  3)
print(re)



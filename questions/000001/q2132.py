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
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in visit:
                    if isGood(i,j,i+h-1,j+w-1):
                        for i1 in range(h):
                            for j1 in range(w):
                                visit[(i+i1,j+j1)] = 1 
                    if isGood(i-h+1,j,i,j+w -1):
                        for i1 in range(h):
                            for j1 in range(w):
                                visit[(i-h+1+i1,j+j1)] = 1 
                    if isGood(i-h+1,j-w+1,i,j):
                        for i1 in range(h):
                            for j1 in range(w):
                                visit[(i-h+1+i1,j-w+1+j1)] = 1 
                    if isGood(i,j-w+1,i+h-1,j):
                        for i1 in range(h):
                            for j1 in range(w):
                                visit[(i+i1,j-w+1+j1)] = 1 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in visit:
                    print(visit,presum.pre,i,j)
                    return False
        #print(visit,presum.pre)
        return True



re = Solution().possibleToStamp([[0,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0]], 2,  3)
print(re)



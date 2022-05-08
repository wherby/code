# https://leetcode-cn.com/problems/construct-quad-tree/
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
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
class Solution(object):
    def construct(self, grid):
        p2d = Presum2d(grid)
        def dfs(x,y,xn,yn):
            tmp =p2d.query(x,y,xn-1,yn-1)
            if  tmp== (xn-x)*(yn-y) or tmp ==0 :
                return Node(grid[x][y] ==1,True)
            else:
                hx,hy = (x+xn)//2,(y+yn)//2
                return Node(0,False,
                            dfs(x,y,hx,hy),
                            dfs(x,hy,hx,yn),
                            dfs(hx,y,xn,hy),
                            dfs(hx,hy,xn,yn))
        return dfs(0,0,len(grid),len(grid))
        
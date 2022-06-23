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

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def dfs(x,y,xn,yn):
            if all(grid[i][j] == grid[x][y] for i in range(x,xn) for j in range(y,yn)):
                return Node(grid[x][y] ==1,True)
            else:
                hx,hy = (x+xn)//2,(y+yn)//2
                return Node(0,False,
                            dfs(x,y,hx,hy),
                            dfs(x,hy,hx,yn),
                            dfs(hx,y,xn,hy),
                            dfs(hx,hy,xn,yn))
        return dfs(0,0,len(grid),len(grid))
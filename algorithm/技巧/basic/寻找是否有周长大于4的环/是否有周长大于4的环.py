# https://leetcode.cn/problems/detect-cycles-in-2d-grid/solutions/3952785/wang-ge-tu-dfspythonjavacgo-by-endlessch-dbxw/
# 寻找是否有大于4 的环，如果回到已经访问过的节点，并且次节点不是前两步的话，就是有环
from typing import List, Tuple, Optional


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        vis ={}
        m,n = len(grid),len(grid[0])

        def dfs(x,y,fx,fy):
            vis[(x,y)] = 1
            for dx,dy in (x,y-1),(x,y+1),(x+1,y),(x-1,y):
                if  (dx != fx or dy !=fy) and  0<=dx<m and 0<=dy<n and grid[dx][dy] == grid[x][y] and ((dx,dy) in vis or dfs(dx,dy,x,y)):
                    return True
            return False 
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis and dfs(i,j,-1,-1):
                    return True
        return False 
# https://leetcode.cn/problems/number-of-closed-islands/

from collections import defaultdict,deque

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        cnt =0
        def bfs(x,y,c):
            cand =deque([(x,y)])
            isG = True
            while cand:
                x,y = cand.popleft()
                if x == 0 or y ==0 or x == m-1 or y ==n-1:
                    isG =False
                grid[x][y] =c
                for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0<=a<m and 0<=b<n and grid[a][b] ==0:
                        cand.append((a,b))
            return isG 
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==0:
                    isG = bfs(i,j,1)
                    if isG:
                        cnt +=1
        return cnt
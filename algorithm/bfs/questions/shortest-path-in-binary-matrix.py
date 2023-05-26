# https://leetcode.cn/problems/shortest-path-in-binary-matrix/
from typing import List, Tuple, Optional

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        st = [(0,0)]
        n,m = len(grid),len(grid[0])
        step = 1 
        visit = {}
        if grid[0][0] !=0:
            return -1
        visit[(0,0)]=1
        while st:
            tmp=[]
            for x,y in st:
                if x == n-1 and y==n-1:
                    return step
                for nx,ny in (x,y+1),(x,y-1),(x -1,y-1),(x-1,y),(x-1,y+1),(x+1,y-1),(x+1,y),(x+1,y+1):
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visit and grid[nx][ny] ==0:
                        visit[(nx,ny)] =1
                        tmp.append((nx,ny))
            st = tmp
            step +=1
        return -1
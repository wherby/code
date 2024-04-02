from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        cand =[(0,0,1)]
        visit ={}
        sl1=[SortedList([i for i in range(n)]) for _ in range(m)]
        sl2=[SortedList([i for i in range(m)]) for _ in range(n)]
        while cand:
            tmp = []
            for x,y,c in cand:
                if x== m-1 and y == n-1:
                    return c
                if (x,y) in visit: continue
                visit[(x,y)] =1
                left = sl1[x].bisect_left(y+1)
                idx = sl1[x].bisect_right(grid[x][y] +y)
                for i in range(left,idx):
                    tmp.append((x,sl1[x][i],c+1))
                del sl1[x][left:idx]
                left = sl2[y].bisect_left(x+1)
                idx = sl2[y].bisect_right(grid[x][y] + x)
                for i in range(left,idx):
                    tmp.append((sl2[y][i],y,c+1))
                del sl2[y][left:idx]  
            cand = tmp
        return -1


re =Solution().minimumVisitedCells(grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]])
print(re)
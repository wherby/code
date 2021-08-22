
from collections import deque
class Solution:
    def latestDayToCross(self, row, col, cells) :
        DIR =[0,1,0,-1,0]

        def canWalkFromTopToButtom(dayAt):
            #print(dayAt)
            grid = [[0]* col for _ in range(row)]
            for i in range(dayAt):
                r,c = cells[i]
                #print(r,c,cells,grid)
                grid[r-1][c-1] = 1
            
            bfs = deque([])

            for c  in range(col):
                if grid[0][c] == 0:
                    bfs.append((0,c))
                    grid[0][c] =1
            
            while bfs:
                r,c = bfs.popleft()
                if r == row -1:
                    return True
                for i in range(4):
                    nr,nc = r+DIR[i],c + DIR[i+1]
                    if nr<0 or nr ==row or nc <0 or nc == col or grid[nr][nc] ==1:
                        continue
                    grid[nr][nc] =1
                    bfs.append((nr,nc))
            return False

        left,right = 1,len(cells)
        ans =0
        while left <= right:
            mid =(left + right) //2
            if canWalkFromTopToButtom(mid):
                ans = mid 
                left = mid +1
            else:
                right = mid -1
        return ans






row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]
r=Solution().latestDayToCross(row,col,cells)
print(r)
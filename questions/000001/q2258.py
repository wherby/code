from typing import List, Tuple, Optional

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        lvs = [[10**10]*n for _ in  range(m)]
        cand = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cand.append((i,j))
        turn= 0 
        while cand:
            tmp = []
            for i,j in cand:
                lvs[i][j] = turn
                for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                    nx,ny = i+dx,j +dy 
                    if 0<=nx<m and 0<= ny <n and grid[nx][ny] != 2 and lvs[nx][ny] > turn +1 :
                        lvs[nx][ny] = turn +1
                        tmp.append((nx,ny))
            turn +=1
            cand = tmp
        l,r = -1,10**9 
        def verify(start):
            dp = [[10**10]*n for _ in range(m)]
            cand = [(0,0)]
            turn = start
            while cand:
                tmp = []
                for x,y in cand:
                    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                        nx,ny = x+dx,y +dy 
                        if 0<=nx<m and 0<= ny <n and grid[nx][ny] != 2 and dp[nx][ny] > turn +1 and turn +1 < lvs[nx][ny] :
                            dp[nx][ny] = turn +1
                            tmp.append((nx,ny))
                        if nx==m-1 and  ny ==n-1 and grid[nx][ny] != 2 and dp[nx][ny] > turn +1 and turn +1 <= lvs[nx][ny]  :
                            dp[nx][ny] = turn +1
                            tmp.append((nx,ny))
                turn +=1
                cand = tmp
            return dp[m-1][n-1] < 10**10
        while l< r:
            mid = (l+r+1)>>1
            if verify(mid):
                l = mid 
            else:
                r = mid -1 
        return l 

re = Solution().maximumMinutes(grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]])
print(re)
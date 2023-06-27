
from typing import List, Tuple, Optional

class Solution:
    def flipChess(self, cs: List[str]) -> int:
        dirs = [(i,j) for i in range(-1,2) for j in range(-1,2) if not( i== 0 and j==0)]
        m,n = len(cs), len(cs[0])
        mx = 0
        def bfs(cs,i,j):
            #print(cs,i,j)
            acc =0
            cand =[(i,j)]
            while cand:
                i,j = cand.pop(0)
                x,y = i,j
                for dx,dy in dirs:
                    nx,ny = x + dx,y+dy 
                    cnt = 0  
                    while 0<= nx<m and 0<= ny < n and cs[nx][ny] =="O":
                        cnt +=1
                        nx,ny = nx+dx,ny+dy 
                    if 0<= nx<m and 0<= ny <n and cs[nx][ny] == "X":
                        acc += cnt
                        for k in range(1,cnt+1):
                            cs[i+k*dx][j+k*dy] = "X"
                            cand.append((i+k*dx,j+k*dy))
                    #print(cs,i,j,dx,dy,cnt,cs[dx][dy],acc,dx,dy)
                #print(i,j,cand,cs,acc)
            return acc
        
        for i in range(m):
            for j in range(n):
                if cs[i][j]  != ".": continue
                cs2= [list(cs[i]) for i in range(m)]
                cs2[i][j] = "X"
                mx = max(mx, bfs(cs2,i,j))
        return mx
                
re = Solution().flipChess([".X.",".O.","XO."])       
print(re)
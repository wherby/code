from typing import List, Tuple, Optional
class Solution:
    def pacificAtlantic(self, hs: List[List[int]]) -> List[List[int]]:
        m,n = len(hs),len(hs[0])
        def visit(h):
            
            s=set([])
            cand = []
            for i in range(m):
                cand.append((i,0))
                s.add((i,0))
            for i in range(n):
                if (0,i) not in s:
                    cand.append((0,i))
                    s.add((0,i))
            for x,y in cand:
                for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in s and h[nx][ny] >= h[x][y]:
                        s.add((nx,ny))
                        cand.append((nx,ny))
            return s 
        s = visit(hs)
        hs2 = [a[::-1] for a in hs[::-1]]
        s2 = visit(hs2)
        s3 = set((m-1-a,n-1-b) for (a,b) in s2)
       # print(s,s3,s2)
        return list(s & s3)

re =Solution().pacificAtlantic(hs = [[2,1],[1,2]])
print(re)
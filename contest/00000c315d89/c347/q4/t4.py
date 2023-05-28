from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        cols = [SortedList([]) for _ in range(m)]
        rows = [SortedList([]) for _ in range(n)]
        for i in range(m):
            for j in range(n):
                cols[i].add((mat[i][j],i,j))
                rows[j].add((mat[i][j],i,j))
        #print(cols,rows)
        @cache
        def visit(x,y):
            #print(x,y,mat[x][y],cols[x])
            mx = 1
            col = cols[x]
            kidx = col.bisect_left((mat[x][y]+1,0,0))
            row = rows[y]
            k2idx = row.bisect_left((mat[x][y]+1,0,0))
            #print(k2idx,x,y)
            for i1  in range(kidx,min(kidx+1,n)):
                _,_,i = col[i1]
                #print(col[i1],i1)
                mx = max(mx,1+ visit(x,i))
            for j2 in range(k2idx,min(k2idx+1,m)):
                _,j,_ = row[j2]
                #print(row[j2],j)
                mx = max(mx,1+visit(j,y))
            
            return mx
        mx = 0 
        ls=[]
        for i in range(m):
            for j in range(n):
                ls.append((mat[i][j],i,j))
        ls.sort(reverse= True)
        for _,i,j in ls:
            mx = max(mx,visit(i,j))
        return mx





re =Solution().maxIncreasingCells(mat = [[3,1,6],[-9,5,7]])
print(re)
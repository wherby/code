from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        mn = 10**8
        m,n = len(grid),len(grid[0])
        st = deque([(0,0,1)])
        visit = {}
        #print(m,n)
        while st:
            x,y,cs = st.popleft()
            #print(x,y,cs)
            if x == m-1 and y == n-1:
                return cs
            if (x,y) in visit: continue
            visit[(x,y)] =1
            mx =0
            for i in range(min(n-1,grid[x][y]+y+1),y,-1):
                if (x,i) not in visit:
                    acc = grid[x][i] + i
                    if acc > mx:
                        mx = acc
                        st.append((x,i,cs+1))
            mx =0
            for i in range(min(m-1,grid[x][y]+x+1),x,-1):
                if (i,y) not in visit:
                    acc =grid[i][y] +i 
                    if acc > mx:
                        mx = acc
                        st.append((i,y,cs+1))
        return  -1
        





re =Solution().minimumVisitedCells(grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]])
print(re)
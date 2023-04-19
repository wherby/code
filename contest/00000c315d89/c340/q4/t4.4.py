# ## sortedlist delete optimization
# https://leetcode.cn/contest/weekly-contest-340/problems/minimum-number-of-visited-cells-in-a-grid/
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
        sl1 =[SortedList([i for i in range(n)]) for _ in range(m)]
        sl2 = [SortedList([i for i in range(m)]) for _ in range(n)]
        #print(m,n)
        while st:
            x,y,cs = st.popleft()
            #\print(x,y,cs)
            if x == m-1 and y == n-1:
                return cs
            if (x,y) in visit: continue
            visit[(x,y)] =1
            left = sl1[x].bisect_left(y+1)
            idx = sl1[x].bisect_right(grid[x][y] +y)
            # while idx< len(sl1[x]) and sl1[x][idx] <= grid[x][y] +y:
            #     st.append((x,sl1[x][idx],cs+1))
            #     idx +=1
            for i in range(left,idx):
                st.append((x,sl1[x][i],cs+1))
            del sl1[x][left:idx]
            # for i in range(min(n-1,grid[x][y]+y),y,-1):
            #     if (x,i) not in visit:
            #         st.append((x,i,cs+1))
            #     else:
            #         break
            left = sl2[y].bisect_left(x+1)
            idx = sl2[y].bisect_right(grid[x][y] + x)
            for i in range(left,idx):
                st.append((sl2[y][i],y,cs+1))
            #rm2 =[]
            #print(sl2[y])
            # while idx < len(sl2[y]) and sl2[y][idx] <= grid[x][y] + x:
            #     rm2.append(sl2[y][idx])
            #     st.append((sl2[y][idx],y,cs+1))
            #     idx +=1
            del sl2[y][left:idx]           
            # for a in rm2:
            #     sl2[y].remove(a)
            # for i in range(min(m-1,grid[x][y]+x),x,-1):
            #     if (i,y) not in visit:
            #         st.append((i,y,cs+1))
            #     else:
            #         break
        return  -1
        





re =Solution().minimumVisitedCells(grid =[[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]])
print(re)
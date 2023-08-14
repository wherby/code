from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if grid[0][0] ==1 or grid[m-1][n-1] ==1:
            return 0
        ls1 = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    ls1.append((i,j))
        dic =defaultdict(lambda:-1)
        for i in range(m):
            for j in range(n):
                tm = m+n
                for a,b in ls1:
                    tm = min(tm,abs(a-i)+ abs(b-j))
                dic[(i,j)] = tm
        l,r  =0,dic[(0,0)]
        def verify(mid):
            visit = {}
            st =[(0,0)]
            while st:
                #print(st,mid)
                x,y = st.pop()
                if x == m-1 and y == n-1:
                    return True
                if (x,y) in visit:
                    continue
                visit[(x,y)] =1
                for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if (a,b) not in visit and dic[(a,b)]>=mid:
                        st.append((a,b))
            return False
        while l <r:
            mid = (l+r+1)>>1
            if  verify(mid) :
                l= mid 
            else:
                r=mid-1
        return l


re =Solution().maximumSafenessFactor
print(re)
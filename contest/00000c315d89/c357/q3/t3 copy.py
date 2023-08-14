from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[n+n]*n for _ in range(n)]
        
        def Spread(a,b):
            st=deque([(a,b,0)])
            visit = {}
            while st:
                a,b,c = st.popleft()
                if dp[a][b] <=c: continue
                dp[a][b] = c 
                #print(dp,a,b,c)
                visit[(a,b)] =1
                for x,y in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                    if 0<=x<n and 0<=y<n and (x,y) not in visit and dp[x][y] >c+1:
                        st.append((x,y,c+1))
            
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==1:
                    Spread(i,j)
                    #print(i,j)
        #print(dp)
        l,r  =0,dp[0][0]
        #print(l,r)
        def verify(mid):
            visit = {}
            st =deque([(0,0)])
            while st:
                x,y = st.popleft()
                #print(st,mid,x,y)
                if x == n-1 and y == n-1:
                    return True
                if (x,y) in visit:
                    continue
                visit[(x,y)] =1
                for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if (a,b) not in visit and 0<=a<n and 0<=b<n and dp[a][b]>=mid:
                        st.append((a,b))
            return False
        while l <r:
            mid = (l+r+1)>>1
            #print(mid)
            #print(verify(mid))
            if  verify(mid) :
                l= mid 
            else:
                r=mid-1
        return l


re =Solution().maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]])
print(re)
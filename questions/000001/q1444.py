from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter
from functools import lru_cache
from functools import cache

class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.m,self.n = m,n
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        #print(x1,y1,x2,y2)
        if x1 >=self.m or y1>=self.n :
            return 0
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m,n  = len(pizza),len(pizza[0])
        arr = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if pizza[i][j] == "A":
                    arr[i][j] = 1 
        p2d = Presum2d(arr)
        #print(p2d.pre)
        mod = 10**9+7
        @cache
        def dfs(idx,x,y):
            if idx == k:
                if p2d.query(x,y,m-1,n-1) >0 :
                    return 1 
                else:
                    return 0
            cnt = 0
            for i in range(x+1,m):
                if p2d.query(x,y,m-1,n-1) - p2d.query(i,y,m-1,n-1)>0:
                    cnt +=dfs(idx+1,i,y)
            for j in range(y+1,n):
                if p2d.query(x,y,m-1,n-1) - p2d.query(x,j,m-1,n-1)>0:
                    cnt += dfs(idx+1, x,j)
            return cnt%mod 
        return dfs(1,0,0)

#re =Solution().ways(pizza = ["A..","AAA","..."], k = 3)
re =Solution().ways(pizza = [".A..A","A.A..","A.AA.","AAAA.","A.AA."], k = 5)
print(re)
             

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Presum2d:
    def __init__(self,arr):
        m,n = len(arr),len(arr[0])
        self.pre = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                #print(i,j,m,n)
                self.pre[i+1][j+1] = self.pre[i][j+1] + self.pre[i+1][j] -self.pre[i][j] + arr[i][j]
    
    def query(self,x1,y1,x2,y2):
        a = self.pre[x2+1][y1]
        b = self.pre[x1][y2+1]
        c = self.pre[x1][y1]
        return self.pre[x2+1][y2+1] -a -b +c
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mx = [[0]*(n+1) for _ in range(n+1)]
        for x1,y1,x2,y2 in queries:
            mx[x1][y1] +=1
            mx[x1][y2+1] -=1
            mx[x2+1][y1] -=1
            mx[x2+1][y2+1] +=1
        pmx = Presum2d(mx)
        ret =[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ret[i][j] = pmx.query(0,0,i,j)
        #print(ret)
        return ret



re =Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]])
print(re)
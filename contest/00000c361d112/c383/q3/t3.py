from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        res = [[0]*n for _ in range(m)]
        dic = defaultdict(list)
        def verify(i,j):
            isG =True
            for i1 in  i-1,i,i+1:
                if abs(image[i1][j] -image[i1][j-1])>threshold:
                    isG = False
                if abs(image[i1][j] -image[i1][j+1])>threshold:
                    isG = False
            for j1 in  j-1,j,j+1:
                if abs(image[i][j1] -image[i-1][j1])>threshold:
                    isG = False
                if abs(image[i][j1] -image[i+1][j1])>threshold:
                    isG = False
            return isG
        for i in range(1,m-1):
            for j in range(1,n-1):
                if verify(i,j):
                    sm =0
                    for i1 in  i-1,i,i+1:
                        for j1 in j-1,j,j+1:
                            sm += image[i1][j1]
                    av = sm // 9 
                    for i1 in  i-1,i,i+1:
                        for j1 in j-1,j,j+1:
                            dic[(i1,j1)].append(av)
        for i in range(m):
            for j in range(n):
                if len(dic[(i,j)]) ==0:
                    res[i][j]=image[i][j]
                else:
                    res[i][j] = sum(dic[(i,j)])//(len(dic[(i,j)]))
        return res
        





re =Solution().resultGrid([[10,20,30],[15,25,35],[20,30,40],[25,35,45]], threshold = 12)
print(re)
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
#from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

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
    def numberOfPairs(self, points: List[List[int]]) -> int:
        xls = []
        yls =[]
        for x,y in points:
            xls.append(x)
            yls.append(y)
        xls =list(set(xls))
        xls.sort()
        yls = list(set(yls))
        yls.sort()
        xdic,ydic= {},{}
        for i,a in enumerate(xls):
            xdic[a]=i
        for i,a in enumerate(yls):
            ydic[a] = i 
        #print(xdic,ydic)
        arr = [[0]*(len(yls)+1) for _ in range(len(xls)+1)]
        for x,y in points:
            xidx = xdic[x]
            yidx = ydic[y]
            arr[xidx][yidx] +=1
        pres = Presum2d(arr)
        ret = 0
        #print(arr)
        for x1,y1 in points:
            for x2,y2 in points:
                if x1 ==y1 and x2==y2: continue
                if xdic[x1] > xdic[x2]:continue
                if ydic[y1] < ydic[y2]:continue
                if pres.query(xdic[x1],ydic[y2],xdic[x2],ydic[y1]) ==2:
                    ret +=1
                #print(xdic[x1],ydic[y2],xdic[x2],ydic[y1],pres.query(xdic[x1],ydic[y2],xdic[x2],ydic[y1]))
        return ret






re =Solution().numberOfPairs(points = [[0,0],[0,3]])
print(re)
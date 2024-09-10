from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        dir = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

        def getLasted(x1,y1,x2,y2):
            visit ={}
            cnt = 0
            cand = [(x1,y1)]
            while cand:
                
                tmp =[]
                for x,y in cand:
                    if x ==x2 and y == y2:
                        return cnt 
                    if (x,y) in visit:continue
                    visit[(x,y)] =1
                    for dx,dy in dir:
                        nx,ny = x+dx,y+dy 
                        if (abs(nx-x2) > 6 and abs(nx-x2) > abs(x1-x2) ) or (abs(ny-y2)> 6 and abs(ny-y2) >abs(y1-y2)) or (nx,ny) in visit:
                            continue
                        if 0<=nx<50 and 0<=ny<50:
                            tmp.append((nx,ny))
                cnt +=1
                cand = tmp
        dic ={}
        n = len(positions)
        for i in range(n):
            for j in range(i):
                dic[(i,j)] = dic[(j,i)] = getLasted(positions[i][0],positions[i][1],positions[j][0],positions[j][1])
        
        @cache
        def dfs(state,lst,b):
            if state == (1<<n)-1:
                return 0
            if b == True:
                ret = 0
            else:
                ret = 10**10 
            for i in range(n):
                if (1<<i)&state == 0:
                    if b == True:
                        ret =max(ret, dfs(state|(1<<i),i,False) + dic[(lst,i)])
                    else:
                        ret = min(ret,dfs(state|(1<<i),i,True) + dic[(lst,i)]) 
            return ret
        
        mx = 0
        for i in range(n):
            tmp =getLasted(kx,ky,positions[i][0],positions[i][1]) + dfs(1<<i,i,False)
            mx = max(mx,tmp)
            #print(i,tmp,getLasted(kx,ky,positions[i][0],positions[i][1]),dic)
        #print(dic)
        return mx






re =Solution().maxMoves(kx = 0, ky = 0, positions = [[6,9],[2,8],[0,10]])
print(re)
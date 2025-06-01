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
    def minMoves(self, cl: List[str], energy: int) -> int:
        m,n = len(cl),len(cl[0])
        sx,sy = -1,-1
        lp = []
        for i in range(m):
            for j in range(n):
                if cl[i][j] == "S":
                    sx,sy= i,j 
                if cl[i][j] =="L":
                    lp.append((i,j))
        if len(lp) ==0:
            return 0 
        lm = len(lp)
        target = (1<<lm) -1
        dic = {}
        for idx,(i,j) in enumerate(lp):
            dic[(i,j)] = 1<<idx
        cand = deque([(sx,sy,energy,0,0)])
        visit=defaultdict(lambda:-1)
        visit[(sx,sy,0)]=energy
        while cand:
            x,y,e,state,step = cand.popleft()
            if state == target:
                return step
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if 0<=nx<m and 0<=ny<n and cl[nx][ny] !="X":
                    if e >0:
                        ne = e-1
                        nstate = state
                        if cl[nx][ny] =="L":
                            nstate |= dic[(nx,ny)]
                        if cl[nx][ny] == "R":
                            ne = energy
                        if ne > visit[(nx,ny,nstate)]:
                            visit[(nx,ny,nstate)]=ne
                            cand.append((nx,ny,ne,nstate,step+1))
        return -1




re =Solution().minMoves(["S.", "XL"], energy = 2)
print(re)
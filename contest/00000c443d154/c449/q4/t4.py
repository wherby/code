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
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        def canDo(gd):
            m,n = len(gd),len(gd[0])
            visit={}
            ls = [sum(a) for a in gd]
            sm = sum(ls)
            isn1 = n !=1
            acc = 0
            t1,t2 = False,False
            for i in range(m-1):
                for b in gd[i]:
                    visit[b] =1 
                acc += ls[i]
                if acc*2 ==sm :
                    return True
                # if i==0 :
                #     t1 = ls[0]  in gd[0][1:]
                #     t2 = ls[-1] in gd[0][:-1]
                if isn1 and (acc*2 -sm) in visit :
                    if i==0 :
                        k = (acc*2 -sm)
                        if k != gd[0][0] and k != gd[0][-1]:
                            continue
                    return True
                if not isn1:
                    k = (acc*2 -sm)
                    if k == gd[0][0] or k == gd[i][0]:
                        return True
            return False
        gr = grid[::-1]
        def reverse(g):
            return [list(a) for a in zip(*g)]
        grr = reverse(grid)
        return canDo(grid) or canDo(gr) or canDo(grr) or canDo(grr[::-1]) 




re =Solution().canPartitionGrid( [[73816],[71688]])
print(re)
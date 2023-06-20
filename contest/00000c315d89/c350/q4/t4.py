from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        mx = sum(cost)
        ls = []
        for c,t in zip(cost,time):
            ls.append((c/t,-c,t))
        ls.sort()
        left =0
        cst= 0
        tacc = 0
        for i in range(n):
            cst -= ls[i][1]
            tacc +=ls[i][2]
            #print(cst,tacc,left,i)
            while tacc + i +1 - left -1 -ls[left][2] >= n:
                tacc -= ls[left][2]
                cst += ls[left][1]
                left +=1
            if tacc +i+1-left >= n:
                mx = min(mx,cst)
        return mx
        



re =Solution().paintWalls([42,8,28,35,21,13,21,35],[2,1,1,1,2,1,1,2])
print(re)
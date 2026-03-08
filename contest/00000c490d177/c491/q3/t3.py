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
    def minimumOR(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ans = 0
        ands=0
        for i in range(m):
            tmp=(1<<32)-1
            for j in range(n):
                tmp &= grid[i][j]
            ands |= tmp
        
        for i in range(32,-1,-1):
            if ands & (1<<i):
                ans |= (1<<i)
            else:
                tts=[]
                for j in range(m):
                    tmp =[]
                    for s in grid[j]:
                        if s & (1<<i)==0:
                            tmp.append(s)
                    tts.append(tmp)
                if all(len(tts[j])>0 for j in range(m)):
                    grid=tts
                else:
                    ans |= (1<<i)
        return ans


re =Solution().minimumOR(grid = [[1,5],[2,4]])
print(re)
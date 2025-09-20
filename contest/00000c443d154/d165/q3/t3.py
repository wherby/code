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
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <=4:
            return [] 
        ret = []
        m = n //2
        ls = [[] for _ in range(4)] 
        for i in range(n):
            for j in range(n):
                if i == j:continue
                if i<m and j<m+n%2:
                    ls[0].append((i,j))
                elif i<m and j>=m+n%2:
                    ls[1].append((i,j))
                elif i >=m and j < m+n%2:
                    ls[2].append((i,j))
                else :
                    ls[3].append((i,j)) 
        cnt = 0 
        print(ls)
        ls[1] = ls[1][::-1]
        ls[3] = ls[3][::-1]
        while cnt <n*(n-1):
            if ls[0]:
                ret.append(ls[0].pop())
                cnt +=1
            
            if ls[1]:
                ret.append(ls[1].pop())
                cnt +=1
            if ls[2]:
                ret.append(ls[2].pop())
                cnt +=1
            if ls[3]:
                ret.append(ls[3].pop())
                cnt +=1
            
            
            
        return ret


re =Solution().generateSchedule(6)
print(re)
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
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        ls= [(s,i) for i,s in enumerate(skills) ]
        cur = ls[0]
        cnt = 0
        for i in range(1,n*2):
            if cur[0]> ls[i][0]:
                cnt +=1
                ls.append(ls[i])
            else:
                cnt =1 
                ls.append(cur)
                cur = ls[i]
                
            if cnt == k:
                return cur[1]
        return cur[1]





re =Solution()
print(re)
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
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9+7
        cnt = 0
        dic = defaultdict(list)
        for x,y in points:
            dic[y].append(x)
        acc = 0 
        for y in dic.keys():
            lx= len(dic[y])
            c1 = lx*(lx-1) //2 
            cnt += c1*acc 
            acc +=c1 
            #print(y,cnt,acc,c1,lx,dic[y])
        return cnt %mod





re =Solution().countTrapezoids( points = [[1,0],[2,0],[3,0],[2,2],[3,2]])
print(re)
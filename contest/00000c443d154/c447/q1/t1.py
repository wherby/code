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
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        ls1,ls2 = defaultdict(list),defaultdict(list)
        for x,y in buildings:
            ls1[x].append(y)
            ls2[y].append(x)
        cnt = 0 
        for k,v in ls1.items():
            ls1[k] = sorted(v)
        for k,v in ls2.items():
            ls2[k] = sorted(v)
        for x,y in buildings:
            if ls1[x][0] == y or ls1[x][-1] ==y or ls2[y][0] ==x or ls2[y][-1] ==x:
                continue
            cnt +=1
        return cnt




re =Solution().countCoveredBuildings( n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]])
print(re)
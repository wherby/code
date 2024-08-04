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
from collections import Counter
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        dic =defaultdict(list)
        for x,y in pick:
            dic[x].append(y)
        sm = 0
        for k,v in dic.items():
            c = Counter(v)
            #print(list(c.values()))
            for vt in c.values():
                if vt>k:
                    sm +=1
                    break
        return sm




re =Solution().winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]])
print(re)
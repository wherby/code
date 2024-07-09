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
    def validStrings(self, n: int) -> List[str]:
        ret =[]
        
        def dfs(acc):
            if len(acc) == n:
                ret.append(acc)
                return 
            
            dfs(acc+"1")
            if acc[-1] =="1":
                dfs(acc+"0")
        dfs("1")
        dfs("0")
        return ret



re =Solution().validStrings(3)
print(re)
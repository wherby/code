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
    def countDistinct(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, is_limit: bool, is_num: int,s:str) -> int:
            if i == len(s): 
                return  is_num >0
            res = 0
            if not is_num: 
                res = f(i + 1, False, 0,s)
            up = int(s[i]) if is_limit else 9  
            for d in range(1 , up +1):  
                if d > up: break 
                res += f(i + 1, is_limit and d == up, is_num+d,s)
            return res
        return f(0,True,0,s)



re =Solution().countDistinct(10)
print(re)
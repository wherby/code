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
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        keys = sorted(c.keys())
        ret = []
        odd =""
        for k in keys:
            v = c[k]
            if v%2 ==1 :
                odd = k
            ret.extend([k] *(v//2))
        rvs = ret[::-1]
        if odd != "":
            ret.append(odd)
        ret.extend(rvs)
        return "".join(ret)




re =Solution().smallestPalindrome("babab")
print(re)
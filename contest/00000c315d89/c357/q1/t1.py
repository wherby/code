from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def finalString(self, s: str) -> str:
        ret =[]
        for a in s :
            if a =="i":
                ret = ret[::-1]
            else:
                ret.append(a)
        return "".join(ret)





re =Solution()
print(re)
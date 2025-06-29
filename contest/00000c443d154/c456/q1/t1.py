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
    def partitionString(self, s: str) -> List[str]:
        ret =[]
        dic = {}
        tmp = ""
        for a in s:
            tmp += a 
            if tmp not in dic:
                ret.append(tmp)
                dic[tmp] =1 
                tmp =""
        return ret





re =Solution().partitionString("abbccccd")
print(re)
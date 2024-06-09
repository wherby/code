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
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        dic = defaultdict(int)
        mx=0
        for i,a in enumerate(s):
            dic[a] +=1
            while dic[a]>2:
                dic[s[l]] -=1
                l +=1
            mx = max(mx,i-l+1)
        return mx 





re =Solution()
print(re)
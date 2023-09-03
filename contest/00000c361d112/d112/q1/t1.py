from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        dic = {}
        dic[s1] = 1
        t2 = s1[2] + s1[1] + s1[0] + s1[3]
        t3 = s1[2] + s1[3] + s1[0] + s1[1]
        t4 = s1[0] + s1[3] + s1[2] + s1[1]
        dic[t2]=1
        dic[t3]=1
        dic[t4]=1
        return s2 in dic





re =Solution().canBeEqual(s1 = "abcd", s2 = "cdab")
print(re)
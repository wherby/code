from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        while len(s.replace("AB","").replace("CD","")) != len(s):
            s = s.replace("AB","").replace("CD","")
        return len(s)





re =Solution().minLength("ABFCACDB")
print(re)
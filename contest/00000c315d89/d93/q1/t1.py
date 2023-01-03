from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        mx = 0
        for st in strs:
            isD = all([a.isdigit() for a in st])
            if isD:
                mx = max(mx,int(st))
            else:
                mx = max(mx,len(st))
        return mx




re =Solution().maximumValue(strs = ["alic3","bob","3","4","00000"])
print(re)
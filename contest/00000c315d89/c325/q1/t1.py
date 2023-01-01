from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        fd =-1
        n = len(words)
        for i in range(n):
            if words[(startIndex +i)%n] == target or words[(startIndex-i+n)%n] == target:
                return i
        return -1





re =Solution()
print(re)
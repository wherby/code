from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num ==0:
            return True
        return num %10 !=0
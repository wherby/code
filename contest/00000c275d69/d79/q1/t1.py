from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from typing import Counter

class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        c =Counter(num)
        for i,a in enumerate(num):
            k = int(a)
            if c.get(str(i),0) != k:
                return False
        return True
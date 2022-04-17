from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def giveGem(self, gem, operations):
        """
        :type gem: List[int]
        :type operations: List[List[int]]
        :rtype: int
        """
        for a ,b in operations:
            t = gem[a] //2
            gem[a] -=t
            gem[b] +=t
        return max(gem) - min(gem)
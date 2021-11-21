from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        sm =0
        for i in range(n):
            for j in range(i,n):
                if colors[i] != colors[j]:
                    sm = max(sm,j-i)
        return sm
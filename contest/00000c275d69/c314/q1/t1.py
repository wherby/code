from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        ret=10**10
        ls = 0
        mn = 0
        for i,a in logs:
            k = a -ls 
            ls = a 
            if k == mn:
                ret = min(i,ret)
            if k > mn:
                mn = k 
                ret =i
        return ret





re =Solution()
print(re)
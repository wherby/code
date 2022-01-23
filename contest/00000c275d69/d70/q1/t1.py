from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left


class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort()
        n = len(cost)
        sm = 0
        status =0
        for i in range(n-1,-1,-1):
            status +=1
            if status %3==0: continue
            sm += cost[i]
        return sm
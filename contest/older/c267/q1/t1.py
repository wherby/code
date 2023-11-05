from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        cnt =0
        idx =0
        n =len(tickets)
        while tickets[k] != 0:
            if tickets[idx] >0:
                tickets[idx] -=1
                cnt +=1
            idx +=1
            idx =idx %n
        return cnt
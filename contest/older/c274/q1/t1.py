from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state =0
        for a in s:
            if a =="a" and state <=1:
                state =1
            else:
                if a == "a":
                    return False
                state = 2
        return True
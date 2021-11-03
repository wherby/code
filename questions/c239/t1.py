# common include
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        mn = len(nums)
        for i,j in enumerate(nums):
            if j == target:
                mn = min(mn, abs(i-start))
        return mn
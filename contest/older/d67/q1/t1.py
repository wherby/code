from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hq =[]
        for i, n in enumerate(nums):
            heapq.heappush(hq,(-n, i))
        res =[]
        while len(res)<k:
            t,idx = heapq.heappop(hq)
            res.append((idx,t))
        res.sort()
        res = list(map(lambda x : -x[1],res))

        return res

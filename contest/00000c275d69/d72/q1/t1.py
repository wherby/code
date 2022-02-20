from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sm =0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if i*j %k ==0 and nums[i] == nums[j]:
                    sm +=1
        return sm
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic ={}
        n = len(nums)
        for i in range(n-1):
            k = nums[i]+ nums[i+1]
            if k in dic:
                return True
            dic[k] =1
        return False





re =Solution()
print(re)
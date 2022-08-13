from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums)
        dic = defaultdict(int)
        cnt =0
        for i in range(1,n-1):
            for j in range(i):
                for k in range(i+1,n):
                    if nums[k]-nums[i] ==diff == nums[i] -nums[j]:
                        cnt +=1
        return cnt
         




re =Solution()
print(re)
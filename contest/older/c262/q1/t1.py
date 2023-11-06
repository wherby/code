from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        dic=defaultdict(int)
        nums =nums1+nums2 + nums3
        res =[]
        for x in nums:
            dic[x] +=1
            if dic[x] >=2:
                res.append(x)
        return list(set(res))
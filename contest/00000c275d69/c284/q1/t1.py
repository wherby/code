from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res =[]
        for i,a in enumerate(nums):
            if a == key:
                res.append(i)
        ret =set()
        mn = 0
        n = len(nums)
        for a in res:
            for i in range(-k,k+1):
                if a+i >=0 and a+i <n:
                    ret.add(a+i)
        ret = sorted(list(ret))
        return ret

re = Solution().findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1)
print(re)
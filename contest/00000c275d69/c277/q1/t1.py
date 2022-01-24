from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left


class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt =0
        mx = max(nums)
        mn = min(nums)
        for a in nums:
            if a != mx and a != mn:
                cnt +=1
        return cnt

re =Solution().countElements( nums =[-71,-71,93,-71,40])
print(re)

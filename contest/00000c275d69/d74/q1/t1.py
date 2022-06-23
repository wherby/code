from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left


from collections import Counter


class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = Counter(nums)
        for i,a in cnt.items():
            if a %2 !=0:
                return False
        return True

re = Solution().divideArray([3,2,3,2,2,2])
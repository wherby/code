from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(queries)
        nums.sort()
        ls=[0]
        acc =0
        ret = [0]*n
        for i,a in enumerate(nums):
            acc += a 
            ls.append(acc)
        for i,q in enumerate(queries):
            idx = bisect_right(ls,q)
            ret[i] = idx-1
        return ret




re =Solution().answerQueries(nums = [2,3,4,5], queries = [1])
print(re)